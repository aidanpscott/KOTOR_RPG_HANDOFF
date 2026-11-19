# TEST 271: The tier arrows and the footer bars

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs and my scripts are in `MAIN_WORK/media/screens/test-271/`. Names in brackets below are files there.

Received since my last report: MAIN's TEST 270 acceptance; MAIN's TEST 271 order.

## Build

- **App**: main `bdbf45d`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in.
- **Heads**: before the gate I checked every shared tree against origin/main. The shared HANDOFF tree was clean and 1 behind, by my own ledger commit. I fast-forwarded it (ff-only) to `30c4ae0`. All the others were at origin and clean.
- **Gate**: I ran `gate.py --at bdbf45d` twice from the project MAIN_WORK (`gate271-1.txt`, `gate271-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at bdbf45d, 6059 tests, 0 failed".
  - Both state lines: "MAIN_WORK f2fa7484 · HANDOFF 30c4ae0 · KOTOR-RPG-APP bdbf45d · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Watch Two (`lu193-guard6b`) and Aoo Eighty on the real data dir. Force Half (28 of 57) is TEST 269's scratch copy in `~/kotor-tester/scratch-269`, unchanged (md5 321b504e).
  - The restore copy `notes/saves271` was taken from `saves270`. Its md5s match the last BEFORE lines (Watch Two 8a9ede2a, Aoo Eighty 4d6fe9eb, Pazaak Ten 6cb1a6a7, four-200 ca0aac5f).
- **Chargens**: a Rodian Soldier and a Rodian Jedi Consular at 1920, and a Bith Soldier at 1366×768. None was played.
- **K2 captures**: `k2-chargen/13`, `/14` (native 3840×2160, halved for the numbers below) and `k2-levelup/arrows-l6/33`, `/40` (resized to 1920, so positions only).

## Summary

One finding and one question for MAIN. Everything else passes, apart from one half of step 4 that can't be shown in the real app.

| # | Check | Result |
|---|---|---|
| 1 | Chargen Feats | **PASS** for the rule: no arrow into a red cell, and taking a feat draws one to a takeable next tier. **FINDING 1**: no class's granted proficiencies show as held at chargen, so the held→held armour arrows can never appear. |
| 2 | Chargen Powers | **PASS**. Every second tier is red at level 1. Taking Force Aura and Burst of Speed draws no arrow. |
| 3 | Watch Two's level-up | **PASS** for the first gap: the same pixels as K2's. Powers: Aura → Shield. **QUESTION**: the second-gap arrow is centred, but K2's sits 8 px right of centre. |
| 4 | In-play Abilities | **PASS** for arrows from held feats and known powers. The "none from unknown or unheld" half can't be shown: play lists neither. |
| 5 | Footer bars | **PASS**. Full, empty and half are as ordered; Vitality edges are 204,51,0. |
| 6 | Whole-screen look | **PASS** at 1920×1080 and 1366×768. |

I checked each grid against the rule row by row with `scripts/rule271.py`. It reads each cell as held (bright), takeable (dim teal) or red, finds any arrow in each gap, and flags any row where an arrow is drawn but shouldn't be, or is missing. It found no breaks on any frame. Its one flag was on a frame where the cell I had just taken was selected: the white selection border hides the cell's teal edge. That cell measured peak 220, so it was taken.

## FINDING 1: Chargen shows no granted proficiency as held

- `classes.toml` gives the Soldier `starting_proficiencies` Armour Proficiency Light, Medium and Heavy (Scout, Marksman and others get Light and Medium).
- On the Soldier's chargen Feats grid, Light is takeable (dim, peak 86) and Medium and Heavy are red. No cell on the whole grid is held except the granted Squad Tactics (`s-cg-feats`, `s-feats-s1`…`s6`).
- I could spend the Soldier's only feat on Armour Proficiency: Light. The hub's Feats tab then listed Squad Tactics and Armour Proficiency: Light (`s-feats-light-taken`, `s-hub-feats-tab`). The Jedi Consular and the 1366 Bith Soldier show the same grid (`j-feats`, `o-cg-feats-light`).
- In play, the Soldier Aoo Eighty's Abilities Feats show Light → Medium → Heavy all held, with two arrows (`a-ab-feats`).
- Code: `lib/chargen/hub.dart` passes `held:` only the level-1 grant (`grantedFeatsFor(... level: 1)`), not `starting_proficiencies`.
- Effect on this test: K2's chargen/13 and /14 draw Light → Medium (both held) → Heavy. In our chargen no class can show that.

## 1. Chargen Feats and Attacks (Rodian Soldier, Rodian Jedi Consular)

- **Before any pick**: no arrows anywhere on either class's Feats or Attacks grid. Squad Tactics (held) has red next tiers, so it gets no arrow (`s-feats-s3`).
- **Taking a feat**: when I took Armour Proficiency: Light, an arrow appeared to Medium, and Medium turned takeable. Heavy stayed red, with no arrow into it (`s-feats-light-taken`). Remove Feat took the arrow away, and re-adding brought it back (`s-feats-light-removed`, `s-feats-light-retaken`).
- **Attacks**: taking Power Attack left Improved Power Attack red (198,52,2), with no arrow (`s-attacks-pa-taken`). The Jedi's four attacks did the same (`j-attacks-picked`).
- **Arrow position**: x 379–393 along its row (y 267–284 on the 276 row), between the cells' edges at 258 and 509. K2's chargen arrow is at 379–393.5 along its row. All positions in this report are read along the row's centre line with `scripts/edges271.py` (runs of grid-border and arrow colour); K2's native 4K capture is halved.

## 2. Chargen Powers (Jedi Consular)

- Before any pick, there are no arrows, and every second-tier cell is red at level 1 (`j-powers-before`).
- After I took Force Aura (peak 242) and Burst of Speed (238), Force Shield and Knight Speed stayed red, with no arrows (`j-powers-after`).

## 3. Watch Two's level-up (Jedi Guardian, to level 8)

**Feats** (`w-lu-feats-popup`, `w-lu-feats-s1`…`s8`). All nine frames have no rule breaks.

| Row | Cells | Arrows |
|---|---|---|
| Armour Proficiency | Light held, Medium takeable, Heavy red | Light → Medium |
| Force Jump | Force Jump held, Advanced held, Mastery red | Force Jump → Advanced (held to held) |
| Unarmed Specialist | I held, II held, III red | I → II (held to held) |

- I took Armour Proficiency: Medium. An arrow appeared Medium → Heavy, and Heavy turned takeable (`w-lu-feats-medium`).
- **First gap**: the arrow is at x 379–393 on its row, against K2's 379–393 (`k2-levelup/arrows-l6/33`) and 379–393.5 (`k2-chargen/14`), with the same cell edges (258, 509). It's centred on the row: 275.5 against a cell centre of 276.

**QUESTION, the second gap.** Medium → Heavy draws at x 671–685. K2's own second-gap arrow (chargen/14, native, halved) is at 679–693.5. The cell edges are identical in both (550 and 802).
- Ours is centred in the gap (gap middle 676, arrow middle 678).
- K2's sits 8 px right of centre. Its first-gap arrow is close to centred, at 386 against 383.5.
- The order says "centred in the gap", and K2 draws it 8 px right of centre. Which should it match?

**Powers** (`w-lu-powers`, `w-lu-powers-s1`…`s8`). No rule breaks.
- Force Aura → Force Shield, both known (Add Power is dim on Shield, `w-lu-powers-shield-lit`), with an arrow. Force Armor (level 12) is red, with no arrow.
- Burst of Speed isn't known on Watch Two, so there's no arrow, and Knight Speed is red anyway.
- Force Stun isn't known. When I took it, Force Stasis (level 9) stayed red, with no arrow (`w-lu-powers-stun-taken`).
- Position: x 375–391 at the row centre, against K2's 377–391 on the resized capture. The cell edges match (256, 507, 548, 800).
- **Stun Droid → Disable Droid**: Watch Two doesn't know Stun Droid, so Disable Droid is red ("Character Level 6, Stun Droid"). When I took Stun Droid, Disable Droid stayed red, with no arrow (`w-lu-powers-stundroid-taken`). See "Odd" below.
- I cancelled the level-up, and nothing was kept.

## 4. In-play Abilities

- **Watch Two, Powers**: Force Aura → Force Shield, with an arrow (`w-ab-powers`).
- **Watch Two, Feats**: Force Jump → Advanced and Unarmed Specialist I → II, with arrows. Every other feat stands alone (`w-ab-feats`).
- **Aoo Eighty, Feats**: Light → Medium → Heavy, with two arrows (`a-ab-feats`).
- The small arrows sit at x 236–242, between cell edges at 231 and 246.
- **Can't be shown**: play lists only known powers and held feats (`lib/play/play_screen.dart` lines 3140 and 3143). An unknown power or an unheld feat is never on screen, so there's nothing for a wrong arrow to come from.

## 5. The footer bars (menu-screen portrait)

Readings run down the strip's columns and across rows 900 and 960 (`scripts/strip270.py`, `scripts/hrun271.py`).

| Character | Force strip | Vitality bar |
|---|---|---|
| Watch Two (`w-ab-powers`), Force 57 of 57, Vitality 59 of 59 | inside 4,119,124; edges 0,217,236 all round | inside 98,42,16; edges 204,51,0 all round |
| Aoo Eighty (`a-ab-feats`), no Force, Vitality 6 of 11 | inside 13,55,45; edges 29,119,99 | filled 919–986 (68 of 124 rows; 6/11 is 67.6); edges 204,51,0 beside the fill, 29,119,99 and 13,55,45 above it |
| Force Half (`h-abilities`, `h-inventory`), Force 28 of 57 | empty 865–925, filled 926–986 (61 of 123, 0.50; 28/57 is 0.49); edges 0,217,236 beside the fill, 29,119,99 beside the empty part | — |

- Force Half reads the same on Abilities and Inventory.
- At 1366×768 the strip is filled 42 of 87 rows, 0.48 (`o-inventory`).

## 6. Whole-screen look

- **1920×1080**: chargen (species, class, hub, Feats with the granted box, Forms, Attacks with the recommended popup, Powers with its help), level-up (class, hub, Attributes, Skills, Feats, Powers), play, Character, Abilities and Inventory. Nothing cut off, overlapping or missing.
- **1366×768** (`o-*`): chargen (species, class, hub, Feats with Light taken), level-up (class, hub, Feats), play, Inventory, Abilities (Skills, Powers, Feats), Character, Equip and the Map. Nothing cut off, overlapping or missing.
  - The level-up and chargen Feats arrows land in the same scaled place (x 382.3 in 1920 terms).

## Odd, not filed

- **Powers don't open the next tier on a pick; Feats do.** Taking Medium turned Heavy takeable, with an arrow. Taking Stun Droid left Disable Droid red: its prerequisite reads only known powers. I have no K2 capture of either case on Powers.
- **Vigil has no icon** in Watch Two's Abilities Feats (`w-ab-feats-empty`).
- **Aoo Eighty's live save** reads 8b8c8171 after the session. Its AFTER line at load read 4d6fe9eb, so the app wrote it later. The restore copy is untouched.

## What I got wrong

- My first Force Half load picked Con Twenty. OCR read "FORCE HALF", but the card moved on after the read. It's on the scratch dir, and I took no readings from it. The load log says so, and the redo has frames of the card and the click (`loadclick-forcehalf-list`, `loadclick-forcehalf`).
- On the level-up Powers grid the page had shifted, and I took Force Affliction, not Force Stun. I removed it before taking Stun. Its next tier, Force Contagion (level 9), stayed red, with no arrow.
- My Jedi chargen script stalled in Skills twice (a different point count). I accepted the unspent points and ran the rest by hand.
