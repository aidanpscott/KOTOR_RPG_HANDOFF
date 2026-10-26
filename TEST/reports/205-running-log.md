# TEST 205 running log (draft, text only)

Started 2026-10-25. Ruled, don't file: a fall bleeds from the next round, not at the instant of the fall.

## Build
- Settings: no settings.json (defaults); brightness default. Shelf 88d0d8f unchanged; packages identical.
- saves/fight12-204.sav = the authored copy (md5 83763b0677993324175907284d941290), no marks.
- App main a599a96, worktree builds/test205. Lodestar c5cb345 (lock), Lens 5fe60a9.
- Gate: "FOR TESTER — CORE at a599a96, 5190 tests, 0 failed, 12m38s at -j 3, peak 1778 MB"; "ARCHIVE last green at a599a96".
- Build through the lock 10.1 s; pubspec.lock unchanged; Lodestar c5cb345 = lock = compiled.

## 2. Companions' first manual turns — PASS
After the walk-in: first Vela 'move 5 of 5 · reactions 1 of 1 · MANUAL', slots lit (vela-t1); the second Vela the same (vela2-t1).
## 1. Replay of fight12-204-authored.sav — PASS
Tap 1194,338, bump Right, End Turn (fall at the 16th of this count; frames shots/205/f, 255; seq in shots/205/seq.txt). Second pass from the authored copy to read Messages > Combat before the defeat (log-pages.txt). Frame vitality against each logged line:
- R1 'damages Fight Twelve for 4', 'for 3' -> 12 -> 5. R2 'for 7' -> 5 -> -2 (f0016) with 'Party Member Down / Fight Twelve' (f0016-17). The player stays -2 through that round and bleeds from the next (-3 at f0076, then -1 a round).
- Vela A: R2 'for 5', 'for 1' (40 -> 34; frame shows 35 then 30), R3 'for 4' -> 30, R4 'for 4' -> 26, R5 'for 12' -> 14 and 'for 7' -> 7, R6 'for 6' -> 1.
- R8 'Gunman attacks Vela : *critical hit* : (19 + 3 = 22 : Threat Roll: 20)' / 'Gunman damages Vela for 13 damage': Vela A 1 -> -12 (f0196), exactly 13, with 'Party Member Down / Vela' on its own row under the attack banner, both up together. She stays -12 (f0203, f0211) and bleeds to -13 only at the next round's end (f0226).
- Vela B: R8 'for 3', 'for 8', R9 'for 10' -> 40 -> 19 (f0211), matching; then 19 -> 7 (round 10, 12 more).
- Run 1 ended in total defeat at f0241 (Vela B fell to the killing blow; the defeat popup, no separate Party Member Down banner seen for that last fall).

## 3. Round-end tick (attempt 1)
Tick One (specs205/tick.json, Scout 1, CON 6: 6 vitality) stepped onto the strongroom's poison mine: 'goes off — d20 5 = 5 vs 15 · 6 damage · 0 of 6 · 2 more rounds' — felled by the mine's first blow (not a tick); solo, so the party fell at once. (tick-1)
Attempt 2: Tick Two (CON 12, 9 vitality): the mine left her 3 of 9 '· 2 more rounds'; out of a fight steps don't tick (stays 3). Walked to the Probe Droid: on reaching the fight the party fell at once (0 of 9, total defeat); a solo character's fall ends the party, so the defeat popup replaces any banner, and whether a tick or a blow felled her can't be told. 3 NOT REACHED cleanly (needs a party with a companion). (tick/)

## 5a. Dice — FINDING: same die stream, different round grouping from TEST 185
Dice One Quick Save (Oct 19 07:40:30), same walk. Messages > Combat on a599a96:
Round 1: Gunman attacks Dice One *hit* (14+3=17) / damages Dice One for 11 / Gunman attacks Vela *hit* (13+3=16) / damages Vela for 7 / Gunman attacks Vela *miss* (8+3=11)
Round 2: *hit* (13+3=16) damages Vela for 5 / *miss* (5+3=8) / *miss* (8+3=11)
Round 3: *miss* (1+3=4 Automatic Miss!) / *hit* (18+3=21) damages Vela for 3 / *hit* (15+3=18) damages Vela for 7
TEST 185 (and TEST 204 on 0233f17): Round 1 = Dice One hit 11, 'Gunman has already acted', Vela hit 7; Round 2 = miss (8+3), hit (13+3) 5, miss (5+3); Round 3 = miss (8+3), miss (1+3 AM), hit (18+3) 3.
Every roll and damage is the same in the same order; but now each of the three gunmen attacks in round 1 (no 'Gunman has already acted'), so every later round shifts by one attack. With the shift, three Spaces end in total defeat (Vela 40 -> 18 after two). (dice/combat-tab, combat-tab2, w7-w10)

## 4. Critical hits on the player / an enemy — NOT REACHED
The regression fight's whole combat log (12 pages, log-pages.txt) has no critical hit; the only crit seen this test is round 8's on Vela (1 -> -12, exactly the logged 13).
## 5b. Regression (Icon Nine) — PASS
reg204 loaded; Save > New Slot '42 : reg205' (21:03:56); Escape then F4: one quick.mark (21:04:01); Load lists Auto, Quick, '42 : reg205'; loaded; fight with run/fightbolt.py: WON ('FIGHT OVER 42'). (reg/load-list, reg/start, reg/end)
