"""r2_state.py — master_tables 基准 / 交接文件 与 R2 的同步。

R2 布局 (bucket = env R2_DATA_BUCKET, 前缀 R2_DATA_PREFIX 默认 pipeline):
  <p>/mt/                  master_tables 基准 (每个文件都是归档的原样副本)。
                           裁剪: master_data / asset_version 只保留最新 KEEP_FULL 个完整目录,更早的只留
                           changelog.md + _meta.json (索引重建要读);scenario/unity3d 只留最新一个 (判 unchanged 用)。
  <p>/wiki/_npc_motions.json   下游发布的基线,本侧只追加新 key 后传回
  <p>/wiki/icons_index.txt     下游发布的现有 icons 清单 (只读)
  <p>/wiki/assets/             本侧解出的新图标源 (`<assets>` 布局),下游取走后删

用法 (cwd = 仓库根):
  python update/r2_state.py pull   # R2 → mt/ + wiki/,记录 md5 到 .r2_state.json
  python update/r2_state.py push   # 裁剪 mt/ → 按 md5 差异上传/删除;_npc_motions.json 变了才传;assets_out/ 全传
"""
import hashlib
import json
import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3
from botocore.exceptions import ClientError

ROOT = Path.cwd()
MT = ROOT / "mt"
WIKI = ROOT / "wiki"
ASSETS_OUT = ROOT / "assets_out"
STATE = ROOT / ".r2_state.json"
BUCKET = os.environ.get("R2_DATA_BUCKET", "")
PREFIX = os.environ.get("R2_DATA_PREFIX", "pipeline").strip("/")
KEEP_FULL = 2
STUB_KEEP = ("changelog.md", "_meta.json")
WIKI_FILES = ("_npc_motions.json", "icons_index.txt")


def _client():
    return boto3.client(
        "s3",
        endpoint_url=os.environ["R2_ENDPOINT"],
        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
        region_name="auto",
    )


def _md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _files(d: Path) -> dict:
    if not d.is_dir():
        return {}
    return {p.relative_to(d).as_posix(): p for p in d.rglob("*") if p.is_file()}


def _keys(s3, prefix: str):
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
        for o in page.get("Contents", []):
            yield o["Key"]


def _pmap(fn, items):
    with ThreadPoolExecutor(16) as ex:
        return list(ex.map(fn, items))


def pull():
    s3 = _client()
    base = f"{PREFIX}/mt/"
    keys = [k for k in _keys(s3, base) if not k.endswith("/")]
    if not keys:
        raise SystemExit(f"R2 {BUCKET}/{base} 为空 —— 基准未初始化、中止 (不能在空基准上跑)")

    def dl(k):
        dst = MT / k[len(base):]
        dst.parent.mkdir(parents=True, exist_ok=True)
        s3.download_file(BUCKET, k, str(dst))

    _pmap(dl, keys)
    WIKI.mkdir(exist_ok=True)
    for name in WIKI_FILES:
        try:
            s3.download_file(BUCKET, f"{PREFIX}/wiki/{name}", str(WIKI / name))
        except ClientError:
            print(f"  R2 无 {PREFIX}/wiki/{name}")
    state = {
        "mt": {rel: _md5(p) for rel, p in _files(MT).items()},
        "wiki": {n: _md5(WIKI / n) for n in WIKI_FILES if (WIKI / n).is_file()},
    }
    STATE.write_text(json.dumps(state), encoding="utf-8")
    print(f"pull: mt {len(keys)} 个文件、wiki {sorted(state['wiki'])}")


def _stub(folder: Path):
    for f in folder.iterdir():
        if f.name in STUB_KEEP:
            continue
        shutil.rmtree(f) if f.is_dir() else f.unlink()


def prune():
    md = MT / "master_data"
    if md.is_dir():
        folders = sorted(p for p in md.iterdir() if p.is_dir() and p.name.replace("_", "").isdigit())
        for d in folders[:-KEEP_FULL]:
            _stub(d)
    av = MT / "asset_version"
    if av.is_dir():
        folders = sorted((p for p in av.iterdir() if p.is_dir() and p.name.isdigit()), key=lambda p: int(p.name))
        for d in folders[:-KEEP_FULL]:
            _stub(d)
    u3d = MT / "scenario" / "unity3d"
    if u3d.is_dir():
        vers = sorted(u3d.glob("scenario-*.unity3d"), key=lambda p: int(p.stem.split("-")[1]))
        for f in vers[:-1]:
            f.unlink()


def push():
    if not STATE.is_file():
        raise SystemExit("无 .r2_state.json (没 pull 过) —— 中止、避免误删 R2 基准")
    state = json.loads(STATE.read_text(encoding="utf-8"))
    prune()
    s3 = _client()

    old = state["mt"]
    cur = _files(MT)
    if not cur:
        raise SystemExit("mt/ 为空 —— 中止")
    up = [rel for rel, p in cur.items() if old.get(rel) != _md5(p)]
    rm = [rel for rel in old if rel not in cur]
    if len(rm) > max(200, len(old) // 4):
        raise SystemExit(f"要删 {len(rm)} / {len(old)} 个 R2 基准文件、超出预期 —— 中止")

    _pmap(lambda rel: s3.upload_file(str(cur[rel]), BUCKET, f"{PREFIX}/mt/{rel}"), up)
    for i in range(0, len(rm), 1000):
        s3.delete_objects(Bucket=BUCKET, Delete={"Objects": [{"Key": f"{PREFIX}/mt/{r}"} for r in rm[i:i + 1000]]})
    print(f"push mt: 上传 {len(up)}、删除 {len(rm)}")
    for rel in sorted(up)[:40]:
        print(f"  + {rel}")

    npc = WIKI / "_npc_motions.json"
    if npc.is_file() and state["wiki"].get(npc.name) != _md5(npc):
        s3.upload_file(str(npc), BUCKET, f"{PREFIX}/wiki/{npc.name}")
        print("push wiki/_npc_motions.json")

    assets = _files(ASSETS_OUT)
    _pmap(lambda rel: s3.upload_file(str(assets[rel]), BUCKET, f"{PREFIX}/wiki/assets/{rel}"), list(assets))
    if assets:
        print(f"push wiki/assets: {len(assets)} 个图标源")


if __name__ == "__main__":
    if not BUCKET:
        raise SystemExit("缺 env R2_DATA_BUCKET")
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "pull":
        pull()
    elif cmd == "push":
        push()
    else:
        raise SystemExit("用法: python update/r2_state.py pull|push")
