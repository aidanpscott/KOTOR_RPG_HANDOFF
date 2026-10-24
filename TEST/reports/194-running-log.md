# TEST 194 running log (draft, text only)

Started 2026-10-23. Tester, Xvfb :2, own data dir. TEST 193 follow-ups.
Known, don't file: prestige descriptions, in-game frames and store, missing pictures, Recommended dimmed at level-up and on Equipment/Background.

## Build
- App fcf7d0c, git archive from my own clone to builds/test194. Built through the lock: 9.7 s. pubspec.lock unchanged.
- Gate: "gate.py --at fcf7d0c" -> "FOR TESTER — CORE at fcf7d0c, 4993 tests, 0 failed, 11m53s at -j 3, peak 1711 MB"; "ARCHIVE last green at fcf7d0c".
- Lodestar 240bc46bf5d1478b7648b1bd899139cb77914de0 = lock = compiled. Lens 5fe60a9. Loom: no entry.
- Shelf 3c9ae3e (origin newest: attacks.toml without authoring notes). check_shelf: 33 rules files, 125 blueprints, identical.
- Fixtures (specs194/): Off Six (Soldier 6, Alertness 8, XP for 7), Watch Four (Guardian 6, Stealth 8, XP for 7), RX-194 (Battle Machinist 6, XP for 7), T3-Voice (astromech with a voice, to see the refusal).

## Items
4. Attacks Recommended popup: "The following attack(s) have been recommended." (Guided Strike). PASS.
1. All 142 attack panes swept and scrolled to the end (panescan.sh, panes.tsv): no authoring notes. Combination "Rapid unarmed strikes thrown in quick succession. Level 1. Strike twice unarmed...", Barrage "Level 8. Three strikes. Attack -1, Defense -1.", Volley of Bolts "Level 8. Three shots. Attack -1, Defense -1.", Quick Attack, Riposte clean. PASS.
3. Attacks tab (Consular): Strike, Shoot, Jab, Punch, Kick, then the picks. PASS.
2. Counts: Profession Bonus "Security Tunneler" with 2 on the icon, pane "2 Security Tunnelers / 200cr"; "Medpac" with 2 on the icon, pane "Medical Supplies / 2 Medpacs". PASS.
6. Prestige panes: Off Six (Soldier 6, Alertness 8) Officer: "Prerequisites: / Soldier 6 or Agent 6 / Alertness 8 / Hit Die: d8", OK lit. Unmet: Shadow Hunter "Prerequisites: / Stealth 8 / Killer's Instinct / Hit Die: d8", OK dead; Juggernaut "Armor Proficiency: Heavy or Droid Upgrade 3 / Hit Die: d10". Watch Four (Guardian 6, Stealth 8): Jedi Watchman "Any Force base class 6 / Stealth 8 / Neutral or a light band / Hit Die: d8 / Force Die: d8", OK lit; Jedi Weaponmaster (unmet) "Weapon Focus: Lightsaber / Hit Die: d10 / Force Die: d6". Nothing printed twice. PASS. (Note: Watchman, a met entry, shows all three prerequisite lines; Officer too: right, the "only unmet" rule is for refused entries.)
5. Droids: refusal for a voiced astromech: "An Astromech droid carries no vocabulator and this one has a voice." PASS. RX-194 (Battle): level-up hub attributes 14/14/16/10/12/8 = sheet. PASS. Sheet Character Info: "Species Droid / Chassis Battle / Model War Droid Mark I", no Subrace. PASS.
7. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 28 "reg194", Escape then F4 rewrote one quick save, Load, a fight to its end. PASS.
