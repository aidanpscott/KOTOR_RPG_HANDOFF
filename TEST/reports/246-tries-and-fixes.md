# TEST 246: Difficulty hash 3 and TEST 245's fixes

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the load log are in `KOTOR_RPG_MAIN_WORK/media/screens/test-246/`; names in brackets below are files there.

## Build

- **App**: main `9a09ff9`, a fresh clone. `gate.py --at 9a09ff9`: "FOR TESTER — CORE at 9a09ff9, 5859 tests, 0 failed".
- **Lodestar**: `ed9f5d0` compiled into both the app and Loom, as the order says. **Loom**: `cf8e7be`, a fresh clone.
- **Settings**: defaults at the start. **Shelf**: `65931d1`, check_shelf clean ("33 rules files and 128 standard blueprints, all identical").
- **Beds**: all 27 save tools ran with no errors, the tries and death tools included. Saves folder: 551 entries, 354 `.sav`, 7.2 MB. I copied the whole folder, `.marks` folders included, as the restore source.
- Every step ran on `9a09ff9`.
- **Loads, by the new rule**: before each `.sav` load I deleted the save's `.marks` folder, copied back the `.sav` and its whole `.marks` folder (where one existed) from that copy, and logged the md5s BEFORE the load. Every one is a `BEFORE` line in `loads.txt`, with an `AFTER` line once the save was loaded. The `.sav` md5 changes on load, because the fight-on-load saves write events. Quick-save reloads are logged with the `quick.mark` md5 before the load.

## Summary

No findings. Step 13 is NOT RUN, because Proof Immune's fight can't be won. I also report one Death Yard load that started differently from the same restored file (H), and a Death Bare wording change (I).

| # | Check | Result |
|---|---|---|
| 1 | Hard door, Open Lock | **PASS**. "open lock — d20 5 + Security 4 = 9 vs 40 (legendary) · This object cannot be opened through conventional means." |
| 2 | The door again | **PASS**. Both entries refused with K2's line; clicking either rolls nothing. |
| 3 | Footlocker below | **PASS**. "· the lock is destroyed", then refused the same way. |
| 4 | Footlocker left | **PASS**. "it holds" three times, a new roll each time. |
| 5 | Quick save and reload | **PASS**. Door and footlocker below still refused. |
| 6 | Tries Normal | **PASS**. Both "hold" and roll again. |
| B | The mine, Normal and Hard | **PASS**. Two tries each, all "vs 40 (legendary) · it is still live"; no refusal. |
| 7 | Envoy, Normal | **PASS**. The opening ends with Hear me out., Please., Goodbye. |
| 8 | Leave and talk; reload | **PASS**. The same both times. |
| 9 | Envoy, Easy | **PASS**. As Normal, and Move. stays. |
| 10 | Envoy, Hard | **PASS**. As Normal. |
| 11 | Blast Normal and Easy | **PASS**. Normal: Mate and the Dummy take 4. Easy: only the Dummy takes 4. |
| 12 | Death Easy, then Death Normal, win | **PASS**. Easy: Mate stands at 12 of 12. Normal: "revived at 1". |
| 13 | Proof Immune, Easy, win | **NOT RUN**. The three foes have 400 vitality each; the fight can't be won. |
| 14 | Death Hard | **PASS**. "Mate dies"; Mate leaves the board and the portraits; win: Keeper "revived at 1", Mate stays dead. |
| 15 | Death row, both menus | **PASS**. "Same as Difficulty"; the words change nothing; left is Hard, right is Easy. |
| 16 | Same follows Difficulty | **PASS**. In game, and after a reload. |
| 17 | Overwatch row and blurb | **PASS**. Inside the border; "the difficulty, death, and the reactions". |
| 18 | Loom, the marks | **PASS**. Footlocker "destroyed" lit; door "lockout" lit. |
| 19 | Loom, Hear me out. | **PASS**. "if Persuade" with "until-success" lit. |
| 20 | Loom, clear a DC | **PASS**. Footlocker and door: the mark goes, on screen and in the file. |
| H | Snap Yard dice | **PASS**. The Sniper's first rolls 10, 12, both loads; the whole log identical. But see the Death Yard below. |
| I | Regression | **PASS**. SAME17; slot 84 to **86** (85 was my TEST 245 bookmark), fight won; TEST 245's steps and its 242/243 steps as before. Death Bare's treat line now reads "stabilized". |

## A. Hard's locks (Tries Hard)

The yard is as the order says: you at (1,1), the door (2,1), the footlockers (1,2) and (0,1), the mine (2,2), the Envoy (1,0) (`a0`).

1. **The door**: right-click lists Examine (Science), Open Lock (legendary), Open Lock (spend a spike, +5) (`a1-menu`). Open Lock: "**open lock — d20 5 + Security 4 = 9 vs 40 (legendary) · This object cannot be opened through conventional means.**" (`a1-box`).
2. **Again**: both Open Lock entries are greyed, each followed by "— This object cannot be opened through conventional means." (`a2-menu`). Clicking each puts only that line in the box, with no roll (`a2-box1`, `a2-box2`).
3. **The footlocker below**: "**open lock — d20 8 + Security 4 = 12 vs 40 (legendary) · the lock is destroyed**" (`a3-box1`). Right-click again: both Open Lock entries are refused with K2's line (`a3-menu2`); clicking one rolls nothing (`a3-box2`).
4. **The footlocker left**: "d20 16 … = 20 vs 40 (legendary) · it holds", then d20 20 = 24, then d20 16 = 20, all "it holds" (`a4-box1` to `a4-box3`).
5. **Quick save (F4) and reload** (Quick Save 16:26:34): "you notice Mine" again, so the load took. The door's and the footlocker's menus are still refused (`a5-door`, `a5-foot`).
6. **Tries Normal**: the door "d20 5 … = 9 vs 40 (legendary) · it holds", then d20 8 = 12, "it holds". The footlocker below: d20 16 = 20, then d20 20 = 24, "it holds" both times. Its menu stays open (`n6-door1`, `n6-door2`, `n6-foot1`, `n6-foot2`).

## B. The mine

The mine's menu has one entry, "Disarm (legendary)" (`bh-menu`).
- **Hard**: "disarm — d20 6 + Demolitions 4 = 10 vs 40 (legendary) · it is still live", then d20 8 = 12, the same (`bh-box1`, `bh-box2`).
- **Normal**: d20 16 = 20, then d20 18 = 22, the same (`bn-box1`, `bn-box2`).

## C. The Envoy

Walking into the Envoy opens "Envoy: State your business." with six replies. Each reply rolls when picked, then "Envoy: No." or "Very well." and [Continue.] back to the opening.

**7, Normal** (`e7-r1` to `e7-r5`, `e7-end`):

| Reply | Roll | Back at the opening |
|---|---|---|
| Let me through. | "persuade failed — 9 needed 40 (d20 9)" | gone |
| Hear me out. | "persuade failed — 10 needed 40 (d20 10)" | stays |
| You know me. | "persuade passed — 17 needed 1 (d20 17)", "Very well." | gone |
| Please. | "persuade failed — 2 needed 40 (d20 2)" | stays |
| Move. | "intimidate failed — 18 needed 40 (d20 15 +3 Strength)" | gone |

The opening then reads "1. [persuade] Hear me out. 2. [persuade] Please. 3. Goodbye."

**8**: Goodbye ("Safe travels.", [Leave.]), then talking again shows the same three (`e8-again`). F4, then loading that Quick Save (16:33:47) and talking again: the same three (`e8-reload`).

**9, Easy**: the same rolls and lines, but the opening reads "Hear me out. · Please. · **Move.** · Goodbye." Leave and talk again: the same four (`e9-end`, `e9-again`).

**10, Hard**: the same as Normal: "Hear me out. · Please. · Goodbye.", and again after leaving and talking (`e10-back5`, `e10-again`).

## D. Easy's extras

**11, Blast Yard**: the fight starts on load and it's already your turn (initiative "Blast Normal 21 · Mate 15 · Dummy 15"), so there were no turns to end. o, then the Dummy:
- **Blast Normal**: the log reads "Blast Normal uses Frag Grenade. / Mate damaged: 4 / Dummy damaged: 4"; the box shows Mate 396 of 400 and the Dummy 396 of 400 (`g11n-log`, `g11n-box`).
- **Blast Easy**: "Blast Easy uses Frag Grenade. / Dummy damaged: 4". Mate stays at 400 of 400 and the Dummy goes to 396 (`g11e-log`, `g11e-box`).

**12, Death Yard, Death Normal save**:
- **Death set to Easy** in Table Rules (+ once from "Same as Difficulty"). The Brute dropped Mate to 0, and Mate stayed at 0. I shot the Brute twice (10 vitality): "Brute and Mate and Keeper falls … -6 left … dies". Mate's portrait reads "**Vitality 12 of 12**", and so does Keeper's (`d12-r1-full`, `d12-portm1`, `d12-portm2`).
- **Death Normal** (a fresh load, Death left on "Same as Difficulty" with Difficulty Normal): Mate went to -3. I shot the Brute until it fell (Keeper hit it once too): "**Mate: 1 of 12 — in your campaign, a01 left you at -3 · revived at 1**" (`d12n-s3`).

**13, Proof Immune: NOT RUN.**
- The fight starts when you walk into Rock. Rock, Steady and the Thug have **400 vitality each**. Proof Immune has 239 Force, and Force Push does 8d6 for 6f, so winning is out of reach. The Force refill can't be seen without a win.
- What I could see: on Easy, Force Push reads "**Force Push · 6f — 239 > 233 · ceiling −1 to 238** … stunned · Rock — 8d6 21", and the box shows "force 233 of 238 (max 239)" (`p13-push2`).
- On Normal the line is the same: "6f — 239 > 233 · ceiling −1 to 238 … Thug — 8d6 25" (`p13n-push`).
- Pressing the target's number aims the power. Clicking a foe after choosing the power makes an unarmed attack instead (`p13-push`).
- It needs a bed with a foe that can be beaten.

## E. Death Hard

14. Death Hard's own save, with Death set apart at Hard:
- I ended turns. Mate went to -1 at my third End Turn and then bled one a round; Keeper went to -7, then -10, and stayed on the board.
- In round 12 the log reads "**Mate dies**" (`e14-log`). Mate is gone from the board, and the party portraits at the right show only one companion (`e14-full15`). The status row still reads "Mate: -10 of 12".
- I shot the Brute twice: "**Keeper: 1 of 12 — in your campaign, a01 left you at -10 · revived at 1**". Mate isn't revived (`e14-s2`).
- After the fight, the portraits at the right and the Options party row show Keeper only. Keeper's portrait hover reads "Vitality 1 of 12" (`e14-after`, `e14-board`).

## F. Table Rules

15. **"Death: Same as Difficulty"** is the default, from the package menu and in game (`d12-table0`, `f15-pkg0`).
- Clicking the words "Death: Same as Difficulty" changes nothing, and neither does clicking "Difficulty: Normal" (`f15-label`, `f15p-label`, `f15p-difflabel`).
- From Same, **left is Hard** and **right is Easy** (`f15-minus`, `f15p-left`, `f15p-right`).
- The full cycle to the right is Same → Easy → Normal → Hard → Same (`f16-p1` to `f16-p4`).

16. **Same follows Difficulty**:
- **In game, Death Normal save**, Death stepped away and back to Same. Mate went to -1 at my third End Turn and then -2, and Keeper to -7, both bleeding.
  - Difficulty to Easy: Mate held at -2 and Keeper at -7 for two rounds (`g16-easy`, `g16-x1` to `g16-x6`).
  - F4, then I loaded that Quick Save ("the fight resumes — round 10"). The rows still read "Difficulty: Easy, Death: Same as Difficulty" (`g16-reload-rows`).
  - Difficulty to Normal: Mate -2, -3, -4 … -7 and Keeper -7, -8, -9, -10, so both bleed again (`g16-normal`, `g16-y1` to `g16-y6`).
- **On the package menu**: Difficulty + to Hard leaves Death on "Same as Difficulty". settings.json reads `"newGameDifficulty":{"tester-death":"hard"},"newGameDeath":{}`, and after close and reopen it's the same. I set Difficulty back to Normal afterwards.
- In my first try at 16, I put Mate at exactly 0 on Easy and then switched to Normal. Mate and Keeper stayed at 0 for three rounds. A character at 0 isn't dying under the d20 rules, so that try tested nothing, and I redid it with Mate below 0.

17. The Overwatch row sits inside the list's border on both pages (`d12-table0`, `f15-pkg0`). The Table Rules blurb reads "**The table's rules: the difficulty, death, and the reactions**" in the in-game Options and in the package-menu Options (`f17-blurb-ingame`, `f17-pkgopts`).

## G. Loom (Tester Tries)

I opened a copy of the package (`notes/loom246/tester-tries`), so the shelf's own copy wasn't touched.
18. a01, footlocker.tries.02: "locked at 40" and "**on Hard, a failed attempt** · can be tried again · lockout · **destroyed**", with destroyed lit (`g18-foot`). door.tries.01: the same row with **lockout** lit (`g18-door`).
19. The envoy conversation, "Hear me out." selected: "**if Persuade** · one-try · **until-success** · retryable", with until-success lit (`g19-hear`).
20. Clearing the footlocker's DC field: the panel reads "not locked" and the "on Hard" row is gone (`g20-cleared`). In `areas/a01.toml`, its `locked` and `hard_failure` lines are both gone. The door does the same (`g20-door`).

## H. Snap Yard dice

- snap-one.sav restored before each load (md5 `b1425848` both times; there is no `snap-one.marks` in the regenerated folder), Snap Shot on Ask, End Turn twice answering No.
- Both loads: "Sniper attacks Snap One : \*hit\* : (**10** + 9 = 19)", then "(**12** + 9 = 21)". The two Combat logs are identical line for line (`h1-all`, `h2-all`).
- **But the Death Yard did not hold still.** I loaded death-normal.sav four times from the same restored file (md5 `c57a4656` before each, no `.marks` folder). Three loads matched TEST 245: the Brute acts first, and Mate is dropped at my third End Turn. The 16:57:02 load started differently. The strip and the status row read Keeper, Mate, Brute, then me, and Mate went to -3 at my second End Turn (`d12n-board`; compare `d12-0`). The four loads are lines 14 to 24 of `loads.txt`. One load in four, so I've only reported it.

## I. Regression

Every step below ran on `9a09ff9`.

- **Dice**: the right Dice One Quick Save (Oct 19, 07:40:30); the first 17 lines match the baseline (SAME17). dice-one and icons-185 were restored with their `.marks` folders and logged first (`loads.txt` lines 34 and 35).
- **Regression**: Icon Nine. I loaded slot 84 (reg245) and saved it as "reg246". That took **slot 86, not 85**: slot numbers are shared across characters, and 85 is my TEST 245 bookmark in `watch-one.marks`. Then a quick save mid-fight, a load of slot 86, and the win: "Icon Nine: 103 of 196", "FIGHT OVER" (`reg-end`).
- **TEST 245's own steps**:
  - **Launch** (step 1): "library: 76 packages listed in 940 ms", "checked in 7726 ms", "save scan: 1 saves in 1663 ms".
  - **Scale** (step 7): the same lines as in TEST 245. The grenade does 2 and 2, 4 and 4, 6 and 6 to Mate and you. Force Shock does 1 and 5 on Easy, 3 and 10 on Normal, 4 and 15 on Hard (`s7e-log`, `s7n-log`, `s7h-log`).
  - **Treat** (step 9), Death Normal, Mate at -1: "**treat Mate — d20 8 + Medicine 0 = 8 · Medpac — + base 10 + Medicine check 8 = 18 · Mate 12 of 12 (was -1) · 2 left**", then "treat — you have already acted" (`t9-treat`, `t9-again`).
  - **No medpac** (step 10), Death Bare, Mate at -1: "treat Mate — d20 8 + Medicine 0 = 8 · **stabilized — no longer bleeding out**", and Mate is at 0. In TEST 245 this read "brought up to 0". A second t that turn: "treat — no medpac" (`t10-treat`, `t10-again`).
  - **Steps 4 to 6 and 8 to 13** are covered by this test's D, E and F.
- **TEST 242 (Snap Yard)**: the same lines and numbers as in TEST 245.
  - "(8 + 11 = 19)", one only; Ask, No and Yes; no shot on Never or with no gun.
  - Reflex Fire "(12 + 7 = 19)" once a walk, then "(11 + 7 = 18)"; "(18 + 13 = 31)"; "(18 + 15 = 33)" then "(18 + 7 = 25)".
  - Interdiction "(8 + 15 = 23)"; on Ask the only question was "Skirmisher attacks Mate".
  - In TEST 245's batch, the Skirmisher's round-2 d20 on ask-no and sb4 was 14. Today it is 8 both times, matching my first TEST 245 run (`sa1-all`, `sb4-all`).
- **TEST 243 (Watch Yard)**, from the rerun: the same as in TEST 245.
  - Overwatch "(9 + 14 = 23)", one only. Sustained hits Frail and the Watcher; Total hits three at +16.
  - Never fires nothing. Blade Watch: "Overwatch needs a gun in hand". Ask: "Frail moves" (No), then "Watcher attacks" (Yes) "(10 + 14 = 24)".
  - The Watcher declares; my second step draws "(10 + 9 = 19)".
  - Bookmark "bm246" took **slot 87**. Loaded in a fresh app: the hover reads "overwatch · move 5 of 5 · reactions 3 of 3", w reads "already holding your shot", and End Turn fires once, "(6 + 14 = 20)".
  - Long One: "(20 + 14 = 34)", and the Distant draws no shot.
- **My first Watch Yard batch is void** (`regress.out`). My restore copy of `watch-one.marks` still held my TEST 245 bookmark (slot 85) and an autosave, so those loads opened the held state ("already holding your shot", no declaration line). I moved those leftovers out of the restore copy and reran the Watch sections (`regress-watch.out`, `loads.txt` lines 77 to 95). No other save in this test restored a non-empty `.marks` folder, except dice-one and icons-185, which are meant to.

## Odd, not filed

- "**Brute and Mate and Keeper falls**" ends the fight. The words list the downed companions, and on Death Hard they include the dead Mate.
- After the Hard footlocker's lock is destroyed, its menu runs off the bottom of its frame, and the Search (Awareness) row isn't visible (`a3-menu2`).
- After a grenade throw or a shot with a single click, the box adds "you have already acted" (`g11n-box`, `g11e-box`).
- In both Death Normal runs, Mate's first bleed came a round late again (Mate -3 held a round before the win, `d12n-s1`, `d12n-s2`). That is TEST 245 finding 2, still with Coder.
- An F4 quick save also writes an Auto Save with the same time (`a5-list`).

## What I got wrong

- Twice an Escape meant to close a menu opened Options instead, because the menu had already closed. Both times I closed Options and redid the step. The first time it showed the in-game blurb, which I kept for step 17.
- In my first Proof Immune run, Force Push went to Rock rather than the Thug. I pressed 3 for the Thug, but the list's numbering had changed after the first round. The Normal run hit the Thug.
- My first try at step 16 used Mate at exactly 0, which can't show a bleed (above).
- My restore copy of the saves folder carried leftover `.marks` from earlier tests. For watch-one that included my own TEST 245 bookmark and an autosave, so my first Watch Yard regression batch loaded the wrong state. It's rerun and the first batch is void (I, above). The restore copy should have held only what the save tools write.
