# TEST 275: TEST 274's fixes

Real game, my Xvfb `:2`, no K2 running. Text only. Frames, the load log (with a frame at every Load click), both gate outputs, the dev logs, my scripts and the authored scratch saves are in `MAIN_WORK/media/screens/test-275/` (MAIN_WORK `1105ade6`). Names in brackets below are files there. Frames named `o720-*` were taken with the window at 1280×720.

Received since my last report: MAIN's welcome and answers to the gaps (TEST 274 acceptance resent); MAIN's TEST 275 order.

## Build

- **App**: main `c5b65a3`, a fresh clone from GitHub, built debug through `tool/one_at_a_time.sh` (11 s, pubspec.lock unchanged). Lens `e449221` and Lodestar `a554b93` are the locked refs.
- **Heads**: before the gate I checked every shared tree against origin (ls-remote) and for local changes. All were at origin and clean, apart from the shared HANDOFF, which was one behind by my own ledger commit; I fast-forwarded it (ff-only) to `ba20f4c`.
- **Gate**: `gate.py --at c5b65a3` twice from the project MAIN_WORK (`gate275-1.txt`, `gate275-2.txt`). Both read "SENDABLE — 5 warning(s)" and "FOR TESTER — CORE at c5b65a3, 6103 tests, 0 failed".
  - Both state lines: "MAIN_WORK 747ad21f · HANDOFF ba20f4c · KOTOR-RPG-APP c5b65a3 · Lodestar a554b93 · Loom 9a1c3ef · Shelf af7a8e1 · Atlas 0b7cc47 · Lens e449221".
- **Shelf**: my data dir's packages fast-forwarded to `af7a8e1`. check_shelf: "34 rules files and 151 standard blueprints, all identical", on my data dir.
- **Saves**: restore copy `notes/saves275`. Before testing, every live file matched it, apart from the four known since TEST 274 (Aoo Eighty, Four Up with its marks, open-walker-259, Pazaak Ten). At the end the same holds, and those four still carry the md5s they had before the test.
  - Every chargen in this test was cancelled, so nothing was saved to the real data dir. No real save was loaded.
- **Scratch saves**, each in its own data dir (`scratch-275a` to `-275g`, packages copied from my data dir at `af7a8e1`):

  | Dir | Character | Level | Made with | md5 |
  |---|---|---|---|---|
  | 275a | Gate Four (Rodian Soldier) | Soldier 2 | TEST 274's authored 274g copy | bbd40980 |
  | 275b | Gate Four | Soldier 3 | TEST 274's 274h copy | 716bb402 |
  | 275c | T3-58 (Astromech) | Bounty Hunter 7, holds Close Combat | TEST 274's 274b copy | 91f521ac |
  | 275d | War-Nine (Battle droid) | Bounty Hunter 7, holds Close Combat | `mksave273.py` 7, then `addfeats272.py close_combat:4`, from saves275 | ef234ea0 |
  | 275e | T3-58 | Bounty Hunter 12 | `mksave273.py` 12 | 79ce24b1 |
  | 275f | Sentry-7 (Remote) | Engineer 12 | `mksave273.py` 12 | 55a0f082 |
  | 275g | War-Nine | Bounty Hunter 12 | `mksave273.py` 12 | 06abd8f3 |

  - Eight loads, each with BEFORE and AFTER md5s in `loads.txt` and a frame at the Load click. I cancelled every level-up, and every scratch file still matches its authored copy (`scratch/`).

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Close Combat one level short | **PASS** |
| 2 | Plating Proficiency: Light | **PASS** |
| 3 | Designation refusal clearance | **PASS** at 1920. **FAIL** at 1280×720 with a two-line warning: **FINDING 2** |
| 4 | Improved Close Combat, Astromech and Battle | **PASS** |
| 5 | Skill Focus | **PASS** on the chargen grids I checked |
| 6 | Droid portraits | **PASS**, with notes |
| 7 | Hardened Chassis and Droid Upgrade 3 | **FAIL** on the pane text: **FINDING 1**. Droid Upgrade 3 **PASS** |
| 8 | Whole-screen look | **PASS** where looked; the 1280 pass is partial (see step 8) |

## FINDING 1: The Hardened Chassis panes don't carry the organics/droids line

- **Repro**: New Game, Custom, Droid, Astromech, T3-series, Engineer, through to Feats. Click Hardened Chassis, then Improved and Master Hardened Chassis in its row.
- **Hardened Chassis** reads "Prerequisites: None / Reinforced plating and shock mounting. / +2 to your death threshold." and nothing else; the pane's scroll bar runs its full height (`a-hardened`).
- **Improved** reads "Prerequisites: Hardened Chassis / Reinforced plating and shock mounting. / +4 to your death threshold." **Master** reads "Prerequisites: Improved Hardened Chassis / Reinforced plating and shock mounting. / +6 to your death threshold, and immunity to ion damage's Constitution drain." (`a-hardened-530`, `a-hardened-823`).
- **Data**: in `Shelf af7a8e1 base-rules/rules/feats.toml` the words "organics cannot take this chain, droids cannot take that one" are in `hardened_chassis`'s `note` field ("effect: The droid equivalent of Tenacity — …"), not in its description or effect, and the pane doesn't show notes.

## FINDING 2: At 1280×720 a two-line designation warning doesn't clear Random Name's border

- **Repro**: window resized to 1280×720 (`xdotool windowsize`). New Game, Custom, Droid, Assassin, HK-24, Engineer, through to Name; type "HK-4" (also "Hk 4").
- **Measure** (`strict275.py`, x 386–894, `o720-s-name-hk4`, `o720-s-name-hkspace`, zoom `o720-s-name-hk4-zoom4x`):
  - The second line's text body ends at row 359. Descender pixels (2–3 per row) run down to row 362.
  - Random Name's border starts at row 363 (its anti-aliased top, 241 teal-ish pixels across) and is solid at 364.
  - So no row between the text and the border is fully clear. Counted from the text body, there are 3 rows (360–362), and they hold the descenders.
- **The other cases pass**:

  | Size | Warning | Text body ends | Last reddish row | Border starts | Fully clear rows |
  |---|---|---|---|---|---|
  | 1920 | 2 lines ("Astro Nine", "T3-M4", "HK-4") | 539 | 542 | 546 | 3 |
  | 1920 | 3 lines ("HK-47") | 555 | 555 | 562 | 6 |
  | 1280 | 2 lines ("HK-4", "Hk 4") | 359 | 362 | 363 | **0** |
  | 1280 | 3 lines ("HK-47") | 369 | 369 | 374 | 4 |

- My first, looser measure (`gap275.py`, red above 60 and a border spanning 60% of the width) read 2 clear rows at 1280. That measure misses the faint descender row and the border's anti-aliased row, so I don't rely on it.

## 1. Close Combat one level short

- **Chargen, level 1**:
  - Rodian Soldier: Close Combat is red (border 198,52,2 unselected), pane "Prerequisites: Character Level 4" (`o-cc`, `o-cc-unsel`).
  - Battle droid Bounty Hunter: the same, red with "Character Level 4" (`b-cc`, `b-cc-unsel`).
  - Astromech: not on the grid, as its chassis bar has it (`a-cg-scan.txt`).
- **Level-up to 3** (Gate Four, 275a): Close Combat is on the grid, red, pane "Character Level 4". Add Feat stays dim (peak 66), and clicking it leaves Remaining Feats at 1 (`a2-cc`, `a2-cc-unsel`, `a2-cc-sel`, `a2-cc-addtry`).
- **Level-up to 4** (275b): takeable (teal border 28,119,96; Add Feat 136). I took it: Remaining Feats 1 → 0 (`b3-cc`, `b3-cc-sel`, `b3-cc-taken`).

## 2. Plating Proficiency: Light

- **Organic**: not on the Rodian Soldier's chargen grid (`o-cg-scan.txt`) or on Gate Four's level-up-to-3 grid (`a2-lu-scan.txt`).
- **Droids**: the chargen granted popup lists it for all four:
  - Astromech: "Droid Upgrade 1, Plating Proficiency: Light, Blaster Integration, Field Override" (`a-feats-granted`).
  - Assassin: "Droid Upgrade 1, Plating Proficiency: Light, Field Override" (`s-feats-granted`, and again at 1280 in `o720-s-feats`).
  - Remote: "Droid Upgrade 1, Plating Proficiency: Light, Blaster Integration, Field Override" (`r-feats-granted`).
  - Battle: "Droid Upgrade 1, Plating Proficiency: Light" (`b-feats-granted`).
  - On the Astromech's grid the Plating cell is lit as held (46,194,162).

## 3. The designation refusal

See FINDING 2 for the table.
- At 1920 the dialog grows with the warning (bottom 656 → 674 for two lines) and goes back to 656 when the designation is valid ("T3-61", "HK-71") (`a-name`, `a-name-invalid`, `a-name-valid`, `s-name-*`).
- At 1280 the valid "HK-71" shows no warning (`o720-s-name-valid`).

## 4. Improved Close Combat

- **T3-58, Astromech, level-up to 8, holding Close Combat** (275c): Improved Close Combat is red. Its pane reads "Prerequisites: Close Combat / Character Level 8 / Closed to Astromech". Add Feat is dim; clicking it leaves Remaining Feats at 1 (`c8-icc`, `c8-icc-addtry`).
- **War-Nine, Battle droid, level-up to 8, holding Close Combat** (275d): Improved Close Combat is takeable. Its pane reads "Close Combat / Character Level 8" with no chassis line, and Add Feat is lit at 136. I took it: Remaining Feats 1 → 0 (`d8-icc`, `d8-icc-taken`).

## 5. Skill Focus

- Red (border 198,52,2 unselected), with pane "Prerequisites: No skill can be chosen for it yet". Checked on the chargen grids of:
  - the Astromech (`a-skillfocus`, `a-sf-page`);
  - the Assassin (`s-sf`, `s-sf-unsel`);
  - the Remote (`r-sf`, `r-sf-unsel`);
  - the Rodian Soldier (`o-sf`, `o-sf-unsel`).
- Add Feat was dim on the Astromech's. Not checked: the Battle droid's grid, any level-up grid, and an Add Feat click.

## 6. Droid portraits

Checked on the chargen Portrait page (preview size by `bbox275.py`):

| Chassis | Offered | First (selected on open) | Preview |
|---|---|---|---|
| Astromech | 2 | T3-M4 | 256×256; the second (another T3 picture) 128×128 |
| Assassin | 2 | HK-47 | 256×256; the second (another HK) 128×128 |
| Remote | 2 | G0-T0 | 256×256; the second, the Remote's own face (a white training sphere), 256×256 |
| Battle | 1 | the "?" placeholder | 256×256 |

- No two chassis offer the same picture. Frames: `a-portrait`, `a-portrait2`, `s-portrait`, `s-portrait2`, `r-portrait`, `r-portrait2`, `b-portrait`.
- **Note**: the Remote opens with G0-T0 selected, not its own face; its own face is the second choice. The order reads "the Remote its own face (G0-T0 is also offered)", so I'm noting this rather than filing it. Picked, the Remote's own face carries to the hub (`r-cancel`).
- T3-58 shows T3-M4 in play and in the level-up hub (`c7-char`, `e12-char`).

## 7. Hardened Chassis and Droid Upgrade 3

- **Pane text**: FINDING 1.
- **Droid Upgrade 3**:
  - **Astromech** (T3-58, level-up to 13, 275e): it isn't in the granted popup ("Droid Upgrade 2, Plating Proficiency: Medium, Quarry, Run to Ground, No Escape"). On the grid it's red in the Droid Upgrade row's third column (Droid Upgrade 1 and 2 held), with pane "Droid Upgrade 2 / Character Level 13 / Closed to Astromech". Add Feat leaves Remaining Feats at 1 (`e13-granted`, `e13-du1`, `e13-du3`, `e13-du3-addtry`).
  - **Remote** (Sentry-7, Engineer, level-up to 13, 275f): it isn't in the granted popup ("Droid Upgrade 2, Plating Proficiency: Medium, Subverted, Turned") (`f13-granted`). An Engineer has no Feats step at 13, so I couldn't see its grid there (`f13-now`).
  - **Battle control** (War-Nine, level-up to 13, 275g): the popup grants Droid Upgrade 2, Plating Proficiency: Medium, **Droid Upgrade 3**, Plating Proficiency: Heavy, Quarry, Run to Ground (`g13-granted`).
  - Droid Upgrade 2 appears at 13 because the authored saves have the levelled events without the earlier levels' grants. That's my fixture, not filed.

## 8. Whole-screen look

- **1920×1080**:
  - Chargen for all four chassis (species, chassis, racial skill, model, class, Voice, Portrait, Background, Attributes, Skills with the unspent-points question, Feats with both popups, Attacks, Equipment, Name with the dialog) and the Rodian Soldier (through Feats).
  - Level-ups for the Soldier and both droid classes: class, hub with its popup, Feats.
  - Nothing cut off, overlapping or missing.
- **1280×720**:
  - Gate Four's level-up (275b): Character sheet, class, hub with its popup, Feats (`o720-char`, `o720-lu-*`).
  - The Assassin's chargen: Portrait, Feats with the granted popup, Attacks, Name with the dialog (`o720-s-*`).
  - Nothing cut off, overlapping or missing, apart from FINDING 2.
  - **Not done at 1280**: an organic chargen and a droid level-up. So the odd-size half covers a droid chargen and an organic level-up only.

## Odd, not filed

- **The second portrait previews at half size** for the Astromech and the Assassin (128×128 against 256×256 for the first), in the same 256 preview box. The Remote's second is full size.
- **The Remote opens on G0-T0**, not its own face (step 6).
- **Recommended on chargen Attacks**: on the Astromech, with Remaining Attacks 2, it shows "The following attack(s) have been recommended:" with an empty list (`a-rec`).
- **Saves made before this build keep the old shared face**: War-Nine (Battle droid) and Sentry-7 (Remote), both made in TEST 274, show the HK-47 picture in play and in the level-up hub (`d7-char`, `f12-char`, `g12-char`, `f13-now`). A new Battle droid gets the placeholder and a new Remote its own pictures.

## What I got wrong

- **An organic chargen started on the wrong screen.** My click to dismiss the Battle droid's granted popup landed after the popup had already closed, and my cancel didn't go through. The "organic" script then drove the still-open Battle chargen. I caught it because the scan read Droid Upgrade 1, set those frames aside in `void/`, cancelled properly with a frame at each click, and reran. Nothing in this report is read from `void/`.
- **Missed clicks on the Assassin's Attacks page.** My first cell positions were wrong and left one attack unspent; I took it by hand from the frame.
- **The first clearance measure was too loose** (FINDING 2). I replaced it with the per-row count and report that.
- **Step 8 at 1280 is partial**, and step 5 left out the Battle droid's grid and the level-up grids (see those steps).
