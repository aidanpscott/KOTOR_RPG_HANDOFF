# TEST 259: The Opening's facings, the player's own range, and an arrival's facing row

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, the load log (with a frame at every Load click), the dev logs (app and Loom), my scripts, my save tool and my edited copy of the Long Yard are in `KOTOR_RPG_MAIN_WORK/media/screens/test-259/` (7302e4b1); names in brackets below are files there.

## Build

- **App**: main `a8778ce`, a fresh clone. `gate.py --at a8778ce`: "FOR TESTER — CORE at a8778ce, 5971 tests, 0 failed".
- **Loom**: `6ee4c0b`, a fresh clone, built.
- **Lodestar**: `e81b358` in both locks and compiled into both.
- **Shelf**: `3b95e67` ("The Opening's Trask and every Sith face west, toward the door the party enters by."). check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults, except Snap Shot on Always for step 2.
- **Saves**:
  - `author_tester_snap_saves.dart` wrote long-one.
  - For the Opening I wrote Open Walker with my own tool (`zz_tester259_saves.dart`): a Soldier 12 with a Vibroblade in `endar-spire-opening`. It has no `.marks` folder, so the Quarters are entered fresh.
  - I didn't use the old Opening saves (Aptitude Consular and the rest), because their snapshots carry no facings (TEST 258's Finding 1, not fixed on this build).
- **Restore copy**: `notes/saves259`. The md5s were logged before each load, with the build (`loads.txt`). `load222.sh` now saves a frame at each Load click (`loadclick-*`).
- **Hand edits**:
  - `tester-long` for step 2, the same as TEST 258's runs (a) and (b). I restored it with `git checkout`; the copy is in the media.
  - Loom worked on a copy in `kotor-rpg/loom259/`.

## Summary

All four steps pass. Nothing to file.

| # | Check | Result |
|---|---|---|
| 1 | The Opening's five rooms | **PASS**. In every room, on the first frame, Trask's and every Sith's arc points west (179–181°). |
| 2 | Range 10 and ruling (f) | **PASS**. From 23 squares, no Snap Shot; at 10, it fires. |
| 3 | Loom: an arrival's facing | **PASS**. north writes `facing = "north"` and survives a Loom restart; south removes the line and keeps the name. The placement row still works. |
| 4 | Loom: an arrival named "north" | **PASS**. Deleted where no doorway lands on it; refused by name where one does. |

## 1. The Opening (Open Walker, through every door)

- Each arc was measured on a ring around its token (`arcdir.py`), 0° east, 180° west. Each room was captured as I came in, on my own first turn. I won initiative in all four fights, so nothing had moved yet.

| Room | Who | Arcs |
|---|---|---|
| Quarters (load, start) | Trask (2,3) | 180°, pale (`a-01-quarters`) |
| Room 3 (door from the Quarters) | Sith Soldier (7,2), straggler (7,4) | 181°, 180° (`b-01-room3`) |
| Room 4 (door from Room 3) | two Sith (the minion blueprint, named "Sith Soldier") (7,2), (7,4) | 181°, 180° (`c-01-room4`) |
| Hall (door from Room 4) | three Sith Soldiers (8,2), (8,4), (8,6) | 173° each on a ring cutting the token edge; the middle one 179° on the arc itself (`d-01-hall`) |
| Bridge (door from the Hall) | two Sith (6,2), (6,4) | 181°, 179° (`e-01-bridge`, `e-02-bridge`) |

- I cleared each room before going on. Trask didn't follow me out of the Quarters.
- My own arrow pointed south on arriving in each room, because the Opening's arrivals have no facing.

## 2. The player's range of 10 (Long One, my edited Long Yard: Distant a charger, Frail removed)

- **(a) Arrival (4,2), 23 squares from Distant**: "Distant closes 5 squares — 23 to 18". The Combat log has no Snap Shot (`f-02-a-combat`).
- **(b) Arrival (16,2)**: Distant's first step off cover put it 10 squares away. "Interdiction: Long One attacks Distant : *hit*", 6 damage (`f-04-b-combat`).
- The same as TEST 258 on 82f5745. A range of 25 isn't tested here, as ordered.

## 3. Loom: an arrival's facing (Command Deck, arrival "aft")

- The arrival's sheet shows "aft · arrival point · at 1, 3" and a facing row of the same eight words, with south lit (`g-02-aft`).
- **north** wrote `facing = "north"` under `name = "aft"` / `at = [1, 3]` (`g-03-north`).
- **Close and reopen**: a middle click on the area's tab doesn't close it, so I quit Loom, launched it again and reopened the copy. aft's row showed **north** lit (`g-06-reopened`).
- **south** removed the `facing` line. `name = "aft"` stayed, and the area file again matched the Shelf's, apart from the arrival I'd added for step 4 (`g-07-south`).
- **The placement row**: the trooper's row wrote `facing = "east"`, then `facing = "west"` again (`g-09`, `g-10`).

## 4. Loom: an arrival named "north"

- **Where no doorway lands**: I added `[[arrivals]] name = "north"` at (10,6) to the Command Deck copy by hand. I selected it from the tree, and its sheet showed "north · arrival point · at 10, 6", south lit. delete removed it at once, and the file matched the Shelf's again (`h-02`, `h-03`).
- **Where a doorway lands** (the Starboard Hold's own "north", which the Command Deck's door lands on): delete gave "Cannot delete "north": a doorway lands on it — door.command-deck.01 in a01-command-deck. Delete or re-point it first." The file didn't change (`h-05-hold-delete`).
- Verify on the copy afterwards: "Endar Spire · No problems found." (`h-06-verify`).

## Odd, not filed

- **Trask**: his token in the Quarters is drawn red, like an enemy, with a pale arc. His placement sets no side, and Loom shows "enemy" as the default for a placement with none (my reading, not checked for Trask). No fight started.
- **Clicking an arrival on the board**: with a placement's sheet open, the sheet covers the lower half of Loom's board, so a click on an arrival there doesn't reach it. I selected it from the tree.

## What I got wrong

- My first click on the Command Deck's "north" landed under the open trooper sheet and selected nothing.
- In the Hall my strikes carried on after a kill and walked me onto the back arrival, beside the exit door. I went round instead of stepping on.
