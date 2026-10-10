# TEST 159b (the held parts of TEST 159, on the PT-2739 build)

Written for: Main and Coder. Real game on my Xvfb `:2`, my own data dir, K2 not launched. Screenshots: `HANDOFF/BUILD/screens/test-159b/` (28 images). Coder's PT-2739 answer read first: the ledger entry (Main's order) and the five commit messages 0ac3935, 21d6765, 0233cf2, 40241c6, d75c3da.

## Build

- App `d75c3da93940c197b1c00013dedfb95cf7de3f36` (= origin/main; `git archive` into `/tmp/test159b-build`, `flutter build linux --debug`; `pubspec.lock` unchanged by the build).
- Shelf `1f04018394ddfb66bbab47985aa30932b7d44aef` (my data dir's `packages/` checked out at it).
- Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = the app's lock = pub-cache.
- Lens `2bad745a53a1e741ab8d8ef94a954e6e3973b99b`, MAIN_WORK `5df1ae35617a7d597d0d29804a2d84be4bce2665`, HANDOFF `4a370e8` at start.
- `check_shelf` clean (30 rules files, 105 blueprints).

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Continue after leaving mid-fight resumes the same fight | **PASS, 4 of 4** (3 in-session + 1 across an app restart): same round, turn, initiative, both HPs, moves, action, square. Leaving on the enemy's turn was **not possible** (her turn finishes within 0.15 s of ending mine) |
| 2 | In-game loads, F5 ×5 and Options > Load ×5, mid-fight | **PASS, 10 of 10**, no error screen; every load restored the saved turn |
| 3 | Strongroom card has its own text; no card carries another package's text | **PARTIAL**: own text, and no card carries another package's text; **but the card says "two mines" and the package holds four** |
| 4 | Name, not tag (Endar Spire + Tester Save Bed; conversation + fight) | **PASS**: header, status line, combat log, turn order, examine and free-strike lines all show names; no tag anywhere. The message history has no tags but also holds no creature lines to name |
| 5 | Quick regression | **PASS**: Save, Load, Quick Save, Quick Load, Options open/close, New Game after a Jedi starts clean |

New, outside the order: **a New Game whose name matches an existing character silently overwrites that character** (see "Seen").

## 1. Continue after leaving mid-fight — PASS (4 of 4)

Fixture `onjo-hp` (Jedi Sentinel 1, 103 HP) against Dressa in Tester Save Bed. Fight started by bumping Dressa: **initiative Onjo Hp 9, Dressa 7** (turn-order panel). After every Continue the status line reads *"the fight resumes — round N, Onjo Hp's turn"*.

| Run | Before Exit Game | After Continue |
|---|---|---|
| 1 | one round played, a step: round 2, Onjo's turn, initiative 9/7, Onjo 44 of 103, Dressa 20 of 20, 4 moves, action available, (4,2) (`c1-run1a`) | **round 2, Onjo's turn**, 9/7, 44 of 103, 20 of 20, 4 moves, action available, same square (`c1-run1b`) |
| 2 | end turn, step to (4,3), attack (lightsaber hit 12): round 3, Onjo 44, **Dressa 8 of 20**, 4 moves, **action spent** (`c1-run2a`) | round 3, Onjo's turn, 44, 8 of 20, 4 moves, **action spent**, (4,3) (`c1-run2b`) |
| 3 | end turn and Escape 0.15 s later, trying to leave on Dressa's turn: her turn had already resolved ("Dressa: unarmed … miss"); round 4, Onjo's turn, 5 moves, action available, (4,3) (`c1-run3a`) | round 4, Onjo's turn, 44, 8, 5 moves, action available, (4,3) (`c1-run3b`) |
| 4 (**app restarted** between leaving and Continue) | step to (4,2): round 4, 4 moves (`c1-run4a`) | round 4, Onjo's turn, 44, 8, 4 moves, action available, (4,2) (`c1-run4b`) |

`autosave.world.json` now has a `fight` block: run 1 `{"encounter":{"round":2,"order":["Onjo Hp","merchant.bed.02"]},"turn":"Onjo Hp",…}` with each combatant's initiative and vitality; run 3 `round 4, turn Onjo Hp, at [4,3]`; run 4 `round 4, turn Onjo Hp, at [4,2]`.

**Enemy's turn:** not reachable. With a single unarmed enemy, her whole turn is resolved before an Escape sent 0.15 s after *space* arrives, so a save can only be made on the player's turn here. Not a defect; a fixture with a slower enemy turn (several enemies, or movement) would be needed to try it.

## 2. In-game loads — PASS (10 of 10)

All mid-fight (round 4, Onjo's turn, on (4,2), quick save made there with F4).
- **F5 ×5**, a step right before each so every load has something to undo: each lands on the board with Onjo back on (4,2), 4 moves, *"the fight resumes — round 4, Onjo Hp's turn"*; no error screen (`c2a`, `c2b`).
- **Options > Load Game ×5**, alternating the Quick Save and the Auto Save row, a step before each: each lands on the same resumed turn; no error screen (`c2c`: the list as clicked on top, the result, the status line).

## 3. Library cards — PARTIAL

- **Tester Strongroom** (`c3c`): *"A strongroom with a guard droid, a locked footlocker, a locked console, a crate and two mines in the floor. Two doors lead to an empty vault: one locked, one opened with a Sith keycard."* Its own text, matching the package's guard droid, footlocker, console, crate, the two doors (locked 30 / `sith-keycard`) and the empty vault. **But `a01-strongroom.toml` holds four hazards, all mines: `mine.strongroom.01` (damage over time), `.08`, `.09`, `.10` (conditions).** The card says two.
- **Every other card** (`c3a`, `c3b`, `c3c`; 22 cards) checked against its own package's areas and contents: none carries another package's text. One wrong for its own package: **Tester Probe** says *"A single room, for checking that a package reaches the game at all"* and the package has **11 areas, 18 doors** and ~30 creatures (unchanged since 8fa2475; not "another package's text", so outside the order's question).

## 4. Name, not tag — PASS

| Where | Tester Save Bed (Dressa, `merchant.bed.02`) | Shelf's Endar Spire (Sith Trooper, Tee Three) |
|---|---|---|
| Conversation header | **DRESSA** (`c4a`; TEST 158: MERCHANT.BED.02) | **SITH TROOPER** (`c4c`) |
| Fight start line | "So be it. · initiative — T3-75 16 · Dressa 15" | "Then you die here. · initiative — Tee Three 7 · Sith Trooper 3" |
| Status line | "T3-75: 9 of 9 · Dressa: 20 of 20" | "Tee Three: 9 of 9 · Sith Trooper: 18 of 18" |
| Combat log | "Dressa: unarmed · rolled 7 …" (`c4b`); Onjo's fights: "Dressa: unarmed … miss" | "Sith Trooper: Blaster Rifle · rolled 5 …" (`c4d`); "Sith Trooper catches Tee Three leaving — unarmed …" (`c4g`) |
| Turn order / panel | "Dressa" | "Sith Trooper" (`c4e`) |
| Examine (right-click) | — | "examine Sith Trooper — d20 17 + Xenology 0 …" (`c4f`) |
| Messages log | Combat: "A fight begins." ×3; Dialogue: "nothing here yet" | the same (`c4h`) |

No tag on any screen. The message history has no tag either, **but it carries no creature lines at all**: Combat holds only "A fight begins.", and **Dialogue stays empty after a full conversation** (both packages). So "names in the message history" cannot be shown; the log itself is near-empty (observation, not the name/tag question).

## 5. Quick regression — PASS

- **Save / Load:** Endar Spire mid-fight, Save Game → New Slot → "R159" → OK; a step (the trooper's free strike: 8 of 9); Options → Load → R159: 9 of 9, 5 moves, (6,3), *"round 2, Tee Three's turn"* (`c5a`).
- **Quick Save / Quick Load:** F4, step to (5,3) (4 moves), F5: 5 moves, round 2 (`c5b`). (Plus the ten loads of check 2.)
- **Options** opened and closed some forty times in this session, by Escape and by Close.
- **New Game after a Jedi:** Onjo Hp opened twice (mid-fight both times, `c5c`), left; New Game droid: on "in", empty well, no fight, own "3 rules" count (`c5d`).

## Seen, not in the order

- **A New Game silently overwrites an existing character with the same name.** Chargen generated the designation **T3-75**, already an existing character: `t3-75.sav` was replaced (19:33:46) by the new droid; the old T3-75 (its fight with Dressa, its moves) is gone. Repro on purpose: New Game → droid → at the Name step type an existing designation (`T3-35`) → no warning on the Name or Story step (`s1`) → Play: `t3-35.sav` rewritten at 19:37:22, one T3-35 left (`s2`). The stale `autosave.world.json` of the old character stayed in `t3-75.marks/` and was correctly **not** applied to the new one on Continue (it arrived on "in", no fight), so FIX 1's guard holds; but the old character's own data is lost, and any bookmarks in its `.marks` folder would now list under the new character. The droid designation pool is "T3-" + two digits, so collisions are likely. **Likely cause, not shown:** the save file is keyed by the character name and New Game writes it without checking for an existing one.
- **Message history is near-empty** (above): no dialogue lines, combat only "A fight begins.".
- `gobed.sh`'s fixed click landed one card off once (library scroll position differs between runs); now found by matching the card's title (`run/findcard.py`).

## Fixtures

`onjo-hp` (its autosave now mid-fight, round 4), `t3-75` and `t3-35` **replaced** by new droids (by the defect above), `tee-three` (bookmark R159 + quick save, mid-fight). Shelf in my data dir at 1f04018.

Skills used: `verification-before-completion` (every PASS a screen value and, for check 1, the autosave's own fight block), `diagnosing-bugs` (the overwrite reproduced on purpose with a chosen name after the accidental case), `research` (Coder's commits and the ledger first), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
