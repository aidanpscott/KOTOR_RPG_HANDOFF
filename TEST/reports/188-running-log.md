# TEST 188 running log (draft, text only)

Started 2026-10-19. Tester, Xvfb :2, own data dir. TEST 187 fixes, the Forms step, arrows.
Known, don't file: Entry, Class, base page, our own steps, the Attacks page, level-up pages, in-game frames, Mire/Contagion pictures.

## Build
- App 9b30272, git archive from my own clone to builds/test188. Built through the lock: 200 s (mostly the Lodestar fetch/compile). pubspec.lock unchanged.
- Gate: "gate.py --at 9b30272" -> "FOR TESTER — CORE at 9b30272, 4258 tests, 0 failed, 9m12s at -j 3, peak 1746 MB, run 2026-10-19T22:38:21"; "ARCHIVE last green at 80355dd".
- Lodestar 181ac71940854923a7f2c3a71aa4d1276cddc03c = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf 5ac3d20 (as ordered). check_shelf: 32 rules files, 118 blueprints, identical.

## Items

### Run 1 (Human Female Jedi Consular)
2a. Hub, 13 steps, no scrolling: Gender, Portrait, Origin, Background, Attributes, Skills, Feats, Forms, Attacks, Powers, Equipment, Name, Play (hub-jedi). Tabs: Basic Info, Character, Skills, Feats, Forms, Attacks, Powers. PASS. Note: at 1920 "Basic Info" and "Character" nearly touch ("BASIC INFOCHARACTER").
3a. Feats at creation: no arrow anywhere (feats-open2). Took Armour Proficiency: Light -> an arrow appears Light -> Medium (Medium now takeable); none to Heavy (refused). PASS.
1c. Remaining 0 (Feats): Cautious (takeable) shows Add Feat in its normal look; pressing it changes nothing (still 0). Armour Proficiency: Heavy (refused, needs Medium) shows Add Feat dimmed. PASS.
2b. Forms page: lightsaber forms on top (Determination, Contention, Resilience / Aggression, Perseverance, Moderation / Ferocity), Force forms below (Force Focus, Force Potency, Force Affinity / Force Mastery), all four red-bordered (refused). Determination held, Remaining Forms 1, Add Form dimmed on it (pane "Lightsaber Form / Prerequisites: Any Force class / ... Attack Modifier: +1, Defense: +3, Defense vs. Current Target: -3 ..."). Force Mastery pane: "Force Form / Prerequisites: Jedi Sage, Sith Sorcerer, Jedi Watchman, Sith Marauder". No help box on this step. PASS.
   Recommended took Moderation (Form VI): matches FORMS-01 §2.4 (Consular -> Form VI Moderation). PASS.
   Remaining 0 (Forms): Resilience shows Add Form normal; pressing it changes nothing. Force Mastery shows Add Form dimmed. PASS.
   Forms tab: "Determination", "Moderation" with icons. PASS.
   Reopen Forms: kept (Moderation held, Remaining 0) but the page OPENS ON DETERMINATION, not the chosen form (twice: forms-reopen, forms-reopen2). FINDING.
   Change form with later steps done (Powers, Equipment, Name finished): "Every step after this one will be lost. Proceed?" -> OK clears Powers onward (name gone). With nothing finished after Forms, a change gives no warning (nothing to lose). PASS.
3b. Powers at creation: no arrow anywhere (powers-open). PASS. Level-6 Consular: level-up not reached.
1a. Name caret (xdotool key + clicks): typed "Abcdef Ghijk_"; click at start "_Abcdef Ghijk"; middle "Abcde_f Ghijk"; end "Abcdef Ghijk_"; Left x3 "Abcdef Gh_ijk"; Home "_Abcdef..."; Right x2 "Ab_cdef..."; End "...Ghijk_". The "_" follows the caret every time. PASS.
1b. Granted lists, all 19 base classes at level 1 (grants/): Soldier "Squad Tactics" (icon); Scout "Targeting 1" (icon), "Terrain Sense" (empty slot); Smuggler "Smuggler's Luck" (icon), "Quickdraw" (K2 empty slot, now drawn), "Killer's Instinct" (icon); Bounty Hunter, Marksman, Agent, Duelist: no popup (no grants); Engineer "Field Override" (empty slot); Machinist "Jury Rig" (empty slot); Treasure Hunter "Read the Ruin" (empty slot); Medic "Triage", "Field Surgery" (empty slots); Brawler "Nothing In My Hands" (empty slot); Saboteur "Salvage Charge" (empty slot); Jedi Guardian "Force Jump" (icon); Jedi Sentinel "Force Immunity: Fear" (icon); Jedi Consular, Sith Inquisitor, Sith Warrior: no popup; Sith Assassin "Vanish" (empty slot), "Killer's Instinct" (icon). Every entry has a visible cell. PASS. Note: many granted class feats have no icon yet (empty slots).
2c. Soldier/Scout etc.: 11 steps, no Forms and no Powers; Attacks follows Feats (hub rows measured). PASS.
2d. Recommended by class: Consular -> Moderation, Sith Assassin -> Contention; both match FORMS-01 §2.4.
2e. Save/load: Form Nine (Sith Assassin, Contention via Recommended), Play, F4, kill -9, Continue: the save holds "character.form-taken {id: form_ii_contention, at_level: 1}" and Continue resumes. In-game Abilities > Feats shows no forms (in-game frames, known). PASS (by the save).
4. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 22 "reg188", Escape then F4 rewrote one quick save, load, a fight to its end. PASS.
