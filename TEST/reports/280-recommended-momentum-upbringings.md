# TEST 280: Recommended on Attributes and Skills, Momentum, the upbringings, and a Medical droid in play

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, both gate outputs, the load log and Load-click frames, the dev logs and my scripts are in `MAIN_WORK/media/screens/test-280/5c1bbde/` (MAIN_WORK `032a0915`; see its PROVENANCE.txt).

Received since my last report: MAIN's first TEST 280 order (logged HANDOFF `eceb0e4`); MAIN's TEST 279 acceptance and the reissued TEST 280 order (logged `cb688aa`).

## Build

- **Waiting**: at 11:20 neither 5c1bbde nor 966cf6a was on GitHub; both existed only on Coder's local branches. I touched nothing and polled. The Shelf landed at 11:22 and the app by 11:23.
- **App**: main `5c1bbde`, a fresh clone in `builds/test280`, built debug through `tool/one_at_a_time.sh` (pubspec.lock unchanged).
- **Gate**: `scripts/gate.py --at 5c1bbde` twice from the project MAIN_WORK, after every head was at origin and clean (11:24:22). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at 5c1bbde, 6129 tests, 0 failed".
  - Both state lines: "MAIN_WORK f74317f1 · HANDOFF cb688aa · KOTOR-RPG-APP 5c1bbde · Lodestar a554b93 · Loom 9a1c3ef · Shelf 966cf6a · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: my data dir's packages moved to `966cf6a`. check_shelf: "35 rules files and 151 standard blueprints, all identical".
- **Saves**: every character in its own fresh scratch data dir. Seven loads of scratch copies, each with BEFORE and AFTER md5s and a frame at the Load click (`loads.txt`). No level-up was accepted, and every copy's md5 is unchanged at the end. The live saves equal `notes/saves275` apart from the four known, at the start and the end.
- **Window sizes**: 1920x1080 and 1366x768 (new).

## Step 1: Attributes at chargen — PASS

| Character | Recommended from all 8s | One attribute moved by hand first, then Recommended |
|---|---|---|
| Human Soldier | 16 14 14 10 12 10, Remaining 0 | INT 14 by hand: INT left at 14; 16 14 14 14 10 8, Remaining 0 |
| Human Bounty Hunter | 14 16 14 10 12 10, Remaining 0 | CHA 12 by hand: CHA left at 12; 14 16 14 8 12 12, Remaining 0 |
| Human Smuggler (1366x768) | 10 16 10 14 12 14, Remaining 0 | — |

- Recommended is lit with points to spend and goes dim once Remaining is 0.
- **Battle droid**: the chassis spread is fixed and Recommended is dim. Clicking it changes nothing on the page (`k-06`, `k-07`).
- **Read from the Shelf**: all 19 spreads in `recommended.toml` cost exactly 30.

## Step 2: Skills at chargen — PASS

Each class's picks against its row in `recommended.toml`. The Human's two skill bonuses went to skills outside the class, so they don't touch the result.

| Character | Points | After Recommended (every other skill 0, Remaining 0) |
|---|---|---|
| Human Soldier | 12 | Medicine 4, Awareness 4, Demolitions 4 |
| Human Bounty Hunter | 16 | Survival 4, Streetwise 4, Intimidate 4, Athletics 4 |
| Human Smuggler (my choice, 1366x768) | 36 | Stealth, Demolitions, Security, Awareness, Slicing 4 each; Persuade 2; Pilot, Sleight of Hand, Streetwise 4 each; Appraise 2 |
| Battle droid Engineer | 16 | Repair 2, Slicing 4, Security 4, Awareness 4, Appraise 2 |

- **Persuade and Repair stop at 2 — not a fault.** Persuade carries the Taris "Aptitude: Persuade +2"; Repair carries a +2 bonus (in play: rank 2, bonus +2, total 4, `k-28`). With a point freed by hand, neither shows a + at 2 (`i-19`, `k-12`). So the hand cap counts the +2, as the Skills help says ("A +2 from a species or homeworld does not raise it"). Recommended stops where a player must, and spends the rest on the next skill in the row.
- **Read from the Shelf**: each base class's row lists exactly its `class_skills`, and each of the 19 prestige rows equals its `class_skills_ranked`.

## Step 3: Skills at level-up — PASS; no prestige class reachable

| Save (scratch copy) | Level | Before | After Recommended |
|---|---|---|---|
| SX-275, Battle droid Scout | 6 to 7 | 25 points, all ranks 0 | Slicing 10, Demolitions 10, Repair 5, Remaining 0 |
| Sentry-7, Remote Engineer | 12 to 13 | 7 points, Repair 0 | Repair 7, Remaining 0, nothing else moved |
| Gate Four, Rodian Soldier | 2 to 3 | 4 points, Medicine 0 | Medicine 4, Remaining 0, nothing else moved |
| Gate Four at 1366x768 | 2 to 3 | 4 points | Remaining 0 |

- Recommended is lit for the class taking the level each time.
- **Prestige**: none of my saves qualifies. The two that reach level 12 are droids, and every prestige class refuses a droid (FINDING 1).

## Step 4: the Upbringing page — PASS

All nine panes show a description, from Noble's "You were born into wealth, title, or political standing. Servants answered, tutors taught, and doors opened before you reached them. ..." to Unknown's "You do not know where you came from. ..." (`a-upb-bg.txt`, crops in `frames/a-upb-bg/`). There's no PT number or note. A stray first character in the OCR is the crop edge; the frames read "You".

## Step 5: Momentum's pane — PASS

On SX-275's Abilities > Feats (Momentum written as held in TEST 278): "Prerequisites: Character Level 1 / Each kill feeds the next, building into a pace no enemy can match. / When you reduce an enemy to 0 or below, +1 to attack rolls for 10 rounds. Another kill while it lasts doesn't raise it past +1." (`b-04`). The gap check reads it single-spaced.

## Step 6: a Medical droid in play — PASS

A Battle droid Engineer with the Medical Droid programming, MD-280. Equipment showed Medpac alone, selected, with OK lit (`k-19`). In play, the inventory lists Ion Blaster (equipped), Computer Spike ×2, Medpac ×2 and Repair Kit ×2 (`k-26`).

## Step 7: whole-screen look — no faults

- **1920**: chargen for the Soldier, the Bounty Hunter and the Battle droid, from species to Play. Level-up for SX-275, Sentry-7 and Gate Four: class, granted list, hub, Skills.
- **1366x768**: the Smuggler's chargen from species to Feats (help, granted list, grid). Gate Four's level-up: class, granted list, hub, Skills, Feats.
- I saw no clipping, overlap or cut-off text in scaled copies.

## FINDING 1: every prestige class refuses a droid, against CLASS-ROSTER-01 §3b

On the level-up class page, a droid gets "A droid cannot take this class." on every prestige class, with OK dim:
- Sentry-7 (Remote Engineer 12): Tech Specialist (`d-05`).
- War-Nine (Battle Bounty Hunter 12): Juggernaut, Commando and Droid Master (`g-02`, `g-04`, `g-05`).

CLASS-ROSTER-01 §3b ("DROIDS AND PRESTIGE CLASSES — PT-577") opens most of these to droids:
- Officer, Tech Specialist and Droid Master: "OPEN".
- Juggernaut: "OPEN, requirement SWAPPED", closed to Astromech and Remote only.
- Commando: "OPEN to Assassin and Battle ONLY".

The Shelf agrees: `classes.toml` gives Commando "only:assassin,battle" and Juggernaut "closed:astromech,remote". The app's refusal is `classRefusal` in `lib/chargen/class_screen.dart`, which bars a droid from any class outside `droidOpenClassIds`. That set holds only the classes with a droid array (`records.dart:3142`), and no prestige class has one.

This isn't from this hash, and TESTs 196, 273 and 276 saw only the base Soldier refusal. It blocks step 3's prestige try for droids. I didn't check whether a droid that met an entry would get past it. None of my saves meets one.

## Odd, not filed

- **The Skills pane hides Repair's +2.** At chargen, the Battle droid's Repair pane reads "Point Cost 1 · maximum rank 4 · Aptitude: class", but there's no + past rank 2 and nothing on the page says why. Persuade's pane at least names "homeworld".
- **Recommended's fill order on Attributes isn't top to bottom.** With CHA held at 12, the Bounty Hunter got INT 8 and WIS 12, not INT 10 and WIS 10. It looks like a priority order. All 30 points are spent either way.
- **sith_assassin's spread** in `recommended.toml` has DEX 15, the only odd score in the table. It still costs 30.

## What I got wrong

- **Fresh launches**: the first menu click after launch was lost twice before I activated the window. I redid both, with no effect on results.
- **Off Six**: I copied the live save (lu194-sol6) before checking its package. It's in my tester-bolt package, which the library didn't scroll to, so I didn't load it and used Gate Four instead.
- **A false alarm**: SX-275's level-up class list first looked like it stopped at Saboteur. A reload and slower scroll showed the full list with the Force and prestige classes (`b2-*`).
- **Coverage**: no organic save reaches a prestige level, so no prestige class's Skills Recommended was tried.
