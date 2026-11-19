# TEST 264: The small fixes

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, crops, the readings (`px-264.txt`, `px-pz-words.txt`), the load log (with a frame at every Load click), both gate outputs, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-264/` (68a10b9f). Names in brackets below are files there.

## Build

- **App**: main `f9264b5`, a fresh clone.
- **Gate**: I ran `gate.py --at f9264b5` twice, one straight after the other (`gate264-1.txt`, `gate264-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at f9264b5, 6023 tests, 0 failed". Both state lines were "MAIN_WORK 468ec707 · HANDOFF ee658ae · KOTOR-RPG-APP f9264b5 · Lodestar e81b358 · Loom eb3aa63 · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221". Every head matched its origin and none was dirty.
- **Locks**: Lens `e449221` and Lodestar `e81b358`, compiled in.
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **The before**: TEST 263's frames of `34f727f`. I didn't rerun 34f727f.
- **K2**: `k2-pazaak` 06, 08, 10, 11 and 13 (native). `k2-capture-run/03a` and `05b`, `k2-ingame/80-map` and `k2-levelup/01` (resized, positions only). `k2-chargen/14` (4K, halved).
- **Saves**: Pazaak Ten, Looter and Watch Two, plus one new character made in chargen. The restore copy `notes/saves264` was taken from `saves263`, and its md5s match TEST 263's BEFORE lines.
- **Xvfb**: down when I checked before the first launch. I restarted it, with xsettingsd (antialias on, as before), and checked it was up.

## Summary

Steps 1, 2, 3, 5, 6 and 7 pass. Step 4 passes in part. Two findings:

- **Finding 1**: "Light" and "Dark" are whole but sit about 28 px left of the bar's ends instead of centred over it.
- **Finding 2**: the table's Forfeit Game words sit 7 px left of K2's.

| # | Check | Result |
|---|---|---|
| 1 | Pazaak words | **PASS**. Play and Clear Cards match K2's 06 and 08 exactly, and End Turn and Stand match 10/13 (End Turn's right edge is 1 px short). **Finding 2**: Forfeit Game. |
| 2 | The store | **PASS**. Thumb at 938–945, list line at 932, rows' box ends at 925. |
| 3 | List arrows | **PASS**. Inventory, Abilities and Party peak at 31,131,110 (05b 31,130,110). |
| 4 | The sheet's labels | **PASS in part**: both words are whole at 1920×1080, 1280×720 and 1280×1080, and the portrait hasn't moved. **Finding 1**: they aren't centred over the bar. |
| 5 | The Map | **PASS**. A 24 by 12 grid with lines within 2 px of 80's, the arrow on the player's square (15×18, pointing up), and the companion as a small dot. |
| 6 | Chargen feat arrows | **PASS**. One teal (46,194,161) arrow appears from the held tier to the takeable one, and none before red tiers. |
| 7 | The help box | **PASS**. A 1 px line with round corners at x 613 and 1306, y 437, and the "N" keeps its black detail. |

## FINDING 1: "Light" and "Dark" are whole, but left of the bar instead of centred over it

- At 1920 "Light" spans 257–301 and "Dark" 258–301, so both centre at about 279 (`cmp-sheet-labels`, `n-t-character`).
- The bar is curved:

  | Part of the bar | x | Centre |
  |---|---|---|
  | Top end (y 372) | 292–325 | ~308 |
  | Bottom end (y 768) | 290–323 | ~307 |
  | Whole bar | 264–325 | 294.5 |

  So the words sit about 28 px left of the bar's ends, and 15 px left of the whole bar's middle.
- K2's 01 (resized) has "Light" at 291–331, centred at 311, over the bar's top end.
- On 34f727f the words started at 291–292 and ran under the portrait. They're now whole because they moved left; the portrait still starts at 329 on both builds.
- At 1280×720 it's the same: the words centre at 184.5, against the bar's ends at about 204 (`n-42-sheet-1280x720`). At 1280×1080 "Light" is at 163–207 (`n-72-1280-sheet`).

## FINDING 2: the table's Forfeit Game words sit 7 px left of K2's (native 10, 11 and 13)

- K2: 1303–1419, rows 956–964, the same in all three captures. Ours: 1296–1412 on the same rows (`n-pz-10`, `px-pz-words.txt`).
- End Turn (1133–1218, K2 1133–1219) and Stand (1509–1563, the same) are on K2's rows 907–915.
- I don't have a 34f727f frame of the table, so I can't say whether Forfeit Game moved in this hash.

## 1. Pazaak (Pazaak Ten)

| Word | K2 06 / 08 | f9264b5 | 34f727f |
|---|---|---|---|
| Play | 1088–1128, rows 945–953 | the same | 1088–1128, rows 946–954 |
| Clear Cards | 1485–1600, rows 945–953 | the same | 1477–1592, rows 946–954 |

- My threshold puts Clear Cards' right edge at 1600 on both K2's frames and ours. MAIN's "about 1599" is the same ink.
- Apart from those two words, setup frames 04, 06, 07, 08 and 08-unhover are pixel-identical to 34f727f's.
- **The table** (`n-pz-10`, after Play and the sidedeck prompt `n-pz-09`): End Turn and Stand as above; Forfeit Game is Finding 2.

## 2. The store (Pazaak Ten's Card Dealer against 03a)

Along row y 600:

| | Rows' box edge | List line | Scroll thumb |
|---|---|---|---|
| 03a | 924–925 | 932–933 (100,86,40) | 938–945 (186,161,74) |
| f9264b5 | 924–925 | 932 (87,74,36) | 938–945 (186,161,74) |
| 34f727f | 924–925 | none | 942–949 |

- The line runs y 250–880 (`n-st-store`).

## 3. List arrows (Looter)

The up arrow beside each list (x 935–950, y 243–254), its peak:

| | Peak |
|---|---|
| K2 05b | 31,130,110 |
| f9264b5: Inventory, Abilities, Party | 31,131,110 |
| 34f727f | 29,119,99 (Party 30,121,100) |

- The change is below my 12-level diff threshold, so these three screens' frames otherwise read as identical to 34f727f's.

## 4. The sheet's labels

- Both words are whole at 1920×1080, 1280×720 and 1280×1080.
- The portrait's left edge is 329 at 1920 on both builds, and 220 at 1280×720 (two thirds of 329).
- Finding 1 for the centring.

## 5. The Map (Looter, then Watch Two for a companion)

- **Grid**: 25 lines across and 13 down, so 24 squares by 12. Against 80, across: 254, 312, 371, 430, 489 … 1664 (80: 256, 312, 371, 430, 488 … 1662). Down: 302, 346 … 830 (80: 303, 346 … 829). Every line is within 2 px; the area box hides the middle ones on my sample row.
- **Fills**: ground 9,32,20 and lines 17,50,36.
- **At 1280×1080** the grid stays 24 by 12 (every 39 px across, 44 down) (`n-71-1280-map`).
- **The arrow**: 15×18 px at x 736–750, y 534–551. It points up, centred on Looter's square (720–766), where TEST 263 drew the old marker (`z-map-arrow`).
- **The companion**: in Watch Two, Vela shows as a teal dot (17×17) one square below the arrow, as on the board (`n-51-watch-map`, `z-watch-board`).
- **The area**: the Range is 12×5 (`a01-range.toml`). The Map centres all 12 columns but paints only the squares explored so far (columns 0–6). That's the Map's explored-only rule, so I'm not filing it.

## 6. Chargen feat arrows (against chargen/14, halved)

- Before any pick, every tier 2 was red and no arrow showed (`n-cg-feats`).
- After Close Combat was held, one arrow appeared between it and its tier 2, which turned teal: 16×18 px at x 377–392, y 414–431, peaking at 46,194,161 (`n-cg-32-feats-held`, `z-feats-held`).
- No arrow appeared before a red tier.

## 7. The help box (the Map's first-visit help, `n-60-map-help`)

- **Line**: 1 px (25,106,87) at x 613 and 1306, top y 437, bottom y 607. The corners are rounded over about 3 px (`z-help-corner`).
- **Icon**: the "N" is black on the light house (`z-help-icon`).
- The same at 1280×1080 (`n-70-1280-map-help`).

## Odd, not filed

- **The "granted feats" popup** ("You have been granted the following feats", Squad Tactics) came up again when I went back into Feats from the hub. I didn't check 34f727f.
- **The store's list line** is 1 px (932); 03a's is 2 px (932–933), but 03a is resized.

## What I got wrong

- My Load helper's OCR failed on "Looter" again; I loaded it by hand with a frame.
- My first restore of xsettingsd's PID file caught the desktop's xsettingsd (6449). I corrected it to mine (13581) before launching.
- At 1280×1080 my first OK on the Map's help missed (the button sits lower at that size), so my first sheet frame shows the help box. I retook it.
