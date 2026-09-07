# CLASS-TABLES-DROID — Marksman and Engineer

**Source: `k1_classes.2da`, `cls_atk_1`, `cls_atk_2`, `cls_st_cm_drd`, `cls_st_ex_drd`.** `source_system: kotor_game`.

**The third of three class-table documents.** *`CLASS-TABLES-BASE` holds Soldier, Scout, and Smuggler; `CLASS-TABLES-JEDI` holds the three Jedi classes.*

> **This document existed nowhere and every droid sheet was built on inference.** **Written after a playtest reported it as a hard blocker.**

---

## Summary

| Class | Hit die | BAB | Base skill points | Saves |
|---|---|---|---|---|
| **Marksman** | **d12** | **full** — `CLS_ATK_1` | 2 | **Fortitude only** |
| **Engineer** | **d8** | three-quarters — `CLS_ATK_2` | 4 | **Reflex only** |

> **The Marksman's d12 is the largest hit die in the game.** **No organic class has one** — the Soldier's d10 is the organic ceiling. **A droid frame takes more punishment than a body.**

**Neither has a `forcedie`.** **Droids have no Force points, which `DROID-SKILLS-01 §2.2` already records as a prohibition rather than an omission.**

**Save progressions are mirror images.** **Marksman: Fortitude strong, Reflex and Will weak. Engineer: Reflex strong, Fortitude and Will weak.** *Rows 1–20 are byte-identical between the games.*

---

## The table

| Level | \multicolumn Marksman | | | | Engineer | | | |
|---|---|---|---|---|---|---|---|---|

| Level | **CD** BAB | Fort | Ref | Will | **ED** BAB | Fort | Ref | Will |
|---|---|---|---|---|---|---|---|---|
| **1** | +1 | +2 | +0 | +0 | +0 | +0 | +2 | +0 |
| **2** | +2 | +3 | +0 | +0 | +1 | +0 | +3 | +0 |
| **3** | +3 | +3 | +1 | +1 | +2 | +1 | +3 | +1 |
| **4** | +4 | +4 | +1 | +1 | +3 | +1 | +4 | +1 |
| **5** | +5 | +4 | +1 | +1 | +3 | +1 | +4 | +1 |
| **6** | +6 | +5 | +2 | +2 | +4 | +2 | +5 | +2 |
| **7** | +7 | +5 | +2 | +2 | +5 | +2 | +5 | +2 |
| **8** | +8 | +6 | +2 | +2 | +6 | +2 | +6 | +2 |
| **9** | +9 | +6 | +3 | +3 | +6 | +3 | +6 | +3 |
| **10** | +10 | +7 | +3 | +3 | +7 | +3 | +7 | +3 |
| **11** | +11 | +7 | +3 | +3 | +8 | +3 | +7 | +3 |
| **12** | +12 | +8 | +4 | +4 | +9 | +4 | +8 | +4 |
| **13** | +13 | +8 | +4 | +4 | +9 | +4 | +8 | +4 |
| **14** | +14 | +9 | +4 | +4 | +10 | +4 | +9 | +4 |
| **15** | +15 | +9 | +5 | +5 | +11 | +5 | +9 | +5 |
| **16** | +16 | +10 | +5 | +5 | +12 | +5 | +10 | +5 |
| **17** | +17 | +10 | +5 | +5 | +12 | +5 | +10 | +5 |
| **18** | +18 | +11 | +6 | +6 | +13 | +6 | +11 | +6 |
| **19** | +19 | +11 | +6 | +6 | +14 | +6 | +11 | +6 |
| **20** | +20 | +12 | +6 | +6 | +15 | +6 | +12 | +6 |

**Skill points:** `(base + Int mod) × 4` at 1st level, `base + Int mod` per level after. **Marksman base 2, Engineer base 4.**

> **`SKILLS-01 §9.1` has no droid row and this supplies it.** **`PREGENS-01` previously flagged the base as invented; it is not — it is `skillpointbase` in `k1_classes.2da`.**

**Feat schedule:** `FEAT-SCHEDULE-01`. **Marksman 11 by level 30, Engineer 16.**

---

## Chassis is not class

> **`DROID-SKILLS-01 §2.3` names four droid *species* — Astromech, Assassin, Battle, and Remote.** **`k1_classes.2da` names two droid *classes* — Combat and Expert.** **They are different axes and both apply.**

| Chassis | Class | Why |
|---|---|---|
| **Astromech** | **Engineer** | Utility. `CLS_ATK_2`, d8, Reflex strong. |
| **Assassin droid** | **Marksman** | Purpose-built to kill. d12, full BAB. |
| **Battle droid** | **Marksman** | Mass-produced infantry. |
| **Remote droid** | **Engineer** | Support and infiltration. |

**So HK-24 is an Assassin-chassis Marksman, and T4-K9 is an Astromech-chassis Engineer.** **The chassis governs which attacks and skills are open; the class governs hit die, attack progression, saves, and skill points.**

---

## What this corrects on the existing sheets

| | Was | Is |
|---|---|---|
| **T4-K9** BAB at 8 | +4 *(`CLS_ATK_3` assumed)* | **+6** — Engineer uses `CLS_ATK_2` |
| **T4-K9** skill base | 6 *(invented)* | **4** — `skillpointbase` |
| **T4-K9** Reflex at 8 | +10 | **+8** — strong save 6, Dex +2 |
| **T4-K9** reactions | 1 | **2** — BAB +6 |
| **HK-24** hit die | d12 *(inferred)* | **d12 — confirmed** |
| **HK-24** BAB at 6 | +6 *(inferred)* | **+6 — confirmed**, `CLS_ATK_1` |

> **`CLS_ATK_3` — the half progression — is used by no class in either game.** **An earlier correction assigned it to the Engineer on the strength of `CLASS-TABLES-BASE` calling it "the droid-expert table." That description was wrong.**
