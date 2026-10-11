# TEST 161 — same-name characters (PT-2740 Fix 1)

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Screens: `BUILD/screens/test-161/`. Coder's answer read first (commit 9675ad4).

## Build

App `9675ad495eeec7d223f276fb3433b04dd66bec94` (git archive, lock unchanged). Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = lock. Shelf (my checkout) `1f04018394ddfb66bbab47985aa30932b7d44aef`. Lens `2bad745`, MAIN_WORK `bc05be08`, HANDOFF `08cd896` at start.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Typed clash (T3-35) | **Files PASS** (two saves, old untouched, both listed, old opens intact). **FAIL: inside the old T3-35, Options > Load Game lists the NEW T3-35's saves**; loading from it switches character |
| 2 | Organic clash (Kel Varn twice) | Same: files PASS, **same in-game Load list FAIL** |
| 3 | Generate | **PASS**: 100 presses, never a taken designation; a generated droid (T3-82) changed no existing file |
| 4 | Bookmarks stay with their character | **PASS** in the menu Load list; the in-game list is the FAIL above |
| 5 | Regression | **PASS**: Continue mid-fight, New Game after a Jedi, Save, Load, F4, F5 |

## The FAIL (1 and 2)

Repro: two characters with one name (old A, new B). From the package menu, Load Game → Switch to A → Load: A opens on its own square. Then Options → Load Game: the list shows **B's** Auto Save and bookmarks, not A's. Loading from it opens B.

- T3-35: A on (8,6) with "6: OLD35"; B on (5,5) with "7: NEW35". Inside A the in-game list shows "Auto Save 22:16:42 / 7: NEW35" (`1d`).
- Kel Varn: A on (2,6) with "8: KEL1"; B on (10,2) with "9: KEL2". Inside A it shows "Auto Save 22:26:31 / 9: KEL2" (`2c`).

Writes are right: F4 inside old T3-35 wrote `quick.mark` into `t3-35.marks` (A's folder), and the in-game **Save** list shows A's own "6: OLD35" (`1e`). Only the in-game **Load** list picks the other character. Likely cause, not shown: it looks the character up by name, not by save id.

## Evidence for the passes

- **Files.** `t3-35.sav` (old, unchanged at 22:10:19) + `t3-35-2.sav`; `kel-varn.sav` + `kel-varn-2.sav`. Each `.marks` holds only its own bookmark (000006 / 000007, 000008 / 000009).
- **Menu Load list** shows two T3-35 and two Kel Varn entries, each with its own bookmark (`1c`, `2c`).
- **Generate.** 100 designations seen (`3a`, `3b`); none of 35, 49, 75, 91 (taken). Then New Game with the generated name T3-82: the saves folder before/after differs only by the new `t3-82.sav` (`saves-pre3.txt`, `saves-post3.txt`).
- **Regression.** Onjo Hp's Auto Save resumes "round 4, Onjo Hp's turn", 44/103, Dressa 8/20, 4 moves (`5a`). T3-82 made right after it: on "in", empty well, no fight (`3c`). Save "R161" on (5,5), step, Load → (5,5); F4, step, F5 → (5,5) (`5c`).

## Fixtures

New: `t3-35-2`, `kel-varn`, `kel-varn-2`, `t3-82`. `run/cghuman.sh NAME` makes a Human Soldier through chargen.

Skills: `verification-before-completion`, `diagnosing-bugs` (the FAIL reproduced with a droid and an organic pair). Kept small per the owner's simplicity rule.
