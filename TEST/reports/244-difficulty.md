# TEST 244: Difficulty (hash 1)

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the load log are in `KOTOR_RPG_MAIN_WORK/media/screens/test-244/`; names in brackets below are files there.

## First: TEST 243's slow first launch, for Coder

- **The saves folder at the time**: 537 entries (`.sav` files plus `.marks` folders), 7.1 MB, measured while the scan was still running. I didn't count the `.sav` files alone then. Today, after the same full regeneration, it is 538 entries, 341 of them `.sav`, 7.2 MB.
- **What I had just done**: the build and all 25 save tools had finished before I launched. It was the first launch after regenerating every save.
- **What else was running**: I didn't look at the process list then, so I don't know. The Steam client and VS Code's Dart tools (language server, tooling daemon, devtools) have been up for days, so they were running.
- **The app at the time**: about 135% CPU and 670 MB of memory, still on "reading saves…" after three and a half minutes.
- **Today's first launch after regenerating**: the scan itself took about 2 s once the card was open. Finding the card in the library took about 3 minutes, though, so the cost may have moved to the library screen.
  - Sitting on the package menu, the app ran at 220–360% CPU for at least a minute (`top`), with nothing happening on screen.
  - Every launch of this build took 3 to 4 minutes from start to the open card.

## Build

- **App**: main `4fa5599`, a fresh worktree. `gate.py --at 4fa5599`: "FOR TESTER — CORE at 4fa5599, 5799 tests, 0 failed".
- **Lodestar**: `aaacdbb` compiled, as the order says.
- **Settings**: defaults at the start. **Shelf**: `7f02f8f`, check_shelf clean.
- **Beds**: all save tools ran with no errors.
- Every step ran on `4fa5599`, including TEST 242's and 243's.
- **Loads**: each load is in `loads.txt`, with the file and md5, or the bookmark's `.mark` and slot.

## Summary: no findings; step 7 has no bed

| # | Check | Result |
|---|---|---|
| 1 | Package Options | **PASS**. The second entry is "Table Rules"; "Difficulty: Normal" on top with K2's text; cycled to Hard. |
| 2 | New Game, then in play | **PASS**. In-game Table Rules reads "Difficulty: Hard"; another package reads its own (Normal). |
| 3 | Damage you take | **PASS**. Normal 19 → 19; Easy 3 → 1 (twice), 7 → 3; Hard 6 → 9 (twice), 5 → 7. |
| 4 | Your blows | **PASS**. Full on Hard (6), Easy (10) and Normal (4). |
| 5 | Changed mid-fight | **PASS**. The next enemy blow used the new setting every time. |
| 6 | Bookmark and load | **PASS**. Hard kept after loading in a fresh app, and the next blow is scaled. |
| 7 | Grenade or damage power | **NOT RUN**. No shelf package gives an enemy a grenade or a damaging power. |
| 8 | Regression, TEST 242 and 243 | **PASS**. SAME17; slot 82 to 83, fight won; every 242 and 243 step as before. |

## 1: Package menu > Options

- On the Tester Watch card, Options lists **Table Rules** second, with the text "The table's rules: the difficulty, and the reactions" (`s1-options`).
- Inside, the top row is **"Difficulty: Normal"**, with K2's text: "This option changes the difficulty level of combat. The game is designed to be played using the NORMAL setting. Adjusting the setting will have a significant effect on combat and damage from enemy attacks." Below it are the six reaction rows (`s1-table`).
- `+` gives **"Difficulty: Hard"** (`s1-hard`). settings.json then reads `"newGameDifficulty":{"tester-watch":"hard"}`: it's stored per package, for new games.
- The page's title bar still reads "Gameplay Options", here and in-game. I've noted it, not filed it.

## 2: New Game, then in play

- New Game on Tester Watch, Custom Character: a Human Soldier, Standard Gear, aptitude Mysticism, named "Diff Hard". Then Play (`n20`, `n21-play`).
- In play, the in-game Options lists **Table Rules** (`s2-menu`), which reads **"Difficulty: Hard"** (`s2-table`).
- **Another package**: Tester Parry's package-menu Table Rules reads **"Difficulty: Normal"** while Tester Watch's is Hard (`s2-other`).
- **An authored save reads Normal**: watch-one.sav, which has no difficulty of its own, loads as "Difficulty: Normal" (`e0-table`), even with Tester Watch's new-game setting on Hard.

## 3 and 5: The damage you take

The status box only keeps the round's last line, so each check is the last actor's "damage N" in the box against its own line in the log. Watch One (124 vitality), with the setting changed in-game mid-fight between rounds:

| Setting | Box (roll) | Log | Expected |
|---|---|---|---|
| Normal | "Runner … damage 19 — 2d10 7+10 + Strength 1x2 x 2 critical" | "Runner damages Watch One for 19 damage" | 19 |
| Easy (changed mid-fight) | "damage 3 — 1d10 2 + Strength 1 · 81 left" | "Runner damages Watch One for 1 damage" | 1 |
| Easy | "damage 3 … 80 left" | "… for 1 damage" | 1 |
| Hard (changed mid-fight) | "damage 6 — 1d10 5 + Strength 1" | "… for 9 damage" | 9 |
| Hard | "damage 5 — 1d10 4 + Strength 1" | "… for 7 damage" | 7 |
| Hard | "damage 6 — 1d10 5 + Strength 1" | "… for 9 damage" | 9 |
| Easy (after the bookmark load, changed) | "damage 7 — 1d10 6 + Strength 1 · 3 left" | "Runner damages Watch One for 3 damage" | 3 |

(`d1-box` to `d7-box`, `d2-log`, `d4-log`, `d7-log`, `p3-box`, `p3-log`.) In each case the first enemy blow after a change used the new setting.

Diff Hard (12 vitality, Hard from the New Game): the Watcher's "damage 9 — 1d8 6 + Dexterity 3 · -1 left" took her from 12 to −1, which is floor(9 × 1.5) = 13. That fits Hard, but I couldn't open the log from the defeat screen to rule out an earlier hit (`h1-defeat`).

## 4: Your blows at enemies

Watch One shooting the Watcher. In each, the box shows "damage N … X left", and the log shows "Watch One damages Watcher for N damage":
- **Hard**: "damage 6 — 1d8 4 + Dexterity 2 · 394 left" (from 400) (`p1-shot`).
- **Easy**: "damage 10 — 1d8 8 + Dexterity 2 · 384 left" (from 394) (`p4-easy`).
- **Normal**: "damage 4 — 1d8 2 + Dexterity 2 · 396 left" (from 400) (`p5-normal`).

## 6: Bookmark and load

- On Hard, after her shot, I saved slot 83, "diff244" (`watch-one.marks/000083.mark`).
- I stopped the app, relaunched it, and loaded slot 83 (`b1-list`). Table Rules reads **"Difficulty: Hard"** (`b2-table`).
- **The next blow**: the Watcher's "damage 11 — 1d8 8 + Dexterity 3 · -5 left" took her from 11 to −5, which is 11 − floor(11 × 1.5) (`b3-box`).

## 7: An enemy grenade or damage power — not run

- I searched every package on the shelf (7f02f8f) for an enemy with a grenade or a damaging power. The only enemy powers list anywhere is `["dark_fury", "stun_droid", "horror", "force_slow"]` (Tester Powers' apprentice). No enemy blueprint carries a grenade.
- So there is no bed for this step. **It needs one**: an enemy that throws a frag grenade or casts a damaging power (lightning, Force Wave) at the player and at a companion, with a save or two.
- I also didn't check scaling on a companion's damage.

## 8: Regression, TEST 242 and TEST 243

- **Dice**: the right Dice One Quick Save; the first 17 lines match the baseline (SAME17).
- **Regression**: loaded slot 82 (reg243), saved it as slot 83, "reg244", quick-saved mid-fight, loaded slot 83, and won: "Icon Nine: 124 of 196", "FIGHT OVER".
- The saves are authored with no difficulty, so all of the following ran on Normal.

**TEST 242 (Snap Yard)**, same lines and numbers as on a5d6662:
1. "Snap Shot: Ask" sits on the Table Rules page (`s1-table`).
2. "Snap Shot: Snap One attacks Skirmisher : \*hit\* : (8 + 11 = 19)", one only (`sn1-all`).
3. "Skirmisher leaves cover · one reaction · 3 left" is asked; No gives no shot, Yes gives the shot (`sa1-all`, `sa2-all`).
4. Interdict One on Never, and Blade One and Plain One on Always: no shot, though the Skirmisher left cover each time (`sn4-all`, `sb4-all`, `sp4-all`).
5. Up to (2,3): "Reflex Fire: Sniper attacks Snap One : (12 + 7 = 19)". Up, down, up: no second shot that walk. On her very next turn, down to (2,3): "(11 + 7 = 18)" (`sw1`, `sw2`, `sw5`).
6. "Skirmisher attacks Mate", then "Reflex Fire: Reflex One attacks Skirmisher : (18 + 13 = 31)"; the Lurker's later hit on Mate got no answer (`rx-log`).
7. "Blade One attacks Guard : (18 + 15 = 33)", then "Reflex Fire: Sniper attacks Blade One : (18 + 7 = 25)" (`bk3-log`).
8. "Interdiction: Interdict One attacks Skirmisher : (8 + 15 = 23)" (`si8-all`).
9. On Ask: "Reflex Fire: Sniper attacks Mate : (18 + 7 = 25)", a square from Reflex One, brought no question (`n9d`).
   - **TEST 242 finding 2 is fixed**: in the whole run, the only question was "Skirmisher attacks Mate". No "Guard attacks Mate" was asked.

**TEST 243 (Watch Yard)**, same as on b733090:
2. "Watch One declares Overwatch"; round 2: "Overwatch: Watch One attacks Frail : (9 + 14 = 23)", Frail dies, one only (`ow2-all`).
3. Sustained: Frail, then the Watcher. Total: Frail, the Watcher and the Gunner at +16 (`ow3s-all`, `ow3t-all`).
4. Frail dies before moving, under all three.
5. "Frail moves · No keeps the hold": No, so Frail walks. "Watcher attacks": Yes, so "Overwatch: Watch One attacks Watcher : (10 + 14 = 24)" comes first (`o5-log`).
   - The new **Sentry** (Tester Watch gained it at 71b47bc, "for the question that must not be asked") stands out of reach at (11,5). It was never asked about in any Ask run.
6. Never: nothing fires (`ow6-all`).
7. Blade Watch: "Overwatch needs a gun in hand" (`bw-try`).
8. Hidden at (2,2): "Watcher declares Overwatch". The first step down draws nothing; the next draws "Overwatch: Watcher attacks Watch One : (10 + 9 = 19)" (`o8d`).
9. Declared, saved slot 84 "bm244", app restarted, loaded: hover "overwatch", w reads "already holding your shot", and End Turn fires once on Frail (`o9-hov`, `o9-again`, `o9-all`).
10. Long One: "Interdiction: Long One attacks Frail : (20 + 14 = 34)", Frail dies in round 1, and the Distant (26 away) draws no shot (`lo-all`).

## Odd, not filed

- The Table Rules page's title bar reads "Gameplay Options", from the package menu and in-game.
- The app's CPU on the package menu (above), and the 3 to 4 minutes per launch, which slowed every rerun.

## What I got wrong

- In the TEST 243 batch, my question detector took the floating combat text ("Runner attacks Watch One") for a question. It then clicked where the No button sits, on the board, about twice per run. The results still match TEST 243 line for line. The detector now needs "ONE REACTION" before it treats anything as a question.
- My status-box screenshots for steps 3 to 6 went to my TEST 243 folder, because I was still using the 243 helper. They're copied into test-244 under the names cited above.
