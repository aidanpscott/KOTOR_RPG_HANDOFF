# STATE — every repository and package, as of the last push

**⚠ Rewritten in full each time, never appended.** If a line here disagrees
with a slice report, this file is the later one.

---

## Repository heads

| Repo | Head | Visible to the owner? |
|---|---|---|
| `KOTOR_RPG_MAIN_WORK` | `869e13a` — batch 4, the five stale extracts closed | ✓ |
| `KOTOR_RPG_HANDOFF` | this commit | ✓ |
| `Lodestar` | `fe58cfe` — `PACKAGE-FORMAT-01 §4·1`, required fields | ⚠ no |
| `Lens` | `d532c0a` — an arrival can be emphasised, keyed by name | ⚠ no |
| `Loom` | `ff4ff81` — required fields, where validate runs, deleting an arrival | ⚠ no |
| `KOTOR-RPG-APP` | `592ec4b` — chargen step 2, the hub opens | ⚠ no |

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
| `base-rules` | ⚠ **Generated, not authored.** 10 TOML files, 671 records. `PACKAGE-FORMAT-01 §3c`. Rebuild with `scripts/gen_base_rules.py` in MAIN_WORK. |
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
| **Worlds** | No world roster and no three-skill menus. `WORLDS-MENUS-01` and the Atlas are named by `CHARGEN-DATA-01` and neither is staged. **This blocks Origin, and because unlock is sequential it blocks every hub step after it for any organic character.** |
| **Hub steps 3–9** | Backstory, Abilities, Skills, Feats, Powers, Equipment, Identity are unbuilt |
| **Character record** | Nothing is written and nothing is saved. `Continue` stays disabled |
| **`base-rules` distribution** | `§3c` says it ships with the product and does not say from where. It is generated onto the shelf and lives in no repository |
| **Five species parents** | The ruling asks for 57 records as 35 parents + 22 subraces; the corpus has 57 with all five parents present since `PT-1333`. ✓ closed at batch 4 |
| **Feat grant levels** | `granted` vs `selectable` is structural and carried; the per-level `_granted` column lives in `feat.2da`, a game file |
| **`recommend_order`** | Unauthored. Scoped negative across all staged files |
