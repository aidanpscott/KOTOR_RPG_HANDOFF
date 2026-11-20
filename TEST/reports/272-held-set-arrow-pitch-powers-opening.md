# TEST 272: Chargen's held set, the arrow pitch, and powers opening

Real game, my Xvfb `:2`, plus my own 3840×2160 Xvfb `:5` for one native-scale capture. No K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the authored scratch save are in `MAIN_WORK/media/screens/test-272/`. Names in brackets below are files there.

Received since my last report: MAIN's TEST 271 acceptance; MAIN's TEST 272 order.

## Build

- **App**: main `fb449fe`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in. Every step below ran on this build.
- **Heads**: before the gate I checked every shared tree against origin/main. The shared HANDOFF tree was clean and 1 behind, by my own ledger commit. I fast-forwarded it (ff-only) to `32d3635`. All the others were at origin and clean.
- **Gate**: I ran `gate.py --at fb449fe` twice from the project MAIN_WORK (`gate272-1.txt`, `gate272-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at fb449fe, 6067 tests, 0 failed".
  - Both state lines: "MAIN_WORK 459d223d · HANDOFF 32d3635 · KOTOR-RPG-APP fb449fe · Lodestar a554b93 · Loom 9a1c3ef · Shelf 8f2d845 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `8f2d845`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: Off Six (`lu194-sol6`, Soldier 6 going to 7), Watch Two (`lu193-guard6b`) and Con Five (`lu192-con5`), all on the real data dir.
  - The restore copy `notes/saves272` was taken from `saves271`. Its md5s match the last BEFORE lines (Watch Two 8a9ede2a, Aoo Eighty 4d6fe9eb, Pazaak Ten 6cb1a6a7, four-200 ca0aac5f).
  - Every load has BEFORE and AFTER md5s in `loads.txt`. At the end of the session every live save I loaded still matched its restore copy: Off Six 2797c6b0, Watch Two 8a9ede2a, Con Five 426740f7. Nothing was written after a load this time.
- **Scratch save**: a copy of Watch Two cut to Jedi Guardian 4 with 19000 XP, in its own data dir `~/kotor-tester/scratch-272` (`scratch/t272-watch-four.sav`, md5 ac861519). I dropped the level 5 and 6 `levelled` events and the level-7 session events, set `class-added` levels to 4, and rebuilt the header per `writeSave`. The real saves have no edits.
- **Chargens**: a Rodian Soldier and a Rodian Scout at 1920, a Rodian Soldier at 3840×2160, a Rodian Sith Assassin at 1920, and a Rodian Soldier at 1600×900. None was played.

## Summary

Steps 1, 2, 3 and 5 pass. Step 4 passes on what it ordered, but I found one finding next to it.

| # | Check | Result |
|---|---|---|
| 1 | Chargen Soldier and Scout | **PASS**. Soldier: Light, Medium and Heavy held, two arrows, none can be added. Scout: Light and Medium held, Heavy takeable with an arrow, and I took it. |
| 2 | Arrow places vs native chargen/14 | **PASS, exact** at native 4K: cores 754–786 and 1354–1386; the third column's edge at 1603. |
| 3 | Soldier level-up (Off Six, 6 to 7) | **PASS**. The armour chain is held, none of it can be added, two arrows. |
| 4 | Powers open their next tier | **PASS** as ordered. Watch Two to 8: Stun Droid opens Disable Droid, with an arrow. Level 5: it stays red. Sith Assassin: Force Camouflage, then Improved. **FINDING 1**: Master Force Camouflage (Level 13) then opens at level 1. |
| 5 | Whole-screen look | **PASS** at 1920×1080 and 1600×900. |

## FINDING 1: Master Force Camouflage opens at chargen level 1

- On the Sith Assassin's chargen Powers grid, before any pick, Force Camouflage is takeable and Improved and Master are red (`sa-impcamo-before`).
- I took Force Camouflage, then Improved. Improved's text reads "Prerequisites: Level 7 Jedi Watchman or Sith Assassin, Force Camouflage" (`sa-impcamo-after`).
- After Improved was taken, Master Force Camouflage turned takeable, with an arrow into it, and Add Power lit. Its text reads "Prerequisites: Level 13 Jedi Watchman or Sith Assassin, Improved Force Camouflage" (`sa-camo3-after`). Remaining Powers was 0, so I couldn't add it.
- So the "Level N <class>" part of these prerequisites isn't checked: a level-1 character is offered a level-13 power.
- The "Character Level 6" part on Disable Droid is checked: it stays red at level 5 (step 4 below).
- **Question for MAIN**: the order says a chargen Sith Assassin can take Improved Force Camouflage, but its own text says Level 7. Is Improved meant to be takeable at level 1, and only Master's gate is wrong? Or should both stay red?

## 1. Chargen Feats: Soldier and Scout (1920)

- **Soldier** (`s-cg-feats`): Light → Medium → Heavy, all held, two arrows. Remaining Feats 1.
  - I selected Light and then Heavy and clicked Add Feat each time. Add Feat stayed dim (peak 66), and Remaining stayed 1 (`s-feats-light-addtry`, `s-feats-heavy-addtry`).
  - Lower down, the held Blaster Pistol, Blaster Rifle and Melee proficiencies each have an arrow to a takeable next tier, and Squad Tactics (held) has red next tiers and no arrow (`s-feats-s1`…`s6`).
  - `rule271.py` found no breaks on any of the seven frames.
- **Scout** (`sc-cg-hub2` reads "Rodian, Scout, Level 1"; `sc-cg-feats`): Light and Medium held, Heavy takeable (dim), with an arrow from Medium.
  - I took Heavy: Remaining Feats went 1 → 0, the arrow stayed, and Remove Feat lit. Heavy's text reads "Prerequisites: Armor Proficiency: Medium" (`sc-feats-heavy-taken`).

## 2. The arrow places (Soldier chargen at 3840×2160)

I ran the app on a 3840×2160 Xvfb and sized its window to fill it, so the chargen screens render at K2's native scale (`k-cg-feats`). Readings come from `scripts/blob272.py` (the bounding box of arrow teal) and `scripts/edges271.py`-style runs along each arrow row's centre line.

| | Ours (native 4K) | K2 chargen/14 (native 4K) |
|---|---|---|
| Light → Medium core (green over 150) | 754–786 | 754–786 |
| Medium → Heavy core | 1354–1386 | 1354–1386 |
| Light → Medium, every arrow pixel | 753–787 | 753–787 |
| Medium → Heavy, every arrow pixel | 1353–1387 | 1353–1387 |
| Along the row centre | 758–787, 1358–1387 | 758–787, 1358–1387 |
| Third feat column's left edge | starts at 1603 | starts at 1603 |
| Arrow height | 36 rows | 36 rows |

- The first column's edges along the row match too (422–423, 434–437, 514–517 in both).
- **Pixel by pixel** (40×44 box round each arrow, best alignment, no shift): the centre colour is 46,194,161 against K2's 46,194,162, and both peak at green 194. 116 pixels per arrow differ by more than 20, all on the sloped edges (2 to 6 a row), with a largest difference of 79. That's anti-aliasing; there's no position difference.
- At 1920 the same arrows sit at 377–392 and 677–692 (the cores), with the third column's edge at 801.

## 3. Off Six's level-up (Soldier 6 to 7)

- The level-up hub granted "Squad Tactics, Improved Squad Tactics, Both Hands, Improvised" this level (`o6-lu-hub`). See Odd below.
- **Feats** (`o6-lu-feats-a`): Light → Medium → Heavy, all held, two arrows. Remaining Feats 1.
  - I selected Medium and Heavy and clicked Add Feat each time. Add Feat stayed dim (peak 66), and Remaining stayed 1 (`o6-lu-feats-medium-addtry`, `o6-lu-feats-heavy-addtry`).
- **The other arrows**:
  - Both Hands → Improvised (both granted this level, with bright borders 46,194,162) is held to held, and Improvised's next tier is red. The checker read them as takeable only because the cells have no icons, which is on the known no-icon list (`o6-lu-feats-row3a`, `row3b`).
  - Squad Tactics → Improved Squad Tactics is held to held.
  - Each weapon proficiency has an arrow to a takeable next tier.
  - No breaks on any frame (`o6-lu-feats-s1`…`s6`).
- The arrows sit at 379–393 and 679–693 along the row, the same as chargen.
- I cancelled the level-up. Off Six's file is unchanged (2797c6b0).

## 4. Powers open their next tier

**Watch Two to level 8** (Jedi Guardian; `w-lu-powers-*`):
- Before: Disable Droid is red; its text reads "Character Level 6, Stun Droid", and Add Power is dim (peak 66) (`w-lu-powers-disable-before`).
- I took Stun Droid. Remaining Powers went 1 → 0, an arrow appeared Stun Droid → Disable Droid, the cell turned takeable, and Add Power lit (peak 136) (`w-lu-powers-stundroid-taken`, `w-lu-powers-disable-after`). Destroy Droid, its next tier, stayed red, with no arrow (`w-lu-z-pt3red`).
- **Taking it**: with Remaining Powers at 0, clicking Add Power on Disable Droid did nothing (`w-lu-powers-disable-addtry`). Watch Two's level-up gives one power, so I couldn't add both. Disable Droid lights Add Power exactly as every other takeable cell does at 0 remaining, so it's offered. See Odd below.
- The arrow sits at 375–391 along the row, the same as TEST 271's.
- The checker's one flag is on the frame after the pick: the white selection border on Stun Droid hides its edge.

**At level 5** (the scratch copy at Jedi Guardian 4, going to 5; `x-character` reads "Jedi Guardian 4", 19000 XP):
- I took Stun Droid (Remaining Powers 1 → 0). Disable Droid stayed red, with no arrow, and Add Power stayed dim (`x-lu-disable-before`, `x-lu-stundroid-taken`, `x-lu-disable-after`, `x-lu-disable-addtry`).

**Chargen Sith Assassin** (`sa-class-picked`, `sa-hub2` reads "Sith Assassin"):
- Remaining Powers 2. I took Force Camouflage (2 → 1). An arrow appeared to Improved Force Camouflage, and it turned takeable (`sa-camo-taken`, `sa-impcamo-after`).
- I took Improved (1 → 0). A second arrow appeared, Improved → Master (`sa-impcamo-taken`). See FINDING 1.

## 5. Whole-screen look

- **1920×1080**: chargen (species, class, hub, Skills with its prompt, Feats with the granted popups, Forms, Attacks with the recommended popup, Powers with its help) and level-up (class, hub with the granted popup, Feats, Powers), plus play and the Character sheet. Nothing cut off, overlapping or missing.
- **1600×900** (`o-*`): chargen (species, class, hub, Skills, Feats) and level-up (play, Character, class, hub with its granted popup, Feats). Nothing cut off, overlapping or missing.
  - The chargen arrows land at 379.2–393.6 and 679.2–693.6 in 1920 terms, the same as at 1920.

## Odd, not filed

- **Add Power and Add Attack light at 0 remaining.** Any takeable cell lights the button (peak 136, against 66 on a red cell), and clicking it does nothing. It's on Watch Two's Disable Droid, Breath Control and Force Camouflage, and on the Assassin's Cleave on Attacks (`w-lu-z-*`, `sa-attacks-picked`).
- **Heavy's prerequisites differ by class.** The Soldier's Heavy (held, granted) reads "Prerequisites: None" at chargen and level-up (`s-feats-heavy-addtry`, `o6-lu-feats-heavy-addtry`). The Scout's Heavy reads "Armor Proficiency: Medium" (`sc-feats-heavy-taken`).
- **Squad Tactics is listed again at level 7.** Off Six's popup "You have been granted the following feat(s) this level" lists Squad Tactics, which a Soldier holds from level 1, as well as Improved Squad Tactics (`o6-lu-hub`).
- Watch Two took its level 7 as Jedi Watchman, so Force Camouflage is rightly takeable for it.

## What I got wrong

- My first Scout chargen built a Soldier: I'd changed the wrong one of my script's two class clicks. The hub frame showed "Soldier", so I took no readings from it, fixed the script and redid it (`sc-cg-hub2`).
- My first Off Six load matched no name: OCR reads "Off Six" as "Orr Six". Nothing was loaded; the load log says so, and the retry used a looser pattern.
- My first scratch save read as Jedi Guardian 3, because I'd also cut its level-4 `levelled` event. I re-authored it and logged both loads.
- One run of cell-name reads on Watch Two's Powers lagged a click behind. I redid those one click at a time with longer waits, and only those readings are used above.
- My chargen scripts stalled in Skills three times (different point counts). I accepted the unspent points and went on by hand.
- I stopped my own Xvfb `:5` with `kill $(pgrep -f ...)`, not by its recorded PID. It was mine, and only it went.
