# TEST 261: The capture sweep

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops, every reading (`px-*.txt`, `geom-pz.txt`), the load log (with a frame at every Load click), the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-261/` (c8464f4c); names in brackets below are files there.

## Build

- **App**: main `fc33a16`, a fresh clone. `gate.py --at fc33a16`: "FOR TESTER — CORE at fc33a16, 6003 tests, 0 failed". The first gate run's top line read "DO NOT SEND"; a second run straight after read "SENDABLE — 5 warning(s)". FOR TESTER was the same both times.
- **Locks**: Lens `e449221` and Lodestar `e81b358`, compiled in.
- **Shelf**: `8f2d845`, origin's head ("The Command Deck trooper's My mistake ends the conversation…"). check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **The before**: TEST 260's build of `ec3fde2`, which is after `a8778ce`, run through the same screens with the same clicks. Its frames start `o-`; fc33a16's start `n-`.
- **K2**:
  - `media/screens/k2-pazaak`, native 1080: edges, lines and text measured.
  - `media/study/pt2752/k2-ingame`, `k2-levelup` and `k2-capture-run` (resized): flat fills and positions only.
  - `k2-chargen`, 4K: flat fill only.
- **Saves**: pazaak-ten and pazaak-full (rewritten by `author_tester_pazaak_saves.dart`), Looter, and Watch Two (`lu193-guard6b`). Restore copy `notes/saves261`.
- **Xvfb**: checked before the first launch. It was down, and I restarted it.

## Summary

Steps 1, 3, 4 and 5 pass. Step 2 passes for the see-through box and the minus arrow. Five findings, all on screens or fills not covered by the known list. Every one of them is the same on ec3fde2, so none is new on this hash.

| # | Check | Result |
|---|---|---|
| 1 | Pazaak setup 06–08 | **PASS**. Card rows are exactly K2's. Cards with none left dim as K2's do, and the counts stay white. Hovered plus badge 205 (K2 204). |
| 2 | Wager page 04 | **PASS** for the box and the minus arrow: the card shows through at 67,22,23 (K2 68,23,23), and the outline is 131,106,0. **Finding 1**: the plus arrow. **Finding 2**: three button words. |
| 3 | Flat fills | **PASS**. Panels and rows, Abilities' selected row, the store box, the Map note box, and the Abilities and Equip plates all match within 3. **Findings 3 and 4**: Inventory and Map plates, and the portrait strip. |
| 4 | Places | **PASS** for the Abilities readout art and the Feedback check boxes. The chargen popup's edge isn't drawn at 1080 (see 4). |
| 5 | Store 03a | **PASS**. 2 px between rows, thumb 186,161,74, title 209. |
| 6 | Whole-screen look | Nothing black, broken or missing on any screen I opened, compared with ec3fde2. **Finding 5**: the Level Up buttons are see-through. |

## FINDING 1: Pazaak's wager "+" arrow is dark at the maximum wager (k2-pazaak 04)

- At wager 40 (the maximum), K2 draws the "+" arrow lit: outline 131,107,5, its sign 217,176,0.
- Ours draws it dark: outline 76,61,0, sign 76,61,10. The "−" arrow is lit in both (131,106,0, peak 217,176,0).
- The same on ec3fde2 (`px-pz04.txt`, `n-pz-04`, `o-pz-04`).

## FINDING 2: three Pazaak button words sit off K2's centres (k2-pazaak 04 and 08, native)

The span of the lit text pixels, K2 against fc33a16:

| Word | K2 x | Ours x | Centre moved |
|---|---|---|---|
| Quit | 605–638 | 612–641 | +5 |
| Wager | 887–940 | 895–946 | +7 |
| Clear Cards | 1485–1600 | 1477–1592 | −8 |
| Play | 1062–1164 | 1064–1162 | 0 |
| How much do you wager? | 646–887 | 646–887 | 0 |

- The words are 1 px lower than K2's (Quit y 568, K2 567; Clear Cards 946, K2 945).
- The same on ec3fde2.

## FINDING 3: Inventory and Map still draw the old plate beside the portrait

- On Abilities, Equip, Character, Journal, Messages, Options and Party, the plates beside the portrait are K2's curved pair, filled 9,36,29 (K2 8,36,29).
- On **Inventory** and **Map**, ours has one square-cornered piece on the left, filled 11,42,35, and **no right piece**.
- K2's 20-inventory and 80-map both have the curved pair at 8,36,29 (`cmp-plates`, `px-plates.txt`).
- The same on ec3fde2.

## FINDING 4: the strip just right of the portrait is black

- K2 fills the narrow strip inside the portrait frame, right of the picture (x 1492–1506), with 12,54,46 on Abilities, Equip, Inventory and Map.
- Ours is 0,0,0 on every screen, on both builds (`cmp-plates`, `px-plates.txt`).

## FINDING 5: the character sheet's Level Up buttons are see-through

- K2's 01-sheet-levelup-offered fills Auto Level Up and Level Up dark: 36,34,33 and 37,37,37.
- Ours shows the portrait straight through both, at 213,179,154 and 172,151,122 under the words (`px-sheet.txt`, `n-lu-01-sheet`).
- The same on ec3fde2 (197,155,127 and 147,124,92).
- Our sheet shows the portrait where K2 shows the 3D model, and the portrait covers part of the alignment bar's "Light" and "Dark" labels.

## 1. Pazaak setup (Pazaak Ten: wager 40, +1, +2, +3 chosen with +3 hovered, then all ten with −4 hovered)

- **Rows** (`geom-pz.txt`). The brightness steps up at the card's top edge in K2 at y 307 (the −3) and y 154 (the +1). The value box is 350–383 by my threshold.

  | | −3's top | value box | +1's top |
  |---|---|---|---|
  | K2 08 | 307 | 350–383 | 154 |
  | fc33a16 | 307 | 350–383 | 154 |
  | ec3fde2 | 308 | 350–384 | 155 |

- **A card with none left** (08, all ten chosen). The available +1:

  | Part | K2 | fc33a16 | ec3fde2 |
  |---|---|---|---|
  | Bottom band | 58,88,168 | 57,89,167 | 49,89,213 |
  | Face | 128,111,96 | 129,111,95 | 149,122,98 |
  | Plus badge peak | 190 | 190 | 255 |
  | Count square | 255 | 255 | 255 |

  - The −3's band is 140,115,101 (K2 139,117,101). The printed values peak at 187,176,155 in all three.
- **Hovered plus badge** (07, +3): 203,204,193 with a peak of 205,205,193 (K2 201,202,193, peak 204; ec3fde2 peak 223).

## 2. The wager page (04)

- **See-through box**: inside the box, over the −2's top band, it reads 67,22,23 (K2 68,23,23). Over its bottom band, 65,20,19 (K2 65,19,19); over the −3's top band, 64,19,19 (K2 64,19,19). On ec3fde2 the same spots were 40,9,9.
- **The "−" arrow outline**: median 131,106,0, peak 217,176,0, exactly K2's.
- **The "+" arrow**: Finding 1. **The button words**: Finding 2.

## 3. Flat fills

| Fill | K2 | fc33a16 | ec3fde2 |
|---|---|---|---|
| Load list panel, right panel, top bar | 8,36,29 | 9,36,31 | 9,36,31 |
| Load list row interior | 0,12,10 | 0,12,10 | 0,12,10 |
| Messages panel; Options right panel | 8,36,29 | 9,36,31 | 9,36,31 |
| Abilities selected row interior | 0,12,10 | 0,12,10 | 6,23,19 |
| Abilities description panel, title box | 8,36,29 | 9,36,31 / 9,36,30 | 9,36,31 / 9,36,30 |
| Abilities readout value cell | 8,36,29 | 9,36,30 | 0,0,0 |
| Plates beside the portrait, Abilities and Equip | 8,36,29 | 9,36,29 | none on Abilities; 11,43,35 on Equip |
| Map note box | 8,36,29 | filled, in K2's place | the same |
| Store description and cost boxes | 33,28,12 | 35,29,12 | — |
| Store list panel | 33,28,12 | 30,27,11 | — |
| Chargen help popup inside | (0,12,10, as ordered) | 0,12,10 | 0,12,10 |

- K2's selected Load row also has a lighter band at its top and bottom (5,21,17), the selection's glow. Ours has only one row.

## 4. Places

- **The Abilities readout** uses K2's rank-table art. Its lines sit at y 739–740, 774–775, 808–809 and 845–846 (K2 740, 774–775, 809–810, 846). The labels start about 5 px left of K2's ("Bonus" at x 1034, K2 1039).
- **The Feedback check boxes** (Options > Feedback):
  - each mark is 13×10 at x 193–205, on rows 266–275, 312–321 and 358–367, exactly K2's;
  - they're teal, peaking 52,206,174 (K2 55,218,184, a peak on a resized capture);
  - ec3fde2 drew them grey-white, 12×9, one row higher (`cmp-feedback-boxes`).
- **The chargen popup's edge**: I opened Species' help popup on both builds. At 1080 neither draws an edge line around it; its inside is 0,12,10.
  - K2's in-game help box (51-messages-help-box, resized) shows a thin teal edge at x 612 and 1307.
  - The order's edge change is bedded at 2160 or taller, and my Xvfb is 1080, so I couldn't see it. Not filed.

## 5. The store (Pazaak Ten's Card Dealer, against k2-capture-run 03a)

- **Row gap**: our rows' lines run 356–357 then 360–361, leaving a 2 px gap. K2's 321–322 then 325–326 also leave 2 px.
- **Scroll thumb**: 186,161,74, exactly K2's. Ours spans x 942–949, K2's 938–945, so ours is 4 px right. That's part of the rows' layout, which is on the next hash.
- **Title "Buying Items"**: peak 209,209,189, exactly K2's.

## 6. The whole-screen look

- **In-game screens**, on both builds with the same clicks (`sheet-n-tour`, `sheet-o-tour`): Options, Equip, Inventory, Character, Abilities, Party, Journal, Map, the four Messages tabs, Options > Feedback, Table Rules, Graphics, Keyboard Shortcuts, Load and Save. Nothing black, broken or missing that ec3fde2 drew.
  - Beyond the findings, the Map shows the area as a pale grey grid in the middle of K2's map grid, with a "Map — (Command Deck)" line under it. K2 has neither. It's the same on ec3fde2.
- **Pazaak setup and wager**: as in steps 1 and 2.
- **Store**: as in step 5.
- **Level-up** (Watch Two; `n-lu-01` to `03`):
  - the character sheet: Finding 5;
  - the class list draws cleanly;
  - the hub fills the screen (in TEST 254 it sat in a smaller window). The left panel's top arc runs through the "Origin" header box.
- **Chargen**: the entry page and Species with its help popup draw cleanly (`n-cg-01`, `n-cg-02`). I didn't go further into chargen.

## What I got wrong

- My Pazaak setup driver went straight on after a failed Looter load and ran the whole tour over the Load screen. I deleted those frames (`loads.txt` says so) and loaded Looter by hand.
- My first two "Abilities tab" frames in each tour caught the Map; my tab clicks went to the wrong place. They're labelled `abil-tab2/3` but show the Map.
- I didn't run the whole chargen, only its entry page and Species.
