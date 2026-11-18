# TEST 263: The store rows, TEST 261 and 262 fixes, and the gate's state line

Real game, my Xvfb `:2`, my data dir, no K2. Text only. Frames, crops, the readings (`px-263.txt`, `px-pz04.txt`), the load log (with a frame at every Load click), both gate outputs, the dev logs and my scripts are in `KOTOR_RPG_MAIN_WORK/media/screens/test-263/` (696025ba). Names in brackets below are files there.

## Build

- **App**: main `34f727f`, a fresh clone.
- **Gate**: I ran `gate.py --at 34f727f` twice, one straight after the other (`gate263-1.txt`, `gate263-2.txt`). Both runs read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 34f727f, 6015 tests, 0 failed". Both state lines were the same and clean (step 1).
- **Locks**: Lens `e449221` and Lodestar `e81b358`, compiled in.
- **Shelf**: `8f2d845`, origin's head. check_shelf: "34 rules files and 151 standard blueprints, all identical", run on my data dir.
- **The before**: TEST 262's frames of `9bd1ffb`, with the same saves and clicks. I didn't rerun 9bd1ffb.
- **K2**: `k2-capture-run/07` and `03a` (resized), positions only. `k2-pazaak/04` (native) for the wager page. `k2-levelup/01` for the sheet's buttons.
- **Saves**: Looter, C79 Battle, Pazaak Ten and Watch Two (`lu193-guard6b`), plus two new characters made in chargen. Restore copy `notes/saves263`.
- **Xvfb**: checked before the first launch; it was up.

## Summary

All five steps pass, with one finding:

- **Finding 1**: the Equipment step still leaves the Security Tunneler without its icon. Play draws it.

| # | Check | Result |
|---|---|---|
| 1 | The gate's state line | **PASS**. It's printed at the top of both runs with every repo's head. Each head matched its origin and none was dirty. |
| 2 | The store (03a) | **PASS**. The rows sit on 03a's 38 px pitch, with the tile and name box in 03a's places. |
| 3 | TEST 261's fixes | **PASS**: the "+" is lit at 40, Quit and Wager are centred, the Level Up buttons are filled, Inventory and Map have the curved pair, the hub's arc clears "Origin", and the Map's line is gone. |
| 4 | TEST 262's fixes | **PASS**: no overlaps at 1280×1080 or 1024×1080, all eight icons open at both, and nothing moved at 1920. The corners are black, the Force bars are drawn and the health bar has its outline. **Finding 1**: one Equipment icon is still missing. |
| 5 | Whole-screen look | **PASS** at 1920×1080 and 1280×1080: play, a fight, Pazaak, the store, Load, level-up, and chargen to play. |

## FINDING 1: the Equipment step leaves the Security Tunneler without its icon

- On the Equipment step, the icons now show for Clothing, Blaster Rifle, Short Sword, Adrenal Strength, Frag Grenade (with "2" on the tile) and Medpac ("2") (`n-cg-31-equipment-clean`).
- Under Profession Bonus, the Security Tunneler's tile shows only its "2", with no picture (`n-cg-31-equip-down`). It's the same at 1280×1080 (`n-8h-equip-down`).
- After chargen, play's Inventory draws the Security Tunneler's icon with its "2" (`n-cg-37-inv`, `cmp-tiles-inv-vs-cg`). So play finds an icon that the Equipment step doesn't.
- On 9bd1ffb every Equipment icon was blank.
- **Dockworker's Treads** is blank both on the Equipment step and in play's Inventory, so I'm only noting it below.

## 1. The gate's state line

- Both runs printed "state: MAIN_WORK 4e677090 · HANDOFF 61ea476 · KOTOR-RPG-APP 34f727f · Lodestar e81b358 · Loom eb3aa63 · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221" under the header.
- Every head equals its origin (`git ls-remote`), and no tree was dirty.
- **The flags.** I ran the gate's two tests on a scratch clone of Atlas:
  - an untracked file gave "dirty";
  - a local commit gave "not on origin".
- **When I pushed the media**, the bare gate's line read "KOTOR-RPG-APP f9264b5 not on origin": a commit in the shared app tree that isn't on origin. It read "SENDABLE" and "NOT FOR TESTER: no passing CORE at f9264b5". It doesn't touch 34f727f. Kept as `gate263-media-push.txt` in my logs.

## 2. The store (Pazaak Ten's Card Dealer against 03a)

- **Rows** (`cmp-store-rows`, `px-263.txt`). The icon tiles' edges, top to bottom:

  | | Row 1 | Row 2 | Row 3 | Row 4 |
  |---|---|---|---|---|
  | K2 03a | 282/288 | 320/326 | 358/364 | 396/402 |
  | 34f727f | 282/288 | 320/326 | 358/364 | 396/402 |

  Both keep a 38 px pitch to row 7.
- **Tile and name box**: across y 300 the name box spans 247–925 in both, and the tile sits left of it in 03a's place.
- **Scroll bar**: 4 px right (known).

## 3. TEST 261's fixes

- **Wager "+" at 40** (`px-pz04.txt`):

  | | "+" outline (median / peak) | "+" sign |
  |---|---|---|
  | K2 04 | 131,107,5 / 217,176,0 | 217,176,0 |
  | 34f727f | 133,108,3 / 217,176,0 | 216,175,0 |
  | 9bd1ffb | 75,61,10 / 90,73,10 | 88,72,10 |

- **Wager words**: Quit is at 603–637 (K2 604–638) and Wager at 886–940 (K2 886–941). On 9bd1ffb they were 7 and 8 px right. Clear Cards hasn't moved (known).
- **Setup frames** 06, 07, 08 and 08-unhover are pixel-identical to 9bd1ffb's.
- **Buttons' fill**: the sheet's Auto Level Up and Level Up are now filled dark, with the portrait showing dimly through them (medians 59,49,42 and 61,49,41). On 9bd1ffb the portrait showed straight through (178,146,126). K2's 01 is see-through the same way over its model (34,34,34 and 36,36,36) (`cmp-lu-01-sheet`, `k2-sheet-buttons`).
- **Inventory and Map**: both now draw the curved pair at 9,36,29, like every other screen (9bd1ffb: one square plate at 11,42,35, no right piece) (`cmp-t-inventory`, `cmp-t-map`).
- **Hub's arc**: the arc clears the "Origin" header, at 1920 and at 1280 (`cmp-lu-03-hub`, `n-63-1280-hub`).
- **Map's line of areas**: "Map — (Command Deck)" is gone (`n-t-map`).
- **TEST 261's Finding 4**, the strip right of the portrait (K2 12,54,46), is still 0,0,0 on every screen. It isn't on this order's list, so I'm noting it, not refiling it.

## 4. TEST 262's fixes

**The HUD at 1280×1080 and 1024×1080** (C79 Battle, mid-fight, so every part is up; `n-30-*`):

| Part | 1280×1080 | 1024×1080 |
|---|---|---|
| Message box | 350–851 | 280–683 |
| Icon bar | 857–1272 | 686–1017 |
| Gap between them | 6 px | 2 px |
| Message box bottom / initiative cards top | 118 / 132 | 99 / 107 |
| Board | 324–1203 | 259–962 |
| Action bar | 6–408 | 5–326 |
| Turn bar | 507–772 | 405–617 |
| Big portrait | 1111–1266 | 889–1012 |

- **No part overlaps another** at either size.
- **The eight icons**: at both sizes I clicked each one. Equip, Inventory, Character, Abilities, Party, Journal, Map and Options each opened, and Escape brought the board back (`sheet-1024-icons`, `sheet-1280-icons`).
- **At 1920**: Looter's board and C79 Battle are pixel-identical to 9bd1ffb's except the portraits' bars, so nothing moved.

**The other fixes:**

- **Chargen corners**: outside the rounded frame, the custom-character hub's portrait box and the Species picture box are now 0,0,0 (9bd1ffb 29,119,99) (`z-hub-portrait`, `z-species-box`). The biography page's box is black too.
- **Force bar**: our characters have no Force, so each portrait draws an empty Force bar on its right: fill 13,55,45 inside a 29,119,99 edge. That's the case of Atton's bar in 07 (`cmp-party-k2-old-new`). Both the big portrait and Kael's small one draw it. No save has Atton, so I compared against 07's Atton.
- **Health bar**: after the droids hit C79 Battle (16 of 23), the empty part above the red has the teal edge round it, with 13,55,45 inside (`z-end6`, `n-21-end6`). On 9bd1ffb it had no outline. The full fill is now 101,53,24 (9bd1ffb 94,23,0; K2's resized 07 111,72,54).
- **Equipment icons**: there, apart from Finding 1.

## 5. Whole-screen look

**At 1920×1080:**

- **In-game screens** (Looter, TEST 262's tour clicks): every frame is pixel-identical to 9bd1ffb's. The exceptions are Inventory's and Map's plates, the Map line, and the Load row's date (`n-t-*`).
- **A fight**: C79 Battle through six turns.
- **Pazaak and the store**: as in steps 2 and 3.
- **Level-up**: Watch Two's sheet, class list and hub. The class list is identical to 9bd1ffb's.
- **Chargen** (Rodian Soldier, Male, Taris, Convict): run to play on the Command Deck as "Vash Halcyon". Feats and Attacks are identical to 9bd1ffb's.

**At 1280×1080:**

- the board, Inventory, Options and Load (`n-41`–`n-44`);
- Pazaak's wager page and the ten-card setup (`n-51`–`n-53`). The used cards dim as at 1920: the +1's band is 57,89,168 (1920: 58,89,168);
- the store (`n-55`);
- Watch Two's sheet, class list and hub (`n-61`–`n-63`);
- the fight and the eight icons (step 4);
- chargen run to play as "Mira Dray": Species, Gender, Portrait, Origin, Background, Attributes, Skills, Feats, Attacks, Equipment, Name and the biography page (`n-71`–`n-8m`).

Nothing was cut off, overlapping or missing.

## Odd, not filed

- **Dockworker's Treads** has no icon, either on the Equipment step or in play's Inventory. The 100 Credits and "Aptitude: Security" rows are blank too, but those aren't items.
- **Recommended-attacks popup**: its icon boxes are still blank (TEST 262's odd one, now with the Coder) (`n-8e-attacks-rec`).
- **At 1024×1080** the message box and icon bar are only 2 px apart.
- **Species frame width**: its edges are 17 px wide at 1920 and 11 px at 1280, with the top and bottom 13 px at both. The frame art stretches to its box.

## What I got wrong

- My first restore copy took the live saves, which TEST 262's play had autosaved (Looter 3b8f5e3e). One Looter attempt ran on it and failed before loading. I refilled `saves263` and the live saves from `saves262`'s clean copies; `loads.txt` says so.
- My Load helper's OCR failed on "Looter" again. I loaded it by hand twice, each with a frame.
- I first ran check_shelf against the default data dir, then reran it on mine.
- On the first chargen I skipped the Equipment scroll and pick, so OK stayed grey. I deleted the three frames taken after it and redid the step.
- At 1024 my pointer, left over the portrait, raised a hover card over Kael's small portrait in `n-30-c79-1024x1080`.
- My readings file first had a guessed range for the small portrait; I replaced it with the measured box before committing.
