# TEST 266: The srcIn hash

Real game and real Loom, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the two scratch files are in `MAIN_WORK/media/screens/test-266/`. Names in brackets below are files there.

## Build

- **App**: main `a5ba1c4`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Loom**: `9a1c3ef`, a fresh clone, built debug, with the same locks.
- **Heads**: before the gate I checked every shared tree against origin/main. All were at origin, and none was dirty.
- **Gate**: I ran `gate.py --at a5ba1c4` twice from the project MAIN_WORK (`gate266-1.txt`, `gate266-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at a5ba1c4, 6038 tests, 0 failed".
  - Both state lines: "MAIN_WORK f0bc3998 · HANDOFF 2726155 · KOTOR-RPG-APP a5ba1c4 · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
  - No "behind origin" showed.
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Looter, Pazaak Ten, Watch Two and Aoo Eighty, plus three new characters made in chargen.
  - The restore copy `notes/saves266` was taken from `saves265`. Its md5s match the last BEFORE lines (Looter 119cbbbd, Pazaak Ten 6cb1a6a7, Watch Two 8a9ede2a, Aoo Eighty 4d6fe9eb).
- **Copies**: step 4's arrival and step 6's Loom runs used scratch copies of the Shelf (below). The real packages have no edits.
- **Xvfb**: down when I checked. I restarted it with xsettingsd and checked it before the first launch.

## Summary

All seven steps pass. Nothing to file; one thing is noted below.

| # | Check | Result |
|---|---|---|
| 1 | Light and Dark | **PASS**. Centred on the bar's tips within 0.5 px at all three sizes, and neither is covered. |
| 2 | Forfeit Game | **PASS**. 1303–1419, rows 956–964, the same ink as native 10. |
| 3 | Granted-feats popup | **PASS**. In chargen, only on the first entry to Feats, whether that visit ends in Cancel or OK. In level-up, over the hub as it opens, and not on Feats. |
| 4 | Map arrow | **PASS**. Up on a north arrival, west after a step west, and about 14° after a shot at a target 5 east and 1 north. |
| 5 | Equip's list arrow | **PASS**. Peak 46,195,164, inside 05a/11/12's range. |
| 6 | Loom Warning | **PASS**. Drawn exactly like a Note. Problems beside it stay red. |
| 7 | Whole-screen look | **PASS** at 1920×1080 and 1280×1080. |

## 1. Light and Dark (Looter's sheet)

Ink edges, with the centre in brackets. The portrait's left edge is the last column.

| Size | Light | Dark | Ordered | Portrait from |
|---|---|---|---|---|
| 1920×1080 | 283–327 (305) | 284–327 (305.5) | 305.5 / 306 | 329 |
| 1280×720 | 188–216 (202) | 188–215 (201.5) | 202 / 202 | 220 |
| 1280×1080 | 172–216 (194) | 174–217 (195.5) | 194.5 / 196 | 220 |

Frames: `n-t-character`, `n-sheet-1280x720`, `n-sheet-1280x1080`.

## 2. Forfeit Game (Pazaak Ten's table)

- **Ours**: 1303–1419, rows 956–964 (`n-pz-10`).
- **Native 10**: the same at my threshold. MAIN's 1420 is the same edge.
- **End Turn and Stand**: unchanged (1133–1218 against K2's 1219, and 1509–1563).

## 3. The granted-feats popup

- **Chargen, first case** (`c1-*`). The first entry to Feats showed "You have been granted the following feat(s) this level." (Squad Tactics), under the first-visit help.
  - Then I left by Cancel. The second entry showed no box.
  - Then I picked Close Combat, left by OK, and entered again: no box.
- **Chargen, second case** (`c2-*`): a fresh character whose first visit to Feats ended in OK. The box showed on that first entry only.
- **Level-up** (Watch Two):
  - Jedi Guardian 7 grants no feat, so the hub opened with no box (`l-03a` at 1 s, `l-03` at 3 s).
  - Back, then Brawler 1: the box came up over the hub as it opened, with "Nothing In My Hands" (`l-05a` at 1 s, `l-05`).
  - After OK, Feats opened with no box (`l-07-feats-try`).

## 4. The Map arrow

- **Arrival facing north**: no Shelf arrival names a facing (only one placement says "west"), so arrivals face south. I gave the Starboard Hold's arrival "north" `facing = "north"` on a scratch copy (`scratch/a02-starboard-hold-with-facing-north.toml`). Then I loaded Looter there and walked through the Command Deck door.
  - The token arrived with its arc at the top, and the Map's arrow pointed up: 89.7° (`m-01-arrived`, `m-02-map-north`).
- **One step west**: the arrow turned to 179.7°, one square left (`m-04-map-west`, `z-m-04-map-west`).
- **Off-axis attack** (Aoo Eighty, real data dir): the same moves as TEST 264's step 8. The click on the droid 5 east and 1 north fired "Blaster Rifle · rolled 8 … miss".
  - The Map's arrow then read 14.0° (`m-13-shot`, `m-15-map-shot-clear`).
  - The board's whole-degree facing for 5 east and 1 north is 11°, and the nearest of eight would be 0°.
  - My angle comes from the arrow's centroid to its tip, on a 15 px arrow, so it's good to about ±3°.
- I measured all three angles with `scripts/arrow266.py`.

## 5. Equip's list arrow (Looter)

- **Ours**: both the up and down arrows peak at 46,195,164 (`n-t-equip`).
- **TEST 264**: 29,119,99.
- **K2**: 05a reads 43,183,154; 11 and 12 read 48,202,170.

## 6. Loom (9a1c3ef, on a scratch copy of the Shelf)

I added TEST 265's `trap-all` conversation to tester-sight's copy, so a Warning sits beside its 3 real problems.

| Package | Item | Label | Text |
|---|---|---|---|
| tester-sight (`l-6-tester-sight`) | Warning | 26,178,140 | 122,108,82 |
| tester-sight | its 3 problems | — | 140,58,50 (red) |
| tester-208 (`l-6-tester-208`) | Note | 26,178,140 | 122,108,82 |
| tester-talk (`l-6-tester-talk`) | 2 Warnings | 26,178,140 | 122,108,82 |
| tester-talk on 06050c3 (TEST 265) | Warning | 140,58,50 | 140,58,50 |

- So a Warning is now drawn exactly like a Note, and a problem beside it stays red.
- All these colours are read through the Verify dialog's dimming, so they compare like with like.

## 7. Whole-screen look

- **1920×1080**: play, every top tab (the `n-t-*` tour), Pazaak setup and table, Equip, the Map, level-up (class list, hub, Feats) and chargen (hub, Feats). Nothing cut off, overlapping or missing.
- **1280×1080** (`o-*`): the board, Equip, the Map, Pazaak setup and table, the level-up hub with its box, and the chargen hub and Feats with their boxes. Nothing cut off, overlapping or missing.
- At 1280 the granted-feats line wraps onto two lines inside its box.

## Odd, not filed

- **Nothing In My Hands has an empty icon box** in the level-up box. K2's 02 draws an icon for each granted feat. It may simply be a feat with no K2 icon, like the known icon gaps.

## What I got wrong

- My Load helper's OCR failed on "Looter" again (twice); I loaded it by hand with a frame each time.
- My first chargen script stopped one line early and skipped Skills, so Feats was still greyed. I ran the Skills line and went on.
- My first level-up pick (Jedi Guardian 7) grants no feat, so its hub couldn't show the box. I went Back and picked Brawler.
