# TEST 270: The progress hash

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs and my scripts are in `MAIN_WORK/media/screens/test-270/`. Names in brackets below are files there.

## Build

- **App**: main `3078d99`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Heads**: before the gate I checked every shared tree against origin/main. All were at origin and clean.
- **Gate**: I ran `gate.py --at 3078d99` twice from the project MAIN_WORK (`gate270-1.txt`, `gate270-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 3078d99, 6055 tests, 0 failed".
  - Both state lines: "MAIN_WORK 82ea6064 · HANDOFF bd0bb5a · KOTOR-RPG-APP 3078d99 · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Four Up (`four-200`, Tester Bolt: the player plus three Velas) and a new Wookiee Exile from chargen.
  - The restore copy `notes/saves270` was taken from `saves269`. Its md5s match the last BEFORE lines, and it already held four-200 and its marks (ca0aac5f).
  - Four Up's Auto Save is a dead party ("Your entire party has been killed"), so I loaded its Quick Save (row 2), with a frame at the click.

## Summary

All five steps pass. Nothing to file.

| # | Check | Result |
|---|---|---|
| 1 | HUD Force bars | **PASS**. Main slot: edges 0,217,236, filled 7,130,132. Small slots: filled 7,130,132, with edges up to 3,203,217 at that size. |
| 2 | HUD Vitality | **PASS**. 204,51,0 edge on the main slot, 101,53,24 fill. |
| 3 | Party of four | **PASS**. All four slots draw. The one with empty bars is the player, who is down at 0/12 and has no Force. |
| 4 | Wookiee Exile | **PASS**. No item row; "Aptitude: Survival" with the empty slot. |
| 5 | Play and a fight | **PASS** at 1920. |

## 1–3. The HUD in a party of four (Four Up, in a fight)

`p-01-play`: the main portrait shows the Vela whose turn it is ("Vela is waiting on you"), and three small slots sit on the right.

| Slot | Vitality bar | Force bar |
|---|---|---|
| Main (acting Vela) | 101,53,24 fill, 204,51,0 edge, empty part 13,55,45 | 7,130,132 fill, edges 0,217,236 |
| Small 2 and 3 (Velas) | 101,53,24 fill, edge peaks 198,53,3 | 7,130,132 fill, edge peaks 3,203,217 |
| Small 1 (Four Up) | empty, 13,55,45 | empty, 13,55,45 |

- **Small 1 is the player.** Clicking it opened Equip for "Four Up, Soldier 1", and the Character sheet shows Vitality 0/12 (`c269-click-top`, `c269-fourup-character`). Empty bars are right for a downed Soldier.
- **The small slots' edges** never reach 0,217,236 or 204,51,0, at most 3,203,217 and 198,53,3. They're thin edges blended at that size.
- **No change from 3a554c9**: I loaded the same quick save on build test269 (`c269-play`). The portrait corner (x 1720–1910, y 700–1080) is pixel-identical to 3078d99's.

## 4. A Wookiee Exile (withheld row)

- Wookiee Soldier (it has a Racial Skill step; I took Intimidate), with the Exile background (`w-bg-picked`).
- Equipment's Profession Bonus holds only "Aptitude: Survival", with an empty icon slot. There's no item row, and OK is already lit (`w-equip-bonus`).
- TEST 269's Rodian Exile had a "Neural Band — a save bonus" item row as well, so the item is the part withheld from a Wookiee.

## 5. Play and a fight (1920×1080)

- The fight with four party members (`p-01-play`), and the Wookiee on the Command Deck (`w-play`, Force well empty 13,55,45). Nothing cut off, overlapping or missing.

## What I got wrong

- I copied four-200 from the live dir into the restore copy before noticing `saves269` already held it with its marks. Its md5 was unchanged, and the marks were restored from the copy.
- My chargen script stalled in Skills for the Wookiee (a different point count). I accepted the unspent point and ran the rest by hand.
