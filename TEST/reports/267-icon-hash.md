# TEST 267: The icon hash

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the two authored scratch saves are in `MAIN_WORK/media/screens/test-267/`. Names in brackets below are files there.

## Build

- **App**: main `6506e9c`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Heads**: before the gate I checked every shared tree against origin/main. All were at origin, and none was dirty.
- **Gate**: I ran `gate.py --at 6506e9c` twice from the project MAIN_WORK (`gate267-1.txt`, `gate267-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 6506e9c, 6042 tests, 0 failed".
  - Both state lines: "MAIN_WORK d3099800 · HANDOFF 9991aff · KOTOR-RPG-APP 6506e9c · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Watch Two and Aoo Eighty, plus new characters made in chargen.
  - The restore copy `notes/saves267` was taken from `saves266`. Its md5s match the last BEFORE lines (Looter 119cbbbd, Pazaak Ten 6cb1a6a7, Watch Two 8a9ede2a, Aoo Eighty 4d6fe9eb).
- **Scratch**: step 2's Force-at-0 character came from two saves I wrote in a scratch data dir (below). The real saves and packages have no edits.

## Summary

All five steps pass. Nothing to file; three things are noted below.

| # | Check | Result |
|---|---|---|
| 1 | Chargen Equipment's bonus row | **PASS**. Convict's Security Tunneler row draws the same icon and "2" as Play's Inventory. Doctor and Mechanic draw their items' icons too. |
| 2 | The empty Force strip | **PASS**. 12,54,46 on Equip, Inventory, Abilities, Character and Map, for no Force and for Force at 0. The Vitality bar keeps its black empty part. |
| 3 | Recommended-attacks popup | **PASS**. Both boxes have icons, the same glyphs as their grid cells. |
| 4 | Map arrow, 5 east and 1 south | **PASS**. −14.0° at 1920 and −8.8° at 1600×900, against a bearing of −11.3°. |
| 5 | Whole-screen look | **PASS** at 1920×1080 and 1600×900. |

## 1. Chargen Equipment's Profession Bonus

- **Convict** (Rodian Soldier, Talia Solvek): the Security Tunneler row draws the tunneler icon with a teal "2" (`c1-equip-bonus`, `z-c1-tunneler-icon`).
  - Play's Inventory draws the same icon and "2" (`c1-inventory-clear`). Side by side in `z-tunneler-chargen-vs-inventory`.
- **Doctor**: the bonus row draws the Advanced Medpac icon with "2" (`c2-equip-bonus`).
- **Mechanic**: the bonus row draws the Adrenaline Amplifier icon, with no count (`c3-equip-bonus`).
- In all three, the second bonus row ("Aptitude: Security", "Aptitude: Medicine", "Aptitude: Repair") has an empty box. It's an aptitude, not an item.

## 2. The empty Force strip

MAIN's x 1492–1506 is the portrait on the menu screens. There the strip runs x 1491–1509, rows 863–986, all 12,54,46. TEST 266 read 0,0,0 at the same pixels (`n-t-equip`, `n-t-inventory`).

| Character | Force | Screens read | Strip |
|---|---|---|---|
| Talia Solvek (Soldier, chargen) | none | Equip, Inventory | 12,54,46 |
| Veya Lhent (Soldier, chargen) | none | Abilities, Character | 12,54,46 |
| Aoo Eighty (Soldier, 6 of 11) | none | Inventory, Map | 12,54,46 |
| Force Zero (scratch, Watch Two's build) | 0 of 57 | Inventory | 12,54,46 |
| Force Hurt (scratch, the same) | 0 of 57 | Inventory | 12,54,46 |

- **Force at 0**: Watch Two loads at 57 of 57, and spending 57 by hand wasn't practical. I copied Watch Two's save into a scratch data dir (`~/kotor-tester/scratch-267`) and appended one `power.cast` event carrying `force: 0` before the last line, with a new id and name. It loaded with "force 0 of 57" (`f0-loaded`, `f0-inventory`). The files are in `scratch/`.
- **Vitality**: on Aoo Eighty (6 of 11) the menu portrait's Vitality bar is black from row 863 to 918, then filled 97,53,34 to 987 (`a8-inventory`). At 1600×900 it's the same, scaled (`o-02-inventory`).
- **The HUD's portrait** (board, bottom right) is unchanged from TEST 266: its Force well is 13,55,45 for no Force and for Force at 0. The empty part of its Vitality bar is also 13,55,45, not black (`z-a8-portrait`). TEST 266 shows the same.

## 3. The recommended-attacks popup (Convict)

- Both boxes have icons: Power Attack (a red sword) and Charged Shot (`c1-cg-attacks-rec`). TEST 264 drew both boxes empty.
- **The grid**: I clicked cells until the name box read "Power Attack" (`c1-grid-power-attack`). Its cell and Charged Shot's cell hold the same glyphs as the popup (`z-rec-vs-grid`: grid, popup, grid, popup).
- The grid draws them dimmer than the popup, even when selected.

## 4. The Map arrow (Aoo Eighty, real data dir)

- I loaded Aoo Eighty and took one step west, so the east droid sat 5 east and 1 south. Walking into the near droid (Right) started the fight, with Aoo Eighty first (initiative 20).
- On Aoo Eighty's turn I moved two north, back to that square. The near droid's opportunity attack missed (`a8-07-up2`).
- The click on the east droid fired "Blaster Rifle · rolled 6 … needed 10 — miss" (`a8-09-shot`).
- **The Map's arrow**: −14.0° at 1920 (`a8-11-map-clear`, `z-a8-map-arrow`) and −8.8° at 1600×900 (`o-03-map`).
  - The bearing of 5 east and 1 south is −11.3°.
  - TEST 266's 5 east and 1 north read +14.0°, so the two shots mirror each other.
  - The 1600 arrow is smaller, so its reading is coarser.

## 5. Whole-screen look

- **1920×1080**: chargen from the package menu to play (species, hub, Feats, Attacks with the popup, Equipment, name, bio, Play), the board, Equip, Inventory, Abilities, Character, the Map, and the fight. Nothing cut off, overlapping or missing.
- **1600×900** (`o-*`): the recommended-attacks popup, the chargen hub, Equipment (help and bonus rows), the fight board, Inventory and the Map. Nothing cut off, overlapping or missing.

## Odd, not filed

- **Empty attack-grid cells.** Covering Fire, Disarming Shot, Overwatch, Point Blank Shot and Shoot have empty boxes in chargen's attack grid (`c1-grid-325` shows Covering Fire selected). TEST 264's frame shows the same. They may be our own attacks with no K2 icon, like the known feat gaps.
- **The grid's icons are dimmer than the popup's** for the same attack (`z-rec-vs-grid`).
- **Aptitude rows have empty boxes** in the Profession Bonus list (step 1).

## What I got wrong

- My first package search ran with an empty "previous word" and could never match, then a second one timed out. A fresh launch found Endar Spire.
- My typed name didn't take, so the Convict kept the random name Talia Solvek.
- To reach a Mechanic, I changed the Doctor's background on the hub. That threw away the later steps, and I redid them.
- My tab tour stalled behind Equip's first-visit help, so all its frames (`t1-*`) are Equip, not five screens. I read Abilities, Character and the Map separately (`c4-*`, `a8-11`).
- My Force Hurt save also set `vitality_of` to the save's id, to show a hurt bar. It didn't take, so I used Aoo Eighty's real wound instead.
- My load helper didn't cycle far enough through Tester Bolt's characters. I picked both scratch saves by hand, with a frame at each Load click.
