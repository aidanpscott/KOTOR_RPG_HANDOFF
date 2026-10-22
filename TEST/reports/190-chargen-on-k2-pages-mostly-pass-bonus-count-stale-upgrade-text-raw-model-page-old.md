# TEST 190: all of chargen on K2's pages

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-190/` (MAIN_WORK `40d999e3`). The step-by-step log is `TEST/reports/190-running-log.md`.

## Build

App `c9946f8`, git archive from my own clone. `gate.py --at c9946f8`: "FOR TESTER — CORE at c9946f8, 4295 tests, 0 failed"; ARCHIVE last green at c9946f8. Lodestar `181ac71` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `5ac3d20`; check_shelf clean. The build (10.0 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Characters made end to end, each played, saved with F4, killed and continued: **Story One** (Human Female Jedi Consular), **Twi Scout** (Twi'lek Female Scout), **RX-190** (Droid, Battle chassis, Machinist), **Quara Four** (Aqualish Quara Male Sith Warrior). A fifth, **Bith Seven** (Bith Jedi Consular), was made at 1280x720.

## Summary: most items pass; five findings

| # | Check | Result |
|---|---|---|
| 1a | Description bars | **PASS**: every box I saw has K2's bar. Quick's reason (it overflows) gets a short thumb, and its last line can be reached; Custom's (it fits) gets a full-track thumb |
| 1b | Droid refusal | **PASS**: "A droid chassis holds no Force class." with a capital and a full stop; OK dead |
| 1c | Pick order | **PASS** on Powers, twice: Force Valor picked first, then Burst of Speed (higher on the grid); reopen lights Force Valor. Every class I made has one feat pick and one form pick at level 1, so on Feats and Forms the first pick can't differ from grid order; both reopen lit on the single pick |
| 2 | Species | **PASS** for the page, the picture box (empty, known), Subrace with Back (Aqualish), Chassis with Back (droid), Racial Skill (nothing lit, OK waits). Skill Bonuses **behaviour PASS**: judged by the row outlines and OK, two different skills are needed, touching one again gives it back, and a third isn't taken. **FINDING**: the pane's "Skill Bonuses: N of 2" line is stale (finding 1) |
| 3 | Gender / Voice | **PASS**: Male and Female; a droid gets Masculine, Feminine and Neither. One press commits, and reopen shows the choice |
| 4 | Origin | **PASS**: Homeworld, then the world's skills under stratum bars ("Lower City / Aptitude: Intimidate +2" from one touch), then Upbringing. Back works. No authoring marks seen. Notes: after Back and OK, the skills page lights the first skill again, not the earlier pick; Upbringing's description box is empty |
| 5 | Background | **PASS**: professions show the grant, aptitude and detail ("melee weapon / Aptitude: Beast Handling / a better melee weapon"); the first line is a bare lower-case word. Programmings show "From: Slicer / Grant: 2 Computer Spikes / Cost: 500cr", with no aptitude line, and "Cost: 500cr" may not be meant for the player |
| 6 | Equipment | **PARTIAL**: Standard Gear rows, with "1 tier-1 saber upgrade" dimmed. Profession Bonus makes OK wait. Purchase Gear opens K2's store with Credits 200; buying a Short Sword gives Credits 180 and In Inventory 1; Close returns, and the route becomes "Purchase Gear: Short Sword, 180 Credits". **FINDING**: the upgrade pick shows the raw table, not plain words (finding 2). Only the lightsaber row has an icon |
| 7 | Your Story | **PASS** for the page, Try another and CLEAR, and the keys after a click (Left, BackSpace, Home, Delete and End, with the "_" following). **FINDING**: before any click, the "_" is drawn but keys do nothing (finding 4) |
| 8 | Minus signs | **PASS**: hyphens everywhere ("-2 Wisdom", "8 (-1)", "-2 Constitution") |
| 9 | Look, 1920 and 1280 | **PASS** for the chargen pages: nothing clipped or overlapping, K2 fonts, no "Defence". Exceptions are findings 2, 3 and 5 |
| 10 | Dice, regression | **PASS**: the replay matches TEST 185 pixel for pixel. Escape > Save (slot 24), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings, most important first

1. **The Skill Bonuses count is stale.** The pane can read "Skill Bonuses: 2 of 2" with one skill chosen and OK dim (`i02b-bonus-count-stale`). `K2ListPage` keeps its items in `late final _all` (`k2_list_page.dart:104`), so a description that holds a count never refreshes after the first build. Any other page that puts live state in a row's description would do the same.
2. **The melee-upgrade bonus shows the raw table.** It reads "Your class's own melee upgrade — Soldier → Long Sword + Short Sword or a Double-Bladed Sword; Scout → Double-Bladed Sword; Duelist → Vibrosword + Vibroblade", for a Consular as well as a Scout, instead of the plain line for the character's own class. On the Purchase route its row runs out of the list and over the frame on the right (`i06b`, `i06d`).
3. **The droid's Model page is still the old page** (plain font, empty right pane), not a K2 page (`i02e`).
4. **Story: keys don't reach the box until it's clicked**, though the "_" is drawn from the start.
5. **The store page** (Purchase Gear) has its right-hand labels clipped on the left ("nothing selected", "n Cost", "n Inventory"), a non-K2 font, and very small text at 1280x720. It may count as an in-game frame; filed so MAIN can decide.

## Notes for MAIN

- **Quara Four, a level-1 Sith Warrior with WIS 8 and CHA 8, reads "force 0 of 0" in play** while holding two powers.
- The Scout's hub has no Forms or Powers steps, but its tabs still show Forms and Powers.
- Cancel from Class back to Species forgets the species pick (as in TEST 184).
- Equipment text: "Training Lightsaber red" (a stray lower-case colour), "1 Parts", "Armor" in the gear pane against "Armour" in the feats, "Security Tunneler, ×2".

Known and not filed: missing pictures, the Attacks page, level-up, in-game frames, Recommended on Equipment and Background.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
