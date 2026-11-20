# master_data changelog: 2026_11_19_17_32_43 → 2026_11_20_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| items | 1 | 0 | 0 |
| jobs | 1 | 0 | 0 |

## items

### 新增 (1)

- [`1198022`](items.json#L155059) ヤグルシの花嫁衣装
  - ヤグルシの新たな力を
引き出すことができる魔術礼装。

## jobs

### 新增 (1)

- [`1579`](jobs.json#L202251) サウザンド【大罪】 rarity=5
  - rarity=5 / max_level=50
  - job_abilities (18):
    - WeaponType 長剣(1): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 大剣(2): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 太刀(3): pos=1.4 / neg=1.06 (rank=a 得意)
    - WeaponType 杖棒(4): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 弓矢(5): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 連弩(6): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 戦斧(7): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 騎槍(8): pos=1.9 / neg=1.135 (rank=splus 超得意)
    - WeaponType 投擲(9): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 拳闘(10): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 魔典(11): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 大鎌(12): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 火(1): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 水(2): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 風(3): pos=1.9 / neg=1.135 (rank=splus 超得意)
    - Element 光(4): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 闇(5): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 無(6): pos=0.3 / neg=0.3 (rank=d 超苦手)
  - job_skills (10):
    - WeaponArtsHitCount Addition +7.0 — 大きな罪を背負う者の証。自分のB.D.ヒット数+7
    - Attack Multiply ×1.66 — 風装備で攻撃力とモーション速度が66％UP
    - HitCount Addition +0.0 — 騎槍装備で攻撃ヒット数それぞれ+3
    - GuardBreak Multiply ×0.33 — ブレイク力67%DOWNを代償に、サファイア66%UPとダメージ上限6億UP
    - Speed Multiply ×0.33 — スピード67%DOWNを代償に、残HPが多いほど攻撃力UP（最大111%）
    - HP Multiply ×0.5 — 力に耐えきれずHP50%DOWN
    - MotionSpeed Multiply ×1.66 — 風装備でモーション速度が66％UP
    - SapphireDrop Multiply ×1.66 — サファイア66%UP
    - DamageLimitBreak Addition +600000000.0 — ダメージ上限6億UP
    - Vitality_Attack Multiply ×2.11 — 残HPが多いほど攻撃力UP(最大111%)

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
