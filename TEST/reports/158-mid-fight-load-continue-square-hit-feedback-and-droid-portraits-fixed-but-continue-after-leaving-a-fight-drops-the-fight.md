# TEST 158

Written for: Main and Coder. Re-check of TEST 157's faults against PT-2736 (app a845f96). Screenshots and analysis: `HANDOFF/BUILD/screens/test-158/` (28 images, two 60 fps takes as MP4, per-attack tables, the analysis scripts). Real game on Xvfb `:2`. First report on the new OS (Ubuntu 24.04, user `aidanpscott`); every fixture rebuilt from TESTER-STATE.

## Build

App `a845f96a10230f065cad6b8d617fea56b733e7d9` (`git archive a845f96` into `/tmp/test158-build`, `flutter build linux --debug`, 11 s, no `flutter create`; `pubspec.lock` unchanged by the build). Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = the lock = the pub-cache checkout. Lens `2bad745`, Shelf `8fa2475`, MAIN_WORK `34984a07`, HANDOFF `9776672` at start. `check_shelf` clean (30 rules files, 105 blueprints). Toolchain: Flutter 3.47.2 from `~/spike/flutter` on PATH only, with the system clang 18.1.3 / cmake 3.28.3 / ninja / libgtk-3-dev (installed by the owner 2026-10-10). **`tool/env.sh` cannot be used on this OS**: it puts `~/spike/prefix` (its own glibc) on `LD_LIBRARY_PATH` and every binary aborts with "stack smashing detected"; without it the prefix's cmake cannot find `librhash`. App and Xvfb stopped by PID.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Mid-fight load restores HP, moves, square, turn | **PASS** (bookmark twice, quick save once); clicks during a load do nothing |
| 2 | Continue after a bookmark load keeps the square | **PASS** (TEST 157's repro, and load → walk → leave → Continue) |
| 2b | Continue after leaving **mid-fight** resumes the fight | **FAIL**: right square and HP, but the fight is gone; bumping the enemy starts a new fight with new initiative |
| 3 | Hit feedback, 60 fps | **PASS**: flash on **26 of 26** hits on the HP-change frame (13 ON, 13 OFF); number on 13 of 13 ON hits, same frame; "miss" on 14 of 14 ON misses; nothing over the token with Floating Numbers OFF. Flash is ~4× longer than the parity table and stepped (observation) |
| 4 | One outline on the Load list | **PASS** (60 fps: no frame with two lit rows) |
| 5 | Droid portraits, library text, Saving picture, brightness default | Droid portraits **PASS**; card text **PASS** except **Tester Strongroom's new description is Visual Pass's** (wrong content); Saving picture shows 17 frames (Coder: 14); brightness default 0.57 PASS |

## 1. Mid-fight load — PASS

Fixture: `onjo-proof` (my copy of `author_pt2721_equip_save.dart` pointed at `tester-save-bed`, CON 18, DEX 8) against Dressa ("Draw your blade.").

- **Bookmark.** State S, saved as MID: Onjo on (4,2), 4 moves, action available, 12/12, Dressa 20/20, round 1, Onjo's turn (`t1a`). Played on to state T: (6,2), 9/12, round 2, 5 moves (`t1b`). Loading MID gives exactly S, with the line *"the fight resumes — round 1, Onjo Proof's turn"* (`t1c`). Done twice, same result.
- **Quick save.** F4 at (4,4), 2 moves (`t1i`); ended the turn: Dressa missed, round 2, 5 moves (`t1j`); F5: (4,4), 2 moves, round 1, 12/12 (`t1k`).
- **Clicks during a load (Coder's explanation of the sign-off video).** 60 fps capture, times from the Load click (≈1.17 s in the clip):

| Time after Load click | Screen |
|---|---|
| 0 → 0.70 s | the Load list, unchanged (`t1d`) |
| 0.70 → 0.88 s (11–12 frames) | the Loading picture (`t1e`) |
| 0.88 → 2.05 s (≈69 frames) | play shell with a **black, empty board**, party panel filling in (`t1f`) |
| 2.05 s | board drawn |

  25 clicks on board tile (4,4), 0.13 s apart, from 0.5 s to ≈3.5 s after the Load click. On the first frame with the board drawn Onjo is still on (4,2) (`t1g`); he walks to (4,4) only after the board had been visible ≥ 0.23 s (`t1h`), i.e. from a click on a shown board. **No click during the picture or the black board moved him, and none was queued.** Note: the Loading picture covers only 0.18 s of the ≈2 s load; the rest is the unchanged Load list (0.7 s) and a black board (1.2 s). Clicks there did nothing, so this is cosmetic, but it is not "covers every load from the first frame".

## 2. Continue after a bookmark load — PASS

Five-party game (rebuilt: `author_tester_visual_save.dart`, played once so the two companions join, then `author_five_party_fixture.dart tester-visual-4`).

- **TEST 157's repro:** walk to (2,3), Save REGR (`v01-hall · 2, 3`), walk to (6,0), Load REGR (back on (2,3), `t2a`), Options → Graphics → keys → Close, Exit Game → OK → Continue: party on **(2,3)**, same arrangement (`t2b`). `autosave.world.json`: `"at":[2,3]`, `logLen` 46.
- **Discriminating version** (the bookmark square and the left square differ): Load REGR, walk to (8,3) (`t2c`), Exit → Continue: **(8,3)**, every companion where it stood (`t2d`); autosave `"at":[8,3]`, `logLen` 47. Neither the arrival square nor the bookmark's (2,3).

## 2b. Continue after leaving mid-fight — FAIL

Coder's b8f87ff says Continue "now resumes the fight it left".

Smallest repro (`tester-save-bed`, any character):
1. Talk to Dressa, "Draw your blade." Fight starts (Dressa initiative 7, Onjo 1).
2. Take a step (4 moves left); optional F4.
3. Options → Exit Game → OK → package menu → Continue.

Expected: the fight, Onjo's turn, round 1, the moves left. Got: Onjo on the **right square** (4,4) with the right HP, but **no fight** (no turn order, no move/action HUD), and he walks freely (`t2e`). Walking into Dressa then starts a **new** fight with **new initiative, Onjo 18 / Dressa 15** (`t2f`), so this is not the saved fight resuming late. The autosave written at Exit has the fight's data (`hostile: [merchant.bed.02]`, a `combatants` block with initiative 1 and vitality 12/12) but no round/turn/budget key. **Likely cause, not shown:** Continue rebuilds the area and hostility from the autosave but never re-enters the encounter.

## 3. Hit feedback at 60 fps — PASS

Fixture: `onjo-hp` (same tool, CON 200 → 103 HP, the way Coder's "Onjo Proof (103 HP)" was made; the save is `[Modded]`), against unarmed Dressa. Each take is 140 s at 60 fps (x11grab, qp 12, yuv444p), one *space* every 5 s = one Dressa attack; the pointer parked off the board. Per-frame detection (scripts in `analysis/`): HP-card text change, red excess (R−G) in strips along the board panel's top, right and bottom edges, red pixels and white pixels in a full-resolution crop above Onjo's token. Each table row was checked against the log line; two detector oddities in take A (a log transient at 6790, a repeated identical log line at turn 20) were resolved by looking at the frames.

| | Attacks | Hits | Edge flash on hit | Flash frame vs HP change | Number | "miss" |
|---|---|---|---|---|---|---|
| Take A, Floating Numbers ON | 27 | 13 (103→77) | **13 / 13** | +0 on all 13 | **13 / 13**, +0 | **14 / 14** misses |
| Take B, Floating Numbers OFF (`settings.json` `floatingNumbers:false`) | 27 | 13 (77→47) | **13 / 13** | +0 on all 13 | none | none (log still says "— miss") |

- No flash on any miss; no flash without an HP change.
- Number stays 33–57 frames; "miss" 36–55 frames.
- **Flash shape (observation, not a regression):** the bottom band's red excess steps 29 → **42** (at +14 frames) → 35 → 24 → 12 → 0, each step ≈14 frames, gone at 53–78 frames (0.9–1.3 s); top +12, right +9.4. The parity doc says "~+55 red along the bottom… up in ~3 frames, gone in ~8 (~0.27 s)". Ours is ~4× longer, in five coarse steps rather than a ramp. Coder already notes it is not tuned against K2.
- Capture quality: take A had 30 gaps > 25 ms (max 116 ms), take B 38 (max 67 ms); all hits still show +0, so no hit fell in a gap.
- `t3a` (ON hit frame: flash, "-3", HP 100 of 103, log "hit", all frame 456), `t3b` (number crop), `t3c` (ON miss), `t3d` (OFF hit: flash, no number), `t3e` (three OFF misses: nothing over the token). Tables: `analysis/table-hfA.txt`, `table-hfB.txt`; video: `analysis/hfA-60fps.mp4`, `hfB-60fps.mp4` (re-encoded crf 28 for size; the analysis ran on the lossless capture).

## 4. One outline on the Load list — PASS

Tee Three's game with Auto Save and Quick Save; Options → Load Game clicked so the pointer rests on the Quick Save row as the list opens; 60 fps capture of the opening. From the list's first frame only Auto Save is lit, through 2.4 s; no frame lights both (`t4a`). The pointer resting (not moving) on row 2 does not select it. Earlier, with the pointer moved onto a row, only the hovered row was lit (one outline, PT-2734's hover selection).

## 5. Smaller items

- **Droid portraits — PASS.** Tee Three (`author_droid_save.dart` + a copy that adds seven carried items): the Load row (`t5a`) and the Options footer (`t5b`) show an astromech portrait. TEST 157: human face and a flat teal box.
- **Library cards — PASS except one.** All 22 cards read (`t5c`, `t5d`): no PT or TEST numbers, no "baseitem", no backticks, no item ids, no "§". Droid Shield Bed reads *"One merchant selling a droid-only shield and an ordinary forearm shield. Play it once as a droid and once as a living character…"*. **FAIL: Tester Strongroom's new summary** (Shelf 8fa2475) is *"A strongroom and a vault: a hall with rows of cover, two allies (a Jedi Consular and a Soldier) and one enemy Soldier."* That is Visual Pass's content (`tester-visual/package.toml`: Guardian + Grunt henchmen, one hostile). The strongroom actually holds a locked footlocker (20), a locked console (15), a crate (30) and a guard droid; the vault is empty. No cover rows, no allies, no Soldier.
- **Saving picture on a named save:** shown for **17 frames (0.283 s)** in one 60 fps capture with no dropped frames (`t5e`). Coder measured K2's as 14 (0.233 s). One sample.
- **Brightness default:** `settings.json` reads `"brightness":0.57` on a fresh data dir; the Graphics slider sits just past the middle.
- **Auto Save pinned first:** yes, in every Load list I opened.

## Seen, not in the order

- **Conversation header and combat log use the placement tag, not the name.** Talking to Dressa shows **MERCHANT.BED.02** as the speaker, and every combat log line says `merchant.bed.02: unarmed · rolled …`, while the party panel says "Dressa". My fixture copies store-bed's blueprint (`name = "Dressa"`), so the name is authored. Not checked on a Shelf package.
- **Options menu shows two lit rows** while hovering: Save Game (the default selection) stays outlined and the hovered row is outlined too. Same pattern TEST 157 reported on the Load list, now only on the Options menu. Not compared with K2.
- **Graphics → Close once dropped me into play** (my next "Exit Game" click walked the leader); a later re-check returned to the Options menu correctly. Not reproduced; not filed.
- **The first click on a menu row after Escape was ignored once** (Graphics did not open; a second click did). One occurrence.

## Fixtures I made (my data dir, none on Shelf)

- `packages/tester-save-bed`, rebuilt: 12×8 "Save Bed", arrival "in" (1,1), a door that stays at (6,1) (a connection with no `to`), Dressa (store-bed's blueprint, unarmed, 20 HP) at (3,3) with "Draw your blade." → `encounter.began` and "Just looking", the endar-spire Sith Trooper (+ its doctrine and dialogue) at (9,5). No quest reply this time. The library flags it with "2 problems" (not read; it plays).
- Saves: `onjo-bed` (CON 10), `onjo-proof` (CON 18, DEX 8, 3 medpacs), `onjo-hp` (CON 200, DEX 8), from `tool/tester_author_onjo.dart` (a sed copy of `author_pt2721_equip_save.dart`: package → `tester-save-bed`, area → `a01-bed`). `tester-visual-4` + `five-party`. `tee-three` with seven carried items (`tool/tester_author_droid.dart`). The two tool copies live only in the snapshot.

## What I did not check

The trooper in the bed; Hide Unequippable again; K2's own footer with a party; the medpac and XP pop-ups (Coder's open items); the 60 fps count for other attackers (only Dressa unarmed, 1d3); hits on companions; a load from the main menu's Load Game mid-fight (all loads here were in-game).

Skills used: `verification-before-completion` (every PASS is a frame time, a settings.json reading or an autosave field, and the hit counts are reconciled with the log line by line), `diagnosing-bugs` (two-step repro for the Continue fight loss, with the new-initiative control; the load timeline split into its four phases by frame), `research` (Coder's sign-off README and the parity numbers first), `writing-for-agents`. `handoff`: `TESTER-STATE.md` rewritten for the new OS.
