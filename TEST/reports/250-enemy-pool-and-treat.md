# TEST 250: The enemy pool rests, Loom's power check, the treat line

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, the load log and the dev log of every launch are in `KOTOR_RPG_MAIN_WORK/media/screens/test-250/`; names in brackets below are files there.

## Build

- **App**: main `8769dce`, a fresh clone. `gate.py --at 8769dce`: "FOR TESTER — CORE at 8769dce, 5884 tests, 0 failed".
- **Lodestar**: `ac2bf78` compiled into both the app and Loom. **Loom**: `02fc8f5`, a fresh clone.
- **Settings**: defaults at the start. **Shelf**: `9c28184`, check_shelf clean.
- **Beds**: the test221 and death save tools rerun with no errors.
- **Restore and logs**: the restore copy holds every `.sav`, plus `.marks` for dice-one and icons-185. Each load's md5s are logged before it (`loads.txt`), and each launch's dev log is kept in `devlog/`.
- Every step ran on `8769dce`.
- A (TEST 249) was filed as TEST 249 on `ac9dbd1`.

## Summary

No findings. B's restart can only be a fresh load on this bed (see B). On Death Normal the treat line is the medpac line, because that save carries medpacs (D). Loom's first Verify after a hand edit missed the edit, and "Verify again" caught it (C).

| # | Check | Result |
|---|---|---|
| B | Apprentice pool | **PASS** for the casts: Horror, Horror, Force Slow, 25 to 15 to 5 to 0, then it fights. Started again: Horror first, from Force 25 of 25. |
| C | Loom, powers | **PASS**. "the rules carry no power forse_push", Create dim; force_push is legal; Verify names a hand-written forse_push. |
| D | Treat, Death Bare | **PASS**. "brought up to 0" with Mate bleeding, and with Mate held (Death set to Easy). |
| D | Treat, Death Normal | The medpac line ("Mate 12 of 12 (was -1) · 2 left"). This save has medpacs. |
| E | Regression | **PASS**. Popup as in TEST 249; end line "Mate and Keeper fall"; the footlocker menu inside its frame; SAME17; slot 89 to 90, fight won. |

## B. The enemy pool (Power Four)

The dev log for each load reads "fight opens: seed 194523214, 0 dealt, rolling Power Four, apprentice.powers.01". Initiative: Power Four 10, Sith Apprentice 2.

Hovering the apprentice after each of its turns (`b2-hov0` to `b2-hov3`):

| After | Its line | Hover |
|---|---|---|
| (start) | | Force 25 of 25 |
| turn 1 | "Sith Apprentice — Horror at Power Four · … vs 7 · shaken" | Force 15 of 23 · exhausted from 25 |
| turn 2 | "Horror at Power Four · … Horror 2 = 13 vs 7 · shaken" | Force 5 of 21 · exhausted from 25 |
| turn 3 | "Force Slow at Power Four · … · slowed · −2 defense · −2 reflex · −2 attack" | Force 0 of 20 · exhausted from 25 |
| turn 4 | "Sith Apprentice closes 3 squares … unarmed … hit · damage 1" | |

It passes over Dark Fury and Stun Droid every turn, as the save's notes say.

**Ending the fight and starting it again.** The apprentice has 400 vitality, and the Power Yard has no exit. A fight ends only when the party is wiped or no enemy stands; the app's `over` is `partyWiped || _noEnemyUpright`. So the only end I could reach was defeat:
- I set Difficulty to Hard to speed it up. After about 20 End Turns: "YOU FALL, AND NOBODY IS LEFT STANDING. That is a total party defeat".
- The panel reads "Your entire party has been killed. … no save to go back to — this run was never saved", with "Go to Load Game List" and "Main Menu" (`b-defeat`).
- I loaded Power Four again (restored). The apprentice reads **Force 25 of 25**, and its first turns are Horror, Horror, Force Slow again (the table above is that second fight).
- Because the restart is a fresh load, this bed can't tell a pool that rests at the end of a fight from one that a reload refills. A winnable apprentice, or a yard with an exit, would show the rest itself.

## C. Loom (on a copy of Tester Powers)

Palette > creatures > custom > +: New Creature. Name "Pusher", class soldier, level 1, species Human.

- Powers "**force_push, forse_push**": the box goes red and reads "**the rules carry no power forse_push**", and Create is dim (`c9-typo2`).
- Changed to "**force_push, force_push**": no message, and Create lights (`c9-fixed2`). Create wrote `blueprints/characters/pusher.crtr` with `powers = ["force_push", "force_push"]`.
- My first try left Create dim with no word near the powers box. The form also wanted a species: "needs a species" sits under the species list, at the bottom of the form, and I hadn't scrolled down to it. With Human picked, the typo alone dims Create (above).
- **Verify on a hand-written typo**: I edited `pusher.crtr` on disk to `powers = ["force_push", "forse_push"]`.
  - Verify, pressed just after the edit: "Tester Powers · No problems found." (`c10-verify`).
  - **Verify again**: "1 problem. pusher — "pusher.crtr" lists the power "forse_push", and the rules carry no power by that id, so it would never be cast." (`c11-verify2`).
  - So a Verify run straight after an edit outside Loom may read the old file. I've noted it, not filed it.

## D. Treat

- **Death Bare, Mate bleeding** (-1, my turn, t, 1): "treat Mate — d20 8 + Medicine 0 = 8 · **brought up to 0**"; Mate is at 0 (`d-bare-bleed`).
- **Death Bare, Mate held** (a fresh load, Mate at -1, then Death set to Easy in Table Rules so the bleed stops, then t, 1): "treat Mate — d20 8 + Medicine 0 = 8 · **brought up to 0**" (`d-easy`, `d-bare-held`).
- **Death Normal, Mate bleeding** (-1): "treat Mate — d20 8 + Medicine 0 = 8 · Medpac — + base 10 + Medicine check 8 = 18 · Mate 12 of 12 (was -1) · 2 left" (`dn-bleed`).
  - Death Normal's save carries three medpacs, so treat uses one. "brought up to 0" is the line without a medpac, and it can't appear there until all three are spent. I didn't spend them, so the held state on Death Normal isn't run.

## E. Regression

- **The event popup** (Mine Two, the quartermaster): one popup on the board, with the same Item(s) Received row as TEST 249's Finding 2, which Coder is fixing (`e-pop`).
- **The end line** (Death Normal win): "Mate and Keeper fall — Blaster Pistol … -3 left …"; Mate and Keeper are each "revived at 1". That's the same as TEST 249 (`e-end1`).
- **The menu inside its frame** (Tries Hard, the destroyed footlocker, right-clicked near its bottom): it opens upward, inside its frame, with Search (Awareness) visible (`e-menu`).
- **Dice**: SAME17.
- **Regression**: Icon Nine. I loaded slot 89 (reg249) and saved it as "reg250", which took slot 90. Then a quick save mid-fight, a load of slot 90, and the win: "Icon Nine: 151 of 196", "FIGHT OVER" (`dicereg.out`).

## What I got wrong

- In C, I took Create's dimness for the powers field before I'd scrolled to the species list. The code says Create also waits for a species. I picked Human and redid the check.
