# TEST 186: the TEST 185 retest and the new Powers grid

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-186/` (MAIN_WORK `224d4be8`), one prefix per item. The step-by-step log is `TEST/reports/186-running-log.md`.

## Build

App `9386aee`, git archive from my own clone to `~/kotor-tester/builds/test186`. `python3 scripts/gate.py --at 9386aee` reads "FOR TESTER — CORE at 9386aee, 4122 tests, 0 failed" and "ARCHIVE last green at 9386aee". Lodestar `c172e5863f0e07b12fff911aa77b66a936b38b0b` = lock = compiled. Lens `5fe60a9c2be41852fd8818c1ca579a2077808d79`. Loom has no entry in the lock. Shelf `3662ad4` (grid_order); check_shelf clean on my data dir (118 blueprints). The build (9.6 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

## Summary: every TEST 185 fix passes; one comparison does not match K2

| # | Check | Result |
|---|---|---|
| 1a | Dominate Mind | **PASS**: "Point Cost 25" |
| 1b | Lit first slot | **DOES NOT MATCH K2's L2-08**. K2 draws every icon dimmed grey, and its first slot (Heal) is no brighter than its neighbours; only the borders differ. Ours draws the icons in full colour, with the first slot's icon bright white. So ours is a stronger mark than K2's, and the whole grid is brighter than K2's (`i01b`, K2 left, ours right) |
| 1c | Portraits | **PASS**: a Twi'lek woman gets K2's "?" placeholder, already selected; OK goes through, and the hub shows the "?". An Echani woman (subrace Eshan) gets 32 human women; the man, 31 human men. An Astromech gets its two T3 faces. In the code, `portraitsFor` always returns at least the placeholder |
| 1d | Reopen every step | **PASS**: all ten finished steps (Gender, Portrait, Origin with its upbringing, Background, Attributes, Skills, Feats, Powers, Equipment, Name) reopened with their saved choices. OK at once gave no warning and Play stayed current. Changing the feat (Armour Proficiency: Light to Dueling) gave the warning, and OK cleared Powers onward. Changing Gender did the same |
| 1e | Em dash | **PASS**: "14 metres — 7 squares radius"; "Single-weapon combat discipline — the counterpart …" |
| 1f | "Defense" | **PASS**: Basic Info, the Dexterity description ("a character's Defense"), Dueling, Burst of Speed. No "Defence" seen on a rebuilt page |
| 2 | The new grid | **PASS**: opens on Heal, and the rows begin Heal, Force Aura, Burst of Speed, Force Valor, matching L2-08. All 6 pages swept: 101 powers, none twice. Force Sleep and Force Static Field each sit under an empty first cell, the row below Force Stun and below Stun Droid. Beast Control > Beast Confusion share a row; Beast Confusion's pane lists "Beast Control". Shutdown, Overload, Force Sleep and Force Root have their own icons. A level-up grid was not reached (known list) |
| 3 | Look across pages | **PASS**: at 1280x720 every rebuilt page fits, in K2's fonts, with nothing clipped or overlapping |
| 4 | Dice | **PASS**: two launches from TEST 185's Dice One Quick Save are pixel-identical to TEST 185's run |
| 5 | Regression | **PASS**: Escape > Save (slot 20); Escape then F4 rewrote the one quick save; loading the slot works; a fight ran to its end |

## Findings and notes

1. **The lit first slot is brighter than K2's** (1b above). K2 dims every icon and marks the first slot only faintly. Ours shows full-colour icons and a white first icon.
2. Beast Confusion's prerequisites include "Any Prestige Class" while a level-1 character can see it. Check that this is wanted at chargen.
3. The grid has Inspire Followers I, III, IV and V, but no II.
4. Each attribute description still ends with a bare "None." line.
5. Name: typing "Retest Six" over the pre-filled name gave "Retest Six Quell". BackSpace doesn't clear the field (known from the droid run), so the old surname stayed.

Known and not filed: Entry, Class, our own steps, the Attacks step, level-up, in-game frames. Force Mire and Force Contagion still share their old pictures.

## How it was run

The grid was swept cell by cell (`run/gridscan.sh`, `run/pagemap.sh`). Reopening used `run/reopen.sh`, which opens a step, presses OK and screenshots the hub. The dice ran `run/dicerun.sh` from the TEST 185 save. The 720 pass used a fresh window sized at launch.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
