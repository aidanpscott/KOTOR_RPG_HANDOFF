# TEST 189: Entry, Class, the Forms list, reopen lighting, hub tabs, and Powers at Remaining 0

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-189/` (MAIN_WORK `43fb6839`). The step-by-step log is `TEST/reports/189-running-log.md`.

## Build

App `900a05f`, git archive from my own clone. `gate.py --at 900a05f`: "FOR TESTER — CORE at 900a05f, 4272 tests, 0 failed"; ARCHIVE last green at 900a05f. Lodestar `181ac71` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `5ac3d20`; check_shelf clean. The build (9.6 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

## Summary: everything passes; one question and two small notes

| # | Check | Result |
|---|---|---|
| 1 | Entry | **PASS**: Quick, Custom and Premade in a column, 57–58 px apart at 1920 (32 units at 1.8×). The description box ends above Cancel. Pointing at a dimmed option shows why: Quick says "Not available yet: no class has a recommended build written …", and Premade says "Tester Bolt supplies no premade characters …". The base page behind has empty cells and no face. **Note**: Quick's reason is longer than the box; its last line ("to fill it in from.") shows only after scrolling the box, and nothing shows that it scrolls |
| 2 | Class | **PASS**: a list with an empty icon cell per class, the name bar, and a scrolling description; no face. A click lights a class without choosing it; OK chooses. A droid on Jedi Consular: the Force classes are red, the description begins "a droid chassis holds no Force class", and OK is dead. (The reason starts lower-case) |
| 3 | Forms list | **PASS**: "Lightsaber Forms", the seven forms, then "Force Forms" straight after with no gap, then the four. No scrolling at 1920 or 1280. Clicking a heading changes nothing. Icons in colour; Form I held; one pick; the Force forms red |
| 4 | Reopen lighting | **PASS** for Feats (lit on Cautious) and Forms (lit on Contention). **Question** for Powers: I took Burst of Speed first, then Force Aura, and the page opens lit on Force Aura. Aura is the first of my powers in grid order, not the first I picked. Which is wanted? |
| 5 | Hub tabs | **PASS**: at 1920 the gaps between labels are 41–43 px, and "Basic Info" stands clearly apart from "Character". At 1280 they look even |
| 6 | Powers at Remaining 0 | **PASS**: Force Valor shows Add Power in its normal look, and pressing it does nothing; Improved Heal (refused, Character Level 12) shows Add dimmed |
| 7 | Dice, regression | **PASS**: the dice replay matches TEST 185 pixel for pixel. Escape > Save (slot 23), Escape then F4 (one quick save), Load, and a fight to its end |

Known and not filed: our own steps, the Attacks page, level-up, in-game frames, missing class and feat icons.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
