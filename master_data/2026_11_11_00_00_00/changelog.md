# master_data changelog: 2026_11_10_16_00_00 → 2026_11_11_00_00_00

## 总览

| 表 | 新增 | 删除 | 调整 |
|---|---:|---:|---:|
| weapons | 0 | 0 | 2 |

## weapons

### 调整 (2)

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

---

★ 跳过的 derived 表(非 local-master.dat 产物,需 server response 聚合):
- `memory_slot_skills.json`
- `npc_motions.json`
