# TEST 258: Facing hash 2 (sight for reactions, one range, the save race)

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops, the load log, the race timings, the dev logs (app and Loom), my scripts, my two save tools and my edited copy of the Long Yard are in `KOTOR_RPG_MAIN_WORK/media/screens/test-258/` (dc8ceff9); names in brackets below are files there.

## Build

- **App**: main `82f5745`, a fresh clone. `gate.py --at 82f5745`: "FOR TESTER — CORE at 82f5745, 5967 tests, 0 failed".
- **Loom**: `999614b`, a fresh clone, built.
- **Lodestar**: `9e841f5` in both locks and compiled into both.
- **Shelf**: `37551b0` ("Endar Spire's Command Deck trooper faces west, toward the aft arrival."). check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults, except Snap Shot on Always for step 2 and 3.
- **Saves**:
  - `author_tester_inventory_saves.dart` wrote tester-looter (Looter, Soldier 4, on the Command Deck).
  - `author_tester_snap_saves.dart` wrote snap-one and long-one.
  - `author_tester_test215_saves.dart` wrote sneak-one (Scoundrel 5, Sneak Attack, Stealth 8).
  - No tool writes a Sneak Attack character on the Command Deck, so I wrote two with my own tool (`zz_tester258_saves.dart`, Sneak One's events with the package set to `endar-spire` and a `character.moved`): Back Sneak at (8,4), two squares behind the trooper, and Front Sneak at (4,4), in front of him.
- **Restore copy**: `notes/saves258`. The md5s were logged before each load, with the build (`loads.txt`).
- **Hand edits to the Shelf** for steps 2 and 3 were in `tester-long` only, and I restored it with `git checkout` afterwards. The final edited copy is in the media (`edited-tester-long/`).

## Summary

One finding. Steps 1 to 8 pass.

| # | Check | Result |
|---|---|---|
| 1 | Command Deck before anything moves | **PASS**. A pale arc points west; the hover wedge is behind him (east) and nothing shows in front. |
| 2 | Snap Shot and range 10 | **PASS**. Snap Yard: it fires at about 5 squares. Long Yard (edited): from 23 squares, nothing; from 10 squares, it fires. |
| 3 | A companion at 11 and 10 squares | **PASS** (edited Long Yard). At 11 squares, nothing; at 10 squares, "Snap Shot: Mate attacks Distant". |
| 4 | Hidden step out of reach | **PASS**. Visible, "Sentry catches Sneak One leaving"; hidden, the same step draws nothing. |
| 5 | Unaware from behind | **PASS**. Behind: "+2d6 Sneak Attack 2+1". In front, on the same dice: no Sneak dice. |
| 6 | The save race, three times | **PASS**. Continue 2.0–2.4 s after OK, then a load: the trooper keeps his wounds all three times. |
| 7 | Loom's facing row and Verify | **PASS**. Writes `facing = "north-east"`; south removes the line; a hand-made bad word is refused, and the refusal names all eight. |
| 8 | Save mid-fight and load | **PASS**. Both facings come back as saved. |
| — | A save from before this hash | **FINDING 1**. It loads with no facings at all. |

## FINDING 1: a save written before this hash loads with no facings

- **What shows**: on loading an older save that hasn't been played since, no creature has an arc and the player has no arrow.
  - **Gear Note** (TEST 197's, Command Deck, its snapshot from Oct 24): the trooper has no arc at all (`e-01-back-load`). With Looter, a save with no snapshot, the same trooper has his west arc (`a-01-load`).
  - **Bolt Eighty** (Store Bed, its snapshot from Oct 14): the merchant has no arc on any side (`f-06-ivy-load`, `f-08-bolt-unhover`).
- **After one step it's fine**: I stepped Gear Note once, then loaded it again in a fresh launch. The trooper faced west, with his wedge on hover (`f-01-gearnote`, `f-02c`).
- **Why, as far as I can read it**:
  - These saves' `autosave.world.json` carry `"facing": {}`, and their `logLen` still matches the log.
  - On a load, `play_screen.dart` (12899–12901) clears the facings and fills them only from that snapshot, so nothing gets its file's way.
  - `_inView` (10753) treats a creature with no facing as seeing all round. So until the trooper moves or strikes, he has no back (that part is from the code; I didn't play a blind-spot strike on this save).
  - A step makes the snapshot outdated, so the next load seeds the facings fresh. That fits what I saw.
- **How many**: a check through Lodestar's `readSave` (`zz_snap258.dart`) lists 22 saves in my folder with a matching snapshot and an empty facing map.

## 1. Command Deck (Looter, loaded at the aft arrival; `a-01`, `a-02c`)

- Before anything moved, the trooper's arc pointed west and was pale, 196,196,176. My arrow pointed south.
- With the pointer on him, a pale wedge showed behind him to the east, and nothing changed in front of him (west):
  - its edges are at ±59° from straight behind (120° in all);
  - it reaches 176 px, which is 2.5 squares at 70 px a square;
  - the fill is 50,69,61 over the floor's 18,42,35.
- In TEST 257 the wedge was red, after a fight. Unnoticed, it's pale like his arc.
- He didn't notice me as I walked up to his front, 1 square away. Bumping him opens "This deck is sealed. Turn around."

## 2. Snap Shot and the range of 10

- **Snap Yard** (Snap One, as shipped): after two End Turns, "Snap Shot: Snap One attacks Skirmisher : *hit*" as the Skirmisher left its cover about 5 squares away (`b-03-combat`).
- **Long Yard** (Long One):
  - As shipped, Distant holds its post, so its step off cover never happens. In my copy I made Distant a charger (`doctrines/charger`), removed Frail and moved the arrival.
  - **(a) Arrival (4,2), 23 squares from Distant**: Distant went first, "Distant closes 5 squares — 23 to 18". The Combat log has no Snap Shot, and Reactions still read "three" (`c-01`, `c-02-a-combat`).
  - **(b) Arrival (16,2)**: Distant's first step off cover put it 10 squares away. "Interdiction: Long One attacks Distant : *hit*", 6 damage (`c-04-b-combat`). It's labelled Interdiction because Long One holds all three chains.

## 3. A companion at 11 and 10 squares (my Long Yard copy)

- I added Mate as a companion holding Snap Shot and a Blaster Pistol (level 6), with the player back at (1,2), 25 squares off.
- **(c) Mate at (15,2)**: Distant's first step off cover was 11 squares from Mate. "Distant closes 5 squares — 12 to 7", and Mate made no reaction (`c-07-c-combat`).
- **(d) Mate at (16,2)**: the same step was 10 squares from Mate. "Snap Shot: Mate attacks Distant : *hit*", 7 damage (`c-10-d-combat`).

## 4. Hidden, stepping out of reach (Sneak One)

- **Visible**: I bumped the sentry, and the fight began with me first. Stepping left drew "Sentry catches Sneak One leaving — unarmed … hit · damage 1" (`d-03`).
- **Hidden**, from a fresh load: bump, End Turn (the sentry hit me for 1), then s: "hidden — d20 16 + Stealth 8 + Dexterity 4 = 28 beat 18". The same step left drew nothing, and I stayed at 31 of 32.
- The Combat log ends "Round 2 / Sneak One is hidden." with no catch after it (`d-13`, `d-15-combat`).

## 5. Unaware from behind (Back Sneak, Front Sneak)

- Outside a fight, x answers "nothing is threatening you", and a bump opens the trooper's conversation.
- **Behind**:
  - From (7,4), behind him, the bump opened the conversation, and he didn't turn. "Stand aside." started the fight, and I won initiative 13 to 2.
  - With his arc still west, I pressed x then struck: "Sneak Attack · Vibroblade · rolled 24 — d20 18 … hit · damage 8 — 1d10 4 + Strength 1 +2d6 Sneak Attack 2+1 · 14 left" (`e-13-back-strike`).
- **Front**:
  - From (5,4), in front of him, the same path: initiative 13 to 2, then x and strike.
  - "rolled 24 — d20 18 … hit · damage 5 — 1d10 4 + Strength 1 · 17 left", with no Sneak dice (`e-24-front-strike`).
- **Same dice both times**: d20 18 and d10 4, so only the side I struck from differs.
- The trooper's Dexterity is 10, so the "Dexterity: unaware" term can't show on him.

## 6. The save race (Looter, three runs)

- **The route**: Escape opens Options, then Exit Game, then OK on "Do you really want to quit?". On the menu I clicked Continue on the first frame it lit, using a 20 ms screen grab (`fastcont258.py`).
- **Continue stays dim for about 2 s** after OK while saves are scanned. I clicked it 2211 ms, 2441 ms and 2034 ms after OK (`r1-race.txt` to `r3-race.txt`).

| Run | Before leaving | After Continue | After Load Game > Auto Save |
|---|---|---|---|
| 1 | trooper 17 of 22 | 17 of 22, "round 1, Looter's turn" | 17 of 22 |
| 2 | 17 of 22 | 17 of 22 | 17 of 22 |
| 3 | 3 of 22 (two rounds, and he fired once) | 3 of 22, "round 2" | 3 of 22 |

- Runs 1 and 2 used the same dice, so for run 3 I took a second round to vary it.
- An extra run before run 1 doesn't count: my second hit killed him, and I discarded that run.

## 7. Loom (`999614b`, on a copy of Endar Spire in `kotor-rpg/loom258/`)

- Verify on the clean copy: "Endar Spire · No problems found." (`g-04`).
- The trooper's placement sheet has a facing row of eight: east · south-east · south · south-west · west · north-west · north · north-east, with west lit (`g-06`).
- **north-east** wrote `facing = "north-east"` under the placement. **south** removed the line. Against the Shelf's copy the file then differs only by the missing `facing = "west"` (`g-07`, `g-08`).
- **A bad word by hand**: I wrote `facing = "sideways"` on the copy. Verify gave "2 problems" (`g-09-verify-bad`):
  - the trooper's own: "…says facing = "sideways", which is not a direction. It is one of east · south-east · south · south-west · west · north-west · north · north-east, or leave it out for south.";
  - a knock-on from the same error: the Starboard Hold's door "leads to "a01-command-deck", which this package lists but could not read".

## 8. Save mid-fight and load (Looter, run 3's fight)

- I stepped up, then ended the turn; the trooper fired and turned toward me. My arrow pointed north and his arc north-west. I saved "fight258" as slot 95.
- I stepped left, then loaded row 2, "95 : fight258, Nov 13, 2026 - 13:04:32". The fight resumed at "round 3", with both facings as saved (`cmp-h-facings`).
- Against the frame before the save, the only pixels that differ are in the turn-order strip.

## Odd, not filed

- **A load of the wrong character, not reproduced**: my helper read "Back Sneak" on the panel and loaded row 1, and Gear Note loaded (`e-01`, `loads.txt` 13:05–13:06). Two more tries loaded the right character, one by hand and one through the helper. My helper saves no frame of the panel at the moment it clicks, so I can't say whether that was the app or my tool.
- **Gear Note has changed**: that wrong load let me step it once, so its `.sav` changed (TEST 197's save, not one of mine). Its `.marks` snapshot didn't change.
- **Continue's delay**: Continue stays dim about 2 s after leaving a game. The race is therefore against a 2-second wait, not an instant click.

## What I got wrong

- My card finder opened "Endar Spire — The Opening" first; I cancelled with nothing loaded. I wrote `findpkg3.sh`, which skips a title with more words after "Spire".
- In step 6 my first fight killed the trooper before I left, so I discarded it and stopped after one hit from then on.
- When I loaded Bolt Eighty by hand I first logged it as Ivy Eighty, from my helper's stale read. The panel showed Bolt Eighty; I corrected `loads.txt`.
