# master_data changelog: 2026_10_30_18_23_29 → 2026_11_03_00_00_00

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

- [`170001`](weapons.json#L278291) マナガルム.ALICE
  - base_name: マナガルム.ALICE (costume: 魔装)
  - element=風(3) / type=投擲(9) / rarity=SS(4) / cv=加隈亜衣
  - max stats: HP=15560 / ATK=20860 / DEF=6770 / SPD=43 / BREAK=2940
  - hit_counts=[2, 4, 8] (3段)  motion_speed=[1.6/1.6/1.1]  mp=888
  - three_size=64/52/67 / initial_slot=3
  - BD: MOON-SNATCHER《Dormouse》 (arts_id=700)
    - description: 敵全体に超強力な66連ダメージ＆自分HP完全回復
    - cost=6 / hit_count=66 / value=2.2 / additional_value=0.0
  - innate skills (6):
    - Vitality_Speed Multiply ×3.0 — 味方全体が、残HPが多いほどスピード超絶大にアップ（最大3倍）
    - RemHP_Speed Multiply ×0.1 — 味方全体が、残HPが少ないほどスピード超絶大にダウン（最大0.1倍）
    - Vitality_Attack Multiply ×12.9286 — 残HPが多いほど自身の攻撃力がアップ(最大13倍)【熟度UPにつれてさらに効果値がUP（最大20倍）】
    - DamageLimitBreak Addition +8000000000.0 — 自身のダメージ上限が80億アップ
    - Heal Addition +300.0 — 非行動時に自身のHPが徐々に回復
    - AnyElement Multiply ×1.0 — 闇属性を対象とした他魔剣からのスキル効果を受けられる
- [`170002`](weapons.json#L278524) マナガルム.ALICE【極】
  - base_name: マナガルム.ALICE (costume: 極魔装)
  - element=風(3) / type=投擲(9) / rarity=SS(4) / cv=加隈亜衣
  - max stats: HP=20220 / ATK=27110 / DEF=8800 / SPD=43 / BREAK=3820
  - hit_counts=[3, 4, 11] (3段)  motion_speed=[1.6/1.6/1.1]  mp=888
  - three_size=64/52/67 / initial_slot=4
  - BD: MOON-SNATCHER《Dormouse》 (arts_id=700)
    - description: 敵全体に超強力な66連ダメージ＆自分HP完全回復
    - cost=6 / hit_count=66 / value=2.2 / additional_value=0.0
  - innate skills (6):
    - Vitality_Speed Multiply ×3.0 — 味方全体が、残HPが多いほどスピード超絶大にアップ（最大3倍）
    - RemHP_Speed Multiply ×0.1 — 味方全体が、残HPが少ないほどスピード超絶大にダウン（最大0.1倍）
    - Vitality_Attack Multiply ×12.9286 — 残HPが多いほど自身の攻撃力がアップ(最大13倍)【熟度UPにつれてさらに効果値がUP（最大20倍）】
    - DamageLimitBreak Addition +8000000000.0 — 自身のダメージ上限が80億アップ
    - Heal Addition +300.0 — 非行動時に自身のHPが徐々に回復
    - AnyElement Multiply ×1.0 — 闇属性を対象とした他魔剣からのスキル効果を受けられる

## materials

### 新增 (1)

- [`52140104`](materials.json#L20779) ねずのばん rarity=5
  - 報酬は添い寝でおねがいしまーす。[上限値:普]
[同装備ｾｯﾄ風が残HP多いほど攻撃力UP]

## items

### 新增 (2)

- [`15363`](items.json#L33589) グリーンスタージュエル
  - 膨大な魔力から偶然精製された
稀少鉱石。ダイヤに似た別物。
- [`3010163`](items.json#L166603) ﾏﾅｶﾞﾙﾑ.ALICE熟度15製造チケット
  - マナガルム.ALICEを熟度15で確実に製造できる術符。

## evolution_recipes

### 新增 (1)

- `170001`

## attack_motions

### 新增 (1)

- [`835`](attack_motions.json#L3335) 眠鼠

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
