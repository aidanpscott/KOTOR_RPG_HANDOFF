# TEST 257: Facing hash 1 and TEST 256's fixes

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, side-by-side crops (`cmp-*`), every reading (`px.txt`), the match logs, the load log, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-257/` (10218955); names in brackets below are files there.

## Build

- **App**: main `0af500f`, a fresh clone. `gate.py --at 0af500f`: "FOR TESTER — CORE at 0af500f, 5958 tests, 0 failed".
- **Lodestar**: `3386f72` in the app's lock and compiled in. **Loom**: not built, because no step uses it.
- **Shelf**: `286f416` ("dialogue.node-reached is campaign, so a save keeps the lines the Dialog tab shows"). check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Settings**: defaults.
- **Saves**:
  - `author_tester_pazaak_saves.dart` wrote pazaak-ten, pazaak-full and pazaak-broke.
  - `author_tester_test208_saves.dart` wrote proof-equal (Casters' Hall: Caster as companion, and the Thug).
  - `author_tester_test215_saves.dart` wrote power-one (Power Yard: Thug, Gunner, Treaded Droid; Power Attack's knockdown).
  - None of these tools writes a save that has both a Sith Trooper and the Thug. For the blind spot I used `farone-219.sav` (TEST 219's Far Hall), whose Sith Trooper is the same blueprint with `blind_spot = 120`.
- **Restore copy**: `notes/saves257`. The md5s were logged before each load, with the build (`loads.txt`).
- Pazaak Ten's leftover `.marks` folder from TEST 256 (my dlg256 and Auto Save) was removed before the first load, so the bed started clean.

## Summary

All four steps pass. Nothing to file. A few odd items are listed at the end.

| # | Check | Result |
|---|---|---|
| 1 | Dialog after a load | **PASS**. All three lines, with speakers, after the Auto Save and after a named save (slot 94, "dlg257"), loaded in a fresh launch. |
| 2 | Match line | **PASS**. "Pazaak with Pazaak Player · wager 40" just before "Set 1"; the moves say "Opponent". The second match opens with its own line, straight after "Opponent wins the match, 3 sets to 0". |
| 3 | Setup hover | **PASS**. The +3 and a Chosen +3 fade and keep the plus sign, blue bands and value box, within 12 of K2's 07 except the plus badge (14). The -1's description wraps after "your", each line centred, on K2's 08 pixels. |
| 4 | Facing | **PASS**. Every item. Details below. |

## 1. Dialog after a load (Pazaak Ten)

- I stepped right once, walked into the Pazaak Player, chose "5. Not now.", then "1. [Leave.]".
- Before the load, Journal > Messages Log > Dialog read (`a-06-dialog-before`):
  1. "Pazaak Player: Care for a game of pazaak?"
  2. "Pazaak Ten: Not now."
  3. "Pazaak Player: Come back any time."
- **Auto Save**: Options > Load Game, row 1, "Auto Save, Nov 13, 2026 - 08:33:52". After the load, the area's name showed again, and Dialog held all three lines (`a-08-afterload`, `a-09-dialog-after`).
- **Named save**: I saved "dlg257" (slot 94). Then I closed the app, launched it again, and loaded row 2, "94 : dlg257, Nov 13, 2026 - 08:35:43", from the package menu. Dialog held all three lines (`a-14-row2`, `a-16-dialog-after2`).

## 2. The match line (Pazaak Ten, friendly, wager 40)

- I played two matches back to back (`m1-actions.txt`, `m2-actions.txt`). The second was started from "Up for another?". Its wager page read "Credits: 402", so the first had cost 40 (`c-04-wager`). After the second, "Credits Lost: 80".
- Journal > Messages Log > Feedback (`d-fb1` to `d-fb7`):
  - "You reached level 3." then **"Pazaak with Pazaak Player · wager 40"**, then "Set 1", "You draw 5 · 5", "You play +5 · 10", ...
  - Every move says "You" or "Opponent".
  - After match 1's last lines, "Opponent wins set 3 · 0 to 3" and "Opponent wins the match, 3 sets to 0", comes **"Pazaak with Pazaak Player · wager 40"**, then "Set 1", "You draw 3 · 3", "You play +2 · 5", ... (`d-fb5`).

## 3. Setup hover (against `k2-pazaak/07` and `08`)

**The +3, with the pointer on it** (`b-07-hover-plus3`; `cmp` in `px.txt`). It's faded with its plus sign, blue bands and value box showing through, as in K2's 07. Medians of each part:

| Part | K2 07 | Ours |
|---|---|---|
| Top band | 139,149,169 | 135,148,174 |
| Value box | 129,129,117 | 122,123,107 |
| Bottom band | 140,151,173 | 136,150,179 |
| Card face | 173,165,148 | 180,170,145 |
| Plus badge | 176,178,176 | 188,192,182 |

- Everything is within 12, except the plus badge: 12 to 14 brighter.
- The brightest pixels: the value box's matches exactly (187,176,155). The top band's and the badge's are 19 brighter (223 against 204).

**A Chosen card**: the Chosen column's +3 under the pointer reads the same as the available +3, part for part (`b-08-hover-chosen-plus3`).

**The -1 and the description** (`b-08-hover-minus1`, `b-08-hover-minus4`):
- "When you play a negative card, its value is subtracted from your" / "score.", wrapped after "your".
- Both lines span the same pixels as K2's 08: x 208–860 and x 510–559, each centred at 534. Ours sits 2 px lower (y 859 against 857).

**The red card against K2's 08**: K2's 08 hovers the -4, so I compared ours at the same card.
- Ours is about 15 brighter: bands 189 and 193 against 174 and 178, and the face 180 against 165.
- K2's own two captures disagree on the same pale face by 8 (173 in 07, 165 in 08). So I can't tell how much of the 15 is ours.

## 4. Facing

**Walking** (Proof Equal, Casters' Hall; `cmp-walk`, `cmp-walk2`, `cmp-walk3`):
- My teal arrow pointed along each step (up, left, down, down, right, right) and stayed that way after I stopped.
- On load, before any step, no one had an arrow (known).

**A following companion**:
- Caster (teal) stayed put while it was already next to me.
- When I walked away it followed: right, down, right, right. Its arrow pointed along each of its own steps, not mine. For example, after my second step right, Caster stepped down and its arrow pointed down (`e-9c-crop`).

**In a fight**:
- **Casters' Hall**: the Thug struck me and its red arc turned toward me (`f-03-after-thug`). My arc stayed toward the Thug. Caster's stayed the way it last walked.
- **Power One**: at the start of the fight, the Gunner (above), Thug (right) and droid (below) each struck me. All three red arcs pointed at me (`h-02-bump`).
- **Turning to strike**:
  - I Power Attacked the Thug on my right, and my arrow pointed right (`h-03-strike-thug`).
  - Next turn I struck the Gunner above me without moving, and my arrow turned up (`h-06-strike-up`).
- **Knockdown and Force Push**:
  - The Power Attack knocked the Thug prone and threw it from (5,4) to (8,4). Its arc still pointed left, the way it faced before, and still did after it got up (`h-03`, `h-05`).
  - In the Casters' Hall, my Force Push threw the Thug from (3,1) to (1,1), "stunned". Its arc still pointed right, the way it faced before the push (`g-02-push-target`).

**The blind spot** (Far Hall, Sith Trooper; `cmp-wedge`):
- I struck the trooper and it shot back, so its arc points left at me.
- With the pointer on it, a faint red wedge shows behind it, to its right. Hovering the Thug, which has no blind spot, shows no wedge (`g-03c`).
- Measured against the frame without the pointer:
  - the wedge's lower edge is at 60° from the facing line, half of 120°;
  - it reaches 147 px, which is 2.5 squares at 59 px a square;
  - the fill is 41,28,23 over the floor's 11,23,18.
- The trooper's hover card and tooltip cover the wedge's upper half.

**Save and load mid-fight** (Proof Equal):
- With the Thug's arc toward me, mine toward it and Caster's right, I saved "fight257" (slot 94).
- I then stepped up, which turned my arrow up, and loaded row 2, "94 : fight257, Nov 13, 2026 - 09:11:16".
- "the fight resumes — round 2". Every facing was back as saved: mine left, the Thug's right, Caster's right (`f-11-after-load`).

## Odd, not filed

- **The Auto Save picture**: after my step in the Casters' Hall, Load Game drew the Auto Save row's picture with me on my new square. The stored `autosave.png` and the `.sav` were unchanged, and still showed me on the old square (`f-09-loadlist`, `f-10b-autosave-file`). I didn't load the Auto Save, so I don't know where it would have put me.
- **Grise isn't in the Load list**: the card titled "Endar Spire — The Opening" lists 11 characters. Grise (`tester-force-grey`), whose save names the `endar-spire` package, isn't among them. That's why I used Far One for the blind spot.
- **"[Leave.]"** still isn't in the Dialog tab (with Coder).

## What I got wrong

- I gave the package finder a save name instead of the card name, so it scrolled through the library and opened Tester Throw. I relaunched and loaded correctly. Nothing was loaded from the wrong package.
- My load helper's OCR read "PrRooF EQUAL" and gave up on Proof Equal, so I picked it by hand (logged).
- My first try at Grise opened "Endar Spire — The Opening" and found no Grise. I cancelled without loading (`loads.txt`, 09:15:47 has no AFTER line).
