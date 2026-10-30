# TEST 214 running log (draft, text only)

Started 2026-10-29. One run covering 36c1d38 and e7095dc. KNOWN, not filed: Stasis's description still says "instead of stunned"; the three 213 small items; Sneak Attack. Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate `--at e7095dc`: "FOR TESTER — CORE at e7095dc, 5318 tests, 0 failed, 13m20s at -j 3, peak 1816 MB"; ARCHIVE last green at e7095dc. The verdict line read "DO NOT SEND — 1 blocking failure": check_shelf_repo.py, "1 path(s) under base-rules/ differ from HEAD" in the shared Shelf working tree (KOTOR_APP_PROJECT/Shelf), not in the build.
- App main e7095dc (worktree builds/test214): built through the lock in 10.4 s; pubspec.lock unchanged (f1dc056c); git status clean; Lodestar 279b521 resolved (= lock).
- Settings: no settings.json (defaults). Packages synced to Shelf e612e14 (git checkout in my packages dir; old copies in notes/packages-before-test214); check_shelf: "33 rules files and 125 standard blueprints, all identical".
- Beds (specs214, local package tester-214): Stasis Yard. Para Guard (Force Immunity: Paralysis), Stun Guard (Force Immunity: Stun), Target, Seer (Precognition), all Soldier 3, Dex 16, Con 3, Wis 3, 300 vitality; Saver (same, Con 30); companion Blade Mate (Soldier 6, vibroblade, no Killer's Instinct). Players: Yard Jedi (Consular 16, Wis/Cha 10, Killer's Instinct, Stealth 20, lightsaber; Stun, Stasis, Stasis Field, Blindness, Push), Yard Flurry (the same, Wis 20 Cha 18, Freedon Nadd's Short Lightsaber, Flurry). Implant Room: Implant Low (Soldier 4, Con 6, Cybernetic Implantation, Strength Package and Mental Boost Package in the bag), Implant None (the same, no feat).

## 4. Implants — PASS, one finding
- Implant Low (Con 6, feat), Equip implant slot: Strength Package and Mental Boost Package both offered, neither red. Strength Package pane: "Feats Required: Cybernetic Implantation", "Strength: +1", K2's description; no Constitution line. Mental Boost: the same shape. OK equips it ("(Equipped)"); Character: Strength 11 (base 10), Constitution 6; Character Info has no refusal line; Defense 11 = Equip DEF 11. (imp-slot, imp-str, imp-mb-c, imp-eq, imp-char, imp-info-c)
- Implant None (Con 6, no feat): Strength Package refused with K2's line and "Strength Package has no effect: it needs the Cybernetic Implantation, Advanced Cybernetic Implantation or Master Cybernetic Implantation feat." No Constitution. (noimp-slot)
- Chargen (Bith Soldier), Attributes, Constitution: "Constitution represents health and resiliency. A high Constitution adds modifiers to the vitality points gained at each level and to Fortitude saving throws. This attribute is important for all classes." No implants. (cg13)
- Companion's file implant (Kit Leader, tester-kit): Weak Mate (Con 10, Crado's Robe + Bio-Antidote System in the file) Character Info shows only "Alignment Committed Dark (20)", no gate line. FINDING: her Stats read Constitution 10, not 11; the Bio-Antidote's +1 Constitution is not on the sheet, while the robe in the same file counts (Defense 13). Equip says "No equipment is recorded for Weak Mate: a companion is a blueprint in the roster and carries none", so I can't see whether the implant is worn. (weak-stats, weak-info-c, weak-equip)
- Note: Kit Leader's Character small portraits cycle Leader/Crado Mate and Crado/Arca Mate; Weak Mate reached by HUD portrait (known 213 small item, not filed).

## 1. One fold — PASS
- Equal Jedi (tester-align): Equip DEF 15 = Character Defense 15. Plain Mate: Equip DEF 15 = Character Defense 15 (was 11 vs 15). (al-def, al-names)
- Also Implant Low 11 = 11; Blade Mate Equip DEF 13 = sheet 13. (p3-char-mate, p3-eq-mate)

## 2. Companion casts outside a fight — PASS
Equal Jedi, Align Hall, no fight. HUD portrait → "you are now controlling Plain Mate"; f: "cast — 1 Heal 8f · 2 Force Affliction 12f · 3 Force Push 6f · esc", "force 105 of 105" (the player's pool is 155). 1 → "Heal — 1 Dark Mate · 2 Plain Mate · 3 Equal Jedi · esc"; 1 → "Plain Mate: Heal · 8f — 105 → 97 · ceiling −1 to 104 · at Dark Mate · Dark Mate — healed 5 +2 cha +2 wis +10 level 19 · 80 → 80". (i2-f, i2-castc)

## 3. Small portraits switch the page's member — PASS
- Out of a fight (Implant Low + Blade Mate): Character → Blade Mate (Defense 13); Equip shows Blade Mate, its portrait → Implant Low; Abilities → Blade Mate. (p3-*)
- In a fight on my turn (Yard Jedi + Blade Mate): Character Yard Jedi → Blade Mate; Equip Blade Mate → Yard Jedi; Abilities Yard Jedi → Blade Mate. (f3-all)

## 5. Stasis and Stasis Field paralyse — PASS
Yard Jedi (DC 21), then Yard Flurry (DC 30):
- Stasis on Target: "d20 20 = 19 vs 21 · slowed" (a natural 20 made the save). Stasis on Stun Guard: "d20 4 = 3 vs 21 · paralysed". (y-st1c, y-st3c)
- Stasis Field at Target (DC 21): Target "d20 2 = 1 vs 21 · paralysed", Para Guard "d20 4 = 3 vs 21 · resists", Stun Guard "d20 20 = 19 vs 21 · slowed", Seer "12 vs 21 · paralysed", Saver "d20 20 = 33 vs 21 · slowed". (y-sf1c)
- Stasis Field (DC 30): Target, Stun Guard, Seer, Saver "paralysed"; Para Guard "d20 3 = 2 vs 30 · resists". (y2-sfc)
- No "is stunned" anywhere for either power. Combat log: "Target is paralysed." / "Target has been affected by Force Stasis Field"; a made save "*resisted* : (20 - 1 = 19 vs. 21 automatic success)" then "Stun Guard is slowed."; turn lines "Target is paralysed". (combat2-4)

## 6. Unaware — PASS, one finding
Baseline (aware, Dex 16): "needed 13" from both of us. (y-a1c, y-b1ac)
- Paralysed: Blade Mate at Target "needed 9 (-3 Dexterity: unaware)" (Target also still slowed −1 from the round-2 save); Yard Flurry at Target (paralysed only) "needed 10 (-3 Dexterity: unaware)". (y-b3ac, cr1c)
- Stunned (Force Stun "d20 4 = 3 vs 21 · stunned"): at Para Guard "needed 9 (-3 Dexterity: unaware)" (also still slowed from an earlier Stun save). (y-stun3c, y-a9c)
- Hidden: s → "hidden — 22 beat 3"; next turn at Target (no condition) "needed 10 (-3 Dexterity: unaware)". (y-hidec, y-a15c)
- Blinded (Force Blindness: all five "blinded"): FINDING — Blade Mate at Saver "needed 8 — miss" (aware 13), I at Target "needed 8 — hit"; the line names no Dexterity. It drops 5, not 3, and says nothing. (y-bl1c, y-b10c, y-a11c)
- Prone (Freedon's knockdown "prone — … 10 vs 14 · takes hold"): Blade Mate at Target "needed 13", no term. (y2-a1c, y2-b1c)
- Slowed (Stasis save): Blade Mate at Target "needed 12", no term (slowed's own −1 Defence, conditions.dart). (y-b2ac)
- Precognition: paralysed Seer, Blade Mate "needed 13", no term. (y-b4ac)

## 7. Killer's Instinct — PASS
- Unaware hits add the rider: paralysed "+1d6 Killer's Instinct 6", stunned "… 3", blinded "… 1", hidden "… 2". (y-a4c, y-a9c, y-a11c, y-a15c)
- Critical (Yard Flurry, paralysed + prone Target): "rolled 35 — d20 19 … needed 10 (-3 Dexterity: unaware) — hit · threat confirmed: rolled 28 … · damage 35 — 4d6 2+3+6+6 + 1d8 energy 1+5 + Strength 3×2 × 2 critical +1d6 Killer's Instinct 6". The weapon dice doubled; the rider was rolled once. (cr2c)
- Without the feat: Blade Mate at paralysed Target "damage 6 — 1d10 3 + Strength 3", no rider; his critical on a prone Target "2d10 3+5 + Strength 3×2 × 2 critical", no rider. (y-b3ac, y2-b1c)

## Seen, not filed
- Rounds 12 and 13 of the first fight rolled the same damage dice ("2d8 8+1 … +1d6 Killer's Instinct 1") on different d20s (2 and 16). One sample. (y-a1213)
- Four natural 20s in about a dozen saves in the first fight. One sample.
- Stasis's description "instead of stunned": KNOWN.
- I couldn't find how to declare Flurry from the combat bar; not in the order.

## 8a. Dice — PASS: 17/17 lines = dice-baseline-206 (the only differences are two OCR marks in the baseline file). (dice/)
## 8b. Regression — PASS: '50 : reg213' loaded; New Slot '51 : reg214' (000051.mark 01:25:03); F4: one quick.mark 01:25:19; Load '51 : reg214'; fightbolt WON ("Gunman and Gunman and Gunman falls"; Icon Nine 106 of 196). (reg/)
## Processes: app, xsettingsd, Xvfb stopped by PID.
