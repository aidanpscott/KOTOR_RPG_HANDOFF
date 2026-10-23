# TEST 191 running log (draft, text only)

Started 2026-10-22. Tester, Xvfb :2, own data dir. Level-up and multiclass, plus TEST 190's fixes.
Known, don't file: level-up Skills not counting homeworld/profession aptitudes; prestige prerequisites and the three-class cap; "Jedi Robe a_robe_08"; the empty Force pool on low-stat builds; the model frame; the Attacks page; in-game frames and the store; missing pictures.

## Build
- App 46b7cab, git archive from my own clone to builds/test191. Built through the lock: 9.8 s. pubspec.lock unchanged.
- Gate: "gate.py --at 46b7cab" -> "FOR TESTER — CORE at 46b7cab, 4923 tests, 0 failed, 11m38s at -j 3, peak 1719 MB"; "ARCHIVE last green at 46b7cab".
- Lodestar fec65ecb1753d014818df55819a78fb0d1c21bc7 = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf 5ac3d20 (= origin). check_shelf: 32 rules files, 118 blueprints, identical.
- Authored (specs191/): Sol Six (Soldier 6, +6000 XP -> 7), Con Five (Consular 5 with Force Aura and Burst of Speed, +5000 -> 6), Mix Five (Consular 3 / Guardian 2 with Force Aura, +5000 -> 6), RX-191 (Battle droid Machinist 1, +1000 -> 2).

## Items

### Sol Six: Soldier 6 -> Jedi Guardian at 7
2. In-game sheet: Auto Level Up dimmed, Level Up lit. Level Up opens the Class page titled "LEVEL UP / Choose your class" over play; Cancel before choosing returns to play. The list includes prestige classes (known). Jedi Guardian, OK.
   Granted popup on arriving at the hub AND again on opening Feats: "Squad Tactics, Improved Squad Tactics, Both Hands, Improvised, Force Jump" (Both Hands, Improvised in empty slots). The four Soldier feats are probably catch-up because my authored save never recorded the Soldier's grants (fixture effect, not filed).
   Hub: "Level Up", portrait box (empty), name/class/level 7, stats; rows 1 Skills, 2 Feats, 3 Powers, 4 Forms, 5 Attacks (dimmed); Back beside Accept; Accept dim until all done, then lit. PASS. Note: hub saves read 5/2/2 (base only) while the in-game sheet read +7/+4/+3.
3. Multiclass: Skills (3 points): gold = Alertness, Athletics, Awareness, Demolitions, Intimidate, Medicine, Mysticism, Persuade, Survival, Swim = Soldier's 8 + Guardian's Mysticism, Persuade. PASS. Feats: Remaining 1, "Armor Proficiency: Light" (K2 spelling) with an arrow Light -> Medium. Powers: Remaining Powers 2 (took Heal, Force Aura). Forms: Determination held + one pick (Perseverance); Recommended dimmed on the level-up Forms page (chargen has it lit).
   After Accept: party card "Soldier 6 / Jedi Guardian 1 · 7, 52 of 60, force 18 of 18": a Force pool. Saves Fort +9 Ref +6 Will +4 = Soldier 6 (5/2/2) + Guardian 1 (2/2/1) + CON 2/DEX 2/WIS 1: summed per class. PASS. Vitality 52 -> 60 max (+8 = d10 6 + CON 2); Soldier and Guardian are both d10, so this character can't show which die was used. Survives F4 + kill + Continue. PASS.
   In-game sheet still lists "Armour Proficiency: Light" (in-game frame, known).

### Con Five: Consular 5 -> 6 (holds Force Aura, Burst of Speed)
Granted popup: "Unarmed Specialist I", "Unarmed Specialist II-VIII" (one entry named for a range) — for MAIN: right for a level-6 Consular? 
2. Hub rows Skills, Feats, Powers, Forms, Attacks (dim): the Forms page appears at Force level 6 (Remaining Forms 1, Determination held). PASS.
4. ARROWS: no arrow anywhere on Powers. FINDING (important): Force Shield, whose pane reads "Character Level 6 / Force Aura", is shown REFUSED (red, Add Power dimmed) while this character holds Force Aura and is levelling to 6. Heal ("Character Level 6") is refused too. Knight Speed (Character Level 9) refused correctly. So the level-up page checks "Character Level N" against the level BEFORE the level-up, which also hides the Aura -> Shield arrow. (Sol Six levelling 6 -> 7 saw Heal teal, consistent.)
Took Force Valor, Moderation, Alertness x5, Armor Proficiency: Light; Accept: "Jedi Consular · 6, 32 of 38, force 69 of 69".

### Mix Five: Consular 3 / Guardian 2 -> Guardian 3 (Force level 6)
(First pass: OCR missed "Guardian" and I chose Jedi Sentinel by accident: hub rows Skills/Feats/Powers/Attacks, no Forms either. Hub Back returned to the Class page with Sentinel lit: PASS for Back.)
3. FINDING: at Force level 6 by multiclass (C3/G3) the hub has rows 1 Skills, 2 Powers, 3 Attacks — NO Forms step, so no form pick at all (MAIN expected one). Con Five (single-class) got the Forms page at Force 6. K2-style gaps between rows where Feats/Forms are absent. Granted: Force Jump, Unarmed Specialist I, Unarmed Specialist II-VIII.
Accepted: "Jedi Consular 3 / Jedi Guardi... 36 of 44, force 63 of 63".
2. Droid RX-191 Level Up: Force classes (Guardian, Sentinel, Consular, Inquisitor, Warrior, Assassin) red/refused; Machinist lit. PASS.

### 1. TEST 190 fixes (chargen)
- Skill Bonuses count live: 0 -> 1 -> 2 -> (re-touch) 1 -> 2 of 2. PASS.
- Upgrade (Soldier, Hunter): "Your class's own melee upgrade — Long Sword + Short Sword or a Double-Bladed Sword", only the Soldier's line, inside the row, on the Standard route and the Purchase route. PASS.
- Droid Model page: K2 list page with the picture box (pane "Chassis Battle / Frame 1900 Credits": model frame, known). PASS.
- Story takes keys at once: no click, Home, typed "ZZ " -> entered. PASS.
- Soldier hub tabs: Basic Info, Character, Skills, Feats, Attacks (no Forms/Powers). PASS.
- Cancel keeps: Human: Cancel from Class -> Racial Skill with Appraise lit; Character tab shows "Aptitude: Appraise". Droid: Cancel from Class -> Model "War Droid Mark II" kept; Back -> Racial "Scavenging" kept; Back -> Chassis "Battle" kept. PASS.
- Words: "Training Lightsaber" (Sith Inquisitor kit, no colour word), "Parts" (droid kit), "Armor Proficiency: Light" on Feats pages, "Defense" on hubs. No "Armour"/"Defence" on chargen/level-up pages. (In-game sheet still "Armour Proficiency: Light": in-game frame, known.) Small: "tier-1 saber upgrade" and "2 medpacs" lower case.
- Programming pane (Slicer Droid): "2 Computer Spikes / Aptitude: Slicing", no cost. FINDING (small): no chassis line, which MAIN listed.
5. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 25 "reg191", Escape then F4 rewrote one quick save, Load, a fight to its end. PASS.
