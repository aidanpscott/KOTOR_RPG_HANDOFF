# TEST 187 running log (draft, text only)

Started 2026-10-19. Tester, Xvfb :2, own data dir. TEST 186 fixes, forms, class features at their levels, grids.
Known, don't file: Entry, Class, base page, our own steps, Attacks, level-up pages, in-game frames, Force Mire/Contagion pictures.

## Build
- App fa7fb60, git archive from my own clone to builds/test187. Built through the lock: 9.7 s. pubspec.lock unchanged.
- Gate: "gate.py --at fa7fb60" -> "FOR TESTER — CORE at fa7fb60, 4232 tests, 0 failed, 8m25s at -j 3, peak 1753 MB, run 2026-10-19T18:38:00"; "ARCHIVE last green at fa7fb60".
- Lodestar c172e5863f0e07b12fff911aa77b66a936b38b0b = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf 3662ad4 -> bcf7bc7 (origin newest). check_shelf: 31 rules files, 118 blueprints, identical.

## Items

### Run 1 (Human Female Jedi Consular, same path as 185/186)
1c. "None.": Human (no adjustments): the Strength description ends after its text, no "None." line (attr-human-str). PASS (species with adjustments: below).
1a. Feats icon tint vs L3-07: every not-held icon now draws dim grey-green like K2's; the first cell (Aggression (Form IV)) is not brighter than the rest; the HELD feat (Determination) draws bright with a lit border, the same way K2 draws held feats (Armour Proficiency etc. in L3-07). Side by side kc.png. PASS (Powers below).
2a. Forms: on opening Feats, K2's popup "You have been granted the following feat(s) this level." listing "Determination (Form I)" with OK (granted.png). Determination is held and lit in the grid; pane: "Prerequisites: None / Force classes only. A lightsaber form, also known as Shii-Cho, Form I. Its stance gives the line below while a lightsaber is held. / Attack +1; Defense +3; Defense vs. current target −3. Net +0 against your target, +3 against everyone else — defensive when outnumbered." Remaining Feats 2.
2b. One more form: Aggression (Form IV) added -> Remaining Feats 2 -> 1, Remove Feat shown; a second form (Contention (Form II)) then refused: Add Feat dim, Remaining stays 1 — but the pane gives NO reason ("Prerequisites: None", nothing about a form already chosen). With the form removed and only the ordinary feat spent, OK -> K2 popup "You have gained new feats. You must use "Add Feat" to select your new feats before continuing." / OK. The last slot then refused Blindside and took Aggression (Remaining 0): a form-only slot. PASS (note: no refusal reason).
   Forms on the grid (sweep fgrid.tsv): Determination (I), Contention (II), Resilience (III), Aggression (IV), Perseverance (V), Moderation (VI), Ferocity (VII), and the Force forms Force Affinity, Force Focus, Force Mastery, Force Potency.
1a. Powers tint vs L2-08 side by side (pc.png): the same dim tint; Heal's cell no brighter than its neighbours. PASS.
1b. Inspire Followers II: lit cell (row with I and III), pane by eye "Inspire Followers II / Light Side Power / Point Cost 12 / Prerequisites: / Officer 5 / Inspire Followers I / Restricted By Armor ..." It was always there; my TEST 186 "no II" was an OCR misread ("II" -> "I"). CORRECTION to 186.
1d. Name field (xdotool key, window focused): BackSpace, Delete, Home, End, Left, Right all work. xdotool type of "\b" does nothing (expected: type sends text, not keys). Without a click, typing appends at the end. FINDING: a click inside the field moves the real caret to the click point (centre click -> mid-name: "Sura XSarn"), but the drawn "_" stays at the end, so the caret is invisible: the first BackSpace after clicking deleted "k" from "Ravik Dray".
4. Forks: Force Stun / Stasis / Stasis Field, then Force Sleep alone in column 1; Stun Droid / Disable / Destroy, then Force Static Field alone in column 1; Shutdown > Overload. No row starts with an empty cell on the fork page. PASS. (Correction to my 186 log: the "zzz" icon is Force Stasis Field's; Force Sleep's own icon is the spiky head.)
4. Powers grid re-sweep (pgrid.tsv): 101 distinct powers. Every name seen in more than one column of a page was checked against the cell map: those are only my 24 px clicks landing in the empty space right of a single-icon row (the pane keeps the last selection). No power found in two cells. PASS.
2c. SOLDIER (Human, Soldier): granted popup lists only "Squad Tactics"; the form-check script (formcheck.sh) tried Add Feat on all 10 non-held forms: Remaining unchanged for every one (Aggression's pane shows Add Feat dim, "Force classes only."). Control: Armour Proficiency: Light added at once (Remaining 1 -> 0, probe saw it). PASS.
2d. JEDI GUARDIAN: granted "Force Jump" and "Determination (Form I)". Forms: Contention, Resilience, Aggression, Perseverance, Moderation, Ferocity each takeable (Remaining 2 -> 1, removed again); the four Force forms (Affinity, Focus, Mastery, Potency) refused (Remaining unchanged). PASS.
3a. BOUNTY HUNTER level 1: NO granted popup at all; hub Feats tab after spending: only "Armour Proficiency: Light". No Quarry. PASS.
3b. SOLDIER level 1: granted Squad Tactics only, no Both Hands. PASS.
3c. SMUGGLER level 1: granted "Smuggler's Luck", "Quickdraw", "Killer's Instinct". PASS. FINDING (small): Quickdraw's row in the granted list has NO icon cell at all (Smuggler's Luck and Killer's Instinct have theirs).
3d. Level-up: not reached (level-up pages are on the known list).
4b. Feats grid, all 6 pages (fg-page1..6): a pixel check finds no row whose column-1 cell is missing while column 2 or 3 has one. PASS. (Several column-1 cells are empty frames: feats with no icon yet, as in 185 — Blindside, Cautious, Elusive, Freetrader rows etc.)
1c. Twi'lek (adjustments): every attribute pane ends with "+2 Charisma, −2 Wisdom." (attr-twilek-str/int). Human: no line. PASS.
5. DICE: Dice One Quick Save, one launch: log crop md5 = TEST 185's run A. PASS.
5. REGRESSION (Icon Nine): Escape > Save slot "reg187" (000021); Escape then F4 rewrote the one quick.mark; Load list Auto, Quick, 21, 20, 19; loading reg187 works; a fight to its end (party defeat box). PASS.
