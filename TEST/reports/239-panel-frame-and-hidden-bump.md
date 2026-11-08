# TEST 239: The name panel inside the frame, Post B, and the hidden bump (Q1, Q2)

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the quick saves I read are in `KOTOR_RPG_MAIN_WORK/media/screens/test-239/` (MAIN_WORK `bdb67f89`); names in brackets below are files there. Pixel positions are on the 1920×1080 screen.

## Build

- **App**: main `5dfd3ab`, a worktree beside my clone. `gate.py --at 5dfd3ab`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at 5dfd3ab, 5711 tests, 0 failed"; ARCHIVE last green at 5dfd3ab. Lodestar `1b24e7e` = the lock.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf**: main, `bdf60a9`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: every `author_tester_*` tool ran first time, with no errors. Every run starts from a pristine copy in a relaunched app.

## Summary: one finding

| # | Check | Result |
|---|---|---|
| 1 | Name panel at the frame | **PASS**. Third, first and last columns. See below. |
| 2 | Post B | **FINDING 1**. It flips below even though the slot directly over B leaves room. See below. |
| 3 | Q1, outside a fight | **PASS**, but no initiative line shows. See below. |
| 4 | Q2, in a fight | **"Past" PASS from both sides. "Still to come" not reachable**: Post E always joins on 6, ahead of her 5. See below. |
| 5 | In a fight, first bump then second | **PASS**. The first bump spends nothing; the second is an ordinary strike. |
| 6 | Dice; regression | **PASS**. The right Dice One Quick Save; the first 17 lines match the baseline. Icon Nine slot 76 (reg238) loaded, saved as slot 77 (reg239), quick save, load, fight won, 95 of 196. |

## 1: The name panel at the frame

The panel is 376 px wide.

- **Point Yard, Two** in the third column, at (2,6): the board's left frame is at x 760 to 762, and the panel's left edge is on it (x 760 to 762, right edge x 1138). Centred over Two it would start at about 734, so it has slid about 28 px to the right. It stands above Two, clear of the token and under the strip (`s1-hovTwo`).
- **First column**: the Point Yard creatures do not move toward her, so I used the Attack Yard. In **Charged One** she walked to (0,3), then (0,5), and the Weakling followed to **(0,4)**. Its panel's left edge is on the left frame (x 856 to 858). It stands above the Weakling: panel top y 303, slot bottoms y 260, Weakling square from y 403 (`s1-hovFirst`).
- **Last column**: in **Charged One**, the knockback threw the brute to **(8,4)** ("· d20 18 = 18 vs 21 · takes hold"; `c1-shot`). Its panel spans x 1056 to 1432, inside the right frame (x 1433 to 1435). Centred, it would run to about 1590. Here it stands below the brute (top y 484), clear of the token, because the W and B slots are over it (`s1-hovLast`).
- In all three, nothing covers its own creature or a strip portrait.

## 2: Post B (Corner Blade, the seven-slot strip, her turn)

After she walked to (6,4) and A and C joined, the strip read P, P, Mate, P, P, Corner Blade (large, active), B. I hovered Post B at (3,3) (`s2-hovB`).

- **The slot directly over B** (square x 890 to 954) is the **fourth slot, Post B's own small slot**, at x 923 to 986. Mate's slot (830 to 892) ends just left of it. **It is not the large active one.** The small slots' bottoms are y 210 to 211.
- **Room above**: the panel is 84 px tall (y 420 to 503 where it stands). B's square starts at y 339, and the gap is about 16 px (the Weakling's panel sat 16 px above its square). Above, it would stand at about 339 − 16 − 84 = 239. The ceiling from the small slots is about 211 + 16 = 227. **So the slot directly over B leaves room, and the panel should stand above.**
- **What it does**: it **flips below** (top y 420, x 733 to 1110).
- **Why, as I measure it**: the panel's right end (x 1110) reaches under the **active slot**, her own, whose orange bar is at x 1102 to 1108 and whose portrait ends at about y 234. That ceiling, about 234 + 16 = 250, is more than 239. The code takes its ceiling from every slot under the panel's width (`_OverTheHead._under`). That one slot, 8 px into the panel's right end, decides the flip, not the slot directly over B.

**FINDING 1**: the order says the panel stands above B when the slot directly over it leaves room. It does leave room, by about 12 px, yet the panel flips below, because of the active slot at the panel's far right end. This is my reading from the pixels, not something I could vary in the window: the active slot is always hers or Mate's when I can hover.

## 3: Q1, outside a fight (Corner Fist)

She walked from the start to (3,8) with no fight, then Right into the hidden Post E (`q1-bump1`, rapid shots `q1b-1` to `q1b-8`):
- **Line 1 is "Post E was hiding there."**, then "Mate is waiting on you".
- **The fight begins**: "Enemy Sighted / Combat Round 1" shows on the pause box (`q1b-1`), and the Combat log reads "A fight begins." (`q1-log1`).
- **Post E is on the strip**: seven slots, A, Mate, C, Bump, B, Corner Fist, Post E. The roster lists "Post E: 400 of 400".
- **Nothing is rolled**: there is no strike line, and Post E stays at 400.
- **No initiative line shows.** Post A won initiative, so the enemy turns ran at once and "Mate is waiting on you" replaced the "initiative — …" line within 0.4 s. In the code, `_begin` sets the initiative line, then `_enemyTurns` overwrites it whenever a creature acts before her. That is the same for any fight she doesn't open. So "the initiative line" from the order did not show here.
- **On her turn**, Right into Post E again: "unarmed · rolled 19 — d20 8 + attack 8 + Strength 3 · needed 10 — hit · damage 5 — 1d3 2 + Strength 3 · 395 left" (`q1-bump2`, `q1-log2`).

## 4: Q2, in a fight

**From the right** (Corner Fist, bump Bump, then to (5,8) over two turns; Left into Post E in round 2):
- "Post E was hiding there.", and the strip has eight slots (`r5-revealR`).
- Post E's slot is sixth, just before hers, and **greyed with the slots already past**; Bump's, after hers, is bright.
- Round 2 has no Post E line (`r7-log`). Its first line is in round 3, right after Post A's slot: "Post E attacks Corner Fist : *hit* : (18 + 1 = 19)" (`r8-log`).

**From the left**, round-3 reveal (Corner Fist from (2,8), Right to (3,8), Right into Post E; `l5-revealL`, `l5-quick.mark`):
- Post E joined on **6**: order D 17, Mate 16, B 15, A 11/18, C 11/1, **E 6**, Corner Fist 5, Bump 4. Its slot is again before hers, greyed as past.
- **The 237 case (Post E after Bump) did not happen.** On this build Post E rolls 6 every time. Corner Blade on the same route gave the same 6 (`m6-quick.mark`), and so did revealing a round later, in round 4 (`n4-revealL`, `n4-quick.mark`).
- In that round-4 run, round 4 has no Post E line, and its first attack is in round 5: "Post E attacks Corner Blade : *miss*" (`n6-log`).

So "the slot after Bump's isn't greyed and acts in round 3" is **not reachable** in the Corner Yard on this build. **Bed only.**

**A joiner tie, by the way** (the TEST 238 step 3 case): in those runs **Posts A and C both joined on 11** and rolled off **18 against 1**, so A comes first. Tag order would put A first too, so it doesn't separate the rules.

## 5: The first bump, in a fight

From the right: the first Left revealed Post E with no strike line and nothing spent ("Post E was hiding there."). The second Left was "unarmed · rolled 12 — d20 1 + attack 8 + Strength 3 · needed 10 — miss" (`r6-strikeR`).

## Odd, not filed

- The Pointer save's name OCRs as empty in my old loader. I loaded it with a whole-line check that reads "POINTER" (single-line OCR) and a row check, so the load was the right one. That's my tooling, not the app.

## What I got wrong

- My first first-column try clicked (0,0) in the Attack Yard, which is under the strip's "I" slot, so nothing happened. I walked to (0,3) instead. On the Point Yard try, Near did not follow her into column 0; those yard creatures stay put.
- From the left, my first walk took three turns to reach (2,8), not (3,8), so the reveal came in round 3 from (2,8) via one step Right. That is still MAIN's "round-3 reveal from the left".
