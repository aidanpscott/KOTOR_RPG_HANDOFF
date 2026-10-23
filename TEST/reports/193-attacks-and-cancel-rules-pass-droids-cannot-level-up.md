# TEST 193: the Attacks page, Cancel and spending, Force +12, Watchman, droid upgrades

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-193/` (MAIN_WORK `cd37476d`). The step-by-step log is `TEST/reports/193-running-log.md`. **The severe finding was sent ahead: `TEST/reports/193-SEVERE-droids-cannot-level-up.md` (HANDOFF `ce7238e`).**

## Build

App `35c2893`, git archive from my own clone. `gate.py --at 35c2893`: "FOR TESTER — CORE at 35c2893, 4985 tests, 0 failed"; ARCHIVE last green at 35c2893. Lodestar `7af61b9384e775d6c5f4914e5521b8dea2a72d85` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `bf52834`; check_shelf clean (33 rules files, 125 blueprints). The build (9.7 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Characters:
- Through chargen: Con Twenty (Human Jedi Consular, WIS 16 / CHA 14); a Quara Sith Warrior at WIS/CHA 8 (shown as 6 after the −2); a Human Soldier at STR 8.
- Authored (`specs193/`): Watch Two (Guardian 6, Stealth 8, XP for 8) and RX-193 (Battle droid Machinist 6, XP for 7).

## Summary: most pass; one severe failure

| # | Check | Result |
|---|---|---|
| 1a | Level-up Cancel and Escape | **PASS**: Escape on the Class page leaves level-up. Escape on the hub goes to the Class page. Cancel there leaves with nothing written (still Guardian 6, 52 of 52). Escape on a spend page returns to the hub |
| 1b | Droid facts | **PASS**: Species, Chassis, Model, with no Subrace, on the level-up hub |
| 1c | No "Fly" | **PASS**: a human Soldier's Skills tab goes Demolitions, Intimidate, Medicine |
| 1d | Counts | **PARTIAL**: "Medpac" shows its 2 on the icon cell. **But** the Profession Bonus row still reads "Security Tunneler, ×2" |
| 2 | Force | **PASS**: the Quara has 12/12 at level 1; the Consular at 16/14 has 25/25. (An Arkanian Offshoot Sith Warrior at 8/8 shows 14/14. Vela went 51 → 63.) Watchman can be taken at character level 7. Its pool went 52 → 59 (+5 die + 2 CON). Watchman is d8 in the table, but one roll of 5 fits d8 or d10, so **d8 is not proven** |
| 3 | Droid upgrades | **PASS**: crossing class level 7 grants Droid Upgrade 2 and Plating Proficiency: Medium |
| 4 | Attacks | **PASS** for the layout and rules: K2's grid with no headings, grouped Ranged, Melee, Unarmed, Lightsaber, Stealth (142 names swept). Refused cells are red with their prerequisites in the pane. Shoot is drawn held. Recommended at chargen takes the class opening: Guided Strike (Consular), Power Attack (Quara at STR 18), Charged Shot (Soldier at STR 8). It's dimmed at level-up. OK with picks left gives the K2 "You have gained new attacks…" popup. A droid's grid shows only ranged rosters. Level-up has an Attacks row that holds Accept. **Findings**: authoring notes in panes, and the level-1 pick count (below) |
| 5 | Cancel and spending | **PASS**: Cancel leaves Attributes, Skills, Feats and Forms undone. Skills OK with points left gives K2's save prompt: Cancel stays, OK finishes. The 6 saved points (`character.skill-points-saved {points: 6}`) joined the next level's budget (12 = 6 + 6). Attributes OK with points left gives K2's "You must spend all of your points…" and stays |
| 6 | Dice, regression | **PASS**: the replay matches TEST 185 pixel for pixel. Escape > Save (slot 27), Escape then F4 (one quick save), Load, and a fight to its end |

## Findings, most important first

1. **SEVERE, sent ahead: a droid can't level up.** The level-up Skills step reads "This droid is on none of them. / this step cannot complete for a droid". OK is dead and Accept never lights. `play_screen.dart:2932` matches the species id "droid" against the droid skill ids ("droid-battle" …) and never reads the chassis.
2. **Authoring notes on screen in Attacks panes.** Combination: "Moved from the feats, 2026-10-19 (MAIN: an attack; the Brawler's starting attack:304, and attacks are not feats." (`attacks.toml:1750`). Volley of Bolts: "The source names this tier Multi-Shot." Barrage: "The source names this tier Whirlwind Attack."
3. **Pick counts at level 1 look high.** Remaining Attacks at chargen is 5 for a Consular and 6 for a Sith Warrior; the `classes.toml` progression gives `attack_picks` 1 and 2 at level 1. MAIN to confirm which is right.
4. Small:
   - "Security Tunneler, ×2" keeps the count in the text.
   - Jedi Watchman's description box is empty on the level-up Class page.
   - The hub's Attacks tab lists Strike and Shoot but not Jab, Punch or Kick.
   - The Recommended popup says "feat(s)" on the Attacks page.

Known and not filed: in-game frames and the store, missing pictures, Recommended dimmed at level-up and on Equipment and Background.

Skills: `verification-before-completion`. Kept small per the simplicity rule.

## Addendum: the droid retest on app 94a5615 (MAIN: severe fixed)

`gate.py --at 94a5615`: FOR TESTER, CORE 4988 passed, 0 failed; ARCHIVE green. Built from my own clone (9.8 s); the lock was unchanged; Lodestar `7af61b9` = lock = compiled. Screenshots: MAIN_WORK `c4fbd75f` (`media/screens/test-193b/`).

- **Battle Machinist 6 → 7 (RX-193): PASS.** The Skills page lists droid-battle's exact 15 skills with 6 points; then Attacks (1 pick); Accept gives "Machinist · 7, 44 of 51".
- **Astromech Scout 6 → 7 (T3-193): PASS.** Granted Droid Upgrade 2 and Plating Proficiency: Medium. Skills shows droid-astromech's 15 (Botany, Medicine, Pilot, Sleight of Hand; no Acrobatics or Athletics); Feats; Accept gives "Scout · 7, 45 of 52".
- **Remote Scout 6 → 7 (RM-193): PASS.** Upgrade 2 and Plating Medium granted. Skills shows droid-remote's 14 (Acrobatics, Medicine, Stealth; no Athletics or Intimidate); Feats; Accept gives "Scout · 7, 45 of 52".
- **No developer text** on any level-up page for the three droids.
- **The sheet's Species row reads "Droid"**, without the chassis. MAIN to say whether "names the species" means the chassis should show (the hub shows "Species Droid / Chassis Battle").
- **New finding:** the level-up hub's attribute cells leave out the chassis adjustments. RX-193's hub shows STR 12, CON 14, INT 12, CHA 10, while the sheet shows 14 / 16 / 10 / 8 (Battle +2 STR, +2 CON, −2 INT, −2 CHA).
- Small: a save refusal names the raw id: "A droid-astromech droid carries no vocabulator…". (That was my fixture's fault, giving an astromech a voice, but the wording shows on screen.)
- Your answer on the level-1 attack picks (rate + 4 credits) is noted; I won't raise it again.
