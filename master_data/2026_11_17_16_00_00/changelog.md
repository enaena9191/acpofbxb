# master_data changelog: 2026_11_15_16_00_00 → 2026_11_17_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 2 | 0 | 0 |
| materials | 1 | 0 | 0 |
| items | 2 | 0 | 0 |
| evolution_recipes | 1 | 0 | 0 |
| attack_motions | 1 | 0 | 0 |

## weapons

### 新增 (2)

- [`170201`](weapons.json#L279565) 霊獣刀タマモノマエ=ハクビ
  - base_name: 霊獣刀タマモノマエ=ハクビ (costume: 魔装)
  - element=水(2) / type=太刀(3) / rarity=SS(4) / cv=七瀬つむぎ
  - max stats: HP=15380 / ATK=23610 / DEF=7690 / SPD=39 / BREAK=2370
  - hit_counts=[1, 2, 6] (3段)  motion_speed=[1.8/1.6/1.2]  mp=999
  - three_size=80/55/82 / initial_slot=3
  - BD: 白面九尾玉藻ノ神刃 (arts_id=702)
    - description: 【超瞬速B.D.】敵全体に超絶強力な89連ダメージ＆9秒間自身のスピードが9倍
    - cost=5 / hit_count=89 / value=18.0 / additional_value=0.0
  - innate skills (4):
    - Blaze_DamageLimitBreak Addition +8900000000.0 — 自身のB.D.ダメージ上限が89億アップ
    - BlazeAttack Multiply ×3.0 — 水属性の魔剣のB.D.攻撃力が絶大にアップ
    - MotionSpeed Multiply ×2.0 — 水属性の魔剣の攻撃モーションが大幅に加速
    - AnyElement Multiply ×1.0 — 火属性を対象とした他魔剣からのスキル効果を受けられる
- [`170202`](weapons.json#L279760) 霊獣刀タマモノマエ=ハクビ【極】
  - base_name: 霊獣刀タマモノマエ=ハクビ (costume: 極魔装)
  - element=水(2) / type=太刀(3) / rarity=SS(4) / cv=七瀬つむぎ
  - max stats: HP=19990 / ATK=30690 / DEF=9990 / SPD=39 / BREAK=3070
  - hit_counts=[2, 2, 9] (3段)  motion_speed=[1.8/1.6/1.2]  mp=999
  - three_size=80/55/82 / initial_slot=4
  - BD: 白面九尾玉藻ノ神刃 (arts_id=702)
    - description: 【超瞬速B.D.】敵全体に超絶強力な89連ダメージ＆9秒間自身のスピードが9倍
    - cost=5 / hit_count=89 / value=18.0 / additional_value=0.0
  - innate skills (4):
    - Blaze_DamageLimitBreak Addition +8900000000.0 — 自身のB.D.ダメージ上限が89億アップ
    - BlazeAttack Multiply ×3.4847 — 水属性の魔剣のB.D.攻撃力が超絶大にアップ【熟度UPにつれてさらに効果値UP】
    - MotionSpeed Multiply ×2.325 — 水属性の魔剣の攻撃モーションが絶大に加速【熟度UPにつれてさらに効果値UP】
    - AnyElement Multiply ×1.0 — 火属性を対象とした他魔剣からのスキル効果を受けられる

## materials

### 新增 (1)

- [`53010228`](materials.json#L21465) キツネのおさそい rarity=5
  - 一緒に既成事実、つくりませんか？
[太刀のみ][スピードがUP][上限値:超絶高]

## items

### 新增 (2)

- [`15366`](items.json#L33607) ダークスタージュエル
  - 膨大な魔力から偶然精製された
稀少鉱石。ダイヤに似た別物。
- [`40854`](items.json#L129097) 【期間限定】真式･超強化の鍵γ
  - 12月4日16時までショップで特定魔剣の熟度をあげられる鍵。

## evolution_recipes

### 新增 (1)

- `170201`

## attack_motions

### 新增 (1)

- [`840`](attack_motions.json#L3343) 白眉

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
