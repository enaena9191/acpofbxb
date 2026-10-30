# master_data changelog: 2026_10_30_16_00_00 → 2026_10_30_18_23_29

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| materials | 2 | 0 | 0 |
| items | 3 | 1 | 0 |
| jobs | 1 | 0 | 0 |
| pictures | 1 | 0 | 0 |
| scenarios | 14 | 0 | 0 |

## materials

### 新增 (2)

- [`43070065`](materials.json#L17181) ラストスタンド rarity=4
  - ｢最後｣に立ち向かうのは誰だい？[投擲]
[残HP多いほどﾓｰｼｮﾝ速度UP][上限値:高]
- [`52140105`](materials.json#L20779) ギブアンドテイク rarity=5
  - まずは報酬のご相談から、です♪[風投擲]
[残HP多いほど攻撃力UP][上限値:超高]

## items

### 新增 (3)

- [`6280`](items.json#L7151) 11月魔装交換クーポン
  - 12月15日16時までショップで特定魔剣の魔装と交換できるクーポン。
- [`91282`](items.json#L130843) 作戦貢献度
  - 「エンドカードじゃ終わらせない｣ 作戦に貢献した証。
- [`2500049`](items.json#L166189) おはよう、眠りネズミ
  - マナ.ALICEを悪夢から目覚めさせた証

### 删除 (1)

- [`8830`](../2026_10_30_16_00_00/items.json#L24547) 魔力補給装束（おばけ仕様）

## jobs

### 新增 (1)

- [`1576`](jobs.json#L200765) イーヴィル rarity=4
  - rarity=4 / max_level=40
  - job_abilities (18):
    - WeaponType 長剣(1): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 大剣(2): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 太刀(3): pos=1.7 / neg=1.105 (rank=s 超得意)
    - WeaponType 杖棒(4): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 弓矢(5): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 連弩(6): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 戦斧(7): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 騎槍(8): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 投擲(9): pos=1.7 / neg=1.105 (rank=s 超得意)
    - WeaponType 拳闘(10): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 魔典(11): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 大鎌(12): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 火(1): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 水(2): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 風(3): pos=1.7 / neg=1.105 (rank=s 超得意)
    - Element 光(4): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 闇(5): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 無(6): pos=1.7 / neg=1.105 (rank=s 超得意)
  - job_skills (8):
    - Speed Multiply ×1.2 — 世界を守り抜く証。装備セット全ての速度が大アップ
    - MotionSpeed Multiply ×1.4 — 風か無属性装備でモーション速度40%UP
    - DamageLimitBreak Addition +700000000.0 — 風属性装備でﾀﾞﾒｰｼﾞ上限7億UPし、無属性装備でサファイア獲得量45%UP
    - Attack Multiply ×1.5 — 太刀か投擲装備で同装備セット全体の攻撃力50%UP
    - InstantDeath Repel_Percent ×100.0 — 悪人の意地が即死攻撃を無効化する
    - MotionSpeed Multiply ×1.4 — 無属性装備でモーション速度40%UP
    - SapphireDrop Multiply ×1.45 — 無属性装備でサファイア獲得量45%UP
    - Attack Multiply ×1.5 — 投擲装備で同装備セット全体の攻撃力50%UP

## pictures

### 新增 (1)

- [`2050`](pictures.json#L7163) 輝く希望とぬるぬるにょろろ！
  - skill: 残HPが多いほどモーション速度が30%UP[長剣のみ]

## scenarios

### 新增 (14)

- [`328201`](scenarios.json#L10423) 決戦！かがやく未来へ！
- [`328202`](scenarios.json#L10433) このままエンディング？
- [`328203`](scenarios.json#L10443) 魔法少女のハジマリ♪
- [`328204`](scenarios.json#L10453) 大変！最終回が終わらない！
- [`328205`](scenarios.json#L10463) ドキドキ！悪の作戦会議！
- [`328206`](scenarios.json#L10473) 愛と希望は誰のため…？
- [`328207`](scenarios.json#L10483) Re決戦！かがやく未来へ！
- [`328208`](scenarios.json#L10493) 驚愕！スリーピーの正体！
- [`328209`](scenarios.json#L10503) ReRe決戦！かがやく未来へ！
- [`328210`](scenarios.json#L10513) 真相！本当の最終回へ？
- [`328211`](scenarios.json#L10523) 悪の組織と魔法少女
- [`328212`](scenarios.json#L10533) マナガルム.ALICEの夢
- [`328213`](scenarios.json#L10543) オルタが届ける希望
- [`328214`](scenarios.json#L10553) おやすみ、眠りネズミ

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
