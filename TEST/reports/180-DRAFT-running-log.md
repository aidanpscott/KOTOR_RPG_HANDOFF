# TEST 180 running log (draft, text only)

Started 2026-10-14. Tester, Xvfb :2, own data dir (~/.local/share/tester-data), no K2, no BG3.

## Build
- App 617578e (git archive to ~/kotor-tester/builds/test180, on disk). Built through tool/one_at_a_time.sh: 11 s, no wait. pubspec.lock unchanged.
- Lodestar d8390023997fdb17e4e897bafe70f14254f494fd = lock = compiled. Lens fe10327793b1a28882b088d2fbf8148e83ead926 = lock = compiled. Loom: no entry in the app's lock.
- Shelf 1e3ffb4 (data dir, = origin HEAD). check_shelf: see below.
- tool/env.sh sourced. Bundle launched with plain & outside the lock (run/launch.sh).
- Read first: Coder's TEST 179 fix entry (PLAYTEST-RULINGS-01.md, MAIN_WORK 5c443b57). Coder flags as open: mine damage writes no vitality event (reload restores health); outside a fight there is no path line, so "Walks onto a mine" shows only in a fight.

## Items
- check_shelf: 31 rules files, 118 standard blueprints, identical.
- Local beds (my data dir only, not on Shelf): tester-mines (copy of Locked and Trapped + guard droid at (3,0) by the mines + a hidden crate at (5,4)); tester-lshape (start (0,2), droid (1,2) to bump, droid (5,0) offset, Kael henchman at (9,4)); tester-nine (nine sentry droids); tester-rough from TEST 179.
- Authored saves (one locked dart run, specs in notes/fixtures/specs180/): flank-ninety (tester-rough), lsh-ninety (tester-lshape), nine-ninety (tester-nine): Soldier 3, CON 30, Short Sword C1 + Blaster Rifle C2, 3 medpacs; boot-ninety (Store Bed, Soldier 3, Heavy Leather Armour worn, 5000 credits).

### Items 1, 2, 10 (tester-rough, Flank Ninety + Kael manual, two sentry droids)
- 1: from (6,2) at turn start, hover rough (5,1): "2 squares (3 movement) · 2 left" + "Provokes an attack from Sentry Droid" (i01-rough-label-and-legend.png). Plain (4,4): "4 squares · 1 left" (i01-plain-4-squares.png). PASS.
- 2: the legend follows the hover: "5 → 2" on the rough path, "5 → 1" on the 4-square path. After a click it reads plain "4 move" (i02-legend-after-click-and-L.png). At a turn start on (8,1), with no rough neighbour, plain "5 move" (i02-legend-turn-start-no-rough.png). BUT at a turn start next to rough ground ((5,2) and (6,2), with rough (5,1)/(6,1) above), with the pointer far off the board (1850,1000), it reads "5 → 3 move" (i02-legend-pointer-off-next-to-rough.png). Coder's entry says that is PT-1519's next-step-onto-rough preview, by design. Against the order's wording ("pointer off the board, no stale preview") it is not stale but it is a preview with no pointer: MAIN to rule. PASS for click and turn change; pointer-off shows the PT-1519 preview.
- 10 flanking:
  - Straight (me (6,3), Kael (4,3), droid (5,3)): hover "90% (needs 3+) / +3 attack · +2 Strength · +2 Flanking, against Defence 10" (i10a); my line "... + Strength 2 + Flanking 2 · needed 10 — hit" (i10b); Kael's line "Kael: unarmed · ... + Strength 1 + Flanking 2 · needed 10 — hit" (i10c). PASS. Wording: the reasons say "+2 Flanking", the lines "Flanking 2" (order said "Flanking +2").
  - Diagonal (Kael (6,3), me (8,1), droid (7,2)): Kael's line "+ Flanking 2" (i10e). PASS.
  - L (me (8,2), Kael (6,3), droid (7,2)): my line has no flanking term (i10f). PASS.
  - Ranged (Blaster Rifle from (6,3), opposite Kael): no flanking term (i10d). PASS.
  - Downed ally: not reached yet. Enemy pair flanking me: not yet.
- Findings so far:
  - The combat log panel sits on top of the board's right columns (x 1227+): it hides a droid standing at (7,2) (i14-your-turn-banner-log-hides-droid.png), most of the path to (8,4) and (8,1), and it covers the hit-chance tooltip (i13-log-covers-tooltip.png). Clicks still reach the square under it.
  - Status line after a kill ends with a raw event tag: "... · 0 left · a shot uses Dexterity, not Strength · character.died" (i10d).
- 14 (seen so far): hover banner "Sentry Droid · Level 1" with a vitality bar and "24 of 24"; red dashed melee-reach ring 3x3 including diagonals (i10a). The strip: portraits/initials in initiative order, the actor raised, hourglasses on those who have acted (i14-strip-start.png); a dead droid leaves the strip (i14-strip-dead-removed.png). "Your Turn" big centre text appears with the last enemy action banner "Sentry Droid: unarmed on Flank Ninety" still visible (i14-your-turn...).
- 13 (seen so far): the log groups by "Round N", each action line with its roll line beneath; it keeps every line (rounds 1-4 scroll).

### Items 3-6 (tester-mines: fresh chargen Mine Eighty, Mine Two, Mine Three)
- 3a: a click at (560,600), just left of the grid, does nothing (i03a). PASS.
- 3d: outside a fight, click (3,3) from (1,1): arrived at (3,3), 11 of 11, both noticed mine squares unsprung (went round) (i03b). PASS.
- 3b: in a fight (guard droid bumped at (3,0)), hover (1,2) and (1,1) from (3,1): the route goes down column 3, along row 4, up column 0 round the mines (red past movement) (i03c). PASS.
- 3c: hover the mine square (2,2): "2 squares · 3 left / Walks onto a mine / Provokes an attack from Probe Droid" (i03d). PASS.
- 4: walked onto the mine in a fight: "goes off — d20 20 = 20 vs 15 · 3 damage · 8 of 11 · 2 more rounds"; centre line "Mine Two: 8 of 11", party bar 8 of 11 (i04a). Quick save + load mid-fight: 8 of 11, "the fight resumes — round 1, Mine Two's turn" (i04b). Outside a fight (Mine Three): "goes off — d20 7 = 7 vs 15 · 6 damage · 5 of 11"; centre and bar 5 of 11 (i04c); F4, Load: 5 of 11; app RESTARTED, Continue: 5 of 11 (i04d). PASS (better than Coder expected: the reload keeps the health). Note: after the reload the line reads "you notice Mine — 15 against 12" for a mine already sprung (not drawn).
- 5: "the Damaged Power Panel is in the way", "the Footlocker is in the way", "the Security Console is in the way" (i05a, i05b); routes go round them (i03c). A found hidden crate (no stealth) blocks: "the Shipping Crate is in the way" (i05a). An UNFOUND hidden crate (stealth 60, fresh character, no "you notice" line) does not block: I stood on its square (i05c). PASS. FINDING: the unfound hidden crate is still DRAWN ("C" at (5,4)) from the moment the area loads, for every fresh character. Lens's skip list for concealed things is built from creatures only (play_screen.dart ~line 764 walks _here). My bed's crate is the only hidden placeable anywhere (no shipped package has one).
- 6: panel header "POWER COUPLING FAULT — OUTPUT 0%" -> after the repair "POWER COUPLING ONLINE — OUTPUT 100%" (i06a). PASS. Once online the panel lists no reply at all, so its dimmed line no longer appears; the console's dimmed lines fit in full: "— you have 1 spike", "— you have 0 spikes" (i06b). PASS.

### Item 7: organic and the Treaded Motivator (Boot Ninety, Store Bed)
- Selecting Treaded Motivator: "In Inventory 0 · Only a droid can fit a motivator." and no "replaces" line (i07). PASS for the wording. Note: the row itself looks like every other row (no red or dimmed can't-use tint as far as I can see).

### Item 11: boots Defence (Boot Ninety: Soldier 3, Heavy Leather Armour worn, 5000 credits)
- Names in the store exactly: "Sith Trooper Greaves", "Mandalorian Battle Greaves", "Krath War Boots", "Vanguard Assault Boots" (i11e). PASS.
- Prices: Sith Trooper 900, Mandalorian 6500, Krath 24000; with 5000 only the Sith pair could be bought ("You do not have enough credits to purchase this item.") (i11a, i11b). Authored a 100000-credit fixture and a fight fixture carrying all four; both dart runs are still queued behind Coder's flutter test (PID 249033, holding the lock since about 07:05).
- Sith Trooper Greaves over Heavy Leather Armour: Equip DEF 17 -> 18 (i11c); sheet Defence 18 (i11d). +1, stacks. PASS for this pair. The other three and the in-fight hit chance wait for the fixtures.

### Item 12: L-shaped approach (tester-lshape, rebuilt: me (0,4), droid (1,4), droid (5,0), Kael (0,0); fresh chargen Ell Eighty / Ell Two)
- Kael AUTO (click MANUAL cycles MANUAL -> HANDS OFF -> AUTO; "Change Doctrine > Aggressive" did not change MANUAL).
- Droid from (5,0): "Sentry Droid closes 5 squares — 5 to 2" and lands on (2,2) — a (3 across, 2 down) offset covered in exactly 5 steps, so no diagonal step was taken (four-way). It then struck Kael from (1,3)/(1,2) region; follow-up "closes 1 square — 2 to 1".
- WHETHER IT WAS AN L OR A STAIRCASE CANNOT BE SEEN: every move is drawn as a jump. A 10 fps recording (vid t180-L.mp4) shows the droid at (5,0) in one frame and at (2,2) in the next, Kael (0,0) -> (0,3) likewise (i12a). The log says only how many squares. NOT OBSERVABLE as built.
- Kael AUTO closed straight down column 0 (0,0)->(0,3) and stopped diagonal to the droid at (1,4), then killed both droids. A straight run, not an L (my bed did not force one for him).
- Earlier run (Kael MANUAL, droid from (5,0) with me at (0,2) and Kael at (9,4)): the droid alternated targets every round, "closes 5 squares — 6 to 2 / out of movement 2 squares short", "closes 5 squares — 8 to 3", for 17 rounds without reaching either of us (i12c). Dithering between two targets.
- **Item 12: four-way PASS by step count; the L itself NOT OBSERVABLE (moves are drawn as jumps); a dithering enemy noted.**

### Item 10 (rest)
- Enemy pair flanking me (tester-nine, me at (0,3), droids on (0,2) and (0,4)): "Sentry Droid: unarmed · rolled 20 — d20 17 + attack 1 + Strength 0 + Flanking 2 · needed 12 — hit · damage 1 — 1d3 1 · 38 left" and "... rolled 17 — d20 14 + attack 1 + Strength 0 + Flanking 2 · needed 12 — hit ..." (i10g). PASS.
- Downed ally (tester-rough with Kael's local blueprint at 3 HP, fresh chargen Down Eighty): control first: me (5,2), Kael (5,4), droid (5,3): Kael's hover "75% (needs 6+) / +1 attack · +1 Strength · +2 Flanking, against Defence 10" and line "Kael: unarmed · rolled 10 — d20 6 + attack 1 + Strength 1 + Flanking 2 · needed 10 — hit" (i10h). After the droid downed Kael (card "0 of 3", token "K", line "Kael: -7 of 3", "1 bleeding · round 6"), my hover on the same droid: "65% (needs 8+) / +1 attack · ..." — the arithmetic (1 + 1 vs 10 -> 8+) has no flanking term (i10i). PASS from the preview; my attack line was not captured (the droids ended the fight first: total party defeat). Kael's blueprint restored to 40 afterwards.
- **Item 10: PASS** (straight, diagonal, L, ranged, downed, enemy pair). Wording: the reasons say "+2 Flanking", the attack lines "Flanking 2".
- Seen: the downed Kael's card reads "0 of 3" while the status line reads "Kael: -7 of 3".

### Item 9: move-and-attack tooltip (tester-nine, hovering a droid two squares off)
- The tooltip sits to the right below the target; the ghost at (4,4) and the target's red ring at (5,5) are both fully visible (i14b). PASS. BUT the combat log panel can cover the tooltip when the target is right of centre (i13-log-covers-tooltip.png, i10i: "65% (need..." cut by the log).

### Item 14: enemy hover and strip
- Hover banner: "Sentry Droid · Level 1", red vitality bar, "24 of 24" / "21 of 24"; red dashed ring = the 3x3 around it, diagonals included (i10a, i10h). PASS.
- Gunman with no ring: not yet (sentry droids are all unarmed).
- Strip: strict initiative order (tester-nine: 20, 19, 18 raised, me 11, 11, 10, 7, 6, 4, 2), acting tile raised, hourglass on each who has acted (i14a); the dead and the downed leave the strip (i14-strip-dead-removed, i10i). PASS.
- Nine enemies + me = ten tiles; the strip fits above the board (i14a). PASS. Note: the party sidebar in that fight is cut at the bottom (Nine Ninety's card half shown) — nine enemy cards fill it.
- Hovering an enemy's strip tile raises the tile and shows its name under it, its banner, its ring, and the move-and-attack preview on the board (i14b). PASS.
- "Your Turn" appears in big text with the last enemy action banner still showing above it ("Sentry Droid: unarmed on Flank Ninety") (i14-your-turn...). PASS.

### Item 13: log and banners (record, word for word)
- Banner hold, 10 fps recording (vid t180-banner.mp4): lit 2.4, 2.5, 2.5, 2.5 s each. PASS (about 2.5 s).
- Banners appear for attacks only: "Sentry Droid: unarmed on Nine Ninety", "Sentry Droid: unarmed on Kael", "Sentry Droid: unarmed on Flank Ninety". An enemy turn that only moves ("closes 5 squares") or does nothing ("nothing it can walk gets it closer") showed no banner (17 s with none in the recording while droids took turns).
- Log: grouped by "Round N", each action line with its roll line indented beneath. The panel shows only the last 6 entries (play_screen.dart:11482 sublist(length-6)); earlier rounds are not reachable by scrolling. The panel always sits bottom right over the board (Positioned right 6, bottom 6, width 150 s) and hides tokens there.
- Names, not tags: every line I saw uses names (Sentry Droid, Probe Droid, Kael, the player). One raw tag: a kill with the rifle ended the status line with "· character.died" (i10d).
- Lines seen, verbatim (action line / beneath):
  - "Round 1"
  - "Sentry Droid out of movement 4 squares short" / "Sentry Droid has already acted"
  - "Sentry Droid: unarmed" / "rolled 18 — d20 17 + attack 1 + Strength 0 · needed 11 — hit · damage 2 — 1d3 2 · 38 left"
  - "Sentry Droid closes 2 squares — 3 to 1" / "Sentry Droid: unarmed · rolled 15 — d20 14 + attack 1 + Strength 0 · needed 12 — hit · damage 2 — 1d3 2 · 50 left"
  - "Sentry Droid closes 5 squares — 6 to 2" / "out of movement 2 squares short · Sentry Droid: unarmed · out of reach — unarmed reaches 1 square and Kael is 2 away"
  - "Sentry Droid nothing it can walk gets it closer" / "Sentry Droid: unarmed · out of reach — unarmed reaches 1 square and Nine Ninety is 2 away"
  - "Sentry Droid: unarmed" / "rolled 21 — d20 20 + attack 1 + Strength 0 · needed 12 — hit · threat confirmed: rolled 14 — d20 13 + attack 1 + Strength 0 · needed 12 · dama…" (cut with an ellipsis)
  - "Flank Ninety: Short Sword" / "rolled 16 — d20 9 + attack 3 + Strength 2 + Flanking 2 · needed 10 — hit · damage 8 — 1d6 5 + Strength 3 · 16 left"
  - "Flank Ninety: Blaster Rifle" / "rolled 12 — d20 11 + attack 3 + Dexterity 2 − point blank 4 · needed 10 · 1 square, increment 14 — hit · damage 14 — 1d12 12 + Dexterity 2 · 0 left · …"
  - "Kael: unarmed" / "rolled 21 — d20 17 + attack 1 + Strength 1 + Flanking 2 · needed 10 — hit · damage 2 — 1d3 1 + Strength 1 · 14 left"
  - "Kael closes 3 squares — 4 to 1"
  - "Probe Droid: unarmed" / "rolled 10 — d20 7 + attack 1 + Strength 0 + closed on a ranged weapon 2 · needed 11 · 1 square — miss"
  - Status lines: "initiative — Sentry Droid 18 · Nine Ninety 11"; "Sentry Droid and Sentry Droid falls — Kael: unarmed · ..." ("falls" with two subjects); "the fight resumes — round 1, Mine Two's turn"; "goes off — d20 20 = 20 vs 15 · 3 damage · 8 of 11 · 2 more rounds"; "YOU FALL, AND NOBODY IS LEFT STANDING. That is a total party defeat, and it is the only thing that kills. — Sentry Droid: unarmed · ..."; defeat box "Your entire party has been killed. / Anyone who goes down is revived when a battle ends. Nobody is left standing, so there is no end of battle. / the newest save is this one — it already records the defeat".
- Attacks of opportunity in the log: not yet seen.

### AMENDMENT (MAIN): app 4c01d57 pushed after TEST 180 was written. I am already on 617578e: finishing there. RE-CHECK ON 4c01d57 at the end: item 4 (mine, save, load; and mine, rest, save, load), item 10 ranged flanking (a) on the line within half range with an adjacent ally +2 both, (b) past half range none, (c) off the line none, item 13 K2 wording ("<A> attacks <B> : hit (roll + bonus = total)", "<A> damages <B> for N damage", "Opportunity attack: ", " · Flanking +2"), strip enemy tiles stay initials. NEW item 16 (attacks of opportunity, a-g) to run on 4c01d57.

### Item 11 (rest): Boot Rich (100000 credits) bought all four (900, 6500, 24000, 31000). Heavy Leather Armour alone: DEF 17.
- Equip DEF / sheet Defence: Sith Trooper Greaves 18 / 18; Mandalorian Battle Greaves 19 / 19 (Fortitude +5 -> +6); Krath War Boots 20 / 20; Vanguard Assault Boots 20 / 20 (DEX 14 -> 15, modifier stays +2; Fortitude +7) (i11f, i11g). Each adds on top of the armour. PASS.
- In a fight (Boot Fight, authored with all four in the bag, Krath worn): "defence base 10 + Dexterity 2 + armour 8 = 20"; every droid attack on me reads "needed 20" (on Kael "needed 11") (i11h). PASS. Note: the line folds the boots into "armour 8" rather than naming them.
- Long names fit their Equip square (three lines for "Mandalorian Battle Greaves").
- **Item 11: PASS.**

### Item 8: Equip
- "Silenced Motivator" fits its square in full (Bolt Eighty, authored, wearing it) (i08a). PASS.
- Abilities > Feats: the three Cybernetic Implantation feats draw three different K2 implant icons by tier (i08b). PASS.
- Switch Weapons on Kael's turn, inside Equip: a red-bordered box "switching weapons — it is Kael's turn; wait for your own" (i08c). PASS. On my own turn it swaps (Config 1 empty <-> Short Sword) and the second press says "switching weapons — your second interaction this turn, so it cost your Action" (i08d).
- **Item 8: PASS.**

### Item 14 (rest): the gunman
- Sith Trooper (Blaster Rifle, Tester Save Bed, fight from "Stand aside."): hover shows "Sith Trooper · Level 3", bar, "18 of 18", and NO reach ring (i14c). PASS. Note: the hit-chance tooltip there covers my own token beside him.
- **Item 14: PASS** (strip tiles as initials: re-check on 4c01d57).

### Item 13 (rest): attack of opportunity in the log (617578e)
- Stepping away from an adjacent droid: status line "Sentry Droid catches Aoo Eighty leaving — unarmed · rolled 23 — d20 20 + attack 1 + Strength 0 + closed on a ranged weapon 2 · needed 11 · 1 square — hit · threat confirmed: ..."; the log files it under a plain "Sentry Droid: unarmed" heading with the same roll beneath (i13b). The log keeps it, but without saying it was an opportunity attack. Re-check wording on 4c01d57.
