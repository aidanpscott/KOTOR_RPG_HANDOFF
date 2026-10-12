# TEST 172 — boots, the full text sweep, the rewritten descriptions and the Precognition ambush

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-172/`. Read first: Coder's entries for boots and the TEST 171 fixes.

## Build

App `919a530` (no newer hash; git archive, lock unchanged). Lodestar `5487840dddd07492721aa74015dd23e79b531a88` = lock. Shelf `e835bde` (my data dir and clone). check_shelf clean (31 rules, 111 blueprints). Fresh fixtures.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Boots | **FAIL**: a new Soldier starts with Dockworker's Treads in the Boots square, not also in the bag (`1a-sol-equip`). Taking them off works, but **the Boots list then offers only "None"**: the Treads sit in the bag (`1-treads-in-bag`) and can't be put back on (`1-boots`). No store in any package sells boots, so "buy another pair" couldn't be done. Droid (T3-87): no Boots square (`1h-s`); "boots refused with a plain line" not testable (the droid has no boots to offer) |
| 2 | Starting items | **PASS**: Bounty Hunter (Blaster Pistol, Stun Baton, Stamina, 2 medpacs, Treads), Treasure Hunter (Blaster Pistol, Short Sword, Adrenal Stamina, Glow Rod…), Jedi Guardian (Padawan Robe, Training Lightsaber blue, Adrenal Strength…), Sith Warrior (Dark Padawan Robe, Training Lightsaber red…) (`bounty-s`, `2-classes`) |
| 3 | Text sweep | **PASS**: Dashade and Kaleesh pages clean (`3-species`); world openings are player sentences (`3-worlds-full`); 16 item descriptions in Inventory read as game text (`3-items`); professions read in TEST 171 and unchanged in shape. One world (Yavin, by list position) shows its skills but no description line |
| 4 | Descriptions | **PASS** with a note: no empty panes. Skill Focus "Grants aptitude in that skill: 1 point per rank instead of 2…"; Advanced/Master TWF "This feat further/again reduces the attack penalty… to −2 / −1."; Master Close Combat "When your target is within one range increment, you receive a +3 attack bonus…"; level-up feats show a description sentence then the effect (`4-abilities-feats`, `4-levelup-feats`, `4-master-close-combat`). But some higher tiers still show **only the effect line** with no "what it does" sentence: Grand Loremaster "+3 Archaeology, Mysticism, and Xenology.", Improved/Master Cautious, Adept Gear Head, Improved Toughness (`4-grand-loremaster`). Precognition not offered at chargen for a Jedi Consular or a droid (`4-jedi-chargen-feats`, `4-droid-chargen-feats`) |
| 5 | Recommended | **PASS**: dimmed and does nothing on chargen Abilities, level-up Skills and level-up Feats (`5-recommended`) |
| 6 | Precognition ambush | **PASS**: (a) "Teach Kael.", walk into the droid: ambush with the second droid hidden; Kael (16) acts in round 1, Dov Rask (13) tries to act: **"you are surprised"** (`6e-fight-s`, `6h-s`). (b) New character, "Teach me.": Ren Volt acts normally (5 moves, action); on Kael's turn his action is dimmed and he can't act (`6j-s`, `6l-s`). Kael's line reads "no move left this turn", not "surprised" (`6p-kael-act`) |
| 7 | Regression | **PASS**: Battle Precognition "+ Battle Precognition 1 = 16" in a Jedi Robe (`bp-line`); enemy-turn hold (`h`); Grise Heal 10f after a Shock, 217 → 207 (`g`); Escape+F4 ×3 one save each |

## New: a help box that can't be closed

On the droid (T3-87, Tester XP Bed), the Inventory's first-open help box appeared and **would not dismiss**: clicking its OK where it's drawn, and Enter, did nothing; it stayed over the play screen after the Inventory closed, and again on reopening (`FAIL-stuck-help-box`). The game kept running underneath (moves still worked). Before it, my library scroll (mouse wheel) had landed on the play board and zoomed it. Likely cause, not shown: the box is drawn under the board's zoom but hit-tested without it (on the board it sat at a different place than in the Inventory). An app restart cleared it.

## Notes

- Treasure Hunter's equipment page: "Training Lightsaber  blue" has a double space before the colour (Jedi and Sith too).
- Ambush, run (a): the board start square and Kael's position are fine; the hidden droid shows as "hidden" in the turn order.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
