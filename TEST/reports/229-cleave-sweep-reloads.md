# TEST 229: the Cleave family, the Sweep family, the mid-fight reloads

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-229/` (MAIN_WORK `d5a690c4`).

## Build

- **App**: main `0f8ae8e`, a worktree beside my clone. `gate.py --at 0f8ae8e`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at 0f8ae8e, 5550 tests, 0 failed"; ARCHIVE last green at 0f8ae8e. Lodestar `4199fd7` = lock; built through the lock.
- **Settings**: defaults (no settings.json). **Shelf** `a1f1bab`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test229_saves.dart` ran first time and wrote all six, pristine copies kept. For G, pristine Staggering (TEST 225), Combination Fists and Body Blow Fists (TEST 228).

## Summary: A to H all pass; two findings; one part not reached

| # | Check | Result |
|---|---|---|
| A | Cleaver | **PASS**. x steps Cleave, Wide Cleave, Great Cleave. **Cleave** on the Brute: "Cleave · Brute · Vibrosword · … d20 15 … − Cleave 3 · needed 10 — hit · damage 12 … 374 left", then "Ironhide · Vibrosword · … d20 12 … − Cleave 3 · needed 16 — hit · damage 9 … 382 left". **Wide Cleave** on the Weakling: "Wide Cleave · Weakling · … − Wide Cleave 2 … -8 left · dies", then "Gunman · … − Wide Cleave 2 + closed on a ranged weapon 2 …", then "Brute · … − Wide Cleave 2 …". **Great Cleave** on the Brute with all four standing: Brute, Ironhide, Weakling, Gunman at "− Great Cleave 1"; the Weakling falls on line three ("-4 left · dies") and the Gunman still strikes. With the Weakling already dead it is three lines. Own dice on every line. **Defense**: the HUD reads "Defense base 10 + Dexterity 2 + class 2 = 14" after each tier, with no penalty |
| B | Cleaver Pair | **PASS**. "Cleave · Brute · Vibroblade · … − dual-wield 3 − Cleave 3 …", then "Ironhide · Vibroblade · … − dual-wield 3 − Cleave 3 …", both Vibroblade, with no "off-hand:" line (twice). **Control**: a plain swing is "Vibroblade …", then "off-hand: Vibrosword …" |
| C | Sweeper | **PASS**. **Win**: "Knockdown · Vibrosword · rolled 37 — d20 20 + attack 8 + Strength 3 + Knockdown 6 · against 14 — win · damage 9 — 1d12 5 + Strength 4 · 391 left · prone · cannot stand". "Legsweep · … + Legsweep 3 · against 12 — win · … prone · cannot stand". "Sweep Attack · … against 5 — win · …". **Loss**, on the Ironhide: "Legsweep · … rolled 26 … + Legsweep 3 · against 27 — loss · damage 3 — 1d12 3 + Strength 4 — half damage · 397 left"; it stays up. **Natural 20**: the Knockdown above and "Sweep Attack · … rolled 31 — d20 20 … against 25 — win": no confirmation, no critical. **Prone**: End Turn reads "Brute gets still down — cannot stand". On her next turn, no x: "… 2d12 2+4 + Strength 4×2 + Knockdown 6×2 × 2 critical", Knockdown, not the lower tiers. The turn after: "Brute gets up — that was the Action", and a plain swing has no bonus ("1d12 8 + Strength 4"). The Ironhide swept by a natural 20 goes the same way |
| D | Sweep Plain | **PASS**. A plain swing at a prone Brute: "1d12 3 + Strength 4 + Sweep Attack 2". **Gunman**: "Sweep Attack · … + closed on a ranged weapon 2 · against 14 · 1 square — win · … 391 left · prone · cannot stand", with no save rolled. Then a plain swing: "… + Sweep Attack 2×2 × 2 critical", and next round "Gunman gets up — that was the Action" |
| E | Sweep Pair | **PASS**. One line: "Sweep Attack · Vibroblade · … − dual-wield 3 · against 14 — win · … prone · cannot stand", no off-hand line. A loss is the same: "… − dual-wield 3 · against 22 — loss · damage 2 — 1d10 2 + Strength 3 — half damage". Plain at a prone target, both hands: "… 2d10 2+4 + Strength 3×2 + Sweep Attack 2×2 × 2 critical", then "off-hand: Vibrosword · … 1d12 6 + Strength (off hand) 1 + Sweep Attack 2". **Control**: once it has stood, neither hand has the bonus |
| F | Sweep Shot | **PASS, one part not reached**. x once and x three times declare nothing, and no text appears. The next shot is a plain "Blaster Pistol · … − point blank 4 …". The hotbar's attack slot is empty. **Not reached**: the passive on a shot at a prone target (from the tool's header; not in the order). A pistol can't knock anything down here and nothing else in the yard does |
| G | Reloads | **PASS, see Finding 1**. All on the Quick Save row (a mid-fight F4, then Load). **Sweep Plain**: after "· prone · cannot stand", the hover reads the same after the load; End Turn gives "Brute gets still down — cannot stand"; a plain swing has "+ Sweep Attack 2"; the next round "Brute gets up — that was the Action". **Combination Fists**: "Defense base 10 + Dexterity 2 + class 4 + Combination -2 = 14" before and after the load. The Brute's turn reads "needed 14 (-2 Combination)", and her next turn shows "… class 4 = 16". **Staggering**: Pinning Fire from 4 squares, "d20 15 = 15 vs 21 · held"; hover "held" after the load; "Brute out of movement 5 squares short"; her next turn, hover clean. **Body Blow Fists**: "· cannot take a reaction", hover the same after the load, clean after its turn. **Beyond the order**: Body Blow, load, walk off: "Ironhide catches Body Blow Fists leaving", and the Brute takes nothing. **Control**, a plain swing then a walk: "Brute catches Body Blow Fists leaving" |
| H | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 66 ("reg229"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 166 of 196) |

## Findings

1. **After a load, an enemy killed earlier in the fight is back as a target: its square blocks a walk, and a swing lands on the corpse and spends her action.**
   - Pristine Body Blow Fists: bump the Brute, End Turn, plain Left kills the Weakling ("-6 left · dies"), End Turn.
   - **Her action already spent**: plain swing at the Brute, F4, Load the Quick Save. A dim ring is on the Weakling's square (3,4), not there before the load (`t229-h2-beforeload.png`, `h2-afterload`). The bar still reads G, I, B. Left reads "you have already acted", and she stays put (`h2-walk`); clicking the square does the same (`h2-clickcorpse`). **Control**: with no load in that turn, the same Left walks her onto the square (`g7-walk`).
   - **Her action not spent**: End Turn, F4, Load. The ring is back. Left swings: "unarmed · rolled 21 — d20 10 + attack 8 + Strength 3 · needed 10 — hit · damage 5 — 1d3 2 + Strength 3 · -11 left", the status line goes from -6 to -11, and her action is gone (`h3-left`). The log: "Body Blow Fists attacks Weakling : *hit*". It reads no "dies" this time.
   - The ring goes once she has swung at it. In the first run she was back to walking onto the square a turn after the load (`g7-walk`). The Weakling takes no turn in any of this.

2. **The Combat log calls a lost Sweep a miss and leaves out its half damage.**
   - The box: "Legsweep · … against 27 — loss · damage 3 … — half damage · 397 left". The log: "Sweeper attacks Ironhide : *miss* : (12 + 14 = 26)", with no "damages" line, then the next round (`t229-c6-log.txt`).
   - The same for Sweep Pair's loss: the Ironhide drops 400 to 398, and the log has "Sweep Pair attacks Ironhide : *miss* : (4 + 8 = 12)" alone (`e5-log.txt`).
   - A win logs *hit* and "damages" as usual.

Seen, not filed:
- For Coder's dice replay: in nine fresh fights, the first swing after bump and End Turn is d20 20 every time, with these beds all seed 1. Plain swings do it too: Body Blow Fists, no x, at the Weakling, "d20 20 … threat confirmed … d20 13". So on these beds it isn't only a chain's first strike. Replaying a seed repeats dice, so it may be no more than that: the same bed run twice gives the same roll. Sweep Shot's first shot is a d20 9. Screens `a1`, `a4`, `b1`, `c1`, `d1`, `e1`, `g3`, `g5`, `h1`.
- Saving and loading restarts the Combat log at the load. The box then reads "the fight resumes — round 3, Body Blow Fists's turn".

My slips, no findings: my first Sweep Plain load took the Auto Save row (same second as the quick save; it read the same), so that was rerun on Quick Save. One Body Blow load picked the wrong character when OCR missed the name; that pass is thrown away. Her first walk off after the load was a diagonal click, which doesn't walk.

KNOWN, not filed: the enemy's line "gets still down — cannot stand" (seen); Great Cleave's hover drawing a walk (not tried).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
