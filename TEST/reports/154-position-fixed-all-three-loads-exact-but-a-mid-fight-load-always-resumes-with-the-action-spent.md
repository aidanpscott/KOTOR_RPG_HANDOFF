# TEST 154

Written for: Main and Coder. Re-run of TEST 153's failure and partials. Screenshots: `HANDOFF/BUILD/screens/test-154/` (42 images, paths below relative to it). Real game only: clicks and keys on Xvfb `:2`, K2 not launched. The only non-game steps are fixture authoring, listed under "Fixtures I made".

## Build

App `origin/main` = `051728c8544d45cbda520e51e911563ba804ed14` (`git archive 051728c` into `/tmp/test154-build`, `flutter build linux --debug`, no `flutter create`). `pubspec.lock` Lodestar `resolved-ref` `6c02a42281c119ea0564359f7b14a05c98abf6e0` = Lodestar HEAD = the pub-cache checkout the binary was built from (read from `.dart_tool/package_config.json`) = Coder's `6c02a42`; no difference. Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `cbd54428`, HANDOFF `7c01a7f` at pull. `check_shelf` against my directory: 30 rules files, 105 standard blueprints, all identical. App and Xvfb stopped by recorded PID.

## Summary (7 checks)

| # | Check | Result |
|---|---|---|
| 1 | Position (153's FAIL) | **153's FAIL is FIXED** (square, HP, credits, journal, hostility, dead creatures, door: all exact on A, B, C). **One new FAIL:** a mid-fight bookmark (B) resumes with the **action spent** although it was saved with the action available. Facing and a poison-type condition could not be observed (see below). |
| 2 | Quick Save and Auto Save positions | **PASS** (F4/F5, Continue, and the Auto Save row of the Load list) |
| 3 | World state | **PASS for a door** (open stays open, closed stays closed). A hidden character was **COULD NOT TEST** (not run). Hostility seen restored on B only. |
| 4 | F4 after Escape | **PASS, not reproduced** (3 variants incl. the exact 153 sequence). Steps listed. |
| 5 | Party of more than 3 | **PASS** for arrows and paging (3 + 2, back). "Player first" cannot be read from the fixture's stock faces; see note. |
| 6 | Player's portrait | **PASS** for male and female (default by gender on a new save). Old bookmark stays empty as expected. Auto Save row's panel still has no portrait. |
| 7 | Quick regression | **PASS** for save, overwrite, delete, load, F4 in a conversation. Mid-fight resume **FAIL for the action budget** (same defect as 1). |

## 1. Position — 153's FAIL fixed; one new FAIL (action budget)

Fixture: my local package `tester-save-bed` (12×8 room: merchant Dressa at (3,3), Sith Trooper at (9,5), a door at (6,1) that **stays in the room**, arrival (1,1)) with Onjo (authored with the app's own tool). Readouts: the status line prints `a01-bed · x, y` while you walk; credits from Inventory; journal from the Journal tab; HP and force on the party card. I took the Inventory, Character and Journal tab after each load and compared them to the same tab at save time **pixel for pixel**.

| | A (bookmark 9) | B (bookmark 10) | C (bookmark 11) |
|---|---|---|---|
| square | **(2,3)** (arrival was (1,1)) | **(4,2)** | **(5,1)** |
| credits | 100 | **0** (bought a 100 cr Vibroblade) | 0 |
| journal | none | **A Debt Outstanding** (quest reply to the merchant) | same |
| HP / force | 10 of 10 / 8 of 8 | **9 of 10** (Dressa hit for 1) / 8 of 8 | 9 of 10 / 8 of 8 |
| creatures | trooper alive, Dressa alive | trooper dead; **fight on** (round 5, Onjo's turn, Dressa 20 of 20 and hostile) | trooper dead, Dressa dead |
| door at (6,1) | closed | closed | **opened** |
| move / action | not in a fight | **4 move, action available** | not in a fight |

Loaded in the order B, C, A, then each again where noted:
- **A** (`t1k`): play view **pixel-identical** to the view at save time (`t1j`) except the status-line text; credits 100, sheet and journal tabs identical (re-loaded twice, identical both times).
- **B** (`t1h`): square (4,2), 9 of 10, Dressa 20 of 20, round 5, **4 move** — all as saved. Credits 0, sheet and journal tabs identical to B at save time.
- **C** (`t1l`): square (5,1), 9 of 10, Dressa gone, loot icon in place; board pixel-identical to C at save time; credits/sheet/journal identical.
- **FAIL — the action budget.** B was saved with the action circle bright (`t1f`: `4 move`, action available). After the load it is dim with *"⟩ nothing left — space to end your turn"* (`t1h`; side-by-side crop `t1i`). Reproduced three more times, so I also did a **discriminating control**: (a) F4 at the start of a fight, round 1, **5 move, action available** (`t7d`); I then attacked (action spent, Dressa 15, `t7e`) and pressed F5 → round 1, Dressa **20 of 20**, 5 move (all as saved) but **action spent** (`t7f`); (b) I ended my turn so the **live** action was available again (`m5`), pressed F5 → **spent** again (`t7g`). So the restore does not copy the live value and does not copy the saved one: **the action budget comes back spent every time** (4 observations: B bookmark, B quick save, round-1 quick save, live-available control). Move is restored correctly. *Cause not shown;* likely the combatant restore sets the action spent (or a new-turn flag is not reset). In 153 this was invisible because the fight I saved had already spent the action.
- **Facing: COULD NOT OBSERVE.** I turned by walking (A: arrived moving east; B: last move north; C: last move east), but nothing on the screen shows which way anyone faces (no arrow, no text). I cannot say it was or was not restored.
- **Condition: wound only.** The only damage source in my fixture is an unarmed merchant (1d3), so the condition shown is HP 9 of 10. A poison/effect type condition was **not exercised** (the bookmark carries it per Coder's table; I did not see it).
- Trooper corpse/loot icon: on C the trooper stays dead (loot icon in place); on A it is alive again, as saved.
- Bookmark sizes (bytes): A 13,089 · B (mid-fight) 13,267 · C 12,223 · Quick Save (mid-fight) 13,202. Budget 65,536.

## 2. Quick Save and Auto Save positions — PASS

- **Quick Save.** F4 from (5,1) (A-world, door closed, 10 of 10), then Left×2, Down×1 to (3,2) (a conversation with the merchant was open when I pressed F5), **F5 → back on (5,1)**, door still closed, board identical to the F4 moment (`t7b` before, `t7c` after).
- **Continue.** Standing on (8,5) after killing the trooper (`t2b`), Options → Leave Session → package menu → Continue → **(8,5)** again, the loot icon where it was (`t2c`).
- **Auto Save row of the Load list.** Standing on (5,3) (`t2f`), Leave Session, Load Game, click the **Auto Save** row, Load → **(5,3)** (`t2e`; its thumbnail `t2d` shows the ring on (5,3)). The Auto Save is written beside its picture (`autosave.world.json` on disk, 716 B).
- **Side finding, Load list.** On first opening from the package menu, **two rows looked selected** (Quick Save and Auto Save both with the bright outline) and the panel showed the **Quick Save's** thumbnail until I clicked the Auto Save row (`t2g`).

## 3. World state — door PASS; hidden character not run

- The door is a connection with no `to`; **walking into a shut one says *"the way opens — step through to pass it"*** (`t3a`) and a second walk-in steps onto it. The glyph does **not** change when it opens, so I discriminate by that message.
- Saved C with the door open. **Loaded C → walk into the door → I step straight onto (6,1), no message** (`t3b`): open is restored. **Loaded A (door shut at save) → walk to (5,1), walk in → *"the way opens"* again** (`t3c`): shut is restored. Both directions hold.
- **Hostility:** Dressa starts friendly (a conversation); after the "Draw your blade" reply she is hostile. Loading B (mid-fight, Dressa red, in the turn order) restored that; loading A (before) put her back as a talker. Not isolated beyond that.
- **A hidden character: COULD NOT TEST — not run.** `two-enemies` has a hidden creature; `ranged-detection`'s `a04-hidden-wall` is flagged unreachable by the library. I did not set up either.

## 4. F4 after Escape — not reproduced (PASS)

Steps of **TEST 153's failing case**, read back from my 153 session log:
1. In play, Escape (Options opens).
2. Options → Save Game.
3. Select the slot *Bravo*, click Delete, click OK in *"Are you sure you want to delete the save game?"* (the slot disappears).
4. On the Save list click **Cancel** (323, 954) → back on Options.
5. Wait 2.5 s.
6. Press **Escape** (Options closes).
7. Wait 3 s.
8. Press **F4** → in 153 nothing: no Saving picture, `quick.mark` unchanged. A click on the map (1090, 700) and then F4 worked.

Repeated **exactly** in 154 (`Vela Sorn`, on the freshly deleted slot): steps 1–8 → **F4 worked**: the Saving picture was up 1.1 s after the key (`t4b`; the 0.45 s frame still showed the play view, so the UI paints a beat late) and `vela-sorn.marks/quick.mark` appeared at 06:48:56.
Also worked: (a) Options opened with Escape, a save made from Options (naming box, OK), Escape, 1 s, F4 → `quick.mark` 06:35:47 (`t4a`); (b) Options → **CLOSE with the mouse**, 1.2 s, F4 → `quick.mark` 06:41:25. F5 and the movement keys also reached the board after each close. I could not make the 153 failure recur in three tries; I do not know what differed in 153; the quick save also did not exist yet in my retry, so that is not it.

## 5. Party of more than 3 — PASS

`five-party` (Coder's fixture tool, run in my data dir): **Load Game → "8 : FIVE IN THE PARTY"** shows a **dim left arrow and a teal right arrow** (`t5a`); **click right** → members 4 and 5, **third box empty**, right arrow dimmed, left lit (`t5b`); **click left** → page one again, pixel-identical to the first view (`t5c`). Five distinct faces over the two pages. A party of **3 or fewer shows no arrows**: Mira Mourn's old 3-box bookmark (`t6a`) and every one-member party (`t6b`, `t6d`).
- **Note on "player first".** On page one the **left** box is pixel-identical to the app's default *male* portrait and the **middle** box to the default *female* one, so I cannot say which box is the player (the fixture uses stock faces). The fixture doc says the leader is the **middle** box on page one, K2-style; every one-member party I opened puts the player in the **middle** box too. Your text says "player first" — one of them is out of date; I report what I see.
- The fixture's **Auto Save row reads "Dec 31, 1969 – 19:00:00"** (epoch time; the authored save has no autosave file). Only the fixture, as far as I know.

## 6. The player's portrait — PASS

- **Male, no chosen portrait** (Mira Mourn, `portrait: null` in her log, gender Male): a **new** bookmark (12 : GOLF) shows the **default male face** in the middle box (`t6b`).
- **Female, no chosen portrait** (an authored `Vela Sorn`, gender female, `portrait: null`): a new bookmark (13 : HOTEL) shows the **default female face** (`t6d`) — a different face from the male one.
- **Older bookmark:** Mira Mourn's earlier **7 : FOXTROT** still shows three **empty** boxes (`t6a`), as you predicted.
- **Not fixed: the Auto Save row.** Its panel has **no portrait in any of the three boxes**, an **empty package-name bar**, and the area text reads *"BED"* where the numbered rows read *"SAVE BED"* with *"TESTER SAVE BED"* above (`t6f`, `t6e`). The **Save screen's "New Slot" panel** also shows empty boxes (`t8b`), which may be intended.
- A character with a chosen portrait (Onjo, `po_pmha01`) shows it on bookmark rows (`t1g`).

## 7. Quick regression — PASS (mid-fight resume FAIL for the action, see 1)

- **Save:** Options → Save Game → New Slot → name → OK; slots numbered globally (Onjo 9, 10, 11; Mira 12; Vela 13).
- **Overwrite:** *"Are you sure you want to overwrite the save game?"* (`t8a`) → OK: the row keeps number 13 and its time moves 06:47:18 → 06:47:55 (`t8c`).
- **Delete:** *"Are you sure you want to delete the save game?"* (`t8c`) → OK: the row is gone (list shows only New Slot).
- **Load:** done many times (above).
- **Mid-fight save:** resumes with *"the fight resumes — round N, Onjo Trigit's turn"*, round, order, HP, enemy HP and move all correct; **only the action is wrong**.
- **F4 in a conversation:** no Saving picture and `quick.mark` unchanged (06:41:25 before and after) (`t7a`).
- **Side finding:** **F5 pressed while a conversation was open loaded the quick save** and dropped the conversation (`t7b` → `t7c`). Your table covers F4 only; I cannot say what K2 does.

## Fixtures I made (all in my own data dir, none on Shelf)

- `packages/tester-save-bed` — copy of `store-bed` + Endar Spire's trooper blueprints, one added quest (`a-debt-outstanding`), a door with no `to`, and two added replies on the merchant ("I hear there is a debt…" sets the quest flag, "Draw your blade." starts a fight). **No shipped package has a door that stays in its room, a merchant who can be fought, and a journal reply in one place**, so I built it; the library still reports the same 5 packages with problems (mine is clean).
- `onjo-bed.sav`, `vela-sorn.sav` — authored with copies of the app's own `tool/author_pt2721_equip_save.dart` (package and area strings changed; Vela: female, `portrait: null`). `five-party.sav` — Coder's tool, as in `TEST/fixtures/five-party-save.md`.

## What I did not check

Facing; a poison-type condition; a hidden character; a Force-pool change (force stayed 8 of 8); the Auto Save "party of more than 3" panel; K2 side-by-side images (I read the doc, not the captures); Escape in a conversation (not asked); the 153 notes on text sweep and key tests (not re-run).

Also seen, unchanged from earlier reports: Inventory rows still show raw ids (`adrenaline-amplifier`, `dominator-gauntlets ×2 (Equipped)` …), the TEST 149 finding.

Skills used: `verification-before-completion` (every PASS has a screenshot, a pixel diff or a file time; the one FAIL has a control; untested items listed), `diagnosing-bugs` (the action-budget control: live-available then F5), `research` (read PT-2733's ledger entry, `SAVE-LOAD-01` addendum and my own 153 log before the F4 retry), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
