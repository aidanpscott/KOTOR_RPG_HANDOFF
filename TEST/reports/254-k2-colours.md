# TEST 254: K2's colours

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops (`cmp-*`), every pixel reading (`px.txt`), the load log, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-254/` (5df785eb); names in brackets below are files there.

## Build

- **App**: main `c961987`, a fresh clone. `gate.py --at c961987`: "FOR TESTER — CORE at c961987, 5941 tests, 0 failed".
- **Lodestar**: `6fc2738`, compiled into the app. **Loom**: not built, because no step uses it.
- **Shelf**: `6656cc9`. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Beds**: `author_tester_pazaak_saves.dart` wrote pazaak-ten, pazaak-full and pazaak-broke with no errors.
- **Restore copy**: `notes/saves254`, every `.sav`, with dice-one and icons-185 each kept with its own `.marks`. The md5s were logged before each load (`loads.txt`).
- **Before and after**: I ran the same screens on TEST 253's `6e6b961` build with the same clicks (`pzrun254.sh`). Frames from c961987 start `n-`; frames from 6e6b961 start `o-`.
- TESTs 252 and 253 were already filed, so I didn't rerun them.

## How I read the colours

- Each spot is a small box at the same place on K2's capture and on my frames.
- `px254.py` gives two numbers per box:
  - the median colour of the box's brightest tenth (the body of the letters);
  - **pk**, the single brightest pixel. That's the colour the text or line is drawn in.
- Below I give pk. The medians differ a little more, because our letters are thinner than K2's, so fewer pixels reach full colour. All the numbers are in `px.txt`.

## Summary

All four checks pass. On these screens, every K2 colour I read now matches K2's capture to within a few points. Two things still look off against the captures, and neither changed between 6e6b961 and c961987. Both are in Pazaak and the popups:

| # | Check | Result |
|---|---|---|
| 1 | The store's gold | **PASS**. Gold text 163,135,46 → **184,161,73** (K2 177,155,71). Lines and the Filter tab 79,64,23 → **109,93,44** (K2 108,93,44). |
| 2 | Pazaak's pale words | **PASS**. Pale words 196,196,176 → **217,217,196**, exactly K2's. The dim headers 196 → **155,155,131**, exactly K2's. The gold buttons 197–203 → 210–216 (K2 217). |
| 3 | The Exit Game box's teal line | **PASS**. 21,86,72 → **29,119,99** (K2 25,109,90). |
| 4 | Level-up's current-step circle | **PASS**. 102,102,77 on both builds (K2 103,103,84). The circle column is identical pixel for pixel. |
| — | Dim buttons, and buttons behind a box | **FINDING 1**. |
| — | Box buttons' borders | **FINDING 2**. |

## 1. The store (Tester Pazaak's Card Dealer, against `k2-capture-run/03a`)

| Spot | K2 | 6e6b961 | c961987 |
|---|---|---|---|
| "Buying Items" | 209,209,189 | 196,196,176 | 217,217,196 |
| Labels ("Item Cost", "Credits", "In Stock") | 177–178,155,71–72 | 163,135,46 | 184,161,73 |
| "442" | 180,158,73 | 163,135,46 | 184,161,73 |
| "Close", "Show Sell List" | 176,154,71 | 163,135,46 | 184,161,73 |
| "Filter" tab text | 181,158,73 | 163,135,46 | 184,161,73 |
| Filter tab fill | 109,94,44 | 79,64,23 | 109,93,44 |
| Lines under the tabs and over the buttons | 108,93,44 | 79,64,23 | 109,93,44 |

- The gold is brighter, and the lines and tab fill are now K2's to within one point (`cmp-store-labels`, `cmp-store-tabs`).
- The gold text is now a few points brighter than K2's (184 against 177). The title is too (217 against 209).

## 2. Pazaak (Pazaak Ten, against `k2-pazaak` 04, 07, 09, 12, 14)

| Spot | K2 | 6e6b961 | c961987 |
|---|---|---|---|
| "Choose Sidedeck" (04, 07) | 217,217,196 | 196,196,176 | 217,217,196 |
| "How much do you wager?", "Maximum wager: 40" (04) | 217,217,196 | 196,196,176 | 217,217,196 |
| "When you play this card…" (07) | 217,217,196 | 196,196,176 | 217,217,196 |
| Player's name, "Opponent" (14) | 217,217,196 | 196,196,176 | 217,217,196 |
| "Available cards", "Chosen cards", "Player Hand", "Opponent Hand" | 155,155,131 | 196,196,176 | 155,155,131 |
| Card values ("+1", "+3", "-1") | 187,176,155 | 166,153,128 | 187,176,155 |
| "Quit", "Wager" (04) | 217,176,0 | 197–202,148–152,0 | 210–215,170–175,0 |
| "Clear Cards", "End Turn", "Stand", "Forfeit Game" (07, 14) | 217,187,79 | 200–203,163–166,50–51 | 212–216,184–187,77–79 |
| Box text: "Are you sure…" (09), "The opponent wins the set." (12) | 196,196,176 | 196,196,176 | 196,196,176 |
| The wager box's gold line (04) | 131,107,0 | 131,107,0 | 131,107,0 |

- The pale words now match K2's. The dim headers were too bright on 6e6b961 and now match too (`cmp-pz04-wager`, `cmp-pz14-names`).
- The score numbers read 201,201,181 at their brightest (6e6b961: 181; K2: 217). Their medians are close to K2's, so I think the thin digits never reach full colour.

## 3. The in-game Exit Game box (Pazaak Ten, Options > Exit Game, against `k2-ingame/98`)

| Spot | K2 | 6e6b961 | c961987 |
|---|---|---|---|
| The box's line, all four sides | 25,109,90 | 21,86,72 | 29,119,99 |
| The box's fill | 0,12,10 | 2,8,7 | 2,8,7 |
| The Options rows' lines | 26,106,88 | 29,119,99 | 29,119,99 |
| "Do you really want to quit?" | 231,231,207 | 196,196,176 | 196,196,176 |
| Teal row text ("Save Game", "Close") | 57,226,190 | 47,196,165 | 47,196,165 |

- The box's line is no longer dimmed. It's now the same teal as the row lines, which is slightly brighter than K2's: the known "popup lines a little brighter" (`cmp-exit-box`).
- On this screen K2's text is brighter than ours: the question is 231 against 196, and the teal text 226 against 196. Neither changed between the two builds. In the Pazaak captures, K2's box text reads 196, the same as ours.

## 4. Level-up (Watch Two, `lu193-guard6b`, Level Up, then Jedi Guardian, OK)

- The current step (Attributes) has its circle at 102,102,77 on both builds. K2's 03-levelup-hub reads 103,103,84 for its current step (Skills).
- The other circles read 29,119,99 on both builds and in K2's capture.
- The circle column (x 1160–1220, y 490–690) is identical on the two builds (`n-lu-after-class`, `o-lu-after-class`).

## FINDING 1: dim buttons are dark gold, and buttons behind a box go dim

- **Dim buttons**: K2 draws a dim button's text grey, 131,131,106, on a lighter grey-olive fill. We draw it dark gold, 76,65,28 (6e6b961: 71,58,18) (`cmp-pz-play-dim`). Examples:
  - Play before ten cards are picked (K2 07);
  - End Turn while a set message is up (K2 12).
- **Behind a box**:
  - With "Are you sure you want to use this sidedeck?" up, K2's Play stays lit at 217,186,79. Ours goes dim, 76,65,28 (`cmp-pz09-confirm`).
  - With "The opponent wins the set." up, K2's Stand and Forfeit Game stay lit at 217,187,79. Ours go dim, 74,64,27 (`cmp-pz12-setmsg`).
- This is the same on 6e6b961. It may be related to the known Forfeit centre, but it's a dim state, not a lit button's centre.

## FINDING 2: the box buttons' borders

| Box | Button | K2 | Ours (both builds) |
|---|---|---|---|
| "Are you sure you want to use this sidedeck?" (09) | OK | 217,217,196, 2 px | 132,131,118, 1 px |
| | Cancel | gold, 109,92,43 | **teal**, 29,119,99 |
| "The opponent wins the set." (12) | OK | 217,217,196, 2 px | 154,153,137, 1 px |
| "Do you really want to quit?" (98) | OK | 194,196,177 | 128,134,121 |
| | Cancel | 26,109,90 | 19,76,63 |

- Pazaak's Cancel border is the in-game teal, inside a gold Pazaak box. In K2 it's gold.
- Every OK and Cancel border is dimmer than K2's. That's the reverse of the known "popup lines a little brighter".
- In K2's 12, the OK text is dimmer (136) than ours (196).

## Odd, not filed

- K2's quit box reads "Do you really want to quit? Your progress will not be saved." Ours stops after "quit?".
- With Options open, our Exit Game row keeps a white border while its box is up. K2's 98 lights no row.
- In K2, the card under the pointer on the setup page goes pale (07's +3). Ours doesn't.
- In K2's 12, the player's light is red after the bust. Ours shows both lights grey under the set message.
- Our level-up hub sits in a smaller window over the board; K2's fills the screen. It's the same on 6e6b961.
- My first launch opened the wrong package, because I gave the helper the wrong card name. Nothing was loaded; I stopped it (`loads.txt`).
