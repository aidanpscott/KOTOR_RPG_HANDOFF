# TEST 188: TEST 187's fixes, the Forms step, and the arrows

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-188/` (MAIN_WORK `8246ca6a`). The step-by-step log is `TEST/reports/188-running-log.md`.

## Build

App `9b30272`, git archive from my own clone. `gate.py --at 9b30272`: "FOR TESTER — CORE at 9b30272, 4258 tests, 0 failed"; ARCHIVE last green at 80355dd. Lodestar `181ac71940854923a7f2c3a71aa4d1276cddc03c` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `5ac3d20`; check_shelf clean (32 rules files, 118 blueprints). The build (200 s, most of it fetching the new Lodestar) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

## Summary: everything passes but one item

| # | Check | Result |
|---|---|---|
| 1a | Name caret | **PASS**: the "_" follows the caret: a click at the start gives "_Abcdef Ghijk", the middle "Abcde_f Ghijk", the end "Abcdef Ghijk_". Left ×3, Home, Right ×2 and End all move it |
| 1b | Granted lists | **PASS**: all 19 base classes at level 1. Quickdraw now shows K2's empty slot. Every entry in every list has a visible cell. Classes with grants: Soldier, Scout, Smuggler, Engineer, Machinist, Treasure Hunter, Medic, Brawler, Saboteur, Guardian, Sentinel, Sith Assassin. No grant at level 1: Bounty Hunter, Marksman, Agent, Duelist, Consular, Inquisitor, Warrior |
| 1c | Remaining 0 | **PASS** on Feats and Forms: Add keeps its normal look and pressing it changes nothing; a refused pick shows Add dimmed (Armour Proficiency: Heavy, Force Mastery). Powers wasn't tried at 0 |
| 2a | Jedi steps | **PASS**: thirteen in the ordered sequence, no scrolling. Tabs: Basic Info, Character, Skills, Feats, Forms, Attacks, Powers |
| 2b | Soldier steps | **PASS**: eleven steps; no Forms and no Powers; Attacks follows Feats |
| 2c | Forms page | **PASS**: the seven lightsaber forms on top, the four Force forms below and refused. Form I is held and one pick is open. Recommended took Moderation for the Consular and Contention for the Sith Assassin, both as FORMS-01 §2.4 says. The Forms tab lists Determination and the chosen form |
| 2d | Reopen Forms | **FAIL (small)**: the choice is kept (Remaining 0), but the page **opens on Determination, not the chosen form** (twice). Changing the form with later steps done warns and clears Powers onward; with nothing done after Forms, there is no warning, because nothing would be lost |
| 2e | Save and load | **PASS**: after Play, F4, kill and Continue, the save holds `character.form-taken {id: form_ii_contention, at_level: 1}`. Forms don't show on the in-game Abilities screen (in-game frames, known) |
| 3 | Arrows | **PASS**: no arrow anywhere on Feats or Powers at creation. Taking Armour Proficiency: Light adds one arrow, Light → Medium, and none to Heavy (refused). No arrow points to a refused tier or joins two unheld tiers. The level-6 Consular case was not reached (level-up) |
| 4 | Dice, regression | **PASS**: the dice replay matches TEST 185 pixel for pixel. Escape > Save (slot 22), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings

1. **Reopened Forms opens on Determination** instead of the chosen form (`i02b-reopen-opens-on-determination`).
2. Small: at 1920 the "Basic Info" and "Character" tab labels nearly touch. Many class feats granted at level 1 have no icon yet: Terrain Sense, Field Override, Jury Rig, Read the Ruin, Triage, Field Surgery, Nothing In My Hands, Salvage Charge and Vanish all show empty slots (correct per the fix, just without art).

Known and not filed: Entry, Class, our own steps, the Attacks page, level-up, in-game frames, the Mire and Contagion pictures.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
