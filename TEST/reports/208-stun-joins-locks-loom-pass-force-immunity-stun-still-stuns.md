# TEST 208: the stun fix, immunities, a dark power's drift, a join in a fight, skill checks by the controlled member, Loom

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-208/` (MAIN_WORK `76498b78`). The step-by-step log is `TEST/reports/208-running-log.md`.

## Build

- **App**: main `95765ea`, a git worktree beside my own clone. `gate.py --at 95765ea`: "FOR TESTER — CORE at 95765ea, 5233 tests, 0 failed"; ARCHIVE last green at 95765ea. Lodestar `f6495d3` = lock = compiled. The build (12.5 s) went through the lock, and `pubspec.lock` was unchanged.
- **Loom** `cc325e5`, from a fresh clone (item 7).
- **Settings**: defaults. Brightness: default.
- **Shelf** `553002b`: the new `tester-208` package synced; nothing else changed.
- **Beds**: Coder's tool wrote proof-immune, proof-drift, proof-muster and proof-locks. For item 1 I wrote a fresh push bed, `push-208`, from `specs207/push.json`.

## Summary: all pass but one finding

| # | Check | Result |
|---|---|---|
| 1 | Stun | **PASS**. Slowpoke is stunned in round 1, moves 2 squares without attacking ("Slowpoke closes 2 squares — 3 to 1 · Slowpoke is stunned"), then attacks in round 2. Quickstep is stunned in round 2, moves without attacking, then attacks in round 3. Push Jedi had the highest initiative (14), so no enemy could be stunned after its own turn in the same round. Quickstep was stunned after its round-1 turn instead |
| 2 | Combat log | **PASS**: "Slowpoke is stunned." appears once, under Round 1; "Quickstep is stunned." appears once, under Round 2 |
| 3 | Immunities | **PASS** for the push: under both Push and Wave, Rock and Steady are "not Force Pushed" and the Thug "is Force Pushed". **FINDING** for the stun (below) |
| 4 | Drift | **PASS**: Force Affliction on the Target gives "You have moved closer to the Dark Side of the Force." in Feedback |
| 5 | Join in a fight | **PASS**. "Then you both die." starts the fight, and Feedback reads "Recruit has joined the party." He leaves the board and Party Selection doesn't open. Opened by hand mid-fight, Party Selection shows "0 Available Slots" with the Recruit listed but not fielded, and "You are unable to change your party at this time" |
| 6 | Skill checks | **PASS**. The leader is refused at the footlocker: "you cannot use Security untrained — it needs at least one rank". Controlling Mate, it rolls "open lock — d20 5 + Security 10 = 15 vs 15 (moderate) · open". The console shows Slicing 12 and the vault door at "1 spike" for Mate; for the leader, Slicing 0 and "3 spikes". On a fresh bed, switching to Mate and back gets the same refusal. Sheets: Mate's Security reads Rank 8, Bonus +2, Total 10; the leader's reads 0 / 0 / 0 |
| 7 | Loom | **PASS**. A party.joined effect on the conversation tab gives "refused — party.joined needs subject, from, role: use the wizard", and nothing is written. A fresh clone at `cc325e5` builds in 11.0 s: `linux/` is tracked, nothing is generated, `pubspec.lock` is unchanged and git status is clean |
| 8 | Dice, regression | **PASS**. All 17 Round, attack and damage lines in Messages > Combat match `dice-baseline-206.txt`. The only difference is an OCR mark on "A fight begins.", which changes the md5. Regression: Save (slot 45, "reg208"), Escape then F4 (one quick save), Load, and a fight won |

## Finding: Force Immunity: Stun doesn't stop the stun

Steady holds Force Immunity: Stun (from the bed's `force_immunity_stun` feat).

- **Push on Steady**: "Steady is not Force Pushed" / "Steady is stunned." / 27 damage. Steady's own turn is "Steady closes 1 square — 2 to 1 · Steady is stunned", so it moves and loses its attack.
- **Force Wave**: the same "not Force Pushed" / "is stunned." for Steady.

Rock, which holds Immovable Object, is also stunned. MAIN to say whether Immovable Object should stop the stun as well as the push. Logs: `i2-c1.png`, `i3-c1.png`.

## Bed note: the proof beds read as level 1

The Proof Immune sheet shows "Jedi Consular 1", Vitality 8/8 and Experience 0 / 1000. But Force (104), the saves (+12/+8/+15) and the power DC (30) are level-16 values. The tool writes a single `classAdded {levels: 16}`, whereas my per-level beds read 16 everywhere. With 8 vitality, each Proof Immune run ended in total defeat by round 3, so I needed three runs for item 3.

## Small

- While Mate is controlled, the console's reach is measured from the leader. With Mate beside it and the leader 2 squares away, it said "Slice (Slicing) — 2 squares away". It opened once the leader stood next to it (`l-c4`, `l-c5`).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
