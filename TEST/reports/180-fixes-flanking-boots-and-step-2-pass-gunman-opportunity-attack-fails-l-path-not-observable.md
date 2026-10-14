# TEST 180: the TEST 179 fixes, flanking, boots Defence, an L approach, PT-2749 step 2, and attacks of opportunity

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-180/` (MAIN_WORK `f77675c4`, prefix per item). The step-by-step log is `TEST/reports/180-running-log.md`.

## Build

- **Main run, app `617578e`**, git archive to `~/kotor-tester/builds/test180`. Lodestar `d8390023997fdb17e4e897bafe70f14254f494fd` = lock = compiled. Lens `fe10327793b1a28882b088d2fbf8148e83ead926` = lock = compiled. Loom has no entry in the lock.
- **Amendment re-checks and item 16, app `4c01d57`**, `~/kotor-tester/builds/test180b`. Lodestar `17754af47278c63621fd3323c8362cf0bbd09cf1` = lock = compiled. Lens `fe10327` = lock = compiled.
- Shelf `1e3ffb4` (= origin). check_shelf clean (31 rules files, 118 blueprints). `tool/env.sh` sourced. Both builds went through `tool/one_at_a_time.sh` (11 s each), and `pubspec.lock` was unchanged. Every `dart run` went through the lock; my fixture runs waited about 40 minutes on Coder's full suite. The bundle was launched outside the lock.
- Fresh fixtures: chargen characters and authored saves (specs in `~/kotor-tester/notes/fixtures/specs180*`). Local beds, my data dir only: `tester-mines`, `tester-lshape`, `tester-nine`, `tester-rflank`, `tester-oa-droid`, plus `tester-rough` from TEST 179.

## Summary: thirteen pass, one fail inside item 16, and two parts not observable

| # | Check | Result |
|---|---|---|
| 1 | Rough-ground label | **PASS**: "2 squares (3 movement) · 2 left" from (6,2) to rough (5,1); "4 squares · 1 left" without rough ground |
| 2 | Move counter | **PASS** after a click and at a turn change. **Note**: at a turn start beside rough ground, with the pointer off the board, the legend reads "5 → 3 move" (PT-1519's next-step-onto-rough preview, per Coder). MAIN to rule whether a preview with no pointer is wanted |
| 3 | Clicks and mines | **PASS**: a click just outside the grid does nothing. Routes go round noticed mines in and out of a fight. Hovering the mine square shows "Walks onto a mine" |
| 4 | Health after a mine | **PASS on both builds**: the centre line and the bar read the same number. On 4c01d57: mine 8 of 11, save, app restart, Continue: 8. Rest "8 → 11", save, restart: 11. (617578e already kept the mine damage across a reload, unlike Coder's note.) |
| 5 | Placeables | **PASS**: the panel, footlocker, console and a found hidden crate each block ("the Security Console is in the way"), and routes go round. An unfound hidden crate does not block. **Finding**: it is still drawn from the start (see below) |
| 6 | Terminal panel | **PASS**: "POWER COUPLING ONLINE — OUTPUT 100%" after the repair. Dimmed replies fit ("— you have 0 spikes") |
| 7 | Store, organic and Treaded | **PASS**: "In Inventory 0 · Only a droid can fit a motivator.", with no "replaces" line |
| 8 | Equip | **PASS**: "Silenced Motivator" fits. The three implant feats show three tier icons. Switch Weapons on Kael's turn shows "switching weapons — it is Kael's turn; wait for your own" inside Equip |
| 9 | Move-and-attack tooltip | **PASS**: the ghost and the target ring are visible. **Note**: the combat log panel can still cover the tooltip for targets right of centre |
| 10 | Flanking | **PASS**: straight, diagonal and enemy pair give +2. The L gives none, and a downed ally gives none. On 4c01d57, ranged: on the line at 7 squares (half the rifle's 14) +2 for both me and Kael; at 8 squares none; off the line none |
| 11 | Boots Defence | **PASS**: names exact. Over Heavy Leather Armour (DEF 17): Sith Trooper 18, Mandalorian 19, Krath 20, Vanguard 20 (DEX 15), on Equip and the sheet. In a fight with Krath every attack reads "needed 20" |
| 12 | L-shaped approach | **PARTIAL**: four-way holds (the droid covered a 3-across, 2-down offset in exactly 5 squares), and AUTO Kael closed and fought. **Not observable**: whether the path was an L or a staircase, because every move is drawn as a jump (10 fps capture: one frame at the start, the next at the end). **Seen**: with two targets far apart, one droid alternated targets for 17 rounds and never reached either |
| 13 | Combat log and banners | **PASS**: rounds, every action with its result beneath, the opportunity attack included, names not tags. Banners hold 2.4–2.5 s. Wording is recorded below. **Notes**: the panel shows only the last six entries (no scroll back), sits over the board's bottom-right corner hiding tokens and paths, and banners appear for attacks only, not for a move or a pass |
| 14 | Hover and strip | **PASS**: name, level and bar, plus a red dashed 3×3 ring, diagonals included. The gunman shows no ring. Strict initiative order, the actor raised, hourglasses. Ten tiles fit. Hovering a tile shows the banner and ring. "Your Turn" comes up with the last enemy banner still showing. Enemy tiles are initials |
| 15 | Quick regression | **PASS** (on 4c01d57): the numpad does nothing, a diagonal neighbour is hit in place, the path is an L with a rounded bend, stack numbers show, Escape+F4 rewrites one quick save, and Auto Save shows the party |
| 16 | Attacks of opportunity | **(a), (b), (c), (d), (e), (g) and the droid half of (f) PASS. The ranged-only half of (f) FAILS**: a Sith Trooper holding only a Blaster Rifle makes an opportunity attack when I step away. The owner's bug (an attack on merely walking up) is **not reproduced** on 4c01d57 |

## Findings, most important first

1. **A ranged-only enemy makes opportunity attacks (item 16 f).** Tester Save Bed's Sith Trooper (blueprint: `weapon_r_1 = blaster-rifle`, nothing else). After "Stand aside." starts the fight, stepping away from beside him logs "Opportunity attack: Sith Trooper attacks Gun Eighty : *miss* : (5 + 5 =…" (`i16f-gunman-provokes-FAIL.png`, `i16f-gunman-log.png`). ACTION-ECONOMY-01 §10 says a ranged-only enemy makes none.
2. **The combat log panel covers part of the board.** It is fixed at the bottom right (`play_screen.dart:20419`, width 150 × s) and hides tokens, paths and the hit-chance tooltip there. In one bed it hid a droid for a whole fight (`i14-your-turn-banner-log-hides-droid.png`, `i13-log-covers-tooltip.png`). It also keeps only six entries (`play_screen.dart:11482`).
3. **An unfound hidden placeable is drawn.** A crate with `hidden = true, stealth = 60` (my bed; no shipped package has a hidden placeable) is drawn from the first frame for a fresh character, while it correctly does not block (`i05c`). Lens's skip set seems to be built from creatures only (`play_screen.dart:764` walks `_here`).
4. **L approaches cannot be judged by eye**: moves are drawn as jumps, and the log gives only the square count (`i12a`). Either an animated step or the route in the log would make item 12 testable.
5. **A droid dithering between two targets** for 17 rounds ("closes 5 squares — 6 to 2 · out of movement 2 squares short", then "8 to 3" the other way), never reaching either (`i12c`).
6. **Wording oddities**: a kill line ends with a raw tag, "· character.died" (`i10d`). "Sentry Droid and Sentry Droid falls". The downed Kael's card reads "0 of 3" while the line reads "Kael: -7 of 3". The status line still uses the old long roll form while the log uses K2's.
7. **Continue lands on the arrival square**, not where I saved (Tester Mines: saved on (2,1), back on (1,1)).

## Combat log wording on 4c01d57 (verbatim, for the comparison)

- `Sentry Droid attacks Kael : *hit* : (10 + 1 = 11)` / `Sentry Droid damages Kael for 1 damage`
- `Sentry Droid attacks Gee Two : *miss* : (3 + 3 = 6)` (the centre banner shows the same line)
- `Sentry Droid attacks Rifle Eighty : *critical hit* : (20 + 3 = 23 : Threat …` (cut)
- `Opportunity attack: Sentry Droid attacks Boot Fight : *miss* : (10 + 1 …` (cut by the panel width)
- `Rifle Eighty attacks Sentry Droid : *hit* : (10 + 4 = 14)`, with `Flanking +2` on its own indented line beneath, not ` · Flanking +2` at the end of the line as the amendment describes
- `Kael attacks Sentry Droid : *hit* : (11 + 2 = 13)` / `Kael damages Sentry Droid for 2 damage`
- `Sentry Droid has already acted`; `OA Droid is a droid holding unarmed — melee is closed to every droid chassis, so it has no attack it can make`
- Status line, unchanged: `Sentry Droid catches Boot Fight leaving — unarmed · rolled 11 — d20 10 + attack 1 + Strength 0 · needed 20 — miss`; `disengaging — your movement provokes nothing this turn`; `you rest a day · vitality 8 → 11 of 11`

The 617578e wording (before K2's lines) is recorded in the running log.

## Item 16 detail (4c01d57, Boot Fight in tester-rough unless noted)

- (b) (5,2) → (6,2), still adjacent to the droid at (5,3): no provoke line, no attack.
- (c) (6,2) → (6,1), out of reach: "Provokes an attack from Sentry Droid" on the line, then one opportunity attack.
- (a) (6,1) → (8,1), stopping diagonal to the second droid at (9,2): no provoke line, no attack.
- (d) (8,1) → (11,1), past that droid in one move: provoke line, then exactly one opportunity attack.
- (e) Disengage, then step away: no provoke line, no attack.
- (f) The droid (local copy of the shipped Opportunity Attacks package, entering its droid room): no attack, with the "closed to every droid chassis" line. The gunman: **an attack (finding 1)**.
- (g) Kael's move-and-attack onto the square beside a droid in tester-lshape: no provoke line, a hit, no opportunity attack.
- Also seen: each creature has one reaction per encounter ("reaction · per encounter"), so a second step out of the same droid's reach later drew nothing.

## Notes

- Kael's "Change Doctrine > Aggressive" did not change his MANUAL label. Clicking the label cycles MANUAL → HANDS OFF → AUTO.
- Boots in a fight are folded into "armour 8" on the defence line rather than named.
- With nine enemies, the party sidebar cuts off the player's own card.
- I briefly set my local `tester-rough` Kael to 3 HP for the downed-ally case, then restored it to 40.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
