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
| `base-rules` | ⚠ **Generated, not authored.** 14 TOML files, 986 records. `PACKAGE-FORMAT-01 §3c`. Rebuild with `scripts/gen_base_rules.py` in MAIN_WORK. |
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
| **Three Sith base classes at creation** | ✓ **closed at `PT-1407`.** One feat at first level. `first_level_feats.toml` carries it as an override with `sets_cadence: false` |
| ⚠ **Three Sith base classes at LEVEL-UP** | Still open, and `PT-1407` says so. Level-30 totals are authored — `PT-126` fixes the Sith Assassin's at 12 — and **when they gain the other eleven is unwritten** |
| ⚠ **`CLASSES-FORCE-PHB`'s Jedi Guardian attack row is transposed** | It reads `picks 18 · chains 20`; `CLASS-ATTACKS-01` gives Combat **36** picks and assigns the Guardian **18** chains with **20** feats at 30. Capstones match at 11, which says the row was built from `§2.3` and the two numbers crossed. **The extraction is faithful; the source is wrong.** Reported, not fixed |
| ⚠ **`PT-126` vs the Sith Assassin's rate** | `PT-126` ruled it **`Specialist`** *"by owner instruction"* and said the Sith side loses its `Middle` class; `CLASSES-FORCE-PHB` and `classes.json` both carry **`Middle`**. Does not touch creation; does touch attacks |
| **`attack_chains` / `attack_picks_at_30`** | Populated for **14** classes, not one. Read from each PHB chapter's record table, which 5 of 6 Force classes and all prestige classes lack. **`picks` is derivable from `rate`** (`§3`: 36/27/18); **`chains` is not** — `§2.3` makes it a per-class assignment inside a band, and its table is headed *"Assigned so far"* |
| ⚠ **`FEAT-SCHEDULE-01`'s "Seven schedules" row** | Reads `Every third from 1 · Sith Assassin · 10`, where its own summary gives Sith Assassin **12** and the grid's `Assassin` column reaches 10 on that cadence. Either a mislabel of the prestige Assassin, or a cadence contradicting `PT-126`'s owner-instructed 12. **Reported, not resolved** |
| ⚠ **Skill Focus** | Half closed at `PT-1405`: the aptitude applies from level 2 and Skills are not repriced. **Still unbuildable** — `SKILLS-01 §12` says 23 exist, one per skill, and the library holds **one generic record with no skill on it** |
| **13 unfinished menus → aptitude** | The 13 three-skill worlds grant one fewer aptitude source than the 288 four-skill ones. They are not offered, so nothing is wrong today |
| ⚠ **Hub step 8, Equipment** | **STOPPED.** `STARTING-EQUIPMENT-01` — 709 lines, CLOSED, 18 organic + 9 droid arrays, three routes, 28 grants — **is the source of no extract**, and neither is `ITEMS-01..09`. `equipment.json` reads `EQUIPMENT-01` and is the weapon RULES table, not a catalogue. So `PT-1200`'s offer cannot be priced and the two boxes stay unclickable |
| **Hub step 9, Identity** | Unbuilt |
| ⚠ **The profession grant is a category** | *robe · gauntlets · melee weapon · a tier above* — not an item and not a value. Resolving it needs the item catalogue |
| **The import question** | ✓ **Answered: ART.** `ITEMS-01..09` already hold 1,425 converted resrefs under seven named rulings; a stats import would overwrite them with the game's balance. See BUILD 12 |
| ⚠ **`PT-1369`'s pairing must count ICONS, not items** | K1 ships **183 `ii_*` icons across 38 classes** against **557** `.uti` blueprints — icons are per class + variation. Counted against items the pairing can never balance |
| ⚠ **K2's item icons not located** | No `ii_*` in K2's `chitin.key`, and this Steam build's `TexturePacks/` holds only controller overlays. Not checked: module `.rim`/`.erf`, `override/` |
| ⚠ **Powers at 1st level reads two sources one way** | `MULTICLASS-01 §2.2a` states 2 at Jedi level 1 and `PT-128` corrected the Sith Assassin to it; `POWER-COSTS-01 §6` calls acquisition **open**. Read as compatible — §6's open item is the schedule *after* level 1 — **and that reading is Claude's, not a ruling** |
| **Character record** | Nothing is written and nothing is saved. `Continue` stays disabled |
| **`base-rules` distribution** | `§3c` says it ships with the product and does not say from where. It is generated onto the shelf and lives in no repository |
| **Five species parents** | The ruling asks for 57 records as 35 parents + 22 subraces; the corpus has 57 with all five parents present since `PT-1333`. ✓ closed at batch 4 |
| **Feat grant levels** | `granted` vs `selectable` is structural and carried; the per-level `_granted` column lives in `feat.2da`, a game file |
| **`recommend_order`** | Unauthored. Scoped negative across all staged files |
