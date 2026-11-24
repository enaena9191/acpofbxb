# master_data changelog: 2026_11_23_00_00_00 → 2026_11_24_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 2 | 0 | 6 |
| weapon_costumes | 1 | 0 | 0 |
| materials | 6 | 0 | 0 |
| items | 7 | 2 | 0 |
| pictures | 1 | 0 | 0 |
| evolution_recipes | 1 | 0 | 0 |
| attack_motions | 1 | 0 | 0 |

## weapons

### 新增 (2)

- [`169901`](weapons.json#L279546) 暁の竜機ドゥルガー
  - base_name: 暁の竜機ドゥルガー (costume: 魔装)
  - element=光(4) / type=拳闘(10) / rarity=SS(4) / cv=小鹿なお
  - max stats: HP=10580 / ATK=9820 / DEF=12150 / SPD=41 / BREAK=1940
  - hit_counts=[4, 7, 8] (3段)  motion_speed=[1.8/1.8/1.2]  mp=512
  - three_size=72/57/78 / initial_slot=2
  - BD: ジ･エンド･オブ･セラフィム (arts_id=699)
    - description: 敵全体に超強力な73連ダメージ＆30秒間、敵の動きを止める
    - cost=7 / hit_count=73 / value=2.0 / additional_value=0.0
  - innate skills (4):
    - HitCount Addition +1.951 — 光属性の味方全体の1～3撃目ヒット数を+2する【熟度21,41,60,80,99でさらに+1(最大+7)】
    - Vitality_Attack Multiply ×5.0 — 光属性の味方全体が、残HPが多いほど攻撃力がアップ（最大5倍）
    - Vitality_Speed Multiply ×3.0 — 光属性の味方全体が、残HPが多いほどスピードがアップ（最大3倍）
    - Defense Multiply ×1.25 — 光属性の魔剣の防御力がかなりアップ
- [`169902`](weapons.json#L279741) 暁の竜機ドゥルガー【極】
  - base_name: 暁の竜機ドゥルガー (costume: 極魔装)
  - element=光(4) / type=拳闘(10) / rarity=SS(4) / cv=小鹿なお
  - max stats: HP=13750 / ATK=12760 / DEF=15790 / SPD=41 / BREAK=2520
  - hit_counts=[5, 7, 11] (3段)  motion_speed=[1.8/1.8/1.2]  mp=512
  - three_size=72/57/78 / initial_slot=3
  - BD: ジ･エンド･オブ･セラフィム (arts_id=699)
    - description: 敵全体に超強力な73連ダメージ＆30秒間、敵の動きを止める
    - cost=7 / hit_count=73 / value=2.0 / additional_value=0.0
  - innate skills (4):
    - HitCount Addition +1.951 — 光属性の味方全体の1～3撃目ヒット数を+2する【熟度21,41,60,80,99でさらに+1(最大+7)】
    - Vitality_Attack Multiply ×5.0 — 光属性の味方全体が、残HPが多いほど攻撃力がアップ（最大5倍）
    - Vitality_Speed Multiply ×3.0 — 光属性の味方全体が、残HPが多いほどスピードがアップ（最大3倍）
    - Defense Multiply ×1.5 — 光属性の魔剣の防御力が大幅にアップ

### 调整 (6)

- [`169801`](weapons.json#L279156) ハジマリ
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
- [`169802`](weapons.json#L279351) ハジマリ【極】
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
- [`170001`](weapons.json#L279936) マナガルム.ALICE
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
- [`170002`](weapons.json#L280169) マナガルム.ALICE【極】
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
- [`170201`](weapons.json#L280402) 霊獣刀タマモノマエ=ハクビ
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
- [`170202`](weapons.json#L280597) 霊獣刀タマモノマエ=ハクビ【極】
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

## weapon_costumes

### 新增 (1)

- [`1544050`](weapon_costumes.json#L27377) 魔装《魔法少女》
  - 归属武器: 刻鳴鐘ユノ (weapon_base_id=1544)
  - effects: MotionSpeed Multiply ×1.03, SapphireDrop Multiply ×1.05

## materials

### 新增 (6)

- [`42170065`](materials.json#L14773) へーんしん rarity=4
  - 願いはいつか叶うんだから♪[拳闘のみ]
[ﾀﾞﾒｰｼﾞ減衰なしでﾋｯﾄ数増加][上限値:普]
- [`53010230`](materials.json#L21493) プロミス･トゥ･ユー rarity=5
  - ぜんぶ私で上書きしてあげる。
[同装備ｾｯﾄ光のスピードがUP][上限値:普]
- [`62010450`](materials.json#L27065) ﾌﾞﾙｰｼｪﾘｰの純真記憶･攻 rarity=6
  - 夢と希望はあたしが守るの♪
[ﾌﾞﾙｰｼｪﾘｰのみ][攻撃力がUP][上限値:極]
- [`62010451`](materials.json#L27079) ﾛｰｽﾞﾌｨﾉの純真記憶･攻 rarity=6
  - 魔法少女はぜったい負けない！
[ﾛｰｽﾞﾌｨﾉのみ][攻撃力がUP][上限値:極]
- [`63020304`](materials.json#L29403) ﾌﾞﾙｰｼｪﾘｰの純真記憶･速 rarity=6
  - 夢と希望はあたしが守るの♪
[ﾌﾞﾙｰｼｪﾘｰのみ][ﾓｰｼｮﾝ速度がUP][上限値:極]
- [`63020305`](materials.json#L29417) ﾛｰｽﾞﾌｨﾉの純真記憶･速 rarity=6
  - 魔法少女はぜったい負けない！
[ﾛｰｽﾞﾌｨﾉのみ][ﾓｰｼｮﾝ速度がUP][上限値:極]

## items

### 新增 (7)

- [`13297`](items.json#L33211) ﾌﾞﾙｰｼｪﾘｰの純真記憶･攻
  - 変換用だよ！
- [`13298`](items.json#L33229) ﾌﾞﾙｰｼｪﾘｰの純真記憶･速
  - 変換用だよ！
- [`13299`](items.json#L33247) ﾛｰｽﾞﾌｨﾉの純真記憶･攻
  - 変換用だよ！
- [`13300`](items.json#L33265) ﾛｰｽﾞﾌｨﾉの純真記憶･速
  - 変換用だよ！
- [`15367`](items.json#L33679) スタージュエル
  - 膨大な魔力から偶然精製された
稀少鉱石。ダイヤに似た別物。
- [`40855`](items.json#L129169) 【期間限定】真式･超強化の鍵α
  - 12月11日16時までショップで特定魔剣の熟度をあげられる鍵。
- [`1544050`](items.json#L162601) 刻鳴鐘ユノの変身衣装
  - 刻鳴鐘ユノの新たな力を
引き出すことができる魔術礼装。

### 删除 (2)

- [`15364`](../2026_11_23_00_00_00/items.json#L33571) オレンジスタージュエル
- [`40852`](../2026_11_23_00_00_00/items.json#L129061) 【期間限定】真式･超強化の鍵β

## pictures

### 新增 (1)

- [`7100`](pictures.json#L17297) ふたりで魔法少女！
  - skill: サファイア量が25%UP

## evolution_recipes

### 新增 (1)

- `169901`

## attack_motions

### 新增 (1)

- [`841`](attack_motions.json#L3355) 竜機

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
