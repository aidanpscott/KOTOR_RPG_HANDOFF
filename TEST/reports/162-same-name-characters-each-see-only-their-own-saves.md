# TEST 162 — same-name characters each see only their own saves (PT-2740 Fix 1b)

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Screens: `BUILD/screens/test-162/`. Coder's answer read first (b143592, 9a1919f).

## Build

App `9a1919f45c539f197d872e01c0402034a1f70797` (git archive, lock unchanged). Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = lock. Shelf (my checkout) `1f04018394ddfb66bbab47985aa30932b7d44aef`. Lens `2bad745`, MAIN_WORK `4cc6bdd2`, HANDOFF `55f888f` at start.

## Summary: all six PASS

Pair used: T3-35 A (`t3-35`, OLD35, on (8,6)) and B (`t3-35-2`, NEW35, on (5,5)). B's save header (22:14) is newer than A's (22:10), so the old "Continue opens the other one" fault would show.

| # | Check | Result |
|---|---|---|
| 1 | Inside A: in-game Load list | **PASS**: only A's Auto Save, Quick Save and "6: OLD35"; OLD35 and Quick Save each open A on (8,6) (`1A-*`) |
| 2 | A: F4, walk, F5 | **PASS**: F4 on (6,4), walk to (2,2), F5 back on (6,4) (`2A`) |
| 3 | A: leave, Continue | **PASS**: after the session (6,4); after a session doing nothing (6,4); after one step (7,4). Always A (`3A`) |
| 4 | Same from B | **PASS**: in-game list only "Auto Save 22:16:42 / 7: NEW35"; NEW35 opens B on (5,5); F4 on (3,6), walk to (9,1), F5 back on (3,6); Continue after session (3,6), after nothing (3,6), after a step (4,6) (`4B-*`) |
| 5 | Main menu Load Game | **PASS**: opens on the last played: T3-82 at start, A after A's tests, B after B's. Switch Characters reaches both T3-35 and both Kel Varn, each with its own saves (`0`, `5-6`) |
| 6 | Regression | **PASS**: Onjo Hp resumes "round 4, Onjo Hp's turn", 44/103, Dressa 8/20; then New Game droid T3-27 on "in", empty well, no fight (`5-6`, `6`) |

The Kel Varn pair was not re-run (same code path; the T3-35 pair covers it).

Skills: `verification-before-completion`. Kept small per the owner's simplicity rule.
