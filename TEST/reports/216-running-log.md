# TEST 216 running log (text only)

Started 2026-11-01. One run on app main c124f76. KNOWN, not filed: the blasters doing 0 (ruled); Trask has no portrait; Loom has no controls for opens, shelf or attack. RULED, not filed: Strength 6 on damage against 4 on attack for a one-hander with an empty off hand (PT-2222). Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate `--at c124f76` (shared MAIN_WORK): "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at c124f76, 5395 tests, 0 failed, 14m09s at -j 3, peak 2058 MB"; ARCHIVE last green at c124f76.
- App main c124f76 (worktree builds/test216): built through the lock in 10.2 s; git status clean; Lodestar 69d8d69 (lock resolved-ref = package_config).
- Settings: none (defaults). Packages synced to Shelf 701a740 (old copies in notes/packages-before-test216); check_shelf: "33 rules files and 125 standard blueprints, all identical". My own unshelved packages were moved aside for item 4, then put back.
- Beds: author_tester_test215_saves.dart rerun twice (fresh Power One). Mine: specs216/robesoldier-216.json, Robe Soldier (Soldier 10, no Jedi Defense, bag Crado's, Matukai Apprentice, K1 Jedi Knight, Shelf Padawan Robe) in tester-215. Reused Robe Plain (tester-215), Dice One and Icon Nine (tester-bolt).

## 4. Library — PASS
- First tile "Endar Spire — The Opening", card "The Endar Spire is under attack. Wake in your quarters, find Trask, and fight through to the bridge." Then "Test beds", then every bed from A Gated Implant to Two Enemies, "Tester Visual" among them. No Base Rules tile. (t216-lib2, t216-libt10)
- With my own packages back, Tester 215 (no shelf line) sits second, before "Test beds": my package, not the Shelf's.

## Characters
- Open Soldier: Human Soldier, Taris/Noble/Acolyte, Str 16 Dex 14 Con 14, 12 vitality, Defense 12, took the Acolyte "Padawan Robe → Jedi Robe" pick at Equipment. Her bag held only the Blaster Rifle (equipped) and Body offered only Clothing: the robe never arrived. (t216-cg33, t216-inv1, t216-eq2)
- Frail Sage: Bith (−2 Con) Jedi Consular (d6), Con 8 (−1), 5 of 5 vitality, Defense 14; the same Acolyte pick, and she starts in the Padawan Robe (Equipped). Feats: Blaster, Dueling, Melee, Jedi Defense, Lightsaber. (t216-c2t, t216-c2feats2, t216-c2eq2)
- Both backstories read "The Noble part comes last, if_ at all."

## 5. Quarters — PASS
- Step into Trask: "We've been ambushed by a Sith battle fleet! …"; 1 "Who are you?" → "I'm Trask Ulgo, ensign …"; Continue → "Now hurry up, we have to find Bastila! …" with "1. Okay, let's go help Bastila!" and "2. Oath or no oath - I'm heading to the escape pods!". (t216-q3, t216-q5)
- Open Soldier took 2: "Don't be stupid! You won't stand a chance …" → "We should stick together; you'll have more success with a party than on your own." with "Trask Ulgo is with you now". Frail Sage took 1: straight to "We should stick together …". (t216-q6, t216-q7)
- Messages > Feedback: "Trask Ulgo has joined the party.", "Trask Ulgo reached level 2.", "Trask Ulgo reached level 3.". (t216-msg2)
- Footlocker: "Medpac" ×2; Get Items → "took 2 things", then "Container is Empty". (t216-fl1)

## 6. Rooms 3, 4 and the hall — PASS
- Room 3: closed east door with both Sith standing: "That cannot be done while there are enemies nearby." (t216-r3b)
- Counts and vitality: room 3 "Sith Soldier: 15 of 15 · Sith Soldier: 1 of 1"; room 4 two at "12 of 12"; hall three at "15 of 15". (t216-r3e, t216-r4d, t216-h7)
- Sith shots: "Sith Soldier: One Damage Blaster · rolled -3 — d20 9 + attack 1 − Dexterity 4 − weapon 5 − point blank 4 · needed 12"; the one hit: "Sith Soldier damages Open Soldier for 0 damage" (and "damage 0 — 1d1 1 − Dexterity 4 — not enough to hurt" on Frail Sage). (t216-r3g, t216-c2r4c)
- Each east door opened once its room was clear (walked through all three, both runs). Each room has a door on the west wall at the "in" arrival. I didn't walk back through one.
- Seen: no fight starts until I bump a Sith. Open Soldier walked from the west door past both room-3 Sith to the east door with no fight; "initiative" appeared only on the bump.

## 7. The hall's security panel — PASS
- Step into it outside a fight: "Trask Ulgo: We'll be fighting in close quarters on the bridge. You better equip a melee weapon before we go through that door." with "1. Okay."; then "the conversation is over". (t216-h3, t216-h4)
- Character: Experience 1000, Needed 0; Level Up lit. Feedback reads "Experience: —." with no number. (t216-h5, t216-h6)
- Level up at the panel: Open Soldier to Soldier 2 (12 of 20); Frail Sage to Jedi Consular 2 (5 of 8).
- During the hall fight: step into the panel → "the Security Panel is in the way". (t216-h8)

## Level-up skills — FINDING
- The level-up Skills page shows every rank at 0, though ranks were bought at creation. (t216-lv3, t216-c2lv3)
- Frail Sage before the level-up (Abilities > Skills): Alertness rank 4, Awareness rank 4, Archaeology 4. At the level-up I added 3 to Alertness and 1 to Awareness (its plus went dim at 1). After it: Alertness rank 3, Awareness rank 1, Archaeology (untouched) still 4. (t216-c2-skills-before, t216-c2-skills-after, t216-c2-archaeology)
- Open Soldier: raised Alertness/Athletics/Awareness at the level-up; after it each read rank 1 (Athletics 1 + 5 bonus = 6), while untouched Acrobatics kept 2. (t216-sk3)

## Trask in a fight — FINDING
- Trask (hover: "Trask Ulgo · Soldier · 3 · Vitality 22 of 22 · MANUAL") never appears in a fight's initiative or strip and never acts, in all four fights on both runs. Room 3's initiative: "Open Soldier 6 · Sith Soldier 4 · Sith Soldier 2". (t216-r3e, t216-r4d, t216-h7)
- On the bridge Open Soldier fell and the box said "YOUR ENTIRE PARTY HAS BEEN KILLED." with "YOU FALL, AND NOBODY IS LEFT STANDING. That is a total party defeat …", while Trask stood at 22 of 22 beside her. (t216-b-dead)
- Hint, unverified: the opening's trask.crtr has `[vitality] override = 0`.

## 8. The bridge — PARTLY
- Two Sith, "15 of 15" each, "Sith Soldier: One damage blade". Every blade hit did 1: "Sith Soldier damages Frail Sage for 1 damage" (four hits), and one unconfirmed threat (natural 20, "threat not confirmed") did 1.
- A confirmed critical never came in about 14 Sith swings, so the 2 is not seen. A chance mechanic: the quick save replays the same dice.
- Frail Sage won the bridge at 3 of 8. The log shows "Flanking +2" on the Sith and "Opportunity attack: Sith Soldier attacks Frail Sage". (t216-c2b-end)
- Open Soldier: I passed about 30 turns on the bridge to collect hits and she died at 0 of 20 (my choice, not the opening's). The run was never saved, and the defeat box blocks the log.

## 9. Survival
- No moment where either character could have died before acting. Frail Sage (5 vitality) took 0 from every blaster hit and 1 per blade hit. The only death was Open Soldier's, after I passed turns on purpose.

## 1. Robes — PASS
- Robe Soldier (Soldier 10, no Jedi Defense): Body lists Crado's, Matukai Apprentice, Jedi Knight (K1) and Padawan Robe, all red. OK on each: "You cannot equip this item. You don't have the prerequisites. Please see the item description." with "Jedi Defense" under it. (t216-rs3, t216-rs-ok306/344/382/420)
- Robe Plain's Feats: Blaster, Melee, Force Sensitive, Jedi Defense, Lightsaber. She wears the Jedi Knight Robe (Equipped); Crado's and Matukai aren't red; Jolee's, Qel-Droma and Star Forge are red (alignment). (t216-plain-feats, t216-plain-eq)

## 2. Power Attack critical — PASS
- Fresh Power One, bump the thug, then x + Up (Gunner) each round. Round 13: "threat confirmed: rolled 25 … damage 40 — 3d10 1+5+5 + 3d6 5+4+2 + Strength 6×3 × 3 critical · 191 left". (t216-pg-13)

## Small
- After a load, the Combat log names the fallen hall Sith by tag: "sith-soldier.hall.03 falls.", "sith-soldier.hall.05 falls.", "sith-soldier.hall.04 falls." (they read "Sith Soldier falls." in the fight itself).

## 10a. Dice — PASS: 17/17 Combat log lines = dice-baseline-206 (Dice One from its Oct 19 quick save). (t216-dice-4.txt)
## 10b. Regression — PASS: '52 : reg215' loaded; New Slot '53 : reg216' (000053.mark 07:37:58); Escape then F4: one quick.mark 07:38:04; Load '53 : reg216'; fightbolt WON ("Gunman and Gunman and Gunman falls"; Icon Nine 124 of 196). (t216-r4, t216-reg-end)
## Processes: app, xsettingsd, Xvfb stopped by PID.
