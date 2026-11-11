# TEST 249: The event popup, plus TEST 246's fixes

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, sample logs, the load log and the dev log of every launch are in `KOTOR_RPG_MAIN_WORK/media/screens/test-249/`; names in brackets below are files there.

## Build

- **App**: main `ac9dbd1`, a fresh clone. `gate.py --at ac9dbd1`: "FOR TESTER — CORE at ac9dbd1, 5881 tests, 0 failed".
- **Lodestar**: `2c2fb92` compiled into both the app and Loom. **Loom**: `d3004d6`, a fresh clone.
- **Settings**: defaults at the start. **Shelf**: `9c28184`, check_shelf clean.
- **Beds**: the tries, death and test208 save tools rerun with no errors.
- **Restore copy**: every `.sav`, plus `.marks` for dice-one and icons-185 only. Before each load I restored the `.sav` (and `.marks` where the copy has one) and logged the md5s (`loads.txt`).
- **Dev log**: my load helper copies `app.log`, the app's terminal output for that launch, into `devlog/` before it stops the app. The names show the time and the save that came next.
- My session restarted once, after the SAME17 run. I restarted my Xvfb `:2` and reran the dice and regression on the same build.
- Every step ran on `ac9dbd1`.

## Summary

Two findings: no popup at a fight's end even when it awards XP (A), and the Item(s) Received row has a missing glyph and runs past the popup's right edge (A). D's end line names the downed companions but not the Brute.

| # | Check | Result |
|---|---|---|
| A | Reward conversation | **PASS**, with **FINDING 2**. One popup on the board: "Journal Entry Added" and "Item(s) Received". |
| A | No popup in a fight; XP at its end | **FINDING 1**. Nothing during the fight, but nothing at the end either, with 75 XP awarded (twice). |
| A | Store buy and sell | **PASS**. No popup. |
| A | Medpac outside a fight | **PASS**. No popup. |
| A | Status Summary off, then Default | **PASS**. Off: nothing pops. Default turns it back on. |
| A | Credits row | **NOT RUN**. No package on the shelf gives credits in a reward. |
| B | Death Normal, four loads | **PASS**. The same "fight opens:" line and the same order all four times. |
| C | Death Bare treat | Noted: "stabilized — no longer bleeding out". |
| D | Death Hard end line | **Differs from the order**: "Keeper falls", not "Brute and Keeper fall". Mate is left out. |
| E | Destroyed footlocker's menu | **PASS**. Inside its frame, Search visible. |
| F | Proof Immune, Easy and Normal | **PASS**. Easy: force 239 of 239 after the win. Normal: 189 of 224 (max 239). |
| G | "you have already acted" | Not seen after a single click in this test. |
| H | Regression | **PASS**. Log out.; the pulse rest (CPU 0.0); Loom delete; SAME17; slot 88 to 89, fight won. |

## A. The event popup

**Reward conversation** (Tester Mines, Mine Two, the quartermaster at (1,3)):
- "Spikes and a repair part, if you have them.", then [Leave.]. Back on the board, one popup (`a-pop2`):
  - "Journal Entry Added"
  - "Item(s) Received: Security spike, Security spike, Security spike, Security spike, Repair part"
  - OK
- **FINDING 2**: in the Item(s) Received row, a missing-glyph box sits between "Received:" and "Security spike". The row also runs past the popup's right border: the border is at about x 1345, and the text ends at about x 1540 (`a-pop2`).
- **The Credits row**: no package on the shelf (9c28184) gives credits in a conversation or holds them in a container, so I couldn't show it. It needs a bed.

**Status Summary**: Options > Feedback has a fourth row, "Status Summary", ticked by default (`a-feedback`).
- Unticked: settings.json reads `"statusSummary":false`. I reloaded Mine Two (restored) and took the quartermaster's supplies again: nothing popped (`a-off1` to `a-off4`). Talking to him again offered only "Nothing, thanks.", so the reward was given.
- Default: `"statusSummary":true` again.

**In a fight, and at its end** (Status Summary on):
- Death Normal: nothing popped during the fight or when it ended (`a-end1` to `a-end6`). That fight awards 0 XP (the sheet's Experience reads 0), so that was expected there.
- **FINDING 1**, the Icon Nine regression fight. Slot 89 (saved just before the fight) reads Experience **66000**. After the win it reads **66075**, so the fight gives 75 XP. No popup appeared at the end:
  - in the regression run (`reg-end`);
  - in a replay from slot 89 with frames every half second for 5 s after the last blow (`xp-end1` to `xp-end10`, unchanged).
  - My fight script presses nothing after its last attack: it stops when End Turn goes, and the screenshots follow.

**Store** (Store Bed, Boot Rich, Dressa): bought a Medpac (credits 37600 to 37560) and sold Sith Trooper Greaves (to 38055). Closing the store and leaving the conversation: no popup (`s-board1` to `s-board5`).

**Medpac outside a fight** (Mine Two, 8 of 11): Inventory > Medpac > Use Item. The box reads "Medpac — 11 of 11 (was 8) · 1 left", and there's no popup (`m2-board1` to `m2-board3`).
- The first Use Item click came while a tutorial popup ("The INVENTORY screen shows a list…") was showing. The medpac was used then, with nothing on screen to say so. The next click said the character is at full health.

## B. Death Normal, four loads

The same restored file each time (md5 `d95273c4` before each load, no `.marks`; `loads.txt` lines 1 to 8). The dev log's line is the same all four times (`devlog/b-load1.log` to `b-load4.log`):

> fight opens: seed 1874682765, 0 dealt, rolling Death Normal, brute.death.01, mate.death.01, keeper.death.01

The status row reads Brute, Mate, Death Normal, Keeper all four times (`b-load1` to `b-load4`). A fifth load later in the test (line 23) opened the same way.

## C. Death Bare treat (noted, not filed)

Mate at -1, my turn, t, 1: "treat Mate — d20 8 + Medicine 0 = 8 · stabilized — no longer bleeding out", and Mate is at 0 (`c-treat`).

## D. Death Hard

- Mate reaches -10 at my 15th End Turn, and the log reads "Mate dies" (`d-log`).
- I shot the Brute twice. The box reads "Keeper: 1 of 12 — in your campaign, a01 left you at -10 · revived at 1", then "**Keeper falls** — Blaster Pistol · rolled 13 … -8 left … dies" (`d-s2`).
- The dead Mate is left out, as wanted. But the line names only Keeper, not "Brute and Keeper fall" as the order expects.
- On Death Normal (A's fight) it reads "**Mate and Keeper fall** — Blaster Pistol …", the two downed companions, and again no Brute.
- The Icon Nine win now reads "it is over — unarmed …" where TEST 248's read "Gunman and Gunman and Gunman falls".

## E. The destroyed footlocker's menu

Tries Hard: "open lock — d20 5 + Security 4 = 9 vs 40 (legendary) · the lock is destroyed". I right-clicked the footlocker near its bottom edge (1002,525). The menu opens upward and stays inside its own frame. It lists Examine (Science), the two refused Open Lock entries with K2's line, and **Search (Awareness)** at the bottom (`e-menu`).

## F. Proof Immune

The foes are at 30 vitality each.
- **Easy**: Force Push on the Thug ("6f — 239 > 233 · ceiling −1 to 238"), then two Force Waves ("22f … ceiling −7"). The second ends it: "it is over — Force Wave …". After that the box reads "**force 239 of 239**", so the bar and the ceiling are both full (`f-push`, `f-w1`, `f-w2`).
- **Normal**: the same casts, and after the win the box reads "**force 189 of 224 (max 239)**" (`fn-win`).
- Neither fight brought a popup.

## G. "you have already acted"

I didn't see it after a single click in this test.

## H. Regression

- **Log out.**: Tries Hard console (2,0): "1 Read the yard log. 2 Log out.", and 2 logs off to the board (`h-console`).
- **The pulse rest**, on the package menu: Continue breathes, then holds at 201 from about 31 s (`h-pulse.txt`). CPU after: 0.0 in all 13 samples (`h-cpu.txt`).
- **Loom delete** (Loom `d3004d6`, a copy of Tester Death): Mate "stays down" adds her exception. Deleting Mate leaves package.toml naming her nowhere, and Verify reads "Tester Death · No problems found." (`h-deleted`, `h-verify`).
- **Dice**: the right Dice One Quick Save; SAME17.
- **Regression**: Icon Nine. I loaded slot 88 (reg248) and saved it as "reg249", which took slot 89. Then a quick save mid-fight, a load of slot 89, and the win: "Icon Nine: 107 of 196" (`dicereg.out`).
  - My first run stopped at the load list, because OCR read "88" as "8S". I widened the match and reran.

## Odd, not filed

- The character sheet's portrait covers the alignment bar's labels (`a-sheet`).
- A save made with F4 also writes an Auto Save. After the Icon Nine win there is an Auto Save at 07:36:32, the time of the win.

## What I got wrong

- In the Death Normal fight for A, my first two clicks on where I thought the Brute stood walked me to that square instead, because the Brute had moved. I found it and shot it on the next turns.
- I first tried the medpac on Boot Rich, who was at full health, and the first quick slot I clicked was the shield, not the medpac. I redid it on Mine Two.
