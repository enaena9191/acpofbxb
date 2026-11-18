# master_data changelog: 2026_11_17_16_00_00 → 2026_11_18_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 2 | 0 | 0 |
| items | 10 | 0 | 0 |
| evolution_recipes | 2 | 0 | 0 |
| attack_motions | 2 | 0 | 0 |

## weapons

### 新增 (2)

- [`134703`](weapons.json#L142882) リンドヴルム【極弐】
  - base_name: リンドヴルム (costume: 極弐魔装)
  - element=風(3) / type=大鎌(12) / rarity=S(3) / cv=浜崎奈々
  - max stats: HP=17070 / ATK=12680 / DEF=12170 / SPD=22 / BREAK=4230
  - hit_counts=[6, 4, 6] (3段)  motion_speed=[2.6/2.2/1.6]  mp=286
  - three_size=75/55/76 / initial_slot=5
  - BD: フライハイラヴデアリング (arts_id=10347)
    - description: 敵全体に超絶強力な39連ダメージ＆自分HP回復
    - cost=6 / hit_count=39 / value=26.4 / additional_value=0.0
  - innate skills (3):
    - BlazeAttack Multiply ×3.0 — 風属性の魔剣のB.D.攻撃力が絶大にアップ
    - HP Multiply ×1.5 — 風属性の魔剣のHPが大幅にアップ
    - DamageLimitBreak Addition +1600000000.0 — 自身のダメージ上限が16億アップ
- [`158003`](weapons.json#L239575) 戦闘距離拡大戦略【極弐】
  - base_name: 戦闘距離拡大戦略 (costume: 極弐魔装)
  - element=闇(5) / type=投擲(9) / rarity=S(3) / cv=北島瑞月
  - max stats: HP=13340 / ATK=2080 / DEF=15390 / SPD=26 / BREAK=1510
  - hit_counts=[10, 10, 13] (3段)  motion_speed=[2.0/2.0/1.1]  mp=257
  - three_size=69/54/70 / initial_slot=5
  - BD: 究極隔絶★コンプリートディスタンス (arts_id=10580)
    - description: 敵全体に超強力な45連ダメージ＆wave中、防御力20%UP
    - cost=4 / hit_count=45 / value=1.72 / additional_value=0.0
  - innate skills (8):
    - AllTarget Multiply ×1.0 — 攻撃力を下げずに自分の攻撃範囲が敵全体になる
    - Attack Multiply ×1.75 — 闇属性の魔剣の攻撃力が絶大にアップ
    - InstantDeath Repel_Percent ×50.0 — 編成魔剣全体が即死特性の攻撃を確率で回避する
    - BlazeAbsorb Repel_Percent ×50.0 — 編成魔剣全体が勇気分解の発生を確率で回避する
    - Stun Repel_Percent ×50.0 — 編成魔剣全体がスタンの発生を確率で回避する
    - Mez Repel_Percent ×50.0 — 編成魔剣全体が麻痺の発生を確率で回避する
    - RateDamage Repel_Percent ×50.0 — 編成魔剣全体が割合ダメージ攻撃を確率で回避する
    - DamageLimitBreak Addition +500000000.0 — 自身のダメージ上限が5億アップ

## items

### 新增 (10)

- [`134701`](items.json#L146419) 夢幻深層リンドヴルム
  - 古代石版に深く刻み込まれた
リンドヴルムの深層記憶。
- [`134702`](items.json#L146437) リンドヴルムジーン
  - 進化の為の情報が詰め込まれた
リンドヴルムの覚醒術式。
- [`134703`](items.json#L146455) リンドヴルムハート
  - 強き想いから生まれた
リンドヴルムの残留思念。
- [`134704`](items.json#L146473) リンドヴルムコア
  - 魔力結晶に封印された
リンドヴルムのコア。
- [`134705`](items.json#L146491) 特殊設計書リンドヴルム
  - 極弐改造について記された
リンドヴルムの特殊設計書。
- [`158001`](items.json#L151315) 夢幻深層戦闘距離拡大戦略
  - 古代石版に深く刻み込まれた
戦闘距離拡大戦略の深層記憶。
- [`158002`](items.json#L151333) 戦闘距離拡大戦略ジーン
  - 進化の為の情報が詰め込まれた
戦闘距離拡大戦略の覚醒術式。
- [`158003`](items.json#L151351) 戦闘距離拡大戦略ハート
  - 強き想いから生まれた
戦闘距離拡大戦略の残留思念。
- [`158004`](items.json#L151369) 戦闘距離拡大戦略コア
  - 魔力結晶に封印された
戦闘距離拡大戦略のコア。
- [`158005`](items.json#L151387) 特殊設計書戦闘距離拡大戦略
  - 極弐改造について記された
戦闘距離拡大戦略の特殊設計書。

## evolution_recipes

### 新增 (2)

- `134702`
- `158002`

## attack_motions

### 新增 (2)

- [`837`](attack_motions.json#L3339) 隔絶2
- [`838`](attack_motions.json#L3343) 祈斬2

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
