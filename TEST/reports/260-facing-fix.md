# TEST 260: The facing fix

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames (with one at every Load click), the load log, the dev logs (app and Loom) and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-260/` (cac86fd8); names in brackets below are files there.

## Build

- **App**: main `ec3fde2`, a fresh clone. `gate.py --at ec3fde2`: "FOR TESTER — CORE at ec3fde2, 5976 tests, 0 failed".
- **Loom**: `eb3aa63`, a fresh clone, built.
- **Locks**: Lens `e449221` and Lodestar `e81b358` in both locks, and compiled into both.
- **Shelf**: `667d1ba` ("Trask is of the Republic, the player's side."). check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Saves** (restore copy `notes/saves260`; md5s logged before each load, with the build, in `loads.txt`):
  - **Old saves**, from my folder with their own `.marks`, unchanged: Bolt Eighty (from `notes/saves258`), Pr Remote, C79 Battle, Stun Three.
  - **Gear Note**: TEST 258 had stepped it. I rewrote its `.sav` with `author_tester_test197_saves.dart` into a scratch folder and copied back only `gear-note.sav`. That gives 16 events, which matches its untouched Oct 24 snapshot (`logLen` 16), so it's an old unplayed save again.
  - **Mine from earlier tests**: Looter, Back Sneak and Open Walker.
  - **Pazaak Ten**: rewritten by `author_tester_pazaak_saves.dart`.
- **My Xvfb died between tests**: the first launch (Nov 13, 18:25) found no display, so nothing loaded. I restarted Xvfb detached on Nov 14 and began again (`loads.txt`).

## Summary

All six steps pass. Nothing to file.

| # | Check | Result |
|---|---|---|
| 1 | Old saves, no step | **PASS**. The trooper's arc points west and his wedge shows behind him. The merchant's arc points south. Pr Remote, C79 Battle and Stun Three show an arc on every creature. |
| 2 | A save after a turn | **PASS**. The trooper turned north, I saved, stepped, and loaded: his arc stays north, not his file's west. |
| 3 | The talk turn | **PASS**. From behind, the trooper turns east to face me, I face west, and his wedge is behind him to the west. The Pazaak Player, from his west side, turns west, and I face east. |
| 4 | Sides | **PASS**. Trask in the Quarters is pale on edge and arc; Room 3's Sith are red on both; after joining, Trask is teal on both. |
| 5 | Loom's board beside the sheet | **PASS**. The board doesn't move when the sheet opens, and a bottom-row arrival selects with the sheet open. |
| 6 | Load list | **PASS**. In every Load-click frame, the panel names the character that loaded (10 loads, 9 different saves). |

## 1. Old saves, loaded with no step taken

- **Gear Note** (Command Deck):
  - The trooper has a pale arc pointing west (179°), and my arrow points south (`a-01-gearnote`). In TEST 258 this load showed neither.
  - With the pointer on him, his wedge is centred at 0° (behind him, east), 119° wide, reaching 176 px, which is 2.5 squares at 70 px. The fill is 51,70,62 (`a-02c`).
- **Bolt Eighty** (Store Bed; loaded by hand, because my helper's OCR can't read "Bolt"): the merchant has a pale edge and a pale arc pointing south, since his file sets no facing (`b-01-bolt`). In TEST 258 he had none.
- **Pr Remote** (Tester Probe's Probe Room): every creature has an arc pointing south, red on red tokens and pale on pale ones (`b-02-prremote`). Three teal letter tokens have no arc. They're the bed's deliberately broken placements (two blueprint paths that don't open, and the empty "zoo" creature), and none of them is a combatant in the snapshot.
- **C79 Battle** (Tester Rough Ground, saved mid-fight on Oct 13): both Sentry Droids have red arcs, and Kael and I have teal arcs, all pointing south (`b-03-c79`).
- **Stun Three** (Rx Stun Bed): the enemy has a red arc, and I have a teal arrow, both pointing south (`b-04-stun`).

## 2. A save made after a turn (Looter, from a fresh load)

- I walked to (6,3), above the trooper, and talked. He turned north to face me.
- "Stand aside." started the fight, and he fired at me ("Blaster Rifle … miss").
- I saved "turn260" (slot 95), stepped left so my own arrow turned, then loaded row 2, "95 : turn260, Nov 14, 2026 - 08:43:27".
- His arc points north as he turned, not west as in his file. Mine points south as saved (`cmp-c-turned`).

## 3. The talk turn

- **The trooper from behind** (Back Sneak; she stepped from (8,4) to (7,4), behind him, and bumped him):
  - "This deck is sealed. Turn around." He turned east, with his pale arc at 2°, toward me. I turned west, at 180°.
  - Hovering him during the talk, his wedge is centred at 180°, behind him and away from me, 120° wide, reaching 206 px, which is 2.5 squares at 82 px in the talk layout (`d-02-talk`, `d-04-hover`).
- **The Pazaak Player from one side** (Pazaak Ten; he stands at (2,0), facing south by default):
  - I stepped to (1,0), his west side, and bumped him: "Care for a game of pazaak?". He turned west (180°) and I turned east (0°).
  - The dealer, who isn't in the talk, still faces south (`d-12-talk`).

## 4. Sides (Open Walker, the Opening)

- **Quarters, before he joins**: Trask's token edge and arc are both 196,196,176, pointing west (`e-01-trask-zoom`).
- **Joining**: I talked to him (he turned to face me), then chose "Who are you?", "[Continue.]" and "Okay, let's go help Bastila!". "Trask Ulgo is with you now."
  - His token became a teal "T", with edge and arc both 143,216,196 (`e-03-joined`).
- **Room 3**: both Sith, who see me, are 176,52,42 on edge and arc (`e-05-room3`). Trask came through the door with me, teal on both, his arc pointing south like mine.

## 5. Loom (`eb3aa63`, on a copy of Endar Spire in `kotor-rpg/loom260/`)

- I added an arrival "low" at (5,7), the bottom row, to the copy's Command Deck by hand.
- The board now sits in the left half of the work pane at about 31 px a square, whether or not a sheet is open (`g-01-area`).
- **Opening the trooper's sheet**: the sheet is drawn to the right of the board. Comparing the board region before and after, the only pixels that changed are the selection ring on the trooper (`g-02-sheet`).
- **With the sheet still open**, clicking "low" in the bottom row selected it: "low · arrival point · at 5, 7", with its facing row (`g-03-low`).

## 6. The Load list (a frame at every Load click)

| Frame | Panel | Row clicked | What loaded |
|---|---|---|---|
| `loadclick-082552` | Gear Note | Auto Save | Gear Note |
| `loadclick-083326-bolt` | Bolt Eighty | Auto Save | Bolt Eighty |
| `loadclick-083548` | Pr Remote | Auto Save | Pr Remote |
| `loadclick-083801` | C79 Battle | Auto Save | C79 Battle |
| `loadclick-084014` | Stun Three | Auto Save | Stun Three |
| `loadclick-084223` | Looter | Auto Save | Looter |
| `loadclick-084352-turn260` | Looter | 95 : turn260 | Looter, at turn260 |
| `loadclick-084555` | Back Sneak | Auto Save | Back Sneak |
| `loadclick-084952` | Pazaak Ten | Auto Save | Pazaak Ten |
| `loadclick-085133` | Open Walker | Auto Save | Open Walker |

- The loads covered seven cards: Endar Spire, Store Bed, Tester Probe, Tester Rough Ground, Rx Stun Bed, Tester Pazaak and Endar Spire — The Opening. No delete was involved, as ordered.

## Odd, not filed

- **"My mistake." loops**: in the trooper's conversation, "6. My mistake." brings his first line back. The dialogue file authors it that way (`then = ["this-deck-is"]`), so there's no way to end that conversation peacefully from it. Escape does nothing in a conversation, by ruling, so I closed the app.
- **Trask's arrow in Room 3**: Trask came in facing south, the arrival's way, like me. Only the Opening's creatures face west.

## What I got wrong

- I didn't notice my Xvfb had died after the crash restart, so the first launch ran with no display. I now start it detached and record its own PID (my first PID was my own shell's).
- My helper's OCR failed on "Bolt Eighty", so I loaded it by hand, with a frame.
