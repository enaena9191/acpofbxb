# master_data changelog: 2026_11_11_15_58_05 → 2026_11_12_16_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| materials | 2 | 0 | 0 |
| items | 1 | 0 | 0 |
| jobs | 1 | 0 | 0 |
| scenarios | 11 | 0 | 0 |

## materials

### 新增 (2)

- [`42030061`](materials.json#L14031) ナインテイルズ rarity=4
  - 物語を書き加えるのはわたし。
[水太刀][B.D.攻撃力がUP][上限値:超高]
- [`53020306`](materials.json#L22067) エンジェルダウン rarity=5
  - 今度こそ私が守ってみせるわ。
[光拳闘][ﾓｰｼｮﾝ速度がUP][上限値:超高]

## items

### 新增 (1)

- [`8832`](items.json#L24565) 魂濁のオーブ
  - 魂濁の記憶の欠片。手に取ると
魔法少女になったあの日の記憶が蘇る。

## jobs

### 新增 (1)

- [`1577`](jobs.json#L201177) ドリーミン rarity=4
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
    - WeaponType 投擲(9): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 拳闘(10): pos=1.7 / neg=1.105 (rank=s 超得意)
    - WeaponType 魔典(11): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 大鎌(12): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 火(1): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 水(2): pos=1.7 / neg=1.105 (rank=s 超得意)
    - Element 風(3): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 光(4): pos=1.7 / neg=1.105 (rank=s 超得意)
    - Element 闇(5): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 無(6): pos=0.3 / neg=0.3 (rank=d 超苦手)
  - job_skills (8):
    - Speed Multiply ×1.2 — 世界を守り抜く証。装備セット全ての速度が大アップ
    - SapphireDrop Multiply ×1.45 — 水か光属性装備でサファイア獲得量45%UP
    - BlazeAttack Multiply ×2.0 — 水属性装備でB.D.攻撃力が100%UPし、光属性装備でモーション速度40%UP
    - DamageLimitBreak Addition +700000000.0 — 太刀か拳闘装備で同装備セット全体のﾀﾞﾒｰｼﾞ上限7億UP
    - BlazeAbsorb Repel_Percent ×100.0 — 魔法少女の願いが勇気分解を無効化する
    - SapphireDrop Multiply ×1.45 — 光属性装備でサファイア獲得量45%UP
    - MotionSpeed Multiply ×1.4 — 光属性装備でモーション速度40%UP
    - DamageLimitBreak Addition +700000000.0 — 拳闘装備で同装備セット全体のﾀﾞﾒｰｼﾞ上限7億UP

## scenarios

### 新增 (11)

- [`328215`](scenarios.json#L10563) 降臨！悪の大首領！
- [`328216`](scenarios.json#L10573) まさか！魔界が大パニック!?
- [`328217`](scenarios.json#L10583) 出撃！悪の組織！
- [`328218`](scenarios.json#L10593) ハクビという魔剣
- [`328219`](scenarios.json#L10603) 絢爛！九尾のキツネ！
- [`328220`](scenarios.json#L10613) 起動！古の巨大兵器！
- [`328221`](scenarios.json#L10623) ドゥルガーの真実
- [`328222`](scenarios.json#L10633) ピンチ！囚われたハジマリ！
- [`328223`](scenarios.json#L10643) 黒幕！明かされる野望！
- [`328224`](scenarios.json#L10653) 悪の組織はあきらめない！
- [`328225`](scenarios.json#L10663) エンドカードじゃ終わらせない！

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
