# TEST 189 running log (draft, text only)

Started 2026-10-20. Tester, Xvfb :2, own data dir. Entry, Class, Forms list, reopen lighting, hub tabs, Powers at 0.
Known, don't file: our own steps, the Attacks page, level-up pages, in-game frames, missing class and feat icons.

## Build
- App 900a05f, git archive from my own clone to builds/test189. Built through the lock: 9.6 s. pubspec.lock unchanged.
- Gate: "gate.py --at 900a05f" -> "FOR TESTER — CORE at 900a05f, 4272 tests, 0 failed, 8m33s at -j 3, peak 1756 MB, run 2026-10-20T08:39:28"; "ARCHIVE last green at 900a05f".
- Lodestar 181ac71 = lock = compiled. Lens 5fe60a9 = lock = compiled. Loom: no entry.
- Shelf 5ac3d20 (= origin). check_shelf: 32 rules files, 118 blueprints, identical.

## Items
1. ENTRY (1920): Quick, Custom, Premade in a column (y 642-690, 699-748, 757-805: 57-58 px apart = 32 units at 1.8x); the description box 815-921 ends above Cancel 930-978. Base page behind: empty portrait cell, empty name box, empty stat cells, no face. Hover Quick: "Select this option to have your character's creation handled for you. You will only choose your character's appearance and name. / Not available yet: no class has a recommended build written, so there is nothing to fill it in from." Hover Premade: "Tester Bolt supplies no premade characters, so there is nothing here to choose between." PASS. Note: Quick's text is longer than the box; the last line only shows after scrolling the box with the wheel, and nothing shows that it scrolls. Same at 720.
2. CLASS: list with an empty icon cell per class, the name bar ("Soldier"), a scrolling description; no face (class-open). A click on Smuggler lights it and changes the name bar/description, stays on the page; OK chooses. Droid (Astromech T3) on Jedi Consular: rows of Force classes red; the description starts "a droid chassis holds no Force class" then the class text; OK dim and pressing it does nothing (droid-consular, droid-consular-ok). PASS. Note: the reason starts lower-case.
3. FORMS LIST: "Lightsaber Forms" heading, Determination ... Ferocity, "Force Forms" heading straight after (no gap), Force Focus, Potency, Affinity, Mastery; no scrollbar needed at 1920 and 1280. Clicking either heading changes nothing (selection stays). Icons in colour; Form I held; Remaining Forms 1; the four Force forms red. PASS.
6. POWERS AT REMAINING 0: Force Valor (takeable) shows Add Power normal, pressing it does nothing (Remaining 0); Improved Heal (refused, Character Level 12) shows Add Power dimmed. PASS.
4. REOPEN LIGHTING (Lit Nine: Feats Cautious; Form Contention; Powers Burst of Speed then Force Aura): Feats opens lit on Cautious; Forms opens lit on Contention; Powers opens lit on Force Aura — the first of my powers in GRID order (Aura's row is above Burst's), not the one I chose first in time (Burst of Speed). PASS if "first" means grid order; MAIN to say.
5. HUB TABS: 1920 gaps between labels 41-43 px, "Basic Info" (word gap 15) clearly apart from "Character" (41). 1280: evenly spaced by eye (hub-tabs). PASS.
7. Dice: identical to TEST 185 (md5). Regression (Icon Nine): slot 23 "reg189", Escape then F4 rewrote one quick save, Load list shows it, loaded, a fight to its end (party defeat box). PASS.
