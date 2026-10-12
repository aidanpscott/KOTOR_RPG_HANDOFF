# TEST 171 — the Precognition chain and the text sweep again

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-171/`. Read first: Coder's entry for the Precognition rulings and the TEST 170 fixes.

## Build

App `cb57359` (git archive, lock unchanged). Lodestar `b3b0dbafae70837b45f5ea7879a244b591601641` = lock. Shelf `e37a0b8` (my data dir). check_shelf clean (31 rules, 108 blueprints). Fresh fixtures.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Chargen text sweep | **FAIL (2 species lines)**: backstories clean (Acolyte through Scavenger, 12 read; Merchant ends "one starting item, one band above", no "see §") (`1a-merchant`, `bs`); Soldier equipment clean, Dockworker's Treads dimmed with no explanation (`1b-sol-equip`); droid class refusal "A droid cannot take this class." (`droid-class-refusal`); droid chassis/species pages clean (`dA`, `dB`). Two species pages still carry source notes: **Dashade** "…Not a KOTOR mechanic — it comes from the tabletop line, which is why it costs a pick." and **Kaleesh** "Hunter's scent … **UAA p.183.**" (`sp`) |
| 2 | Level-up | **PASS**: XP Bed, level-1 Soldier, dummy killed, Class / Skills / Feats; the Skills page shows no "recommended allocation" line (Recommended just does nothing) (`l2-recommended-s`) |
| 3 | Feats tab | **PASS** on the letter: no history, counts, sources or design notes in Skill Focus, Master Two-Weapon Fighting or 13 others (`ft`, `ft2`). But **Skill Focus is now empty** (no description at all), and several are bare fragments: Master Two-Weapon Fighting "−1.", Advanced Two-Weapon Fighting "−2.", Improved Close Combat "…drops to 0. Level 8" |
| 4 | Precognition / Battle Precognition | **Not offered** at level-up (list goes "Plating Proficiency: Light, Regenerate Vitality Points") (`fl`). **Battle Precognition PASS** with my own authored save (both feats in the log; the app accepts them, sheet shows both "chosen") (`4c-c`): fight Defence line in a Jedi Robe "base 10 + Dexterity 2 + armour 1 + class 2 + Battle Precognition 1 = 16"; in Reinforced Fiber Armor "… armour 7 + class 2 = 21", no term (`4kn`). **Precognition / ambush: not tested** — no package that starts with a concealed enemy has a holder, so no fixture can test it. Coder needs to add one. Not checked: chargen feat lists scrolled to "P" for a Jedi and a droid (level-up covered) |
| 5 | Regression | **PASS**: enemy-turn hold (Options 10 s, trooper acts after close, 40 → 36); Grise Heal 10f after a Shock, 217 → 207; Escape+F4 ×3 one save each; status line "Room" / "Command Deck" (`rg-hold`, `rg-grise`) |

## Notes

- My Battle Precognition fixture: `tool/tester_author_precog.dart` (my copy of the Strongroom author with `precognition` and `battle_precognition` added to the feats), save `pre-cog` (Jedi Sentinel 1, WIS 12 → +1).
- The sheet and the Equip DEF moved oddly once while swapping (17 shown right after "None"), probably a frame read too early; the fight's breakdown is the clean read and is what the table uses.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
