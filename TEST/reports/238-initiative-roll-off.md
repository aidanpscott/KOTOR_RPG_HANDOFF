# TEST 238: The initiative roll-off

Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots, Combat log text and the quick saves I read are in `KOTOR_RPG_MAIN_WORK/media/screens/test-238/` (MAIN_WORK `5fa16128`); names in brackets below are files there.

## Build

- **App**: main `a8338e9`, a worktree beside my clone. `gate.py --at a8338e9`: "SENDABLE — 7 warning(s)"; "FOR TESTER — CORE at a8338e9, 5709 tests, 0 failed"; ARCHIVE last green at a8338e9. Lodestar `1b24e7e` = the lock.
- **Settings**: defaults (no settings.json), and none at the end. **Shelf** `bdf60a9`, synced; check_shelf clean (33 rules files, 128 blueprints). The order named no Shelf hash, so I took Shelf main; it is one powers.toml note past 237's `9b90871`.
- **Beds**: every `author_tester_*` tool ran first time, with no errors. There is no 226 tool; TEST 226 used the 225 saves. Stagger Plain's seed now reads 3, and Flurry One's and Rapid One's read 1. Every run starts from a pristine copy in a relaunched app.
- **How I read the tie**: the screen shows no initiative numbers, so I quick saved and read each save's `initiative` and `tiebreak` (the roll-off; 0 = none) for every combatant. These are written below as initiative/roll-off.

## Summary: all pass; nothing filed

| # | Check | Result |
|---|---|---|
| 1 | Ties | **PASS**. The game shows the tie only through the strip's order. See below. |
| 2 | Reload | **PASS**. The order and every roll-off value are the same after a load, with no new roll-off, on Flurry One and on a mid-round save of Stagger Plain. |
| 3 | A new joiner who ties | **Bed only**. Four joiners in two yards; none tied. See below. |
| 4 | Regression | **PASS**. Stagger Plain (225), Staggering (226) and Clincher (231), one step each. See below. |
| 5 | Dice; regression | **PASS**. The right Dice One Quick Save; the first 17 lines match the baseline. Icon Nine slot 75 (reg237) loaded, saved as slot 76 (reg238), quick save, load, fight won, 147 of 196. |

## 1: Ties

**Flurry One** (seed 1). Bumping the brute starts the fight. The strip reads W, G, I, B, Flurry One: the gunman before the ironhide (`a2-start`). The save (`a3-quick.mark`): weakling 20/0, gunman 16/18, ironhide 16/9, brute 8/0, Flurry One 7/0. The gunman and the ironhide tie at 16 with the same Dexterity (10 for all four creatures), and the roll-off of 18 against 9 puts the gunman first. The log has the same order: "Weakling attacks … / Gunman attacks … / Ironhide attacks … / Brute attacks …" (`a2-log`).

**How the tie shows: only in the strip's order. There is no wording.**
- The Combat log opens "A fight begins. / Round 1", then the attacks, with no tie line (`a2-log`).
- The strip draws one slot per creature, with no number or mark on the tied pair (`a2-start`).
- Hovering a strip slot shows only the name ("Gunman", "Ironhide") and highlights the token. There is no initiative and no roll-off (`k-hovG`, `k-hovI`).
- Nothing in the app's `lib` prints a roll-off. Lodestar's `_rollOff` sets `tiebreak` and writes no line.

**Flurry One cannot tell the new rule from the old one.** Gunman comes before ironhide by tag too, so the old tag order gives the same strip. Two other beds can tell:
- **Stagger Plain** (seed 3; `g-quick.mark`, strip `g-strip`): brute 12/10, Stagger Plain 12/5, weakling 8/19, ironhide 8/9, gunman 7/0. The strip reads B, Stagger Plain, W, I, G. **Both ties go against tag order**: by tag, "Stagger Plain" would come before "brute.attacks.01" and the ironhide before the weakling. The roll-off decides each one, and one of them includes her.
- **The modifier step**: in **Rapid One** (`c1-quick.mark`), Rapid One 8/0 comes before brute 8/0. The totals tie, Rapid One's Dexterity is 16 (+3) and the brute's is 10 (+0), so the modifier decides and neither rolls off. **Staggering** does the same (8/0 before the brute's 8/0).

## 2: Reload

- **Flurry One**: I quick saved on her round-1 turn and loaded through Load Game. The status line read "the fight resumes — round 1, Flurry One's turn", and the strip again read W, G, I, B, Flurry One (`b1-loaded`). Round 2 played in that order (`b2-log`). Saved again: gunman 16/18, ironhide 16/9, the same as before (`b4-quick.mark`). Her slot is last, so this save comes after everyone else's turn in the round.
- **Stagger Plain, mid-round**: I saved on her round-5 turn with W, I and G still to act (`g-quick.mark`), and loaded it. "the fight resumes — round 5, Stagger Plain's turn", and the strip read B, Stagger Plain, W, I, G (`h1-loaded`). End Turn: "Weakling attacks … / Ironhide attacks … / Gunman attacks … / Round 6 / Brute attacks …" (`h2-log`). Saved in round 6: brute 12/10, Stagger Plain 12/5, weakling 8/19, ironhide 8/9, all unchanged (`h3-quick.mark`).

## 3: A new joiner who ties: bed only

Each joiner's place, read from the save after it joined:
- **Corner Yard, Corner Blade**: the opening was Post D 17, Mate 16, Post B 15, Corner Blade 5, Bump 4. When she walked to (6,4), **Post C** joined on 18 and **Post A** on 12, with no roll-off (`d4-quick.mark`).
- **Corner Yard, Corner Fist**: the same opening and joins. When she bumped the hidden **Post E** from (5,8) ("Post E was hiding there."), it joined on 11, between Post A and Corner Fist (`e7-quick.mark`).
- **Reach Yard, Reacher**: the opening was Runner 16, Post 8, Reacher 7. When she bumped the **Lurker**, it joined on 14 (`f4-quick.mark`). The Talker took a hit (394 left) and did not join (`f3-quick.mark`).

None tied, and these are seeded paths, so a replay gives the same rolls. Bed only.

## 4: Regression

- **225, Stagger Plain** (seed 3): Staggering Shot on the brute. "· d20 17 = 17 vs 18 · movement halved", then "· d20 4 = 4 vs 18 · movement halved", then "… needed 10 … — miss" with no save asked (`g1`, `g2`, `g3`). The first shot staggers, as the reseated bed test says.
- **226, Staggering**: Pinning Fire on the brute: "· d20 17 = 17 vs 21 · held"; the next one misses and asks no save (`i1`, `i2`).
- **231, Clincher**: Clinch on the gunman: "win · damage 5 — 1d3 2 + Strength 3 · 395 left · slowed · cannot make ranged attacks" (`j1`).

## Odd, not filed

- Two app comments still describe the superseded rule. `lib/play/fight.dart:708`: "§9 FORBIDS RE-ROLLS, SO A TIE IS BROKEN DETERMINISTICALLY: higher Dexterity modifier first, then tag order". `lib/play/play_screen.dart:12205`: "PT-1422 breaks a tie on Dexterity then tag". The code is right; only these labels are out of date.
- Lodestar's `_rollOff` says a latecomer who ties a group that has already rolled off rolls alone, and calls that "CODER's reading, awaiting MAIN". No yard gave me that case.

## What I got wrong

- My first load ran in the foreground and hit the tool's timeout, which killed the app before it loaded. I reran it in the background. Nothing from it is used.
- In Corner Blade my first arrow keys came on Mate's turn, so they moved Mate. I ended Mate's turn and walked her on her own turn. The joins above are from her walk.
- Once I pressed F4 with the options menu open, and nothing saved. I saw the save's time had not changed, closed the menu and saved again (`h3-quick.mark`).
- The tightened loader held: every load matched the whole name, and one row check refused the autosave row (WRONG) before I picked the quick save.
