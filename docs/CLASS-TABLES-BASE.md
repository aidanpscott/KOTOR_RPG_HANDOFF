# CLASS-TABLES-BASE — Soldier, Scout, Smuggler

**Source: `k1_classes.2da`, `cls_atk_1/2`, `cls_st_soldier`, `cls_st_scout`, `cls_st_scndrl`.** `source_system: kotor_game`. **Values identical in both games.**

**Companion to `CLASS-TABLES-JEDI`, which holds Guardian, Consular, and Sentinel.**

---

## Summary

| Class | Hit die | BAB | Primary ability | Base skill points | Saves |
|---|---|---|---|---|---|
| **Soldier** | **d10** | **full** — `CLS_ATK_1` | Strength | 2 | **Fortitude only** |
| **Scout** | **d8** | three-quarters — `CLS_ATK_2` | Dexterity | 6 | **all three good** |
| **Smuggler** | **d6** | three-quarters — `CLS_ATK_2` | Dexterity | 8 | **Reflex only** |

> **The Scout is the anomaly and it is the source's own.** **It has every save at the good progression** — +2 at level 1 rising to +12 — **where the Soldier and Smuggler each get one.** **Nothing in either game explains it.**

**Three BAB progressions exist.** **`CLS_ATK_1` is full** *(+1 per level, +20 at 20)*. **`CLS_ATK_2` is three-quarters** *(+15 at 20)*. **`CLS_ATK_3` is half** *(+10 at 20)* **and no class in either game uses it** — **not the Engineer, which uses `CLS_ATK_2`.** *An earlier version of this line called it "the droid-expert table" and that was wrong; see `CLASS-TABLES-DROID`.*

---

## Soldier — d10, Strength, 2 base skill points

**Full base attack bonus. Fortitude is the only good save.**

| Level | BAB | Fort | Ref | Will |
|---|---|---|---|---|
| **1** | +1 | +2 | +0 | +0 |
| **2** | +2 | +3 | +0 | +0 |
| **3** | +3 | +3 | +1 | +1 |
| **4** | +4 | +4 | +1 | +1 |
| **5** | +5 | +4 | +1 | +1 |
| **6** | +6 | +5 | +2 | +2 |
| **7** | +7 | +5 | +2 | +2 |
| **8** | +8 | +6 | +2 | +2 |
| **9** | +9 | +6 | +3 | +3 |
| **10** | +10 | +7 | +3 | +3 |
| **11** | +11 | +7 | +3 | +3 |
| **12** | +12 | +8 | +4 | +4 |
| **13** | +13 | +8 | +4 | +4 |
| **14** | +14 | +9 | +4 | +4 |
| **15** | +15 | +9 | +5 | +5 |
| **16** | +16 | +10 | +5 | +5 |
| **17** | +17 | +10 | +5 | +5 |
| **18** | +18 | +11 | +6 | +6 |
| **19** | +19 | +11 | +6 | +6 |
| **20** | +20 | +12 | +6 | +6 |

**Skill points: `(2 + Int mod) × 4` at level 1, `2 + Int mod` per level.** *`SKILLS-01 §9.1`.*

---

## Scout — d8, Dexterity, 6 base skill points

**Three-quarters base attack bonus. All three saves good.**

| Level | BAB | Fort | Ref | Will |
|---|---|---|---|---|
| **1** | +0 | +2 | +2 | +2 |
| **2** | +1 | +3 | +3 | +3 |
| **3** | +2 | +3 | +3 | +3 |
| **4** | +3 | +4 | +4 | +4 |
| **5** | +3 | +4 | +4 | +4 |
| **6** | +4 | +5 | +5 | +5 |
| **7** | +5 | +5 | +5 | +5 |
| **8** | +6 | +6 | +6 | +6 |
| **9** | +6 | +6 | +6 | +6 |
| **10** | +7 | +7 | +7 | +7 |
| **11** | +8 | +7 | +7 | +7 |
| **12** | +9 | +8 | +8 | +8 |
| **13** | +9 | +8 | +8 | +8 |
| **14** | +10 | +9 | +9 | +9 |
| **15** | +11 | +9 | +9 | +9 |
| **16** | +12 | +10 | +10 | +10 |
| **17** | +12 | +10 | +10 | +10 |
| **18** | +13 | +11 | +11 | +11 |
| **19** | +14 | +11 | +11 | +11 |
| **20** | +15 | +12 | +12 | +12 |

**Skill points: `(6 + Int mod) × 4` at level 1, `6 + Int mod` per level.**

---

## Smuggler — d6, Dexterity, 8 base skill points

**Three-quarters base attack bonus. Reflex is the only good save.**

| Level | BAB | Fort | Ref | Will |
|---|---|---|---|---|
| **1** | +0 | +0 | +2 | +0 |
| **2** | +1 | +0 | +3 | +0 |
| **3** | +2 | +1 | +3 | +1 |
| **4** | +3 | +1 | +4 | +1 |
| **5** | +3 | +1 | +4 | +1 |
| **6** | +4 | +2 | +5 | +2 |
| **7** | +5 | +2 | +5 | +2 |
| **8** | +6 | +2 | +6 | +2 |
| **9** | +6 | +3 | +6 | +3 |
| **10** | +7 | +3 | +7 | +3 |
| **11** | +8 | +3 | +7 | +3 |
| **12** | +9 | +4 | +8 | +4 |
| **13** | +9 | +4 | +8 | +4 |
| **14** | +10 | +4 | +9 | +4 |
| **15** | +11 | +5 | +9 | +5 |
| **16** | +12 | +5 | +10 | +5 |
| **17** | +12 | +5 | +10 | +5 |
| **18** | +13 | +6 | +11 | +6 |
| **19** | +14 | +6 | +11 | +6 |
| **20** | +15 | +6 | +12 | +6 |

**Skill points: `(8 + Int mod) × 4` at level 1, `8 + Int mod` per level.**

---

## Cross-checks

**Hit dice against `SKILLS-01`'s skill-point table:** **Soldier 2, Scout 6, Smuggler 8.** **`k1_classes.2da` agrees on all three.** *`SKILLS-01` also lists Machinist at 6 and the three Jedi classes; those come from K2 and are held separately.*

**Primary ability:** **Soldier STR, Scout DEX, Smuggler DEX** in K1. **K2 changed the Soldier's to CON** — *the change that dates the cut Bounty Hunter row, which kept STR.*

> **⚠ This cited `FEATS-LIBRARY-01 §9.1`, which does not exist — that document has sections 1 through 5.** **Grepped: the STR/CON claim appears in no other file either.** **Citation struck rather than repointed, because repointing it would require guessing which document was meant.** **The claim itself may still be true and now rests on nothing.**

**No `forcedie` on any of the three.** **Force points are a Jedi property.**

---

## Two things this does not carry

**Class skill lists** — **`SKILLS-01 §9.2` holds the rebuilt versions** against our 24 skills, not the source's 8.

**Feat and attack grants** — **`ATTACKS-01 §7` and §11.6 defer both to the class workstream.** **`k1_classes.2da` names a `featstable` per class — `SOL`, `SCT`, `SCD` — which is where the source's grant schedule lives.** **Those tables are not in current holdings.**

---

## Still missing for a playable character

**Machinist** — **K2 only.** `k1_classes.2da` does not carry it. **`SKILLS-01` gives 6 base skill points and `FEATS-CLASSWORK-01` discusses its feat table; hit die, BAB, and saves need `k2_classes.2da`.**

**Vitality per level** — **`PORT-01 v2` makes vitality accumulative from class, level, and Constitution modifier.** **The hit die is here; the formula that uses it should be checked against `RULES-01 v2`.**

**⚠ Bounty Hunter saving throws — authored. `PT-93`.**

    Fort strong, Reflex strong, Will weak — 12 / 12 / 6 at level 20.

    Scout           12 / 12 / 12  = 36
    Guardian        12 / 12 /  9  = 33
    Bounty Hunter   12 / 12 /  6  = 30
    Soldier         12 /  6 /  6  = 24
    Smuggler         6 / 12 /  6  = 24

**No Bounty Hunter save progression existed in any document.** **The source row points at `CLS_ST_SOLDIER`, which `PT-68` rejected as a placeholder — so it could not be ported without reversing that ruling.**

**Fort and Reflex is `PT-68`'s own description made mechanical:** *"hits as often and as hard as a Soldier, carries a Scout's bag of tricks."* **The Soldier's body and the Scout's feet.** **Will stays weak because nothing in the class is about resolve, and 33 would put it level with a Jedi.**

**⚠ It sits above the Soldier, 30 to 24. That is the price of the Soldier's twelve capstones.** **If that reads as too much the lever is Reflex to 9, giving 27.**

**Bounty Hunter and Smuggler** — **both are ours to design.** *`classes.2da` row 10 carries the cut Bounty Hunter skeleton: d10, `CLS_ATK_1`, Soldier saves, `skillpointbase` 1.*
