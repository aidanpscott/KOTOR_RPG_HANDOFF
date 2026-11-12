# TEST 255: The store, the button centres, the popup line and the Pazaak log

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops (`cmp-*`), every reading (`px.txt`), the match's action logs, the load log, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-255/` (e7a73a51); names in brackets below are files there.

## Build

- **App**: main `da46ed5`, a fresh clone. `gate.py --at da46ed5`: "FOR TESTER — CORE at da46ed5, 5942 tests, 0 failed". The gate also printed "pazaak.started is READ and NOTHING CONSTRUCTS IT", among other warnings.
- **Lodestar**: `6fc2738`, compiled into the app. **Loom**: not built, because no step uses it.
- **Shelf**: `e466b46`. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Beds**: `author_tester_pazaak_saves.dart` wrote pazaak-ten, pazaak-full and pazaak-broke with no errors.
- **Restore copy**: `notes/saves255`. The md5s were logged before each load, with the build of each launch (`loads.txt`).
- **Comparison**: c961987 frames are TEST 254's `n-` frames, plus `nb-table*` taken today. da46ed5 frames start `d-`, `db-`, `m-`, `m2-` and `f-`.
- **The machine rebooted** at 20:33, before my first launch, and my Xvfb `:2` was gone. The first launch found no window, and nothing was played. I restarted Xvfb (1920x1080x24) and began again.

## Summary

One finding: on da46ed5, Pazaak's setup page and table draw with no art. Steps 1, 3 and 4 pass. Step 2 passes for Forfeit Game, but End Turn and Stand can't be measured, because they aren't drawn.

| # | Check | Result |
|---|---|---|
| 1 | Store gold lines, 2 px at about 96,82,39 | **PASS**. Every box and button line is now 2 px at 96,82,39 (K2 96,82,39 then 100,86,40). c961987 was 1 px at 109,93,44. |
| 2 | End Turn, Stand, Forfeit centres about 129,111,47, and the profile | **Forfeit PASS**: its centre is 129,111,47 (K2 130,112,47; c961987 107,92,39). **End Turn and Stand BLOCKED** by Finding 1. |
| 3 | Exit Game box line 1 px at 25,106,87; page lines stay 29,119,99 | **PASS**. The box is 1 px at 25,106,87 on all four sides. The page lines are still 29,119,99. |
| 4 | The Pazaak log in Feedback; reload; forfeit | **PASS**. Every move of a three-set match is there, in order, matching the table at each set's end. The lines survive a reload. The forfeit logs its own line. |
| — | Pazaak screens draw without their art | **FINDING 1**. |

## FINDING 1: Pazaak's setup page and table draw with no art on da46ed5

- **What shows**: a black screen with only the boxes, their text, and two buttons, Clear Cards and Forfeit Game (`cmp-table-c961987-vs-da46ed5`, `d-04-wager`, `d-07-setup3`, `d-09-sure`).
- **What's missing**: the metal panel, every card on the setup page and the table, the hands, the score boxes, and End Turn and Stand.
- **While a set or match box is up**, the whole table draws, cards and all (`d-12-setmsg`, `m2-001`, `m2-006`, `m2-011`). After OK it goes black again.
- **After the match**, the board comes back with a stray Forfeit Game button drawn over its bottom right (`m2-012`).
- **Clicks still work**: I played a whole match and a forfeit without seeing the table.
- **It happened in all three da46ed5 launches.** The drawn-pixel count is 19,266 on the black table, against 1,813,936 on c961987's (`px.txt`).
- **c961987 draws every screen in full** on this same Xvfb, with the same save and the same clicks (`nb-table0` to `nb-table2`, then `db-table0` to `db-table2`).
- The dev log has no error.

## 1. The store (Card Dealer, against `k2-capture-run/03a`)

Each line is scanned across, one pixel at a time:

| Line | K2 | c961987 | da46ed5 |
|---|---|---|---|
| Title box, top | 96,82,39 then 100,86,40, soft edges | 109,93,44, 1 px | 96,82,39, 2 px |
| Title box, left | 96,82,39 then 100,86,40 | 109,93,44, 1 px | 96,82,39, 2 px |
| List box, left | 96,82,39 then 100,86,40 | 109,93,44, 1 px | 96,82,39, 2 px |
| Description box, top | 96,82,39 then 100,86,40 | 109,93,44, 1 px | 96,82,39, 2 px |
| Cost box, top | 96,82,39 then 100,86,40 | 109,93,44, 1 px | 96,82,39, 2 px |
| Close and Buy Item, top | 96,82,39, 2 px | 109,93,44, 1 px | 96,82,39, 2 px |
| Row lines | 98,83,39 then 100,84,39, 2 px | 109,93,44 | 96,82,39 |

- The gold text, the Filter tab, the line under the tabs and the line above the buttons are the same as on c961987 (`px.txt`).
- Two small differences:
  - The fill inside the boxes is now 30,27,11 (c961987: 33,29,12; K2: 33,28,12).
  - Where two of our rows touch, the bottom line of one and the top line of the next make a band 3 to 4 px wide (y 357–361). K2 leaves a 2 px gap between rows.

## 2. The Pazaak buttons (against `k2-pazaak/14`)

Forfeit Game, scanned across at y 944–947, every 25 px (`cmp-pz-buttons`). Each is the median of a 4 px tall strip:

| x | K2 | c961987 | da46ed5 |
|---|---|---|---|
| 1083 | 24,23,8 | 9,9,3 | 10,11,4 |
| 1158 | 60,51,23 | 34,29,12 | 41,35,15 |
| 1233 | 94,80,34 | 65,57,24 | 79,69,28 |
| 1308 | 119,102,43 | 94,80,34 | 113,96,41 |
| **1358 (centre)** | **130,112,47** | **107,92,39** | **129,111,47** |
| 1408 | 122,104,45 | 98,84,36 | 118,101,43 |
| 1483 | 98,84,36 | 71,62,26 | 86,74,31 |
| 1558 | 66,57,24 | 40,34,15 | 48,41,17 |
| 1633 | 29,26,10 | 12,11,4 | 14,13,5 |

- The centre now matches K2. Away from it, ours is darker than K2: 12 darker at x 1483, 18 at 1558, and 19 at 1158. That's the known falloff.
- End Turn and Stand aren't drawn on da46ed5 unless a box is up, and behind a box they're dimmed (75,64,27, as on c961987). So I couldn't take their lit profile on this build. c961987's End Turn centre was 105,91,38 (K2 129,111,47).

## 3. The in-game Exit Game box (against `k2-ingame/98`)

| Line | K2 | c961987 | da46ed5 |
|---|---|---|---|
| Box top | 25,109,90, 1 px | 29,119,99, 1 px | **25,106,87**, 1 px |
| Box left | 25,106,87, 1 px | 29,119,99 | **25,106,87** |
| Box bottom | 25,109,90 | 29,119,99 | **25,106,87** |
| Line under the icons (y 189–191) | 27–30,112–125,93–104 | 29,119,99 | 29,119,99 |
| Save Game row, top | 26,106,88 | 29,119,99 | 29,119,99 |

- The box's line is now K2's colour. The page lines didn't change. The OK and Cancel borders and the text are as in TEST 254 (known) (`cmp-exit-corner`).

## 4. The Pazaak log (Pazaak Ten, friendly, wager 40)

**How I played it.** The table wasn't drawn (Finding 1), so I played on a fixed plan:
- one side card on my first turn;
- End Turn on turns 1 and 2, and Stand on turn 3 (`blind255.sh`, `m-actions.txt`, `m2-actions.txt`).

At each set's end, the box frame shows the whole table, so I checked the log against those frames (`m2-001`, `m2-006`, `m2-011`).

**The match** (I lost 0 sets to 3). Journal > Messages Log > Feedback, after the match (`m-feedback1` to `m-feedback4`):

- Set 1:
  - "You draw 5 · 5", "You play +5 · 10", "You end the turn at 10".
  - "Opponent draws 2 · 2", "Opponent ends the turn at 2".
  - "You draw 3 · 13", "You end the turn at 13".
  - "Opponent draws 10 · 12", "Opponent ends the turn at 12".
  - "You draw 2 · 15", "You stand at 15".
  - "Opponent draws 4 · 16", "Opponent ends the turn at 16".
  - "Opponent draws 8 · 24", "Opponent plays -6 · 18", "Opponent stands at 18".
  - "Opponent wins set 1 · 0 to 1".
- Set 2:
  - "Opponent draws 10 · 10", "Opponent ends the turn at 10".
  - "You draw 6 · 6", "You end the turn at 6".
  - "Opponent draws 4 · 14", "Opponent ends the turn at 14".
  - "You draw 8 · 14", "You end the turn at 14".
  - "Opponent draws 2 · 16", "Opponent ends the turn at 16".
  - "You draw 10 · 24", "You bust at 24".
  - "Opponent wins set 2 · 0 to 2".
- Set 3:
  - "You draw 1 · 1", "You end the turn at 1".
  - "Opponent draws 8 · 8", "Opponent ends the turn at 8".
  - "You draw 5 · 6", "You end the turn at 6".
  - "Opponent draws 2 · 10", "Opponent ends the turn at 10".
  - "You draw 9 · 15", "You stand at 15".
  - "Opponent draws 3 · 13", "Opponent ends the turn at 13".
  - "Opponent draws 8 · 21", "Opponent plays -3 · 18", "Opponent stands at 18".
  - "Opponent wins set 3 · 0 to 3".
- "Opponent wins the match, 3 sets to 0".

**Against the table at each set's end:**
- Set 1: my cards 5, +5, 3, 2, score 15. The opponent's 2, 10, 4, 8, -6, score 18. "The opponent wins the set."
- Set 2: mine 6, 8, 10, score 24; the opponent's 10, 4, 2, score 16.
- Set 3: mine 1, 5, 9, score 15; the opponent's 8, 2, 3, 8, -3, score 18. "You have been defeated."
- Every card, total and order agrees with the log, including both of the opponent's side cards. Set 1 opened with me, set 2 with the opponent, and set 3 with me.
- In set 2 I pressed Stand at 24. The log calls that "You bust at 24".

**Reload.** I left the conversation and closed "Credits Lost: 40". Then Options > Load Game, the only row: "Auto Save, Nov 11, 2026 - 21:41:18", the time the `.sav` was last written. After the load, Feedback holds the same lines, from "Set 1" to "Opponent wins the match, 3 sets to 0" (`m-reload-fb1`, `m-reload-fb2`).

**Forfeit.** Another friendly game: credits 402, wager 40. I forfeited after my first draw ("You have been defeated." over a table at 5 to 0). Feedback adds "Set 1", "You draw 5 · 5", "You forfeit the match". The popup reads "Credits Lost: 40" (`f-wager`, `f-defeated`, `f-feedback`, `f-popup`).

**Pazaak Full**: not used. Its setup page draws no cards on da46ed5 either, so I couldn't choose a side deck by sight. Pazaak Ten covers every kind of line the order lists.

## Odd, not filed

- The Load list's picture of that Auto Save shows me beside the Pazaak Player at (1,0), but the load put me on the start square at (0,0).
- No line marks a new match: the forfeit match's "Set 1" follows straight on from "Opponent wins the match".
- The dev log doesn't record a load, so I confirmed the reload from the board: I was moved to the start square, and the area's name showed again as it does on entering.

## What I got wrong

- My first match runner never moved, because I hadn't made the score reader executable. I deleted those frames and started again from the same table.
- My set-box check (taken from TEST 254) looked for an OK border brighter than the real one, so it missed the first set message. The runner pressed Stand 77 more times, which did nothing, while the box was up. I switched the check to the box's gold line, and the match carried on from that box (`m-actions.txt`, then `m2-actions.txt`). In TEST 254, that check had also never fired; I'd taken its frames after a fixed number of turns.
