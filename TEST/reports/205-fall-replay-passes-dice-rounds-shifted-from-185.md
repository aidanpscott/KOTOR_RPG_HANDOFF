# TEST 205: the fight12 replay, companions' first turns, round-end ticks, critical hits

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and logs are in `KOTOR_RPG_MAIN_WORK/media/screens/test-205/` (MAIN_WORK `5f06fe8d`). The step-by-step log is `TEST/reports/205-running-log.md`.

## Build

App main `a599a96`, a git worktree beside my own clone. `gate.py --at a599a96`: "FOR TESTER — CORE at a599a96, 5190 tests, 0 failed"; ARCHIVE last green at a599a96. Lodestar `c5cb345` = lock = compiled. The build (10.1 s) went through the lock, and `pubspec.lock` was unchanged. Settings: defaults. Brightness: default. Shelf `88d0d8f`; all packages identical. `saves/fight12-204.sav` was the authored copy (md5 83763b06…); I restored it before each replay.

## Summary: the fix passes; one finding in the dice baseline

| # | Check | Result |
|---|---|---|
| 1 | The replay | **PASS** (detail below). The crit takes Vela from 1 to **−12**, exactly the logged 13, with "Party Member Down / Vela" on its own row under the attack banner, both up together. She stays at −12 and bleeds to −13 only at the next round's end. The player's fall (5 → −2 from a 7) shows the banner too, and bleeds from the round after. Every frame's vitality matches the logged damage |
| 2 | Companions' first turns | **PASS**: both Velas start their first manual turn with "move 5 of 5 · reactions 1 of 1" and their slots lit |
| 3 | A round-end tick felling someone | **Not reached cleanly**. Tick One (6 vitality) was felled by the mine's own first blow. Tick Two (9) was left at 3, and outside a fight the poison doesn't tick on steps. On reaching the Probe Droid's fight she fell at once, and a solo fall is a total defeat, so the defeat box replaces any banner and I couldn't tell a tick from a blow. It needs a party with a companion |
| 4 | Criticals on the player or an enemy | **Not reached**: the regression fight's whole log has no critical hit. The only critical seen (on Vela) matched exactly |
| 5 | Dice, regression | **FINDING** for the dice (below). Regression **PASS**: Save (slot 42, "reg205"), Escape then F4 (one quick save), Load, and a fight won with `run/fightbolt.py` |

## Item 1, line by line (frames in `media/screens/test-205/f/`, log in `log-pages.txt`)

- Round 1: "damages Fight Twelve for 4", "for 3", taking the player 12 → 5.
- Round 2: "for 7", taking the player 5 → −2 (frame 16), with "Party Member Down / Fight Twelve" (frames 16–17). She stays at −2 through that round, then −3, −4 … one a round.
- Vela A:
  - round 2 "for 5" and "for 1" (40 → 34);
  - round 3 "for 4" (→ 30); round 4 "for 4" (→ 26);
  - round 5 "for 12" (→ 14) and "for 7" (→ 7);
  - round 6 "for 6" (→ 1).
- Round 8, "Gunman attacks Vela : *critical hit* : (19 + 3 = 22 : Threat Roll: 20)" / "Gunman damages Vela for 13 damage": Vela A 1 → −12 (frame 196), banner shown. Still −12 at frames 203 and 211, and −13 at frame 226 (the next round's end).
- Vela B: round 8 "for 3" and "for 8", round 9 "for 10", taking her 40 → 19 (frame 211), matching. Her later fall came with the total defeat (the defeat box, no separate banner).

## Finding: the dice replay now groups rounds differently from TEST 185

From Dice One's Quick Save (Oct 19, 07:40:30), with the same walk, Messages > Combat on a599a96 reads:

- Round 1: Dice One *hit* (14+3=17), 11; Vela *hit* (13+3=16), 7; Vela *miss* (8+3=11)
- Round 2: *hit* (13+3=16), 5; *miss* (5+3=8); *miss* (8+3=11)
- Round 3: *miss* (1+3=4 Automatic Miss!); *hit* (18+3=21), 3; *hit* (15+3=18), 7

TEST 185, and TEST 204 on 0233f17, read differently:

- Round 1: Dice One hit 11, "Gunman has already acted", Vela hit 7
- Round 2: miss (8+3), hit (13+3) 5, miss (5+3)
- Round 3: miss (8+3), miss (1+3 AM), hit (18+3) 3

Every roll and damage is the same, in the same order. What's changed is that the gunman who "has already acted" now attacks in round 1, so every later round is shifted by one attack. With the shift, three Spaces now end in total defeat. This changed between 0233f17 and a599a96. MAIN to say whether that's the intended effect of this hash's round timing, or a fault.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
