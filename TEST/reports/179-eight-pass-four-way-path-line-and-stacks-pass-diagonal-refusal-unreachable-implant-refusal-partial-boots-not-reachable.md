# TEST 179: TEST 178's checks on the newest build, plus four-way movement, the path line and stack numbers

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-179/` (MAIN_WORK `71aadd87`), one prefix per item (`i01-` … `i12-`). The step-by-step log is `TEST/reports/179-running-log.md`.

## Build

App `4a9c20c` (cf6b705 plus `tool/one_at_a_time.sh`; against cf6b705 only `README.md` and the script change). Exported with git archive to `~/kotor-tester/builds/test179` on disk, not `/tmp`. Lodestar `fffb58050d389b297fbd2522d1fac6af47f9094c`, which equals the lock and the compiled copy (`package_config.json`). Lens `ca980549c6b8064038931f5817cbeff0547c080e`, which equals the lock and the compiled copy. Loom has no entry in the app's lock. Shelf `83b5bec` (my data dir; origin is at the same commit). check_shelf is clean (31 rules files, 114 blueprints). `tool/env.sh` was sourced, and `pubspec.lock` was unchanged after the build.

The build ran through the lock. Every `dart run` of my fixture tools also went through the lock. The app was launched first through the lock (the old rule) and, after MAIN's correction, as the built bundle with a plain `&`. Fixtures are fresh. TEST 178's fixture authors were lost with `/tmp` in the reboot, so I wrote `tester_author.dart` (a JSON spec in, a save out) and `tester_dump.dart`. Copies are in the snapshot's `tool/`, and my own copies are in `~/kotor-tester/notes/fixtures/`.

## Summary: eight pass, two partial, one pass with one failed point, one not reachable

| # | Check | Result |
|---|---|---|
| 1 | Config 2 | **PASS**: Soldier and Medic (fresh chargen) take the Config 2 Short Sword off, get it offered back, and put it on again. Config 1 (Blaster Rifle / Hold Out Blaster) does the same. While the sword sits in Config 2, the Config 1 list never offers it |
| 2 | Spikes and repair | **PASS**: the Quartermaster gives 4 spikes and a part. The console opens free and reads Spikes 4 at once. "Cycle the corridor lights" spends 1, "Unseal the vault door" spends 3, and both are usable. At 0, both rows are dimmed with "— you have 0 spikes". The panel's "Repair (Repair)" spends the part |
| 3 | Turn lines | **PASS**: "switching weapons — it is Kael's turn; wait for your own", and on a droid's turn, "… it is Sentry Droid's turn; wait for your own" (pause 4000 ms) |
| 4 | Names | **PASS**: the Sith Warrior gets a "Dark Padawan Robe" in chargen and in Equip. Starting items carry their own names. "Dockworker's Treads" keeps its apostrophe everywhere. The Marksman Rifle comes off and goes back on. No "Training Blade" exists; the nearest item is "Training Lightsaber red" |
| 5 | Motivators | **PASS**: Quick Fix sells Treaded (75) and Silenced (400). "MOTIVATOR" fits on one line. Treaded gives an astromech 3 move instead of 4, and rough ground costs nothing extra. Silenced gives Stealth Bonus +2 (control without it: 0). Organic and droid refusals happen by omission (not offered), with no refusal line |
| 6 | Droid speed | **PASS**: Astromech 4, Assassin 5, Battle 5, Remote 6. The Remote crosses rough ground at no extra cost |
| 7 | Boots Defence | **NOT REACHABLE**: those four boots exist only as rows in `base-rules/rules/items.toml`. No item blueprint, store or creature carries them |
| 8 | Implants | **PARTIAL**: the three feats show their own names and description lines. The items read Cybernetic, Advanced Cybernetic and Master Cybernetic Implant. A holder of all three feats equips the Master. A character without the feat is refused, but with K2's generic line; only the side pane names the feat |
| 9 | Quick regression | **PASS**: the Auto Save row shows the companion's face. Own-turn swap goes free, then costs the Action, then is refused. Party bar faces show. Boots come off and go back on. Escape + F4 writes one quick save each time |
| 10 | Four-way movement | **PARTIAL**: 7/9/1/3 do nothing. A diagonal square takes two steps. A diagonal neighbour is hit in place and provokes when you walk away. A follower stops on the diagonal. **Not met**: no play input can produce the "diagonal step is refused" line; flanking has no code to show; an L-shaped enemy approach was not observed |
| 11 | Path line | **PASS except one point**: every square is marked teal, red or amber. The line is straight or has one rounded bend, and detours around occupied squares. Provoke lines show and go away under Disengage. The click walks the drawn path. Move-and-attack shows the ghost and "65% (needs 8+)" with reasons, then moves and strikes. Outside a fight there is no line and no attack. **FAIL**: on rough ground the label counts movement spent, not marked squares |
| 12 | Stack numbers | **PASS**: a bare teal "2" sits at the bottom right of the icon with no box. Names carry no "x2". Single items show no number |

## What needs a decision or a fix

1. **The diagonal refusal line can't be reached in play (item 10).** The line "step up, down, left or right — a diagonal square takes two steps" is at `play_screen.dart:7455`. Its only diagonal caller is `stepForTest` (`test/path_line_test.dart:319`). Keys bind only the four arrows (`play_screen.dart:19779-19786`), and the click walker sends orthogonal legs. Pressing a numpad diagonal does nothing and shows nothing. KP_6 doesn't move either, so the numpad isn't bound at all. If a player is meant to see the line, numpad 7/9/1/3 need binding to `_step(±1, ±1)`.
2. **The label count on rough ground (item 11).** From (6,2) to rough (5,1), two squares are marked and the label reads "3 squares · 2 left / rough ground costs extra" (`i11-rough-count-and-provoke.png`). Either the count should be squares or the order's wording should say movement.
3. **Flanking (item 10).** Kael and I stood diagonally opposite across a droid, and neither the hit-chance reasons nor the attack line had a flanking term (`i10-diagonal-hover-no-flank-term.png`). "flank" appears in `lib` only in comments (`play_screen.dart:7452`, `fight.dart:1154`). It can't be checked until it exists.
4. **The implant refusal line (item 8)** is still K2's generic "You cannot equip this item. You don't have the prerequisites. Please see the item description." (`i08d-refusal-no-feat.png`). The side pane names the feat ("Feats Required: Advanced Cybernetic Implantation"). This is the same result as TEST 178.
5. **L-shaped approaches (item 10)**: not observed. In two fights every droid moved in a straight run and stopped on a diagonal to its target ((9,2)→(5,2), (5,2)→(4,2), (5,3)→(7,3)). My bed didn't force an L. Kael is MANUAL, so a companion's approach wasn't seen either.
6. **Boots Defence (item 7)**: blocked until one of Sith Trooper Greaves, Mandalorian Battle Greaves, Krath War Boots or Vanguard Assault Boots gets a blueprint and a source. Note the first two ship as "Greaves", not boots.

## Notes (not failures)

- **Stale move counter**: at the start of a turn the legend read "5 → 3 move", and later "2 → 0", with the pointer off the board, while the real allowance was 5 ("4 squares · 1 left"). It looks like the last hover's preview survives the click and the turn change (`i11-stale-move-counter.png`).
- **A click just outside the grid walks**: a click at x 560 (the grid starts at 572) after the panel closed walked me to (0,3) straight through both noticed mine squares. Both were sprung, and HP went 11 → 8 (`i02k-click-outside-walked-mines.png`). After that the centre line read "Lock Ninety: 11 of 11" while the party bar read 8 of 11.
- Down from (6,0) put my token **on** the console's square (6,1) with no message.
- The dimmed panel reply is cut off at "— you have 0 p…". The panel header still reads "OUTPUT 0%" after the repair.
- The store's row for an organic buying a Treaded Motivator says "In Inventory 1 · replaces Dockworker's Treads", though an organic can't wear it.
- The move-and-attack tooltip covers most of the ghost figure (`i11-move-attack-hover.png`).
- Equip's slot label "Silenced Motivato…" is cut. No icon is drawn for the Marksman Rifle, the Dockworker's Treads, the motivators, the implants or the implant feats.
- In Equip, Switch Weapons on another's turn shows its refusal only on the play status line, after Close.
- The Auto Save row lists Kael's face first and the leader second, and its time equals the Quick Save's (23:38:55).
- The Remote's legend shows two reaction stars.
- 178's Powers clicks no longer hit two pickable rows in chargen; I picked by hand (my script, not the app).

## Corrections to my own earlier messages

- **TEST 178 was not lost.** I told MAIN that the run was lost and that nothing had been written down. That was wrong: `TEST/reports/178-…md` was committed at 18:07, before the 18:52 reboot, and `TESTER-STATE.md` records it. I didn't check HANDOFF before answering. MAIN retired 178 on my word; its results stand as filed, and 179 repeats them on the newer build anyway.
- **I deadlocked on the lock** by launching the app through it and then queueing a `dart run` behind Coder's build. MAIN caught it. I closed the app (nothing was lost) and now launch the bundle outside the lock.
- My first chassis loop ended the astromech's own turns, because "Kael is waiting on you" stays on the status line into the player's turn. The droids took it to "-14 of 18". I fixed the loop to read the turn-order ▶ (`run/turn.py`). The speed reading is unaffected, since the legend shows the player's allowance.

## Fixtures and beds (my data dir only)

- `packages/tester-rough` (new, local, not on Shelf): Rough Field, 12×5, with rough ground in column 2 and at (5–6, 0–1), Kael as henchman, and sentry droids at (9,2) and (5,3).
- Chargen: Sol Ninety, Med Ninety, Mark Ninety, Sith Ninety (Store Bed), Lock Ninety (Locked and Trapped), Rough Ninety and Rough Two (Tester Rough).
- Authored: `bolt-ninety`, `c79-astromech/-assassin/-battle/-remote/-tread`, `ivy-ninety`, `ivy-none` (specs in `~/kotor-tester/notes/fixtures/specs/`).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
