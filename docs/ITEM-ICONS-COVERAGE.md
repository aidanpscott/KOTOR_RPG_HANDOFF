# ITEM-ICONS-COVERAGE — every catalogue item's icon (PT-2744 item 1, for the owner)

**1353 of 1424 catalogue items now have their own game icon** (964 from K2, 389 from K1; K2 first where both games have the item). Derived, not picked: `i` + the base item's `itemclass` (`baseitems.2da`) + `_` + the `.uti`'s model (or texture) variation, read from each item's own `.uti` (chitin templates, else a module), the texture from that game's `swpc_tex_gui.erf`. Script: `scripts/extract_all_item_icons.py`; the per-item map: `data/extracted/item_icons.json`. The art is in the app's private repo (`assets/extracted/items/`), never HANDOFF.

A standard blueprint with no catalogue row of its own (`items/weapons/ion-blaster`) draws the game's icon for the item of its name, K2's first. A guard test fails if any carried item that maps to game art draws an empty cell (`every_item_the_games_draw_has_its_icon_test.dart`).

## The 71 without art, and why

| Why | Count |
|---|---|
| an item of ours (authored; neither game has it) | 39 |
| a creature's natural weapon or hide (the games give these no icon) | 25 |
| the icon the game names is not in its texture pack (ia_cloths_010; no .uti) | 1 |
| the icon the game names is not in its texture pack (ia_cloths_011; no .uti) | 1 |
| the icon the game names is not in its texture pack (ia_class6_010; no .uti) | 1 |
| the icon the game names is not in its texture pack (ii_torch_001; no .uti) | 1 |
| the icon the game names is not in its texture pack (base item has no itemclass; no .uti) | 1 |
| the icon the game names is not in its texture pack (iw_crbite_001; no .uti) | 1 |
| the icon the game names is not in its texture pack (iw_crpierce_001; no .uti) | 1 |

## The list, with a proposal for each (the owner rules)

The proposal is the icon of the nearest game item WITH art: the same base type, else the same category, lowest tier first. "none" where nothing shares either.

| Item | Id | Why | Proposed icon (from) |
|---|---|---|---|
| Training Lightsaber | `a_w_trnsbr01` | an item of ours | k2:iw_lghtsbr_007 (Lightsaber, same category) |
| Training Double-Bladed Lightsaber | `a_w_trnsbr03` | an item of ours | k2:iw_dblsbr_006 (Double-Bladed Lightsaber, same category) |
| Training Short Lightsaber | `a_w_trnsbr02` | an item of ours | k2:iw_shortsbr_006 (Short Lightsaber, same category) |
| Marksman Rifle | `a_w_mrksmnrfl01` | an item of ours | k1:iw_blstrcrbn_001 (Blaster Carbine, same category) |
| Sniper Rifle | `a_w_snprrfl01` | an item of ours | k1:iw_blstrcrbn_001 (Blaster Carbine, same category) |
| Sparring Gloves | `a_gloves_00` | an item of ours | k2:ii_gauntlet_001 (Insulated Gloves, same category) |
| Echani Sparring Gloves | `a_gloves_00b` | an item of ours | k2:ii_gauntlet_001 (Insulated Gloves, same category) |
| Clarity Package | `a_imp1_11` | an item of ours | k2:ii_implant1_002 (Reflex Package, same category) |
| Motor Package | `a_imp1_12` | an item of ours | k2:ii_implant1_002 (Reflex Package, same category) |
| Presence Package | `a_imp1_13` | an item of ours | k2:ii_implant1_002 (Reflex Package, same category) |
| Fortitude Package | `a_imp1_02` | an item of ours | k2:ii_implant1_002 (Reflex Package, same category) |
| Will Package | `a_imp1_03` | an item of ours | k2:ii_implant1_002 (Reflex Package, same category) |
| Shock Arm | `a_shockarm_01` | an item of ours | none |
| Advanced Shock Arm | `a_shockarm_02` | an item of ours | none |
| Dockworker's Treads | `a_boots_01` | an item of ours | none |
| Spacer's Magboots | `a_boots_02` | an item of ours | none |
| Tarisian Streetwalkers | `a_boots_03` | an item of ours | none |
| Dune Striders | `a_boots_04` | an item of ours | none |
| Kashyyyk Climbing Boots | `a_boots_05` | an item of ours | none |
| Republic Marching Boots | `a_boots_06` | an item of ours | none |
| Sith Trooper Greaves | `a_boots_07` | an item of ours | none |
| Corellian Smuggler's Softsoles | `a_boots_08` | an item of ours | none |
| Echani Duelling Slippers | `a_boots_09` | an item of ours | none |
| Mandalorian Battle Greaves | `a_boots_10` | an item of ours | none |
| Cortosis-Weave Boots | `a_boots_11` | an item of ours | none |
| Jedi Traveller's Boots | `a_boots_12` | an item of ours | none |
| Zeltron Gravity Shoes | `a_boots_13` | an item of ours | none |
| Refinery Sole-Guards | `a_boots_16` | an item of ours | none |
| Ithorian Wading Boots | `a_boots_17` | an item of ours | none |
| Salvager's Steel-Toes | `a_boots_18` | an item of ours | none |
| Undercity Waders | `a_boots_19` | an item of ours | none |
| Cantina Dress Boots | `a_boots_20` | an item of ours | none |
| Selkath Pressure Boots | `a_boots_21` | an item of ours | none |
| Czerka Surveyor's Boots | `a_boots_22` | an item of ours | none |
| Onderon Ridgewalkers | `a_boots_23` | an item of ours | none |
| Sith Academy Initiate Boots | `a_boots_24` | an item of ours | none |
| Nar Shaddaa Slipsoles | `a_boots_25` | an item of ours | none |
| Krath War Boots | `a_boots_14` | an item of ours | none |
| Vanguard Assault Boots | `a_boots_15` | an item of ours | none |
| Assault Droid Mark I Hide | `g_i_crhide001` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Assault Droid Mark IV Hide | `g_i_crhide002` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Rakghoul Fiend & Kataarn Hide | `g_i_crhide003` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Tuk'ata Hide | `g_i_crhide004` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Katarn Hide | `g_i_crhide005` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Tuk'ata Hide | `g_i_crhide006` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Canderous' Hide | `g_i_crhide007` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Droid Hide | `g_i_crhide008` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| HK-47 Hide 1 | `g_i_crhide009` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| HK-47 Hide 2 | `g_i_crhide010` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| HK-47 Hide 3 | `g_i_crhide011` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| HK-47 Hide 4 | `g_i_crhide012` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| HK-47 Hide 0 | `g_i_crhide013` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Canderous' Agility Hide | `g_i_crhide014` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Droid Hide Debuffer | `g_i_crhide015` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Canderous' Strength Hide | `g_i_crhide016` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Canderous' Endurance Hide | `g_i_crhide017` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Canderous' Regen Hide | `g_i_crhide018` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Veerkal Bite | `g_w_crslprc001` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Tuk'ata Bite | `g_w_crslprc002` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Gizka Bite | `g_w_crslprc003` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Dire Tuk'ata Bite | `g_w_crslprc004` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Shyrack Wyrm Bite | `g_w_crslprc005` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Katarn Slam | `g_w_crgore001` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Dire Katarn Slam | `g_w_crgore002` | a creature's natural weapon or hide | k2:iw_crslash_001 (Claw1d4, same category) |
| Clothing {Variant Czerka} | `g_a_clothes011` | the icon the game names is not in its texture pack | k2:ia_cloths_001 (Atton's Ribbed Jacket  UNIQUE, same base) |
| Clothing {Variant 11} | `g_a_clothes012` | the icon the game names is not in its texture pack | k2:ia_cloths_001 (Atton's Ribbed Jacket  UNIQUE, same base) |
| Khoonda Militia Armor | `a_khoonda` | the icon the game names is not in its texture pack | k2:ia_class6_001 (Military Suit, same base) |
| Torch | `g_i_torch01` | the icon the game names is not in its texture pack | k1:ii_collarlgt_001 (Collar Light, same category) |
| Recording Rod | `g_i_recordrod01` | the icon the game names is not in its texture pack | k2:ip_pltuseitm_001 (Aesthetic Item, same category) |
| Energy Emitter Mk 1 | `w_blhvy001` | the icon the game names is not in its texture pack | k1:ia_cloths_001 (Energy Emitter Mk 1, same category) |
| Energy Emitter Mk 2 | `w_lghtsbr001` | the icon the game names is not in its texture pack | k1:ia_cloths_001 (Energy Emitter Mk 1, same category) |


## Force powers (PT-2747): 106 of 106 have an icon

86 are the games' own, matched by name in `spells.2da` (K2 first, K1 as the fallback). The 20 below are ours, in neither game; the owner approved one icon each from the proposal sheet (private: `MAIN_WORK media/screens/pt2747-abilities/proposed-icons-for-our-20-powers.png`): an unused K2 icon nearest in meaning, or the icon of the power each one extends or copies. `scripts/extract_power_icons.py` carries the same table (`APPROVED`).

**Owner ruling (PT-2747): where the Full Force Mod (installed under `kotor 2 mods/Full Force Mod-987-1-0`) has its own icon for one of our powers, that icon is used instead of the stand-in, everywhere the power is drawn** (the Abilities screen and chargen's Powers screen read the one asset). Seven come from the mod (`FFM_ICONS` in the script): Arrow of White Dawn, Dark Healing, Deadly Sight, Force Combustion, Force Enflame, Sever Force and Spear of Midnight Black. The other thirteen keep the approved stand-in below.

| Power | Icon (K2 `swpc_tex_gui.erf`; ✦ = now the Full Force Mod's own) |
|---|---|
| Beast Control | `ip_affectmind` |
| Force Distraction | `isa_senses` |
| Dark Fury | `ip_fury01` |
| Deadly Sight | ✦ was `ip_horror` |
| Dark Healing | ✦ was `ip_drainlife` |
| Force Blindness | `isa_camo` |
| Force Enflame | ✦ was `ip_fury02` |
| Force Combustion | ✦ was `ip_scram01` |
| Force Incinerate | `ip_scram03` |
| Sever Force | ✦ was `ifrm_force04` |
| Force Sleep | `ip_sleep` |
| Force Mire | `ip_slow` |
| Force Root | `ip_hold` |
| Force Static Field | `isa_psystance` |
| Force Strangle | `ip_wound` |
| Force Contagion | `ip_plague` |
| Shutdown | `ip_droiddisable` |
| Overload | `ip_droiddestroy` |
| Spear of Midnight Black | ✦ was `ip_fury03` |
| Arrow of White Dawn | ✦ was `isa_rage` |

## Skills and feats (PT-2747): 6 of 26 skills, 75 of 322 feats

**63 feats** match a game feat by exact name (spelling normalised only), K2 first, K1 as the fallback. **Owner ruling (2026-10-12): a feat that is the game's feat at the same tier under another name takes its icon.** `scripts/extract_ability_icons.py` (`by_tier`) walks the game's own chains down `feat.2da`'s `successor` column. It anchors each of our chains to a game chain through a tier whose name matches exactly; every exact match in the chain must agree on the same offset; then our tier n takes the game's tier n. That gives **9 more**, for the owner to check:

| Ours | The game's | Icon |
|---|---|---|
| Advanced Two-Weapon Fighting | K2 Improved Two-Weapon Fighting | `if_2weap02` |
| Adept Gear Head | K2 Improved Gear Head | `if_gearhead02` |
| Force Jump Advanced | K2 Improved Force Jump | `if_jump02` |
| Force Jump Mastery | K2 Master Force Jump | `if_jump03` |
| Logic Upgrade: Combat | K2 Logic Upgrade | `if_droidac01` |
| Advanced Dueling | K2 Improved Dueling | `if_duel02` |
| ~~Unarmed Specialist II–VIII~~ | ⚠ split into II to VIII, one row per tier (TEST 191, MAIN 2026-10-22); each now takes K2's own tier icon | `if_unarmspec02` to `08` |
| Advanced Assassin Protocols | K2 Modified Assassin Protocols | `if_assassin02` |
| Master Assassin Protocols | K2 Integrated Assassin Protocols | `if_assassin03` |
| Weapon Proficiency: Blaster | K2 Weapon Proficiency: Blaster Pistol (named alias, see below) | `if_weapprof01` |
| Weapon Focus: Blaster | K2 Weapon Focus: Blaster Pistol (by tier from the alias) | `if_weapfoc01` |
| Weapon Specialization: Blaster | K2 Weapon Specialization: Blaster Pistol (by tier from the alias) | `if_weapspec01` |

**One named alias (TEST 174):** our blaster family is K2's blaster pistol family. Our own Weapon Focus: Blaster reads "with blaster pistols and hold-outs", and K2's row 39 is Weapon Proficiency: Blaster Pistol. The alias (`ALIASES` in the script) anchors the chain; the tier pass does the rest. Feats with a game icon: 75 of 322.

Not matched, because no tier's name anchors the chain: our Superior Two-Weapon Fighting chain against K2's "Superior Two-Weapon Fighting I/II/III" (the names differ by the numeral). Feats and skills with no game equivalent draw K2's empty slot, as ruled. Test: `abilities_k2_test.dart`, "a feat matched to K2's by chain and tier draws K2's icon".
