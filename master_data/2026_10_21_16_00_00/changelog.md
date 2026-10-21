# master_data changelog: 2026_10_20_16_00_00 → 2026_10_21_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 2 | 0 | 0 |
| items | 10 | 0 | 0 |
| evolution_recipes | 2 | 0 | 0 |
| attack_motions | 2 | 0 | 0 |

## weapons

### 新增 (2)

- [`130603`](weapons.json#L131519) 不知火検校【極弐】
  - base_name: 不知火検校 (costume: 極弐魔装)
  - element=闇(5) / type=投擲(9) / rarity=S(3) / cv=石原夏織
  - max stats: HP=15550 / ATK=12680 / DEF=7780 / SPD=33 / BREAK=2120
  - hit_counts=[4, 5, 8] (3段)  motion_speed=[2.6/2.6/1.2]  mp=165
  - three_size=75/55/76 / initial_slot=3
  - BD: 夜竜と揺蕩う血月骸宴 (arts_id=10306)
    - description: 敵全体に超強力な33連ダメージ＆一瞬だけ攻撃力2倍
    - cost=6 / hit_count=33 / value=3.5 / additional_value=0.0
  - innate skills (4):
    - GuardBreak Multiply ×1.75 — 闇属性の魔剣が絶大にガードブレイクしやすく
    - Attack Multiply ×1.5 — 闇属性の魔剣の攻撃力が大幅にアップ
    - Enemy_BreakAttack Multiply ×3.0 — ブレイク時に闇属性の魔剣の攻撃力が3倍
    - EventDropRate Multiply ×2.0 — マスターと夜こっそり抜け出して秘密の隠れ場所を見つけたことで「セポネの散歩だより」の取得数が上がる。
- [`131703`](weapons.json#L135594) ヴァジュラ【極弐】
  - base_name: ヴァジュラ (costume: 極弐魔装)
  - element=光(4) / type=杖棒(4) / rarity=S(3) / cv=木戸衣吹
  - max stats: HP=16570 / ATK=9640 / DEF=7610 / SPD=32 / BREAK=1620
  - hit_counts=[8, 7, 12] (3段)  motion_speed=[3.0/3.0/1.0]  mp=242
  - three_size=78/56/74 / initial_slot=5
  - BD: 天創雷ヴァジュラダーラ (arts_id=10317)
    - description: 敵全体に超強力な69連ダメージ＆一瞬だけスピード狂化
    - cost=7 / hit_count=69 / value=2.3 / additional_value=0.0
  - innate skills (3):
    - Vitality_Attack Multiply ×2.24643 — 残HPが多いほど攻撃力が絶大にアップ【熟度UPにつれてさらに効果値UP】
    - DamageLimitBreak Addition +1000000000.0 — 自身のダメージ上限が10億アップ
    - Mez Repel_Percent ×100.0 — 麻痺の発生を完全回避する

## items

### 新增 (10)

- [`130601`](items.json#L144871) 夢幻深層不知火検校
  - 古代石版に深く刻み込まれた
不知火検校の深層記憶。
- [`130602`](items.json#L144889) 不知火検校ジーン
  - 進化の為の情報が詰め込まれた
不知火検校の覚醒術式。
- [`130603`](items.json#L144907) 不知火検校ハート
  - 強き想いから生まれた
不知火検校の残留思念。
- [`130604`](items.json#L144925) 不知火検校コア
  - 魔力結晶に封印された
不知火検校のコア。
- [`130605`](items.json#L144943) 特殊設計書不知火検校
  - 極弐改造について記された
不知火検校の特殊設計書。
- [`131701`](items.json#L145231) 夢幻深層ヴァジュラ
  - 古代石版に深く刻み込まれた
ヴァジュラの深層記憶。
- [`131702`](items.json#L145249) ヴァジュラジーン
  - 進化の為の情報が詰め込まれた
ヴァジュラの覚醒術式。
- [`131703`](items.json#L145267) ヴァジュラハート
  - 強き想いから生まれた
ヴァジュラの残留思念。
- [`131704`](items.json#L145285) ヴァジュラコア
  - 魔力結晶に封印された
ヴァジュラのコア。
- [`131705`](items.json#L145303) 特殊設計書ヴァジュラ
  - 極弐改造について記された
ヴァジュラの特殊設計書。

## evolution_recipes

### 新增 (2)

- `130602`
- `131702`

## attack_motions

### 新增 (2)

- [`833`](attack_motions.json#L3327) 血界2
- [`834`](attack_motions.json#L3331) 神雷2

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
