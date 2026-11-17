# TEST 262: The HUD at K2's one scale

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops, the readings (`px-hud.txt`), the load log (with a frame at every Load click), both gate outputs, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-262/` (53c392b7); names in brackets below are files there.

## Build

- **App**: main `9bd1ffb`, a fresh clone.
- **Gate**: I ran `gate.py --at 9bd1ffb` twice, one straight after the other (`gate262-1.txt`, `gate262-2.txt`). Both runs read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 9bd1ffb, 6004 tests, 0 failed".
- **Locks**: Lens `e449221` and Lodestar `e81b358`, compiled in.
- **Shelf**: `8f2d845`, origin's head. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **The before**: TEST 261's build of `fc33a16`, with the same saves and clicks. Its frames start `o-` and fc33a16's tour frames are TEST 261's `n-t-*`.
- **K2**: `k2-capture-run/07` (a true 1080 run, compositor-scaled), positions only. `k2-chargen/14` and `k2-live/33` (resized) for layout only.
- **Saves**: Looter, C79 Battle, Aoo Eighty, Pazaak Ten and Watch Two (`lu193-guard6b`). Restore copy `notes/saves262`.
- **Xvfb**: checked before the first launch; it was up.

## Summary

Steps 1, 2, 5 and 6 pass. Steps 3 and 4 pass in part. Two findings:

- Finding 1 is **new** on this hash.
- Finding 2 is the same on fc33a16.

| # | Check | Result |
|---|---|---|
| 1 | HUD places against 07 | **PASS**. Icon bar, action bar, big portrait, swap button and Kael's small portrait are all within 2 px. Neither build draws a minimap (owner, in `k2_hud.dart`). |
| 2 | Icon detail | **PASS**. Black "?" on Character and Journal, black "N" on Map, the hand's lines, and the party icon's head outlines. |
| 3 | The board | **PASS at 1080 and 1280×720**. The HUD covers less than on fc33a16, and clicks next to it land on the board. **Finding 1**: at 1280×1080 the message box covers Equip. |
| 4 | Chargen's portrait border | **PASS** on the entry, Gender and biography pages and the level-up hub: a rounded frame with black outside. **Finding 2**: the custom-character hub and Species keep teal corners. |
| 5 | Fight lines | **PASS**. Three long lines all show whole on screen in three rows, none cut. Messages > Combat has each one in K2's short form. |
| 6 | Whole-screen look | **PASS**. Every in-game screen, Load, Save, Pazaak and level-up are pixel-identical to fc33a16. Chargen ran to play; nothing newly broken. |

## FINDING 1 (new): at 1280×1080 the message box covers the Equip icon, and Equip can't be opened

- On 9bd1ffb, with the window resized to 1280×1080, the message box spans x 314–879 and the icon bar 805–1271. The box is drawn over the first icon: Equip shows dimmed through the box's edge (`n-16-1280x1080`).
- A click on Equip (842,38) does nothing (`n-17-1280-equip-click`). A click on Inventory (898,38) opens Inventory (`n-18-1280-inventory-click`).
- On fc33a16 at 1280×1080 the box ends at 851 and the bar starts at 857. Equip (890,40) opens Equip (`o-05-1280x1080`, `o-06-1280-equip-click`).
- At 1920×1080 and 1280×720 the two don't meet.

## FINDING 2: the custom-character hub's portrait box, and Species' picture box, still have teal-filled corners

- The order's rounded frame is now drawn on the chargen entry page, Gender, the biography page and the level-up hub. Outside the rounded corners is black, where fc33a16 filled it teal (`cmp-cg-portrait`, `cmp-hub`).
- The **custom-character hub's** portrait box (Rodian Soldier, x 986–1186, y 320–472) still fills outside the rounded corners with 29,119,99 on both builds (`n-cg-06`, `n-cg-14`, `o-cg-hub`).
- The **Species** page's big picture box (x 232–768, y 282–684) does the same, also on both builds and on ec3fde2 (`n-cg-02`).
- The same on fc33a16, so not new on this hash. I'm filing it because step 4 names the chargen portrait border.

## 1. HUD places (Looter on the Command Deck; C79 Battle for the party)

Teal edges along fixed lines (`px-hud.txt`):

| Part | K2 07 | 9bd1ffb | fc33a16 |
|---|---|---|---|
| Icon bar frame, x | 1444–1911 | 1444–1911 | 1387–1909 |
| Icon bar icons, row y 45 | 19 runs | the same runs, within 1 px (one shape edge 3 px) | — |
| Action bar frame, x | 6–458 | 7–459 | 9–613 |
| Action bar frame, y | 950–1071 | 950–1071 | 950–1071 |
| Big portrait frame, top and bottom | 938–940, 1070–1073 | 938–940, 1071–1073 | 938–940, 1071–1073 |
| Big portrait picture, x | 1752–1883 | 1752–1883 | 1696–1872 frame |
| Swap Weapons button, x | 1600–1656 | 1600–1655 | 1493–1568 |
| Swap Weapons button, y | 1014–1071 | 1015–1071 | — |
| Kael's small portrait, x | 1831–1893 (slot 2) | 1832–1892 | — |
| Kael's small portrait, y | 868–929 | 868–930 | — |

- **The Stealth button** (the head) sits at 1470–1526. K2's file puts `TB_STEALTH` at 548 of 800, which is 1466 here. K2's 07 doesn't show Stealth, and its Solo and Pause aren't ours. So its place is K2's, though 07 can't show it.
- **The minimap** isn't drawn on either build, by the owner's ruling quoted in `k2_hud.dart`.

## 2. Icon detail (`cmp-iconbar`)

- **Black detail**: the "?" on Character and on Journal and the "N" on Map are black inside the teal shapes, and the hand's inner lines show black, as in 07.
- **Head outlines**: the party icon's heads have their dark outlines.
- **Inventory icon**: still bright where 07 shows it dim (known).

## 3. The board

**What the HUD covers.** Measured at 1920×1080, 9bd1ffb against fc33a16:

| Part | 9bd1ffb | fc33a16 |
|---|---|---|
| Action bar | 7–459 | 9–613 |
| Icon bar | 1444–1911 | 1387–1909 |
| Message box | 634–1199 | 525–1278 |
| Portrait | 1730–1885 | 1667–1872 |
| The two buttons | 1470–1655 | 1320–1568 |

**The board's box.** Zoomed in, the board fills a fixed box, x 379–1912 by y 83–787, on both builds. At 1080 that box touches only the icon bar and the message box.

**Clicks at 1080.**
- Under the icon bar, (1850,92): the player walked there (`n-07`).
- Above the board's top row, beside the box, (500,86): walked.
- Below the message box, (900,100) and (1000,120): walked (`n-09`, `n-14`).
- Inside the message box's own frame, (1000,86): nothing. The box draws over the board's top 6 px (y 83–89) and takes clicks there. fc33a16 does the same at (1000,86), so it's not new (`o-03`, `o-04`).

**Other window sizes.**
- **1280×720**: the 1080 layout scaled by two thirds. The board box is 253–1280 by 55–525, and nothing meets (`n-15`).
- **1280×1080**: Finding 1.

## 4. Chargen's portrait border

- **Entry page**: on fc33a16 the corners outside the rounded frame were filled 29,119,99. On 9bd1ffb they're 0,0,0 (`cmp-cg-portrait`). Nothing else on the page changed.
- **Other pages with the rounded frame**: the same frame on Gender (`n-cg-08`), the biography page (`n-cg-34`) and the level-up hub (`cmp-hub`).
- **Custom-character hub and Species**: Finding 2.

## 5. Fight lines

The on-screen lines are the turn's own line. Enemy turns resolve too fast to read, so these three are ours. Each wrapped whole across three rows of the box, and none was cut:

1. **Kael's first attack** (C79 Battle): "Kael: unarmed · rolled 12 — d20 10 + attack 1 + Strength 1 · needed 10 — hit · damage 2 — 1d3 1 + Strength 1 · 22 left" (`n-23`). Messages > Combat has "Kael attacks Sentry Droid : \*hit\* : (10 + 2 = 12)" and "Kael damages Sentry Droid for 2 damage" (`n-25`).
2. **Aoo Eighty's shot** (Aoo Eighty): "Blaster Rifle · rolled 4 — d20 6 + attack 1 + Dexterity 1 − point blank 4 · needed 10 · 1 square, increment 14 — miss" (`n-35`). Combat log: "Aoo Eighty attacks Sentry Droid : \*miss\* : (6 - 2 = 4)" (`n-37`).
3. **The opportunity attack** (Aoo Eighty): "Sentry Droid catches Aoo Eighty leaving — unarmed · rolled 7 — d20 4 + attack 1 + Strength 0 + closed on a ranged weapon 2 · needed 11 · 1 square — miss" (`n-36`). Combat log: "Opportunity attack: Sentry Droid attacks Aoo Eighty : \*miss\* : (4 + 3 = 7)".

- The log keeps each roll and total, K2's way. The parts (point blank, increment, closed on a ranged weapon) are only on screen.
- Kael's second attack, a 2-row line, is in `n-27`.

## 6. The whole-screen look

**In-game screens** (Looter, the same clicks as TEST 261's tour): Options, every top tab, the Messages tabs, the Options pages, Load and Save are pixel-identical to fc33a16's frames. The only exceptions are the board itself (the HUD) and the Load row's date (`sheet-n-tour`).

**Pazaak** (Pazaak Ten): the wager page and setup frames 06, 07, 08 and 08-unhover are pixel-identical to fc33a16's.

**Level-up** (Watch Two): the sheet and class list are identical. The hub changed only in its portrait border.

**A fight**: the fight frames are C79 Battle and Aoo Eighty.
- The initiative row and the combat queue draw.
- The message box grows down for long lines and pushes the initiative row down onto the board's top edge (`n-23`). I didn't check this on fc33a16.

**Chargen**, to play (Rodian Soldier, Male, Taris Upper City, Noble, Convict; "Mira Veld"): Species, racial skill, class, hub, Gender, Portrait, Homeworld, Upbringing, Background, Attributes, Skills, Feats, Attacks, Equipment, Name, the biography page, then play in the Stasis Yard (`n-cg-*`). fc33a16 on the same path is pixel-identical at the hub, Feats, Attacks and Equipment (`o-cg-*`).

## Odd, not filed (the same on fc33a16)

- **Feats grid**: many boxes are empty where K2's `k2-chargen/14` has an icon in every box, and K2's ▶ arrows between a chain's tiers aren't drawn (`n-cg-23`).
- **Blank icons in lists**: the recommended-attacks popup's icon boxes are blank, and so are the Equipment list's item icons (`n-cg-28`, `n-cg-30`).
- **Health bar**: at 6 of 11 the big portrait's red bar has no outline over its empty part (`cmp-portrait-frame`).
- **Force bar**: neither the big nor the small portraits draw K2's right-hand Force bar for characters without Force (07 shows an empty one on its second portrait).
- **Message box over the board**: the box takes clicks on the board's top 6 px under it (step 3).
- **Rodian portraits**: Rodian has no portraits, only "?".

## What I got wrong

- My Load helper's OCR failed on "Looter" again. I loaded it by hand three times, each with a frame.
- After a later failed load I clicked Cancel and backed out of the Load screen, then loaded by hand.
- My first screen tour ran on the new chargen character, and Equip's first-visit help popup covered every frame. I deleted those frames (noted in `loads.txt`) and ran the tour again on Looter.
- At 1280×1080 my window finder didn't know the new size, so my first Equip click failed to send. The click I report is the second.
