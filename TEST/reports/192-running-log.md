# TEST 192 running log (draft, text only)

Started 2026-10-23. Tester, Xvfb :2, own data dir. TEST 191 fixes and the new level-up items.
Known, don't file: Force pool rules, Attacks page, in-game frames and store, missing pictures, an old save showing "Unarmed Specialist Ii Viii", the ten-level prestige gate.

## Build
- App 71a7386, git archive from my own clone to builds/test192. Built through the lock: 9.8 s. pubspec.lock unchanged.
- Gate: "gate.py --at 71a7386" -> "FOR TESTER — CORE at 71a7386, 4954 tests, 0 failed, 11m46s at -j 3, peak 1706 MB"; "ARCHIVE last green at 71a7386".
- Lodestar 50e3f93444bec6352cf626c95a65325117155821 = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf 4795bc3 (as ordered). check_shelf: 32 rules files, 123 blueprints, identical.
- Fixtures (specs192/): Con Five (C5, Aura+Burst, ->6); Mix Five FIXED per Coder (class-added Guardian 0 + levelled 4,5 = C3/G2, ->G3); Mix Six (C3/G3, ->G4); RX-191 (droid Machinist 1 ->2). The spent 191 saves moved to ~/kotor-tester/old-saves.

## Items

### Con Five (Consular 5 -> 6, holds Force Aura, Burst of Speed)
1a. Powers: Force Shield ("Character Level 6 / Force Aura") teal with Add Power lit, and the arrow Aura -> Force Shield shows; Heal teal; Force Armor ("Character Level 12 / Force Shield") red, Add dimmed; no arrow Burst -> Knight Speed. PASS. Took Force Shield.
1c. Saves: hub Fortitude 6, Reflex 4, Will 7 = sheet +6/+4/+7. PASS.
1e. Granted popup: "Unarmed Specialist I" and "Unarmed Specialist II", separate entries, each with its own icon. PASS.
2. Model frame: the level-up hub shows facts under the portrait (Species Human, Homeworld, Upbringing, Background). PASS (seen).
Forms at Force 6: Remaining Forms 1, Recommended LIT; it took Resilience (FORMS-01 §2.5: Consular third form = III Resilience). PASS.
Accept: Jedi Consular 6, 32 of 38, force 69 of 69.

### Mix Five FIXED (Consular 3 / Guardian 2 -> Guardian 3)
Sheet before: "Jedi Consular 3 / Jedi Guardian 2 · level 5" (fixture now right).
2. Level-up Class page: prestige classes red; Jedi Watchman: "Prerequisites: Character Level 10 / Any Force base class 6 / Stealth 8", OK dead. PASS (the level-10 gate is known).
1b. Hub rows 1 Skills, 2 Feats, 3 Powers, 4 Forms, 5 Attacks: a Forms row. Forms: Remaining 1, Recommended LIT, took Resilience (Guardian's third form per FORMS-01 §2.5; the Consular's is also Resilience, so it can't show which class it read). PASS. Accept: 36 of 44, force 57 of 57.
1b. Mix Six (Consular 3 / Guardian 3 -> Guardian 4): hub rows 1 Skills, 2 Feats, 3 Powers, (gap), 4 Attacks: no Forms row. PASS.
FINDING: once a class is chosen there is no way out of level-up except Accept: hub Back -> Class page; Class Cancel -> back to the hub (as specified); Escape does nothing on the hub. (Before a class is chosen, Cancel leaves.) mix6-trapped-hub. Finished Mix Six to 7 to get out.
2d. Level-up skills count aptitudes: Apt Two (Consular 1->2, Taris aptitude Intimidate): Intimidate "Class Skill / Point Cost 1 · maximum rank 5 / Aptitude: homeworld", plus stops at rank 3 (+2 bonus = cap 5). Apt Three (same + grant-resolved taken: aptitude, Hunter): Beast Handling "Class Skill / Point Cost 1 · maximum rank 5 / Aptitude: profession". (Apt Two without the grant choice: Beast Handling cross-class: right, Hunter's bonus is item OR aptitude.) PASS. Model frame on the level-up hub: Species Human, Homeworld Taris, Upbringing Noble, Background Hunter. PASS.
Small finding: "Fly" is listed on the level-up Skills page, yet its pane says "Beast only. Does not appear on a character's skill list."
1d. Programming panes (droid chargen, all nine): Medical "2 Medpacs / Aptitude: Medicine / Chassis: Any chassis"; Slicer "2 Computer Spikes / Slicing"; ... "Droid Motion Tracker / Repair"; "Droid Deflector Mark I / Alertness"; "Parts / Scavenging"; Repair "2 x Advanced Repair Kit / Repair"; "2 Frag Grenades / Demolitions"; "Minor Frag Mine / Survival"; Archive "a fragment of an old puzzle / Archaeology" — every one with "Chassis: Any chassis". PASS (2e droid programming gives items and aptitude: PASS). Words: "2 x Advanced Repair Kit" vs "2 Medpacs"; "a fragment of an old puzzle" lower case.
2a. Model frame: droid Voice page shows Origin (Species Droid, Subrace "Droid, Battle", Chassis "War Droid Mark I", Voice), Background (Aptitude Scavenging), Languages. Small finding: the labels look shifted one place: the chassis (Battle) sits under Subrace and the model under Chassis. Entry: empty frame (no character yet).
2f. Three-class cap: Tri Six (Soldier 2 / Scout 2 / Smuggler 2, authored, XP for 7): Level Up Class page: every other class red; Medic pane begins "Three classes, maximum."; OK dead. Soldier/Scout/Smuggler open. PASS.
2b/2c (Watchman d8 pool; droid upgrade tiers by its own class levels): not reached — no Watchman can be reached at level 10 in this build, and a droid at a tier boundary wasn't authored.
2g. No file names in any grant I saw (popups, programming panes, Equipment). PASS (as far as seen).
3. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 26 "reg192", Escape then F4 rewrote one quick save, Load, a fight to its end. PASS.
