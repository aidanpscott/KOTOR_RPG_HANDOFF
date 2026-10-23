# TEST 192: TEST 191's fixes and the new level-up work

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-192/` (MAIN_WORK `692cfe36`). The step-by-step log is `TEST/reports/192-running-log.md`.

## Build

App `71a7386`, git archive from my own clone. `gate.py --at 71a7386`: "FOR TESTER — CORE at 71a7386, 4954 tests, 0 failed"; ARCHIVE last green at 71a7386. Lodestar `50e3f93444bec6352cf626c95a65325117155821` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `4795bc3`; check_shelf clean (123 blueprints). The build (9.8 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Fixtures (`notes/fixtures/specs192/`):
- **Con Five**: Consular 5 holding Force Aura, levels to 6.
- **Mix Five**: corrected per Coder; Guardian is added with 0 levels and then levelled twice, so she's Consular 3 / Guardian 2. The sheet confirms "Jedi Consular 3 / Jedi Guardian 2 · level 5".
- **Mix Six**: Consular 3 / Guardian 3, takes Guardian 4.
- **Apt Two / Apt Three**: Taris (Intimidate aptitude) and Hunter; Apt Three also records the aptitude grant choice.
- **Tri Six**: Soldier 2 / Scout 2 / Smuggler 2.

## Summary: every TEST 191 fix passes; one new finding

| # | Check | Result |
|---|---|---|
| 1a | Level-6 gates | **PASS**: Con Five, levelling 5 → 6: Force Shield ("Character Level 6 / Force Aura") and Heal can be taken, and the **Aura → Force Shield arrow shows**. Force Armor (Character Level 12) stays refused, and Burst → Knight Speed has no arrow |
| 1b | Forms by multiclass | **PASS**: Mix Five (C3/G2 → G3) gets a Forms row; Recommended is lit and took Resilience, the Guardian's third form under FORMS-01 §2.5 (the Consular's is also Resilience). Mix Six (C3/G3 → G4) has no Forms row. Con Five's Recommended took Resilience too |
| 1c | Hub saves | **PASS**: hub 6/4/7 = sheet +6/+4/+7 |
| 1d | Programming pane | **PASS**: all nine programmings show "Chassis: Any chassis", plus their items and aptitude |
| 1e | Unarmed Specialist | **PASS**: a level-6 Consular is granted "Unarmed Specialist I" and "Unarmed Specialist II" as separate entries, each with its own icon |
| 2a | Model frame | **PASS**: the level-up hub shows Species, Homeworld, Upbringing and Background under the portrait; the droid's Voice page shows Origin, Background and Languages. **Small**: on the droid, the chassis ("Battle") appears under Subrace and the model under Chassis, which looks shifted by one row |
| 2d | Level-up aptitudes | **PASS**: Intimidate (homeworld) reads "Class Skill / Point Cost 1 / Aptitude: homeworld" and stops at rank 3 (+2 bonus = cap 5). With the profession's aptitude chosen, Beast Handling reads "Class Skill / Point Cost 1 / Aptitude: profession" |
| 2e | Droid programming | **PASS**: items and aptitude on every programming |
| 2f | Class page | **PASS**: a fourth class is refused with "Three classes, maximum." and OK is dead. Prestige prerequisites show (Jedi Watchman: "Character Level 10 / Any Force base class 6 / Stealth 8"; the level-10 gate is known) |
| 2g | File names | **PASS** in every grant I saw |
| 2b, 2c | Watchman d8 pool; droid upgrade tiers | **Not reached**: no Watchman can be reached while the level-10 gate stands, and I didn't author a droid at a tier boundary |
| 3 | Dice, regression | **PASS**: the replay matches TEST 185 pixel for pixel. Escape > Save (slot 26), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings

1. **There's no way out of level-up once a class is chosen.** On the hub, Back goes to the Class page, Cancel there goes back to the hub (as specified), and Escape does nothing. The only exit is to finish and Accept (`i02-no-way-out`). Before a class is chosen, Cancel does leave. To get out, I had to level Mix Six to 7.
2. Small: "Fly" appears on the level-up Skills list, though its pane says "Beast only. Does not appear on a character's skill list." The droid model frame's rows look shifted (above). Words: "2 x Advanced Repair Kit" next to "2 Medpacs"; "a fragment of an old puzzle" lower case.

Known and not filed: the Force pool rules, the Attacks page, in-game frames and the store, missing pictures, the level-10 prestige gate.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
