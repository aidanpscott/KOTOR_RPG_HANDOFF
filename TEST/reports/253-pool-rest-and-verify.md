# TEST 253: The pool rests at a real fight's end, and Loom's Verify

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, the load log, the dev logs (app and Loom) and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-253/` (fee12fd5); names in brackets below are files there.

## Build

- **App**: main `6e6b961`, a fresh clone. `gate.py --at 6e6b961`: "FOR TESTER — CORE at 6e6b961, 5937 tests, 0 failed".
- **Lodestar**: `6fc2738`, compiled into both the app and Loom. **Loom**: `524143e`, a fresh clone.
- **Shelf**: `6656cc9`. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Beds**: `author_tester_test221_saves.dart` wrote power-four, fearless-one, sneak-strike and shot-strike with no errors.
- **Restore copy**: every `.sav`, each with its own `.marks` folder:
  - dice-one: its `.sav` and `.marks`;
  - icons-185: the `.sav` and `.marks` as they stood together at the end of TEST 252;
  - power-four: no `.marks`.
- The md5s were logged before each load (`loads.txt`).
- Every step ran on `6e6b961`. TEST 252 had already started on `89d68b4`, so it was filed there.

## Summary

No findings. The apprentice's pool rests at a real fight's end, and Loom's first Verify after a hand edit names it.

| # | Check | Result |
|---|---|---|
| A | The pool rests at a fight's end | **PASS**. Force 5 after two Horrors. Left: Side Room, the fight is over. Left: a new fight; its first cast is Horror, and it then reads Force 15 of 23. |
| B | Loom's Verify, once | **PASS**. Clean, then a single Verify after the hand edit names "forse_push". "No problems found" didn't show. |
| C | Dice; regression | **PASS**. SAME17; slot 92 to 93, fight won, "Experience Points (XP) Received: 75". |

## A. Power Four

- The dev log: "fight opens: seed 194523214, 0 dealt, rolling Power Four, apprentice.powers.01". Initiative: Power Four 10, Sith Apprentice 2. The yard now has a door square to my left (`a-board`).
- **Two spaces**:
  - "Sith Apprentice — Horror at Power Four · Power Four — d20 18 + will 1 = 19 vs 7 · shaken"
  - "Sith Apprentice — Horror at Power Four · … Horror 2 = 13 vs 7 · shaken" (`a-t1`, `a-t2`).
- **Hover**: "Sith Apprentice · Level 2 · 400 of 400 · **Force 5 of 21** · exhausted from 25" (`a-hov2`).
- **Left**: "Side Room — arrived at in". The combat bar and End Turn are gone, so the fight is over (`a-side`).
- **Left again**: back at the start, and a new fight. The dev log reads "fight opens: seed 194523214, 4 dealt, rolling Power Four, apprentice.powers.01". The apprentice acted first this time: "Sith Apprentice — Horror at Power Four · Power Four — d20 1 + will 1 − shaken — Horror 2 = 0 vs 7 · cowering" (`a-back`).
- **Hover** after that cast: "**Force 15 of 23** · exhausted from 25" (`a-hov-new`). That's 25, less 10 for one Horror. The order expected "15 of 25"; the second number is the lowered ceiling (23), the same way TEST 250 read "15 of 23" after one Horror.
- So the first cast after the rest was **Horror**, which 5 Force couldn't have paid for, and the pool started the new fight full.

## B. Loom (`524143e`, on a copy of Tester Powers in `kotor-rpg/loom253/`)

- **Verify**, opened clean: "Tester Powers · No problems found." (`b-verify0`).
- I closed it, then edited `blueprints/characters/apprentice.toml` on disk:
  - from `powers = ["dark_fury", "stun_droid", "horror", "force_slow"]`
  - to `powers = ["dark_fury", "stun_droid", "horror", "force_slow", "forse_push"]`
- **Verify, once**, 2 s after the edit: "Tester Powers · **1 problem.** apprentice — "apprentice.toml" lists the power "forse_push", and the rules carry no power by that id, so it would never be cast." (`b-verify1`). The bar beside the package name and the status bar both read "1 problem". "No problems found" never showed.
- On TEST 250's and 250u's Loom builds, the first Verify after a hand edit read the old file. Here it reads the edit at once.

## C. Dice and regression

- **Dice**: the right Dice One Quick Save (Oct 19, 07:40:30); SAME17 (`dice.out`).
- **Regression**: I loaded slot 92 (reg252), restored with the `.sav` it was saved against, and it opened. I saved "reg253", which took **slot 93**. Then a quick save, a load of slot 93, and the win: "Experience Points (XP) Received: 75" (`xp-end3`).
- I've kept the icons-185 `.sav` and `.marks` together for the next step, slot 93 to 94.

## Odd, not filed

- Loom's file dialog lists a "loom253" bookmark that points at Loom's build folder, not at my package copies. Typing the path slowly reached the copy.
