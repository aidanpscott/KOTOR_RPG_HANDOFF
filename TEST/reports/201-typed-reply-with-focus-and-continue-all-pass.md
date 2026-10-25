# TEST 201: the typed reply with focus, "[Continue.]", and regression

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-201/` (MAIN_WORK `64c534d6`). The step-by-step log is `TEST/reports/201-running-log.md`.

## Build

App main `5e92c46`, a git worktree beside my own clone. `gate.py --at 5e92c46`: "FOR TESTER — CORE at 5e92c46, 5143 tests, 0 failed"; ARCHIVE last green at 5e92c46. Lodestar `e1b6ed9` = lock = compiled. Lens `5fe60a9`. The build (10.0 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged. Settings: defaults (no settings.json). Brightness: default. Shelf `b2de52b`, unchanged since TEST 200; every Shelf package in my data is identical to it.

Character: Tab Eleven (`specs201/tab.json`, a level-1 Consular at DEX 12), at party-lock-bed's Warden and Engineer.

## Summary: all pass

| # | Check | Result |
|---|---|---|
| 1 | Typed reply with focus | **PASS**. Tab, then "50 credits": the field reads "50 credits" and nothing is picked. A letter then a digit ("x9"): both type. Tab, a letter, Escape, then "2": the field empties and "2" picks [Continue.]. A click, then "1": types "1"; backspace to empty, then "1": picks [Leave.]. Escape never ended the conversation, neither with the field focused nor (twice) with it unfocused |
| 2 | "[Continue.]" | **PASS**: "2. [Continue.]" with its full stop at the Warden |
| 3 | TEST 200 points | **PASS**: "[Type a reply.]" is unnumbered; Tab and a click reach it; with the field empty, digits pick replies |
| 4 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185 line for line. Regression: Save (slot 37, "reg201"), Escape then F4 (one quick save), Load, and a fight to its end |

No findings.

Known and not filed: rows 2 px long; the red disc at load; no K2 capture of the combat bar or the container.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
