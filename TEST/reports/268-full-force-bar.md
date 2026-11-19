# TEST 268: The full Force bar

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the three authored scratch saves are in `MAIN_WORK/media/screens/test-268/`. Names in brackets below are files there.

## Build

- **App**: main `82a105f`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Heads**: before the gate I checked every shared tree against origin/main. The shared HANDOFF tree was clean but 2 behind, by my own two ledger commits. I fast-forwarded it (ff-only) to `c8a259d`. All the others were at origin and clean.
- **Gate**: I ran `gate.py --at 82a105f` twice from the project MAIN_WORK (`gate268-1.txt`, `gate268-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 82a105f, 6044 tests, 0 failed".
  - Both state lines: "MAIN_WORK 74680619 · HANDOFF c8a259d · KOTOR-RPG-APP 82a105f · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Watch Two (Force 57 of 57) and Aoo Eighty (no Force) on the real data dir. The restore copy `notes/saves268` was taken from `saves267`. Its md5s match the last BEFORE lines (Looter 119cbbbd, Pazaak Ten 6cb1a6a7, Watch Two 8a9ede2a, Aoo Eighty 4d6fe9eb).
- **Scratch**: Force 0, 19 and 38 of 57 came from copies of Watch Two's save in a scratch data dir (`~/kotor-tester/scratch-268`), each with one `power.cast` event carrying the Force value. They're in `scratch/`. The real saves have no edits.

## Summary

All three steps pass, apart from one difference from the order: the full bar has no lighter top row.

| # | Check | Result |
|---|---|---|
| 1 | Menu screens' Force strip | **PASS** for no Force, 0, a third, two thirds and full, on all five screens. **Difference**: full is 10,119,124 on every row, with no ~10,129,133 top row. |
| 2 | In-play Force well | Reported below. |
| 3 | Whole-screen look | **PASS** at 1920×1080 and 1280×720. |

## 1. The menu screens' strip

I read the strip's middle column (x 1500) on Equip, Inventory, Character, Abilities and Map for each character (`scripts/strip268.py`). The five screens gave identical readings every time. The strip's inside is rows 863–986, 124 rows, framed by 29,119,99.

| Character | Force | Empty (12,54,46) | Blend row | Filled (10,119,124) | Filled share |
|---|---|---|---|---|---|
| Aoo Eighty (`a-*`) | none | 863–986 | — | — | 0 |
| Force Zero (`f0-*`) | 0 of 57 | 863–986 | — | — | 0 |
| Force Low (`fl-*`) | 19 of 57 | 863–944 | 945 (12,72,69) | 946–986 | 41 rows + blend, 0.333 is 41.3 |
| Force High (`fh-*`) | 38 of 57 | 863–903 | 904 (11,97,97) | 905–986 | 82 rows + blend, 0.667 is 82.7 |
| Watch Two (`w-*`) | 57 of 57 | — | — | 863–986 | all |

- The fill rises from the bottom, and the split is in proportion within the blend row.
- **Full has no lighter top row.** On Watch Two, every row 863–986 is 10,119,124. Across the whole strip (x 1488–1512, rows 858–991) the only colours are 10,119,124 and the frame's own. Nothing reads near 10,129,133 (`w-inventory`).
- Aoo Eighty's Vitality bar keeps its black empty part: rows 863–918 black, 97,53,34 from 920 (`a-inventory`).

## 2. The in-play portrait's Force well (report only)

Middle column x 1894 of the well beside the board portrait. The inside is rows 945–1066.

| Character | Force | Empty | Filled |
|---|---|---|---|
| Aoo Eighty, Force Zero | none, 0 | 13,55,45 all | — |
| Force Low | 19 of 57 | 945–1028, 13,55,45 | 1029–1066, 29,120,100 |
| Force High | 38 of 57 | 945–982, 13,55,45 | 983–1066, 29,120,100 |
| Watch Two | 57 of 57 | — | 945–1066, 29,120,100 |

- It fills from the bottom, in proportion, but in the frame's teal (29,120,100), not the Force colour.
- The frame lights up beside the filled part only: 46,195,164 where filled, and 29,119,99 where empty (`fl-play`, zoomed in the frames).

## 3. Whole-screen look

- **1920×1080**: play and all five menu screens, for Watch Two, Aoo Eighty and the three scratch characters. Nothing cut off, overlapping or missing.
- **1280×720** (`o-*`, Force High): play and all five menu screens. Nothing cut off, overlapping or missing.
  - The strip scales to rows 576–657 (82). The fill is 603–657 plus a blend row at 602, which is 0.68 against 0.667.

## Odd, not filed

- **Character's Level Up buttons are still see-through** over the portrait (`w-character`), as in TEST 261's Finding 5. I found no ruling on it in my ledger.

## What I got wrong

- Nothing new this run. I wrote the Force saves on scratch copies from the start, and picked each by hand with a frame at the Load click.
