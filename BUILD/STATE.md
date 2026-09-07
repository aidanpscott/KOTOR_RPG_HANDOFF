# STATE — every repository and package, as of the last push

**⚠ Rewritten in full each time, never appended.** If a line here disagrees
with a slice report, this file is the later one.

---

## Repository heads

| Repo | Head | Visible to the owner? |
|---|---|---|
| `KOTOR_RPG_MAIN_WORK` | `d4a4ca1` — check_decisions.py | ✓ |
| `KOTOR_RPG_HANDOFF` | this commit | ✓ |
| `Lodestar` | `fe58cfe` — `PACKAGE-FORMAT-01 §4·1`, required fields | ⚠ no |
| `Lens` | `d532c0a` — an arrival can be emphasised, keyed by name | ⚠ no |
| `Loom` | `ff4ff81` — required fields, where validate runs, deleting an arrival | ⚠ no |
| `KOTOR-RPG-APP` | `b1e57ae` — Backstory one tab, and Abilities | ⚠ no |

All six clean and level with origin.

## What each repository is

**`Lodestar`** — the rules engine. Pure Dart, no Flutter. Opens packages, areas
and characters; validates a package; answers where packages and saves live
(`Locations`, needs D and E). 10 test files.

**`Lens`** — the shared view layer, `PT-1381`. The area board, its palette, its
metrics and the pan/zoom viewport. Exists because `AREA-FORMAT-01 §2b` governs
how an area looks in **both** Loom and the app, the engine may hold no widgets,
and neither program may depend on the other.

**`Loom`** — the Builder. Package and area creation, tile painting, placing,
connections and arrivals, Package Properties, and `validate` on open with a
re-runnable Verify dialog. 12 test files.

**`KOTOR-RPG-APP`** — the play client. Console Home, the Package Main Menu, the
area and the walk, and character generation as far as the hub. 10 test files,
70 tests.

## The shelf — `~/.local/share/kotor-rpg/packages/`

| Package | What it is |
|---|---|
| `base-rules` | ⚠ **Generated, not authored.** 13 TOML files, 983 records. `PACKAGE-FORMAT-01 §3c`. Rebuild with `scripts/gen_base_rules.py` in MAIN_WORK. |
| `endar-spire` | The two-area test bed, made entirely in Loom |
| `taris-undercity` | A second package, so the library holds more than one tile |

## What runs end to end

Console Home lists three packages → selecting one reaches the Package Main
Menu → New Game opens the character entry screen → Create New Character runs
the pre-hub (Species → Model for droids → Class) → the hub opens with its step
strip → Back reaches the area → the marker walks through a door and arrives at
the named point in the second area, and back.

## ⚠ What is open

| | Need |
|---|---|
| **Worlds** | ✓ **closed at `PT-1396`.** 301 worlds ship in `base-rules`, exported from the Atlas resolver. Origin completes and the strip unlocks past step 1 |
| **13 unfinished menus** | 13 worlds carry three skills because `D-MENU4` is applied only where a menu is finished. They ship, and are not offered |
| **`ATLAS/decisions/`** | ⚠ 34 files `MAIN_WORK` has never read. `D-MENU4` sat there superseding a ruling three documents still carried |
| **Droid ability scores** | ✓ **closed at `PT-1403`.** `chassis.toml` ships 7 production spreads, all totalling 72 — 4 derived, 3 inferred and marked as such on screen. A droid completes Abilities |
| **Droid skills** | ✓ **closed at batch 5.** `droid_skills.toml` ships the four bodies. A droid completes Skills |
| **`DROID-SKILLS-01` §2.3 vs §2.4** | ✓ **closed at `PT-1405`.** The grid is right and the totals lag: Assassin 15, Battle 13. `stated_total` still carries what `§2.4` says, with the ruling named beside it. Athletics is offered |
| ⚠ **Science and Survival for droids** | On the 25-skill roster and **nowhere in the chapter**. Neither opened nor closed. Withheld, and said on screen |
| ⚠ **`PT-621`'s Protocol carve-out** | Opens `Persuade` to a "Protocol chassis" that is not one of `§2.3`'s four bodies. The carve-out names an axis the table cannot express |
| ⚠ **Three Sith base classes have no feat schedule** | **Searched and it holds.** All 34 `ATLAS/decisions/`, the Library's live tree, `CLASS-TABLES-AUTHORED` (`Level·BAB·Fort·Ref·Will`, no Feats column), `CLASSES-FORCE-PHB` (says it holds no level tables), and every `MAIN_WORK` file naming a Sith base class. **Level-30 totals exist; no cadence and no first-level count does.** Feats cannot complete for them |
| ⚠ **`FEAT-SCHEDULE-01`'s "Seven schedules" row** | Reads `Every third from 1 · Sith Assassin · 10`, where its own summary gives Sith Assassin **12** and the grid's `Assassin` column reaches 10 on that cadence. Either a mislabel of the prestige Assassin, or a cadence contradicting `PT-126`'s owner-instructed 12. **Reported, not resolved** |
| ⚠ **Skill Focus** | Half closed at `PT-1405`: the aptitude applies from level 2 and Skills are not repriced. **Still unbuildable** — `SKILLS-01 §12` says 23 exist, one per skill, and the library holds **one generic record with no skill on it** |
| **13 unfinished menus → aptitude** | The 13 three-skill worlds grant one fewer aptitude source than the 288 four-skill ones. They are not offered, so nothing is wrong today |
| **Hub steps 7–9** | Powers, Equipment, Identity are unbuilt. Skills and Feats are built |
| **Character record** | Nothing is written and nothing is saved. `Continue` stays disabled |
| **`base-rules` distribution** | `§3c` says it ships with the product and does not say from where. It is generated onto the shelf and lives in no repository |
| **Five species parents** | The ruling asks for 57 records as 35 parents + 22 subraces; the corpus has 57 with all five parents present since `PT-1333`. ✓ closed at batch 4 |
| **Feat grant levels** | `granted` vs `selectable` is structural and carried; the per-level `_granted` column lives in `feat.2da`, a game file |
| **`recommend_order`** | Unauthored. Scoped negative across all staged files |
