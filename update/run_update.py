"""run_update.py — 游戏侧数据更新编排 (纯 HTTP API, 免模拟器/ADB)。

模块:
  npc-motion 预取 : asset manifest + 增量 _npc_motions.json
  D. master_data  : login → get_master_data → archive (split+派生) → mt/master_data/<date>/ + changelog + 索引
  C. asset_version: 快照归档 → mt/asset_version/<ver>/;缺失的图标源 → BXB_ASSETS_OUT
  Scenario        : utage3_scenario_version 变化 → mt/scenario/

结果都落在本地目录,workflow 再经 r2_state.py 传回 R2。
致命失败 (login / master_data / asset_version manifest) → 直接非零退出、workflow 失败。
其余优雅降级:icons / npc-motion 预取 / scenario 失败不阻塞快照产出。

env:
  BXB_UNIQUE_KEY / BXB_BOOTSTRAP_KEY   API 凭据 (必需)
  BXB_MASTER_TABLES                    master_tables 基准根 (默认 ./mt)
  BXB_NPC_MOTIONS                      _npc_motions.json 基线 (默认 ./wiki/_npc_motions.json)
  BXB_ICONS_INDEX                      现有 icons 清单 (默认 ./wiki/icons_index.txt)
  BXB_ASSETS_OUT                       新图标源输出目录 (默认 ./assets_out)

输出: $RUNNER_TEMP/ci_update_summary.json
"""
import json
import os
import sys
import tempfile
from pathlib import Path

UPDATE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = UPDATE_DIR.parent
sys.path.insert(0, str(UPDATE_DIR))
sys.path.insert(0, str(PROJECT_ROOT))   # import scripts.api_client (workflow 从 R2 routines/ 取进 scripts/)

import scripts.api_client as api_client  # noqa: E402
import master_tables_archive as mta  # noqa: E402
import cdn  # noqa: E402
import sync_icons  # noqa: E402
import sync_npc_motions  # noqa: E402
import sync_scenario  # noqa: E402

NPC_MOTIONS = Path(os.environ.get("BXB_NPC_MOTIONS") or PROJECT_ROOT / "wiki" / "_npc_motions.json")
ICONS_INDEX = Path(os.environ.get("BXB_ICONS_INDEX") or PROJECT_ROOT / "wiki" / "icons_index.txt")
ASSETS_OUT = Path(os.environ.get("BXB_ASSETS_OUT") or PROJECT_ROOT / "assets_out")


def prefetch_npc_motions():
    print("== 预取: asset manifest + npc-motion ==")
    try:
        manifest = cdn.get_manifest()
        print(f"  asset_version = {manifest.get('version')} | files = {len(manifest.get('files', []))}")
        nm = sync_npc_motions.sync(manifest, NPC_MOTIONS)
        return manifest, {"npc_motions_added": len(nm.get("added", []))}
    except Exception as e:
        print(f"  npc-motion 预取失败 (降级、module C 再重抓 manifest): {type(e).__name__}: {e}")
        return None, {"npc_motions_added": 0, "npc_motions_prefetch_error": str(e)}


def module_d(session) -> dict:
    print("== 模块 D: master_data 快照 + changelog ==")
    master = session.get_master_data()
    mdv = master.get("master_data_version")
    print(f"  master_data_version = {mdv}")
    root = mta.master_tables_root()
    status, folder = mta.archive_master_data(master, root)
    print(f"  归档: {status} → {folder.name}  (root={root})")
    return {"snapshot_status": status, "master_data_version": mdv, "snapshot_folder": str(folder)}


def module_c(manifest) -> dict:
    print("== 模块 C: asset-version 归档 + 图标源 ==")
    if manifest is None:
        manifest = cdn.get_manifest()  # 失败 raise → 致命
        print(f"  asset_version = {manifest.get('version')} | files = {len(manifest.get('files', []))}")
    root = mta.master_tables_root()
    av_status, av_folder, _ = mta.archive_asset_version(manifest, root)
    print(f"  asset_version 归档: {av_status} → {av_folder.name}")
    try:
        ic = sync_icons.sync(manifest, ICONS_INDEX, ASSETS_OUT)
        icons_ex = ic.get("extracted", 0)
    except Exception as e:
        print(f"  图标源下载失败 (降级、不阻塞 asset_version): {type(e).__name__}: {e}")
        icons_ex = 0
    return {
        "asset_version": manifest.get("version"),
        "asset_version_status": av_status,
        "icons_extracted": icons_ex,
    }


def module_scenario(session) -> dict:
    print("== 模块 Scenario: utage3_scenario_version → unity3d + TSV ==")
    ver = session.login_resp.get("utage3_scenario_version")
    if not ver:
        print("  login 响应无 utage3_scenario_version、跳过")
        return {"scenario_status": "none", "scenario_version": None}
    root = mta.master_tables_root()
    res = sync_scenario.sync(ver, root)
    if res["status"] == "archived":
        tail = (f" ({res['size']:,} bytes, {res.get('tsv', 0)} TSV; "
                f"新增 {len(res.get('added', []))} / 修改 {len(res.get('modified', []))} 本)")
    elif res.get("error"):
        tail = f" — {res['error']}"
    else:
        tail = ""
    print(f"  scenario {ver}: {res['status']}{tail}")
    return {"scenario_status": res["status"], "scenario_version": ver,
            "scenario_added": res.get("added", []), "scenario_modified": res.get("modified", [])}


def _warp_pool():
    pool_dir = os.environ.get("BXB_WARP_POOL_DIR")
    if not pool_dir or not os.path.isdir(pool_dir):
        return None, None
    try:
        import warp_pool  # workflow 从 R2 routines/daily/warp_pool.py 取到 update/
    except ImportError:
        return None, None
    if not any(f.endswith(".conf") for f in os.listdir(pool_dir)):
        return None, None
    pool = warp_pool.WarpPool(pool_dir, os.environ.get("BXB_WIREPROXY_BIN", "bin/wireproxy"),
                              os.environ.get("BXB_WARP_BURNED", "warp_burned.txt"))
    return warp_pool, pool


class _ApiSession:
    def __init__(self, sid, skey, home):
        self.session_id, self.key, self.login_resp = sid, skey, home

    def get_master_data(self) -> dict:
        d, st = api_client.get("/master_data", self.session_id, self.key)
        if not isinstance(d, dict) or not d.get("master_data_version"):
            keys = list(d)[:6] if isinstance(d, dict) else type(d).__name__
            raise RuntimeError(f"/master_data 未正确返回 (status={st}, keys={keys})")
        return d


def _connect() -> _ApiSession:
    uk = os.environ.get("BXB_UNIQUE_KEY")
    if not uk:
        raise SystemExit("缺 BXB_UNIQUE_KEY (GitHub Actions secret)")
    sid, skey, _name = api_client.login(uk, platform=2)
    home, st = api_client.get("/my/data?home=1", sid, skey)
    if not isinstance(home, dict) or home.get("error_reason"):
        et = home.get("error_type") if isinstance(home, dict) else home
        raise RuntimeError(f"GetHomeMyData 失败 (status={st}, {et})")
    return _ApiSession(sid, skey, home)


def main():
    wp, pool = _warp_pool()
    # login+home 是首个且致命的游戏 API;直连出口被封 → 切 WARP 重试(成功后 env 代理留存、master_data 同走 WARP)
    session = wp.with_warp_retry(pool, _connect, log=print) if pool else _connect()
    print(f"login ok: id={session.login_resp.get('id')} name={session.login_resp.get('name')!r}\n")

    manifest, summary = prefetch_npc_motions()
    summary.update(module_d(session))
    summary.update(module_c(manifest))  # asset_version 失败 → 致命
    summary.update(module_scenario(session))  # 降级、不致命

    if pool:
        pool.stop()
    out = Path(os.environ.get("RUNNER_TEMP", tempfile.gettempdir())) / "ci_update_summary.json"
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n== 完成 ==")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    print(f"  summary → {out}")


if __name__ == "__main__":
    main()
