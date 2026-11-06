# TEST 235: Point Blank Shot

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and Combat log text are in `KOTOR_RPG_MAIN_WORK/media/screens/test-235/` (MAIN_WORK `2bbe6f3c`); names in brackets below are files there.

## Build

Same as TEST 234: app main `d0eaa56`, gate SENDABLE (6 warnings), CORE 5686/0, Lodestar `9950093` = the lock, Loom `fcae558`, Shelf `e454ade`, check_shelf clean, defaults. `author_tester_test235_saves.dart` ran first time and wrote all three; pristine copies kept.

## Summary: 1 to 7, dice and regression pass; one question

| # | Check | Result |
|---|---|---|
| 1 | The list | **PASS**. Pointer: x steps Point Blank Shot, Lethal Shot, Execute, then back to Shoot (`p-x1` to `p-x4`). |
| 2 | Nothing declared, Near | **PASS**. Hover: "65% (needs 8+) · +8 attack · +2 Dexterity · −4 point blank, against Defense 14" (`p-hov-plain-near`). The shot: "rolled 16 — d20 10 + attack 8 + Dexterity 2 − point blank 4 · needed 14 · 1 square" (`p2-plain-N`). |
| 3 | Declared hovers | **PASS**, table below. |
| 4 | Hits on Near and Two at each tier | **PASS**, table below. Each line reads "needed 10 (−4 Dexterity: <tier name>)". A plain shot at Two reads "needed 14" (`p4-plain-T`), so Defense is 4 lower. |
| 5 | Hits on Far | **PASS**. Tier 1: "− Point Blank Shot 2 · needed 14 — hit · damage 10 — 1d8 8 + Dexterity 2" (`p5-t1-F`). Tier 3: "− Execute 2 · needed 14 — hit · threat not confirmed … damage 3 — 1d8 1 + Dexterity 2" (`p5-t3-F`). Tier 2 missed, with "− Lethal Shot 2 · needed 14" (`p5-t2-F`). No dice, and Dexterity kept at every tier. |
| 6 | Point Pair on Near | **PASS**. Main-hand miss, swing 23: "rolled 10 — d20 1 … dual-wield 3 + Point Blank Shot 2 · needed 10 … — miss · off-hand: Blaster Pistol · rolled 28 — d20 19 … + Point Blank Shot 2 … hit · damage 6 — 1d8 1 + 1d6 3 + Dexterity 2" (`pp-23`). On the other 22 turns both hands hit: the main hand took the 1d6 and the off hand took none (`pp-1` to `pp-22`). Neither hand has the −4. The undeclared hover does, beside the −3 dual-wield (`pp-plain-N`). |
| 7 | Point Blade | **PASS**. x does nothing at all: four presses, and the box doesn't change (`pb-after-x`). |
| | Dice | **PASS**. All 17 lines match the 206 baseline (`dice-*`). |
| | Regression | **PASS**. Save to slot 71 ("reg234b"), one quick save (one `quick.mark`), Load, and a fight won (Icon Nine 127 of 196) (`reg2-*`). |

### Step 3, hovers

| | Near (1 square) | Two (2 squares) | Far (4 squares) |
|---|---|---|---|
| Nothing declared | 65%, −4 point blank, Defense 14 | 85%, Defense 14 | 85%, Defense 14 |
| Point Blank Shot | 95%, +2, Defense 10, no −4 | 95%, +2, Defense 10 | 75%, −2, Defense 14 |
| Lethal Shot | 95%, +3, Defense 10, no −4 | 95%, +3, Defense 10 | 75%, −2, Defense 14 |
| Execute | 95%, +4, Defense 10, no −4 | 95%, +4, Defense 10 | 75%, −2, Defense 14 |

### Step 4, hits

| Tier | Near | Two |
|---|---|---|
| Point Blank Shot | d20 12, +2, 15 damage: 1d8 7 + 1d6 6 + 2 (`p4-t1-N`) | d20 20, threat confirmed, 14 damage: see the question (`p4-t1-T`) |
| Lethal Shot | d20 19, +3, 14 damage: 1d8 6 + 2d6 2+4 + 2 (`p4-t2-N`) | d20 2, +3, 14 damage: 1d8 7 + 2d6 4+1 + 2 (`p4-t2-T`) |
| Execute | d20 8, +4, 18 damage: 1d8 8 + 3d6 1+6+1 + 2 (`p4-t3-N2`); a first try missed on a natural 1 (`p4-t3-N`) | d20 12, +4, 10 damage: 1d8 1 + 3d6 2+2+3 + 2 (`p4-t3-T`) |

After those shots, an undeclared hover on Two reads 85% against Defense 14 again (`p-after-plain-T`).

## Question

**Does the chain's die multiply on a critical?** Point Blank Shot on Two, confirmed: "damage 14 — 2d8 1+1 + 2d6 3+5 + Dexterity 2x2 x 2 critical", so the 1d6 became 2d6. ATTACKS-01 says that of the Power chain's dice ("multiplied on a critical"), so it may be as meant; I found no such line for this chain. Not filed. Tell me if it's wrong.

## Notes on how it ran

- **Regression, first attempt invalid.** My script's click landed before the save list had filled, so it took the Auto Save from the end of TEST 232's fight. It saved that as slot 70 ("reg234") and read "FIGHT OVER 0" at 130 of 196. That's a script timing error and nothing in the app; I reran from REG232 (slot 69) with longer waits. Slot 70 stays in my data dir, post-fight, and isn't a usable base.
- **Point Blade came up by accident.** My name match missed "Pointer", which OCRs empty, so I picked it by reading the panel directly. Step 7's run is still the Point Blade save, checked by name in the box.
- **Known, not filed:** Lethal Shot's and Execute's text mentioning a death threshold.
- Point Pair at tiers 2 and 3 wasn't ordered and wasn't run.
