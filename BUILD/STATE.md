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
| ⚠ **`DROID-SKILLS-01` §2.3 vs §2.4** | They disagree about **Athletics** on the Assassin and Battle bodies — 15 against 14, and 13 against 12. `§2.2` says six and lists five; `§2.3` says eight and grids nine. **Reported, not resolved.** The app withholds Athletics meanwhile, which is valid under both readings |
| ⚠ **Science and Survival for droids** | On the 25-skill roster and **nowhere in the chapter**. Neither opened nor closed. Withheld, and said on screen |
| ⚠ **`PT-621`'s Protocol carve-out** | Opens `Persuade` to a "Protocol chassis" that is not one of `§2.3`'s four bodies. The carve-out names an axis the table cannot express |
| ⚠ **Three Sith base classes have no feat schedule** | `CLASS-TABLES-AUTHORED` has no Feats column and `FEAT-SCHEDULE-01`'s grid has no column for them. How many feats they gain at 1st level is not written, so Feats cannot complete for them |
| ⚠ **Skill Focus** | `SKILLS-01 §12` says 23 exist, one per skill; the library holds **one generic record**. And it grants aptitude at step 6, after Skills was priced at step 5 — a second backwards dependency where `CHARGEN-FLOW-MAP-01` names one. `PT-1200` ruled the first; nothing rules this |
| **13 unfinished menus → aptitude** | The 13 three-skill worlds grant one fewer aptitude source than the 288 four-skill ones. They are not offered, so nothing is wrong today |
| **Hub steps 7–9** | Powers, Equipment, Identity are unbuilt. Skills and Feats are built |
| **Character record** | Nothing is written and nothing is saved. `Continue` stays disabled |
| **`base-rules` distribution** | `§3c` says it ships with the product and does not say from where. It is generated onto the shelf and lives in no repository |
| **Five species parents** | The ruling asks for 57 records as 35 parents + 22 subraces; the corpus has 57 with all five parents present since `PT-1333`. ✓ closed at batch 4 |
| **Feat grant levels** | `granted` vs `selectable` is structural and carried; the per-level `_granted` column lives in `feat.2da`, a game file |
| **`recommend_order`** | Unauthored. Scoped negative across all staged files |
