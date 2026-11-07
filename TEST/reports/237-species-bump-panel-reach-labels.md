# TEST 237: Low-Light Vision, the hidden bump, the name panel, out of reach, the labels

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-237/` (MAIN_WORK `cbb7ba11`); names in brackets below are files there.

## Builds

- **Steps 1 to 6: app main `e91a568`**, a worktree beside my clone. `gate.py --at e91a568`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at e91a568, 5708 tests, 0 failed". Lodestar `9950093` = the lock.
- **The added step (the owner's line): app main `4f10fda`**, its own worktree. `gate.py --at 4f10fda`, checked three times, last at about 17:30: "SENDABLE — 6 warning(s)" but "NOT FOR TESTER: no passing CORE at 4f10fda". I ran the step anyway because you ordered that build and it is one line on screen. Lodestar `9950093` = the lock. The running app's directory was `builds/test237b`.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf** `9b90871`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: the 233 and 234 tools ran first time (six and three saves). For step 5, I also ran the 225 tool (Staggering) and the 231 tool (Clincher). Every yard run starts from a pristine copy in a relaunched app.

## Summary: two findings, two questions

| # | Check | Build | Result |
|---|---|---|---|
| 1 | Species screen | e91a568 | **PASS**. Aqualish: "Low-light vision / See at full range in dim light. Eyes built for deep water, not for daylight." Nautolan: "Low-light vision / See at full range in dim light." Twi'lek: "Low-light vision / See at full range in dim light." (`s1-aqualish-*`, `s1-nautolan-*`, `s1-twilek-*`) |
| 2 | The hidden bump, in a fight | e91a568 | **PASS from both sides**, with one question (Q2). See below. |
| 2 | The hidden bump, outside a fight | e91a568 | **Question (Q1)**. The reveal starts no fight. See below. |
| 3 | The name panel | e91a568 | **Near and Far PASS; under the strip PASS. FINDING 1**: Two's panel leaves the board. See below. |
| 4 | Out of reach | e91a568 | **PASS**. See below. |
| 5 | Labels | e91a568 | **Staggering Shot, Pinning Fire, Lockdown PASS. FINDING 2**: Clinch. See below. |
| 6 | Dice; regression | e91a568 | **PASS**. The right Dice One Quick Save; the first 17 lines match the baseline. Icon Nine slot 74 (reg233) loaded, saved as slot 75 (reg237), quick save, load, fight won, 127 of 196. |
| + | The owner's line | 4f10fda | **PASS**. "Post E was hiding there.", exactly, outside a fight and in one. See below. |

## 2: The hidden bump (Corner Yard, Corner Fist), e91a568

Post E stands hidden at (4,8), with Post C at (4,7) above it.

**In a fight, from the right.** I bumped Bump from (4,4) to start the fight. Post D, Mate, Post B, Corner Fist and Bump joined, and Post C and Post A joined as she walked. Post E did not, and the strip had seven slots (`d6-at58`). From (5,8), Left:
- "something was waiting there — Post E". The token shows, the strip has eight slots, and "Post E: 400 of 400" is on the roster (`d7-bumpL`).
- Left again was an ordinary strike: "unarmed · rolled 12 — d20 1 … miss" (`d8-bump2L`).
- In round 3: "Post E attacks Corner Fist : *hit* : (18 + 1 = 19)" (`d10-log`).

**In a fight, from the left.** The same start, over two turns to (3,8), then Right:
- "something was waiting there — Post E". The token shows, and the strip has eight slots, with Post E last, after Bump (`e8-bumpR`).
- Right again was an ordinary strike: "rolled 29 … hit · damage 5 … 395 left" (`e9-bump2R`).
- Post E first acted in round 4: "Post E attacks Corner Fist : *miss*" (`e12-log`). See Q2.

**Outside a fight, from the left.** She walked to (3,8) freely, and no fight began. Right:
- "something was waiting there — Post E", and the token shows (`b2-bumpR`). There was no strip and no turn order, still none 5 seconds later (`b2-bumpR-later`).
- The second Right started the fight: "A fight begins.", seven slots with Post E in them, and no strike line (`b3-bump2R`, `b3-log`).
- The third Right was an ordinary strike: "rolled 19 … hit · damage 5 … 395 left" (`b5-bump3R`). Post E then took its turn in round 1: "Post E attacks Corner Fist : *miss*" (`b6-log`).

**Control**: bumping a visible enemy outside a fight does the same. From (5,7), Left into Post C: "A fight begins.", no strike (`c1-bumpC`, `c1-log`). In that run Post E was diagonal to her, joined the fight on its own and attacked from hiding, so I could not use it for the bump (`c1-board`).

## 3: The name panel, e91a568

- **Point Yard, Near**: the panel is centred over Near's head and clear of its token (`s3-pNear`).
- **Point Yard, Far**: the same (`s3-pFar`).
- **Corner Yard, Post D**, at (7,1) right under the strip: the panel sits below the token, clear of it, under the strip and on the board (`s3-hovD`).
- **Corner Yard, Posts A and C**: above the head, clear (`s3-hovA`, `s3-hovC`).

**FINDING 1: Two's panel leaves the board.** In the Point Yard, Two stands in the board's third column. Its panel is centred over its head, and its left edge is at about x 733. The board's left frame is at about x 762, so the panel runs about 28 px past the board, onto the black outside it (`s3-pTwo`, zoomed in `s3-pTwo-zoom`). It is still on screen. The order says the panel always stays on the board.

From the diff (my reading of the code, not something I ran): `_OverTheHead.getPositionForChild` clamps the panel's height to the strip but sets x as the token's centre minus half the panel's width, with nothing keeping it inside the board. So any creature in the first three columns, or the last three, should do this. Two was the only one I could reach.

**Odd, not filed:**
- **Post B, (3,3).** It is two rows under the strip, yet its panel flips below the token and covers Bump at (3,4) (`s3-hovB`). With the larger active portrait the strip reaches about y 233, and above B there is about 4 px too little room for the panel. So "right under the strip" in practice reaches row 3 here.
- **Covering other tokens.** Two's panel, above Two, covers her own token at (2,4) and part of Near (`s3-pTwo`). Post A's panel covers Bump and part of Post B (`s3-hovA`). The order only says the panel never covers its own creature, and none did.

## 4: Out of reach (Corner Yard, Corner Blade, as in TEST 233), e91a568

She bumped Bump from (4,4), walked to (6,4) so A and C joined, walked home to (4,4) in round 2 and stayed there. Mate stood at (8,2) until its round-6 turn, when I moved it to (5,3), behind the closed corner with her (`g5-matemoved`). Each of her turns I hovered A and C. From (4,4) she cannot see A: "You cannot target a creature you cannot see …" (`f3-hovA`).

| Round | Post A | Post C |
|---|---|---|
| 2 | adjacent to her at (6,4): "Post A attacks Corner Blade" | sees her: "out of reach — … Corner Blade is 3 away" |
| 3 to 5 | sees Mate at (8,2): "out of reach — … Mate is 3 away", every round | sees Mate: "out of reach — … Mate is 5 away", every round |
| 6 | Mate moved before A's turn: no line | C's turn came before Mate moved: "Mate is 5 away" |
| 7, 8 | no line | no line |

Lines show in every round where they can see a foe, and in none where they can't (`f5-log`, `g7-log`). Post D, which sees her the whole time, posts "Corner Blade is 3 away" every round. TEST 233's missing rounds 4 and 5 now have their lines.

## 5: Labels (Attack Yard), e91a568

- **Staggering Shot** ends "· movement halved", three times: "d20 11 = 11 vs 21 · movement halved", "d20 8 = 8 vs 21 · movement halved" (a confirmed critical), "d20 2 = 2 vs 21 · movement halved" (`l3-x1a`, `l3-x1b`, `l3-x1c`). The first shot met a natural 20: "d20 20 = 20 vs 21 · resists", with no label, as it should be (`l2-x1`).
- **Pinning Fire** ends "· held": "d20 2 = 2 vs 21 · held" (`l2-x2`).
- **Lockdown** ends "· held": "d20 12 − Lockdown 4 = 8 vs 21 · held" (`l2-x3`).
- **FINDING 2: Clinch** ends "· slowed · cannot make ranged attacks", not "· Slowed". Three Clinches all read the same way, for example "Clinch · unarmed · rolled 31 — d20 20 + attack 8 + Strength 3 · against 14 — win · damage 5 — 1d3 2 + Strength 3 · 395 left · slowed · cannot make ranged attacks" (`m2-a`, crop `m2-a-box`; also `m2-b`, `m2-c`). "slowed" is lower case, and a second clause follows it. That clause is the Clinch row's own wording, which the word guard allows from the TEST 231 ruling (`k2_feedback.dart`). If "ends · Slowed" was shorthand, this is no defect, but it is not what the order says.

## +: The owner's line, 4f10fda

- **Outside a fight**, from (3,8), Right: the status line reads "Post E was hiding there.", exactly, full stop included (`n1-bumpR`, crop `n1-box`).
- **In a fight**, from (5,8), Left: "Post E was hiding there.", and Post E joins the roster at once (`o5-bumpL`). Left again: an ordinary strike, "rolled 12 — d20 1 … miss" (`o6-bump2L`).
- No other wording on screen or in the Combat log, which has no reveal line, the same as on e91a568 (`o7-log`). In the source, the only text for it is the new line and its guard.

## Questions

- **Q1: should a reveal outside a fight start one?** On e91a568 the reveal outside a fight starts nothing. The second bump starts the fight, as for any visible enemy (the control), and only the third bump strikes. The diff guards the join with `if (_fight != null)`, so this looks deliberate. The order's "it joins the fight at once" is true only when a fight is running. Which do you want?
- **Q2: should a creature revealed mid-round act later that same round?** From the left, Post E was revealed on her round-3 turn and its strip slot was after Bump's, later in round 3. Round 3 ended after Bump with no Post E line, and its first turn was in round 4. From the right, its slot fell before hers, so it naturally acted in the next round. It is in the turn order at once either way. The question is whether a slot the strip shows later in the same round should be played.

## What I got wrong

- **Two wrong loads in step 5.** Both times the cause was a loose name pattern. Nothing from those runs is used here.
  - `^Stagger` matched "Stagger Plain" before "Staggering". I saw the name and reloaded with the exact name before acting.
  - For Clincher, the OCR reads "CLUNCHER", so `^CLINCHER$` never matched. The loader then loaded whatever row was showing, and a full scripted run went on "Rapid One", then "Twin One". In my data dir those characters, and Stagger Plain, have new autosaves from that.
- **The guarded loads held.** The dice and regression loads, which matter most, went through the name-and-row check and got the right saves first time. The yard loads have no row check yet; they will next time.
