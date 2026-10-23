# TEST 193 running log (draft, text only)

Started 2026-10-23 (after the K2 capture hold was lifted). Tester, Xvfb :2, own data dir.
Known, don't file: in-game frames and store, missing pictures, Recommended dimmed at level-up and on Equipment/Background.

## Build
- App 35c2893, git archive from my own clone to builds/test193. Built through the lock: 9.7 s. pubspec.lock unchanged.
- Gate: "gate.py --at 35c2893" -> "FOR TESTER — CORE at 35c2893, 4985 tests, 0 failed, 11m51s at -j 3, peak 1718 MB"; "ARCHIVE last green at 35c2893".
- Lodestar 7af61b9384e775d6c5f4914e5521b8dea2a72d85 = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf bf52834 (as ordered). check_shelf: 33 rules files, 125 blueprints, identical.
- Fixtures (specs193/): Watch Six (Guardian 6, Stealth 8, Force Aura, XP for 7), RX-193 (Battle droid Machinist 6, XP for 7; Droid Upgrade 2 is "Granted at level 7").

## Items

### Chargen: Human Female Jedi Consular "Con Twenty-Five" (Taris, Noble, Merchant)
4/hub: 13 steps; Attacks after Forms; tabs Basic Info, Character, Skills, Feats, Forms, Attacks, Powers.
5. Attributes: OK with points left -> K2 "You must spend all of your points. Click on the +/- arrows or use the arrow keys to assign points." / OK; page stays open. Cancel -> hub, Attributes still current (undone). PASS.
2. Force: WIS 16 / CHA 14 -> Basic Info Force 25/25. PASS.
5. Skills: Cancel -> hub, Skills still current. OK with 14 points left -> K2 "You have not spent all of your skill points. These will be saved and you may spend them the next time you gain a level. Do you wish to continue?" OK / Cancel; Cancel stays (14 left); OK finishes (Feats current). PASS (carry-over checked at level-up below).
5. Feats Cancel / Forms Cancel -> hub, that step still current (undone). PASS.
4. ATTACKS (Consular chargen): K2 Feats-style grid, no headings; order Ranged (Charged Shot ... Staggering Shot line), Melee (Cleave ... Body Blow), Unarmed (Clinch ... Uppercut, Jab/Kick/Punch, Claw/Pounce for Cathar), Lightsaber (form openings), Stealth (Sneak Attack, Stealthy Shot lines): 142 names swept. Refused cells red; panes show "Prerequisites:" lines (Strength 12, Base Attack Bonus +1, Character Level N, the form, Cathar, Echani Combat Training, Stealth 6). Shoot drawn held (bright border, Add dimmed). Recommended took Guided Strike (Moderation's opening) with K2's "The following feat(s) have been recommended." popup. OK with 4 unspent: "You have gained new attacks. You must use "Add Attack" to select your new attacks before continuing." / OK. PASS.
   QUESTION: Remaining Attacks 5 at level 1 for a Consular; classes.toml progression gives attack_picks 1 at level 1 (1,1,2,2,...). 
   FINDING: authoring notes in panes: Combination "Moved from the feats, 2026-10-19 (MAIN: an attack; the Brawler's starting attack:304, and attacks are not feats." (attacks.toml:1750); Volley of Bolts "The source names this tier Multi-Shot."; Barrage "The source names this tier Whirlwind Attack."
   Note: the hub Attacks tab lists Strike and Shoot (and picks) but not Jab, Punch, Kick.
1d. Counts: Equipment "Medpac" with "2" on the icon cell. PASS. FINDING: Profession Bonus row still "Security Tunneler, ×2" (count in the text).
Con Twenty played: "Jedi Consular · 1, 8 of 8, force 25 of 25". PASS (2).
2. Quara (Aqualish/Quara Male Sith Warrior, bought WIS/CHA 8, shown 6 after -2): Force 12/12. PASS. (An Arkanian Offshoot Sith Warrior at 8/8 showed 14/14.) Vela's pool now reads 63 (51 before: +12).
4. Recommended: Quara (STR 18) -> Power Attack + Sarlacc Sweep; Human Soldier at STR 8 -> Charged Shot. PASS. Remaining Attacks at level 1: Consular 5, Sith Warrior 6 (classes.toml progression gives 1 and 2): QUESTION.
1c. No "Fly" in a human Soldier's Skills tab (Demolitions, Intimidate, Medicine...). PASS.

### Level-up: Watch Two (Guardian 6, Stealth 8, XP for 8)
1a. Class page: Escape leaves level-up (back to play). Chose Watchman -> hub; Escape on hub -> Class page (= Back); Cancel on Class page -> play, still "Jedi Guardian 6, 52 of 52" (nothing written). On a spend page (Skills) Escape -> hub. PASS.
2. Jedi Watchman open at character level 7 (no ten-level gate): PASS. Note: its description box on the level-up Class page is EMPTY. Granted popup listed Force Jump, Force Jump Advanced, ..., Pillar's Support?, Unarmed Specialist I, II.
   Vitality 52 -> 59 (+7 = 5 + CON 2). classes.toml: Watchman d8, Guardian d10; a +5 roll fits both, so one roll can't prove d8. NOT PROVEN.
5. Level-up Skills with 6 left: OK -> the K2 save prompt; OK -> saved; the save holds character.skill-points-saved {points: 6}. Next level (8): Remaining Points 12 = 6 saved + 6 new. PASS.
4. Level-up Attacks: row present (Remaining 1); Recommended dimmed; Accept waited for it; took Covering Fire. Hub order Skills, Feats, Powers, Forms, Attacks. At 8 an Attributes row appears first. PASS.

### Droid RX-193 (Battle Machinist 6 -> 7)
3. Granted: Droid Upgrade 1, Plating Proficiency: Light, Droid Upgrade 2, Plating Proficiency: Medium, Jury Rig, Percussive Maintenance (1/Light/Jury Rig/Percussive likely catch-up for the authored save). Upgrade 2 + Medium plating at class level 7: PASS.
1b. Level-up hub facts: Species Droid, Chassis Battle, Model War Droid..., Homeworld, Upbringing; no Subrace. PASS.
4. Droid Attacks: only ranged rosters (melee hidden), Remaining 1; Shoot held.
SEVERE (sent ahead, HANDOFF ce7238e): the droid's level-up Skills step shows an empty list and "This droid is on none of them. / this step cannot complete for a droid"; OK dead; Accept dim: a droid can never level up. play_screen.dart:2932 _droidSkills matches species id "droid" against droid_skills ids "droid-battle" etc.
6. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 27 "reg193", Escape then F4 rewrote one quick save, Load, a fight to its end. PASS.
