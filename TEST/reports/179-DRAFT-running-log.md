# TEST 179 running log (draft, text only)

Started 2026-10-13 22:30 EDT. Tester, Xvfb :2, own data dir (~/.local/share/tester-data), no K2, no BG3.

## Build
- App 4a9c20c (cf6b705 + tool/one_at_a_time.sh; diff vs cf6b705 = README.md + tool/one_at_a_time.sh only), git archive to ~/kotor-tester/builds/test179 (on disk, not /tmp).
- Lodestar fffb58050d389b297fbd2522d1fac6af47f9094c = lock = compiled (package_config.json).
- Lens ca980549c6b8064038931f5817cbeff0547c080e = lock = compiled.
- Loom: no entry in the app's lock.
- Shelf 83b5bec (data dir; origin HEAD is also 83b5bec). check_shelf clean: 31 rules files, 114 blueprints.
- tool/env.sh sourced. Build through tool/one_at_a_time.sh: 257 s incl. lock wait. pubspec.lock unchanged after build.
- App launches through the lock (run/launch.sh wraps it; lock held while the app runs). First launch waited on Coder's compile.
- MAIN_WORK 2ea6c37 at start; HANDOFF ee47a27 at start.
- Fixtures: fresh (TEST 178's fixture authors were in /tmp and were lost in the reboot).

## Items

### Setup note (22:58): self-deadlock on the lock, cleared
- I launched the app through the lock (old rule), then queued tester_dump.dart behind it: the app held the lock, Coder's build waited on the app, my dump waited on Coder. MAIN flagged it.
- Fix: closed my app (PID 40291). Nothing unsaved was lost; the app was on the library screen only.
- NEW RULE (MAIN): the lock covers compiling only (flutter build/test, big dart analyze, dart run on tool scripts). The built bundle is launched with plain & outside the lock. Never flutter run.
- Local bed made: packages/tester-rough (my data dir only): Rough Field 12x5, ':' rough column 2 and block (5-6, 0-1), Kael henchman, sentry droids at (9,2) and (5,3). For rough ground (items 5, 6) and the path line (11).
- Fixture author: ~/kotor-tester/notes/fixtures/tester_author.dart (JSON spec -> save), copied into the build's tool/.

### Item 1: Config 2 (in progress)
- Fixture: Sol Ninety, fresh chargen Soldier in Store Bed (run/cgrun.sh; Standard Gear: Blaster Rifle C1, Short Sword C2, clothing, Dockworker's Treads).
- Soldier: Equip > Config 2 Short Sword -> None: slot empty; reopened: "Short Sword" offered; picked: back on. Config 1 Blaster Rifle -> None: 2-4 (unarmed); reopened: "Blaster Rifle" offered; back on, 2-13 +2. While the sword sits in Config 2, the Config 1 list offers None + Blaster Rifle only (no sword). PASS. Shots: i01-sol/lists.png, i01-sol/slots.png (+ per-step a-d).
- Medic (Med Ninety, fresh chargen, Store Bed): Config 2 Short Sword off/offered/on; Config 1 Hold Out Blaster off (2-4) / offered / on (2-5 +1); Config 1 list never offers the sword. PASS. Shots: i01-med/lists.png, i01-med/slots.png.
- **Item 1: PASS.**

### Item 4: Names
- Fixtures: fresh chargen in Store Bed: Mark Ninety (Marksman), Sith Ninety (Sith Warrior), plus Sol Ninety's chargen screen.
- Sith Warrior robe: chargen Standard Gear lists "Dark Padawan Robe" (i04-sith-chargen.png); in play, Equip > Body reads "Dark Padawan Robe (Equipped)" (i04-sith-equip.png). Not "Robe 1". PASS.
- Starting items own names: Soldier "clothing, Blaster Rifle, Short Sword, Adrenal Strength, 2 Frag Grenades, 2 medpacs, Dockworker's Treads" (i04-sol-chargen.png); Marksman "Marksman Rifle, Hold Out Blaster, Adrenal Stamina, Dockworker's Treads" (i04-mrk-chargen.png). No "Training Blade" item exists; the nearest is the Sith Warrior's "Training Lightsaber red" (note: colour word lower-case and after the name). PASS.
- Apostrophes: "Dockworker's Treads" on all three chargen screens; "Dockwor ker's Tr..." slot label in Equip. None lost. PASS.
- Marksman Rifle: Config 1 off (2-4) / offered / back on (2-11 +2) (i04-mrk/lists.png, slots.png). PASS. Note: the rifle still draws no icon (empty cell), as in TEST 178.
- Powers screen note: cgrun.sh's power clicks no longer hit two pickable rows; I picked Fear + Force Push by hand. Not an app fault.
- **Item 4: PASS** (notes: "Training Lightsaber red" casing; Marksman Rifle no icon).

### Item 2: Spikes and repair (Locked and Trapped)
- Fixture: Lock Ninety, fresh chargen Soldier (Slicing 1, Repair 1 on the console card).
- Quartermaster: "Spikes and a repair part" -> "Four spikes and a part. That is all I can spare." (i02a-quartermaster.png)
- Console (right-click > Slice (Slicing)): opens free and reads Spikes 4 and Parts 1 at once, no reload; both "[Slicing] Unseal the vault door. (3 spikes)" and "[Slicing] Cycle the corridor lights. (1 spike)" offered (i02b-console-open.png). Lights: "— 1 spike spent" (i02c). Reopened free: Spikes 3, both offered (i02d). Unseal: "— 3 spikes spent" (i02e). Reopened: Spikes 0, both dimmed "— you have 0 spikes" (i02f). Sequence: i02-console-sequence.png. PASS.
- Damaged Power Panel (6,3): right-click shows "Examine (Science)" and "Repair (Repair)" (i02g). Repair opens "POWER COUPLING FAULT — OUTPUT 0%" with "1 [Repair] Reroute the power coupling. (1 part)" (i02h). Picked: "— 1 part spent" (i02i). Reopened: Parts 0, reply dimmed "— you have 0 p..." (i02l). PASS.
- **Item 2: PASS.**
- Notes (not failures): (a) the dimmed panel reply is cut off: "— you have 0 p..."; (b) the panel header still reads "OUTPUT 0%" after the repair; (c) Down from (6,0) put my token ON the console's square (6,1) with no message (con1); (d) a click just left of the grid edge (x 560) walked me to (0,3) straight through both noticed mine squares (2,1)/(2,2): both sprung, HP 11 -> 8 (i02k-click-outside-walked-mines.png); (e) after that the centre line reads "Lock Ninety: 11 of 11" while the party bar reads 8 of 11 (i02k, i02l).
- Console exit: Escape opens Options (Close returns to the console); a click outside the console closes it.

### Item 10 (in progress) and 11 out-of-fight parts. Bed: tester-rough, Rough Ninety (fresh chargen Soldier) + Kael. App relaunched with KOTOR_ENEMY_TURN_PAUSE_MS=4000.
- Numpad out of a fight: 7/9/1/3 (Num Lock off: KP_Home/Prior/End/Next; Num Lock on: KP_7/9/1/3) do nothing: no move, no line (i10a, i10b). Control: Right arrow moves one square and Kael follows (i10c). PASS for "7/9/1/3 do nothing".
- "a diagonal step is refused with its line": NOT SEEN IN PLAY. The line exists ("step up, down, left or right — a diagonal square takes two steps", play_screen.dart:7455) but no play input can send a diagonal step: keys bind only the four arrows (play_screen.dart:19779-19786), the click walker sends orthogonal legs (_walkRoute), and the only diagonal caller is stepForTest (test/path_line_test.dart:319). Numpad keys are silent. Also: KP_6 does not move either (numpad not bound at all).
- 11, outside a fight: hover over a square and over the far droid draws no path line (i11-out-of-fight-no-line.png). Click on the droid is not an attack: "walk into them to act — choose an action first to aim at somebody" (i11-out-of-fight-click-creature.png). PASS.

### Item 3: Turn lines (KOTOR_ENEMY_TURN_PAUSE_MS=4000, confirmed in the app's environ)
- Bed: tester-rough fight (Rough Ninety bumped the droid at (5,3)); order Sentry Droid 19, Sentry Droid 7, Rough Ninety 5, Kael 3.
- Kael's turn (i03a): Equip > Switch Weapons: nothing changes; status line "switching weapons — it is Kael's turn; wait for your own" (i03b). PASS.
- Sentry Droid's turn: Equip > Switch Weapons inside the droid's turn; status line "switching weapons — it is Sentry Droid's turn; wait for your own" (i03c, top half; the bottom half 0.6 s later shows the next droid acting). PASS.
- Note: the line is on the play status line only; inside Equip the press shows nothing (the line is visible after Close).
- **Item 3: PASS.**
