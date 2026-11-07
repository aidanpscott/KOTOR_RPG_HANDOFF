# TEST 233: The corner sweep, plus the fixes

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-233/` (MAIN_WORK `4179afdd`); names in brackets below are files there.

## Build

- **App**: main `8ecbc37`, a worktree beside my clone. `gate.py --at 8ecbc37`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 8ecbc37, 5698 tests, 0 failed"; ARCHIVE last green at 8ecbc37. Lodestar `9950093` = the lock. Loom `fcae558` as ordered.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf** `ab1b938`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: both tools ran first time (233: six saves; 234: three). Every yard run starts from a pristine copy in a relaunched app.

## Summary: everything I could reach passes; nothing filed

| # | Check | Result |
|---|---|---|
| A1 | Post A, and (4,8) | **PASS**. Hover A: "Post A / You cannot target a creature you cannot see or do not have a line of sight to." No reach ring, only the hover circle on its token (`a1-hovA`). Click: the same sentence; she stays at (4,4) (`a1-clickA`). Hover and click (4,8): "there is no way there", no name, no sentence (`a1-hovE`, `a1-clickE`). |
| A2 | Quick Attack on D | **PASS**. x goes Cleave first, then Quick Attack. Hover D: "+8 attack · +3 Strength · −2 Quick Attack, against Defense 10" (`b2-hovD1`). Mate walked to (6,2) on its own turn (`b2-matemoved`). Next turn, hover D: "+2 Quick Attack" (`b2-hovD2`). |
| A3 | Bring A in | **PASS**. The walk to (6,4) runs (4,3), (5,3), (6,3), (6,4), 4 squares, 1 left; Post B and Bump swing as she leaves (4,4). A and C join (`c3-hov64`, `c3-at64`). With 1 square left, the walk back stops at (6,3): "Opportunity attack: Post A attacks Corner Blade : *miss* : (1 + 1 = 2 Automatic Miss!)". One blow (`c3-hovback`, `c3-back`, `c3-log`). Next turn I walked her home to (4,4). |
| A4 | Hover A, in the fight | **PASS**. The sentence. The dashed ring takes in (6,4), (6,5), (6,6), (5,6), (4,6), leaving out (4,4), (5,4) and (4,5) (`d4-hovA2`). |
| A5 | End Turn | **PASS**. "Post B attacks Corner Blade : *hit* : (18 + 1 = 19)", no Flanking. A makes no attack (`e5-log`, `f6-log`). |
| A6 | Cleave on B | **PASS**. "Cleave · Post B · … d20 1 … miss", then "Bump · Vibroblade · rolled 22 … hit · damage 9 … 391 left". A untouched at 400 (`f6-hovB`, `f6-cleave`). |
| A7 | Step to (4,3) | **PASS**. Fresh turn: hover reads "1 square · 4 left", no warning. Up arrow: she's at (4,3), no blow (`g7-hov43`, `g7-step`, `g7-log`). |
| A8 | Corner Fist | **PASS**. Click A: the sentence (`h8-clickA`). x: Combination. Click A: the sentence, still declared (`h8-x`, `h8-clickAx`). Click Bump: three Combination swings, 396, 392, 387 left (`h8-bump`). |
| B | Right-click (4,8) | **PASS**. "nothing to do there", the same as plain floor at (7,8) (`b-right48`, `b-right68`). Control: right-click Bump opens "Examine (Xenology)" and "Repair — not a droid" (`b-rightBump`). |
| C | Post C, a stranger | **Bed only here, see below.** From (4,4) the hover and the click agree (`cc-hovC`, `cc-click`, `cc-log`). |
| D | Treat and Repair | **Beside: PASS. Across a closed corner: bed only.** Mate beside her, (6,4) and (6,5): R gives "repair — not a droid", so it gets past the reach question. T gives "treat — no medpac", which refuses before reach comes up (`dd-mate`, `dd-R`, `dd-T2`). |
| E | The tip | **PASS**. See below. |
| F9 | Declared, Lurker | **PASS**. Hover: "Lurker / 95% (needs 2+) / +8 attack · +3 Strength, against Defense 10 / 5 squares · 0 left", no "Provokes" (`f9-hovLurker`). Click: she walks to (6,5). No opportunity line, still 77 of 84. The Lurker joins, and "Inside Reach · … d20 4 … hit · damage 6 … 394 left" (`f9-click`, `f9-click-log`). |
| F10 | Undeclared, Lurker | **PASS**. Hover adds "Provokes an attack from Post" (`f10-hovLurker`). Click: "Opportunity attack: Post attacks Reacher : *hit* : (15 + 1 = 16)", then the punch, 396 left (`f10-click`, `f10-click-log`). |
| F11 | Declared, Talker | **PASS**. Hover: "Talker / 3 squares · 2 left / Provokes an attack from Post", no chance line (`f11-hovTalker`). Click: she walks to (3,6), the Post's opportunity attack hits for 3, no strike (`f11-click`, `f11-click-log`). |
| G | Dice; regression | **PASS**, on the second attempt; see below. 17 lines match (`dice-4`). Slot 74 (reg233), one quick save, load, fight won, Icon Nine 120 of 196 (`reg-end`). |

## C: why it's bed only

From (4,4) the only way to C goes round the wall through (6,4), too far for her movement. The hover says so: "Post C / Not enough movement / Provokes an attack from Post B / Provokes an attack from Bump", with no chance line. The click does the same: she walks 5 squares to (6,5), B and Bump take their opportunity attacks, and there is no strike. On that walk C sees her and joins, so it's no longer a stranger. Coder's bed clears the way by moving Bump and B, which I can't do in the window. The real-window stranger case is F9 to F11.

## D: across a closed corner

The yard's two closed corners have Post A and Post D on the far squares, so I can't stand across a corner from Mate. Bed only, as you allowed. Also, Corner Fist carries no medpac, so Treat says "no medpac" before it asks who is in reach.

## E: the tip

- Reacher, hover on the Runner: the tip sits right of the name panel, all five lines clear, "Provokes an attack from Post" included (`e-hovRunner`).
- Post: the tip flips left of the panel, clear (`e-hovPost`). The same happens on Post B in the Corner Yard (`f6-hovB`).
- Corner Yard Post D, just under the initiative strip: the tip sits below the strip and right of the panel, clear (`b2-hovD1`).
- Point Yard: Near flips left, clear, "−4 point blank" readable (`ep-hovNear`). Two and Far are clear too (`ep-hovTwo`, `ep-hovFar`).
- No creature stands at the board's top-left corner in these yards. Post B (3,3) and Post D (7,1) are the closest.

## Odd on screen, not filed

- The name panel now sits over the hovered creature's own token, on Near and Far in the Point Yard. The diff says the panel stays where K2 has it and only the tip moves, so I took it as intended.
- After A and C join, their turns post an "out of reach" line in round 3 but no line in rounds 4 and 5. A doesn't attack, as step 5 wants. I only noticed the missing line.

## What I got wrong

- **A2, first try.** I clicked Mate, then (6,2), on her turn, so she walked there herself. Mate moves only on its own turn ("Mate is waiting on you"). I restarted from the pristine save and did it that way. The first try's shots are `a2-*`.
- **G, first try.** My script picked save rows from a list that hadn't refreshed. The list orders characters by last played, and a "Four Up" character had moved up, so the dice load and the regression ran on the wrong saves: the dice stopped short and the regression lost. In my data dir that left Four Up with a new Auto Save, a Quick Save and a slot 73 (reg233) from that run. Nothing in the app. I added a check that reads the character name and the row text before each load, then reran: the right Dice One Quick Save, and Icon Nine's slot 72 (reg236).
