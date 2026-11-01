# TEST 215: weapons, the menu footer, a companion's gear, blinded and slowed, item panes, robes, Power Attack, Sneak Attack and Stealthy Shot

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-215/` (MAIN_WORK `19c3d94b`). The step-by-step log is `TEST/reports/215-running-log.md`.

## Build

- **App**: main `e798167`, a git worktree beside my own clone. `gate.py --at e798167`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at e798167, 5378 tests, 0 failed"; ARCHIVE last green at e798167. Lodestar `c5abf53` = lock = compiled. The build (10.4 s) went through the lock, and git status was clean.
- **Settings**: defaults.
- **Shelf** `c93a685`, synced; check_shelf clean (33 rules files, 125 blueprints).
- **Beds**: `author_tester_test215_saves.dart` (Power One, Sneak One, Shot One) and the 208 tool, both rerun. My own, package **tester-215** "Gear Room":
  - Pair Jedi (Lightsaber in R, Short Lightsaber in L);
  - Robe Jedi, Robe Dark, Robe Plain (no Jedi Defense), Robe Light, and Robe Shelf (no Jedi Defense, carrying the Shelf's own robes);
  - Sneak Instinct and Shot Instinct (the 215 beds plus Killer's Instinct).
- **Reused**: Kit Hall (tester-kit) and Stasis Yard (tester-214).

## Summary: all pass except item 6's Jedi Defense gate (one finding); one small item

| # | Check | Result |
|---|---|---|
| 1 | Weapons | **PASS**. With the Short Lightsaber in L: the Double-Bladed Lightsaber into R equips, L empties, and the bag holds two Short Lightsabers. The Blaster Rifle does the same. The Vibroblade into R keeps the Short Lightsaber in L |
| 2 | Menu footer | **PASS**. In Kit Hall, Equip, Character and Options each show three small portraits, and every member opens. With two in the party (Stasis Yard), one larger portrait sits beside the main one and opens Blade Mate |
| 3 | A companion's gear | **PASS**. Weak Mate reads Strength 16 and Constitution 9 (Defense 13). Her Equip shows Crado's Robe (Equipped) and the implant. OK pops K2's "You cannot equip or remove an item from this slot."; Switch Weapons is dim, with that line in red under it |
| 4 | Blinded and slowed | **PASS**. Blade Mate's line and mine both read "needed 8 (-3 Dexterity: unaware, -2 blinded — Force Blindness)", against 13 when aware. On the slowed Saver: "needed 12 (-1 slowed — Force Stasis)" |
| 5 | Item panes | **PASS**. Crado's Robe reads "Strength: +6 · Constitution: -2"; the Droid Remote Interface reads "Skills: Awareness -3, Security +10". Star Forge Robes and Atton's Ribbed Jacket read "Saves: All +2". Dune Striders read "Saves: Fortitude +1 vs. fire". No pane lists Computer Use or Treat Injury (Czerka and Tech Specialist belts). The gloves, the Alacrity Implant and the Targeting Visor read "Saves: Reflex +1"; the Fortitude, Will and Reflex Packages read +2. Three notes are below the table |
| 6 | Robes | **Defense PASS, gate FAILS (finding 1)**. Defense equals the robe's Armor: Crado's +2, Jolee's +3, Qel-Droma +5, Handmaiden's +3. The Matukai Apprentice Robe adds 0. Every pane shows its row's "Feats Required: Jedi Defense", and Handmaiden's shows none. Without the feat, Equip refuses only Star Forge |
| 7 | Power Attack | **PASS, one small item**. Thug: "− Power Attack 3", "+ 1d6 6", "prone — d20 20 = 20 vs 22 · shaken off"; on a failed save, "d20 2 = 2 vs 22 · takes hold", and the thug moved 3 squares. Treaded Droid: "d20 15 + gear 4 = 19 vs 22". Gunner: no prone or knockback in 13 swings; a confirmed critical read "3d10 3+6+4 + 1d6 5+1+1 + Strength 6×3 × 3 critical". The declaration resets each turn. Undeclared swings carry no Power terms |
| 8 | Sneak Attack, Stealthy Shot | **PASS**. In plain sight, no dice. Hidden: "+2d6 Sneak Attack 4+3" and "+2d6 Stealthy Shot 6+5". With Killer's Instinct: "+1d6 Killer's Instinct 3 +2d6 Sneak Attack 2+6". On criticals the riders aren't multiplied: "2d10 1+3 + Strength 1×2 × 2 critical +1d6 Killer's Instinct 6 +2d6 Sneak Attack 5+1", and the same for Stealthy Shot |
| 9 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 52 ("reg215"), Escape then F4 (one quick save), Load, and a fight won |

Item 5 notes:
- I found no item named "Master Jedi Robe". Both Jedi Master Robes carry no save in their records, and they show none.
- The three Armorply Platings are armour upgrades with no base type, so I couldn't put them in a bag. They're unchecked.
- Item 7: undeclared swings read "Vibroblade · rolled … — hit · damage 13 — 1d10 7 + Strength 6". The line has no Power terms, and the word "Strike" doesn't appear. If "Strike" should show, say so and it becomes a small item.

## Findings

1. **The Jedi Defense gate isn't enforced at Equip for robes whose gate is only on the item.** Robe Plain has no Jedi Defense; her Feats tab shows only Force Sensitive and Weapon Proficiency: Lightsaber. She equips these with no refusal and no red row:
   - Crado's Robe (DEF 14 → 16);
   - the Matukai Apprentice Robe;
   - the K1 Jedi Knight Robe (`g_a_kghtrobe01`; DEF 16).

   Each pane reads "Feats Required: Jedi Defense". The Shelf's own Padawan Robe (`a_robe_02`) equips the same way, so this isn't my bed. Star Forge Robes is the only Jedi Defense refusal: "…it needs to be Light Side, and the Jedi Defense feat." Its gate is also in its properties, as "Use Limitation Feat (Jedi Defense)". Jolee's and Qel-Droma are red only for alignment.

   Unverified hint: `unmetFeat` skips any required feat that `requiredFeatId` can't map to an id in `widget.featIds`. Jedi Defense is `availability = "granted"`, so it may be missing from that set.

## Small

1. On Power Attack's confirmed critical, the tripled Power dice read "1d6 5+1+1" (three rolls under a 1d6 label), while the weapon's read "3d10".

Seen, not filed:
- Stasis cost 18 Force Points ("81 → 63 · ceiling −4"), while the cast menu listed it at 14f before the fight. Blindness had just moved Yard Jedi toward the dark side, so it's probably the alignment cost. One sample.
- Power One's damage adds "Strength 6" while her attack adds "Strength 4" (Strength 18, a one-handed Vibroblade, nothing in the off hand).

KNOWN, not filed: the Caution items show nothing in play; the stealth tier extras (re-hide, Marked Shot, the stun) are held.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
