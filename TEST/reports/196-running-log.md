# TEST 196 running log (draft, text only)

Started 2026-10-24. Tester, Xvfb :2, own data dir. Batch 2 + TEST 195 fixes + store ruling.
Known, don't file: old frames on HUD/Party/Options/Save-Load (batch 3); store gold reasoned; no K2 capture for lit rows or combat bar; list boxes 4-7 px short at right.

## Build
- App bb8bf48, git archive from my own clone to builds/test196. Built through the lock: 9.8 s. pubspec.lock unchanged.
- Gate: "gate.py --at bb8bf48" -> "FOR TESTER — CORE at bb8bf48, 5017 tests, 0 failed, 13m47s at -j 3, peak 1874 MB"; "ARCHIVE last green at bb8bf48".
- Lodestar 240bc46 = lock = compiled. Lens 5fe60a9. Loom: no entry.
- Shelf 9706207 (= origin). check_shelf: 33 rules files, 125 blueprints, identical.
- Fixtures (specs196/, Store Bed): Lang Two (Twi'lek Soldier 1, medium armour worn, XP for 2), Jedi Arm (Guardian 1 holding Form I and Form V), RX-196 (Battle droid Machinist 6).

## Items

1. Character with a level waiting (Lang Two, Twi'lek Soldier 1 with 1000 XP): Auto Level Up (dim) and Level Up (lit) shown, inside the figure box over the portrait. Without a level waiting (Frame One): both hidden (ruled as K2). PASS. Note: with the level reached, "Experience 1000 / Needed 0".
3. Character Info: Experience and Needed numbers now shown (Frame One 0/1000; Lang Two 1000/0). PASS.
   Languages: Frame One (Human): "Languages / Speak and read/write Basic. A Human may select one additional language ..." PASS. FINDING: Lang Two (Twi'lek, species id "twi'lek" as chargen writes it, e.g. Twi Scout's save): NO Languages section, and Species shows the raw id "twi'lek" (lower case) where Frame One shows "Human". Probably the species lookup misses "twi'lek" vs species.toml's "twi-lek". To confirm with a chargen-made Twi'lek (Twi Scout is in Tester Bolt).
   FINDING: gear notes and Defense's reason: Lang Two wears Medium armour (Equip: "Medium (Equipped) / Defense Bonus: 4"; sheet Defense 16) and Character Info shows neither a gear note nor a Defense reason line.
4. Store (Dressa): seven tabs in order All, Datapads, Weapons, Armor, Useable, Quests, Misc. All = everything; Datapads empty (shows); Weapons = Vibroblade; Armor empty (shows; stock holds no armour suits, boots are Misc); Useable = Medpac; Quests empty (shows); Misc = boots, motivators, greaves. PASS.
   Prices: Medpac buy 40, sell 22; Adrenal Strength (cost 50) sells 27; Frag Grenade (cost 100) sells 55: 55% rounded down. In Stock "Infinite" buying, "—" selling. PASS. Note: the Vibroblade's In Inventory line reads "0 + replaces Blaster Rifle".
2. Purchase Gear (Jedi Guardian, Tester Bolt): tabs All, Datapads, Weapons, Armor, Useable, Quests, Misc. Weapons 25; Useable 12 (Repair Kit, Medpac, Antidote Kit, Adrenal Strength/Alacrity/Stamina, Advanced Medpac, Security Tunneler, Frag Grenade, Minor Frag Mine, Parts, Computer Spike); Misc 5 (Clothing?, Dockworker's Treads, Sparring Gloves, ... Field Generator, Sensor Probe); Armor 2 (Padawan Robe, Dark Padawan Robe); Datapads and Quests shown, empty. PASS.
2b. Purchase Gear for a Human SOLDIER (Tester Bolt, base rules): Armor tab = Padawan Robe, Dark Padawan Robe only. FINDING: no Soldier armour (its Standard Gear is Clothing); MAIN asked that a non-Jedi package's Armor tab list its starting armour. (Store Bed and Tester Bolt share base-rules' catalogue.)
5a. Abilities: Jedi Arm (Guardian 1, Form I + Form V held, no lightsaber): tabs Skills, Powers, Feats, Forms (Forms after Feats). Forms list = two icon cells; pane "Determination / Lightsaber Form / Attack +1; Defense +3; ..." and "Perseverance / Lightsaber Form / Attack +2; ...". No "Current stance" line (no lightsaber equipped): right per the order. Watch Four (no forms held): no Forms tab. PASS. NOT REACHED: "Current stance: Form I" with a lightsaber equipped (fixture has no saber).
   Note: the Load list only scans saves at launch: a save authored while the app runs isn't listed until restart (fixture quirk, not filed).

## Journal (Jedi Arm) — PASS
Matches K2 60-journal: "Active Quests By / Time / Name / Planet" (no Priority), Messages Log, Close with Notes right of it. (journal.png)

## Messages — PASS
Tabs Filter, Dialog, Feedback, Combat, Effects as K2 52. Effects: Good Effects and Bad Effects side by side as K2 54. Close returns to the Journal. (messages.png, effects.png, messages-close.png)

## Map — PASS (small notes)
Areas-entered strip at BTN_RETURN's place reads "map — ⟨Market⟩" in K2's face (EquipText, k2Teal; map_screen.dart:218). Small: starts with a lower-case developer-ish "map —"; the note strip above the board is empty and has no up/down arrows (K2 80-map has arrows and "Map Note: Morgue"); possibly no notes in a01-market. (map.png)

## Droid Attacks tab — PASS
Chargen Battle droid, Machinist: hub tabs Basic Info, Character, Skills, Feats, Attacks (no Forms/Powers). Attacks tab lists Shoot alone; no Strike/Jab/Punch/Kick. (droid-cg-attacks-tab.png). Soldier refused for a droid on the class page: "A droid cannot take this class."
Also: RX-196 level-up 6→7 hub has no tabs (tabs are chargen-only); granted popup lists Droid Upgrade 1, Plating Light, Upgrade 2, Plating Medium, Jury Rig, Percussive Maintenance. Left without Accept. Small: hub portrait box is black for RX-196 though the sheet has its portrait.

## Portrait edge at 1920 — FINDING
RX-196 (real portrait) on the sheet: alignment bar ends x 301, portrait starts x 384 at y 500: an 83 px gap. Level Up/Auto Level Up drawn over the portrait (Level Up at ~570,620). (droid-sheet.png)
At 1280x720 (xdotool windowsize): same gap; see measurement in report. (droid-sheet-1280.png). Window restored to 1920x1080.
1280 gap at y470: bar ends x206, portrait starts x256 = 50 px.

## Regression (Icon Nine) — PASS
Loaded 29 reg195 (start), Escape > Save > New Slot 'reg196' (000030.mark); Escape then F4: one quick.mark; Load lists Auto Save, Quick Save, '30 : reg196'; loaded reg196 back at the start. A fight to its end (bump the gunman each turn): 'Your entire party has been killed.' box with Go to Load Game List / Main Menu. (reg/end.png)

## Dice — PASS
Dice One Quick Save (Oct 19 07:40:30), dicerun.sh A: merged log md5 6b13820a706d9c9d6a266b848440eef7 = TEST 185 run A.
