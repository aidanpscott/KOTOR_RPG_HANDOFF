# TEST 273: Prerequisites read in full

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the authored scratch saves are in `MAIN_WORK/media/screens/test-273/`. Names in brackets below are files there.

Received since my last report: MAIN's TEST 272 acceptance; MAIN's TEST 273 order.

## Build

- **App**: main `44cf61f`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in. Every step ran on this build.
- **Heads**: before the gate I checked every shared tree against origin/main. The shared HANDOFF tree was clean and 1 behind, by my own ledger commit. I fast-forwarded it (ff-only) to `0ab697f`. All the others were at origin and clean.
- **Gate**: I ran `gate.py --at 44cf61f` twice from the project MAIN_WORK (`gate273-1.txt`, `gate273-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 44cf61f, 6074 tests, 0 failed".
  - Both state lines: "MAIN_WORK ad80a4b6 · HANDOFF 0ab697f · KOTOR-RPG-APP 44cf61f · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**:
  - The restore copy `notes/saves273` was taken from `saves272`. Its md5s match the last BEFORE lines (Off Six 2797c6b0, Watch Two 8a9ede2a, Con Five 426740f7, Aoo Eighty 4d6fe9eb).
  - Two new characters from chargen on the real data dir: Sith Seven, a Rodian Sith Assassin (3d8b15f1), and BT-6, a Battle droid Engineer (b8a81252). Both were copied into `saves273`.
  - Every load has BEFORE and AFTER md5s in `loads.txt`. At the end of the session Off Six, BT-6 and Sith Seven all matched their restore copies.
- **Scratch saves**, each in its own data dir, authored from the two new characters by `scripts/mksave273.py` (class levels, matching `levelled` events, and an XP award):
  - `scratch-273a`: Sith Seven at Sith Assassin 6 with 21000 XP (`scratch/t273-sith-seven-level6.sav`, 22c62c17). Unchanged after its session.
  - `scratch-273b`: Sith Seven at Sith Assassin 5 with 15000 XP (`scratch/t273-sith-seven-level5.sav`, 9bc9bdb2). Unchanged after its session.
  - `scratch-273c`: BT-6 at Engineer 6 with 21000 XP (`scratch/t273-bt-6-level6.sav`, a4ba3144). I accepted its level-up to 7, which rewrote that scratch file.
  - These logs record no feats for the levels I added. So their level-up popups list every grant from level 2 on, as MAIN noted for Off Six.

## Summary

All four steps pass. One finding came up in the droid work.

| # | Check | Result |
|---|---|---|
| 1 | Class-level gate | **PASS**. Chargen Assassin: Force Camouflage takes; Improved and Master stay red. Class level 7: Improved opens, Master stays red. Class level 6: Improved stays red. |
| 2 | Droids | **PASS** at chargen for all four chassis (Astromech, Assassin, Battle, Remote): Droid Upgrade 1 announced, held and in the summary; Upgrade 2 and 3 not offered. Battle droid to 7: Upgrade 2 granted. **FINDING 1**: the droid's chassis ability adjustments show in play but not in chargen. |
| 3 | Heavy's prerequisites | **PASS**. "Armor Proficiency: Medium" for the Soldier and the Scout at chargen, and for Off Six's level-up. |
| 4 | Whole-screen look | **PASS** at 1920×1080 and 1280×720. |

## FINDING 1: A droid's chassis adjustments appear in play, not in chargen

- The Battle chassis reads "+2 Strength, +2 Constitution, −2 Intelligence, −2 Charisma" (`species.toml`).
- **Chargen**: BT-6's droid Attributes screen and hub show Strength 14, Dexterity 12, Constitution 14, Intelligence 10, Wisdom 12, Charisma 10, Vitality 10/10 (`db-attr2`, `db-after-attr`, `db-name`).
- **The save** records those same six scores in its `character.ability-set` events: 14, 12, 14, 10, 12, 10.
- **In play**, I loaded the same save (md5 unchanged, b8a81252). The Character sheet shows Strength 16, Dexterity 12, Constitution 16, Intelligence 8, Wisdom 12, Charisma 8, Vitality 11/11, Fortitude +3, Experience 0 (`bt1-character`).
- So play adds the chassis adjustment to scores that chargen showed as final. Either chargen leaves the adjustment out, or play applies it twice. I can't tell which from the screens.
- **For comparison**: the Rodian Sith Assassin is recorded as Dexterity 13 and shown as 15 in both chargen and play, so a species adjustment there shows the same in both.
- The scratch copy of BT-6 at level 6 shows the same 16/8 scores (`bt-character`).

## 1. The class-level gate

**Chargen Sith Assassin** (`sa-class-picked`, `sa-hub`):
- I took Force Camouflage: Remaining Powers went 2 → 1, and Remove Power lit (`sa-camo-taken`).
- Improved Force Camouflage stayed red with no arrow. Its text reads "Level 7 Jedi Watchman or Sith Assassin, Force Camouflage". Add Power was dim (peak 66), and clicking it did nothing; Remaining stayed 1 (`sa-imp-after`, `sa-imp-addtry`).
- Master Force Camouflage stayed red ("Level 13 Jedi Watchman or Sith Assassin, Improved Force Camouflage") (`sa-master-after`).
- The checker read the row as "held, red, red", with no breaks.
- I took Breath Control with the second pick and played the character, so the game wrote Sith Seven's save for the next two checks.

**Class level 7** (`scratch-273a`; `s7-character` reads "Sith Assassin 6", Experience 21000; the level-up class was Sith Assassin):
- Force Camouflage held, with an arrow to Improved. Improved is takeable and Add Power lit (`s7-camo`, `s7-imp`).
- I took Improved: Remaining Powers 1 → 0, and Remove Power lit (`s7-imp-taken`).
- Master stayed red, with no arrow from Improved, and Add Power was dim (`s7-master`, `s7-master-addtry`).

**Class level 6** (`scratch-273b`; Sith Assassin 5 going to 6, `s6-lu-hub` reads "Level 6"):
- Improved stayed red with no arrow from Force Camouflage. Add Power was dim, and clicking it did nothing; Remaining stayed 1 (`s6-imp`, `s6-imp-addtry`).

## 2. Droids

**Battle droid at chargen** (BT-6: Battle chassis, War Droid Mark I, Engineer):
- The Feats step's popup reads "You have been granted the following feat(s) this level: Droid Upgrade 1, Plating Proficiency: Light, Field Override" (`db-feats-granted`).
- On the grid, Droid Upgrade 1 is held. Droid Upgrade 2 is red: "Prerequisites: Droid Upgrade 1, Character Level 7". Add Feat stayed dim and did nothing; Remaining Feats stayed 1. Droid Upgrade 3 is red: "Droid Upgrade 2, Character Level 13" (`db-du1`, `db-du2`, `db-du2-addtry`, `db-du3`).
- The hub's Feats tab lists Droid Upgrade 1, Plating Proficiency: Light, Field Override and the feat I chose, Cautious (`db-hub-featstab`).

**Battle droid's level-up to 7** (`scratch-273c`):
- The popup reads "Droid Upgrade 2, Plating Proficiency: Medium, Subverted" (`bt-lu-hub`).
- An Engineer gets no feat pick at level 7, so this level-up has only a Skills step and no Feats grid. Nothing is offered at all.
- After I accepted, Abilities → Feats shows Droid Upgrade 1 → Droid Upgrade 2, both held, with an arrow (`bt-ab-feats`). Abilities lists only held feats, so Upgrade 3 can't show there.

**The other chassis at chargen.** The chassis list has four: Astromech, Assassin, Battle and Remote. I ran each to its Feats grid as an Engineer (`da-*`, `dr-*`, `ds-*`):
- Each announces Droid Upgrade 1, Plating Proficiency: Light and Field Override.
- Each holds Droid Upgrade 1, with Upgrade 2 and 3 red. Add Feat stays dim on all three; peak 66 on each (`da-du*`, `dr-du*`, `ds-du*`).
- Astromech and Remote have no Voice step, and Astromech has no Racial Skill step.
- I didn't level the other three chassis.

## 3. Heavy's prerequisites

- **Soldier** (`s-cg-hub` reads "Soldier"): Heavy reads "Prerequisites: Armor Proficiency: Medium", and Medium reads "Armor Proficiency: Light" (`s-heavy`, `s-medium`). The armour row is still held, held, held, with two arrows.
- **Scout** (`sc-hub` reads "Scout"): the same two texts (`sc-heavy`, `sc-medium`). The row is held, held, takeable, with two arrows.
- **Off Six's level-up** (Soldier 6 to 7, at 1280×720) reads "Armor Proficiency: Medium" too (`o-lu-heavy`). TEST 272 read "None" there.

## 4. Whole-screen look

- **1920×1080**:
  - Chargen for a Sith Assassin, a Soldier, a Scout and all four droid chassis: species, chassis, racial skill, model, class, hub, Voice, Portrait, Background, Attributes, Skills, Feats with its popups, Forms, Attacks, Powers, Equipment, Name and the backstory.
  - Level-up for two Sith Assassins and the Battle droid: class, hub with its popup, Skills, Powers.
  - Play, Character and Abilities.
  - Nothing is cut off, overlapping or missing, apart from the droid designation warning (Odd below).
- **1280×720** (`o-*`): chargen (species, class, hub, Skills, Feats) and Off Six's level-up (play, Character, class, hub with its popup, Feats). Nothing is cut off, overlapping or missing.
  - The chargen arrows land at 378–390 and 678–690 in 1920 terms; one 1280 pixel is 1.5 of those.

## Odd, not filed

- **Blaster Integration** says "Granted at 1st level to Astromech and Remote droids — the two chassis with no hands to hold one". Neither chassis gets it at chargen: their popups list only Droid Upgrade 1, Plating Proficiency: Light and Field Override. It's takeable for all four chassis, with Add Feat lit (`da-bi`, `dr-bi`, `ds-bi`, `db-feats`). It isn't on the order's known list.
- **The droid designation warning runs off the dialog.** I typed "Battle Six", and the red line "A designation carries no spaces — … a designation on this chassis is letters, digits, hyphe…" runs past the dialog's right edge and is cut off at the screen's edge (`db-name-warning`).
- **Soldier's class row** for a droid reads "A droid cannot take this class", and OK is dim. When another class is selected, its border is red like the other refused classes (`db-class-Soldier`, `db-class-engsel`).

## What I got wrong

- My first scratch load sat on the Welcome screen: I'd put Continue's x in my new load script wrong. Nothing was loaded; the load log says so, and I fixed the script.
- The OCR missed BT-6's name twice, once on the scratch dir and once on the real dir. Nothing was loaded either time. I loaded it by hand, with frames of the list and the click.
- At 1280×720 my New Game click hit Continue, which loaded the real BT-6 unplanned. The load log has it; its md5 was unchanged (b8a81252).
- `mksave273.py` first assumed the class line's position and stopped on BT-6's save before writing anything. I fixed it to find the line. Re-running it for Sith Seven gives the same md5 as before (22c62c17).
- My chargen scripts stalled in Skills again (different point counts). I accepted the unspent points and went on by hand.
