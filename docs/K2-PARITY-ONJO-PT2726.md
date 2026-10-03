# K2-PARITY-ONJO-PT2726 — Onjo Trigit in K2 against the same character in ours

**`PT-2726` item 2.** Every derived number, K2 against ours, for one character, with the cause of every difference.
**K2 side:** save `000008 - game7` (read-only; never saved), read two ways — the save's own `Mod_PlayerList[0]` (`scripts/extract_save_character.py` → `data/extracted/character_000008.json`) and K2's own screens (Character, Abilities, Equip), captured live.
**Our side:** `KOTOR-RPG-APP-clean/test/k2_parity_onjo_probe_test.dart` builds the same character (Human male Jedi Sentinel 1; base abilities 12/14/14/14/12/12 — K2's own; skill ranks 4 in Stealth/Awareness/Persuade/Security; the six proficiency/Jedi Defense feats our feat list has; the same eight worn items) and asks the production screen for every number. It writes `~/kotor-home/.parity-ours.json`.

**Classes of difference:** **(a)** authored — a ruling is cited. **(b)** unintended — fixed at the cause, test first. **(c)** unclear — listed for the owner; nothing guessed.

---

## 1 · The table

| # | Number | K2 | Ours (after this pass) | Class | Cause |
|---|---|---|---|---|---|
| 1 | Species / class / level | Human · Jedi Sentinel · 1 | same | = | |
| 2 | **STR** (gear on) | 17 (+3) | 17 (+3) | **= after fix** | **(b) fixed.** The sheet read the record's raw 12 and the Equip readout added a +1 where the sheet said 17. K2's 17 is 12 + Dominator Gauntlets +5. Fixed at one reader, `_scoreWithGear` (`play_screen.dart`) = bought + species + `§4`'s `mergedAbilityBonuses`, the number `Combatant.scoreOf` rolls. Tests: `worn_gear_reaches_the_sheet_test`, `equip_readout_uses_worn_strength_test` (A = STR 12 + gauntlets, B = STR 17 bare; every readout identical). |
| 3 | DEX / CON | 14 / 14 | 14 / 14 | = | |
| 4 | **INT / WIS / CHA** | 15 / 13 / 13 | 14 / 12 / 12 | **(a)** | K2 wears the Mental Boost Package (+1 to each of the three). Ours **refuses the implant** for this character: `Mental Boost Package needs cybernetic_implantation or advanced_… or master_…`. The base type's feat gate is authored (`EQUIPMENT-01 §12`/`§17`, `PT-2344`); K2's `baseitems` carries no such feat and K2's own pane for the item prints only `Attributes Required: Minimum Constitution: 12`. The sheet shows the refusal in red beside Defence. |
| 5 | Vitality | 36 / 36 | 10 / 10 | **(a)** for the scale, **(c)** for K2's magnitude | Ours: the hit die at level 1 (d8) + Constitution modifier (+2) = 10, nothing rolled — `PT-648`, one pool — `PT-559`/`PROPOSAL-VITALITY-01`. K2's 36 is what its engine stores (`MaxHitPoints` 36, `LvlStatHitDie` 8); it is **not derivable from the save's own class table** (d8 + Con 2 = 10), so the scale difference is authored but *why K2 reads 36* is open. |
| 6 | Force points | 0 / 0 | 8 / 8 | **(a)** | Ours gives every Force class its pool (`FORCE-POOL-01-v3`; the Sentinel table row 1 is 9 at WIS 14). K2's `000008` is the Exile at the start of the story: LvlStatForce 0, no powers learned (every slot on the Powers page reads "Unknown Force Power"). A story state K2 holds in the save; our rules have no such state. |
| 7 | Force powers | none (7 empty slots) | none chosen | = | |
| 8 | **Defence** | 17 | 17 | = | K2: 10 + DEX 2 + Light Combat Suit (class 4, `DecreaseAC −1` → 3) + class 2. Ours: `base 10 + Dexterity 2 + armour 3 + class 2` (`CLASS-DEFENCE-01`). Nomi's Armband's +1 vs. Dark Side is **conditional** and in neither number. |
| 9 | Fortitude / Reflex / Will | 4 / 4 / 4 | +4 / +4 / +4 | = | Fort 2 + CON 2; Ref 2 + DEX 2; Will 1 + WIS 1 + Neural Band +2 (K2 `cls_st_jedi_s` row 1 is 2/2/1, which `CLASS-TABLES-JEDI` carries). The Neural Band's Will +2 reached the **sheet** only in this pass — see §3. |
| 10 | Attack modifier, main hand | 0 | −1 | **(c)** | Ours = BAB 0 (`CLASS-TABLES-JEDI` row 1) + STR +3 − 4 (the dual-wield penalty, no Two-Weapon feat — `ACTION-ECONOMY-01 §7.2`, applied to **every** attack). K2's 0 cannot be rebuilt from its own tables: `cls_atk_1` gives BAB 1 at level 1, STR is +3, so no plain sum reads 0. What K2's "Attack Modifier" adds up is unknown. |
| 11 | Attack modifier, off hand | −6 | −1 | **(a)** for the shared penalty, **(c)** for K2's hand-specific −6 | K2 puts the whole penalty on the off hand (main 0 / off −6); `ACTION-ECONOMY-01 §7.2` puts the same penalty on every attack. |
| 12 | Damage range, main hand | 5–23 | 5–19 | **(a)** | Lightsaber dice: ours 2d8 (`equipment.toml` `damage`), K2 2d10 (`damage_k2`); both + STR +3. **`PT-2727` (Main): the description pane now prints OUR dice too** (`Damage: Energy, 2-16`), from the same source as the readout and every roll; `damage_k2` is reference data only. **EXCUSED — ruled rules difference (our weapon dice).** |
| 13 | Damage range, off hand | 3–17 | 3–13 | **(a)** both | Short Lightsaber: ours 2d6, K2 2d8 (a). **Off-hand Strength: `PT-2727` (owner) — half the modifier, rounded down (+3 → +1), as K2 does; built, so ours now reads +1 too** (was the full +3: 5–15). `ACTION-ECONOMY-01 §7.2a`. |
| 14 | Equip DEF badge | 17 | 17 | = | |
| 15 | **Skill: Computer Use** | 4 ranks +2 = 6 | no such skill | **(a)** | `SKILLS-01 §8` and `PT-370`: Computer Use and Treat Injury are K2's, this ruleset did not keep them; Slicing is *an application of* Computer Use, not a rename. (The same ruling is why the Exchange Casual Gloves' +1 Computer Use is not applied.) |
| 16 | Skill: Stealth | 4 + DEX 2 = 6 | 6 | = | |
| 17 | Skill: Awareness | 4 + WIS 1 = 5 | 6 (4 + INT 2) | **(a)** | Our Awareness is keyed to INT, K2's to WIS (`SKILLS-01 §1`; our Alertness is the WIS one). The INT/WIS gap of #4 is a second, smaller cause. |
| 18 | Skill: Persuade | 4 + CHA 1 = 5 | 5 | = | |
| 19 | Skill: Security | 4 + INT 2 = 6 | 6 | = | |
| 20 | Skill: Repair | 0 + INT 2 = 2 | 2 | = | |
| 21 | **Skill: Demolitions** | 0 ranks → **0** (refused) | 0 ranks → **refused** | **(a) `PT-2727`** | K2's `skills.2da` has `Untrained` 0 for Demolitions, Stealth and Security. **Owner ruled (PT-2727): trained-only, as K2 — `SKILLS-01 §11a`, `SKILL-RESOLUTION-01 §7a`.** With no ranks the action is refused with a stated reason and never rolled. (Apart from §11's Aptitude, which is a cost rule.) |
| 22 | Skill: Treat Injury | 0 + WIS 1 = 1 | Medicine 0 + WIS 1 = 1 | **(a)** | Same number under our name (`PT-370`: not a rename). |
| 23 | Alignment | `GoodEvil` 50 | Neutral 50 | = | |
| 24 | XP | 0 / 1000 | level 1, XP 0 | = | |

## 2 · Starting feats and abilities

| K2 `FeatList` (17) | Ours (the 6 our feat list expresses, all `chosen`) |
|---|---|
| Armor Proficiency: Light · Weapon Proficiency: Blaster Pistol · Blaster Rifle · Lightsaber · Melee Weapons · Jedi Defense | the same six |
| Critical Strike · Flurry · Power Attack · Power Blast · Rapid Shot · Sniper Shot | **not carried** — **(c)**. K2's save holds the Exile's authored starting kit; our Sentinel row 1 grants **one** feat (`CLASS-TABLES-JEDI`: feats `1` at level 1), so six combat feats at level 1 is not something our class gives. |
| Jedi Sense · Force Immunity: Fear | **not carried** — **(c)**. These look like K2 class grants (not verified against a K2 class-feat table in this pass — the installed 2das carry no `cls_feat_*` file); our Sentinel table lists no equivalent level-1 grant. |
| War Veteran · Toughness · Complex Unarmed Animations | **not carried** — **(c)**. Probably the Exile's template (unverified); if Toughness adds Vitality in K2 it would belong to row 5's open magnitude — not checked. |

`Starting abilities`: the Sentinel's Force powers are empty in K2 (§1 row 7); ours chooses none here, so there is nothing to compare.

## 3 · What this pass fixed (the (b) rows, test first)

1. **The sheet's ability scores ignored worn gear** (row 2) — and with them every save, Defence and skill row derived from them. One reader now, `_scoreWithGear`.
2. **The Equip readout's Strength/Dexterity ignored worn gear** (row 2/10–13) — the same fault at the second reader. Fixed with the same reader; the test builds the same score two ways and requires identical readouts.
3. **A worn item's saves, skills, resistances and immunities never reached any roll** unless its blueprint restated them. A blueprint that only names `catalogue = <resref>` (everything chargen delivers) carried its *abilities* through the catalogue row and nothing else, so the Neural Band's Will +2 appeared in the pane and nowhere in the numbers. `wornAt` now joins the row's `save`/`skill`/`resist`/`immune` effects for a table the blueprint does not state itself (a blueprint's own table still wins). The sheet's three saves show the worn bonus (they already rolled it in a fight).

## 4 · Listed for the owner (c) — **all six now RULED, `PT-2727`**

*(1) K2's attack modifier and (4) K2's vitality and (5) the starting feats are recorded as known differences, no change; (2) off-hand Strength is half, built; (3) trained-only is built; (6) the pane shows our dice. The list below is as it stood.*

1. **K2's attack modifier** (rows 10–11): what it adds is not recoverable from its tables (BAB 1 + STR 3 would read +4, it shows 0 / −6).
2. **Off-hand Strength** (row 13): K2 gives the off hand half; ours the full STR modifier. No ruling found.
3. **Untrained skills** (row 21): K2 refuses an unranked Demolitions/Stealth/Security (0); ours rolls it.
4. **Vitality 36** (row 5): the K2 magnitude is unexplained by its own class table.
5. **Starting feats** (§2): eleven K2 feats ours does not grant at level 1.
6. **A mismatch inside our own Equip screen:** the description pane prints K2's weapon dice (`Damage: Energy, 2-20`, `damage_k2`, per `PT-2725`) while the readout beside it and every roll use ours (2d8 → 5–19). Two numbers on one screen for one weapon.

## 5 · Known differences, recorded with no change — `PT-2727` (owner via Main)

- **K2's attack modifier (0 main / −6 off hand)** cannot be rebuilt from K2's own tables; ours follows our ruled attack rules (BAB per `CLASS-TABLES-JEDI`, the dual-wield penalty on every attack per `ACTION-ECONOMY-01 §7.2`).
- **K2's vitality of 36**: ours follows the one-pool ruling (`PT-559`, `PT-648`).
- **The eleven K2 starting feats**: Onjo is the Exile, K2's authored story character; our classes grant their own feats.
- **Force 0/0 (K2) against 8/8 (ours)**, **Mental Boost refused**, **Computer Use / Awareness key / Treat Injury naming** — authored rows above, unchanged.
