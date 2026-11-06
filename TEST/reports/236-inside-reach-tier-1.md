# TEST 236: Inside Reach, tier 1 changed

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-236/` (MAIN_WORK `ab3641d5`); names in brackets below are files there.

## Build

- **App**: main `85a5a63`, a worktree beside my clone. `gate.py --at 85a5a63`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at 85a5a63, 5692 tests, 0 failed"; ARCHIVE last green at 85a5a63. Lodestar `9950093` = the lock. Loom `fcae558` as ordered.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf** `29ec5aa`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test234_saves.dart` ran first time. Each run below starts from a pristine copy of `reacher.sav` in a relaunched app. The yard opens with the Runner at (7,2), the Post at (3,4), the Lurker at (7,6), and her at (2,4) (`start`).

## Summary: 1 to 4, dice and regression pass; one finding, one question

| # | Check | Result |
|---|---|---|
| 1 | Nothing declared | **PASS**. Hover on the Runner: "Provokes an attack from Post" (`h1-plain-full`). Click: "Opportunity attack: Post attacks Reacher : *hit* : (15 + 1 = 16)", 3 damage, then she punches the Runner from (6,3) (`s1-click`, `s1-log`). |
| 2 | Declared, each tier, a fresh fight each | **PASS**. In each run I hovered undeclared first as the control, and it read "Provokes an attack from Post" (`t1-hov0` to `t3-hov0`). Declared, the line is gone (`t1-hov`, `t2-hov`, `t3-hov`). Click: she walks to (6,3) and strikes, no opportunity line in the log, and she stays at 77 of 84 (`t1-click`, `t2-click`, `t3-click`, `t1-log` to `t3-log`). Tiers 2 and 3 still end "cannot move away from you". |
| 3 | Declare, strike the Post beside you, step away | **PASS**. "Inside Reach · unarmed · rolled 26 … 394 left" (`s3-strike`). Left arrow to (1,4): "Post catches Reacher leaving — … hit · damage 2 … 75 left" (`s3-step`, `s3-log`). Tier 1 only. |
| 4 | Declared, click the Lurker | **PASS as ordered, see the finding and the question**. She walks to (6,5): "Opportunity attack: Post attacks Reacher : *hit* : (15 + 1 = 16)", 3 damage (`s4-click`, `s4-log`). Tier 1 only. |
| Dice | Baseline comparison | **PASS**. 17 lines match (`dice-4`). |
| Regression | Slot, quick save, load, the fight | **PASS**. Slot 72 (reg236), one quick save, load, fight won: "FIGHT OVER", Icon Nine 74 of 196, force 97 of 97 (`reg-end`). |

Step 1 gives the control for steps 2 and 4: same opening, same dice. The Post's opportunity roll is 15 + 1 in steps 1 and 4 and absent in step 2.

## Finding

1. **The hover on the Lurker is blank, and the click provokes.**
   - Declared, hovering the Lurker at (7,6) from (2,4): no tip, no route, no "Provokes an attack from Post" (`s4-hov`). The click then walks her out of the Post's reach and the Post swings.
   - I saw this declared only. The code has no branch on the declaration here: `lib/play/play_screen.dart:8153`, `if (stranger) return null`, so undeclared should be blank too.
   - TEST 232's ruling was that the hover must say what the click says. That fix covers the click's refusal; this is a click that goes ahead.

## Question

1. **Should the Lurker click strike at the end of the walk?**
   - Your step says the exemption "needs a strike that can follow". One did follow here: on arrival the Lurker is in the fight and she strikes it with the declaration, "Inside Reach · unarmed · rolled 16 — d20 5 … 396 left" (`s4-click`). So she paid the Post's swing and still got the strike.
   - Your step only says she walks and the Post swings, so I'm not calling this wrong. The app's test says "a creature the strike cannot reach"; on screen it could be reached.

## Not covered

- Steps 3 and 4 on tiers 2 and 3.
- The push on a boxed target, and the `reach-shove` save the tool now also writes. Neither was in the order.
- The regression's 74 of 196 is lower than the last two runs (127, 130). My fight script isn't a pinned sequence, so I didn't compare them; the fight was won.

Known, not filed: the name panel over the tip. It covers part of the Runner's tip in every hover here.
