# TEST 231: Spray, Clinch and Throw Down, the opportunity question, a lost Sweep on Sweep Pair

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-231/` (MAIN_WORK `0879a1f3`).

## Build

- **App**: main `2bd9706`, a worktree beside my clone. `gate.py --at 2bd9706`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at 2bd9706, 5597 tests, 0 failed"; ARCHIVE last green at 2bd9706. Lodestar `9950093` = lock; built through the lock.
- **Settings**: defaults (no settings.json), and back to defaults after E's Options runs. **Shelf** `326ea8b`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test231_saves.dart` ran first time and wrote all six. Sweep Pair from `author_tester_test229_saves.dart`, as MAIN added. Pristine copies kept.
- TEST 230 was already filed, on `e3a90c9`, so it wasn't rerun here.

## Summary: A to G pass as ordered, except one point in C; one finding

| # | Check | Result |
|---|---|---|
| A | Sprayer | **PASS, see Finding 1**. x steps Spray, Suppression Spray, Sweeping Fire. **Spray on A**: hover "Spray · Post A · Post C"; the click shoots A at "− Spray 3" (d20 14, 397 left), then C (d20 12, 391 left). **Suppression on C**: hover "Suppression Spray · Post C · Post D · Post A"; the click shoots those three at "− Suppression Spray 2", not B. **Sweeping on A**: hover "Sweeping Fire · Post A · Post C · Post D · Post B · Post E"; the click shoots those five at "− Sweeping Fire 1", not F or G. **Spray on F**: hover "Spray · Post F"; one shot, then "you have already acted". Own die on each shot. The hover named what the click shot in all of these. **Beyond the order**, range and sight from (1,7), where the wall now hides C, B and E from her and G is in sight: Sweeping on A hovers and shoots A, D, G |
| B | Spray Pair | **PASS**. "Spray · Post A · Blaster Pistol · … − dual-wield 3 − Spray 3 …", then "Post C · … − dual-wield 3 − Spray 3 …", no off-hand line. Spray on F is one shot; Spray on D shoots D, then A (a miss, so a miss doesn't stop it). **Control**: a plain shot has "off-hand: Blaster Pistol …" |
| C | Clincher | **PASS, one point for MAIN below**. x steps Clinch, Off Balance, Throw Down. **Clinch** on the Gunman: "win · damage 5 … · 395 left · slowed · cannot make ranged attacks", and the hover reads the same. His next turn, with her beside him: "Gunman attacks Clincher : \*miss\* : (9 + 2 = 11)", unarmed. The turn after, the hover is clean and he shoots: "(4 − 1 = 3)". **After F4 and load**: the hover still reads "slowed · cannot make ranged attacks"; next turn "(8 + 2 = 10)", then clean and "(4 − 1 = 3)". **Nobody in reach**: Weakling killed, Clinch, she walks to (0,4). The log reads "Gunman cannot make ranged attacks", with no attack; next round he shoots from there, "(7 + 1 = 8)". **Off Balance** on the Brute: "win · … 395 left · prone"; the hover reads "prone" with no "cannot stand"; next turn "Brute gets up — that was the Action". **Throw Down** on the Brute: "· prone · moved 2 squares", (5,4) to (7,4). On the Gunman: "· 396 left · prone", no move, unmoved at (4,3). **Losses**, on the Ironhide: Throw Down "against 35 — loss · damage 2 — 1d3 2 + Strength 3 — half damage · 398 left"; Off Balance "against 32 — loss · damage 3 — half damage"; Clinch "against 40 — loss · damage 2 — half damage". The hover after is clean. The log: "\*loss\* : (5 + 11 = 16)", then "Clincher damages Ironhide for 2 damage — half damage" |
| D | Clinch Armed | **PASS**. x: "Clinch needs empty hands". The next swing is a plain "Vibrosword · …" |
| E | Thrower | **PASS**. A win on the first throw: "· prone · moved 2 squares", the Brute at (5,4), then "Opportunity attack / Brute provokes an opportunity attack from Mate / one reaction · 1 left / 65% (needs 8+)", Yes, No. **While it's open**: clicks on hotbar slots and x change nothing (identical frame), and repeated End Turn clicks don't pass the turn. **No**: the question closes, there's no Mate line in the log, the Brute stays at (5,4), and Shooter isn't asked. **Yes**: one line, "Opportunity attack: Mate attacks Brute : \*miss\* : (3 + 2 = 5)", and nothing after it. **Options, Gameplay, Opportunity attack**: the row reads Ask, then "+" gives Never, then Always. **Never**: no question, no strike. **Always**: no question, and Mate strikes once. All on a replayed seed, so Mate's roll was the same 3 both times and I never saw him hit |
| F | Spray Allies | **PASS**. Sweeping on the Brute: hover "Sweeping Fire · Brute · Ironhide · Gunman", and the click shoots those three (Brute hit, two misses). Mate at (6,4) and Shooter at (6,5) are within 5 squares of the Brute and aren't shot |
| G | Dice, regression, Sweep Pair | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 68 ("reg231"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 115 of 196). **MAIN's added step**, Sweep Pair: the box reads "Sweep Attack · Vibroblade · … d20 20 … − dual-wield 3 · against 33 — loss · damage 2 — 1d10 1 + Strength 3 — half damage · 398 left". The log reads "\*loss\* : (20 + 8 = 28)", then "Sweep Pair damages Ironhide for 2 damage — half damage" |

## Finding

1. **A shot lands on a target the wall hides, whether plain or as a Spray's clicked first target. Only a Spray's other targets ask for sight.**
   - **Where**: Sprayer, Spray Yard, wall at (3,6). I ran the game's own `canSee` with that wall: from (1,4), Post G (5,8) is false. From (1,7), A, B, C and E are false, and D and G are true.
   - **Plain, from (1,4) at G**: the hover offers "95% (needs 2+)" with no warning (`a9-hoverG`). The click lands: "d20 6 … needed 10 — hit · damage 8 … 388 left" (`a9-clickG`). From (1,7), plain shots at C, A and B also land (`a8-plainC`, `-plainA`, `-plainB`).
   - **Spray, from (1,4) at G**: hover "Spray · Post G · Post D", and the click shoots both (`a10`). G is the hidden one. From (1,7), Sweeping on A shoots A, but drops C, B and E, the other three that spot hides (`a6`).
   - **Expected**: the ledger's `PT-2665` says Total Cover is `wall.blocksSight` through `canSee`, "WHICH EVERY TARGETING PATH ALREADY RESPECTS". The order asks for sight on each shot.
   - **Not checked**: whether older builds do this; I only ran `2bd9706`. Whether a melee or enemy attack does the same. G only joined the fight once she saw it from (1,7), so the shot at it came after that.

## For MAIN

- **The barred Gunman with nobody in reach stands still.** The order reads "strikes unarmed if a foe is in reach, or moves". She was 4 squares off and he stayed at (4,3) with the log line (`c5-walked`, `c5-yard`), while the Ironhide and Brute closed on her. The bed pins the log line and no attack, not a move. Filed as a question, not a finding: is standing still right?

Seen, not filed: the red dashed square round a hovered post is its reach, not the Spray's area, so it can include a post the Spray doesn't take (`a2-hover`).

My slips, no findings: my first Clincher load picked Flurry One when OCR misread the name, so that fight is thrown away. In E, my loop kept clicking through the open question, which is how the End Turn check was first seen; I then did the hotbar check on purpose.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
