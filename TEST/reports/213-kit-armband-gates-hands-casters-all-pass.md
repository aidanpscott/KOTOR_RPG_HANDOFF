# TEST 213: a companion's file kit, Nomi's Armband in a fight, the Equip gate's reason, the right hand only, Casters' Hall

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-213/` (MAIN_WORK `5422229d`). The step-by-step log is `TEST/reports/213-running-log.md`.

## Build

- **App**: main `662feaf`, a git worktree beside my own clone. `gate.py --at 662feaf`: "FOR TESTER — CORE at 662feaf, 5288 tests, 0 failed"; ARCHIVE last green at 662feaf. Lodestar `191ac94` = lock = compiled. The build (11.2 s) went through the lock, and git status was clean.
- **Settings**: defaults. Brightness: default.
- **Shelf** `ba538b6`: tester-208 synced. I reran `author_tester_test208_saves.dart`, which adds proof-fewer, proof-equal and proof-more.

Local beds (copies in `specs213/`):

- **tester-kit**, with three alignment-20 companions and an enemy:
  - Crado Mate, in Crado's Robe;
  - Arca Mate, in Arca Jeth's Robe;
  - Weak Mate, Con 10, with a Bio-Antidote System implant;
  - Sith Arca, an enemy in Arca's Robe.
- **tester-gear**, plus Star Forge Robes, the Bio-Antidote System, Nikto Soldier Gloves and a Short Lightsaber.
- **tester-gear-dark** and **tester-gear-light**: one foe each, so the box shows that foe's line.
- **Rifle Soldier copies**: Soldier 10, blaster rifle, Nomi's Armband.

The implant amendment is applied.

## Summary: all pass; one ability item superseded

| # | Check | Result |
|---|---|---|
| 1 | Companion's file kit | **PASS**. Crado Mate is "Committed Dark (20)" with no refusal, and the robe counts (Defense 13). Arca Mate's Character Info reads "Arca Jeth's Robe has no effect: it needs to be Light Side." The enemy is not gated: the leader's swing at Sith Arca "needed 13", the same as the robed mates. **Recorded only** (per the amendment): Weak Mate reads "Bio Antidote System has no effect: it needs Constitution 16." |
| 2 | Nomi's Armband | **PASS**, with the same die rolls in both yards. The Dark Foe's line reads "needed 14 (+1 vs dark side)" against DEF 13; the Light Foe's reads "needed 13". An earlier light run is void because its armband never got equipped; I redid both runs with each equip checked on screen |
| 3 | Gate reasons under K2's line | **PASS**. Alignment: "Arca Jeth's Robe has no effect: it needs to be Light Side." Feat: "Star Forge Robes … needs to be Light Side, and the Jedi Defense feat." Class: "Nikto Soldier Gloves … needs the Soldier class." Ability: **SUPERSEDED**, since every ability-gated item in base-rules is an implant (42 of them). Recorded: the player's Bio-Antidote reads "… needs the Master Cybernetic Implantation feat." |
| 4 | Right hand only | **PASS**. In WEAPON L, Bastila's Lightsaber reads "… is already a pair — it cannot be held with a second weapon". A blaster rifle in WEAPON L reads "Blaster Rifle takes both hands — it cannot be held with a second weapon" (proficient Soldier; a non-proficient wearer is shown the proficiency first). The Short Lightsaber is accepted in WEAPON L. The double-blade is offered for WEAPON R, and the rifle equips in R |
| 5 | Casters' Hall | **PASS**, no crash. On Caster's turn F lists her own 1 / 3 / 5 powers on her own row with her pool "force 87 of 87". Casts spend from it: Force Aura 87 → 81; Force Push (the fifth) 87 → 81, stunning the Thug |
| 6 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save (slot 50, "reg213"), Escape then F4 (one quick save), Load, and a fight won |

## Small

- With a Short Lightsaber already in WEAPON L, OK on a double-blade in WEAPON R pops "… is already a pair — it cannot be held with a second weapon" and equips nothing. K2 empties the left hand instead.
- A companion's kit refusal is on Character Info only, under Alignment, not on the Stats tab. The order said "under the ratings".
- Kit Hall's HUD portraits cycled Weak Mate, Crado Mate and the leader only; I couldn't select Arca Mate there. Her Info was reached once, but her Stats weren't read.

KNOWN, not filed: the four 212 small items. I also didn't file the implant Constitution, per the amendment.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
