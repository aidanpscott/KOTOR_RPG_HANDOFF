# TEST 210: creature alignment (companion and enemy prices, a companion's drift, its sheet, recovery), Loom's alignment box

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, my beds and Loom's written files are in `KOTOR_RPG_MAIN_WORK/media/screens/test-210/` (MAIN_WORK `cac063a3`). The step-by-step log is `TEST/reports/210-running-log.md`.

## Build

- **App**: main `71ce94c`, a git worktree beside my own clone. `gate.py --at 71ce94c`: "FOR TESTER — CORE at 71ce94c, 5243 tests, 0 failed"; ARCHIVE last green at 71ce94c. Lodestar `a9265df` = lock = compiled. The build (10.3 s) went through the lock, and git status was clean.
- **Loom** `949823c`, built in its own worktree through the lock; `pubspec.lock` unchanged, git status clean, Lodestar `a9265df`.
- **Settings**: defaults. Brightness: default.
- **Shelf** `553002b`: all packages identical.

The bed is a local package, `tester-align` (in `specs210/`), with three Jedi Consular 10s:

- Dark Mate: `alignment = 20`, a companion.
- Plain Mate: no alignment line, a companion.
- Sith Foe: `alignment = 10`, an enemy.

The player is Align Jedi (Consular 10; Heal, Force Affliction, Force Push).

A character file has no field for powers, and on her turn f says "Plain Mate knows no Force powers". So I gave the mates powers through `character.power-taken {subject: <tag>}` events in my save.

## Summary: prices and the drift line pass; one severe finding

| # | Check | Result |
|---|---|---|
| 1 | Companion prices | **PASS**. The player pays Heal 8f and Force Affliction 12f. Dark Mate (20) pays **Heal 12f** and **Force Affliction 10f** (105 → 95). Plain Mate (no line) pays Heal 8f and Force Affliction 12f, the same as the player |
| 2 | Companion's drift | **PASS**. After Dark Mate's Affliction, Feedback ends "Dark Mate has moved closer to the Dark Side of the Force." There's no "You have moved" line, and the player's marker stays mid-bar |
| 3 | Companion's sheet marker | **Not reached**. I found no way to open a companion's Character sheet: its small portraits, HUD control and Abilities' switch all show the player's sheet (`a4-ds2`) |
| 4 | Enemy priced at its start | **Not reached**. An enemy file can list no powers, so the Sith Foe only attacks |
| 5 | Recovery to its own start | **Not reached**: no companion sheet to read, and I found no way to step sessions |
| 6 | Loom's alignment box | **PASS** for the box and what it writes: 0 → `alignment = 0`, 100 → `alignment = 100`, empty → no line. **FINDING**: a refused value gives no reason (below) |
| 7 | Dice, regression | **PASS**. All 17 lines match the 206 baseline (only line 1's OCR differs). Regression: Save (slot 47, "reg210"), Escape then F4 (one quick save), Load, and a fight won |

## Severe (sent at once): a companion's cast list kills the play screen

When a companion knows fewer powers than the player, f on her turn turns the play screen into the red error screen: "RangeError (length): Invalid value: Not in inclusive range 0..1: 2". There's no stack in app.log.

The case: the player knew Heal, Force Affliction and Force Push; Plain Mate knew Heal and Force Affliction. Bump the Sith Foe, End Turn to "Plain Mate is waiting on you", press f. With three powers each the list opens. This fits the menu counting the player's list while indexing the companion's (a hypothesis). Frame: `a2-plainf.png`.

## Finding: Loom refuses an alignment silently

With 101, −1, 20.5, abc or 150, Create just dims. The box isn't marked, nothing appears under it, and the status line doesn't change. As a control, the file-name box does give its reason underneath ("A trailing number carries no meaning…"). Frames: `lo10-p2-_101__.png`, `lo10-probe-_100__.png`.

## Small

- On a companion's turn, the cast menu shares the top line with the vitality list and gets cut ("1 Heal 12f · 2 For…"). That line also still reads the player's "force 155 of 155" rather than the caster's 105.
- Loom's Create stays dim until a species is picked, with no word saying so.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
