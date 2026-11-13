# TEST 256: The screen-fidelity build and its fix

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops (`cmp-*`), every reading and drawn-pixel count (`px.txt`), the match and light logs, the load log, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-256/` (58aa637a); names in brackets below are files there.

## Build

- **App**: main `506f5ae`, a fresh clone. `gate.py --at 506f5ae`: "FOR TESTER — CORE at 506f5ae, 5950 tests, 0 failed".
- **Lodestar**: `3386f72`, compiled into the app. **Loom**: not built, because no step uses it.
- **Shelf**: `e466b46` (origin/main hasn't moved since TEST 255; my first fetch failed with "connection reset", and the retry worked). check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Beds**: `author_tester_pazaak_saves.dart` wrote pazaak-ten, pazaak-full and pazaak-broke with no errors.
- **Restore copy**: `notes/saves256`. The md5s were logged before each load (`loads.txt`).
- **Comparison**: the c961987 frames are TEST 254's (`n-`) and TEST 255's (`nb-`). Every 506f5ae launch is listed in `loads.txt`.
- **The machine rebooted** before this order came, and I restarted my Xvfb `:2` (1920x1080x24) then. Nothing was running.

## Summary

Two findings: the Dialog tab loses the other speaker's lines after a load, and the card under the pointer loses its art. Everything else passes. The art blocker from TEST 255 is fixed.

| # | Check | Result |
|---|---|---|
| 1 | Art | **PASS**. The setup page draws 95.2% of the screen (1,974,515 pixels) and the table 87.9% (1,822,104). Before, during and after a set's box, the table is drawn. No Forfeit Game is left over the board after the match. |
| 2 | Setup | **Play PASS**. It's grey (131,131,106, as K2's) until ten cards, gold (centre 130,112,47; K2 131,112,47) with the pointer elsewhere, and gold under "Are you sure...". **The card under the pointer: FINDING 2.** |
| 3 | Table lights | **PASS**. My light is red on my turn. After a set, the light stays on whoever's turn ended it: my side after my stand or bust, the opponent's after it stood. Under the box, End Turn is grey, Stand is dark with gold words, and Forfeit Game is gold, all within 2 of K2. |
| 4 | Gradient buttons | **PASS**. End Turn, Stand and Forfeit Game are within 3 of K2 at every pixel across. The largest gap is 3, at the dark ends. |
| 5 | Boxes | **PASS**. OK is 217,217,196 and Cancel 109,92,43, both 2 px, at K2's pixel rows. The one-button box runs from y 472 to 606, the same as K2's. |
| 6 | Options > Exit Game | **PASS**. Words 231,231,207, teal 57,226,190, OK's line 196,196,176, Cancel's 25,106,87, both 1 px. No row is lit under the box. The text is still "Do you really want to quit?". |
| 7 | Level-up | **PASS**. The hub fills the window, laid out as K2's 03. Escape from a page returns to the hub. |
| 8 | Dialog tab | Every line is there with its speaker, in order. **After a save and load, only my own line is left: FINDING 1.** |
| 9 | Auto Save | **PASS**. I stood below the Pazaak Player at (2,1). The Auto Save's picture shows me there, and the load put me there. |
| 10 | Store | **PASS**. There's a 2 px gap between rows (35,29,12; K2 43,36,16). The lines are 2 px at 96,82,39. |

## FINDING 1: after a load, the Dialog tab keeps only the player's lines

- **Before the load** (Pazaak Ten, fresh): I talked to the Pazaak Player, chose "5. Not now.", then "1. [Leave.]". Journal > Messages Log > Dialog read (`g-06-dialog`, `h-02-dialog`):
  1. "Pazaak Player: Care for a game of pazaak?"
  2. "Pazaak Ten: Not now."
  3. "Pazaak Player: Come back any time."
- **After loading the Auto Save** written when I left the conversation (Nov 12, 21:49:29): only "Pazaak Ten: Not now." (`g-10-dialog-after-autoload`).
- **After a manual save and load**, to rule out the Auto Save: from a fresh load I had the same conversation, and Dialog showed all three lines. I saved "dlg256" (slot 94, Pazaak Ten's own marks) and loaded it from Options > Load Game, row 2. Again only "Pazaak Ten: Not now." was left (`h-06-saved`, `h-07-loadlist`, `h-10-dialog-after-load`).
- So the Pazaak Player's two lines are dropped by the load, and mine is kept.
- TEST 255's Feedback lines did survive a load.

## FINDING 2: the card under the pointer loses its art

- On the setup page, the card under the pointer goes pale, as in K2. But K2 fades the card and keeps its art: the plus sign, the blue bands and the value box show through (`cmp-hover-card`, left).
- Ours replaces the whole card with a flat khaki tile showing only "+3" (right).
- In numbers, the card's lower band reads 147,145,125 on ours against K2's 145,156,182. The top band is 141,140,121 against 174,168,167.
- The same tile shows on Pazaak Full's Chosen column, under the pointer (`u-04-ten`).

## 1. Art (drawn pixels: luminance 20 or more, out of 2,073,600)

| Screen | c961987 | da46ed5 (TEST 255) | 506f5ae |
|---|---|---|---|
| Setup, three chosen (07) | 1,962,724 | 15,594 | 1,974,515 (95.2%) |
| Setup, ten chosen | — | — | 1,946,799 |
| Setup under "Are you sure..." | — | — | 1,834,364 |
| Table at the start | 1,813,936 | 19,266 | 1,822,104 (87.9%) |
| Table after a side card | — | — | 1,821,844 |
| Table under a set's box | — | — | 1,716,252 |
| Table after OK | — | — | 1,822,087 |
| Pazaak Full setup, table | — | — | 1,940,122, 1,822,105 |

- These are the same shares as Coder's bed: 875k and 815k out of 921,600 at 1280x720 are 94.9% and 88.4%.
- After the match the board reads 293,072, with nothing drawn over its bottom right (`s-22b-board`, and `p-033` after the full match).

## 2. Setup (against 07, 08, 09)

- **Play, under ten cards**: 131,131,106, exactly K2's dim grey (c961987: 76,65,28).
- **Play, at ten**, with the pointer on the -4 card as in K2's 08: the fill matches K2's at every point across. The centre is 130,112,47 against 131,112,47, and x 1005 is 59,51,21 against 60,51,21 (`p-08-unhover`, `cmp-play-k2-unhovered-hovered`).
- **Play, with the pointer on it**: the fill turns grey (centre 127,127,127), and the words stay gold (`s-08-ten`). K2's captures don't show Play under the pointer, so I can't compare that state.
- **Under "Are you sure..."**: Play stays gold, words 217,187,79 (K2 217,186,79) (`s-09-sure`).

## 3. Table lights (against 11, 12, 17)

- **Full match** (`p-` frames, `p-actions.txt`): my light (left) is red in every frame on my turn, 4,672 red pixels, and the opponent's has none. I lost 0 to 3, each set ending on my own bust, and under each box my light stayed red.
- **A second match where I stood early** (`q-` frames, `q-lights.txt`, 8 frames 0.4 s apart after each click):
  - Set 1: I opened and stood at 7, then the opponent drew to 18 and stood. Under the box, the **opponent's** light is red and mine is off (`q-017`).
  - Set 2: the opponent opened and stood at 20, then I stood at 6, which ended the set on my turn. Under the box, **my** light is red (`q-043`).
  - Set 3: the same as set 1. The opponent's light is red under the box (`q-069`).
- The opponent's turn finishes within 0.4 s, so I never caught a frame of its light during its own turn.
- **Under the box**, across each button (K2 12 and 17 read the same; ours `q-017`):

| x | End Turn K2 / ours | Stand x | Stand K2 / ours | Forfeit x | Forfeit K2 / ours |
|---|---|---|---|---|---|
| 1090 | 43,43,34 / 43,43,35 | 1448 | 42,42,34 / 42,42,34 | 1188 | 74,64,26 / 75,64,27 |
| 1170 | 77,77,62 / 76,76,62 | 1528 | 76,76,62 / 76,76,61 | 1368 | 130,112,47 / 128,111,46 |
| 1250 | 55,55,45 / 55,55,44 | 1608 | 57,57,46 / 56,56,45 | 1548 | 72,60,26 / 70,61,25 |

- The words: End Turn 131,131,105 (K2's grey), Stand 212,183,79 and Forfeit 214,184,78 (K2 217,187,79).
- The one difference is the outermost rim pixel of Stand and Forfeit (x 1368 and 1008), which reads 24 against K2's 57. It's the same on c961987.

## 4. Gradient buttons, lit (against 14; ours `s-14-sidecard`)

| x | End Turn K2 / ours | x | Stand K2 / ours | x | Forfeit K2 / ours |
|---|---|---|---|---|---|
| 1055 | 39,34,13 / 39,34,14 | 1413 | 36,33,13 / 37,32,14 | 1158 | 60,51,23 / 60,52,22 |
| 1115 | 92,80,34 / 93,80,34 | 1473 | 90,78,33 / 92,79,33 | 1258 | 104,89,37 / 104,90,38 |
| 1175 | 129,111,47 / 129,111,47 | 1533 | 128,110,47 / 128,111,46 | 1358 | 130,112,47 / 129,112,47 |
| 1235 | 103,88,37 / 103,88,37 | 1593 | 105,89,39 / 104,90,38 | 1483 | 98,84,36 / 98,84,35 |
| 1295 | 51,45,19 / 51,44,18 | 1653 | 53,46,19 / 53,46,19 | 1583 | 53,46,19 / 54,46,19 |

- Checked at every pixel across, the largest gap is 3, at x 1033, 1393 and 1070: 22,19,8 against K2's 19,19,8. On c961987 the gap was up to 27.

## 5. Boxes (against 09 and 12)

| Line | K2 rows | 506f5ae rows | Colour, K2 / ours |
|---|---|---|---|
| 09 OK, top | 508–509 | 508–509 | 217,217,196 / 217,217,196 |
| 09 Cancel, bottom | 594–595 | 594–595 | 109,92,43 / 109,92,43 |
| 09 Cancel, left | x 898–899 | x 898–899 | 109,92,43 / 109,92,43 |
| 12 OK, top | 530–531 | 530–531 | 217,217,196 / 217,217,196 |
| 12 box, top | 472–473 | 472–473 | 109,92,43 / 109,92,43 |
| 12 box, bottom | 605–606 | 605–606 | 109,92,43 / 109,92,43 |

- On c961987 these were 1 px, at different rows, and Cancel was teal (`cmp-pz09-box`).

## 6. Options > Exit Game (against 98)

- "Do you really want to quit?": 231,231,207 at its brightest (K2 231,231,207; c961987 196).
- Teal text: "Save Game" 57,226,190 (K2 57,226,190), "Close" 57,226,190, "Quit the game" 55,223,185 (K2 52,215,179).
- OK's line is y 506 only, at 196,196,176 (K2 194,194,175). Cancel's line is y 592 only, at 25,106,87 (K2 25,106,87). The box is 1 px at 25,106,87.
- The Exit Game row under the box keeps its ordinary 29,119,99 line, where c961987 lit it at 196,196,176 (`cmp-exit-box`).
- The OK and Cancel words read 231,231,207 at their brightest, against K2's 210 and 228. That's one of the known bright peaks.

## 7. Level-up (Watch Two)

- The class page and the hub both fill the window. Because the class page now fills the window, its OK sits at the bottom right, at (1600,954) (`l-01-hub`, `cmp-levelup-hub`).
- The current step circle reads 102,102,77 (K2 103,103,84), and the others 29,119,99.
- **Escape**: from the Attributes page it returns to the hub (`l-03-attributes`, `l-04-attr-escape`). From the hub it returns to the class page, as Back does (`l-02-hub-escape`).

## 9. Auto Save (Pazaak Ten, fresh)

- I walked down one step, then right twice, to (2,1), below the Pazaak Player. Up started the conversation; then "5. Not now." and "1. [Leave.]" (`g-01` to `g-05`).
- Options > Load Game: "Auto Save, Nov 12, 2026 - 21:49:29", the time the `.sav` was written. Its picture shows me at (2,1) (`g-08-loadlist`).
- After Load: I'm at (2,1), and the area's name shows again as on a load (`g-09-after-load`).

## 10. Store (Card Dealer, against 03a)

- Between rows 1 and 2 (y 356–361): row 1's bottom line at y 356–357 (96,82,39), a 2 px gap at y 358–359 (35,29,12), then row 2's top line at y 360–361 (96,82,39, then 84,72,33) (`cmp-store-rows`).
- K2's rows: 98,83,39 and 100,84,39; a 43,36,16 gap; then 100,84,39 and 98,83,39.
- So our second pixel of a row's top line is 84,72,33, against K2's 98–100.
- The box lines are 2 px at 96,82,39, as on da46ed5.

## Odd, not filed

- "[Leave.]" doesn't appear in the Dialog tab. I don't know whether K2 logs it.
- Escape on the level-up hub goes back to the class page, not out of level-up. That's the same as Back, so I took it as intended.
- In K2's 08, the setup page's description wraps onto a second line ("score."); ours fits on one.
- The Attributes page shows only + arrows.

## What I got wrong

- My first class-page OK click used the old position, (1652,706), and did nothing. The page had moved to fill the window. I clicked OK at its new place.
- My box check still looked at y 474. In this build the box's top line is at 472, so the check in the screens script never fired, and its loop ran on to its limit of 12 End Turn clicks. The box was already up in its last two frames (`s-12a-before` and `s-12-setmsg` are the same). I moved the check to 472 before the matches.
