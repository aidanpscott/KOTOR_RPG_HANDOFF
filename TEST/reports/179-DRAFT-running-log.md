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
