# Tester fixtures, handed to Coder for Shelf

Each folder is a complete shelf package (copy the folder into `Shelf/` as-is). I authored all three on
2026-09-29 and committed none of them anywhere but here.

**Validation:** every package was opened with Lodestar 496d5e7's own `open()` and `validatePackage()`, and
had no faults. Dialogues passed `openConversation()` and stores passed `openStore()`.
- The validator was mutation-checked: a short map row and a missing blueprint were each reported.
- It was run without the base-rules inputs (`weaponSections`, `startingWeapons`, reserved designations,
  the droid set), so those four checks did not run here.

| package | status | what it's for |
|---|---|---|
| `tester-xp-bed` | **Played live** (TEST 142 §4) | One henchman (`mate`) and one level-9, `challenge = 9` enemy with 1 vitality. A single kill pays every party member 3000 XP. This is the fixture for PT-2708 items 1–2. `challenge` is what XP is priced from; without it the kill pays nothing. |
| `tester-purse` | **Re-authored from TEST 133; not yet played** | The PT-2566/2568 payment-gate bed: merchant Vess, with `browse`, a 400 gate (the control), a 600 gate (the reading) and `leave`. **Not reproducible from the package alone:** TEST 133's character (Purser: 500 credits, two vibroblades, level 4) came from `mk131.py`, which died with the PC. Chargen gives 100 credits and no vibroblades, and packages can't ship a premade (`premadeCount: 0`). The bed needs a save authored the `tool/author_*_save.dart` way before it discriminates. |
| `tester-visual` ("0 AAA Visual Pass") | **Reconstructed from TEST 140/141; partly guessed** | Two auto-joining henchmen (Guardian, Jedi Consular 6; Grunt, Soldier 4), one enemy Soldier, a cover row, and the `guard-grunt` doctrine. **Every unrecorded value is marked `# RECONSTRUCTED`** (see below). The player comes from the app's own `tool/author_tester_visual_save.dart`, which still exists in `KOTOR-RPG-APP`. |

**What `tester-visual` could not recover:**
- the arrival square and name;
- the exact cover and wall squares;
- the placement squares;
- Guardian's and Hostile's ability scores;
- Hostile's level and challenge;
- the vitality dice.

The id, name, 12×4 size, character classes and levels, Grunt's abilities, placement tags and the doctrine
file are as recorded.

## Added at cloud hand-back (2026-09-29)

| package | status | what it's for |
|---|---|---|
| `tester-xp-bed-arena` | **Played live** (TEST 144 §§2–4) | `tester-xp-bed` plus a door at [5,1] into `a02-arena`, which holds one **Sparring Partner** (Soldier 1, `challenge = 1`, vitality 60, unarmed, Dex 3). The first kill in `a01-room` levels the party; the arena then gives a fight that lasts several rounds. That's what checking a companion's level **in combat**, dual-wield −4, the in-combat Equip refusal and Switch Weapons' action cost needs. Its own id, so it can sit on the Shelf beside `tester-xp-bed`. `a01-room` also gains a `back` arrival at [4,1] for the return door. Validated clean with Lodestar 7b6c97f `validatePackage`. |
