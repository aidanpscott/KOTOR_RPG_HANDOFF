# TEST 191: level-up and multiclass

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-191/` (MAIN_WORK `98ffd885`). The step-by-step log is `TEST/reports/191-running-log.md`.

## Build

App `46b7cab`, git archive from my own clone. `gate.py --at 46b7cab`: "FOR TESTER — CORE at 46b7cab, 4923 tests, 0 failed"; ARCHIVE last green at 46b7cab. Lodestar `fec65ecb1753d014818df55819a78fb0d1c21bc7` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `5ac3d20`; check_shelf clean. The build (9.8 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Authored characters, each one `character.xp-awarded` short of a level (specs in `notes/fixtures/specs191/`):
- **Sol Six**: Soldier 6, takes Jedi Guardian at 7.
- **Con Five**: Consular 5 holding Force Aura and Burst of Speed, levels to 6.
- **Mix Five**: Consular 3 / Guardian 2, takes Guardian to 6.
- **RX-191**: Battle droid Machinist 1, levels to 2.

## Summary: most pass; two findings that matter

| # | Check | Result |
|---|---|---|
| 1 | TEST 190's fixes | **PASS** except one small gap. Skill Bonuses count live (0→1→2→1→2). The upgrade shows only the class's line, inside the row, on both routes. The droid Model page is a K2 list page with the picture box. Story takes keys at once. A Soldier's tabs have no Forms or Powers. Cancel keeps the species, the +2s, the racial skill, the chassis and the model. "Training Lightsaber", "Parts", "Armor", "Defense" on chargen and level-up pages. **Small finding**: the programming pane shows the grant and aptitude with no cost, but **no chassis line** |
| 2 | Level-up layout | **PASS**: Auto Level Up dimmed on the sheet. The Class page comes first, titled "Level Up"; Cancel there leaves level-up, and hub Back returns to it with the class still lit. A droid gets the Force classes refused. The hub has numbered rows with K2's gaps, only the steps this level grants, and Attacks dimmed. Accept sits beside Back, dim until every choice is done. K2's granted popup appears. The Forms page appears at Force level 6 (Con Five) |
| 3 | Multiclass | **PASS for Sol Six**: after Guardian 7, a Force pool (18 of 18), Form I held plus one pick, 2 powers. Class skills from both classes are gold. Saves are summed per class (Soldier 6 5/2/2 + Guardian 1 2/2/1 + modifiers = +9/+6/+4). Vitality 52 → 60 (d10 6 + CON 2). Both classes use d10, so this character can't show which die was used. **FAIL for Mix Five**: Consular 3 / Guardian 3 reaches Force level 6 with **no Forms step at all** (finding 2) |
| 4 | Arrows at 6 | **FAIL**: no Aura → Force Shield arrow, because Force Shield is shown **refused** during the level-up to 6 (finding 1). Burst of Speed → Knight Speed correctly shows none |
| 5 | Dice, regression | **PASS**: the replay matches TEST 185 pixel for pixel. Escape > Save (slot 25), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings, most important first

1. **Level-up checks "Character Level N" against the old level.** Con Five, levelling 5 → 6 and holding Force Aura, sees Force Shield ("Character Level 6 / Force Aura") and Heal ("Character Level 6") shown refused, with Add Power dimmed (`i04a`, `i04b`). So level-6 powers can't be taken on the level that unlocks them, and the Aura → Shield arrow never shows. Sol Six, levelling 6 → 7, saw Heal open, which fits the same cause.
2. **No form pick at Force level 6 by multiclass.** Consular 3 / Guardian 3: the hub rows are 1 Skills, 2 Powers, 3 Attacks, with no Forms (`i03f`). Single-class Con Five did get the Forms page at Force 6.
3. Small: the programming pane has no chassis line. On level-up Forms, Recommended is dimmed (on chargen Forms it's lit). The hub's save cells read 5/2/2 (base only) while the in-game sheet reads +7/+4/+3.

## For MAIN

- A level-6 Consular, and Mix Five at 6, are granted "Unarmed Specialist I" and one entry named "Unarmed Specialist II-VIII". Is that right?
- Sol Six's popup at 7 also listed Squad Tactics, Improved Squad Tactics, Both Hands and Improvised. My authored Soldier never had those recorded, so I take it as the app catching up missing grants, not a defect.

Known and not filed: level-up Skills and aptitudes, prestige classes on the level-up list, the model frame, the Attacks page, the in-game sheet's "Armour", missing pictures.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
