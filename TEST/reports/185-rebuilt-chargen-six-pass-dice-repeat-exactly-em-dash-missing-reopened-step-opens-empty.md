# TEST 185: a focused pass on the rebuilt chargen

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-185/` (MAIN_WORK `26d978eb`), one prefix per item. The step-by-step log is `TEST/reports/185-running-log.md`.

## Build

App `55f1a3f`, git archive from my own clone to `~/kotor-tester/builds/test185`. Gate at the hash: `python3 scripts/gate.py --at 55f1a3f` reads "FOR TESTER — CORE at 55f1a3f, 4058 tests, 0 failed, 8m50s at -j 3, peak 2010 MB, run 2026-10-19T07:41:41" and "ARCHIVE last green at fc89fec". The bare gate had read NOT FOR TESTER at the shared HEAD 5aab12e. MAIN ruled that 55f1a3f meets the rule (a clean CORE stamp, and ARCHIVE green at 1605653, after the dbc037c milestone). Lodestar `c172e5863f0e07b12fff911aa77b66a936b38b0b` = lock = compiled. Lens `5fe60a9c2be41852fd8818c1ca579a2077808d79`. Loom has no entry in the lock. Shelf `0fbb89a`; check_shelf clean on my data dir (118 blueprints). The build (9.7 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged. The bundle was launched outside it.

Characters: Dice One (Human Female Jedi Consular, made through the new chargen), a Twi'lek Female Soldier, a second Consular at 1280x720, and an authored "Icon Nine" holding the nine mod feats.

## Summary: six pass, two partial, one with findings

| # | Check | Result |
|---|---|---|
| 1 | Powers | **PARTIAL**: three columns, light and dark mixed, teal or red. The pane shows the side line, "Point Cost N", "Prerequisites:" with one line each, and "Restricted By Armor". Add Power becomes Remove Power, and Remaining Powers is a bare count. Force Crush, Force Enlightenment and Force Sight are not on the grid. Force Armor shows "Character Level 12"; Force Barrier (tier 2, no written level) shows "Character Level 6". OK with a pick unspent gives K2's "You have gained new powers. You must select your new powers before continuing." **Dominate Mind has no Point Cost line.** It opens on the first power, but I couldn't see a lit highlight on its slot |
| 2 | Feats, Attributes, Skills | **PASS**: Feats is the same grid with K2's arrows. All six attribute descriptions match §2; Dexterity and Charisma match word for word. Skills scroll, class and aptitude skills are gold, and the plus is gone at the cap (Alertness 4; Appraise 2 + 2 = 4; Awareness 0 with a +2 from species) |
| 3 | Portrait and Name | **PARTIAL**: Human Female shows 32 faces, all human women. **A Twi'lek woman gets an empty grid**, a "no portrait" circle in a non-K2 font, and an OK that goes through with no portrait at all. Name: K2's font with its "_" caret. Empty shows "A name is required." and OK is dead |
| 4 | Hub | **PASS**: twelve steps (eleven for a Soldier), no scrolling, no numbers. The current step is lit, finished ones teal, locked ones dim. Every tab opens. Skills lists all skills, 0 ranks included, with Rank / Bonus / Total. Basic Info has score and modifier in separate cells, Vitality 9/9 and Force 14/14. Long text stays inside the panel |
| 5 | Going back | **PASS**: change + OK gives "Every step after this one will be lost. Proceed?". OK clears Feats onward; Cancel clears nothing. Leaving with Cancel clears nothing. Re-entering the same choices gives no warning. Locked steps don't open. **But a reopened step opens empty** (finding 2) |
| 6 | Icons | **PASS**: Mind Trick and Force Distraction have their own icons, and Beast Control shows Beast Trick's. Killer's Instinct, Emergency Reboot, Payday, Sadism, Sated, Constancy and Respite draw their mod icons; Shield Boost and Last Stand draw K2's empty slot. These are granted feats, so I saw them on an authored character's in-game Abilities > Feats |
| 7 | Dice | **PASS twice**: three launches from one Quick Save, with the same moves. Initiative (19, 13, 11, 10, 2) and every roll through round 3 matched, and the log crops are pixel-identical (same md5) |
| 8 | Look across pages | **Findings**: K2's bitmap font draws no em dash on any rebuilt page (finding 1). At 1920 the feat pane's text runs to the edge, and each attribute pane ends with a bare "None." line. At 1280x720 every rebuilt page fits with nothing new; the portrait grid's fifth row is cut by its scroll edge at both sizes. In-game at 1920, End Turn sits over "Eight hours of meditation" and cuts it to "Eight ho" (in-game frame, not yet rebuilt) |
| 9 | Regression | **PASS**: Play, Escape > Save (slot 19), F4 (one quick save), and loading the slot all work. A fight went to its end (a total party defeat, with its box) |

## Findings, most important first

1. **K2's bitmap font has no em dash.** Wherever the text has "—", the page shows a gap. Improved Heal reads "14 metres    7 squares radius" (the source has "14 metres — 7 squares"). Mysticism reads "The Force as a subject of study   traditions, relics …" (`i01e`, `i02e`). The rules text uses "—" widely, so this reaches many descriptions.
2. **A reopened step opens empty.** Reopening the finished Skills step showed every rank at 0 and Remaining Points 16. Leaving "with no change" therefore means re-entering every point (OK stays dim until all are spent) or pressing Cancel. Cancel and re-entered identical choices both keep everything, as ruled (`i05a`).
3. **A species with no matching face gets no portrait.** A Twi'lek woman: empty grid, "no portrait" in a non-K2 font, and OK accepted, leaving the hub's portrait box empty (`i03b`). MAIN to rule: fall back to another face, or refuse OK.
4. **Dominate Mind shows no "Point Cost" line**; every other power of the 97 does (`i01d`).
5. Small: the first power's slot isn't visibly lit when the page opens. Basic Info reads "Defense", where the approved texts spell it "Defence". Most skills show an empty icon box in the hub's Skills tab. The hub's Feats tab lists only the picked feat, so does a Consular get any granted feat at level 1? After clicking the dead name OK, typing goes nowhere until you click the field again. Killing the app mid-fight still writes the fight into the character's save and Auto Save (the Quick Save rewinds it).

Known, not yet rebuilt, seen: Entry, Class, Species, Gender, Origin, Background, Equipment and Story are as before. Attacks is a dim placeholder. Random Name gave a male name to a female character. A level-1 Consular (9 HP) goes down to the first gunman shot (11 damage).

## How it was run

The Powers and Feats grids were swept by clicking down each column and reading the pane, page by page (97 powers, 89 feats; `run/powerscan2.sh`, `run/featscan.sh`). The dice runs used a fixed script (`run/dicerun.sh`): the same seven keys into the gunman, Enter on any box, Space otherwise, stopping at round 3. The 720 pass used a fresh window sized at launch.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
