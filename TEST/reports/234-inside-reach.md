# TEST 234: Inside Reach

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-234/` (MAIN_WORK `2bbe6f3c`); names in brackets below are files there.

## Build

- **App**: main `d0eaa56`, a worktree beside my clone. `gate.py --at d0eaa56`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at d0eaa56, 5686 tests, 0 failed"; ARCHIVE last green at d0eaa56. Lodestar `9950093` = the lock. Loom `fcae558` as ordered.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf** `e454ade`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test234_saves.dart` ran first time and wrote both saves; pristine copies kept.

## Summary: 1 to 8 pass; one small finding

| # | Check | Result |
|---|---|---|
| 1 | The list | **PASS**. Reacher, empty hands: x steps Inside Reach, Boxed In, Smother, then back to Strike (`r-x1` to `r-x4`). |
| 2 | Inside Reach on the Runner | **PASS, see the finding**. Hover: "Runner · 95% (needs 2+) · +8 attack · +3 Strength · +2 closed on a ranged weapon, against Defense 10 · 5 squares · 0 left · Provokes an attack from Post" (`r-hov-inside-full`). Click: she walks to (6,3), "Opportunity attack: Post attacks Reacher : *hit* : (15 + 1 = 16)", then "Inside Reach · unarmed · rolled 27 — d20 14 … 395 left". No "cannot move away" (`r-inside-hit`, `r-log1`). |
| 3 | The Runner's turn | **PASS**. The opportunity question appears ("Runner leaves your reach"), I answered No, and it goes from (7,2) to (7,0) (`r-after-et2`). |
| 4 | Boxed In, a hit | **PASS**. "Boxed In · … 389 left · cannot move away from you" (`b-hit`). Its next turn: it stays at (7,0), and still shoots. No question. The turn after: the question, then it goes to (9,0) (`b-et1`, `b-et2`, `b-log`). |
| 5 | A miss | **PASS**, on the second try; see below. "Boxed In · unarmed · rolled 14 — d20 1 … needed 10 · 1 square — miss", no such line (`miss-open-screen`). Its turn: the question, then (7,2) to (7,0) (`miss-open-after`, `miss-open-log`). |
| 6 | Reload between the hit and its turn | **PASS**. Boxed In hit at (9,0) (`c-hit`), F4, load the Quick Save: "the fight resumes — round 5, Reacher's turn" (`c-loaded`). End Turn: it stays at (9,0), no question (`c-et1`). The turn after: the question, then (11,0) (`c-et2`). |
| 7 | Smother, a hit | **PASS**. "Smother · … 379 left · cannot move away from you" (`s-hit`). Stays at (11,0), then the question and (13,0) (`s-et1`, `s-et2`, `s-log`). |
| 8 | Reach Blade | **PASS**. Each x press: "Inside Reach needs empty hands"; nothing declared (`rb-x1` to `rb-x3`). A click on the Post is a plain Vibroblade swing (`rb-swing`). |

Dice and regression are in the TEST 235 report; they ran once after both.

## Finding

1. **The target's name panel covers part of the hover tip, including the provoke warning.**
   - Reacher, Inside Reach, hover on the Runner at (7,2): the "Runner · Level 1" panel sits over the left of the tip. The red line reads "Provokes a…ack from Post", with the covered letters only faint through the panel, and "+8 attack" and "5 squares" are dimmed the same way (`r-hov-inside-full`).
   - The tip's first line is covered the same way on Near in the Point Yard, where the name reads faintly (TEST 235 `p-hov-plain-near`).
   - The numbers can be made out. The warning is the line a player most needs before a walk.

## What I got wrong on step 5

A swing at these odds misses only on a natural 1, so I looped Boxed In swings until one came. On the first try I had walked her to (13,1) with the Runner at (13,0), the corner. That swing missed (`miss-screen`) and the Runner stayed put, with no question (`miss-after`, `miss-log`). That proves nothing, since no square next to it is further from her. So I restarted from the pristine save and looped with the Runner held in open floor at (7,2). The eighth swing missed, and it backed away. I'm not filing the corner stay: (12,0) is no further from her, and (11,0) would need a walk past her.

## Not reachable here

Smother's Disengage rule: the Runner never Disengaged, so I saw only the line and the hold. I left step 2's enemy provoke alone, as you said it's changing.
