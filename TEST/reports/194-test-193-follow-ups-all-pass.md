# TEST 194: the TEST 193 follow-ups

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-194/` (MAIN_WORK `12fa2e0c`). The step-by-step log is `TEST/reports/194-running-log.md`.

## Build

App `fcf7d0c`, git archive from my own clone. `gate.py --at fcf7d0c`: "FOR TESTER — CORE at fcf7d0c, 4993 tests, 0 failed"; ARCHIVE last green at fcf7d0c. Lodestar `240bc46bf5d1478b7648b1bd899139cb77914de0` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `3c9ae3e` (attacks.toml without authoring notes); check_shelf clean (33 rules files, 125 blueprints). The build (9.7 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Characters: a Human Consular made through chargen. Authored (`specs194/`): Off Six (Soldier 6, Alertness 8), Watch Four (Guardian 6, Stealth 8), RX-194 (Battle droid Machinist 6), and T3-Voice (an astromech given a voice on purpose).

## Summary: all seven items pass

| # | Check | Result |
|---|---|---|
| 1 | Attack panes | **PASS**: all 142 attacks lit, and each pane scrolled to its end (OCR in `i01-attack-panes.tsv`); no authoring notes. Combination, Barrage, Volley of Bolts, Quick Attack and Riposte are all clean |
| 2 | Counts | **PASS**: "Security Tunneler" with 2 on its icon and "2 Security Tunnelers" in the pane; "Medpac" with 2 on its icon and "Medical Supplies / 2 Medpacs" in the pane |
| 3 | Attacks tab | **PASS**: Strike, Shoot, Jab, Punch and Kick, then the picks. A droid's tab wasn't checked this time; its grid showed Shoot held in TEST 193 |
| 4 | Recommended popup | **PASS**: "The following attack(s) have been recommended." |
| 5 | Droids | **PASS**: the level-up hub's attributes equal the sheet's (Battle: STR 14, DEX 14, CON 16, INT 10, WIS 12, CHA 8). The sheet's Character Info reads "Species Droid / Chassis Battle / Model War Droid Mark I", with no Subrace. The refusal reads "An Astromech droid carries no vocabulator and this one has a voice." |
| 6 | Prestige panes | **PASS**: Officer (met): "Prerequisites: / Soldier 6 or Agent 6 / Alertness 8 / Hit Die: d8", OK lit. Watchman (met): "Any Force base class 6 / Stealth 8 / Neutral or a light band / Hit Die: d8 / Force Die: d8". Unmet entries show only their unmet lines, with OK dead: Shadow Hunter "Stealth 8 / Killer's Instinct / Hit Die: d8", Juggernaut "Armor Proficiency: Heavy or Droid Upgrade 3 / Hit Die: d10", Weaponmaster "Weapon Focus: Lightsaber / Hit Die: d10 / Force Die: d6". Nothing prints twice |
| 7 | Dice, regression | **PASS**: the replay matches TEST 185 pixel for pixel. Escape > Save (slot 28), Escape then F4 (one quick save), Load, and a fight to its end |

No new findings.

Known and not filed: prestige descriptions, in-game frames and the store, missing pictures, Recommended dimmed at level-up and on Equipment and Background.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
