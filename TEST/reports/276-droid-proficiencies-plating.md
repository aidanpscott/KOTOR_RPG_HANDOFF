# TEST 276: droid proficiencies and plating, on app main 87207e4

Refiled on MAIN's order (2026-11-21) from the last section of TEST/reports/275-test-274-fixes.md (first filed at HANDOFF 220b447). Nothing was rerun; the build, gate and media are the same. MAIN accepted steps 9, 10 and 11 (Bounty Hunter and Scout) and FINDING 3 went to Coder.

MAIN moved TEST 275 to app main `87207e4` and Shelf `c75c1d3`. Steps 1 to 8 were already filed above on `c5b65a3`, so as MAIN said, I ran steps 9 to 11 on `87207e4`. Media: `MAIN_WORK/media/screens/test-275/87207e4/` (MAIN_WORK `c037fe2d` to `98cbd880`, four commits, because one push of all 102 MB timed out with HTTP 408 twice).

Received since my last report: MAIN's move of TEST 275 to 87207e4 with steps 9 to 11, and the two KNOWN items removed (logged HANDOFF `665dd91`).

## Build

- **App**: main `87207e4`, a fresh clone from GitHub in `builds/test275b`, built debug through `tool/one_at_a_time.sh` (12 s, pubspec.lock unchanged). Lens `e449221` and Lodestar `a554b93` are the locked refs.
- **Heads**: every shared tree at origin and clean before the gate. The shared HANDOFF was behind by my own ledger commit, and the shared MAIN_WORK was behind by my own TEST 275 media commit `1105ade6` and nothing else. I fast-forwarded both (ff-only, my own commits only).
- **Gate**: `gate.py --at 87207e4` twice from the project MAIN_WORK (`gate275b-1.txt`, `gate275b-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 87207e4, 6108 tests, 0 failed".
  - Both state lines: "MAIN_WORK 1105ade6 · HANDOFF 665dd91 · KOTOR-RPG-APP 87207e4 · Lodestar a554b93 · Loom 9a1c3ef · Shelf c75c1d3 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: my data dir's packages fast-forwarded to `c75c1d3` (27 untracked fixture packages there, nothing tracked changed). check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: nothing used the real data dir. At the end the live saves equal `notes/saves275`, apart from the four known (same md5s as before).
- **Characters**: made in a new scratch dir `scratch-275h` (packages copied at `c75c1d3`): BX-275 (Battle droid Bounty Hunter), SX-275 (Battle droid Scout), Sura Lhent (Rodian Bounty Hunter), plus a Rodian Scout taken to its Feats page and cancelled. The app's own saves from those are in `base/`.
- **Scratch saves**, each in its own data dir, authored from `base/` with mksave273.py; the copies above a tier level also carry that tier's grants (addfeats275.py, source granted, at the class's own level), as a real character would:

  | Dir | Character | Authored at | Extra grants | md5 |
  |---|---|---|---|---|
  | 275i | BX-275 | Bounty Hunter 3 | none | e217ff74 |
  | 275j | BX-275 | Bounty Hunter 4 | none | abd04009 |
  | 275k | BX-275 | Bounty Hunter 9 | Droid Upgrade 2, Plating Medium at 5 | 690f3811 |
  | 275l | BX-275 | Bounty Hunter 10 | same | 8ac3bd26 |
  | 275m | SX-275 | Scout 5 | none | 03f4ee5b |
  | 275n | SX-275 | Scout 6 | none | d26252e1 |
  | 275o | SX-275 | Scout 11 | Droid Upgrade 2, Plating Medium at 7 | fae1b576 |
  | 275p | SX-275 | Scout 12 | same | 0da651d4 |
  | 275q | Sura Lhent | Bounty Hunter 1 | none | 3a9205b2 |
  | 275r | Sura Lhent | Bounty Hunter 3 | none | cc6cfce6 |

- **Loads**: 11, each with BEFORE and AFTER md5 in `loads.txt` and a frame at the Load click. Two earlier tries matched no name (OCR read "BxX-275") and loaded nothing. Every scratch file is unchanged at the end.

## Step 9: droid proficiencies — PASS

- **Chargen**, droid Bounty Hunter and droid Scout (Battle chassis): the granted popup lists only Droid Upgrade 1 and Plating Proficiency: Light (the Scout also gets Targeting 1 and Terrain Sense). Neither Feats grid has an Armour Proficiency row or a Weapon Proficiency: Melee Weapons row (`h-cg-scan.txt`, `s-cg-scan.txt`). Both hold Weapon Proficiency: Blaster and Blaster Rifle. The hub's Feats tab lists Droid Upgrade 1, Plating Proficiency: Light, Toughness. The droid Bounty Hunter's standard gear carries no armour.
- **Play**: Abilities, Feats. BX-275 holds Toughness, Weapon Proficiency: Blaster, Weapon Proficiency: Blaster Rifle, Droid Upgrade 1 and Plating Proficiency: Light. SX-275 holds the same plus Targeting 1 and Terrain Sense. No armour, no Melee Weapons.
- **Level-up**: BX-275 to 4 (`i-lu-scan.txt`) and SX-275 to 7 (`n-lu-scan.txt`): no Armour Proficiency row, no Melee Weapons row.
- **Organic control**: the Rodian Bounty Hunter holds the Armour Proficiency chain and Melee Weapons at chargen (`o-cg-scan.txt`), in play (the Light, Medium, Heavy chain row and Melee Weapons) and on level-up to 4 (`r-lu-scan.txt`). The Rodian Scout holds Armour Proficiency (Light, Medium held) and Melee Weapons at chargen (`os-cg-scan.txt`, filtered to those rows). I did not take the organic Scout into play or a level-up.

## Step 10: Plating Proficiency — PASS

- Organics never see it: no Plating row on the Rodian Bounty Hunter's or Rodian Scout's chargen grid, or on the Bounty Hunter's level-up grid.
- Droids hold Light from level 1: granted at chargen to BX-275 and SX-275, and held in play.
- With the droid feats: in Shelf `c75c1d3` all three (Light, Medium, Heavy) are section 4 in feats.toml. In the app, the chain shows as one row (Light, then Medium and Heavy in columns 2 and 3) on the droid grids. The Feats grid lists every feat alphabetically, so it shows no sections, and I can't judge the section from the screen.

## Step 11: early plating by class

- **Droid Bounty Hunter: PASS.** BH 3 to 4: granted Quarry only, and Plating Medium is red ("Prerequisites: Plating Proficiency: Light, Character Level 7", Add Feat dim). BH 4 to 5: Droid Upgrade 2 and Plating Proficiency: Medium granted. BH 9 to 10: Quarry, Run to Ground, No Escape; no Heavy. BH 10 to 11: Droid Upgrade 3 and Plating Proficiency: Heavy granted.
- **Droid Scout: PASS.** Scout 5 to 6: no plating. Scout 6 to 7: Droid Upgrade 2 and Plating Proficiency: Medium granted; on that level-up grid Heavy is red ("Plating Proficiency: Medium, Character Level 13"). Scout 11 to 12: no plating (I scrolled the granted list to its end). Scout 12 to 13: Droid Upgrade 3 and Plating Proficiency: Heavy granted.
- **Droid Soldier: CAN'T RUN (FINDING 3).** A droid can't be a Soldier. At chargen the Soldier row reads "A droid cannot take this class." with OK dim (`h-class3`). At level-up for BX-275, the same line and OK dim (`i-lu-soldier`). In Shelf `c75c1d3` droid_arrays.toml opens nine classes to droids: Scout, Smuggler, Bounty Hunter, Engineer, Machinist, Agent, Treasure Hunter, Medic, Duelist. Read from the code, not played: the app's tier table (lib/chargen/granted_feats.dart, `_droidTierRows`) gives early tiers to Soldier, Brawler and Sith Warrior at 4 and 9, and to Marksman, Bounty Hunter, Engineer, Machinist and Droid Master at 5 and 11. Of those, Soldier, Brawler, Sith Warrior and Marksman are closed to droids, so no droid can reach those rows. On the class page Marksman carries the same marker as Soldier; I did not click it. Either the order's droid Soldier or the table's closed rows need MAIN's ruling.
- Note on the authored saves: Quarry and Run to Ground appear again on BH level-ups because mksave273 skips class grants below the authored level. That comes from my authoring, not the app.

## Odd, not filed

- **Plating Medium's and Heavy's panes name the floor level for every class.** For a droid Bounty Hunter at 4, Medium's prerequisites read "Character Level 7", though this class brings it at 5. The effect line does say "Character level 7, or earlier by class."
- **Plating Proficiency: Light shows no held mark on the grid.** Its cell is the known empty icon, so held and takeable look alike; Add Feat is dim on it.
- **Empty Recommended attacks popup** again, now on a Battle droid Bounty Hunter (TEST 275 saw it on an Astromech).

## What I got wrong

- **My first grid scan didn't stop at the end.** The repeat check compared whole frames, and the selected cell changes each page, so it ran 14 pages; pages 4 to 13 are repeats and are left out of the media.
- **Two loads matched no name** before I fixed the regex (whole-line match, OCR "BxX-275"). Nothing was loaded; both are in `loads.txt`.
- **The organic Scout stalled on Skills** (a different point count). I finished the page by hand from the frame.
- **The first media push timed out twice** (HTTP 408); I split my own unpushed commit into four and pushed each.
