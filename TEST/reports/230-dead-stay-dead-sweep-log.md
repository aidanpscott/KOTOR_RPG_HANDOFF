# TEST 230: the dead stay dead through a reload, the Combat log on a lost Sweep

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-230/` (MAIN_WORK `403dfdb0`).

## Build

- **App**: main `e3a90c9`, a worktree beside my clone. `gate.py --at e3a90c9`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at e3a90c9, 5566 tests, 0 failed"; ARCHIVE last green at e3a90c9. Lodestar `4199fd7` = lock; built through the lock.
- **Settings**: defaults (no settings.json). **Shelf** `4f15356`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test229_saves.dart` as ordered. Body Blow Fists isn't in that tool, so I rewrote it with `author_tester_test228_saves.dart` on this build. Pristine copies kept.

## Summary: A to C all pass; nothing filed

| # | Check | Result |
|---|---|---|
| A | The dead stay dead | **PASS**. Body Blow Fists: bump, End Turn, Left kills the Weakling ("-6 left · dies"), End Turn, F4, Load the Quick Save. **Her action unspent**: no ring on (3,4), and the bar reads G, I, B (`a1-afterload2`). Left walks onto the square (`a1-walk`). The action is kept: a click on the Ironhide then swings ("needed 16 — hit · damage 6 … 394 left"). **Swing at the Brute before F4**: 396 left carries through the load, and Left still walks onto the square (`a2-walk`). The action stays spent: a click on the Ironhide reads "you have already acted" (`a2-acted`). **A second F4 and load** with her unmoved: the yard is pixel-identical across the two loads. Against the yard before the first load, the only difference is her portrait's bottom edge, which shifts with the box's height. Hover reads Gunman (4,3), Brute (5,4), Ironhide (4,5), and Left then walks onto the square. **Great Cleave after a load**, Cleaver, Weakling killed first ("-11 left · dies"): Brute hit (392 left), Ironhide hit (385 left), Gunman hit (394 left), all at "− Great Cleave 1". There is no Weakling line, and it stays at -11 (`a4-gc`) |
| B | The Combat log | **PASS**. Sweeper, x twice, on the Ironhide. **Loss**, on the third try: the box reads "Legsweep · … rolled 29 … against 32 — loss · damage 8 — 1d12 7 + Strength 4 + Knockdown 6 — half damage · 371 left". The log reads "Sweeper attacks Ironhide : \*loss\* : (15 + 14 = 29)", then "Sweeper damages Ironhide for 8 damage — half damage" (`b3-log`). No "miss" in seven frames after the key (`b3-burst`). **Win**, twice: "\*win\* : (20 + 14 = 34)", "damages Ironhide for 9 damage"; "\*win\* : (19 + 14 = 33)", "for 12 damage", each matching the box, no "half" (`b1`, `b2`). **True miss**, plain swing: the box reads "needed 16 — miss", the log "\*miss\* : (3 + 11 = 14)" with no damages line, and "miss" floats over the Ironhide (`bm2-burst`, `bm8-burst`). That is also the control: the same script catches the floater when there is one |
| C | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 67 ("reg230"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 128 of 196) |

Not tried: Sweep Pair's loss in the log, which the order didn't list (it was the second case in TEST 229's Finding 2).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
