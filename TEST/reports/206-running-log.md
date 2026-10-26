# TEST 206 running log (draft, text only)

Started 2026-10-25. Known: a hit for 0 damage is being checked (log, don't file).

## Build
- Settings: no settings.json (defaults); brightness default.
- Shelf pulled to 159ce8c; packages synced: base-rules, companion-fixture, ion-vs-droid, precognition-ambush, rx-gone-target, rx-two-triggers, tester-visual, tester-xp-bed, tester-xp-bed-arena (old copies notes/packages-before-test206/), tester-crit and tester-tick added. All identical to the Shelf now.
- Gate: "FOR TESTER — CORE at 2eb32c1, 5206 tests, 0 failed, 12m47s at -j 3, peak 1753 MB"; "ARCHIVE last green at 2eb32c1".
- App main 2eb32c1 (worktree builds/test206): built through the lock 9.9 s; pubspec.lock unchanged; Lodestar c5cb345 = lock = compiled.
- Beds: tool/author_tester_test206_saves.dart wrote tick-one.sav (14 events) and crit-one.sav (14 events).
- Loom dc76470: cloned to ~/kotor-tester/Loom-repo, worktree builds/loom206. Its linux/ folder is gitignored, so a fresh checkout cannot build for Linux; generated it locally with 'flutter create --platforms=linux' (through the lock), which also bumped pubspec.lock (three plugin patch versions) and added test/widget_test.dart — both reverted; rebuilt on the committed lock (OK), Lodestar c5cb345 compiled.
- While waiting for the lock: another agent's 'dart run tool/_seedprobe.dart' was reading save lists (mine included), read-only by the look.
- Local bed packages/tester-story (copy in notes/fixtures/specs206/tester-story-package): a01 Hall (Sage: six replies shifting light/dark tiers 1-3; Zaalbar joins with room), a02 Full House (three allies role companion; Mission joins into a full party; Locker locks then joins), a03 Kennel (beast role companion_beast + three allies), a04 Workshop (three droids role companion_droid + two allies). Saves: story-206 (Jedi Consular, a01), full-206, kennel-206, shop-206 (Soldiers).

## Dice baseline re-recorded on 2eb32c1 (MAIN: Coder traced the shift to the ruled late-arrival fix)
Dice One Quick Save (Oct 19 07:40:30), same walk, two Spaces (three now end in defeat), Messages > Combat: Round 1 Dice One hit (14+3=17) 11, Vela hit (13+3=16) 7, Vela miss (8+3=11); Round 2 hit (13+3=16) 5, miss (5+3=8), miss (8+3=11); Round 3 miss (1+3=4 Automatic Miss!), hit (18+3=21) 3, hit (15+3=18) 7. Identical to a599a96's. New baseline saved: notes/dice-baseline-206.txt (md5 a01882b3…). TEST 185 retired as the baseline. (dice/combat-tab.png)

## 7a. Tick One — PASS
Bump the Dummy (Right), End Turn. Log: R2 'Poisoner attacks Mira : *hit* : (19 - 1 = 18)' / 'Poisoner damages Mira for 3 damage' (6 -> 3); at round 2's end the poison tick takes her 3 -> -4 (frame 051); 'Party Member Down / Mira' shows with 'Your Turn / Combat Round 3' (f051-f057). Then -4 -> -11 (f071: the next tick plus bleed, 'bleeding · round 3'). Note: the tick's damage has no line in Messages > Combat. KNOWN (not filed): R3 'Dummy attacks Tick One : *hit* : (19 - 4 = 15)' / 'Dummy damages Tick One for 0 damage'. Feedback shows 'Mira has joined the party.' from load. (tick/f051, log.txt, feedback.png)

## 7b. Crit One, first pass (only one Right, then End Turn x6 — not the bed's 'repeat')
Duelist never attacked by me, so the stream shifted: R3 'Duelist attacks Crit One : *critical hit* : (20 + 1 = 21: Threat Roll: 16 Automatic Hit!)' / 'damages Crit One for 3 damage' -> 12 -> 9 (f041), matching; R6 hit 2 -> 9 -> 7 (f086), matching. (crit/log1.txt)

## 7b. Crit One as designed (Right, then End Turn, each round) — PASS
Re-authored beds (author tool) and replayed. Log against frames: R2 'Duelist attacks Crit One : *critical hit* : (20 + 1 = 21: Threat Roll: 16 Automatic Hit!)' / 'damages Crit One for 3 damage' -> 12 -> 9 (f020). R4 'Crit One damages Duelist for 4' -> 400 -> 396 (f049); 'Duelist damages Crit One for 3' -> 9 -> 6 (f052). R5 'Crit One attacks Duelist : *critical hit* : (20 + 3 = 23 : Threat Roll: 8 Automatic Hit!)' / 'damages Duelist for 10 damage' -> 396 -> 386 (f065); Duelist 'for 1' -> 6 -> 5 (f068). R6 'for 1' -> 5 -> 4 (f084). Every change equals the logged damage. (crit2/log.txt)
Already acted: a second bump in the same turn -> 'you have already acted'. PASS. Small: the first bump's prompt ('unarmed · rolled 8 — d20 5 + attack 1 + Strength 2 · needed 10 · miss') loses its last line ('miss') to the box's bottom edge. (crit2/act1, act2)

## 1. Alignment shifts — PASS
Story Jedi (Neutral 50) and the Sage's replies (one shift each): light tier 1 +1 (51) 'You have moved closer to the light side of the Force.'; tier 2 +2 (53) 'closer'; tier 3 +4 (57) 'You have moved much closer to the light side of the Force.'; dark tier 1 -1 'You have moved closer to the Dark Side of the Force.'; dark tier 2 -2 'closer'; dark tier 3 -4 'much closer'; added tier 5: light +15 (65, Leaning Light) 'You have moved a great deal closer to the light side of the Force.'; dark -15 'a great deal closer to the Dark Side of the Force.' One Feedback line per shift, no number. The wording follows the points moved (<=2 closer, <=8 much, >8 a great deal; k2_feedback.dart:169), so tiers 1-2 say 'closer', 3-4 'much closer', 5 'a great deal closer'. Sheet marker: mid-bar at 50, well up toward Light at 65. (align/fb*, info*, sheet0, sheet65)
Meditation: Rest column -> 'Eight hours of meditation (n)' asks a side ('you have not chosen a side · l to walk the light · k to walk the dark'); l, then n: 'you meditate the night · ceiling 22 > 22'; Feedback 'You have moved closer to the light side of the Force.' (65 -> 66). Same kind of line. PASS. Dark power drift: not reached (no character with a dark power in a bed). Ordinary Rest (e) writes no alignment line ('you rest a day. Nothing needed mending.'). (align/col6-*, med*, fb-med)

## 2a. Join with room — PASS
Story Jedi talks to Zaalbar ('I will come with you.'): 'Zaalbar is with you now'; Feedback 'Zaalbar has joined the party.'; 'Z' token fielded with a HUD portrait; hover 'Zaalbar / Soldier · 1 / Vitality 8 of 8 / MANUAL' (his own record has a class). Party Selection: Zaalbar's row white (in the field), '2 Available Slots'.
## 5. Party Selection 'Level N' — PASS: 'Zaalbar / Level 1' under the name, no role word. (join/z-*)

## 2b. Join into a full party — PASS
a02 Full House (entry switched to a02; three allies fielded, 0 slots): Mission 'Let me join you, if there is room.'; she leaves the board; when the talk ends Party Selection opens (0 Available Slots, Mission listed not fielded); Cancel returns to play with the party unchanged. Feedback 'Mission has joined the party.' ('wait for you back at your base' is the Party Selection help box's own text, not a separate line.) Not dismissed: later Party Selection lists her and Add + OK fields her ('M'). (join/m-*)

## 2c. Join on a locked party — PASS
Locker: 'The doors are sealed, but I will come.' (effects party.locked then party.joined): the Locker leaves the board and Party Selection does NOT open after the talk. Party Selection: '0 Available Slots', Locker listed (Level 1), Add greyed with 'You are unable to change your party at this time.' In a fight: not reached (no enemy in the bed). (join/l-*)

## 4. Slot rule — Kennel PASS
a03: Beast (role companion_beast) + Ally 1-3 (companion), all fielded (white rows), header '0 Available Slots' (three people; the beast takes no slot). HUD shows the three allies' portraits beside the player. (slots/kennel, kennel-party)
Workshop PASS: a04 Droid 1-3 (role companion_droid) + Ally 1-2, all fielded, '1 Available Slots'. (Each switch of the package entry needed an app restart — the package is read once per launch.) (slots/shop, shop-party)

## 3. Miraluka Soldier — PASS (one note)
Chargen (Tester Story): Miraluka (racial skill Alertness), Soldier, through Play as 'Mira Sight'. No level-up has happened. Abilities > Powers: one power, 'Force Sight / Universal · Tier 1', pane 'Prerequisites: Character Level 3 …', cost 6; held at level 1, so no pick was spent. Sheet and Character Info: no '[Modded]' (OCR 0 on both). Force row empty (a Soldier has no Force pool). Note: the pane's 'Prerequisites: Character Level 3' reads oddly on a level-1 character who holds it by species. (mira/*)
Human control: Shop Keeper (Human Soldier) Abilities > Powers: empty list. PASS. (mira/human-powers)

## 6. Loom — PASS (one small)
Loom dc76470 (built from my clone; launched on :2 with my data dir), opened a scratch copy of store-bed (notes: ~/kotor-tester/loom-scratch-206). Conversation tab: the 'effect' row offers the wizard's whole list, 19 kinds (encounter.began, quest.flag-set, quest.concluded, character.alignment-shifted, party.joined, character.power-taken, store.opened, door.unlocked, container.opened, item.acquired, item.lost, item.quest-done, camera.shown, map.revealed, log.written, droid.reprogrammed, turret.disabled, forcefield.toggled, alarm.raised) — the same 19 as wizard.dart's askableEffectsList. Picking a kind relabels the two boxes with its fields and lists them ('— subject, from, role' for party.joined; '— tier, side'). party.joined with subject + from filled: pressing effect writes nothing (refused: three fields, two boxes). character.alignment-shifted '2' / 'light': accepted; Write -> dialogue/merchant-greeting.dlg: effect = [ { kind = "character.alignment-shifted", tier = 2, side = "light" } ] on 'Suit yourself.' (tier a number), no party.joined anywhere. Small: the join refusal is silent — no line says why (conversation_tab.dart:480 returns). Note: Write produced a new .dlg beside the package's .toml. (loom shots)

## 8. Regression (Icon Nine) — PASS
reg205 loaded; Save > New Slot '43 : reg206' (00:12:14); Escape then F4: one quick.mark (00:12:19); Load lists Auto, Quick, '43 : reg206'; loaded; fight with run/fightbolt.py: WON ('FIGHT OVER 33'). (reg/load-list, reg/start, reg/end)
