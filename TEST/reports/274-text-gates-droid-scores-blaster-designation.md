# TEST 274: Text gates as data, droid scores, Blaster Integration, and the designation refusal

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the authored scratch saves are in `MAIN_WORK/media/screens/test-274/` (MAIN_WORK `6efe93f0`). Names in brackets below are files there. Frames from the 1280×720 window are the `-720` crops.

Received since my last report: MAIN's TEST 273 acceptance; MAIN's TEST 274 order.

## Build

- **App**: main `6aaa63e`, a fresh clone, built debug. Lens `e449221` and Lodestar `a554b93` compiled in. Every step ran on this build.
- **Heads**: before the gate I checked every shared tree against origin/main.
  - The shared HANDOFF tree's unpushed commit from my last message (1fdd108) had been pushed by its owner as `7a21942`. That left the tree clean and 1 behind, by my own ledger commit, so I fast-forwarded it (ff-only) to `42ddf61`.
  - All the others were at origin and clean.
- **Gate**: I ran `gate.py --at 6aaa63e` twice from the project MAIN_WORK (`gate274-1.txt`, `gate274-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 6aaa63e, 6093 tests, 0 failed".
  - Both state lines: "MAIN_WORK bfa216c9 · HANDOFF 42ddf61 · KOTOR-RPG-APP 6aaa63e · Lodestar a554b93 · Loom 9a1c3ef · Shelf d4caf41 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: `d4caf41`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**:
  - The restore copy `notes/saves274` was taken from `saves273`.
    - The six saves this test touches match it (BT-6 b8a81252 among them).
    - Four other live saves differ from it: Aoo Eighty, Four Up, open-walker-259 and Pazaak Ten. The app rewrote those in earlier sessions; TEST 271 noted Aoo Eighty's. The copy keeps the earlier versions.
  - New characters from chargen on the real data dir, all copied into `saves274`:

    | Name | Species | Class | md5 |
    |---|---|---|---|
    | T3-58 | Astromech | Bounty Hunter | 58ed841c |
    | Sentry-7 | Remote | Engineer | ec127887 |
    | HK-59 | Assassin | Engineer | 2d5d6e57 |
    | War-Nine | Battle droid | Bounty Hunter | 87f846d0 |
    | Gate Four | Rodian | Soldier | 869df368 |
    | HK-78 | Assassin, at 1280×720 | Engineer | 39f0b939 |

  - Every load has BEFORE and AFTER md5s in `loads.txt`. At the end of the session all the live saves above matched their restore copies.
- **Scratch saves**, each in its own data dir (`scratch-274a` to `-274j`).
  - Authored with `scripts/mksave273.py` (class levels, matching `levelled` events, and the XP for one more level). `scripts/addfeats272.py` added the listed feats.
  - Copies are in `scratch/`. I cancelled every level-up, and each file's md5 was unchanged afterwards, apart from 274g (see "What I got wrong").

  | Dir | From | Level | Feats added | md5 |
  |---|---|---|---|---|
  | 274a | T3-58 | Bounty Hunter 3 | Logic Upgrade: Combat | 320e92f3 |
  | 274b | T3-58 | Bounty Hunter 7 | Close Combat, Logic Upgrade: Combat | 91f521ac |
  | 274c | T3-58 | Bounty Hunter 9 | Logic Upgrade: Combat, Tactician | 5c280da0 |
  | 274d | BT-6 | Engineer 4 | Logic Upgrade: Combat | 7bb1dfb1 |
  | 274e | BT-6 | Engineer 10 | Logic Upgrade: Combat, Tactician | 281db75d |
  | 274f | War-Nine | Bounty Hunter 3 | none | 0e3719d4 |
  | 274g | Gate Four | Soldier 2 | none | bbd40980 |
  | 274h | Gate Four | Soldier 3 | none | 716bb402 |
  | 274i | Gate Four | Soldier 6 | Close Combat, Advanced Dueling | ce0ea323 |
  | 274j | Gate Four | Soldier 7 | Close Combat, Advanced Dueling | ea33e8f6 |

  Gate Four holds Dueling from chargen.

## Summary

Steps 2, 3 and 4 pass. Step 1 passes apart from Finding 1. Step 5 passes, with a note on spacing. Step 6 passes.

| # | Check | Result |
|---|---|---|
| 1 | Level gates | **PASS** for Improved Close Combat (8), Advanced Dueling (4), Master Dueling (8), Tactician (5) and Battle Droid (11): each is red one level short and takeable at its level. Close Combat is takeable at 4. **FINDING 1**: one level short, Close Combat isn't red; it isn't on the grid at all. |
| 2 | Chassis gates | **PASS**. An Astromech at level 4 isn't offered Close Combat, while a Battle droid at 4 is. An Astromech holding Close Combat gets Improved red at 8. Synthesised Voice is offered to the Astromech and the Remote, not to the Battle droid or the Assassin. |
| 3 | Droid scores | **PASS**. All four chassis read the documented spread at chargen, and the same six scores and Vitality in play. TEST 273's BT-6 now reads 14/12/14/10/12/10 in play. |
| 4 | Blaster Integration | **PASS**. The Astromech and the Remote hold it at chargen, and it's announced and not offered. The Battle droid and the Assassin aren't granted it, and both bought it. |
| 5 | Designation refusal | **PASS** at 1920 and 1280×720. Note: the wrapped warning has no space below it (see step 5). |
| 6 | Whole-screen look | **PASS** at 1920×1080 and 1280×720. |

**FINDING 2**: Plating Proficiency: Light, "Droids only.", is offered to an organic and can be taken.

## FINDING 1: Close Combat is hidden one level short, not red

- **Gate Four at the level-up to 3** (274g): Close Combat isn't on the Feats grid. The scan reads Cautious, then Conditioning (`g-lu-scan.txt`, `g-lu-page0`).
  - On the same grid, Advanced Dueling is red: "Prerequisites: Dueling, Character Level 4". Add Feat stays dim (`g-advd`, `g-advd-addtry`).
- **At the level-up to 4** (274h): Close Combat is between Cautious and Conditioning. It's takeable ("Prerequisites: Character Level 4"), and taking it worked: Remaining Feats 1 → 0 (`h-lu-scan.txt`, `h-cc`, `h-cc-taken`).
- **Code**: `lib/chargen/records.dart` `buyableAtLevelFor` (about line 2667) adds a chain only when its next tier's `level` is at or below the level being taken. A chain whose head is above that level gets no row.
  - Improved Close Combat, Advanced Dueling and Master Dueling show red one level short only because their chains are already held.
  - Logic Upgrade: Combat has no level, so Tactician and Battle Droid aren't affected.
- **Chargen** works the same way: Close Combat isn't on any chargen grid I scanned. That covers the Rodian Soldier and all four chassis (`o-cg-scan.txt`, `a-cg-scan.txt`, `r-cg-scan.txt`, `s-cg-scan.txt`, `b-cg-scan.txt`).
  - So at chargen, the Astromech's missing Close Combat can't be told apart from the level gate. Step 2 rests on the level-up checks below.

## FINDING 2: An organic can take Plating Proficiency: Light

- Its pane reads "Prerequisites: None" and "Droids only. A chassis rated to carry plating, earned by level rather than granted by class."
- **Gate Four's chargen grid** (`o-plating`, `o-plating-taken`, `o-plating-removed`):
  - Plating Proficiency: Light is takeable, with Add Feat lit (136).
  - I took it: Remaining Feats 1 → 0, and Remove Feat shows.
  - I removed it, and took Dueling instead.
- **Gate Four's level-ups** to 3 and 4 list it too (`g-lu-scan.txt`, `h-lu-scan.txt`).
- **Data and code**: `feats.toml` files `plating_proficiency_light` under section "3".
  - `buyableAtLevelFor` skips section 3 for droids and section 4 for organics, so this chain is offered to organics.
  - Droids still get it, as a grant.
- TEST 273's known list included Plating ("gates that live only in a feat's text"). This order's known list has only Hardened Chassis, so I'm filing it.

## 1. Level gates

Gate Four levels as a Soldier (a feat every level). The droids level as Bounty Hunters (feats at 4, 8 and 10) and Engineers (feats at 5 and 11). Each character sheet I framed read the expected class and level before the level-up (`*-character`). I didn't frame 274h's; its level-up hub read Level 4.

| Feat | One level short | At its level |
|---|---|---|
| Close Combat (4) | Level 3 (274g): not on the grid. **FINDING 1** | Level 4 (274h): takeable, pane "Character Level 4". Taken, Remaining 1 → 0 (`h-cc`, `h-cc-taken`) |
| Improved Close Combat (8) | Level 7 (274i): red, pane "Close Combat, Character Level 8". Add Feat dim (66); clicking it changed nothing (`i-icc`, `i-icc-addtry`) | Level 8 (274j): takeable (Add Feat 136). Taken, Remaining 0 (`j-icc`, `j-icc-taken`) |
| Advanced Dueling (4) | Level 3 (274g): red, pane "Dueling, Character Level 4". Add Feat dim (`g-advd`, `g-advd-addtry`) | Level 4 (274h): takeable. Taken, Remaining 0 (`h-advd`, `h-advd-taken`) |
| Master Dueling (8) | Level 7 (274i): red, pane "Advanced Dueling, Character Level 8". Add Feat dim (`i-mdu`, `i-mdu-addtry`) | Level 8 (274j): takeable. Taken, Remaining 0 (`j-mdu`, `j-mdu-taken`) |
| Logic Upgrade: Tactician (5) | T3-58 at level 4 (274a): red, pane "Logic Upgrade: Combat, Character Level 5". Add Feat dim (`a4-tac`, `a4-tac-addtry`) | BT-6 at level 5 (274d): takeable. Taken, Remaining 0 (`d5-tac`, `d5-tac-taken`) |
| Logic Upgrade: Battle Droid (11) | T3-58 at level 10 (274c): red, pane "Logic Upgrade: Tactician, Character Level 11", with Tactician held (peak 231). Add Feat dim (`c10-lub`, `c10-lub-addtry`) | BT-6 at level 11 (274e): takeable. Taken, Remaining 0 (`e11-lub`, `e11-lub-taken`) |

- No arrow runs from held Close Combat into the red Improved tier at 7 (`i-mdu`).

## 2. Chassis gates

- **Close Combat**:
  - **T3-58 at level 4** (274a): not on the grid. The scan reads Cautious, then Droid Interface (`a4-lu-scan.txt`).
  - **Control**: War-Nine, a Battle droid Bounty Hunter at level 4 (274f), has Close Combat takeable, with Add Feat lit and pane "Character Level 4" (`f-cc`). So the Astromech's is the chassis gate, not the level gate.
- **Improved Close Combat**: T3-58 at level 8 holding Close Combat (274b).
  - Close Combat is held (peak 216), and Improved is red. Add Feat stays dim; clicking it changed nothing (`b8-cc`, `b8-icc`, `b8-icc-addtry`).
  - Its pane reads only "Close Combat, Character Level 8", both of which T3-58 meets (see Odd).
- **Synthesised Voice** on the chargen grids:
  - **Astromech** (T3-58): takeable (Add Feat 136), and I took it (`a-synth`, `a-synth-taken`). Play's Abilities lists it (`a-ab-feats`).
  - **Remote** (Sentry-7): takeable (Add Feat 136), and I took it (`r-synth`, `r-synth-taken`).
  - **Battle** (War-Nine) and **Assassin** (HK-59): not on the grid (`b-cg-scan.txt`, `s-cg-scan.txt`).
  - T3-58's level-ups list it too (`a4-lu-scan.txt`).

## 3. Droid scores

| Chassis (character) | Chargen Attributes | Chargen hub Vitality | Play, Character sheet |
|---|---|---|---|
| Astromech (T3-58, Bounty Hunter) | 8/12/12/16/14/10 (`a-attr2`) | 11/11 (`a-name`) | 8/12/12/16/14/10, 11/11 (`a-character`) |
| Remote (Sentry-7, Engineer) | 6/16/10/16/14/10 (`r-attr`) | 8/8 (`r-name`) | 6/16/10/16/14/10, 8/8 (`r-character`) |
| Assassin (HK-59, Engineer) | 12/16/12/14/10/8 (`s-attr`) | 9/9 (`s-name`) | 12/16/12/14/10/8, 9/9 (`s-character`) |
| Battle (War-Nine, Bounty Hunter) | 14/12/14/10/12/10 (`b-attr`) | 12/12 (`b-name`) | 14/12/14/10/12/10, 12/12 (`b-character`) |

- T3-58's save records the same six scores in its `ability-set` events (`scripts/dump274.py`).
- **BT-6**, TEST 273's Battle Engineer, loaded on this build with its md5 unchanged (b8a81252). Play now reads 14/12/14/10/12/10 and Vitality 10/10 (`bt6-character`). On 44cf61f it read 16/12/16/8/12/8 and 11/11.
- **HK-78**, made at 1280×720, reads 12/16/12/14/10/8 and 9/9 in play (`o720-s-character-720`).

## 4. Blaster Integration

- **Astromech** (T3-58):
  - The Feats popup reads "Droid Upgrade 1, Plating Proficiency: Light, Blaster Integration" (`a-feats-granted`).
  - On the grid it's held, and Add Feat is dim (`a-bi`).
  - Play's Abilities lists it, and the save records it as `granted` (`a-ab-feats`).
- **Remote** (Sentry-7):
  - The popup reads "Droid Upgrade 1, Plating Proficiency: Light, Blaster Integration, Field Override" (`r-feats-granted`).
  - The cell is held (peak 225), and Add Feat stays dim (66). Clicking it left Remaining Feats at 1 (`r-bi`, `r-bi-addtry`).
  - Play's Abilities lists it (`r-ab-feats`).
- **Assassin** (HK-59):
  - The popup reads "Droid Upgrade 1, Plating Proficiency: Light, Field Override" (`s-feats-granted`).
  - Blaster Integration is takeable (cell 88, Add Feat 136). Buying it took the cell to 225 and Remaining to 0 (`s-bi`, `s-bi-taken`).
  - Play's Abilities lists it (`s-ab-feats`).
- **Battle** (War-Nine):
  - The popup reads "Droid Upgrade 1, Plating Proficiency: Light" (`b-feats-granted`).
  - Blaster Integration is takeable. Buying it took the cell 88 → 225 and Remaining 1 → 0 (`b-bi`, `b-bi-taken`).
- **HK-78** at 1280 bought it the same way (`o720-s-bi-taken-720`).

## 5. The designation refusal

Positions were read down the dialog at x 700 (467 at 1280) with `scripts/dlg274.py`. "Bottom" is the dialog's bottom edge; Random, Cancel and OK always sat inside it.

| Case | Warning lines | Text rows | Random Name top | Bottom | Frame |
|---|---|---|---|---|---|
| **1920**, valid (T3-58, HK-59) | none | — | 529 | 656 | `a-name-valid`, `s-name-valid` |
| **1920**, "Astro Nine" (T3 model) | 2 | 506–532 | 534 | 661 | `a-name-invalid` |
| **1920**, "HK-4" | 2 | 506–532 | 534 | 661 | `s-name-hk4` |
| **1920**, "HK-47" | 3 | 506–548 | 550 | 677 | `s-name-hk47` |
| **1280**, valid "HK-78" | none | — | 352 | 437 | `o720-name-valid-720` |
| **1280**, "HK-4" and "Hk 4" | 2 | 338–355 | 356 | 440 | `o720-name-hk4-720`, `o720-name-hk-space-720` |
| **1280**, "HK-47" | 3 | 338–365 | 367 | 451 | `o720-name-hk47-720` |

- The warning wraps inside the dialog, above Random Name and Cancel, and every line is inside the dialog's width.
  - At 1920 the text spans x 579–1341, inside the field and buttons (about 576–1344).
- A valid designation put the dialog back to its rows every time.
- **A free model with no Random button** (Sentry-7, Sentry Droid MK 2):
  - Empty, the dialog reads "A designation is required …" (`r-name-empty`).
  - "Rem One" wraps to three lines, 526–571, with Cancel at 590 (`r-name-invalid`).
  - The dialog doesn't grow: its bottom stays at 656.
- **Note**: on the prefixed models the dialog grows only by the text's height less the 27 px gap it already had, so nothing is left below the text.
  - At 1920 the two-line text ends 1 px above Random Name's border. The tail of the "y" in "already" crosses that border, by 1–2 px (rows 533–535 against the border at 534).
  - At 1280 the text's last row is the row just above the border.
  - Above the text there are 4 px to the field.

## 6. Whole-screen look

- **1920×1080**:
  - Chargen for all four chassis and the Rodian Soldier: species, chassis, racial skill, model, class, hub, Voice, Portrait, Background, Attributes, Skills, Feats with its popups, Attacks with the recommended popup, Equipment, Name with the designation dialog, and the backstory.
  - Level-ups for the Soldier and both droid classes: class, hub with its popup, Feats.
  - Play, Character and Abilities.
  - Nothing is cut off, overlapping or missing, apart from the designation spacing above.
- **1280×720** (`o720-*`):
  - Chargen for HK-78 (model, hub, Attributes, Skills, Feats, Name with the dialog, backstory) and a Soldier (species, hub, Background, Skills with the unspent-points question, Feats with both popups).
  - Level-ups for Gate Four (274h) and BT-6 (274d): class, hub with its popup, Feats.
  - Play, Character and Abilities for HK-78 and Gate Four.
  - Nothing is cut off, overlapping or missing.

## Odd, not filed

- **A droid Bounty Hunter holds feats a droid can't use.**
  - T3-58 holds Armor Proficiency Light, Medium and Heavy and Weapon Proficiency: Melee Weapons. Its chargen grid shows the armour row held, with arrows, and play's Abilities lists all four (`a-feats-granted`, `a-ab-feats`). War-Nine's chargen grid shows the same armour row (`b-feats-granted`).
  - They come from the class's starting proficiencies. Melee Weapons' effect reads "Droids cannot take this.", and droids wear plating, not armour.
  - Engineer droids don't get them.
- **Improved Close Combat is red for an Astromech with no reason shown.** Its pane lists only "Close Combat, Character Level 8", and T3-58 at 8 meets both. The chassis bar is in Close Combat's own text, not on this tier's pane (`b8-icc`).
- **Skill Focus is red on T3-58's chargen grid**, and its pane reads "Prerequisites: None" (`a-redcell`). I didn't check it on the other grids.
- **No icon**: Synthesised Voice has none on the grid or in play's Abilities, and Plating Proficiency: Light has none in the granted popup or in Abilities (`a-synth-taken`, `a-feats-granted`, `a-ab-feats`).
- **The Remote, Assassin and Battle droids all show the same portrait**, a humanoid droid head, in chargen and play (`r-character`, `s-character`, `b-character`).

## What I got wrong

- **OCR misses.** The OCR missed BT-6's name twice (once on the real dir, once on 274d), as in TEST 273. Nothing was loaded either time.
  - For 274e and the second 274d load, I gave the load script a pattern that can't match, so it stopped on the list.
  - I loaded every BT-6 by hand, with frames of the card and the click. Each card reads BT-6.
- **A missed click on 274g.** At 1280 my click for the Abilities icon used a position that isn't on the play screen's icon bar. A second click then walked Gate Four into the next room on 274g, where a fight began.
  - The game autosaved that scratch file at 07:54:21 (bbd40980 → 009ab63b). The load log notes it.
  - The authored original is `scratch/t274g-gate-four.sav`, and nothing else was read from 274g after that.
- **My first feat scan** clicked between cells on a page that had scrolled by part of a row. I rewrote it to find the cells by their borders (`scripts/cells274.py`) and rescanned.
- **Lost keystrokes at 1280.** After my framing step parked the pointer outside the 1280 window, my next two entries in the designation field didn't register; those first frames repeat HK-4. I retyped them with a click into the field first.
- **Skills stalls.** My chargen script stalled in Skills at 1280 (it picked a Dashade, with a different point count). I accepted the unspent points and went on by hand.
- **Ledger slip.** In the ledger I first overwrote TEST 273's order line with TEST 274's. I put it back before committing.
