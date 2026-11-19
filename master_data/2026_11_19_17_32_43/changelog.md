# master_data changelog: 2026_11_19_16_00_00 → 2026_11_19_17_32_43

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| jobs | 1 | 0 | 0 |

## jobs

### 新增 (1)

- [`1578`](jobs.json#L201589) スルト rarity=5
  - rarity=5 / max_level=50
  - job_abilities (18):
    - WeaponType 長剣(1): pos=2.0 / neg=1.15 (rank=ss 超得意)
    - WeaponType 大剣(2): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 太刀(3): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 杖棒(4): pos=2.0 / neg=1.15 (rank=ss 超得意)
    - WeaponType 弓矢(5): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 連弩(6): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 戦斧(7): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 騎槍(8): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 投擲(9): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 拳闘(10): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 魔典(11): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - WeaponType 大鎌(12): pos=0.3 / neg=0.3 (rank=d 超苦手)
    - Element 火(1): pos=1.9 / neg=1.135 (rank=splus 超得意)
    - Element 水(2): pos=0.5 / neg=0.5 (rank=c 超苦手)
    - Element 風(3): pos=0.5 / neg=0.5 (rank=c 超苦手)
    - Element 光(4): pos=1.1 / neg=1.015 (rank=bplus 得意)
    - Element 闇(5): pos=1.0 / neg=1.0 (rank=b ふつう)
    - Element 無(6): pos=1.9 / neg=1.135 (rank=splus 超得意)
  - job_skills (19):
    - WeaponArtsHitCount Addition +5.0 — 運命を守る者の証。同装備セットのB.D.ヒット数+5
    - Attack Multiply ×1.77 — 長剣か杖棒装備で攻撃力とブレイク力とスピード77%UP
    - HitCount Addition +0.0 — 火か無属性の魔剣装備で攻撃ヒット数それぞれ+6
    - InstantDeath Repel_Percent ×100.0 — 長剣か杖棒装備で即死･麻痺･勇気分解無効
    - Vitality_Attack Multiply ×2.5 — 防御力を代償に、残HP多いほど攻撃力が超絶UP(最大150%UP)
    - MotionSpeed Multiply ×1.5 — サファイア獲得量DOWNを代償に、モーション速度が超UP
    - GuardBreak Multiply ×1.77 — 長剣でブレイク力77%UP
    - Speed Multiply ×1.77 — 長剣でスピード77%UP
    - Attack Multiply ×1.77 — 杖棒で攻撃力77%UP
    - GuardBreak Multiply ×1.77 — 杖棒でブレイク力77%UP
    - Speed Multiply ×1.77 — 杖棒でスピード77%UP
    - HitCount Addition +0.0 — 無属性で攻撃ヒット数それぞれ+6
    - Mez Repel_Percent ×100.0 — 長剣で麻痺無効
    - BlazeAbsorb Repel_Percent ×100.0 — 長剣で勇気分解無効
    - InstantDeath Repel_Percent ×100.0 — 杖棒で即死無効
    - Mez Repel_Percent ×100.0 — 杖棒で麻痺無効
    - BlazeAbsorb Repel_Percent ×100.0 — 杖棒で勇気分解無効
    - Defense Multiply ×0.05 — 防御を代償
    - SapphireDrop Multiply ×0.1 — サファイア獲得量DOWN

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
