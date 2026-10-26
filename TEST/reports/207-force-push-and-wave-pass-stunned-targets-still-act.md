# TEST 207: Force Push and Force Wave, the text seed, Loom on the new pin

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, logs and my push bed are in `KOTOR_RPG_MAIN_WORK/media/screens/test-207/` (MAIN_WORK `37f86f8b`). The step-by-step log is `TEST/reports/207-running-log.md`.

## Build

- **App**: main `4611a62`, a git worktree beside my own clone. `gate.py --at 4611a62`: "FOR TESTER — CORE at 4611a62, 5214 tests, 0 failed"; ARCHIVE last green at 4611a62. Lodestar `ec4b24b` = lock = compiled. The build (9.9 s) went through the lock, and `pubspec.lock` was unchanged.
- **Loom** `02b6faa`, built from my clone on its committed lock (`linux/` generated locally, as in TEST 206).
- **Settings**: defaults.
- **Shelf** `9656671`: base-rules synced.

No installed bed has Force Push targets, so I made `tester-push`: a 12×9 walled yard holding six targets.

- Slowpoke (DEX 3), with open ground behind it.
- Quickstep (DEX 30).
- Walled (DEX 3), near the corner walls.
- Blocked (DEX 3), with the Crate Dummy directly behind it.
- Droid Box, a droid.

The caster is Push Jedi, a Jedi Consular 16 at WIS 20 / CHA 18 (save DC 30) holding Force Push, Whirlwind and Wave. Each fight was started by bumping Quickstep.

## Summary: most pass; one finding

| # | Check | Result |
|---|---|---|
| 1 | Push, failed save | **PASS**: "Push Jedi attempts Force Push on Slowpoke : *success* : (18 - 4 = 14 vs. 30)" / "Slowpoke is Force Pushed" / "has been affected by Force Push" / 28 damage / "Slowpoke is stunned." The disc moves 128 px, 2 squares straight away. Against the walls, Walled moved 1 square (diagonally, into the corner). Blocked, with a creature behind it, moved 0. No opportunity attack was logged when Slowpoke was pushed out of my reach. **FINDING**: the stun doesn't stop the target's next turn (below) |
| 2 | Made save | **PASS**: "*resisted* : (20 - 4 = 16 vs. 30 automatic success)" / "Blocked is not Force Pushed" / 8 damage (half of level 16); no move |
| 3 | Force Wave | **PASS**: five that failed are each "Force Pushed" and "affected by Force Wave" (stunned), and the visible discs went outward. The Crate Dummy, which saved (natural 20), is "not Force Pushed", takes half damage (13) and isn't stunned |
| 4 | Droid | **PASS**: under Push, Droid Box is "Force Pushed" with no stun line (the prompt reads "resists" for the stun) and moved 1 square (wall). Under Wave the prompt reads "stunned", as K2 does |
| 5 | Immunity | **Not reached**: no installed bed has a creature with Immovable Object or Force Immunity: Stun |
| 6 | Text seed | **PASS**. I copied wave-207.sav by hand (gzip body edited to `"seed":"abc"`, header length patched; the original is untouched, md5 22465886…). Load gives "THIS SAVE WILL NOT OPEN / The campaign seed must be a whole number; this one is "abc", so its dice could not be replayed." The copy is out of `saves/` now. Note: `writeSave` refuses a bad seed, so no tool can write one |
| 7 | Loom | **PASS**: builds and opens a package on the new pin |
| 8 | Dice, regression | **PASS**: after two Spaces, Messages > Combat is identical to `dice-baseline-206.txt` (md5 a01882b3 both). Regression: Save (slot 44, "reg207"), Escape then F4 (one quick save), Load, and a fight won |

## Finding: a stunned target still takes its next turn

- **Slowpoke**, pushed and stunned on my turn in round 1 (my initiative 14, its 3). Still in round 1: "Slowpoke closes 2 squares — 3 to 1 · Slowpoke: unarmed · rolled 4 … miss", and in round 2 "Slowpoke attacks Push Jedi : *miss*".
- **Walled**, stunned in round 2. Still in round 2: "Walled closes 5 squares — 5 to 2 · out of movement…".

The power's text says "stunned for 1 round". Neither creature lost its next turn. Logs: `log1.png`, `log4.png`, `t2.png`.

## Small

- A Wave's prompt runs to 14 lines, and the message box grows down over most of the board.
- When a push moves the target 0 squares (Blocked), the log still says "Blocked is Force Pushed".
- "Slowpoke is stunned." is listed above "Round 1" in the Combat log.

KNOWN, not filed: a hit for 0 damage (PT-1622).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
