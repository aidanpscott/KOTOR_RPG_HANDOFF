# TEST 212 running log (draft, text only)

Started 2026-10-26. KNOWN, not filed: Nomi's Armband +1; Equip gate reason unseen; double-blade in left hand; companion equip from bag (PT-2524); enemies can't list powers. Dice baseline: notes/dice-baseline-206.txt.
(A MAIN -> CODER message, "TEST 212 HASH ACCEPTED … RULING 3 (a) … NEXT HASH (TEST 213)", landed here mid-test; not acted on.)

## Build
- Gate: "FOR TESTER — CORE at 33661f8, 5275 tests, 0 failed, 14m11s at -j 3, peak 2044 MB"; ARCHIVE last green at 33661f8.
- App main 33661f8 (worktree builds/test212): built through the lock in 10.1 s; git status clean; Lodestar 0fe5bff compiled (= lock).
- Settings: no settings.json (defaults); brightness default. Shelf b71849e: base-rules synced (old copy notes/packages-before-test212).
- Beds (notes/fixtures/specs212, authored copies in authored/): tester-align reused; player (Heal, Force Affliction, Force Push) with both mates knowing 2 (fewer-212), 3 (equal-212), 4 (more-212: + Force Stun) via subject-tagged power-taken. Local package tester-immune: Para Guard (feat force_immunity_paralysis) and Stun Guard (force_immunity_stun) via subject feat-taken in the save; a flash mine (tag flash-mine.imm.01) at (2,2) then a frag mine (frag-mine.imm.02) at (3,2), both "stunned 2 rounds, DC 99". Player Stasis Jedi (Consular 16, Force Stun, Force Stasis, feat Force Immunity: Stun).
## 1. Cast menu on a companion's turn — PASS (fewer, equal, more) + player's once
Each: load, Right x8 into the Sith Foe, End Turn to "<mate> is waiting on you", f.
- FEWER (mates 2, player 3; the 210 crash case): Dark Mate "cast — 1 Heal 12f · 2 Force Affliction 10f · esc" on its own top row, the vitality row beneath, "force 105 of 105"; cast 2: "Dark Mate: Force Affliction · 10f — 105 → 95". Plain Mate "1 Heal 8f · 2 Force Affliction 12f"; Heal on the player "105 → 97", 56 → 62. (c1-df, c1-dcast, c1-pf, c1-pheal)
- Player's own menu (fewer bed): "cast — 1 Heal 8f · 2 Force Affliction 12f · 3 Force Push 6f · esc", "force 155 of 155". (c1-next)
- EQUAL (3): Dark Mate "1 Heal 12f · 2 Force Affliction 10f · 3 Force Push 6f", force 105; Push: "6f — 105 → 99". (c3-f-dark, c3-push)
- MORE (4: + Force Stun, which the player lacks): Plain Mate "1 Heal 8f · 2 Force Affliction 12f · 3 Force Push 6f · 4 Force Stun 6f · esc" (wraps to two lines on its own row, nothing cut), force 105; Stun on the Sith Foe: "6f — 105 → 99 · … stunned". (c4-f, c4-stun)
No crash in any case.
Note: OUT of a fight, while controlling a mate (HUD portrait), f lists the player's powers and "force 155 of 155" (c3-f-outfight).
## 2. The selected member's pages — PASS (one small)
- In a fight, my turn, press Plain Mate's HUD portrait: the menu opens on her Equip ("Plain Mate · Jedi Consular 10", DEF 11, "No equipment is recorded for Plain Mate… a companion is a blueprint in the roster and carries none" — PT-2524). Character: her portrait, STR 10 DEX 12 CON 12 INT 10 WIS 14 CHA 14, Vitality 80/80, Force 97/105, Defense 15, marker mid-bar; Character Info "Alignment Neutral (50)"; Abilities footer "Plain Mate". Press Dark Mate's HUD portrait, Character: Force 95/105, marker low toward Dark, Info "Alignment Committed Dark (18)" (her 20 less her own Affliction's drift). (c2-equip-plain, c2-plain-char, c2-dark-x, c2-plain-ab, c2-dark-char, c2-dark-info)
- Out of a fight: press the portrait, Character Info "Neutral (50)" for Plain Mate; Abilities > Powers shows her three powers (Heal cost 8). (c3-info, c3-pw)
- q opens the player's own Equip ("Fewer Jedi") after a mate was selected. (c2-q)
- In a fight the small portraits inside the menus don't switch member; the HUD portraits do.
Small: Plain Mate's Equip shows DEF 11, her Character page Defense 15 (base 10 + Dex 1 + class 4).
## 4. Immunities by text — PASS
stasis-212 in tester-immune (player holds Force Immunity: Stun).
- Flash mine (2,2): "goes off — d20 13 = 13 vs 99 · you shake it off". Frag mine (3,2), same effect: "goes off — d20 1 = 1 vs 99 · stunned for 2 rounds" (and I was stunned into the fight: "you are stunned · nothing spent"). (m-flash, m-frag)
- Force Stasis on Para Guard (Force Immunity: Paralysis): "Force Stasis · 14f — 239 → 225 · at Para Guard · Para Guard — d20 8 = 11 vs 30 · resists"; Combat "attempts Force Stasis on Para Guard : *success* : (8 + 3 = 11 vs. 30)" with no affected line; he attacks in round 4. (m-para, m-c1)
- Force Stasis on Stun Guard (Force Immunity: Stun): "… 22 vs 30 · stunned"; "Stun Guard is stunned." / "Stun Guard has been affected by Force Stasis"; its round-5 turn "Stun Guard is stunned". (m-stun, m-c2)
Note: Stasis's held target is named "stunned" in the lines.
## 3. Loom — PASS
Loom e9528e2 (worktree builds/loom212; built through the lock, pubspec.lock unchanged d5325a99, git status clean). Opened a scratch copy of store-bed placed for a moment in my packages dir as zz212-scratch (the GTK dialog mangles typed /tmp paths), removed after; diff against store-bed: unchanged. New Creature (name "Align Probe"): alignment 101, -1, 20.5, abc, 150 each show "alignment must be a whole number from 0 to 100" under the boxes; 20 clears it. With no species the dialog says "needs a species" and Create is dim; picking Human removes the line and Create lights. Cancelled; nothing written. (lo12-v*, lo12-nospecies, lo12-human)
## 5a. Dice — PASS: 17/17 lines = dice-baseline-206 (line-1 OCR only). (dice/)
## 5b. Regression — PASS: '48 : reg211' loaded; New Slot '49 : reg212' (000049.mark 19:17:09); F4: one quick.mark 19:17:12; Load '49 : reg212'; fightbolt WON ('FIGHT OVER 43'; "Gunman and Gunman and Gunman falls"; Icon Nine 100 of 196). (reg/)
## Processes: app, xsettingsd, Xvfb, Loom stopped by PID.
