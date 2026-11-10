# TEST 245: Difficulty hash 2 (the Death row) and the launch fix

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the load log are in `KOTOR_RPG_MAIN_WORK/media/screens/test-245/`; names in brackets below are files there.

## Build

- **App**: main `0726491`, a fresh worktree. `gate.py --at 0726491`: "FOR TESTER — CORE at 0726491, 5833 tests, 0 failed".
- **Lodestar**: `d0f0e58` compiled, as the order says.
- **Settings**: defaults at the start. **Shelf**: `de3441d`, check_shelf clean ("33 rules files and 128 standard blueprints, all identical"). My MAIN_WORK copy was behind and first reported event_kinds.toml stale (the new `table.death-set` kind); after a pull it was clean.
- **Beds**: all 26 save tools ran with no errors, the death and scale tools included. Saves folder: 545 entries, 348 `.sav`, 7.2 MB.
- Every step ran on `0726491`.
- **Loads**: every load is in `loads.txt`. Each `.sav` load started from the pristine authored copy; the md5 logged there is taken after the load, and a fight-on-load save has already had events written by then. Pristine md5s: death-normal `50dc5b5a`, death-bare `680111cc`, death-hard `0df03855`, scale-easy `178a1821`, scale-normal `b83208c9`, scale-hard `ee8fc307`, watch-one `f72c377e`. The two quick-save loads are listed with their own md5.

## Summary

Two findings: the package menu still runs at 66-70% CPU (step 2), and the first bleed comes a round late (step 8). Step 12's "win the fight" is not run.

| # | Check | Result |
|---|---|---|
| 1 | Launch, console lines | **PASS**. Library listed in 926 ms, checked in 7532 ms; save scan 5 saves in 1617 ms. 9 s to a usable library. |
| 2 | Idle CPU | **FINDING 1**. Library 0.0%, but the package menu holds 66-70%, not near 0. Continue pulses, slow and smooth. |
| 3 | Relaunch twice | **PASS**. 11.5 s to the open card, three times out of three. |
| 4 | Table Rules title and rows | **PASS**. "Table Rules" from the package menu and in game; Difficulty, Death, then the six reactions. |
| 5 | Death follows, then holds (in game) | **PASS**. |
| 6 | Death set apart on the package menu | **PASS**. Holds across close and reopen; Difficulty does not move it; the New Game reads Death: Hard. |
| 7 | Scale Easy / Normal / Hard | **PASS**. Grenade 2+2, 4+4, 6+6; Force Shock 1 and 5 / 3 and 10 / 4 and 15 on the same dice. |
| 8 | Mate bleeds to -10, then holds | **PASS**, with **FINDING 2** (a question): the first bleed comes a round late. |
| 9 | Treat with a medpac | **PASS**. -10 + 13 = 3, standing, Action spent. |
| 10 | Treat with no medpac | **PASS**. "brought up to 0", still down, Action spent; then "treat — no medpac". |
| 11 | Death to Hard with Mate at -10 | **PASS**. Stays down and on the board, through a round and a quick save and reload. |
| 12 | Death Hard | **PASS** for death, Keeper and the switch back; **NOT RUN** for "win the fight" (the Brute has 400 vitality). |
| 13 | Normal to Easy while dying | **PASS**. Both stop bleeding at once. |
| 14 | Regression | **PASS**. SAME17; slot 83 to 84, fight won; every 242 and 243 step as before. TEST 244's damage steps not rerun on the Watch Yard (step 7 covers the scaling). |

## A. The launch

### 1: Console lines and time to the card

First launch after regenerating every save, timed from a terminal:

> library: 75 packages listed in 926 ms
> library: 75 packages checked in 7532 ms
> save scan: 5 saves in 1617 ms

- The "checked in" line came 9.1 s after launch. The library was usable then.
- The Tester Watch card opened 204.7 s after launch, and the "save scan" line came with it. **That time was my own tool, not the app.** My card finder (`findpkg.sh`) scrolls 300 clicks left, then OCRs the whole screen after every 12-click step to the right. On this build it took 195 s to reach Tester Watch.
- Between the "listed" and "checked" lines the console also prints three `⚠ verify:` lines for Tester Probe's walled-in arrival (an existing bed problem).

### 2: Idle CPU (FINDING 1)

`top` on the app PID, 5 s samples:

- **Package menu (Tester Watch, 5 saves)**, 13 samples over 65 s: 70.0, 66.5, 67.0, 66.7, 66.2, 67.3, 66.2, 68.1, 67.0, 66.7, 66.8, 66.8, 66.7.
- **Library screen**, 7 samples: 0.0 every time.
- **Two more package menus** (Endar Spire, 11 saves; Tester 214, 4 saves): 65.7 to 70.0. Every card I opened had saves, so I couldn't see a menu without the Continue pulse.
- **Continue pulses, slow and smooth**: its top border brightness over 4 s of 0.2 s frames went 173, 197, 201, 191, 161, 118, 92, 68, 65, 82, 118, 147, 183, 200, 197, 183, 147, 104, 74, 64, a period of about 2.5 s.

The library idles at 0 and the menu at about 67%, so the cost looks like the pulse being drawn. This is a debug build on Xvfb, which draws in software. It is well down from TEST 244's 220-360%, but not near 0.

### 3: Relaunches

| Run | "checked in" line | Card open ("save scan" line) | Console |
|---|---|---|---|
| 1 | 9.1 s | 11.5 s | listed 923 ms, checked 7703 ms, save scan 11 saves in 1621 ms |
| 2 | 9.1 s | 11.5 s | listed 927 ms, checked 7586 ms, save scan 11 saves in 1620 ms |
| 3 | 9.1 s | 11.5 s | listed 922 ms, checked 7530 ms, save scan 11 saves in 1622 ms |

These were timed on Endar Spire, the first card, so no scrolling is in them. Continue was lit on the open menu each time (`a3-run1` to `a3-run3`).

## B. Table Rules

### 4: Title and rows

- **Package menu** (Tester Death card): Options lists Table Rules first (`b4-options`). The title bar reads **"Table Rules"**. The rows are **Difficulty: Normal, Death: Normal**, then Opportunity attack, Force Deflection, Force Redirection, Parry, Snap Shot and Overwatch (`b4-table-pkg`).
- **In game**: Escape > Table Rules, the same title and the same rows (`b6-ingame`).
- The Death row's text: "What happens to a party member who falls. Easy: down at 0, and up when the fight ends. Normal: below 0 they bleed, down at minus Constitution, and only a wipe kills. Hard: dead at minus Constitution. Until it is changed here, it follows Difficulty."

### 5: In game, Death follows and then holds

On Watch One (authored with no Death setting):

| Click | Difficulty | Death |
|---|---|---|
| loaded | Normal | Normal |
| Difficulty + | Hard | Hard |
| Difficulty + | Easy | Easy |
| Death + | Easy | Normal |
| Difficulty - | Hard | Normal |
| Difficulty - | Normal | Normal |

(`b5-0`, `b5-1`, `b5-2`.)

### 6: Package menu, Death set apart

- Death set to Hard, Difficulty Normal. settings.json then reads `"newGameDifficulty":{"tester-death":"normal"},"newGameDeath":{"tester-death":"hard"}`.
- Closed and reopened: Difficulty Normal, Death Hard (`b6-clean-reopen`).
- Difficulty to Hard, then Easy, then Normal: Death stays Hard each time (`b6-clean-end`).
- **New Game** on Tester Death, Custom Character: a Human Soldier named "Death Apart". In play, the in-game Table Rules reads **"Difficulty: Normal"** and **"Death: Hard"** (`n37`, `b6-ingame`).

## C. Step 7 from TEST 244: Tester Scale

The fight starts on load each time: the Inquisitor has already cast once. I ended my turn and Mate's, and the Grenadier threw. The three saves share their dice, so the Normal numbers are the unscaled ones.

| Save | Grenade (log) | Force Shock, round 1 (resisted) | Force Shock, round 2 (success) |
|---|---|---|---|
| Scale Easy | "Mate damaged: 2", "Scale Easy damaged: 2" | (17 + 4 = 21 vs. 14), 1 damage | (8 + 4 = 12 vs. 14), 5 damage |
| Scale Normal | "Mate damaged: 4", "Scale Normal damaged: 4" | same roll, 3 damage | same roll, 10 damage |
| Scale Hard | "Mate damaged: 6", "Scale Hard damaged: 6" | same roll, 4 damage | same roll, 15 damage |

- Easy: floor(3 x 0.5) = 1, floor(10 x 0.5) = 5. Hard: floor(3 x 1.5) = 4, floor(10 x 1.5) = 15.
- Mate, a companion, is scaled like the player.
- The log shows the scaled number only, and the status box keeps just the last actor, so the Normal run is my source for the unscaled roll (`s7e-log1`, `s7n-log`, `s7h-log`).

## D. The Death row (Tester Death)

Turn order on every Death load: Brute, Mate, you, Keeper. The Brute closes and swings each round; Mate and Keeper hold.

### 8: Death Normal, Mate drops and bleeds

Status line after each End Turn, against the log's round numbers (`d8-all`):

| Round | Mate | Keeper | Log |
|---|---|---|---|
| 1 | 12 | 12 | Brute misses Mate |
| 2 | **-1** | 12 | "Brute damages Mate for 13 damage" |
| 3 | **-1** | 1 | Brute hits Keeper for 11 |
| 4 | -2 | **-7** | Brute hits Keeper for 8 |
| 5 | -3 | **-7** | Brute misses you |
| 6 | -4 | -8 | |
| 7 | -5 | -9 | |
| 8 | -6 | -10 | |
| 9-11 | -7, -8, -9 | -10 | |
| 12 | **-10** | -10 | |
| 13 | -10 | -10 | |
| 14 | -10 | -10 | |

- Mate reaches -10 in round 12 and stays at -10, down and on the board, for rounds 13 and 14 (`d8-e17`). Keeper does the same from round 8.
- Downed allies leave the initiative strip and stay on the board.

**FINDING 2 (a question)**: each one's first bleed comes a round late. Mate dropped to -1 in round 2 and was still -1 in round 3; the first loss was in round 4. Keeper dropped to -7 in round 4, was still -7 in round 5, and first lost one in round 6. Death Bare and Death Hard show the same pattern on the same dice. If one free round is intended, this is not a defect.

### 9: Treat with a medpac (Mate at -10)

- t opens "treat — 1 Mate · 2 Keeper · esc". 1:
  > treat Mate — d20 3 + Medicine 0 = 3 · Medpac — + base 10 + Medicine check 3 = 13 · Mate 3 of 12 (was -10) · 2 left
- Mate is at 3, back on the initiative strip, standing (`d9-treat`).
- t again: "treat — you have already acted" (`d9-again`).

### 10: Death Bare, no medpac

- Mate at -10 after 15 End Turns (the same rounds as above).
- t, 1: "**treat Mate — d20 9 + Medicine 0 = 9 · brought up to 0**". Mate is at 0 and stays off the strip, so still down (`d10-treat`). t again: "you have already acted".
- Next turn, Mate still at 0 (no further bleed). t, 1: "**treat — no medpac**" (`d10-nomedpac`).

### 11: Death Normal, Mate at -10, Death to Hard

- From my quick save (round 11, Mate -9), one End Turn: Mate -10. Table Rules: Death to **Hard** (`d11-hard`).
- Mate stays on the board, at -10, down (`d11-board`), and through one more round.
- F4, then loaded that quick save: "the fight resumes — round 13, Death Normal's turn", Mate -10, still on the board and down. Table Rules still reads Death: Hard (`d11-reload`).

### 12: Death Hard (Difficulty Normal, Death set apart at Hard)

- Loaded: Difficulty Normal, Death Hard.
- Same rounds as Death Normal. In round 12 Mate reaches -10 and **leaves the board**; the status row still reads "**Mate: -10 of 12**" (`d12-e15`).
- **Keeper** reached -10 in round 8 and stays down on the board.
- **Death to Normal**: Mate stays off the board through two more rounds, and the row still reads "Mate: -10 of 12" (`d12b-normal`, `d12b-after`).
- **Win the fight: NOT RUN.** The Brute has 400 vitality and I have a blaster pistol, with 18 vitality left by then. I can't win this fight, so I couldn't see Keeper get up or Mate stay dead at the end. It needs a Brute that can be beaten, or another way to end the fight.

## E. Regression

- **Dice**: the right Dice One Quick Save (Oct 19, 07:40:30); the first 17 lines match the baseline (SAME17).
- **Regression**: Icon Nine. Loaded slot 83 (reg244), saved it as "reg245", which took **slot 84**, quick-saved mid-fight, loaded slot 84, and won: "Icon Nine: 106 of 196", "FIGHT OVER" (`reg-end`).
- The Snap and Watch saves are authored with no difficulty, so all of the following ran on Normal. TEST 244's own steps (damage taken and dealt on Easy, Normal and Hard) are covered by step 7 above and weren't rerun on the Watch Yard.

**TEST 242 (Snap Yard)**, same lines and numbers as in TEST 244:
1. "Snap Shot: Ask" on the Table Rules page.
2. "Snap Shot: Snap One attacks Skirmisher : \*hit\* : (8 + 11 = 19)", one only (`sn1-all`).
3. "Skirmisher leaves cover · one reaction · 3 left" is asked; No gives no shot, Yes gives the shot (`sa1-all`, `sa2-all`).
4. Interdict One on Never, and Blade One and Plain One on Always: no shot (`sn4-all`, `sb4-all`, `sp4-all`).
5. Up to (2,3): "Reflex Fire: Sniper attacks Snap One : (12 + 7 = 19)". Up, down, up: no second shot that walk. Her next turn, down to (2,3): "(11 + 7 = 18)" (`sw1`, `sw2`, `sw5`).
6. "Skirmisher attacks Mate", then "Reflex Fire: Reflex One attacks Skirmisher : (18 + 13 = 31)"; the Lurker's later hit on Mate got no answer (`rx-log`).
7. "Blade One attacks Guard : (18 + 15 = 33)", then "Reflex Fire: Sniper attacks Blade One : (18 + 7 = 25)" (`bk3-log`).
8. "Interdiction: Interdict One attacks Skirmisher : (8 + 15 = 23)" (`si8-all`).
9. On Ask: the only question was "Skirmisher attacks Mate"; "Reflex Fire: Sniper attacks Mate : (18 + 7 = 25)" brought none (`n9d`).

**TEST 243 (Watch Yard)**, same as in TEST 244:
2. "Watch One declares Overwatch"; round 2: "Overwatch: Watch One attacks Frail : (9 + 14 = 23)", Frail dies, one only (`ow2-all`).
3. Sustained: Frail, then the Watcher. Total: Frail, the Watcher and the Gunner at +16 (`ow3s-all`, `ow3t-all`).
4. Frail dies before moving, under all three.
5. Ask: "Frail moves · No keeps the hold": No, Frail walks. "Watcher attacks": Yes, "Overwatch: Watch One attacks Watcher : (10 + 14 = 24)" comes first (`o5-log`).
6. Never: nothing fires (`ow6-all`).
7. Blade Watch: "Overwatch needs a gun in hand" (`bw-try`).
8. Hidden at (2,2): "Watcher declares Overwatch"; the first step down draws nothing, the next draws "Overwatch: Watcher attacks Watch One : (10 + 9 = 19)" (`o8d`).
9. Declared, saved slot 85 "bm245", app restarted, loaded: hover "overwatch · move 5 of 5 · reactions 3 of 3", w reads "already holding your shot", End Turn fires once on Frail, "(6 + 14 = 20)" (`o9-hov`, `o9-again`, `o9-all`).
10. Long One: "Interdiction: Long One attacks Frail : (20 + 14 = 34)", Frail dies in round 1, and the Distant (26 away) draws no shot (`lo-all`).

## Odd, not filed

- **A row's label steps its value.** Clicking the words "Death: Normal" (to read its text) moved it to Hard, exactly like +. Difficulty's label does the same. That is how my first reading of the Death row went wrong (below).
- **There is no way back to "follows Difficulty"** from the menu once Death is changed. Default leaves Difficulty and Death as they are. I cleared it by editing settings.json with the app stopped.
- The package-menu Options text for Table Rules still reads "The table's rules: the difficulty, and the reactions", with no mention of Death.
- The Overwatch row sits below the list's border on the Table Rules page, both menus (`b4-table-pkg`).
- No "Mate dies" line in the Combat log on Death Hard; TEST 243's Frail got "Frail dies".
- After Mate died on Death Hard, the party portraits at the right still showed two companions (`d12-e15`).
- Two loads of the same pristine Snap Yard saves rolled differently today: the Skirmisher's round-2 d20 was 14 in the batch run (`sa1-all`, `sb4-all`) and 8 in my first run of the same steps. The reactions behaved the same both times. One sample each, so only noted.
- With only one downed ally, t treats at once without the menu. On Death Hard, after Mate died, t treated Keeper straight away, so Mate was not offered.

## What I got wrong

- **TEST 244's "3 to 4 minutes per launch" was mostly my own card finder**, not the app. Today `findpkg.sh` took 195 s to reach Tester Watch on a build whose library is ready in 9 s. The 220-360% CPU in TEST 244 was the app's, though. I now use a quicker finder, which still takes about 80 s to reach a card on the right of the library.
- In step 6, my first reading said Death + went from Normal to Easy. I had clicked the Death label first to read its text, which stepped it to Hard; the + then wrapped it to Easy. Repeated from a cleared setting, one + gives Normal to Hard.
- On Death Hard I pressed t to look at the Treat menu and it treated Keeper at once (one target), and my Death switch didn't land. I reloaded Death Hard and replayed it; the dice and rounds matched the first run.
