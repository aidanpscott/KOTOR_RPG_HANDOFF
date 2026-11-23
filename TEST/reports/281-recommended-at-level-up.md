# TEST 281: Recommended at level-up

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, both gate outputs, the authored saves, the load log and Load-click frames, the dev logs and my scripts are in `MAIN_WORK/media/screens/test-281/7575ac9/` (MAIN_WORK `aecd8d8d`; see its PROVENANCE.txt).

Received since my last report: MAIN's TEST 281 order (logged HANDOFF `a5996cd`).

## Build

- **Waiting**: at 13:03, 7575ac9 wasn't on GitHub. It had landed by 13:05, during Coder's push sitting (shared HANDOFF one ahead with `702440e`). I touched nothing until every head was at origin and clean at 13:06:05.
- **App**: main `7575ac9`, built debug through `tool/one_at_a_time.sh` (pubspec.lock unchanged).
- **Gate**: `scripts/gate.py --at 7575ac9` twice from the project MAIN_WORK. Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 7575ac9, 6134 tests, 0 failed".
  - Both state lines: "MAIN_WORK fa6ac897 · HANDOFF 702440e · KOTOR-RPG-APP 7575ac9 · Lodestar a554b93 · Loom 9a1c3ef · Shelf 966cf6a · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: check_shelf: "35 rules files and 151 standard blueprints, all identical".
- **Saves**: none of my saves had these builds, so I authored six with `mksave281.py` from two saves the product had already accepted:
  - TEST 275's Gate Four (Rodian Soldier 2).
  - TEST 280's MD-280 (Battle droid Engineer 1).
  - Each has the classes in the order taken and XP for exactly one more level.
  - Eight loads, each a copy in its own fresh scratch data dir, with BEFORE and AFTER md5s and a frame at the Load click. No level-up was accepted, and every copy's md5 is unchanged.
  - The live saves equal `notes/saves275` apart from the four known, at the start and the end.
- **Window sizes**: 1920x1080 and 1152x648 (new).

## Results

| Step | Save | Before | After Recommended | |
|---|---|---|---|---|
| 1 | Soldier 3 to 4 | all 13, 1 point | STR 14, nothing else, Remaining 0 | PASS |
| 1 | Soldier 3 to 4, STR 23 | STR 23 with no + | DEX 14, nothing else | PASS |
| 2 | Marksman 3 to 4 | all 13 | CON 14 | PASS |
| 3 | Soldier 3 / Scout 4 taking Pirate (level 8) | all 13 | DEX 14, not STR | PASS |
| 4 | Battle droid Soldier 7 taking Pirate | — | can't be reached: see FINDING 2 | BLOCKED |
| 5 | Battle droid Engineer 3 to 4 | — | the page has no rows: see FINDING 1 | FAIL |
| 6 | Soldier 3 to 4, WIS raised by hand first | WIS 14, Remaining 0 | WIS left at 14, nothing else moved | PASS |
| 7 | level-up at 1920 and 1152x648 | | no clipping or overlap | PASS |

- **Step 1**: the STR 23 copy matches the rule. With the primary at the cap, the next is the highest in the Soldier's spread, and DEX and CON tie at 14, so the tie goes to DEX.
- **Step 3**: Pirate is open to the organic character (no requirement). Its level-up Skills, as a control for step 4, put all 5 points into Pilot, the first on the Pirate's list (`d-08`).
- **Step 6**: with a single point there's nothing left once a hand-raised ability takes it. Recommended goes dim and pressing it changes nothing.
- **Ties between base classes**: I couldn't test "ties to the first taken". Two base classes with equal levels at an attribute level (4, 8, 12) would need a third class before the prestige level, which the three-class cap forbids.
- **Droid Skills at level-up**: on the Engineer 3 to 4 droid, Recommended is lit and puts the 4 points in order: Repair 2 to 5 (its cap of 7 less its +2) and Slicing 4 to 5, Remaining 0 (`f-08`).

## FINDING 1: a droid can't finish a level-up at an attribute level

MD-280, Battle droid Engineer 3 taking level 4:
- The level-up Attributes page has no ability rows and reads "no spread is available for this chassis" in red. OK is dim (`f-04`).
- Recommended is lit (new in 7575ac9) and pressing it changes nothing (`f-05`).
- Skills and Attacks complete, but Accept stays dim and clicking it does nothing (`f-12`, `f-13`). The level can't be taken.

The level-up builds `AbilitiesScreen` with `isDroid: true` and no `chassisSpread` (`play_screen.dart`, `LevelUpStep.attributes`). `abilities_screen.dart` then treats it as a chargen droid with no spread (`noSpread`): no rows and OK dim.

The same save on the 5c1bbde build shows the same empty page with Recommended dim (`g-01`). So the page is older than this hash; 7575ac9 only lights Recommended on it.

It applies to every droid at levels 4, 8, 12 and so on, if the authored save is representative. The droid parts came from a chargen-built MD-280, and only its class levels and XP were written. Step 5's "raises its class's primary" can't be seen.

## FINDING 2: step 4's droid can't take Pirate, or another Soldier level

MD-280 written as Battle droid Soldier 7 taking level 8:
- Pirate reads "A droid cannot take this class.", OK dim (`e-02`). This is TEST 280's FINDING 1: every prestige class refuses a droid. CLASS-ROSTER-01 §3b has Pirate "OPEN" (owner, 2026-10-23).
- Soldier is refused the same way, although the droid holds 7 Soldier levels (`e-03`). A droid can't be a Soldier at chargen either (TEST 276's FINDING 3), so the order's droid Soldier 7 isn't a character the game can make.

Step 4 needs both fixed, or a droid-open base class with Pirate open to droids.

## Odd, not filed

- **Recommended is lit with nothing to raise** on the droid's empty Attributes page. It follows FINDING 1.
- **The level-up granted list on an authored save** lists every grant from the authored levels at once (Pirate level: Both Hands, Targeting 1, Uncanny Dodge 1, Terrain Sense, Ground Read, Boresight, …). That comes from my authoring, not the product.

## What I got wrong

- **1152x648**: my window finder didn't know the new size, so the first walk's clicks didn't land. I added the size and redid the walk.
- **Fixtures**: all saves are authored, not played to these levels. Gate Four is Rodian (DEX +2, CHA −2), so the Character sheet differs from the Attributes page's base scores.
