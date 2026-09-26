"""sync_icons.py — 新实体的图标源 (CDN 下 .dat 解出 PNG 到 `<assets>` 布局目录)。

manifest 驱动: 扫 manifest 里图标类资源 (weapon-stand-s / weapon-damage-s / materia-icon /
picture-m / picture-ll / npc-stand-m),推出 copy_images 会产的 icon 路径,对 icons 清单里**缺失**的
下载 + extract 到 out_dir。清单 = 下游每轮发布的现有 icons 列表 (`<cat>/<stem>.png` 一行一个);
out_dir 由 workflow 传 R2、下游取走。
失败/无依赖优雅降级、不阻塞数据更新。重绘 (同 id 换图) 不覆盖、属罕见、本地强刷。
"""
import re
import tempfile
from pathlib import Path


def _asset_to_icon(name: str):
    """asset name → (category 子目录, icon 文件名 stem) 或 None。对应 copy_images 的源→目标。"""
    m = re.match(r"^weapon-stand-s-(\d+)$", name)
    if m:
        i = m.group(1)
        return ("chara", i) if len(i) == 6 else ("masou", i) if len(i) == 7 else None
    m = re.match(r"^weapon-damage-s-(\d{7})$", name)
    if m:
        return ("masou_damage", m.group(1))
    m = re.match(r"^materia-icon-(\d+)$", name)
    if m:
        return ("crystal", m.group(1))
    m = re.match(r"^picture-m-(\d+)$", name)
    if m:
        return ("bg", m.group(1))
    m = re.match(r"^npc-stand-m-(\d+)$", name)
    if m:
        return ("soul", m.group(1))
    return None


def sync(manifest: dict, index_path, out_dir) -> dict:
    """返回 {downloaded, extracted, failed, skipped}。"""
    index_path, out_dir = Path(index_path), Path(out_dir)
    if not index_path.is_file():
        print(f"  sync_icons 跳过: 无 icons 清单 {index_path} (缺清单会当成全缺、不下)")
        return {"downloaded": 0, "extracted": 0, "failed": 0, "skipped": True}
    have = set(index_path.read_text(encoding="utf-8").split())
    idx = {f["name"]: f for f in manifest.get("files", [])}

    # 1. 找缺失的 icon → 需要的 asset
    needed = {}  # asset_name -> entry
    for name, ent in idx.items():
        hit = _asset_to_icon(name)
        if not hit:
            continue
        cat, stem = hit
        if f"{cat}/{stem}.png" not in have:
            needed[name] = ent
            # bg 还要 picture-ll 兜底
            if cat == "bg":
                ll = f"picture-ll-{stem}"
                if ll in idx:
                    needed[ll] = idx[ll]

    if not needed:
        return {"downloaded": 0, "extracted": 0, "failed": 0, "skipped": False}

    try:
        import cdn
        import extract_assets
    except ImportError as e:
        print(f"  sync_icons 降级 (缺依赖 {e})、缺 {len(needed)} 个 icon 源未下")
        return {"downloaded": 0, "extracted": 0, "failed": len(needed), "skipped": True}

    dat_dir = Path(tempfile.mkdtemp(prefix="bxb_dat_"))  # .dat 不进 out_dir (out_dir 整个传 R2)
    out_dir.mkdir(parents=True, exist_ok=True)
    dl = ex = failed = 0
    for name, ent in needed.items():
        dat = dat_dir / f"{name}.dat"
        if not cdn.download_dat(name, ent["version"], dat, ent.get("md5")):
            failed += 1; continue
        dl += 1
        try:
            written = extract_assets.extract_png(dat, name, out_dir)
            ex += len(written)
        except Exception:
            failed += 1
        # 不 unlink: UnityPy 在 Windows 占着 .dat (WinError 32);temp 整目录最后丢弃

    print(f"  icons: 需 {len(needed)} 源 → 下载 {dl} extract {ex} 张 → {out_dir} (失败 {failed})")
    return {"downloaded": dl, "extracted": ex, "failed": failed, "skipped": False}
