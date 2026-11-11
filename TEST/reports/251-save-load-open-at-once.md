# TEST 251: Save and Load open at once and write nothing

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, checksums (`sha/`), timings, the load log, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-251/` (9650057b); names in brackets below are files there.

## Build

- **App**: main `b6d40a5`, a fresh clone. `gate.py --at b6d40a5`: "FOR TESTER — CORE at b6d40a5, 5931 tests, 0 failed".
- **Lodestar**: `6fc2738`, compiled into the app. **Loom**: not built, because no step uses it.
- **Shelf**: `643ae6e`. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Restore copy**: TEST 250u's copy. The md5s were logged before each load (`loads.txt`).
- Every step ran on `b6d40a5`.

## Summary

No findings. One click opens Save Game and Load Game. The screen is up by +0.36 s, the list fills about 2 s after the click, and opening then Cancel changes no byte of any save, after a fresh load and after a won fight. I lost my old slot 91 (see "What I got wrong"), so the regression ran from slot 90 to 91.

| # | Check | Result |
|---|---|---|
| 1 | Save and Load: screen, then list | **PASS**, with the timings below. The screen is up at +0.36 s, the list is empty at +2.2 s, and it fills between +1.9 and +2.5 s. |
| 2, 3 | Checksums, open and Cancel, after a fresh load | **PASS**. Unchanged across 2 Load and 2 Save opens. |
| 2, 3 | Checksums, open and Cancel, after a won fight | **PASS**. Unchanged across 1 Load and 1 Save open. |
| — | Control: a real save | Changes the checksums, so the check can see a write. |
| 4 | Pazaak | Not reachable yet, as the order says. |
| 5 | Dice; regression | **PASS**. SAME17; slot 90 to 91 ("reg251"), fight won, "Experience Points (XP) Received: 75". |

## 1. Timings (`times.txt`, `fill-times.txt`, `fill-save-times.txt`)

The times are measured from the click. Each click came 4 s after Escape opened Options.

| Click | First frame | Next frames | List fills |
|---|---|---|---|
| Load, fresh load | +0.36 s: Load screen, empty list | +2.19 s: still empty | (not watched) |
| Save, fresh load | +0.36 s: Save screen, "New Slot" only | +2.19 s: still empty | (not watched) |
| Load, watched | +0.20 s: **still Options**, Load Game selected | +0.77 s: Load screen, empty | between +1.89 and +2.48 s |
| Save, watched | +0.19 s: still Options | +0.75 s: Save screen, empty | between +1.88 and +2.44 s |
| Load, after the win | +0.36 s: Load screen, empty | +2.18 s: empty | by +3.7 s |
| Save, after the win | +0.37 s: Save screen, empty | +2.20 s: empty | by +3.7 s |

- So the screen appears between +0.20 and +0.36 s. My Xvfb draws only a few frames a second, so I can't say whether that's the very next frame.
- The list takes about 2 s. The dev log reads "save scan: 36 saves in 1640 ms".
- The order's +2 s frame always caught the empty list, so I added the watched runs, with a frame every 0.5 s (`fill-load-1` to `24`, `fill-save-1` to `12`).

## 2 and 3. Checksums (`sha/summary.txt`)

`sha251.sh` takes a sha256 of every file of the character: `icons-185.sav` plus the whole `icons-185.marks` folder, 69 files (70 after the regression save). It also takes one of the whole saves folder (885 files). The full lists are in `sha/`.

**After a fresh load** (slot 90, restored, on the board):

| Step | icons-185 | All saves |
|---|---|---|
| Board | a1654d32e4a976a2 | 2d73a687d0fc83e3 |
| Load, then Cancel | a1654d32e4a976a2 | 2d73a687d0fc83e3 |
| Close, board | a1654d32e4a976a2 | 2d73a687d0fc83e3 |
| Save, then Cancel | a1654d32e4a976a2 | 2d73a687d0fc83e3 |
| Close, board | a1654d32e4a976a2 | 2d73a687d0fc83e3 |
| Load watched, then Cancel; Save watched, then Cancel | a1654d32e4a976a2 | 2d73a687d0fc83e3 |

**Control**: saving "reg251" for real gives `015b2e6c157b1327` and `76886a087ab88537`, with one more file. So the check sees a write.

**After a won fight** (slot 91, Icon Nine won, XP popup closed with OK):

| Step | icons-185 | All saves |
|---|---|---|
| Board, then again 5 s later | 634ef793e02b878b | 158ff50d22564506 |
| Load, then Cancel | 634ef793e02b878b | 158ff50d22564506 |
| Close, board | 634ef793e02b878b | 158ff50d22564506 |
| Save, then Cancel | 634ef793e02b878b | 158ff50d22564506 |
| Close, board | 634ef793e02b878b | 158ff50d22564506 |

The Auto Save's files in `icons-185.marks` are dated by a load or by F4 (14:33:12, 14:35:56, 14:36:16), and never by an open.

## 5. Dice and regression

- **Dice**: the right Dice One Quick Save (Oct 19, 07:40:30); SAME17 (`dice.out`).
- **Regression**: Icon Nine. I loaded slot 90 (reg250) and saved it as "reg251", which took **slot 91**. Then a quick save, a load of slot 91, and the win, with "Experience Points (XP) Received: 75" (`xp-end3`).

## What I got wrong

- **I lost my old slot 91.** In the TEST 250c check I restored icons-185 from TEST 250u's restore copy, which was taken before slot 91 was saved. That replaced the live `.marks` folder, and slot 91 ("reg250u") went with it.
- So this chain step is slot 90 to 91, not 91 to 92. Next time it's 91 to 92.
- A restore of the regression character's `.marks` must come from a copy that includes the latest bookmark.
