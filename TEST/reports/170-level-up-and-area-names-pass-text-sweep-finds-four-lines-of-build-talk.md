# TEST 170 — the text sweep again, and the level-up feat page

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-170/`. Read first: Coder's TEST 169 fixes entry.

## Build

App `3514567` (no newer hash with the power-cost rulings exists; git archive, lock unchanged). Lodestar `b3b0dbafae70837b45f5ea7879a244b591601641` = lock. Shelf `011539a` (my data dir). check_shelf clean. Fresh fixtures.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Chargen text, Jedi / Soldier / droid | **FAIL (3 lines)**: the TEST 169 leaks are gone (class page, pre-hub now "SPECIES AND CLASS / Continue", hub, portrait, powers "withheld"). Still there: Backstory **"see §2"** (Merchant, every class) (`q-bs`); Soldier Equipment **"boots — Dockworker's Treads — the catalogue gives it no base type, so no item can be made of it"** (`q-eq`). Minor wording: droid class refusal "no droid takes this class — one of engineer are open to a chassis"; a chassis line "The feat KOTOR grants T3-M4 by name" (`dA`) |
| 2 | Level-up (Soldier, XP Bed) | **PASS** for the flow: companion behind, dummy in front; killed in two rounds; Character > Level Up > Class, Skills, Feats; feat descriptions clean (Blindside, Conditioning, Gear Head, Hardiness, Improved Cautious); Soldier 2, 8 of 18 (`lvf`, `lvp`, `l-1-s`, `ft`, `l78`). **FAIL (1 line)**: the level-up Skills page says **"no recommended allocation is in the rules yet"** when Recommended is pressed (`l-4b-feats-s`) |
| 3 | Abilities, three tabs | **PASS** for skills (Acrobatics, Alertness, Archaeology, Athletics, Beast Handling) and powers: Heal no longer cites a rule; Lumen's Push 6, Shock 6+3=9, Heal 8−2=6 (`ab-sk`, `ab-pw`). **FAIL (feats)**: **Skill Focus** "Renamed from Class Skill. One feat exists per skill — 23 in total. The fourth of five aptitude sources."; **Master Two-Weapon Fighting** "−1, floored." (a fragment); Close Combat ends "Universal — granted to the Scout at 1, purchasable by anyone." (`ab-ft`). Feat cells draw no icons |
| 4 | Area names | **PASS**: "in your campaign, Room left you at 8", "…Command Deck left you at 154"; Load list place "Command Deck". The package menu shows only "6 saves" (no per-save rows to read). Shut door: "Door is locked — heroic security" (`rg-d12`) |
| 5 | Unpriced powers | Hidden: 3514567 is the newest build; Crush Opposition, Inspire Followers, Force Stasis Field, Dominate Mind and Precognition don't appear on chargen's Powers page, and no "withheld" line shows (`jC`) |
| 6 | Regression | **PASS**: enemy-turn hold (Options 10 s, trooper acts only after close); Grise Heal 10f after a Shock, cast 217 → 207; Escape+F4 ×3 = one quick save each (`rg-e`, `rg-g`) |

## The build-talk lines still on screen

1. Backstory: "see §2"
2. Soldier Equipment: "the catalogue gives it no base type, so no item can be made of it"
3. Level-up Skills: "no recommended allocation is in the rules yet"
4. Skill Focus: "Renamed from Class Skill. One feat exists per skill — 23 in total. The fourth of five aptitude sources."

Plus two oddities: "−1, floored." (Master Two-Weapon Fighting) and the droid class line "one of engineer are open to a chassis".

Skills: `verification-before-completion`. Kept small per the simplicity rule.
