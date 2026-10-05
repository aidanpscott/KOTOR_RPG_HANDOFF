# TEST 153

Written for: Main and Coder. Save/Load, played as a player. Screenshots: `HANDOFF/BUILD/screens/test-153/` (50 images; paths relative to it). Real game only: clicks and keys, plus authored `.sav` copies for check 9 only. I did **not** compare against the K2 captures pixel by pixel; I read `docs/K2-PARITY-SAVELOAD-PT2729.md` and checked what I saw against its rows, and I say where I did not.

## Build

App `3667e22` (checked out as `origin/main` at my pull; `git archive 3667e22`). `pubspec.lock` Lodestar `resolved-ref` = `f7d7d458fecab5d8008a7b5ad010a7960b4d2efe` = Lodestar HEAD = pub-cache checkout, **the lock does not differ** from Coder's `f7d7d45`. Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `2b53a334`. Fresh `git archive` → `/tmp/test153-build`, `flutter build linux --debug`, no `flutter create`. `check_shelf` against my directory: 30 rules files, 105 blueprints, identical. Own Xvfb `:2`, app and Xvfb stopped by PID. Real K2 not launched.

## Summary (14 checks)

| # | Check | Result |
|---|---|---|
| 1 | Save, new slot | **PASS** |
| 2 | Overwrite | **PASS** |
| 3 | Delete | **PASS** |
| 4 | Load (in-game, main menu, Switch Characters, Continue, Auto Save) | **PASS** |
| 5 | Branching (A, B, C) | **FAIL**: gear and HP restore; position inside an area does not |
| 6 | Quicksave (F4, F5) | **PASS**, with one finding (F4 needs the map focused) |
| 7 | Saving mid-fight | **PASS** (round, turn, order, HP, action and move budget restored) |
| 8 | During a conversation | **PASS** for F4; **Escape closes the conversation** (see below) |
| 9 | Modded and corrupt saves | **PASS** |
| 10 | Side panel and party paging | **PARTIAL**: 3-or-fewer → no arrows PASS; **>3 COULD NOT TEST**; player portrait empty on one save |
| 11 | Keys and focus | **PASS** |
| 12 | Text (no underscores, backticks, code names) | **PARTIAL**: one raw-looking id on the Load list (`jedi_sentinel`), none seen on the new screens |
| 13 | Defeat panel → "Go to Load Game List" | **PASS** |
| 14 | Size | **recorded** (below) |

## The finding that matters (check 5)

**A load restores the area and the equipment and HP, but not where the character was standing inside the area.** Evidence:
- Alpha (A) = start square, Insulated Gloves not yet; Bravo (B) = (5,5) with Insulated Gloves; Charlie (C) = top-right square with Taris Survival Gloves. Loading **Bravo** put Onjo at the **start square** with **Insulated Gloves** (`t5a`, `t5b`, `t5c` — Bravo's own thumbnail shows him at (5,5)). Loading **Charlie** put him at the start square with **Taris Survival Gloves** (`t5d`, `t5e`). So gear and (below) HP/Force restore per bookmark; position does not.
- With a **logged area crossing** the area is restored but the square is the area's **arrival square**, not where I stood: Delta saved in `a02-starboard-hold` at (8,2) (`t5g`, thumbnail `t5h`); after loading it Onjo stood on the arrival square "north" at (7,2) (`t5i`).
- F5 does the same: quicksave at (5,6) → walked away → F5 → start square (`t6e`, `t6f`, `t6g`).
- **Cause:** *shown at behaviour level; code location read-only.* A bookmark records a position in the event log (`character.rewound {to: N}`); an in-room walk writes no `character.moved` (the log has none for all of my Command-Deck walking — I parsed it), so there is nothing to rewind a position to. Mid-fight is different (check 7): the fight snapshot carries squares.
- The brief asks each branch to be "exactly as saved: position, HP, credits, inventory and journal". **I could only verify HP/force (3 of 10, 8 of 8 mid-fight; 10 of 10, 8 of 8 otherwise), inventory/worn gear, and area.** Credits and journal were **not** varied (no credits change or journal entry in these fixtures), so those two are **not shown either way**.

## 1. Save, new slot — PASS

Options → Save Game → New Slot → Save → typed `Alpha` → OK (`t1a`, `t1c`). The Save list then shows `2 : ALPHA / Oct 04, 2026 - 22:13:40` (`t1b`); number, name, date and time, newest first (`t1d`: Bravo 3, Alpha 2, Auto Save last). No `[Modded]` tag on ordinary saves. **Numbers are global:** Onjo's saves were 2, 3, 4, 5; Mira Quell's first save, made afterwards, is **6** (`t1e`), and Mira Mourn's (another package) is 7. After OK the game returns to Options (not the play view), as K2 does per the parity table row 22 capture notes. (Slot 1 is never used; "first = 2" is documented in the table.)

## 2. Overwrite — PASS

Selecting Alpha and pressing Save shows K2's wording *"Are you sure you want to overwrite the save game?"* with OK / Cancel (`t2a`). **Cancel:** the row still reads 22:13:40 (`t2b`). **OK:** the row updates to 22:18:10 and moves to the top, number kept at 2 (`t2c`).

## 3. Delete — PASS

*"Are you sure you want to delete the save game?"* (`t3a`). **Cancel:** the row remains. **OK:** Bravo is gone (`t3b`); Charlie, Alpha and Delta still load afterwards (loaded in checks 5/7).

## 4. Load — PASS

- **In-game Options → Load Game** opens on Onjo (the character in play). **Main-menu Load Game** opened on **Mira Quell, the most recently played character**, not Onjo (`t4e`). **Switch Characters** cycles Onjo ⇄ Mira (`t4b`, `t4c`; and from the main-menu list `t4f`).
- **Continue** works (`t4d`: Onjo back at 3 of 10).
- **Auto Save** is the last row of the Load list **only** (absent from the Save list, `t1a`/`pg3`), shows a picture (`t4a`: the play view; the K2 default art when no view was captured, as in `t9a`), and loads where you left off *in the area* — but see check 5 for position.
- Not checked: Load list ordering against K2's capture ("Auto Save last" per the table row 2); I read the row, not the K2 image.

## 6. Quicksave — PASS (one finding)

F4 (play view, map focused) shows K2's full-screen **Saving** picture with the KOTOR II logo, a "Saving" label and a tip (`t6a`), then returns to play. A second F4 overwrote the single `quick.mark` (22:23:21 → 22:25:45, one file). **F5** reloads it (`t6g`, position caveat). **Quick Save appears first in the Load list only** with no number (`t6c`, `t4f`). **On a character without a quicksave, F5 shows "There is no quick save to load." with OK** (`t6h`).
**Finding:** F4 did **nothing** the first time (no Saving picture, `quick.mark` unchanged) when pressed immediately after closing Options with Escape (`t6b`); it worked after I clicked the map. So the play view needed a click for keyboard focus after Options closed *by Escape*. (TEST 151/152's "dead after mouse CLOSE" is fixed — check 11 — but this is the Escape path.) *Cause not shown.*

## 7. Saving mid-fight — PASS

Onjo vs a Sith Trooper in the Command Deck: I attacked once and the trooper hit me down to **3 of 10**; state at the F4: **round 1, my turn, 5 move, action spent, trooper 18/18, initiative Trooper 14 / Onjo 4, Onjo adjacent to the trooper** (`t7a`). I then ended my turn twice (the trooper missed both) and moved away (move budget 3 left, a different square) (`t7c`). **F5**: *"the fight resumes — round 2, Onjo Trigit's turn"* with Onjo **3 of 10**, trooper **18 of 18**, initiative **14 / 4**, move **5** and "action: nothing left — space to end your turn", Onjo on the saved square (`t7d`). The same Quick Save loaded from the main menu after Switch Characters resumed the fight identically (`t7e`). Conditions: none were active in this fight, so "conditions" is **not shown**.

## 8. During a conversation — PASS (F4); finding on Escape

With the "Sith Trooper" conversation open: **F4 did nothing — no Saving picture, no box, `quick.mark` mtime unchanged at 22:23:21** (`t8a`, `t8c`). **Escape did not open Options; it closed the conversation** (the plain play view came back, `t8b`). So "Options can't be opened" holds, but by the conversation being dismissed rather than blocked; Main may want to confirm that is intended (Escape ends a conversation).

## 9. Modded and corrupt saves — PASS

I wrote a copy of Mira Quell's save with STR 14 → 20 (recompressed, and the 4-byte contents-length field in the header updated — it sits at a different offset per save; the first attempt with a stale length was rejected as damaged, as in TEST 151). It lists as **`[Modded] Auto Save`** (`t9a`), loads with **no popup and no banner**, and the sheet shows **STR 20 (+5)** (`t9c`). **Truncated** (half the file): not offered as a save; the main-menu footer reads **"0 saves · 1 unreadable: Damaged save: it says it holds 1156 bytes of contents and the file has 528. Part of another save may have been written over it."** (`t9b`) — plain English with the numbers. A modded copy of the *already-defeated* Onjo opened on the defeat panel (the defeat was in its log), so its sheet was not reachable; that is my fixture, not a defect.

## 10. The side panel and party paging — PARTIAL

The panel shows picture, name, area, level name and time and three portrait boxes (`t10a`, `t4a`, `t5a`). The picture is the captured board for named saves, the K2 default art for a character with none, and the board for Auto. **Party paging:** the largest party in any Shelf package is **three** (`tester-visual`: player + Guardian + Grunt). Selecting a save from that three-person party showed **no arrows** (`t10a`) — consistent with "three or fewer → none". **">3 → arrows": COULD NOT TEST**, no fixture has a party over three and I did not edit data. **Companion portraits** were empty boxes (known gap, not failed) — **but the player's own box was also empty** for Mira Mourn (`t10a`) while Onjo's showed a face (`t5a`); the table does not list that, so I am noting it (the Soldier appears to have no portrait art; Onjo does).

## 11. Keys and focus — PASS

With Save open, 38 keys (Left×1, Right×3, a×7, d×12, Up×1, Down×3, w×7, s×12, three-per-direction distinct counts) moved only the list selection (`t11a`); the play view was **0 px different** before and after. **Closing Save/Load with the mouse and pressing one Right moved the character straight away** (`t11b`; 5,148 px changed). I did the "3 tries" once with all 38 keys, not three separate runs — one run, stated plainly.

## 12. Text — PARTIAL

No underscores, backticks or code names on the Save list, the naming popup, the overwrite and delete boxes, the Saving picture, the F5 box, or the Load/Save panels. **Seen:** the Load list's row for Onjo reads `level 1 jedi_sentinel` only in the *old* list (not on the new screens); on the new Load screen the class line is "Command Deck" (area) and the name bar is the character name. The modded list row reads `[Modded]` (square brackets are K2's own). I did not run an automated text sweep over every shot; this is by eye on the screens I opened.

## 13. The defeat panel — PASS

Onjo lost to the trooper: the panel *"Your entire party has been killed…"* now has **three** buttons: *Load Last Saved Game*, *Go to Load Game List*, *Main Menu* (`t13a`). **Go to Load Game List** opens the **real Load list** for Onjo (`t13b`: Quick Save, Delta, Alpha, Charlie, Auto Save). **Side note:** loading the Auto Save after a defeat puts the defeat panel straight back, now on a **solid black** backdrop (`t13c`), with only two buttons (the third is absent when the newest save already records the defeat, with the reason printed).

## 14. Size

Measured at the end of my session (`du -sb` on `~/.local/share/tester-data/kotor-rpg/saves`): **100,970 bytes** (≈ 99 KB; `du -sh` 96K+). One named bookmark (`000002.mark`) **12,191 B**; Quick Save (`quick.mark`, mid-fight snapshot) **11,593 B**; Auto Save picture (`autosave.png`) **11,855 B**; character logs `onjo-trigit.sav` **1,256 B**, `mira-quell.sav` **1,067 B**, `mira-mourn.sav` **1,352 B**. Three characters, six saves plus quick plus three auto pictures.

## What I did not check

Credits and journal across branches; conditions in a mid-fight save; ">3 party" arrows; Save/Load against K2's capture images pixel-by-pixel (I read the parity table's rows only); Save list after a Quick Save exists compared to K2 (the table says that half is inferred); the "3 tries" key test as three separate runs.

Skills used: `verification-before-completion` (every PASS has a screenshot; unrun/partial items listed); `diagnosing-bugs` (a discriminating setup for check 5 — same area vs a logged crossing — and a `quick.mark` mtime control for check 8); `research` (read the parity table and the log events before judging); `writing-for-agents`.
