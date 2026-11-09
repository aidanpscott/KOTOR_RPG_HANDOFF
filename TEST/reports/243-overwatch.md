# TEST 243: Overwatch (Overwatch, Sustained, Total)

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the load log are in `KOTOR_RPG_MAIN_WORK/media/screens/test-243/`; names in brackets below are files there. Log lines are quoted from the in-game Combat log.

## Build

- **App**: main `b733090`, a fresh worktree. `gate.py --at b733090`: "FOR TESTER — CORE at b733090, 5774 tests, 0 failed"; ARCHIVE last green at b733090.
- **Lodestar**: `bc30c84` compiled (package_config.json), as the order says.
- **Settings**: defaults (no settings.json) at the start. **Shelf**: `858ca4f`, check_shelf clean.
- **Beds**: every `author_tester_*` tool ran with no errors, the watch and snap tools included.
- Every step ran on `b733090`. TEST 242's rerun steps were not repeated here; they were filed on `a5d6662` (HANDOFF 511e303).
- **Loads**, as MAIN asked after TEST 242: every load is listed in `loads.txt`, with the save file, its md5, the row the name check read, and the settings at launch.
  - Each fresh load of a `.sav` was a pristine copy with the same md5 every time (watch-one.sav `49ccf4c5`, sustain-one.sav `dfd9db81`, total-one.sav `460bc238`, blade-watch.sav `77dc04cc`, long-one.sav `a9d1930f`).
  - The step 9 load was `watch-one.marks/000081.mark` (slot 81, "bm243"), in a freshly started app.

## Summary: every step passes, no findings

| # | Check | Result |
|---|---|---|
| 1 | Gameplay row | **PASS**. "Overwatch: Ask". |
| 2 | Watch One, Always | **PASS**. Declared, Action spent, Move kept; refused twice; one shot, before the enemy acts; the hold then gone. |
| 3 | Sustain One, Total One | **PASS**. Two different enemies; three, each at +2. |
| 4 | Frail under Total | **PASS**. Shot before it moves, dies where it stood, never strikes. |
| 5 | Ask | **PASS**. "<enemy> moves" or "<enemy> attacks" asked before it acts; No keeps the hold; Yes fires. |
| 6 | Never | **PASS**. The hold sits, and nothing fires in two rounds. |
| 7 | Blade Watch | **PASS**. "Overwatch needs a gun in hand". |
| 8 | The Watcher | **PASS**. It declares while you're hidden; your first step into its sight draws nothing; the next one does. |
| 9 | A bookmark with a hold up | **PASS** for the hold. "Whom it has fired on" can't be saved (see below). |
| 10 | Long One | **PASS**. Interdiction puts Frail down off its cover; the Distant draws no shot. |
| 11 | Dice; regression | **PASS**. SAME17; slot 80 to 82 (81 was my step 9 bookmark), mid-fight save and load, fight won. |

## 1: Options > Gameplay

There's a new sixth row, **"Overwatch: Ask"** (`s1-gameplay`). Its text: "You declared Overwatch (your Action) and hold your shot: an enemy that moves or attacks in your sight is fired on before it acts, for one reaction (Sustained Overwatch, two enemies; Total Overwatch, three, at +2). … ASK: the game pauses and asks; No keeps the hold for the next. NEVER: hold, and never fire."

The first launch after regenerating every save sat on "reading saves…", with Continue and Load Game greyed out, for over three minutes. After that, each launch's scan took 0 to 4 s (`loads.txt`), so I haven't filed it.

## 2: Watch One, Always

- **The fight begins on load**. Order: Frail, Watcher, Gunner, Runner, Watch One. In round 1 the Runner closes to (6,7) and the others stand (`w0`).
- **w** (`w1-declare`, `w3-log`): the box reads "Overwatch — hold your shot", and the log "Watch One declares Overwatch".
  - Her hover reads "overwatch · move 5 of 5 · reactions 3 of 3" (`w3-hov`).
  - A red marker appears on her portrait (`w5-strip`).
  - The action bar's attack pip goes dim and the move pip stays lit.
  - Clicking Frail to shoot: "you have already acted" (`w4-tryshoot`).
- **w again**: "already holding your shot" (`w2-again`).
- **The initiative strip**: hovering her slot at the top shows only "Watch One" (`w6-hovslot`). "overwatch" is on the portrait's hover and marker. If "your strip" in the order means the initiative strip, it doesn't show it.
- **End Turn**, round 2 (`w7-log`):
  > Overwatch: Watch One attacks Frail : \*hit\* : (18 + 14 = 32)
  > Watch One damages Frail for 3 damage
  > Frail dies
  - Then "Watcher attacks Watch One", "Gunner attacks Watch One" and "Runner attacks Watch One" draw nothing. **One only.**
  - +14 is her attack 12 + Dexterity 2, with no penalty.
- **The hold is gone afterwards**: her hover reads "move 5 of 5 · reactions 2 of 3", with no "overwatch" (`w7-hov`).

## 3: Sustain One and Total One

- **Sustain One** (`su-log`): "Sustain One declares Sustained Overwatch". In round 2:
  > Sustained Overwatch: Sustain One attacks Frail : \*hit\* : (18 + 14 = 32) … Frail dies
  > Sustained Overwatch: Sustain One attacks Watcher : \*hit\* : (10 + 14 = 24)
  - Then "Watcher attacks Sustain One", and the Gunner and the Runner act unshot. Two different enemies, each once. Reactions 1 of 3 (`su-hov`).
- **Total One** (`to-log`): "Total One declares Total Overwatch". In round 2:
  > Total Overwatch: Total One attacks Frail : \*hit\* : (18 + 16 = 34) … Frail dies
  > Total Overwatch: Total One attacks Watcher : hit : (10 + 16 = 26)
  > Total Overwatch: Total One attacks Gunner : \*hit\* : (15 + 16 = 31)
  - Then the Runner acts unshot. Reactions 0 of 3 (`to-hov`).
  - **+2**: 16 against Watch One's and Sustain One's 14 on the same d20s. The box only keeps the round's last line, so I didn't see the term written out as "Total Overwatch 2".

## 4: Frail under Total

In the Total One round above, Frail is shot first and "Frail dies". There's no "Frail closes" line and no Frail attack, and it is gone from the board, so it went down before moving (`to-turn`). The same happens in steps 2 and 3.

## 5: Ask, Watch One

(`k1-q`, `k2-q`, `k-log`)
- Before Frail's move: "**Overwatch / Frail moves / one reaction · 3 left · No keeps the hold / 95% (needs 2+)**". **No**: Frail walks up, "Frail attacks Watch One : \*hit\* : (18 + 4 = 22)".
- Next: "**Watcher attacks** · one reaction · 3 left · No keeps the hold". **Yes**: "Overwatch: Watch One attacks Watcher : \*hit\* : (10 + 14 = 24)", then "Watcher attacks Watch One : \*miss\*".
- The Gunner and the Runner then act without a question; the one shot is spent.

## 6: Never

Watch One declares ("Overwatch — hold your shot") and ends the turn. In rounds 2 and 3, Frail, the Watcher, the Gunner and the Runner all attack or close. There's no question and no Overwatch line (`nv-log`).

## 7: Blade Watch

w: "**Overwatch needs a gun in hand**" (`bw-try`). There's no declaration line in the log (`bw-log`).

## 8: The Watcher (your Overwatch on Never)

- **Round 1**: Up, Up to (2,2) (`v1`), then End Turn.
- **Round 2**: "Frail closes…", then "**Watcher declares Overwatch**", then the Gunner and the Runner (`v2-log`).
- **Her round-2 turn** (`v3`, `v4`):
  - Down to (2,3): no shot.
  - Down again to (2,4): "**Overwatch: Watcher attacks Watch One : hit : (10 + 9 = 19)**", for 4.

## 9: A bookmark with a hold up

- Watch One declared and then saved to a slot, "bm243", slot 81 (`bm1-saved`).
- I stopped the app, relaunched it, and loaded slot 81 (`bm2-row`, `bm2-loaded`).
  - The hold is kept: her hover reads "overwatch · move 5 of 5 · reactions 3 of 3" (`bm2-hov`), and w reads "already holding your shot" (`bm3-again`).
  - End Turn: "Overwatch: Watch One attacks Frail : \*hit\* : (6 + 14 = 20)", then "Frail dies", then the Watcher, the Gunner and the Runner unshot (`bm4-log`). The hold still fires, and once only.
- **"Whom it has fired on" can't be put in a save.**
  - My hold ends at the start of my next turn, so it is only part-used during the enemies' turns, which run without stopping.
  - At an Overwatch question F4 does nothing: there's no quick save in `sustain-one.marks`, only the `.sav` touched (`bk3-f4`).
  - The Watcher holds plain Overwatch (one shot), so its hold is gone once it has fired.
  - So no save I can make holds both a hold and a non-empty fired-on list.

## 10: Long One (Tester Long), Snap Shot on Always

Round 1 (`l-logup`, `l-log`):
> Interdiction: Long One attacks Frail : critical hit : (20 + 14 = 34 : Threat Roll: 16 Automatic Hit!)
> Long One damages Frail for 11 damage
> Frail dies

That fired on Frail's step off its cover, before it struck; it never strikes. Rounds 2 to 4: the Distant's only line is "Distant: Vibroblade · out of reach — Vibroblade reaches 1 square and Long One is 26 away". There's no shot at it.

## 11: Dice and regression

- **Dice**: the right Dice One Quick Save; the first 17 lines match the TEST 206 baseline (SAME17).
- **Regression**: Icon Nine.
  - Loaded slot 80 (reg242, 19:35:46) and saved it as "reg243", which took **slot 82**: slot numbers are shared across characters, and my step 9 bookmark had taken 81.
  - A quick save mid-fight (22:01:37), then loaded slot 82.
  - Won the fight: "Icon Nine: 106 of 196", "FIGHT OVER".

## Odd, not filed

- After the bookmark load (step 9), the round-2 dice differ from a fresh load of the same save: Frail is hit on a d20 6, against 18. The fight carries on from the bookmark's own place in the dice, so I've only noted it, with the file names above for tracing.
