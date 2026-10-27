# TEST 213 running log (draft, text only)

Started 2026-10-26. KNOWN, not filed: the four 212 smalls. Dice baseline: notes/dice-baseline-206.txt.

## Build
- Gate: "FOR TESTER — CORE at 662feaf, 5288 tests, 0 failed, 14m17s at -j 3, peak 1954 MB"; ARCHIVE last green at 662feaf.
- App main 662feaf (worktree builds/test213): built through the lock in 11.2 s; git status clean; Lodestar 191ac94 compiled (= lock).
- Settings: no settings.json (defaults); brightness default. Shelf ba538b6: tester-208 synced (old copy notes/packages-before-test213).
- author_tester_test208_saves.dart rerun (old proof saves/marks moved to specs213/oldproof): proof-immune/drift/muster/locks + proof-fewer (667 B), proof-equal (695), proof-more (706).
- Beds (specs213; authored copies in authored/): local package tester-kit — Crado Mate (Crado's Robe), Arca Mate (Arca Jeth's Robe), Weak Mate (Con 10, Crado's Robe + Bio-Antidote System implant), all alignment 20 companions; Sith Arca, an enemy at 20 in Arca's Robe. tester-gear extended with Star Forge Robes, Bio-Antidote System, Nikto Soldier Gloves, Short Lightsaber (and the blaster rifle). Characters Gear Neutral (gear-n-213), Gear Light (gear-l-213), Kit Leader (kit-213).
## 1. A companion's file kit — PASS (implant part recorded, not filed per the amendment)
kit-213 in tester-kit; the three mates join on load (C, A, W). Character Info (the HUD portrait selects the member):
- Crado Mate (20, Crado's Robe): "Alignment Committed Dark (20)", no refusal line; Defense 13 (the robe's Armor 2 counted). (k-crado-info)
- Arca Mate (20, Arca Jeth's Robe): "Arca Jeth's Robe has no effect: it needs to be Light Side." in red under the Alignment line. (k-arca-info)
- Weak Mate (Con 10, Bio-Antidote System implant): "Bio Antidote System has no effect: it needs Constitution 16." — RECORDED ONLY (owner's amendment: implants need no Constitution; not filed). (k-weak-info)
- Sith Arca (enemy, 20, Arca's Robe): Kit Leader's swing "rolled 24 — d20 15 + attack 7 + Strength 2 · needed 13" — the same 13 as the robed mates of the same class/level/abilities, so the robe is worn: not gated.
Note: the refusal sits on Character Info, under the Alignment row (not on the Stats tab). Arca Mate couldn't be selected by the HUD portraits (they cycle Weak/Crado/Leader only), so her Info was reached once in a cycle and her Stats Defense wasn't read.
## 3 (ability). SUPERSEDED: every item with UseLimitationAttribute in base-rules is an implant (42: implant-1/2/3 and two category-implant packages); no non-implant ability gate exists.
## 3. The Equip gate's reason under K2's line — PASS (ability SUPERSEDED)
Gear Neutral (50), item view, the refused row's popup: K2's "You cannot equip this item. You don't have the prerequisites. Please see the item description." then our line:
- alignment: "Arca Jeth's Robe has no effect: it needs to be Light Side." (g-arca)
- feat (+ alignment): "Star Forge Robes has no effect: it needs to be Light Side, and the Jedi Defense feat." (g-sf-n)
- class: "Nikto Soldier Gloves has no effect: it needs the Soldier class." (g-nikto)
- ability: SUPERSEDED (amendment; no non-implant ability gate exists). Recorded: the player's Bio-Antidote System reads "… it needs the Master Cybernetic Implantation feat." (Con 14; no Constitution named). (g-bio)
## 4. The right hand only — PASS (one small)
- Gear Neutral WEAPON L: Bastila's Lightsaber and Blaster Rifle outlined red; Lightsaber and Short Lightsaber allowed. Bastila's: K2's line + "Bastila's Lightsaber is already a pair — it cannot be held with a second weapon". Rifle (no proficiency): "Weapon Proficiency: Blaster Rifle". Short Lightsaber: OK → "(Equipped)" in WEAPON L. (g-wl, g-wl-bast, g-wl-rifle)
- WEAPON R: Bastila's Lightsaber offered (not red). (g-wr)
- Rifle Soldier (rifle-213, Soldier 10 with blaster rifle proficiency) WEAPON L: rifle → "Blaster Rifle takes both hands — it cannot be held with a second weapon" (r-wl-rifle); WEAPON R: rifle equipped (2-13, +11). (r-wr)
Small: with the Short Lightsaber already in L, OK on Bastila's in R pops "Bastila's Lightsaber is already a pair — it cannot be held with a second weapon" and nothing is equipped; K2 would empty the left hand. (g-after-bast)
## 2. Nomi's Armband in a fight — PASS
A first light run with Rifle Soldier is VOID: its Equip clicks never opened the menu, so the armband was not worn (r-arm shows the board). Redone with each equip verified on screen, one foe per yard (the box shows only the last actor), Rifle Soldier copies (Soldier 10, blaster rifle in WEAPON R, Nomi's Armband on the left arm; Equip DEF 13 both: armband-dark-equip, armband-light-equip):
- Dark Foe alone (tester-gear-dark, rifled-213): "Dark Foe: Blaster Rifle · rolled 10 — d20 11 + attack 3 + Dexterity 0 — point blank 4 · needed 14 (+1 vs dark side) · 1 square, increment 14 — miss"; three turns, all "needed 14 (+1 vs dark side)". (armband-dark)
- Light Foe alone (tester-gear-light, riflel-213): the same die rolls, "… needed 13 · 1 square …" — no +1. (armband-light)
## 5. Casters' Hall — PASS
proof-fewer/equal/more (Tester 208, Casters' Hall: player + Caster companion + Thug). Right x2 bumps the Thug; End Turn to "Caster is waiting on you"; f:
- fewer: "cast — 1 Force Aura 6f · esc", "force 87 of 87"; cast: "Caster: Force Aura · 6f — 87 → 81 … +2 defense · +2 saves". (h-few, h-few-cast)
- equal: "1 Force Aura 6f · 2 Burst of Speed 6f · 3 Energy Resistance 6f · esc", force 87. (h-EQUAL)
- more: "… 4 Force Valor 8f · 5 Force Push 6f · esc" (two lines, own row), force 87; 5 on the Thug: "Caster: Force Push · 6f — 87 → 81 · … stunned · Thug — 3d6 5". (h-MORE, h-more-cast)
No crash.
## 6a. Dice — PASS: 17/17 lines = dice-baseline-206 (line-1 OCR only). (dice/)
## 6b. Regression — PASS: '49 : reg212' loaded; New Slot '50 : reg213' (000050.mark 21:08:34); F4: one quick.mark 21:08:37; Load '50 : reg213'; fightbolt WON ('FIGHT OVER 38'; "Gunman and Gunman and Gunman falls"; Icon Nine 138 of 196). (reg/)
## Processes: app, xsettingsd, Xvfb stopped by PID.
