# TEST 187: TEST 186's fixes, forms, class features at their levels, and the grids

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-187/` (MAIN_WORK `72903c36`). The step-by-step log is `TEST/reports/187-running-log.md`.

## Build

App `fa7fb60`, git archive from my own clone. `gate.py --at fa7fb60`: "FOR TESTER — CORE at fa7fb60, 4232 tests, 0 failed"; ARCHIVE last green at fa7fb60. Lodestar `c172e5863f0e07b12fff911aa77b66a936b38b0b` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `bcf7bc7`; check_shelf clean. The build (9.7 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

## Summary: every item passes; two small findings

| # | Check | Result |
|---|---|---|
| 1a | Icon tint | **PASS**: Feats beside L3-07 and Powers beside L2-08 now share K2's dim tint, and the lit first cell is no brighter than its neighbours. A held feat (Determination) draws bright with a lit border, as K2's held feats do |
| 1b | Inspire Followers II | **PASS**: its cell, read by eye: "Inspire Followers II / Light Side Power / Point Cost 12 / Prerequisites: Officer 5, Inspire Followers I". It was always there. **My TEST 186 note was an OCR misread; I withdraw it** |
| 1c | "None." | **PASS**: a Human's attribute panes end after the text. A Twi'lek's end with "+2 Charisma, −2 Wisdom." |
| 1d | Name keys | **PASS for the keys**: with `xdotool key`, BackSpace, Delete, Home, End, Left and Right all edit correctly. `xdotool type` of a backspace character does nothing, which is expected because it sends text, not a key. **Finding below**: after a click, the caret is invisible |
| 2a | Form I | **PASS**: the Consular gets K2's "You have been granted the following feat(s) this level." with "Determination (Form I)". It is held and lit on the grid, and its pane reads correctly. The Guardian gets Force Jump and Determination |
| 2b | One more form | **PASS**: Aggression (Form IV) takes the form slot. A second form is refused (Add Feat dim), but with no reason shown. The slot is form-only (it refused Blindside). OK with it unspent gives "You have gained new feats. You must use "Add Feat" to select your new feats before continuing." |
| 2c | Soldier | **PASS**: all 10 non-held forms are refused (Remaining unchanged). A control feat was taken at once, so the check could see a change |
| 2d | Guardian | **PASS**: forms II–VII can be taken; Force Affinity, Focus, Mastery and Potency are refused |
| 3 | Class features (PT-239) | **PASS**: a level-1 Bounty Hunter gets no grant at all (no Quarry); a level-1 Soldier gets only Squad Tactics (no Both Hands); a level-1 Smuggler gets Smuggler's Luck, Quickdraw and Killer's Instinct. Level-up was not reached (known list) |
| 4 | Grids | **PASS**: Force Sleep starts its own row in column 1, under the Force Stun row; Force Static Field does the same under Stun Droid. No row on any of the six Feats pages starts with an empty cell (pixel check). The Powers re-sweep gives 101 powers, each in one cell |
| 5 | Dice, regression | **PASS**: the dice replay is pixel-identical to TEST 185. Escape > Save, F4 (one quick save), Load and a fight to its end all work |

## Findings

1. **The name field's caret is invisible after a click.** Clicking in the field moves the real insertion point to the click (a centre click on "Sura Sarn" then "X" gives "Sura XSarn"), but the drawn "_" stays at the end. The next BackSpace deletes a letter the player can't see is targeted (`i01d-name-*`).
2. **Quickdraw has no icon cell** in the Smuggler's granted list: no icon and no empty frame. Smuggler's Luck and Killer's Instinct both show theirs (`i03c`).
3. Small: a second form is refused with no reason in the pane. Some column-1 feat cells are empty frames (feats without icons, as in TEST 185).

Known and not filed: Entry, Class, our own steps, Attacks, level-up, in-game frames, the Mire and Contagion pictures.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
