# TEST 279: closed aptitudes at Equipment, the Upbringing page, a reset, and TEST 278's gaps

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, both gate outputs, the sweeps with their gap checks, the programming and upbringing walks, the dev logs and my scripts are in `MAIN_WORK/media/screens/test-279/b63ea9c/` (MAIN_WORK `94c35f20`; see its PROVENANCE.txt).

Received since my last report: MAIN's TEST 278 acceptance (logged HANDOFF `97537b2`); MAIN's TEST 279 order (logged `db9e91c`).

## Build

- **App**: main `b63ea9c`, a fresh clone from GitHub in `builds/test279`, built debug through `tool/one_at_a_time.sh` (pubspec.lock unchanged). Lens `e449221` and Lodestar `a554b93` are the locked refs.
- **Heads**: at 07:32 Coder's push sitting was running (app 1 ahead, MAIN_WORK 2 ahead, shared HANDOFF 1 ahead and 1 behind). I touched nothing. By 07:35:16 every shared tree was at origin and clean.
- **Gate**: `scripts/gate.py --at b63ea9c` twice from the project MAIN_WORK. Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at b63ea9c, 6126 tests, 0 failed".
  - Both state lines: "MAIN_WORK f64283b2 · HANDOFF 0dbfc84 · KOTOR-RPG-APP b63ea9c · Lodestar a554b93 · Loom 9a1c3ef · Shelf b9bc862 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: my data dir's packages at `b9bc862`. check_shelf: "34 rules files and 151 standard blueprints, all identical".
- **Display**: the machine had rebooted overnight. I restarted Xvfb `:2` (35508) and xsettingsd (35521) detached.
- **Saves**: no loads and no saves this test. Every character was a chargen run in a fresh scratch data dir, stopped before Play. The live saves equal `notes/saves275` apart from the four known, at the start and the end.
- **Window sizes**: 1920x1080 and 1440x900.

## Step 1: Equipment with a closed aptitude — PASS at both sizes

Profession Bonus rows and the state of OK on first opening Equipment, droid Engineers:

| Chassis, programming | 1920 | 1440x900 |
|---|---|---|
| Battle, Medical | Medpac (2) alone, selected; OK lit | the same |
| Assassin, Medical | Medpac (2) alone, selected; OK lit | the same |
| Remote, Medical | Medpac; Aptitude: Medicine; OK dim | the same |
| Astromech, Medical | Medpac; Aptitude: Medicine; OK dim | the same |
| Battle, Salvage | Parts; Aptitude: Scavenging; OK dim | the same |
| Remote, Salvage | Parts (200cr) alone, selected; OK lit | the same |

No "Aptitude: —" row anywhere.

## Step 2: the Upbringing page — PASS

All nine panes are empty, Bastard and Unknown included (`s-upb-bg.txt` and crops). No PT number or note.

## Step 3: a reset — PASS

Human Soldier, Tutorial Popups on, 1920:

1. **First pass**: Feats opened with the help box alone (`s-10`). Closing it brought up the granted list, Squad Tactics (`s-11`). I took a feat and finished Feats.
2. **Reset**: I changed Background and OK'd "Every step after this one will be lost. Proceed?" (`s-14`). Attributes came back at 30 unspent with no help box (`s-16`).
3. **Second pass**: after Attributes and Skills, Feats opened with the granted list (Squad Tactics) and no help box (`s-18`).

The droid passes after a reset (Battle and Remote, Medical to Salvage) did the same at both sizes. The Feats page that a plain reopen from the hub shows, with no reset, has no granted list.

## Step 4: TEST 278's gaps — PASS

- **Remote chargen Feats grid**: 68 panes, all single-spaced by the gap check.
- **Astromech chargen Feats grid**: 65 panes, all single-spaced.
- **Droid Equipment at 1440x900**: all six cases in step 1, plus Salvage on the Battle droid at both sizes.

## Step 5: whole-screen look — no faults

- **Droid**: all four chassis at 1920 and 1440x900, from chassis to Equipment.
- **Organic**: the Human Soldier at 1920, from species to Feats.

I saw no clipping, overlap or cut-off text, viewing scaled copies.

## Odd, not filed

Nothing new.

## What I got wrong

- **Coverage**: I didn't finish a character to Play, so "get the Medpacs outright" rests on the Equipment page (Medpac alone, selected, OK lit), not on an inventory.
- **Organic chargen this time was 1920 only**; the odd size was covered by the droids.
