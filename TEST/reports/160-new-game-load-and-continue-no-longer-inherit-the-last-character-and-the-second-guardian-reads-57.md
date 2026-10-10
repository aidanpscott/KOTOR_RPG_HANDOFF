# TEST 160

Written for: Main and Coder. Re-check of the TEST 159a fixes (PT-2738 FIX 1 and FIX 2). Real game on my Xvfb `:2`, my own data dir, K2 not launched. Screenshots: `HANDOFF/BUILD/screens/test-160/` (13 images). Coder's answer read first (commits `8e4bbf6`, `c7aed04`; ledger PT-2738 TEST 159a entry). Contaminated fixtures `t3-77` and `t3-21` deleted before the run (`.sav` and `.marks`).

## Build

- App `c7aed04a7ab045debf77cc7c34590f1622c24a79` (= origin/main; `git archive` into `/tmp/test160-build`, `flutter build linux --debug`; `pubspec.lock` unchanged by the build).
- Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = the app's lock = pub-cache.
- Lens `2bad745a53a1e741ab8d8ef94a954e6e3973b99b`, Shelf `8fa2475c79a1119b94def5700303481b09d4839f`, MAIN_WORK `71ae4e29bfde93329505d97c5e41ed8c76e1fc5a`, HANDOFF `cebf1da` at start.
- `check_shelf` clean (30 rules files, 105 blueprints).

## Summary

| # | Check | Result |
|---|---|---|
| 1 | New Game after a Jedi opened twice: empty well, arrival square, no old combatant; same after restart + Continue; clean autosave. Twice | **PASS** (2 of 2: T3-35 after Onjo Proof, T3-49 after Onjo Hp) |
| 2 | After a Jedi: Load another character's bookmark / Continue into another character | **PASS** both (Visual Pass: REGR on (2,3); Continue on (8,3); own pools and party) |
| 3 | Leave the Jedi mid-fight, then New Game | **PASS**: no fight, no turn order, Dressa not hostile, autosave `hostile []` |
| 4 | Both Guardians force 57 of 57 | **PASS** for the pool (57 of 57 on both). The companion sheet's WIS/CHA could not be shown: the game opens a companion's sheet only when it has a level pending |
| 5 | PT-2738 regression | **PASS**: droid and Soldier wells empty, Jedi full; footer rect and sidebar position identical for all three |

## 1. New Game no longer inherits — PASS (twice)

Exactly the order's steps, each run in one app session:

| | Run 1 | Run 2 |
|---|---|---|
| Jedi | Onjo Proof (force 8 of 8) | Onjo Hp (force 8 of 8, 47 of 103) |
| Open 1 | walked to `a01-bed · 8, 6`, Exit Game | walked to `8, 6`, Exit Game |
| Open 2 | resumed on (8,6) (the world WAS held), walked to `10, 6` (`c1a`), Exit Game | resumed on (8,6), walked to `10, 6` (`c1d`), Exit Game |
| New Game droid (Astromech / T3 / Engineer) | **T3-35**: sidebar well drawn, **empty**, no "force" line; on **"in" (1,1)**; Dressa (3,3) and the trooper (9,5) at their placements; nothing at (10,6) (`c1b`) | **T3-49**: the same (`c1e`) |
| App restarted, Continue | T3-35 empty, on (1,1) (`c1c`) | T3-49 empty, on (1,1) (`c1f`) |
| `autosave.world.json` | `force: None`, `at [1,1]`, `partyIds ['T3-35']`, `hostile []`, combatants `T3-35, merchant.bed.02, trooper.bed.03` | `force: None`, `at [1,1]`, `partyIds ['T3-49']`, `hostile []`, combatants `T3-49, merchant.bed.02, trooper.bed.03` |

Also: the droid's "N rules not checked" reads **3** (its own count) in both runs; T3-77 in TEST 159a read the Jedi's **1**, so TEST 148 (h)'s leak is gone too. In TEST 159a the same steps gave force 8 of 8 and the Jedi's square.

## 2. Load and Continue into a different character — PASS

Both after Onjo Hp was opened twice (walked to `8, 6` then `10, 6`) and left.

- **Bookmark.** Exit to Library → 0 AAA Visual Pass → Load Game → REGR → Load: Visual Pass Tester (Soldier 5) on **(2,3)**, five-member party as saved, 44 of 44, **empty** well; both Guardians **force 57 of 57**; Grunt empty; no Onjo on the board (`c2a`).
- **Continue.** Visual Pass leader walked to `v01-hall · 8, 3` and left (`c2b`); then Save Bed, Onjo Hp opened twice (`8, 6`, `10, 6`) and left; then Exit to Library → Visual Pass → **Continue**: leader on **(8,3)**, every companion where it stood, Soldier well empty, Guardians 57 of 57, nothing from the Jedi (`c2c`).

## 3. Mid-fight leak — PASS

Onjo Hp in a fight with Dressa: turn order **Onjo 13 / Dressa 10**, Onjo on (8,0), 0 moves, 46 of 103 (`c3a`). (Dressa was already hostile from earlier sessions, so walking toward her started it.) Options → Exit Game → OK → New Game → droid **T3-75**: **no turn order, no move/action HUD**, on "in" (1,1), empty well (`c3b`). Walked to (3,2) and bumped Dressa: she opens her **trade conversation** ("Looking to trade?"), not a fight (`c3c`). T3-75's autosave: `force: None`, `hostile []`, combatants `T3-75, merchant.bed.02, trooper.bed.03`. (Its `at [8,4]` is my own click: a blind click with the conversation still open landed on the conversation's small board and walked the droid there.)

## 4. Companion pool — PASS (pool); sheet not reachable

Five-party game: **first Guardian force 57 of 57, second Guardian force 57 of 57** (TEST 159a: 33 of 33 for the second) (`c2a`, `c2c`). 57 = Jedi Consular d8 at level 6 (33) + (WIS 14 → +2, CHA 14 → +2) × 6 (24), the blueprint's 14/14.

I could not show the companion **sheet's** WIS and CHA in the game: `_openPortrait` opens a companion's Character screen only when a level is pending (otherwise Equip), and the Character icon and the Party screen show the player only / no scores. So "matching its sheet" rests on the blueprint scores and Coder's single resolver (`_companionCombatantFor` feeds both), not on a screen reading.

## 5. PT-2738 regression — PASS

Measured on this build (`c5`, sidebar and footer for each):

| | Sidebar bars (vitality / Force) | Force well colour | Footer frames (vitality / Force) | Footer Force interior |
|---|---|---|---|---|
| Droid T3-75 | x 170–178 / **x 283–291** | (36,31,26) empty | x 1286–1312 / **x 1484–1513**, both y 859–990 | (0,0,0) empty |
| Jedi Onjo Hp | same | (106,143,216) blue, full | same | (12,54,46) full |
| Soldier (Visual Pass) | same | (36,31,26) empty | same | (0,0,0) empty |

Still open from the ledger's CHECK: the footer's full fill (12,54,46) is unchanged against empty black (not part of c7aed04).

## Fixtures

New droids (all clean): `t3-35`, `t3-49`, `t3-75`. `t3-77` and `t3-21` deleted. `run/cgdroid.sh` now detects the Skills/Feats warning line and picks the matching rows (`run/haswarn.py`).

## Still held (PT-2739)

Continue after leaving mid-fight resumes the same fight; the Tester Strongroom card text; name-not-tag in the speaker line and combat log (still `MERCHANT.BED.02` in this build, `c3c`).

Skills used: `verification-before-completion` (every PASS is an on-screen value, a pixel measurement or an autosave field; the Jedi's held world proven by the second open resuming on (8,6)), `diagnosing-bugs` (the leak's exact precondition — two opens — reproduced in each run), `research` (Coder's two commit messages and the ledger first), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
