# master_data changelog: 2026_09_29_16_00_00 → 2026_09_30_15_54_30

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 0 | 0 | 3 |
| materials | 0 | 0 | 1 |
| pictures | 0 | 0 | 1 |

## weapons

### 调整 (3)

- [`113301`](weapons.json#L54905) メルキュルボーラ
  - base_name: メルキュルボーラ (costume: 魔装)
  - element=水(2) / type=投擲(9) / rarity=AA(2) / cv=諏訪彩花
  - max stats: HP=6200 / ATK=1200 / DEF=4100 / SPD=26 / BREAK=1400
  - hit_counts=[3, 6, 2] (3段)  motion_speed=[4.0/4.0/1.0]  mp=84
  - three_size=87/58/86 / initial_slot=2
  - BD: マイリトルサタン (arts_id=133)
    - description: 敵全体に強力な16連ダメージ
    - cost=2 / hit_count=16 / value=1.92188 / additional_value=0.0
  - innate skills (1):
    - Attack Multiply ×1.1 — 水属性の魔剣の攻撃力がアップ
- [`113302`](weapons.json#L55030) メルキュルボーラ【極】
  - base_name: メルキュルボーラ (costume: 極魔装)
  - element=水(2) / type=投擲(9) / rarity=AA(2) / cv=諏訪彩花
  - max stats: HP=8100 / ATK=1560 / DEF=5400 / SPD=26 / BREAK=1820
  - hit_counts=[4, 6, 5] (3段)  motion_speed=[4.0/4.0/1.0]  mp=84
  - three_size=87/58/86 / initial_slot=2
  - BD: マイリトルサタン (arts_id=133)
    - description: 敵全体に強力な16連ダメージ
    - cost=2 / hit_count=16 / value=1.92188 / additional_value=0.0
  - innate skills (1):
    - Attack Multiply ×1.1 — 水属性の魔剣の攻撃力がアップ
- [`113303`](weapons.json#L55155) メルキュルボーラ【極弐】
  - base_name: メルキュルボーラ (costume: 極弐魔装)
  - element=水(2) / type=投擲(9) / rarity=AA(2) / cv=諏訪彩花
  - max stats: HP=10100 / ATK=1900 / DEF=7800 / SPD=28 / BREAK=2230
  - hit_counts=[5, 7, 5] (3段)  motion_speed=[3.0/3.0/1.2]  mp=90
  - three_size=87/58/86 / initial_slot=3
  - BD: ディアプリティサタン (arts_id=10133)
    - description: 敵全体に強力な16連ダメージ＆数秒間サファイア1.5倍
    - cost=2 / hit_count=16 / value=1.92188 / additional_value=0.0
  - innate skills (1):
    - Attack Multiply ×1.5 — 水属性の魔剣の攻撃力が大幅にアップ

## materials

### 调整 (1,按 id 聚合)

- [`53060010`](materials.json#L22109) ごーすとばすたー？ rarity=5
  - `description`: `あたし、ふつうの掃除屋ですよぉ…。[光太刀のみ][残HPが多いほどスピードUP][上限値:超高]` → `あたし、ふつうの掃除屋ですよぉ…。[光太刀]
[残HPが多いほどスピードUP][上限値:超高]`

## pictures

### 调整 (1,按字段聚合)

#### `picture_skills` (1 个)
**子项调整** (2 次):
- id=`401901`:
  - description: [IMTロール=サンタ=ピュアのみ]サファイア量が30%UP → [IMTﾛｰﾙ=ｻﾝﾀ=ﾋﾟｭｱのみ]サファイア量が30%UP
  - 影响 1 个 id: [[`4019`](pictures.json#L7878)]
- id=`401902`:
  - description: [IMTロール=サンタ=ピュアのみ]モーション速度が30%UP → [IMTﾛｰﾙ=ｻﾝﾀ=ﾋﾟｭｱのみ]モーション速度が30%UP
  - 影响 1 个 id: [[`4019`](pictures.json#L7878)]

#### `skill_descriptions` (1 个)
- `["[IMTロール=サンタ=ピュアのみ]サファイア量が30%UP", "[IMTロール=サンタ=ピュアのみ]モーション速度が30%UP"]` → `["[IMTﾛｰﾙ=ｻﾝﾀ=ﾋﾟｭｱのみ]サファイア量が30%UP", "[IMTﾛｰﾙ=ｻﾝﾀ=ﾋﾟｭｱのみ]モーション速度が30%UP"]`: ids = [[`4019`](pictures.json#L7878)]

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
