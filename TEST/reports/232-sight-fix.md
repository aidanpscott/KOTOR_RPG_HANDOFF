# TEST 232: the sight fix

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-232/` (MAIN_WORK `cf173075`).

## Build

- **App**: main `6f9b8e1`, a worktree beside my clone. `gate.py --at 6f9b8e1`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 6f9b8e1, 5630 tests, 0 failed"; ARCHIVE last green at 6f9b8e1. Lodestar `9950093` = lock.
- **Settings**: defaults (no settings.json), and no settings.json at the end. **Shelf** `326ea8b`, synced; check_shelf clean (33 rules files, 128 blueprints), run again after I removed my private yard.
- **Beds**: `author_tester_test231_saves.dart` ran first time and wrote all seven, pristine copies kept. Cleaver from TEST 229. For B and C, my own private yard, described under B and C.

## Summary: A to E pass; one finding; one question

| # | Check | Result |
|---|---|---|
| A | Sprayer | **PASS, see Finding 1**. All with G in the fight, except the first two lines. **From (1,4), G not yet in the fight**: click reads K2's sentence, she stays put, and the same turn's click on A shoots (d20 14, 397 left). The hover is blank (Finding 1). **From (1,4), G in the fight** (she saw it from (1,7) and walked back): hover "Post G / You cannot target a creature you cannot see or do not have a line of sight to.", no percentage, no walk line. Click: the same sentence, no attack, she stays put. **Declared**: Spray on G: hover and click refused, "Spray" stays declared, and the next click on A shoots A, C at "− Spray 3" with the Action still there. **From (1,7)**: hover and plain click refused on A, B, C and E, all four. Declared: Spray on A and C, Suppression on B, Sweeping on E, each refused, and x still steps on from the tier held. After all those refusals, Sweeping on D in the same turn shoots: hover "Sweeping Fire · Post D · Post G", then D (d20 20, critical) and G (d20 9), not A, B, C or E. **Spray on D**: D, G. **Spray on G**: G, D. **Plain**: D (379 left), G (387 left). **Log**: nothing for any refused click; the lines go straight from the last attack to the next real one, and "line of sight" appears nowhere in it |
| B | Melee, foe behind a wall | **PASS, in my private yard**. Corner Blade, Vibrosword, at (4,4); Post C at (4,7) behind the wall at (4,5). Hover: "Post C · 95% (needs 2+) · 3 squares · 1 left · Provokes an attack from Post B", with the walk drawn round the wall. Click: she walks to (3,6) and strikes: "d20 4 … needed 10 — hit · damage 10 … 390 left" |
| C | Closed corner | **PASS, in my private yard; see the question**. Walls at (5,4) and (4,5), she at (4,4), Post A at (5,5) in the fight. Hover: K2's sentence, no percentage, no walk. Click: the same, no attack. **Its turn**: Post A doesn't attack her, and says nothing. **Leaving**: she steps to (4,3) with A's reaction unspent; no opportunity attack, no provoke warning. **Control, same post from the open corner (6,4)**: hover offers a chance; the click hits (d20 17, 384 left); on its turn it attacks her (d20 20, 3 damage); she steps to (6,3) and reads "Post A catches Corner Blade leaving" |
| D | The bar, Clincher | **PASS**. Clinch on the Gunman beside her: "… against 14 · 1 square — win · damage 5 … 395 left · slowed · cannot make ranged attacks". His turn: "Gunman attacks Clincher : *miss* : (9 + 2 = 11) · Flanking +2", his punch's +2 rather than his pistol's −1 from TEST 231, and he is still at (4,3) |
| E | Dice, regression, quick check | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 69 ("reg232"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 130 of 196). **Plain shot in sight**: A above. **Cleave in sight**: Cleaver, "Cleave · Brute · … d20 20 … critical · 386 left", then "Ironhide · … d20 9 … 391 left" |

## Why B and C used a private yard

No Shelf yard has the shape in a form play can reach. Corner Peek (`ranged-detection` a05) and Probe Pinch (`tester-probe` a07) both have a closed corner, but the corner seals the two halves, so no foe can come to stand across it from her. The Attack and Throw Yards have no walls, and the Spray Yard's single wall has no corner. So I wrote a private package in my data dir: 14 by 9, floor, walls (5,4) and (4,5), start (4,4), and three Spray Yard posts at A (5,5), B (3,3), C (4,7). It used the shipped post blueprints and doctrine, and I deleted it afterwards. Nothing went to the Shelf. The save was the TEST 231 tool's `save()` with a Vibrosword.

## Finding

1. **A creature not yet in the fight has a blank hover where the click gives K2's sentence.**
   - Sprayer, first turn at (1,4), Post G hidden by the wall and not on the bar or in the status line.
   - Hover on G, tried four times: no tip, no ring, no banner. A frame diff against the mouse off the board is empty (`a1-hover-g`, `a1-hover-g3`, `hv-G`). The same hover on F, D, C and two empty squares all draw something.
   - Click on G: "You cannot target a creature you cannot see…" (`a2-click-g`).
   - It's the same for Post A in my yard before she had seen it (`c2-hov-A`).
   - This is the state your A.1 describes, from (1,4) at the start. The sentence does show on the hover once G has joined, so the refusal itself holds. What's left is that a player sees a ring on the board and gets nothing on hover until they click.

## Question

**Does a foe across a closed corner still flank?** With her at (4,4), Post B at (3,3) hit with "(19 + 3 = 22) · Flanking +2". The only foe opposite B is Post A at (5,5), which can't strike her there. Control: at (4,3), with no one opposite, Post B reads "(17 + 1 = 18)", no Flanking. §8 says "adjacent to the same enemy on opposite sides", and A is adjacent, so this may be right as written. Post A's red reach ring also takes in her square across that corner (`c3-hovA`). I'm not filing either; tell me if they're wrong.

Seen, not filed:
- Spray's d20 came up 2 three shots running (G, then G, then D, with Post and Bump rolls between them), the other shots varying. I'm calling it chance.
- In my yard Post B took no opportunity attack on either of two later walks, with no provoke warning. It had spent its one reaction in round 2, and the pool lasts the whole fight (`play_screen.dart` 5455), so that's as built.

Bed only, not reachable, as your order says: an enemy whose walk loses its line, and the bar's other cases.

My slips, no findings: my first click on Post B in my yard was before any fight, and read "walk into them to act". My first hover on G looked like a missed mouse event, so I repeated it four ways before calling it blank.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
