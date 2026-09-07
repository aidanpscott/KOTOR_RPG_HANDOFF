# CLASS-TABLES-JEDI — The Three Force-Using Base Classes

**Status: ⚠ SETTLED — `PT-643`.** **The three tables are COMPLETE: 60 per-level rows across Guardian, Sentinel and Consular, with `BAB`, three saves, `Def`, feat schedule, Force points and regeneration.**

> **⚠ THE THREE RCR GAPS `§5` NAMED ARE ANSWERED ELSEWHERE, NOT BY EXTRACTION.**

    ⚠ starting feats and proficiencies  `Weapon Proficiency: Lightsaber` is in
                                        `FEATS-LIBRARY-01`
    ⚠ class features by level           the FEAT SCHEDULE is the progression —
                                        `§5` said so itself
    ⚠ the skill list                    ⚠ OURS IS 26 SKILLS, AUTHORED. Neither
                                        KOTOR's eight nor RCR's list governs.

**⚠ AND `GAP-002`, THE OTHER DEPENDENCY IN THIS HEADER, CLOSED AT `PT-248` — the KOTOR branch.** **RCR's Chapter 3 was the input to a branch the project did not take.**
**Depends on:** `FORCE-POOL-01` (D-AG) — ⚠ **superseded by `FORCE-POOL-01-v3`, SETTLED.** `GAP-002` — ⚠ **CLOSED at `PT-248`.**
**Sources:** `k1_classes.2da`, `cls_atk_1/2.2da`, `cls_st_jedi_g/s/c.2da`, `featgain.2da`, `skills.2da` — all `source_system: kotor_game`.

> **What is not here.** RCR's Chapter 3 has not been extracted. Where RCR and KOTOR diverge — class features, starting feats, proficiencies, the skill list itself — these tables carry the KOTOR structure and flag the gap. **They are not final until the extractor's read lands.**

---

## 1. The three classes at a glance

> **⚠ Feat counts here are K2 and run to level 30**, per `FEAT-SCHEDULE-01`. **This table previously carried K1's twenty-level figures — Guardian 9, Sentinel 7, Consular 7 — without saying which game they came from.** **Corrected.**

| | Jedi Guardian | Jedi Sentinel | Jedi Consular |
|---|---|---|---|
| **Role** | Lightsaber duelist. The Force supplements the blade. | Balance. Skills, stealth, versatility. | The Force is the weapon. |
| **Hit die** | d10 | d8 | d6 |
| **Force die** | d4 | d6 | d8 |
| **Base attack** | Full (+1/level) | Full | Full |

> **⚠ Every class in `k2_classes.2da` is `CLS_ATK_1` — full base attack, all seventeen.** **`PT-72`. BAB carries no information in this source and cannot distinguish a class.**

| **Good saves** | Fortitude, Reflex | Fortitude, Reflex | Fortitude, Will |
| **⚠ Third save** | **Will `Hybrid`** | **Will `Hybrid`** | **Reflex `Hybrid`** |
| **Skill points** | **3 + Int mod** | **5 + Int mod** | **4 + Int mod** |
| **Feats** | **20 across 30 levels** | **15** | **11** |
| **Force regen** | 1, +1 every 5 levels | 2, +1 every 5 levels | 3, +1 every **4** levels |

**Two things the game data settles that were not obvious:**

**Guardian and Sentinel have identical save progressions.** **⚠ Both are Fort/Ref `Strong` and Will `HYBRID` — NOT poor. `PT-530`.** **`cls_st_jedi_g` and `cls_st_jedi_s` give Will `1 → 5 → 9`, which is `PT-119`'s `Hybrid` ladder; `Weak` would be `0 → 6`.** **⚠ ALL THREE JEDI CLASSES CARRY A HYBRID SAVE — none has a weak one.** It differentiates on hit die, Force die, skill points, and BAB, not on saves.

**The Guardian gets five more feats than the Sentinel and nine more than the Consular** — **20 against 15 and 11.** **⚠ Raised from the source's 16 by `PT-84` when the Guardian moved to the `Combat` rate.** That is the whole of their feat advantage, and it lands on exactly the levels where the Force cost tiers step up — which is a coincidence worth noticing rather than a design.

---

## 2. Jedi Guardian

**Hit die d10 · Force die d4 · Skill points 2 + Int · Full base attack**

| Level | BAB | Fort | Ref | Will | **Def** | Feats | Force pts | Regen |
|---|---|---|---|---|---|---|---|---|
| 1 | +1 | +2 | +2 | +1 | — | **1** | 6 | 1 |
| 2 | +2 | +3 | +3 | +2 | — | — | 10 | 1 |
| 3 | +3 | +3 | +3 | +2 | — | **1** | 15 | 1 |
| 4 | +4 | +4 | +4 | +2 | — | — | 19 | 1 |
| 5 | +5 | +4 | +4 | +3 | — | — | 24 | 2 |
| 6 | +6 | +5 | +5 | +3 | — | **1** | 28 | 2 |
| 7 | +7 | +5 | +5 | +4 | — | **1** | 33 | 2 |
| 8 | +8 | +6 | +6 | +4 | — | — | 37 | 2 |
| 9 | +9 | +6 | +6 | +4 | — | **1** | 42 | 2 |
| 10 | +10 | +7 | +7 | +5 | — | — | 46 | 3 |
| 11 | +11 | +7 | +7 | +5 | — | — | 51 | 3 |
| 12 | +12 | +8 | +8 | +6 | — | **1** | 55 | 3 |
| 13 | +13 | +8 | +8 | +6 | — | **1** | 60 | 3 |
| 14 | +14 | +9 | +9 | +6 | — | — | 64 | 3 |
| 15 | +15 | +9 | +9 | +7 | — | **1** | 69 | 4 |
| 16 | +16 | +10 | +10 | +7 | — | — | 73 | 4 |
| 17 | +17 | +10 | +10 | +8 | — | — | 78 | 4 |
| 18 | +18 | +11 | +11 | +8 | — | **1** | 82 | 4 |
| 19 | +19 | +11 | +11 | +8 | — | — | 87 | 4 |
| 20 | +20 | +12 | +12 | +9 | — | — | 91 | 5 |

**Force points assume Wisdom +1, Charisma +1** (a typical Guardian spread). The real figure is `Force die + Wis mod + Cha mod` per level, maximum die at 1st.

**Class skills:** Awareness, Persuade, Medicine.

> **Tied with the Sentinel, not narrowest.** `jgd_class` and `jsn_class` mark exactly the same three rows in `skills.2da`. **The six-skill list this document previously gave the Sentinel is the Consular's.** See `SKILLS-01 §9.3`.

**The Guardian's Force curve, in play.** At 13th level a Guardian can cast **Force Storm twice** before running dry on the third round. At 8th they can afford two cheap utility powers plus two heavier ones with a little left over. **The blade is the primary weapon and the Force is the supplement** — the numbers enforce it without a rule saying so.

> **C-44, propagated.** This read *three castings, dry on the fourth* when written, and that was correct then. **Two inputs moved after:** `POWER-COSTS-01` (D-AL) reprices Force Storm from 20 to **24**, and `FORMS-01` (D-AM) halves in-combat regeneration from 3 to **2** at this level. **Recomputed: pool 60, cost 24, regen 2 → two castings, dry on round three.**
>
> **The level 8 figure is unaffected** — it used tier-1 and tier-2 costs, neither of which moved.

---

## 3. Jedi Sentinel

**Hit die d8 · Force die d6 · Skill points 4 + Int · Three-quarters base attack**

| Level | BAB | Fort | Ref | Will | **Def** | Feats | Force pts | Regen |
|---|---|---|---|---|---|---|---|---|
| 1 | +0 | +2 | +2 | +1 | — | **1** | 9 | 2 |
| 2 | +1 | +3 | +3 | +2 | — | — | 15 | 2 |
| 3 | +2 | +3 | +3 | +2 | — | **1** | 22 | 2 |
| 4 | +3 | +4 | +4 | +2 | — | — | 28 | 2 |
| 5 | +3 | +4 | +4 | +3 | — | — | 35 | 3 |
| 6 | +4 | +5 | +5 | +3 | — | **1** | 41 | 3 |
| 7 | +5 | +5 | +5 | +4 | — | — | 48 | 3 |
| 8 | +6 | +6 | +6 | +4 | — | — | 54 | 3 |
| 9 | +6 | +6 | +6 | +4 | — | **1** | 61 | 3 |
| 10 | +7 | +7 | +7 | +5 | — | — | 67 | 4 |
| 11 | +8 | +7 | +7 | +5 | — | — | 74 | 4 |
| 12 | +9 | +8 | +8 | +6 | — | **1** | 80 | 4 |
| 13 | +9 | +8 | +8 | +6 | — | — | 87 | 4 |
| 14 | +10 | +9 | +9 | +6 | — | — | 93 | 4 |
| 15 | +11 | +9 | +9 | +7 | — | **1** | 100 | 5 |
| 16 | +12 | +10 | +10 | +7 | — | — | 106 | 5 |
| 17 | +12 | +10 | +10 | +8 | — | — | 113 | 5 |
| 18 | +13 | +11 | +11 | +8 | — | **1** | 119 | 5 |
| 19 | +14 | +11 | +11 | +8 | — | — | 126 | 5 |
| 20 | +15 | +12 | +12 | +9 | — | — | 132 | 6 |

**Force points assume Wisdom +2, Charisma +1.**

**Class skills:** Awareness, Persuade, Medicine.

> **CORRECTED.** This document previously gave the Sentinel six class skills and called it *"the broadest list."* **The source gives three — identical to the Guardian's.** Verified against `skills.2da`.
>
> **The skill-points half of the claim survives and is stronger for it.** Skill points were the *only* thing distinguishing the Sentinel from the Guardian in the source. **`SKILLS-01 §9.2` gives them a rebuilt nine-skill list** — Security, Stealth, and Streetwise make them the class that hunts dark siders rather than duels them, which is what the class is for and what the source never expressed.

**Note the skill points.** In the source, 4 + Int against the other two classes' 2 + Int — **and it was the only differentiator, since the class skill lists were identical.** `SKILLS-01 §9.1` supersedes these values: bases of 3, 5, and 4 for Guardian, Sentinel, and Consular, authored against a 23-skill list rather than KOTOR's eight.

---

## 4. Jedi Consular

**Hit die d6 · Force die d8 · Skill points 2 + Int · Three-quarters base attack**

| Level | BAB | Fort | Ref | Will | **Def** | Feats | Force pts | Regen |
|---|---|---|---|---|---|---|---|---|
| 1 | +0 | +2 | +1 | +2 | — | **1** | 12 | 3 |
| 2 | +1 | +3 | +2 | +3 | — | — | 20 | 3 |
| 3 | +2 | +3 | +2 | +3 | — | **1** | 29 | 3 |
| 4 | +3 | +4 | +2 | +4 | — | — | 37 | 4 |
| 5 | +3 | +4 | +3 | +4 | — | — | 46 | 4 |
| 6 | +4 | +5 | +3 | +5 | — | **1** | 54 | 4 |
| 7 | +5 | +5 | +4 | +5 | — | — | 63 | 4 |
| 8 | +6 | +6 | +4 | +6 | — | — | 71 | 5 |
| 9 | +6 | +6 | +4 | +6 | — | **1** | 80 | 5 |
| 10 | +7 | +7 | +5 | +7 | — | — | 88 | 5 |
| 11 | +8 | +7 | +5 | +7 | — | — | 97 | 5 |
| 12 | +9 | +8 | +6 | +8 | — | **1** | 105 | 6 |
| 13 | +9 | +8 | +6 | +8 | — | — | 114 | 6 |
| 14 | +10 | +9 | +6 | +9 | — | — | 122 | 6 |
| 15 | +11 | +9 | +7 | +9 | — | **1** | 131 | 6 |
| 16 | +12 | +10 | +7 | +10 | — | — | 139 | 7 |
| 17 | +12 | +10 | +8 | +10 | — | — | 148 | 7 |
| 18 | +13 | +11 | +8 | +11 | — | **1** | 156 | 7 |
| 19 | +14 | +11 | +8 | +11 | — | — | 165 | 7 |
| 20 | +15 | +12 | +9 | +12 | — | — | 173 | 8 |

**Force points assume Wisdom +3, Charisma +1.**

**Class skills:** Slicing, Demolitions, Awareness, Repair, Persuade, Medicine.

**The Consular is the only Jedi class with Will as a `Strong` save**, and its Reflex is **⚠ `HYBRID`, not poor — `PT-530`.** **`cls_st_jedi_c` gives Reflex `1 → 9`.** Combined with the d6 hit die, they are physically the most fragile and mentally the most resilient — which is what makes the vitality spill from Force overreach bite hardest on them.

---

---

## 5A. The Defense Bonus column

**RCR class tables carry a `Defense Bonus` that progresses by level.** Confirmed on the Noble (RCR pp.42–43), where it runs +2 at 1st to +10 at 20th. **The three tables above carry the column with values unextracted** — the Jedi progressions are in RCR Chapter 3 and have not been read.

> **Reputation Bonus is deliberately absent.** RCR class tables carry it alongside Defense, and it advances on a per-class schedule rather than generically. **This port does not use Reputation** — `INFLUENCE-01` tracks per-companion regard instead, and RCR's global-fame statistic has no role beside it. The column is dropped rather than left blank.

**Consequence for the extraction:** Defense Bonus joins the ordered field list for every class read from RCR. It was not in the original order and would otherwise have been missed on all nine.

---

## 5. What still has to come from RCR

**These tables are the KOTOR skeleton. The following are unresolved and belong to the extractor's Chapter 3 read:**

| Gap | Why it matters |
|---|---|
| **Starting feats and proficiencies** | KOTOR grants lightsaber proficiency and armour restrictions at 1st level. RCR's equivalents are unread. |
| **Class features by level** | KOTOR's Jedi classes have almost none — the feat schedule *is* the progression. RCR may grant named abilities at specific levels. |
| **The skill list itself** | KOTOR has eight skills. RCR has considerably more. **Every class skill list above will need rebuilding** against RCR's list, and the skill-point values may need rescaling with it. |
| **Whether RCR's Jedi classes exist at all in this form** | RCR's Force-using base classes are Force Adept, Jedi Consular, and Jedi Guardian. **There is no Jedi Sentinel in RCR.** The Sentinel here is imported from KOTOR and needs a decision ID. |
| **Multiclassing rules** | A Soldier taking a level of Guardian is the KOTOR narrative. RCR's multiclass rules govern how that works. |

> **The Sentinel is the sharpest of these.** It does not exist in RCR, it is a KOTOR class, and the tables above give it real mechanical identity — **double skill points, against a class skill list identical to the Guardian's.** **Adopting it is a departure and needs an ID**, in the same way that modelling forms as feats does.
>
> **CORRECTION HISTORY.** This line previously read *"the broadest skill list and double skill points."* **The source gives the Sentinel three class skills, the same three as the Guardian.** Applied by the library, **reverted by a supersession that corrected §2 and §3 but re-spliced §5 verbatim**, and re-applied. **See §7.**


---

## 6. Two observations worth recording

**The Guardian's extra feats land at 7 and 13.** The Force cost tiers step at 6 and 13. So the Guardian receives a feat at the exact level their Force economy tightens most. In KOTOR that is coincidence; in this port it could be made deliberate — a combat feat arriving precisely when Force use gets expensive reinforces the "draw the saber" pressure.

**Skill points may be the Sentinel's whole case.** Once RCR's larger skill list replaces KOTOR's eight, 4 + Int against 2 + Int becomes a substantially larger gap than it looks here. If the Sentinel survives the departure decision, that is likely why.

---

## 7. A supersession reverted a correction, and every intake check passed

**Caught by the library at intake. Recorded because the pattern outlives the instance.**

**Three sites carried the Sentinel error.** §2's Guardian line, §3's Sentinel entry, and §5's departure argument. **The library corrected §5 in place under owner instruction.**

**A later revision of this document fixed §2 and §3 at source — and re-spliced §5 verbatim from the pre-correction text.** The correction vanished.

> **Every intake check passed.** The file was newer, byte-verified, and matched its announced checksum. **The predecessor carrying the in-place marker was retired to `_dead/` with the correction inside it.**
>
> **Only diffing against the specific corrected sites caught it.**

**Two guards, and they are different:**

**Correcting at source rather than in the compilation is right** — it is why §2 and §3 stayed fixed. **But it does not protect a site the author did not know had been corrected.**

**So: a supersession must be diffed against every known correction site in the file it replaces**, not merely checksummed. **Recorded as a standing intake step.**

**And it is a distinct failure from the two already named.** A *warrant* error attaches a citation the claim did not earn. A *target* error runs a clean check against the wrong object. **This is neither — it is a correct file overwriting a correct fix, with nothing anywhere in the wrong.**

---
