# TEST 252: Pazaak

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, checksums (`sha/`), the load log, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-252/` (343ab1d4); names in brackets below are files there.

## Build

- **App**: main `89d68b4`, a fresh clone. `gate.py --at 89d68b4`: "FOR TESTER — CORE at 89d68b4, 5936 tests, 0 failed".
- **Lodestar**: `6fc2738`, compiled into the app. **Loom**: not built, because no step uses it.
- **Shelf**: `ecd0c7b`. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Beds**: `author_tester_pazaak_saves.dart` wrote pazaak-ten, pazaak-full and pazaak-broke with no errors.
- **Restore copy**: every `.sav`, plus `.marks` for dice-one and icons-185. The md5s were logged before each load (`loads.txt`).
- Every step ran on `89d68b4`. TEST 253's order came in while this run was nearly done, so I finished TEST 252 here.

## Summary

One finding: no Pazaak move reaches the Combat log, or any other log I could find. Everything else in 1 to 4, 6 and 7 passes. Step 5 (nine cards) wasn't reached.

| # | Check | Result |
|---|---|---|
| 1a | Friendly game: wager page | **PASS**. "Maximum wager: 40", "Credits: 442". Wager 40 → 39 → 38 → 39 → 40, and + stops at 40. Setup shows +1 to +6 and -1 to -4. |
| 1b | Pick ten | **PASS**. Play is dim at nine and lights at ten. Then "Are you sure you want to use this sidedeck?" with OK and Cancel. |
| 1c | A full match | **PASS**, won 3 sets to 2, with one tie. Each set's message sits over the finished set. The last is replaced by "You have defeated your opponent!" |
| 1c | Who opens | Me, opponent, opponent (after the tie), me, opponent, me. That's alternation, except that a tied set keeps its opener. |
| 1d | Win, then lose | **PASS**. After the win: "Credits Received: 40" (442 → 482). After the loss: "Credits Lost: 25" (482 → 457). |
| 1e | "Just for fun." | **PASS**. No wager page, no popup, credits stay 457. |
| 1f | Forfeit Game | **PASS**. "You have been defeated." at once. |
| 2 | High stakes, Flip and Change | **PASS**. The wager starts at 1000. Flip turns ±3 into -3; Change steps 1±2 through +1, -1, +2, -2. |
| 3 | Broke | **PASS**. Credits 0, the wager stays 0, and Wager is dark and does nothing. |
| 4 | Card Dealer | **PASS**. Bought "Pazaak Card +/-4" for 100 (457 → 357). It's offered as ±4 on the setup page. |
| 5 | Nine cards | Not reached. My most was eight, ending on a tie at 20. |
| 6 | Load in play | **PASS**. The Auto Save row shows the board and party as they are. Checksums are unchanged across opening and cancelling Load. |
| — | The Combat log | **FINDING 1**. |
| 7 | Dice; regression | **PASS**. SAME17. Slot 90 to **92**, fight won, "Experience Points (XP) Received: 75". Slot 91 refused to load because of my restore copy (see "What I got wrong"). |

## FINDING 1: Pazaak moves aren't in the Combat log

- After match 1, Journal > Messages Log: **Combat** is empty, **Dialog** is empty, and **Feedback** holds only "You reached level 3." (`combatlog1`, `log-filter`, `log-dialog`, `log-feedback`, `log-effects`, `log-combat2`).
- The Pazaak screen's own message box, under my hand, stayed empty through the whole match.
- The dev log has no Pazaak line either.
- In the code at 89d68b4, `k2_feedback.dart` lists Pazaak's line shapes ("You draw N · N", "… wins set N · N to N", and so on). But `_loggedLines()` in `play_screen.dart`, which fills the Messages screen, writes Combat lines only from fight events and the fight's round log. `pazaak_screen.dart` never mentions a log. So nothing seems to carry `PazaakMatch.log` to any screen.
- So I can't copy the app's log of a match. Below is **my own reading of the frames** (`m1-*`), not the app's words.

### Match 1, read from the frames (Pazaak Ten, friendly, wager 40)

My side deck: +1 to +6 and -1 to -4. My hand: +5, +1, -4, -3.

- **Set 1** (I open): I draw 5 (5); opp draws 2 (2); I draw 3 (8); opp draws 10 (12); I draw 2 (10); opp draws 4 (16); I draw 8 (18), and I stand. Opp draws 4 (20). "The opponent wins the set."
- **Set 2** (opp opens): opp draws 10; I draw 5; opp draws 5 (15); I draw 3 (8); opp draws 5 (20); I draw 7 (15) and play +5 (20).
  - A second side card (+1) in the same turn does nothing; it stays in my hand at 20 (`m1-s2-second-card`).
  - I stand. "The set is tied."
- **Set 3** (opp opens again after the tie): opp 3, me 4; opp 4 (7), me 3 (7); opp 5 (12), me 2 (9); opp 3 (15), me 6 (15).
  - Opp draws 9 (24) and plays **-6** (18), saving the bust.
  - I draw 5 (20) and stand. "You win the set."
- **Set 4** (I open): me 4; opp 6, me 3 (7); opp 10 (16), me 10 (17).
  - I end the turn. Opp draws 8 (24) and busts with three side cards still in hand. "You win the set."
- **Set 5** (opp opens): opp 5, me 3; opp 5 (10), me 2 (5); opp 4 (14), me 4 (9).
  - Opp draws 4 (18) and plays **+2** (20).
  - I draw 6 (15), then 1 (16), then 7 (23). I end the turn at 23, which is a bust. "The opponent wins the set."
- **Set 6** (I open): me 6; opp 3, me 4 (10); opp 2 (5), me 10 (20). I stand.
  - Opp draws 10 (15), then 10 (25), and busts. "You have defeated your opponent!" I win 3 sets to 2.
- The opponent played a side card twice, once to save a bust and once to make exactly 20. In set 4 it busted at 24 with three side cards in hand; I can't see whether any of them could have saved it.
- The +5 I played was gone from my hand for the rest of the match.

## 2. Pazaak Full, High stakes

- The wager page: 1000, "Maximum wager: 1000", "Credits: 2000" (`full-wager`).
- The setup page has two each of +1 to +6, -1 to -6, ±1 to ±6, ±1T, D, 2&4, 3&6 and 1±2. I chose two each of ±1 to ±4, plus two 1±2.
- The 1±2 help line reads: "Before playing this card, you can change its value to 1, 2, -1 or -2."
- My hand: ±3, ±1, 1±2, 1±2. Each card has a cycle icon under it. The legend reads "Flip Hand Card" and "Change Card Value" (`full-start`).
- **Flip**, under ±3: +3 becomes **-3**, and the card turns red with a minus (`full-flip1`). I played it at 12 → 9, then later flipped ±1 to -1 and played it at 21 → 20 (`full-play-flip`, `full-flip2`).
- **Change**, under 1±2: each click steps **+1 → -1 → +2 → -2 → +1** (`full-change1` to `full-change4`). I set it to +2 and played it, 5 → 7 (`full-play-change`).
- Once only the 1±2 was left, the legend showed only "Change Card Value".
- Set 1 tied at 20, with eight cards on my side. Set 2 I opened again, so the tie kept the opener. I forfeited it, and the popup read "**Credits Lost: 1000**" (`full-pop`).

## 3. Pazaak Broke

"Maximum wager: 40", "Credits: 0", and the wager is 0. Wager is dark, + leaves it at 0, and clicking Wager does nothing (`broke-wager`, `broke-clicked`).

## 4. The Card Dealer (Pazaak Ten)

- "Card Dealer: Pazaak cards, every kind there is." Then "1. Show me your cards." opens Buying Items, which lists every card (`dealer-store`, `dealer-scroll`).
- "Pazaak Card +/-4": "This is a standard pazaak side deck card, for use with a pazaak deck."
  - Before buying: Item Cost 100, Credits 457, In Stock Infinite, In Inventory 0.
  - After Buy Item: Credits 357, In Inventory 1 (`dealer-sel`, `dealer-bought`).
  - No popup when I left.
- The player's setup page then shows a **±4** card under -4 (`dealer-setup`).

## 6. Load in play (Pazaak Ten, after the matches and the purchase)

- Checksums before, twice 5 s apart, then with Load open, after Cancel, and after Close: pazaak-ten `562d1d10f39421f6` and all saves `89f6b1588bbc8c63` each time (`sha/summary.txt`).
- The Auto Save row reads Nov 11, 16:50:45, which is the time the `.sav` was last written (leaving the last conversation). Its board picture has me beside the Pazaak Player at (1,0), and its party is Pazaak Ten alone, as on the board (`load-list`).

## 7. Dice and regression

- **Dice**: the right Dice One Quick Save (Oct 19, 07:40:30); SAME17 (`dice.out`).
- **Regression**: slot 91 (reg251) refused to load: "THIS SAVE WILL NOT OPEN … Its history is damaged: a step back in it points at a moment the save does not hold." (`slot91-refused`). That's my doing (below).
- I loaded slot 90 and saved "reg252", which took **slot 92**. Then a quick save, a load of slot 92, and the win: "Experience Points (XP) Received: 75" (`xp-end3`).

## Odd, not filed

- Quit on the wager page goes back to "Good game. Up for another?", though no game was played.
- The Flip and Change icons under the hand cards stay grey; only the legend has yellow and green.
- The Messages Log's Dialog tab was empty after several Pazaak conversations.

## What I got wrong

- **The slot 91 refusal is mine.** For TEST 251's restore copy I added only `000091.mark`, and kept the older `icons-185.sav`. A mark needs the `.sav` it was saved against. This run's restore then overwrote the live `.sav` that matched slot 91, so slot 91 is gone for good.
- I've now kept the live icons-185 `.sav` and `.marks` together (`notes/icons-185-after252`). The next step is slot 92 to 93.
- I reread the score boxes by eye, because my OCR misread single digits.
