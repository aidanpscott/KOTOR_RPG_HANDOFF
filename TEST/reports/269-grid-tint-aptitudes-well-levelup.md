# TEST 269: Grid tint, aptitude icons, the in-play Force well and the Level Up buttons

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the authored scratch save are in `MAIN_WORK/media/screens/test-269/`. Names in brackets below are files there.

## Build

- **App**: main `3a554c9`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Heads**: before the gate I checked every shared tree against origin/main. All were at origin and clean.
- **Gate**: I ran `gate.py --at 3a554c9` twice from the project MAIN_WORK (`gate269-1.txt`, `gate269-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 3a554c9, 6051 tests, 0 failed".
  - Both state lines: "MAIN_WORK d42af2ab · HANDOFF 5a3a4b1 · KOTOR-RPG-APP 3a554c9 · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Watch Two (Force 57 of 57) and Aoo Eighty (no Force) on the real data dir. The restore copy `notes/saves269` was taken from `saves268`. Its md5s match the last BEFORE lines (Looter 119cbbbd, Pazaak Ten 6cb1a6a7, Watch Two 8a9ede2a, Aoo Eighty 4d6fe9eb).
- **Scratch**: Force at half (28 of 57) came from a copy of Watch Two's save in a scratch data dir (`~/kotor-tester/scratch-269`), with one `power.cast` event carrying the Force value (`scratch/`). The real saves have no edits.
- **Chargens**: nine Rodian characters on the real data dir. Seven were Soldiers (Mechanic, Convict, Courtesan twice, Exile, Politician, Demolitionist) and two were Jedi Consulars.

## Summary

All five steps pass. One reading is off MAIN's number, and three things are noted below.

| # | Check | Result |
|---|---|---|
| 1 | Feats and Powers grids | **PASS**. Held, granted and known cells peak at 201–242; the rest peak at 81–95. The same icon goes from 86 to 221 when taken (0.39). |
| 2 | Aptitude rows | **PASS**. Repair, Security, Persuade and Demolitions show their icons; Survival keeps the empty slot. **Noted**: Courtesan shows no Profession Bonus rows at all. |
| 3 | In-play Force well | **PASS** for the edges (0,217,236) and the fill (full, then half). **Off**: the filled inside reads 7,130,132, not ~36,133,137. The menu bar stays 10,119,124. |
| 4 | Level Up buttons | **PASS**. 36,36,36 at both buttons' tops and feet; Auto Level Up's words peak at 74,68,56. |
| 5 | Whole-screen look | **PASS** at 1920×1080 and 1280×1080. |

## 1. Feats and Powers grids

I took each cell's brightest pixel (luminance) inside the icon (`scripts/peak269.py`, `cells269.py`, `pcells269.py`).

- **Soldier's Feats** (Mechanic):
  - Squad Tactics, granted: peak 201, p99 170 (`m-feats-cell423`). Its granted box draws the same icon at peak 188, p99 152 (`v-cg-granted`).
  - Unheld cells on the same frames peak at 76–94 (`m-cg-feats`, `m-feats-s1`…`s5`).
- **The same icon before and after**: Close Combat peaked at 86 before I took it (`m-cg-feats`) and 221 after (`m-feats-top-after`). That's 0.39, about a third.
- **Jedi Consular's Powers**: every cell peaked at 85–95 before I chose any (`j-powers-before`). After I added Force Aura and Burst of Speed, those two peak at 242 and 238. Every other cell is unchanged (`j-powers-after`).

## 2. Aptitude rows (Profession Bonus)

| Profession | Item row | Aptitude row |
|---|---|---|
| Mechanic (`m-equip-bonus`) | Adrenaline Amplifier, icon | Repair: wrench icon |
| Convict (`v-equip-bonus`) | Security Tunneler, icon and "2" | Security: lock icon |
| Politician (`p-equip-bonus`) | "Energy Shield — the standard forearm shield, not a droid Energy Shield Level 1", empty slot | Persuade: head icon |
| Demolitionist (`d-equip-bonus`) | Frag Grenade, icon and "2" | Demolitions: detonator icon |
| Exile (`x-equip-bonus`) | "Neural Band — a save bonus", empty slot | Survival: empty slot, as ordered |
| Courtesan (`c-equip-bonus`) | — | — (no Profession Bonus section) |

- **Withheld row**: on the Mechanic I chose the aptitude, then the item (`m-equip-apt-chosen`, `m-equip-item-chosen`). The row not chosen keeps its icon both times; only the highlight moves.
- **Courtesan**: picked twice (`c-bg-picked` reads Courtesan: "credits / Aptitude: Persuade / more starting credits"). Both times Equipment had no Profession Bonus section: the scrollbar thumb is full length and OK is already lit. `professions.toml` gives Courtesan `has_grant_row = true`.

## 3. The in-play Force well

Columns x 1888, 1894 and 1900 of the well beside the board portrait. The inside is rows 945–1066.

| Character | Force | Filled inside | Lit edge | Empty inside |
|---|---|---|---|---|
| Watch Two (`w-play`) | 57 of 57 | 945–1066, 7,130,132 | 0,217,236 all round | — |
| Force Half (`h-play`) | 28 of 57 | 1007–1066 (60 of 122, 0.49), 7,130,132 | 0,217,236 beside the fill | 945–1006, 13,55,45, frame 29,119,99 |
| Aoo Eighty (`f-fight`) | none | — | — | 13,55,45 |

- Edges match ~0,217,236, and it fills from the bottom: full, then half.
- **The filled inside is 7,130,132, not ~36,133,137.** Green and blue are within 5; red is 29 lower. The well sits over the HUD's black, not a floor, which may be why.
- **The menu bar stays 10,119,124**: full on Watch Two (`w-*`); at half, filled 927–986 plus a blend row at 926, which is 0.49 (`h-inventory`, `o-*`).

## 4. The Character sheet's Level Up buttons (Watch Two)

- Both buttons are now solid over the portrait (`w-character`). Every sample just inside each button's top and foot (rows 472/474, 555/557, 589/591, 652/654; five x positions each) is 36,36,36.
- Auto Level Up's dim words peak at exactly 74,68,56. Level Up's words peak at 217,217,196.
- At 1280×1080 the buttons read 36,36,36 too (`o-character`).

## 5. Whole-screen look

- **1920×1080**: chargen (species, hub, Feats with the granted box, Forms, Attacks, Powers, Equipment), play, the five menu screens, the Character sheet, and a fight (`f-fight`). Nothing cut off, overlapping or missing.
- **1280×1080** (`o-*`): chargen Feats (with the granted box), Powers and Equipment (help and bonus rows); play; the five menu screens; and the fight. Nothing cut off, overlapping or missing.

## Odd, not filed

- **Courtesan has no Profession Bonus rows** (step 2), though its grant row is declared.
- **Two item rows read like notes**: Politician's "Energy Shield — the standard forearm shield, not a droid Energy Shield Level 1" and Exile's "Neural Band — a save bonus". Both have empty icon slots.
- **The Jedi's Standard Gear has a dimmed "Tier-1 Saber Upgrade" row** with no icon (`o-cg-equipment-help`, `o-cg-equipment-bonus`). It may be the withheld row MAIN meant.

## What I got wrong

- My first chargen ran the wrong half of my split script, and its clicks ended in Options > Feedback. Nothing was changed there, but the app rewrote `settings.json` with its defaults (brightness 0.57 is the default). I went back to the one-piece script.
- My Force Half load failed twice because OCR read "ForRcE HALF". I logged the names while cycling and loaded it by hand, with a frame.
- My first odd-size Jedi run added three attacks, not four, so its first "Powers" and "Equipment" frames were really Attacks. I deleted them, added the fourth and reframed.
