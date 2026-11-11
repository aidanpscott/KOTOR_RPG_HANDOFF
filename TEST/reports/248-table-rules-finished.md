# TEST 248: Difficulty and Table Rules finished (TEST 247's steps on this build)

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, sample logs and the load log are in `KOTOR_RPG_MAIN_WORK/media/screens/test-248/`; names in brackets below are files there.

TEST 247 was not filed separately. As the order says, I ran its steps on `d099c6d`, changed by TEST 248's B and C.

## Build

- **App**: main `d099c6d`, a fresh clone. `gate.py --at d099c6d`: "FOR TESTER — CORE at d099c6d, 5869 tests, 0 failed".
- **Lodestar**: `2c2fb92` compiled into both the app and Loom. **Loom**: `add550e`, a fresh clone.
- **Settings**: defaults at the start. **Shelf**: `05afcfa`, check_shelf clean ("33 rules files and 128 standard blueprints, all identical").
- **Beds**: `author_tester_tries_saves.dart` rerun with no errors. The other saves are from TEST 246's full regeneration.
- **Restore copy**: every `.sav`, plus `.marks` only for dice-one and icons-185 (the regression chain). After TEST 246 I no longer copy leftover `.marks` from earlier tests.
- **Loads**: before each `.sav` load I deleted its `.marks`, copied back the `.sav` (and `.marks` where the copy has one), and logged the md5s before the load (`loads.txt`, `BEFORE` lines).
- The machine rebooted partway through (after C's Equip row, before the nav bar recheck). I restarted my Xvfb `:2` and relaunched the same build; nothing else changed.
- Every step ran on `d099c6d`.

## Summary

One finding: a mouse move doesn't wake the nav bar's focused icon (a key does). Everything else passes.

| # | Check | Result |
|---|---|---|
| C1 | Package menu, Continue | **PASS**. Stops at 30.5 s, held bright; CPU 0.0 over a minute; mouse and key wake it. |
| C2 | Equip, the selected row | **PASS**. Stops at 29.4 s, held bright; CPU 0.0; mouse and key wake it. |
| C3 | Nav bar, the focused icon | **FINDING 1**. Stops at 29.4 s, held bright, CPU 0.0, a key wakes it; a mouse move does not, unless the pointer goes onto the icon. |
| B | "Log out." | **PASS**. Tries consoles and the strongroom console end with "Log out."; its number logs off. |
| 247 B | Tries Hard consoles | **PASS**. (0,0) one session; (2,0) two, lockout line at the second log-off, third refused; (0,2) opens every time; still refused after a quick-save reload. |
| 247 C | Tries Normal consoles | **PASS**. (0,0) twice and (2,0) three times, each opens, no lockout line. |
| 247 D | Loom, Tries copy | **PASS**. "marked" 1; + gives 2; − twice stays 1; "no limit" hides the count; container drops the row; the area reopens; Verify clean. |
| 247 D / 248 D | Loom, Death copy | **PASS**. "stays down" adds Mate's `[[death_exception]]`, "dies" removes it; stays down then delete Mate: package.toml no longer names her, Verify clean; deleting the Brute leaves package.toml unchanged. |
| E | Regression | **PASS**. Tries Hard locks and mine as in TEST 246; Table Rules Death row and blurb; dialogue leave row "[Leave.]"; SAME17; slot 86 to 88, fight won. |

## C. The idle pulse

I sampled the brightest pixel in a box every half second (`pulse*.txt` files), and the app's CPU with `top -b -d 5 -n 13` (13 samples over a minute) after each stop.

**C1, the package menu** (Tester Tries, 5 saves, Continue lit):
- After one mouse move, Continue's border breathes between 64 and 201, about every 6.5 s. At **30.5 s** it stops at 201, its brightest, and holds there to 60 s (`c1-pkg-pulse.txt`).
- CPU after the stop: **0.0** in all 13 samples (`c1-pkg-cpu.txt`).
- A mouse move: it breathes again at once (`c1-mouse.txt`). After another rest, a key: it breathes again (`c1-key-a2.txt`).
- Two key tries didn't wake it, and both were my tooling. `xdotool key --window` sends synthetic events, which the app ignores, and Shift that way did nothing. A real key event through my usual key helper woke it.

**C2, Equip, the selected row** (Tries Normal, Equip, the right weapon slot selected, so "Blaster Pistol (Equipped)" is the selected row):
- The row's border breathes between 113 and 194. At **29.4 s** it stops at 194, held bright, to 45 s (`c2-row-rest.txt`).
- CPU after the stop: **0.0** in all 13 samples (`c2-row-cpu.txt`).
- Mouse moves anywhere on the screen wake it (`c2-row-mouse.txt`), and so does a key.
- My first CPU run showed 0 to 12.8%. I took it while the row was still breathing: my box then included the row's text, so it couldn't see the border. The clean run above is all zeros.

**C3, the nav bar's focused icon**:
- On Equip, the icon breathing is the nav bar's second icon (Inventory), once I've pressed Down. Opening Equip by its icon, nothing in the nav bar breathed until that key press (`c2-down`).
- It breathes between 106 and 148. At **29.4 s** it stops at 148, its brightest, to 40 s (`c3-nav-rest.txt`).
- CPU after the stop: **0.0** in all 13 samples (`c3-nav-cpu.txt`).
- A key wakes it.
- **A mouse move does not.** Four moves across the screen, before and after the reboot, left it at 148 (`c3-nav-mouse.txt`, `c3-nav-mouse2.txt`). Moving the pointer onto the icon itself does start it breathing. On the same Equip screen, the same mouse moves woke the selected row. That's **FINDING 1**: the order says each of the three wakes on a mouse move or a key.

## B. "Log out." and TEST 247's B (Tries Hard)

Slice opens the yard console's screen: "1 Read the yard log. 2 Log out." (`b1-screen`).

- **(0,0), one session**: Slice, then Escape. The box reads "**This object cannot be opened through conventional means.**" (`b1-esc`). Right-click again: "Slice (Slicing) — This object cannot be opened through conventional means.", greyed (`b1-menu2`). Clicking it puts only that line in the box, and no screen opens (`b1-again`).
- **(2,0), two sessions**, leaving each time by pressing 2 ("Log out."):
  - Session 1 opens. Log out: no line, the box shows only the name (`b2-off1`).
  - Session 2 opens. Log out: "**This object cannot be opened through conventional means.**" (`b2-off2`).
  - The third try is refused: no screen, and the same refused line (`b2-off3`).
- **(0,2), unmarked**: three sessions, each opens, and Log out gives no line (`b3-s1` to `b3-off3`).
- **Quick save and reload**: F4, then I loaded that Quick Save (21:05:59). (0,0) and (2,0) both show the refused Slice entry; (0,2) still offers Slice (`b4-c00`, `b4-c20`, `b4-c02`).
- **The strongroom console** (Tester 208, Proof Locks): "1 [Slicing] Unseal the vault door. (3 spikes) — you have 0 spikes / 2 [Slicing] Cycle the corridor lights. (1 spike) — you have 0 spikes / **3 Log out.**" Pressing 3 logs off to the board (`b5-screen`, `b5-off`).

## TEST 247's C (Tries Normal)

(0,0) twice and (2,0) three times: each opens "1 Read the yard log. 2 Log out.", and each Log out gives no line (`cn-c00-1` to `cn-c20-off3`).

## D. Loom, on copies

I copied Tester Tries and Tester Death to `kotor-rpg/loom248/` and opened those, so the shelf's own copies weren't touched.

**Tries copy, console.tries.06 (0,0)** (`d1-c00`). The row reads "on Hard, slicing sessions · no limit · **marked** − 1 +". The file follows each click:

| Click | Row | `hard_sessions` in a01.toml |
|---|---|---|
| (start) | marked − 1 + | 1 |
| + | marked − 2 + | 2 |
| − | marked − 1 + | 1 |
| − | marked − 1 + | 1 |
| no limit | marked (no count) | line gone |

- Back to marked (1), then **kind: container**. The sessions row is gone; the panel reads "can be searched, and can be locked … holds nothing". In the file, `kind = "container"`, and `hard_sessions` and `conversation` are gone (`d1-container`).
- The a02 tab, then a01 again: the area opens with the container in place (`d1-a02`, `d1-reopen`). Verify: "Tester Tries · No problems found." (`d1-verify`).

**Death copy, mate.death.01** (`d2-mate`). The row reads "on Normal and Hard · **dies** · stays down".
- "stays down": package.toml gains `[[death_exception]] character = "mate.death.01" instead = "down"` below Keeper's (`d2-staysdown`). "dies": it's removed (`d2-dies`).
- **TEST 248 D**: stays down again, then delete Mate. package.toml names Mate nowhere, and only Keeper's exception is left. Mate is gone from `areas/a01.toml` and the board (`d2-deleted`).
  - The status bar then reads "mate.death.01 can die", not a delete message.
  - Verify: "Tester Death · No problems found." (`d2-verify`).
- **Control**: delete brute.death.01, which has no exception. package.toml's md5 is `08952930` before and after, which is also the file as copied. The Brute is gone from a01.toml (`d2-brute-deleted`).

## E. Regression

- **Tries Hard's marked locks**, from the reloaded quick save:
  - The door: "open lock — d20 6 + Security 4 = 10 vs 40 (legendary) · This object cannot be opened through conventional means."
  - The footlocker below: "d20 8 … = 12 vs 40 (legendary) · the lock is destroyed".
  - The mine twice: "vs 40 (legendary) · it is still live" (`e-door`, `e-foot`, `e-mine1`, `e-mine2`).
- **The consoles**: B and TEST 247's B and C above.
- **Table Rules**, in game (Icon Nine):
  - "Difficulty: Normal, Death: Same as Difficulty". Clicking the words changes nothing; + gives "Death: Easy"; − goes back to "Same as Difficulty" (`e-rows`, `e-label`, `e-plus`, `e-back`).
  - The Options blurb: "The table's rules: the difficulty, death, and the reactions" (`e-blurb`).
- **Dialogue leave rows**: the Envoy's Goodbye leads to "Envoy: Safe travels." with "1. [Leave.]" (`e-env-bye`).
- **Dice**: the right Dice One Quick Save (Oct 19, 07:40:30); the first 17 lines match the baseline (SAME17).
- **Regression**: Icon Nine. I loaded slot 86 (reg246), saved it as "reg248", which took **slot 88** (87 is my TEST 246 bookmark), quick-saved mid-fight, loaded slot 88, and won: "Icon Nine: 87 of 196", "FIGHT OVER" (`dicereg.out`, `reg-end`).

## Odd, not filed

- After deleting Mate in Loom, the status bar reads "mate.death.01 can die" instead of naming the delete.
- On opening Equip, no nav icon breathes until a key moves the focus. The icon that then breathes is Inventory's, not Equip's.

## What I got wrong

- Two key presses on the package menu went through `xdotool key --window`, which the app ignores; the real key press woke it. My first Equip CPU run was taken while the row was still breathing. Both are redone above.
- Loom's file dialog garbles a typed path (its autocomplete races my typing), so I moved the Loom copies to `kotor-rpg/loom248/`, which is one click from where the dialog opens. They're my own copies and aren't on the shelf.
