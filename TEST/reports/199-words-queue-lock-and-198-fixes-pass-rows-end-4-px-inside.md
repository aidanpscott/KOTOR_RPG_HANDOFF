# TEST 199: right edges, conversation words, the store button, the combat queue, the package lock, and the TEST 198 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-199/` (MAIN_WORK `a599eb63`). The step-by-step log is `TEST/reports/199-running-log.md`.

## Build

App `a4446e8` (origin/in-game-batch-4), a git worktree beside my own clone. `gate.py --at a4446e8`: "FOR TESTER — CORE at a4446e8, 5125 tests, 0 failed". ARCHIVE reads "last green at 47fe0ea", not at this hash. Lodestar `8350846` = lock = compiled. Lens `5fe60a9`. Shelf `f0a280a`; check_shelf clean (33 rules files, 125 blueprints). The build (10.1 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Settings were reset to the defaults before the run (the old file is at `notes/settings-before-test199.json`). Brightness: default throughout.

Beds and fixtures:
- party-lock-bed: copied from my Shelf clone into my data dir.
- `specs199/`: Pool One, Pool Two and Pool None are level-1 Consulars at DEX 12, 16 and 10, which give reaction pools of one, two and none. Fight Nine is a Soldier with Vela in Tester Bolt.

## Summary: all pass but one small finding; three things not reached

| # | Check | Result |
|---|---|---|
| 1 | Right edges | **Bar PASS** on Inventory, Equip and Abilities' Skills against K2's 05b, 05a and 05c: the line at x 932–933, a 1 px gap, the 14 px bar (935–948) and the 8 px thumb (938–945), identical to K2 on all three. The same proportions at 1280×720. **Small finding**: the rows end 4 px inside the line, where K2's end 6 px inside (ours at x 927, K2's at 925). At 1280 they also end 4 px inside |
| 2 | Conversation words | **PASS**: "[Interrupt.] Which deck is breached?", "[Continue]", "[Type a reply.]", "[Leave.]". "Reactions left: one" at DEX 12 and "two" at DEX 16. At DEX 10 there's no interrupt row, and the right of the bar reads "⟩ there is an interruption here and you have no reaction to spend". The digit presses Continue and Leave |
| 3 | Store | **PASS**: the button reads "Buy Item", and "Sell Item" while selling; the titles stay "Buying Items" / "Selling Items" |
| 4 | Combat queue | **PASS** on the player's own turn. Three slots: one step dims Move (brightness 93 → 28), an attack dims the action slot, and the oval shows the sword. "Reactions (out of turn): one", with "Defense base 10 + Dexterity 2 = 12" under it. End Turn sits under the queue in a red frame. Hovering a 4-square path shows "5 → 1" at the Move slot's corner. On a companion's turn the slots are the player's |
| 5 | Package lock | **PASS**: after the Warden's second line, Remove is greyed with "You are unable to change your party at this time."; after the Engineer's line it's live again |
| 6 | TEST 198 fixes | **PASS**: a companion down at −2 shows "down — not until this fight is over" while the standing one shows the lock line. After a defeat, Load Last Saved Game appears and loads the newest manual save ("34 : lls199", made after a Quick Save), not the defeat. A lit NEW row keeps its amber frame. The reason line sits clear of the frame line. The terminal: no red box, "[Leave.]" is the last option and its digit leaves, Escape leaves, and a refusal prints in the transcript. Someone sent home isn't drawn, and an Add shows one look |
| 7 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185 line for line, with "A fight begins." once. Regression: Save (slot 35, "reg199"), Escape then F4 (one quick save), Load, and a fight to its end |

## Small

- Rows end 4 px inside the list line, not 6 (item 1).
- The terminal's last option reads "[Leave.]." with a doubled full stop.
- "[Continue]" has no full stop while "[Leave.]" and "[Interrupt.]" do.
- The "6 → 4" preview appears while a path on the board is hovered, not while the Move slot itself is (`k2_hud.dart:263`). I read that as intended; MAIN to confirm.

## Not reached

- A companion down at exactly 0 (I only got −2).
- The gear slot dimming (Fight Nine carries nothing usable: "gear — nothing to use").
- "Reactions (out of turn): none" after spending, and the no-pool line in a fight (party-lock-bed has no enemies).

Known and not filed: the typed-reply row's number and digit typing; consoles opening only from the menu; three HUD portraits for a party of four; Force Deflection defaulting to Always; no K2 capture of the combat bar.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
