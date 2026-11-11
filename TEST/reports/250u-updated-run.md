# TEST 250, updated: the run on 8159056

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, the load log, every launch's dev log and my fight script are in `KOTOR_RPG_MAIN_WORK/media/screens/test-250u/`; names in brackets below are files there. The first TEST 250 run, on 8769dce, is `250-enemy-pool-and-treat.md`.

## Build

- **App**: main `8159056`, a fresh clone. `gate.py --at 8159056`: "FOR TESTER — CORE at 8159056, 5904 tests, 0 failed".
- **Lodestar**: `e7ece7b` compiled into both the app and Loom. **Loom**: `5285e0d`, a fresh clone.
- **Settings**: defaults at the start. **Shelf**: `b630b4b`, check_shelf clean.
- **Beds**: the tries, death and test221 save tools rerun with no errors.
- **Restore copy**: every `.sav`, plus `.marks` for dice-one and icons-185, with md5s logged before each load (`loads.txt`) and each launch's dev log kept (`devlog/`).
- Every step ran on `8159056`.
- No K2 process was running when I started.

## Summary

One finding: a single click on a row of the in-game Options menu now only selects it, and a second click opens it. TEST 249's Finding 1 was my own tool's doing, and the popup does appear.

| # | Check | Result |
|---|---|---|
| A | Pool, Loom, treat | **PASS**, the same as on 8769dce. Pool 25 → 15 → 5 → 0, then a fresh load opens at 25 with Horror. Loom's typo and fix pass, and Verify again names the hand-edited typo. Treat reads "brought up to 0" on Death Bare, bleeding and held. |
| B | The fight-end popup | **PASS**. "Experience Points (XP) Received: 75", twice. TEST 249's Finding 1 was my script's End Turn click closing it. |
| C | Credits, then items | **PASS**. "Credits Received: 40"; "Item(s) Received:" on its own line, with the items wrapped under it, inside the border, and no box. |
| D | Death Hard end line | **PASS**. "Brute and Keeper fall"; Mate isn't named. |
| E | Hash 8 and 9 regression | **PASS**. Popup, end line, menu inside its frame; SAME17; slot 90 to 91, fight won. |
| — | Options rows need two clicks | **FINDING 1**. |

## B. The fight-end popup (TEST 249's Finding 1)

- **Coder is right about my tool.** `fightbolt.py` clicks End Turn at (960,1048) after every attack, and also when no enemy is left. That spot is the popup's OK.
- I made `fightbolt2.py`, which reads the End Turn button before each such click and stops, without clicking, once it's gone (`fightbolt2.py`).
- Icon Nine's win, stopped at the last blow, with frames every half second (`xp-end1` to `xp-end8`): the popup reads "**Experience Points (XP) Received: 75**", with OK at the bottom. Then I clicked OK.
- It happened again on the regression chain's own win (slot 91) (`xp2-end1` to `xp2-end6`).
- The end line after OK: "Gunman, Gunman and Gunman fall — unarmed … dies" (`reg-end`).
- **What I got wrong**: TEST 249's Finding 1 was my script, not the app. I'm withdrawing it.

## C. The reward popup

- **Credits** (Tries Normal, the Envoy): the opening now has "7. Any work for me?". Picking it gives "Envoy: Take this for your trouble." with "1. Goodbye.", then "Safe travels." and [Leave.]. Back on the board, one popup: "**Credits Received: 40**" (`c-pop2`).
- **Items** (Mine Two, the quartermaster): the popup shows "Journal Entry Added", then "**Item(s) Received:**" on its own line. Under it: "Security spike, Security spike, Security spike, Security spike," then "Repair part" on the next line. All of it is inside the border, with no box glyph (`c3-pop2`).
- **What I got wrong**: my first two Mine Two loads came from a restore copy whose mine-two.sav TEST 249 had already played, because the game writes events into the `.sav`. So the supplies were already taken, and no popup came, correctly.
  - The md5s show it: `f5cf5d92` against TEST 249's pristine `7a8be1dc` (`loads.txt` lines 3 to 8).
  - I took the pristine copy from TEST 249's restore copy and redid it (line 7).
  - A restore copy taken from the live folder after a test has played a save is not pristine for that save. Only the saves this test's tools rewrite (tries, death, test221) were fresh.

## D. Death Hard

- Mate reaches -10 at my 15th End Turn, and the log reads "Mate dies" (`d-log`).
- I shot the Brute twice. "Keeper: 1 of 12 — in your campaign, a01 left you at -10 · revived at 1", then "**Brute and Keeper fall** — Blaster Pistol · rolled 13 …" Mate isn't named (`d-s2`).

## A. TEST 250's steps

- **The pool** (Power Four):
  - Its dev-log line: "fight opens: seed 194523214, 0 dealt, rolling Power Four, apprentice.powers.01".
  - Hover readings (`a-hov0` to `a-hov3`): Force 25 of 25; after Horror, 15 of 23; after Horror, 5 of 21; after Force Slow, 0 of 20, "exhausted from 25".
  - A fresh load: Force 25 of 25, and Horror first (`a2-hov0`).
  - The same bed limit as on 8769dce: the fight can only end in defeat, so the restart is always a fresh load.
- **Loom** (`5285e0d`, on a copy of Tester Powers): with Human picked, "force_push, forse_push" shows "the rules carry no power forse_push" and Create is dim; "force_push, force_push" is legal and Create lights (`c-typo`, `c-fixed`).
  - I created pusher.crtr, then hand-edited it to list forse_push.
  - The first Verify (2 s after the edit) said "No problems found." "Verify again": "pusher.crtr lists the power "forse_push", and the rules carry no power by that id, so it would never be cast." (`c-verify1`, `c-verify2`).
  - That's the same as on 02fc8f5.
- **Treat**:
  - Death Bare, Mate at -1 bleeding: "treat Mate — d20 8 + Medicine 0 = 8 · brought up to 0".
  - Death Bare with Death set to Easy (held): "brought up to 0".
  - Death Normal: "Medpac — + base 10 + Medicine check 8 = 18 · Mate 12 of 12 (was -1) · 2 left" (the save carries medpacs) (`d-bare-bleed`, `d-bare-held`, `d-normal-bleed`).

## E. Regression

- **Hash 8** is A.
- **Hash 9**: the event popup (C, and B's XP); the end line (D, and Icon Nine's "Gunman, Gunman and Gunman fall"); and the destroyed footlocker's menu on Tries Hard, which opens upward inside its frame with Search (Awareness) visible (`e-menu`).
- **Dice**: SAME17.
- **Regression**: slot 90 to **91** ("reg250u"), then a quick save mid-fight, a load of slot 91, and the win: "Icon Nine: 100 of 196".
  - My script's own save step didn't save, because of Finding 1 below; that run fought from slot 90. I then did the chain by hand (`loads.txt`, the slot 90 and 91 lines).

## FINDING 1: Options rows take two clicks

- In game, Escape opens Options. One click on **Save Game** (568,271) only selects the row: it lights, and the right pane reads "Save the current game". The Save screen doesn't open. A second click opens it (`o1`, `o2`). **Load Game** behaves the same.
- I waited 4 s after Escape before the click, so it isn't the menu still opening.
- On 8769dce (TEST 250's first run, earlier today), the same script opened Save Game and Load Game with one click and saved slot 90. On 8159056 that save step silently didn't happen.
- I don't know whether two clicks is the intended behaviour now. I'm filing it because it changed between the two builds.

## Odd, not filed

- Loom's first Verify after a hand edit outside Loom still reads the old file; "Verify again" catches it. This happened on both Loom builds.

## What I got wrong

- TEST 249's Finding 1 (above): my script closed the popup.
- My restore copy's mine-two.sav (above).
