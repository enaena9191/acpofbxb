# master_data changelog: 2026_11_06_16_00_00 → 2026_11_10_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 2 | 0 | 0 |
| weapon_costumes | 1 | 0 | 0 |
| materials | 3 | 0 | 0 |
| items | 3 | 0 | 0 |
| evolution_recipes | 1 | 0 | 0 |
| attack_motions | 1 | 0 | 0 |

## weapons

### 新增 (2)

- [`169801`](weapons.json#L278291) ハジマリ
  - base_name: ハジマリ (costume: 魔装)
  - element=無(6) / type=投擲(9) / rarity=SS(4) / cv=春咲暖
  - max stats: HP=11540 / ATK=12830 / DEF=10000 / SPD=42 / BREAK=2600
  - hit_counts=[7, 6, 10] (3段)  motion_speed=[1.8/1.8/1.1]  mp=13
  - three_size=66/55/70 / initial_slot=3
  - BD: 疑似解錠･ラストジェネレイト (arts_id=698)
    - description: 敵全体に超強力な84連ダメージ＆48秒間400ずつ味方HP回復
    - cost=7 / hit_count=84 / value=1.99 / additional_value=0.0
  - innate skills (4):
    - Attack Multiply ×2.969 — 無属性の味方全体が攻撃力3倍【熟度UPにつれてさらに効果値UP（最大6倍）】
    - DamageLimitBreak Addition +2500000000.0 — 無属性の魔剣のダメージ上限が25億アップ
    - SapphireDrop Multiply ×2.0 — 無属性の魔剣の獲得するサファイアの量がかなり増加
    - MotionSpeed Multiply ×3.0 — 自身のモーション速度が3倍に加速
- [`169802`](weapons.json#L278486) ハジマリ【極】
  - base_name: ハジマリ (costume: 極魔装)
  - element=無(6) / type=投擲(9) / rarity=SS(4) / cv=春咲暖
  - max stats: HP=15000 / ATK=16670 / DEF=13000 / SPD=42 / BREAK=3370
  - hit_counts=[8, 6, 13] (3段)  motion_speed=[1.8/1.8/1.1]  mp=13
  - three_size=66/55/70 / initial_slot=4
  - BD: 疑似解錠･ラストジェネレイト (arts_id=698)
    - description: 敵全体に超強力な84連ダメージ＆48秒間400ずつ味方HP回復
    - cost=7 / hit_count=84 / value=1.99 / additional_value=0.0
  - innate skills (4):
    - Attack Multiply ×2.969 — 無属性の味方全体が攻撃力3倍【熟度UPにつれてさらに効果値UP（最大6倍）】
    - DamageLimitBreak Addition +2500000000.0 — 無属性の魔剣のダメージ上限が25億アップ
    - SapphireDrop Multiply ×3.0 — 無属性の魔剣の獲得するサファイアの量が大幅に増加
    - MotionSpeed Multiply ×3.0 — 自身のモーション速度が3倍に加速

## weapon_costumes

### 新增 (1)

- [`1180050`](weapon_costumes.json#L7451) 魔装《魔法少女》
  - 归属武器: 魔劍グラム=オルタ (weapon_base_id=1180)
  - effects: Attack Multiply ×1.13, Defense Multiply ×0.95

## materials

### 新增 (3)

- [`26010067`](materials.json#L9201) 絶魔神の喝采Lv2 rarity=2
  - 結晶化した魔剣の記憶。[無のみ]
[ｻﾌｧｲｱ量がUP][上限値:超絶高]
- [`36010068`](materials.json#L12071) 絶魔神の喝采Lv3 rarity=3
  - 結晶化した魔剣の記憶。[無のみ]
[ｻﾌｧｲｱ量がUP][上限値:超絶高]
- [`53020303`](materials.json#L22039) ハジマリの少女 rarity=5
  - 始まりも終わりもボクが見届けるよ。
[同装備ｾｯﾄ無のﾓｰｼｮﾝ速度がUP][上限値:普]

## items

### 新增 (3)

- [`15365`](items.json#L33607) 【裏式】スタージュエル
  - 膨大な魔力から偶然精製された
稀少鉱石。ダイヤに似た別物。
- [`40853`](items.json#L129097) 【期間限定】裏式･超強化の鍵
  - 11月27日16時までショップで特定魔剣の熟度をあげられる鍵。
- [`1180050`](items.json#L154297) 魔劍グラム=オルタの変身衣装
  - 魔劍グラム=オルタの新たな力を
引き出すことができる魔術礼装。

## evolution_recipes

### 新增 (1)

- `169801`

## attack_motions

### 新增 (1)

- [`839`](attack_motions.json#L3339) 起源

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
