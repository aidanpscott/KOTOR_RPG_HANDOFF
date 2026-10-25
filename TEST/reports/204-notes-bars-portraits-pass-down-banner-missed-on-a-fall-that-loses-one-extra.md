# TEST 204: Notes, "Party Member Down", the strip's bars, portraits, the smalls, and the damage watch

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-204/` (MAIN_WORK `1c4e289a`). The step-by-step log is `TEST/reports/204-running-log.md`.

## Build

App main `0233f17`, a git worktree beside my own clone. `gate.py --at 0233f17`: "FOR TESTER — CORE at 0233f17, 5162 tests, 0 failed"; ARCHIVE last green at 0233f17. Lodestar `ffa3e09` = lock = compiled. The build (10.3 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged. Settings: defaults. Brightness: default. Shelf `88d0d8f`; all packages identical.

Characters (`specs204/`): Note Taker, Fight Twelve and Fight Thirteen, each a Soldier 1 with Vela in Tester Bolt. Also Icon Nine and Dice One.

## Summary: all pass but one; the damage watch reproduced

| # | Check | Result |
|---|---|---|
| 1 | Notes | **PASS**: "Ask the Warden", Enter, "jump then", then five Backspaces gives "Ask the Warden / jump" (Space, a new line, and "j" didn't close the Journal). Save, Back, Close and reopen: the note is kept. Escape leaves |
| 2 | Party Member Down | **PASS** for the player's fall: 5 → −2 on a 7 hit, the banner shows once with "Fight Twelve". **FINDING** for Vela's fall: 1 → −13, no banner (below) |
| 3 | Strip bars | **PASS** at 1920: the fill is dark red from the foot. Vela at 29/40 fills y 146–207 of a frame spanning 122–208, 72% (29/40 = 72.5%); gunmen at 18/18 are full. At 1280 they're proportional by eye (Vela 36 px, gunmen full) |
| 4 | Portraits | **PASS**. Outside a fight, pressing Vela makes her large and the player drops to a small slot; pressing the player brings them back ("you are now controlling Note Taker"). In a fight, the large slot shows Vela on her turn |
| 5 | Enemy strip hover | **PASS**: the banner sits below the strip (with "GUNMAN" under the frame) and is gone when the pointer leaves |
| 6 | Long prompt | **PASS**: it wraps in its own column; the speaker name sits clear |
| 7 | Party list, 1280 | **PASS**: the row line ends at 618 and the list line is 1 px at 623, so 5 px, like the others |
| 8 | Arrows, marks | **PASS**: no arrows above the portraits (marks were checked in TEST 203) |
| 9 | Companion's manual turn | **PASS**: on Vela's turn the Defense line is hers ("10 + Dexterity 1 + class 2 = 13"), the reactions line is hers, and her slots match her hover ("move 0 of 5 · reactions 1 of 1"). Note: her move is already 0 at the start of her manual turn |
| 10 | Damage watch | **Reproduced** (below) |
| 11 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185. Regression: Save (slot 41, "reg204"), Escape then F4 (one quick save), Load, and a fight to its end, **won** with the updated `run/fightbolt.py` |

## Finding: a fall that loses one extra point shows no "Party Member Down"

This was Fight Twelve (`notes/fixtures/specs204/fight12.json`, `fight12-204.sav`, Tester Bolt). I tapped (1194,338), bumped Right, then pressed End Turn 16 times with the player passive, and kept every frame (240).

- Before: frame 225, "Vela: 1 of 40". After: frame 226, "Vela: −13 of 40", in one step, with a "−13" floater.
- The combat log lines for it:
  - "Gunman attacks Vela : *critical hit* : (19 + 3 = 22 : Threat Roll: 20)"
  - "Gunman damages Vela for 13 damage"
- The other Vela's 40 → 29 is the two other hits that round: "damages Vela for 3", and round 9's "damages Vela for 8".
- So Vela lost 14 from a 13 hit. That's the same extra point as in TEST 203, from the same die stream (one sample).
- The player's own fall (5 → −2 from a 7 hit) lost exactly the hit; afterwards the player bleeds 1 a round (−2, −3 … −9).
- No frame from 222 to 240 shows "Party Member Down". The extra point is what defeats the check: −13 + 13 = 0.

So there are two things here: Vela's fall costs one point more than the hit, and the banner misses any fall that does.

## Note

- At the start of Vela's manual turn her move is already 0 of 5 and her action slot dim, before I've done anything. This matches her hover, so the queue is reporting it truly.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
