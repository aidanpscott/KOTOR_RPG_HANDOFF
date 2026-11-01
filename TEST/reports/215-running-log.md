# TEST 215 running log (text only)

Started 2026-10-31. One run on app main e798167. KNOWN, not filed: the Caution items show nothing in play; the stealth tier extras (re-hide, Marked Shot, the stun) are held. Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate `--at e798167` (shared MAIN_WORK): "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at e798167, 5378 tests, 0 failed, 13m42s at -j 3, peak 1782 MB"; ARCHIVE last green at e798167. (A first run from my own MAIN_WORK clone read "NO STAMP": the stamps live in the shared tree.)
- App main e798167 (worktree builds/test215): built through the lock in 10.4 s; git status clean; Lodestar c5abf53 resolved (= lock = package_config).
- Settings: no settings.json (defaults). Packages synced to Shelf c93a685 (git checkout in my packages dir; old copies in notes/packages-before-test215); check_shelf: "33 rules files and 125 standard blueprints, all identical".
- Beds: tool/author_tester_test215_saves.dart wrote power-one (537 B), sneak-one (527), shot-one (522); author_tester_test208_saves.dart rerun (proof-immune/drift/muster/locks/fewer/equal/more). Mine (specs215, local package tester-215 "Gear Room", 23 catalogue items): Pair Jedi (Lightsaber R, Short Lightsaber L; bag Double-Bladed Lightsaber, Quarterstaff, Blaster Rifle, Vibroblade, Short Lightsaber), Robe Jedi (Jedi Defense; every robe and pane item), Robe Dark (Jedi Defense, dark), Robe Plain (no Jedi Defense, dark), Robe Light (light; Qel-Droma, Star Forge, K1 Knight), Robe Shelf (no Jedi Defense; the Shelf's own Padawan, Jedi and Dark Padawan robes), Sneak Instinct and Shot Instinct (the 215 beds plus Killer's Instinct). Reused tester-kit (Kit Hall) and tester-214 (Yard Jedi re-authored fresh).

## 1. Weapons — PASS
- Pair Jedi: Lightsaber R + Short Lightsaber L. Double-Bladed Lightsaber into R: equips; L empty; bag Short Lightsaber x2. (pair-eq, pair-r, pair-dbl)
- Blaster Rifle into R (with the short saber back in L): equips; L empty. (pair-rifle)
- Vibroblade into R (short saber in L): equips; L keeps the Short Lightsaber. (pair-both3, pair-vibro, pair-inv2)

## 2. The menu footer — PASS
- Kit Hall (four): Equip, Character and Options each show three small portraits. Equip: Crado Mate, Arca Mate, Weak Mate. Character (from Weak Mate): Kit Leader, Arca Mate, Weak Mate. Options: Crado, Arca, Weak Mate. Every member opened. (kit-eq*, kit-ch*, kit-opt*)
- Stasis Yard (two): one larger portrait right of the main one; it opens Blade Mate. (y-eq-footer, y-eq-footer-blade)

## 3. A companion's gear — PASS
- Weak Mate: Strength 16 (+3), Constitution 9 (-1), Defense 13. (weak-char)
- Her Equip shows Crado's Robe (Equipped) and the implant in the implant slot; the Body list's pane reads "Feats Required: Jedi Defense / Defense Bonus: 2 / Strength: +6 / Constitution: -2". OK (on None) pops "You cannot equip or remove an item from this slot."; Switch Weapons is dim with the same line in red under it. (kit-eq-1736, weak-body, weak-ok, weak-sw)

## 4. Blinded and slowed — PASS
- Force Blindness (Combat log: Target and Para Guard blinded, Stun Guard resisted). Blade Mate at Target: "needed 8 (-3 Dexterity: unaware, -2 blinded — Force Blindness) — hit". Mine at Target: "needed 8 (-3 Dexterity: unaware, -2 blinded — Force Blindness) — hit · … +1d6 Killer's Instinct 6". Para Guard read the same. (y-bm-hit, y-mine, y-combat)
- Aware controls: Seer and Stun Guard (not blinded) "needed 13".
- Stasis at Saver: "d20 20 = 33 vs 21 · slowed". Mine at Saver: "needed 12 (-1 slowed — Force Stasis) — hit". (y-st5, y-mine4)

## 5. Item panes — PASS
- Crado's Robe: "Feats Required: Jedi Defense · Defense Bonus: 2 · Strength: +6 · Constitution: -2". Droid Remote Interface: "Feats Required: Droid Upgrade Class 2 · Skills: Awareness -3, Security +10".
- Saves on armour/robes: Star Forge Robes "Defense Bonus: 5 · Saves: All +2 · Wisdom: +5"; Atton's Ribbed Jacket "Defense Bonus: 0 · Saves: All +2". Both Jedi Master Robes (a_robe_17, g_a_mstrrobe01) carry no save in their own records and show none; I found no item named "Master Jedi Robe".
- Conditional: Dune Striders "Saves: Fortitude +1 vs. fire"; Undercity Waders "… vs. disease"; Treaded Motivator "Saves: Reflex +4 vs. knockdown and push".
- No Computer Use / Treat Injury: Czerka Utility Belt "Skills: Demolitions +2, Repair +2, Security +2" (record has Treat Injury 3); Tech Specialist Belt "Skills: Awareness +2, Demolitions +4, Repair +5, Security +4 · Dexterity: +2 · Strength: +1" (record has Computer Use 4, Treat Injury 3).
- PT-717: Unarmed Accuracy Gloves, Alacrity Implant ("Feats Required: Advanced Cybernetic Implantation · Saves: Reflex +1 · Dexterity: +2"), Targeting Visor all "Saves: Reflex +1". The three Armorply Platings are armour upgrades with no base type; I could not put them in a bag, so not seen in the app (the Shelf's own pane field reads "Saves: Reflex +1").
- Packages: Fortitude Package "Saves: Fortitude +2", Will Package "Saves: Will +2", Reflex Package "Saves: Reflex +2", each under "Feats Required: Cybernetic Implantation". (pane-*)

## 6. Robes — PASS on Defense; FINDING on the Jedi Defense gate
- Defense = the robe's Armor (Dex 10, base DEF 14 with no robe): Crado's Robe 14 → 16 (Robe Plain); Jolee's Robe pane "Defense Bonus: 3", 14 → 17; Handmaiden's Robe "Defense Bonus: 3", no Feats Required line, 17; Qel-Droma Robes pane "Defense Bonus: 5", 14 → 19 (Robe Light); K1 Jedi Knight Robe "Defense Bonus: 2", 16; Matukai Apprentice Robe stays 14 (Defense 0). (rj-jolee*, rj-hm*, light-qel, plain-*)
- Panes: Crado's, Jolee's, Qel-Droma, both Jedi Master Robes, K1 and K2 Jedi Knight Robes read "Feats Required: Jedi Defense"; Handmaiden's doesn't.
- FINDING: without Jedi Defense (Robe Plain: Feats tab shows only Force Sensitive and Weapon Proficiency: Lightsaber), Crado's Robe, the Matukai Apprentice Robe and the K1 Jedi Knight Robe all equip with no refusal and no red row. The Shelf's own Padawan Robe (Robe Shelf) equips too (DEF 15) under its own "Feats Required: Jedi Defense". The only Jedi Defense refusal seen is Star Forge Robes: "…it needs to be Light Side, and the Jedi Defense feat." (its gate also sits in its properties as "Use Limitation Feat (Jedi Defense)"). Red rows without the feat are Jolee's, Qel-Droma, Star Forge: alignment ("Qel-Droma … needs to be Light Side"). (plain-eq, plain-feats, plain-crado-ok, plain-matukai, plain-k1c, plain-sf2, shelf-pad-ok)

## 7. Power Attack — PASS, one small
- Undeclared: "Vibroblade · rolled 22 — d20 10 + attack 8 + Strength 4 · needed 10 — hit · damage 13 — 1d10 7 + Strength 6". No Power terms; the word "Strike" doesn't appear. (p-strike)
- x lights the first action column and the box reads "Power Attack". (p-x)
- Thug: "Power Attack · Vibroblade · rolled 27 — d20 18 + attack 8 + Strength 4 − Power Attack 3 · needed 10 — hit · damage 19 — 1d10 7 + 1d6 6 + Strength 6 · prone — d20 20 = 20 vs 22 · shaken off". Next: "… prone — d20 2 = 2 vs 22 · takes hold"; the thug moved 3 squares right. (p-pa1, p-pa2, p-pa2-board)
- The status line doesn't say "Reflex" or "knockdown"; the Combat log doesn't show the save.
- Treaded Droid: "prone — d20 15 + gear 4 = 19 vs 22 · takes hold". (p-droid)
- Gunner (13 Power Attacks): never a prone or knockback line. Confirmed critical: "threat confirmed: rolled 20 … · damage 38 — 3d10 3+6+4 + 1d6 5+1+1 + Strength 6×3 × 3 critical". (p-gun1, p-gun8)
- Reset: the next turn opens with the column unlit. (p-reset, p-turn3)
- SMALL: the tripled Power dice read "1d6 5+1+1" (three rolls under a 1d6 label) where the weapon's read "3d10".

## 8. Sneak Attack and Stealthy Shot — PASS
- Sneak One, plain sight, declared: "Sneak Attack · Vibroblade … damage 9 — 1d10 8 + Strength 1", no dice. Hidden ("hidden — 22 beat 17"): "… +2d6 Sneak Attack 4+3". (s-plain2, s-hid1)
- Shot One, plain: "Stealthy Shot · Blaster Pistol … damage 10 — 1d8 6 + Dexterity 4", no dice. Hidden: "… +2d6 Stealthy Shot 6+5". (sh-plain, sh-hid1)
- With Killer's Instinct: "+1d6 Killer's Instinct 3 +2d6 Sneak Attack 2+6"; criticals: "2d10 1+3 + Strength 1×2 × 2 critical +1d6 Killer's Instinct 6 +2d6 Sneak Attack 5+1" and "2d8 7+6 + Dexterity 4×2 × 2 critical +1d6 Killer's Instinct 6 +2d6 Stealthy Shot 2+5". (ski-2, ski-6, shki-2, shki-12)

## 9a. Dice — PASS: 17/17 Combat log lines = dice-baseline-206. (dice-combat)
## 9b. Regression — PASS: '51 : reg214' loaded; New Slot '52 : reg215' (000052.mark 20:50:13); Escape then F4: one quick.mark 20:50:19; Load '52 : reg215'; fightbolt WON ("Gunman and Gunman and Gunman falls"; Icon Nine 119 of 196). (reg-save, reg-end)

## Seen, not filed
- Stasis spent 18f ("81 → 63 · ceiling −4") where the cast menu had listed it at 14f before the fight; Blindness had just moved Yard Jedi toward the dark side ("You have moved closer to the Dark Side of the Force."). Probably the alignment cost; one sample.
- Power One's damage adds "Strength 6" while her attack adds "Strength 4" (Str 18, a one-handed Vibroblade, nothing in the off hand).
- My Sneak Instinct and Shot Instinct saves carry no seed, so both replayed the same d20s and hide rolls. My bed, not the app.
## Processes: app, xsettingsd, Xvfb stopped by PID.
