# TEST 173 — recheck of the TEST 172 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-173/`. Read first: Coder's TEST 172 fixes entry.

## Build

App `ad2d11d` (git archive, lock unchanged). Lodestar `5487840dddd07492721aa74015dd23e79b531a88` = lock. Shelf `00b98e0` (my data dir). check_shelf clean (31 / 111). Fresh fixtures.

## Summary: all eight pass

| # | Check | Result |
|---|---|---|
| 1 | Boots | **PASS**: new Soldier, Treads off then back on from Equip (`1a-boots`); Store Bed sells Dockworker's Treads and Spacer's Magboots; bought the Magboots (In Inventory 1), equipped them, swapped back to the Treads (`1b-buy`, `1c-equip-mag`, `1d-swap-back`). Droid: no Boots square; bought Treads sit in its bag, Use Item dim, nothing equips them (`1e-droid-boots`). No line is shown because nothing offers to put them on |
| 2 | Help boxes after a board zoom | **PASS**: board zoomed by wheel first. Soldier: Inventory (click OK), Abilities (Enter), Map (Escape), Equip (Escape), Journal (Enter); each box closed and the screen stayed open (`2a`, `2b`, `2c`). Options and Character show no first-open box. Droid: Inventory (Escape), Abilities (click), Map (Enter), same result (`2d-droid`) |
| 3 | Surprised lines | **PASS**: "Teach Kael": "you are surprised" (`a2-line`); "Teach me": Kael's turn "Kael is surprised" (`b23`) |
| 4 | Descriptions | **PASS**: Grand Loremaster "Deep knowledge of the dead, the living, and the Force." then "+3 Archaeology, Mysticism, and Xenology." (`4-grand-loremaster`); Adept/Master Gear Head, Improved/Master Toughness, Advanced/Master TWF, Weapon Focus/Specialization: Blaster, Improved/Master Close Combat, Advanced Dueling, Weapon Specialization: Blaster Rifle, Armour Proficiency: Medium/Heavy, Master Conditioning: each a "what it is" line then the effect (`4-upgrades`). Improved/Master Cautious not located in the grid (same chain mechanism) |
| 5 | Worlds | **PASS**: Yavin "A gas giant with a station in orbit. Massassi temples stand on its fourth moon."; Taris, Dantooine, Kashyyyk, Manaan, Korriban, Lehon, Telos all have a line (`5-worlds`). Korriban's line still shouts "SECTOR HEADQUARTERS" |
| 6 | Lightsaber spacing | **PASS**: "Training Lightsaber blue" (`6-guardian-c`) |
| 7 | Abilities first look | Notes only: the K2-style screen opens on all three tabs; feats draw icons in chains; skills show a related attribute and description; the Powers help box shows K2's line; switching portrait to Kael changes the footer name and lists (`a1-s`, `a2-s`, `7-abilities`). Seen: many skill rows have no icon; Ash and Kael share the default portrait, so the switch shows the same face |
| 8 | Regression | **PASS**: enemy-turn hold (trooper first at 17; Options open 10 s, it fires only after close); Grise Heal 10f after a Shock, 217 → 207; Escape+F4 ×3 one save each; Jedi Guardian starts with Padawan Robe, Training Lightsaber blue, Adrenal Strength, 2 medpacs, Treads (`rg`, `6-guardian-c`) |

## Notes (not failures)

- **Store boots have no icon** in the store list (Dockworker's Treads, Spacer's Magboots), and the second reads "Spacer S Magboots" there (apostrophe lost; Equip shows "Spacer's Magboots") (`st0c`).
- **Both boots cost 0** in the store ("Item Cost 0", credits unchanged at 100) (`1b-buy`).
- The chargen Powers page now has taller rows with icons; my scripted clicks no longer land, so a power had to be picked by hand (Tester-side only).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
