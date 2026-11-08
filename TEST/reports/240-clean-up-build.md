# TEST 240: The clean-up build (Post B's panel, the panel checks again, a wide regression)

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the quick save I read are in `KOTOR_RPG_MAIN_WORK/media/screens/test-240/` (MAIN_WORK `ad041ac8`); names in brackets below are files there. Pixel positions are on the 1920×1080 screen.

## Build

- **App**: main `9cbbe6f`, a worktree beside my clone, built through the lock. `gate.py --at 9cbbe6f`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at 9cbbe6f, 5712 tests, 0 failed"; ARCHIVE last green at 9cbbe6f.
- **Lodestar**: the app's lock at `9cbbe6f` pins **`1b24e7e`**, and that is what compiled (package_config.json), not `ffa5b13` from the order. `ffa5b13` is Lodestar main, one commit later. From `1b24e7e` to `ffa5b13` the diff is a `.gitattributes`, one doc comment in `round.dart` ("CODER's reading, awaiting MAIN" becomes "MAIN, PT-2752") and three `!` dropped in a Lodestar test. No library code changes, so I went ahead. Loom has no entry in the app's lock.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf**: `bdf60a9` (= main), check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: every `author_tester_*` tool ran first time, with no errors. Every run starts from a pristine copy in a relaunched app, except where noted under Power below.

## Summary: every step passes, no findings

| # | Check | Result |
|---|---|---|
| 1 | Post B | **PASS**. The panel stands above, top y 239, x 733 to 1110, and covers no slot. |
| 2 | TEST 239's panel checks | **PASS**. Two, first and last column are pixel for pixel as on 5dfd3ab. The last column still flips below, under W and B. |
| 3 | Regression | **PASS**. Level-up Cancel on every page this level-up has (no Forms page came up); a fight won; Power, Cleave, Spray, Clinch chains; a mid-fight save and load. |
| 4 | Dice | **PASS**. The right Dice One Quick Save; the first 17 lines match the baseline. |

## 1: Post B (Corner Blade)

Corner Blade walked from (4,4) to (6,4) (Up, Right, Right, Down), A and C joined, and on her turn I hovered Post B at (3,3) (`s1-hovB`, `s1-hovB-crop`).

- **The panel stands above Post B**: top edge y 239, left edge x 733, right edge x 1110, bottom y 322 (84 tall). Post B's ring starts at y 280, inside its square, so the panel is clear of it.
- **No slot covered**: the small slots end at y 210 to 211. The large active slot (hers, x about 1102 to 1230) ends at y 234, 5 px above the panel's top. Its orange bar (x 1102 to 1108) still sits over the panel's right end, but above it.
- This is the position the order gives.

## 2: TEST 239's panel checks

- **Point Yard, Two** at (2,6), after bumping Right to start the fight (`s2-hovTwo`): left edge on the frame (x 760 to 762), right edge x 1138, y 406 to 514; Two's ring starts at y 543. It stands above Two. The shot matches TEST 239's pixel for pixel. (The panel is 108 tall here because of its "noticing" line, and it sits over Pointer's own token at (2,4), as it did on 5dfd3ab.)
- **First column**, Charged One, the same chase as TEST 239: the Weakling followed to (0,4) (`c2-walk` to `c9`). Its panel's left edge is on the frame (x 856 to 858), right edge x 1234, top y 303. The slots end at y 260, and the Weakling's square starts at y 402. It stands above (`s2-hovFirst`).
- **Last column**, Charged One, the same knockback ("· prone — d20 18 = 18 vs 21 · takes hold", `c1-shot`): the brute at (8,4). The panel spans x 1056 to 1434 (right frame 1433 to 1435), y 484 to 593, **below** the brute (`s2-hovLast`). Standing above, a 110-tall panel would start at about 402 − 16 − 110 = 276. The W and B slots inside its width end at y 335, so it would overlap them by about 59 px. **The flip is the real-overlap case.** Pixel for pixel the same as TEST 239.
- In all three, nothing covers its own creature or a strip portrait.

## 3: Regression

**Level-up Cancel** (Watch Two, `lu193-guard6b`: Guardian 6 / Watchman 1, level 7, 28000 XP, needed 0, so the level-up is to 8):
- **Class page**: Cancel goes back to play (`l2-classcancel`). There is no hub yet at that point; this is TEST 193's behaviour.
- The hub at level 8 lists Attributes, Skills, Feats, Powers, a gap, then Attacks (`l3-hub`). For each page I spent something, pressed Cancel, checked the hub still shows that step as current, then reopened it to check it was undone:
  - **Attributes**: Strength 14 to 15, Remaining 0; Cancel: hub, Attributes still step 1, Strength 14 (`l4-attr-plus`, `l5-hub-afterattr`).
  - **Skills**: Acrobatics 0 to 1, Remaining 10 to 8; Cancel: hub, Skills still current; reopened: Acrobatics 0, Remaining 10 (`l7-skills-plus`, `l8-hub-afterskills`, `l9-skills-again`). OK with points left gives K2's "You have not spent all of your skill points…" prompt.
  - **Feats**: Perceptive added, Remaining 0; Cancel: hub, Feats current; reopened: Remaining 1 (`l11-feats-add2`, `l12-*`).
  - **Powers**: Heal added, Remaining 0; Cancel: hub, Powers current; reopened: Remaining 1 (`l14-powers-add`, `l15-*`).
  - **Attacks**: one added, Remaining 0; Cancel: hub, Attacks current; reopened: Remaining 1 (`l17-attacks-try`, `l18-*`).
- **Nothing spent**: Cancel, Back, then Cancel on the Class page to leave. The sheet still reads "Jedi Guardian 6 / Jedi Watchman 1 · 7", the same six abilities, 59/59, 57/57, 28000, and Level Up is still offered (`l20-sheet-after`; before: `w1-sheet`).
- **Forms: not reached.** Neither Watch Two (to 8) nor Watch Six (`lu193-guard6`, to 7, `x2-hub`) shows a Forms row; both have the gap where it would sit. No level-up save I hold offers one.

**A plain fight won**: Icon Nine. I loaded slot 77 (reg239), saved it as slot 78 ("reg240", 11:24:08), pressed Escape then F4 (one quick save, 11:24:13), loaded slot 78 and won the fight: "Icon Nine: 117 of 196" (`reg-loadlist`, `reg-end`).

**Declared chains**, one per roster:
- **Power** (Power One, `tester-power`; bump the thug, End Turn, x, Right): "Power Attack · Vibroblade · rolled 24 — d20 15 + attack 8 + Strength 4 − Power Attack 3 · needed 10 — hit · damage 16 — 1d10 4 + 1d6 6 + Strength 6 · 384 left · prone — d20 5 = 5 vs 22 · takes hold" (`pw1`).
- **Cleave** (Cleaver; bump the brute, End Turn, x, Right): "Cleave · Brute · Vibrosword · rolled 17 — d20 9 + attack 8 + Strength 3 − Cleave 3 · needed 10 — hit · damage 9 — 1d12 5 + Strength 4 · 391 left", then "Ironhide · Vibrosword · rolled 11 — d20 3 … − Cleave 3 · needed 16 — miss" (`v1`).
- **Spray** (Sprayer; bump Bump, End Turn, x, click Post A): "Spray · Post A · Blaster Pistol · rolled 19 — d20 12 + attack 8 + Dexterity 2 − Spray 3 · needed 10 — hit · damage 9 · 391 left", then "Post C · … rolled 25 — d20 18 … − Spray 3 — hit · damage 3 · 397 left". Same pair as TEST 231 (`sp2-hover`, `sp3-spray`).
- **Clinch** (Clincher; bump Up, End Turn, x, Up): "Clinch · unarmed · rolled 22 — d20 9 + attack 8 + Strength 3 + closed on a ranged weapon 2 · against 10 · 1 square — win · damage 5 — 1d3 2 + Strength 3 · 395 left · slowed · cannot make ranged attacks", word for word TEST 238's (`k1`). The Gunman's next attack: "Gunman attacks Clincher : *miss* : (2 + 2 = 4) · Flanking +2" (`k2-log`).

**A save and a load mid-fight** (Clincher, round 3, her turn): before, the Gunman was at 395 and Clincher at 64 of 84 (67 − 2 − 1 from the round-3 hits). F4 wrote `quick.mark` at 11:33:26, with order weakling, brute, ironhide, gunman, Clincher, round 3 (`k4-quick.mark`). Load (name and Quick Save row checked): "the fight resumes — round 3, Clincher's turn", Gunman 395 of 400, Clincher 64 of 84, the same hover (`k3-hov-before`, `k5-afterload`, `k5-hov-after`).

## 4: Dice

The right Dice One Quick Save; the first 17 lines match the TEST 206 baseline (SAME17).

## Odd, not filed

- **Two tools write `power-one.sav`.** `author_tester_test215_saves.dart` (Power Attack, `tester-power`) and `author_tester_test221_saves.dart` (enemy powers, `tester-powers`) both write it, and the 221 tool runs later, so regenerating every save leaves only the 221 bed. For the Power chain I re-ran the 215 tool alone and loaded its copy from the Tester Power card; afterwards I put the 221 copy back. This is test tooling, not the app.
- On the level-up hub, the ability column still reads Strength 14 after Attributes OK with the point on Strength. 5dfd3ab does the same with the same steps (`z239-hub-attrdone` beside `l6-hub-attrdone`), so this build didn't change it.

## What I got wrong

- Three loads stopped at the name check and loaded nothing: Jedi Arm's name needs the larger OCR scale; I gave findpkg "Store Bed" in the wrong order; and "Power One" sits in Tester Powers, not Tester Power. The loader now takes an optional scale and single-line mode. Jedi Arm turned out to be level 1 with no XP, so she wasn't used.
