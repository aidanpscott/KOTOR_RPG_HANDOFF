# TEST 196: the TEST 195 fixes, the store ruling, and in-game batch 2

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-196/` (MAIN_WORK `9b181d46`). The step-by-step log is `TEST/reports/196-running-log.md`. Compared against `MAIN_WORK/media/study/pt2752/k2-ingame/`.

## Build

App `bb8bf48`, git archive from my own clone. `gate.py --at bb8bf48`: "FOR TESTER — CORE at bb8bf48, 5017 tests, 0 failed"; ARCHIVE last green at bb8bf48. Lodestar `240bc46` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `9706207`; check_shelf clean (33 rules files, 125 blueprints). The build (9.8 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Authored (`specs196/`, Store Bed): Lang Two (Twi'lek Soldier 1, Medium armour worn, XP for 2), Jedi Arm (Guardian 1 holding Form I and Form V), RX-196 (Battle droid Machinist 6, XP for 7). Also a Battle droid Machinist made through chargen, plus Frame One, Watch Four, Icon Nine and Dice One from earlier tests.

## Summary: most pass; four findings

| # | Check | Result |
|---|---|---|
| 1 | Level Up / Auto Level Up | **PASS**: shown when a level waits (Auto dim, Level Up lit), drawn over the portrait; hidden otherwise. Opens level-up on RX-196 |
| 2 | Purchase Gear counts | **PASS** for a Guardian: Weapons 25, Useable 12, Misc 5, Armor 2 (the two Padawan robes), Datapads and Quests empty. **Finding** for a Soldier (below) |
| 3 | Character Info | Experience/Needed numbers **PASS** (0/1000; 1000/0; 21000/0). Languages **PASS** for a Human. **Findings**: Twi'lek languages, gear notes, Defense reason, portrait gap (below) |
| 4 | Store prices | **PASS**: Medpac 40 / 22; Adrenal Strength (50) sells 27; Frag Grenade (100) sells 55, so 55% rounded down. In Stock reads "Infinite" buying and "—" selling. Seven tabs in K2's order, each filtering right, empty tabs shown |
| 5 | Abilities Forms tab | **PASS**: after Feats; each pane gives the form's name and "Lightsaber Form". No "Current stance" without a saber; no Forms tab for a character with no forms. "Current stance: Form I" with a saber equipped was **not reached** (my fixture has no saber) |
| 6 | Journal | **PASS**: "Active Quests By / Time / Name / Planet" with no Priority; Messages Log; Notes to the right of Close |
| 7 | Messages | **PASS**: tabs Filter, Dialog, Feedback, Combat, Effects; Effects shows Good and Bad side by side; Close returns to the Journal |
| 8 | Map | **PASS**: the areas-entered strip sits at K2's Return place, in K2's face and teal |
| 9 | Droid Attacks tab | **PASS**: a chargen Battle Machinist's hub Attacks tab lists Shoot alone (no Strike, Jab, Punch or Kick); no Forms or Powers tabs |
| 10 | Dice, regression | **PASS**: the replay matches TEST 185 (log md5 `6b13820a…`). Escape > Save (slot 30, "reg196"), Escape then F4 (one quick save), Load, and a fight to its end (total party defeat box) |

## Findings, most important first

1. **A Twi'lek has no Languages on Character Info, and Species reads the raw id "twi'lek"** (lower case). Frame One (Human) shows both correctly. I authored Lang Two with "twi'lek" because the author tool refused "twi-lek", while `species.toml:905` has `id = "twi-lek"`. So the lookup probably misses one of the two spellings. I didn't confirm this on a chargen-made Twi'lek.
2. **No gear note and no Defense reason on Character Info.** Lang Two wears Medium armour (Equip: Defense Bonus 4; the sheet's Defense is 16). Character Info shows neither line.
3. **A Soldier's Purchase Gear Armor tab lists only the two Padawan robes.** The order says a non-Jedi package's Armor tab lists its starting armour. (Tester Bolt, base rules; the Soldier's standard gear is Clothing.)
4. **The portrait doesn't meet the alignment bar.** On RX-196 (a real portrait), the bar ends at x 301 and the portrait starts at x 384: an 83 px gap at 1920. At 1280×720 the bar ends at x 206 and the portrait starts at x 256: a 50 px gap.

Small:
- The Map strip starts with a lower-case "map —" ("map — ⟨Market⟩"). The note strip above the board is empty with no up/down arrows (K2's capture has both); a01-market may simply have no notes.
- The level-up hub's portrait box is black for RX-196, though the sheet shows the portrait.
- In the store, the Vibroblade's In Inventory reads "0 + replaces Blaster Rifle".
- Soldier is refused for a droid with "A droid cannot take this class." I note it only in case that isn't intended.

Known and not filed: old frames on the HUD, Party, Options and Save/Load (batch 3); the store's gold is reasoned; no K2 capture for lit rows or the combat bar; list boxes 4–7 px short at the right; Level Up and Auto Level Up hidden while no level waits.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
