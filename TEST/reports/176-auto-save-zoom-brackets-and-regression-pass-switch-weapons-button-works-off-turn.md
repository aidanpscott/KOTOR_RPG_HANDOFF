# TEST 176 — recheck of the TEST 175 fixes and the weapon swap

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 launched. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-176/` (MAIN_WORK `f2059914`). Read first: Coder's TEST 175 fixes entry and the 3443d31 commit.

## Build

App `3443d31cca15819f17f038f2c6b0291b18f6d2f9` (git archive, lock unchanged after build). Lodestar `be1319a5020337e561e6094bd7d2784e866d0045` = lock. Lens `bfc9bff8daeac99c39da6a38283f41dd1551faa2` = lock. Shelf `0f04d41` (my data dir). `tool/env.sh` sourced (it now only puts Flutter on PATH and sets KOTOR1_DIR/KOTOR2_DIR). check_shelf clean (31 rules, 111 blueprints). Fresh fixtures.

**Which build ran what:** I started on `8712a02` before the order moved to `3443d31`. The only change between them is in `_commitEquip` (weapon picks in a fight) plus `_syncFightWeapons`. The Switch Weapons button, Auto Save, zoom and bracket code are untouched. Item 1, item 2 (large room) and the three-press Switch Weapons button sequence in item 4 ran on `8712a02`. Everything else ran on `3443d31`.

## Summary: four pass, one partial

| # | Check | Result |
|---|---|---|
| 1 | Auto Save | **PASS**: Lo Vane dismissed Kael and left the session. Control: Auto Save row shows only Lo (`1a`). New Mo Reed with Kael: Options > Load Game in play, the Auto Save row shows Kael with his face (`1b`). Auto Save, Quick Save and the manual save "mo" all show Kael + Mo (`1c`). After leaving the session, the menu's Load list shows the same (`1d`). Reverse check: dismissing Kael in play, then Load Game, makes the Auto Save row show Mo alone (`1e`) |
| 2 | Zoom | **PASS**: large room (Precognition Ambush): out stops with the whole room in view and a margin; in reaches about 3× (`2a`). Small room (Ion Blaster 2×2): out stops a little smaller than fit, never a speck; in about 3× (`2b`) |
| 3 | Brackets | **PASS**: Comlink now reads "Comlinks are a standard, short range communication device." with no note (`3a`). No brackets in Crystal, Clothing, Medpac, Torch, Adrenal, Ion Blaster, Computer Spike, Treads, Repair Kit (`3a`, `3b`). None in seven feats either (WP Blaster, WP Blaster Rifle, Armour Proficiency: Light, WP Melee, Jedi Defense, WP Lightsaber, Two-Weapon Fighting) (`3c`, `3d`). The **[Modded]** tag still shows on Onjo Hp's Auto Save and Quick Save rows (`3g`). **[Slicing]/[Repair] not reached**: the only console offers "Slice (Slicing)" (round brackets) and is refused before its replies, "slicing in costs 3 spikes … you have 0" (`3e`, `3f`). No fixture carries 3 spikes |
| 4 | Weapon swaps | **PARTIAL**. Passes: own turn, slot picks: first free, the second dims the Action, a third is refused: "putting your weapon away — you have spent your interaction and your Action" (`4i`). Switch Weapons button ×3: first "you switch weapons", second costs the Action, third changes nothing ("switching weapons — you have spent your interaction and your Action") (`4a`, `4b`). Off-turn slot pick refused: "you can change weapons on your own turn" (`4f`). Armour refused: "armour and other gear cannot be changed in a fight — only weapons" (`4g`). After a swap the next attack uses the new weapon: "Short Sword · rolled 6 …" (`4h`). Next turn the free swap is back: "you switch weapons", Action still lit (`4c`). **FAIL: the Switch Weapons button works off your turn.** On the droids' turn, Switch Weapons swapped Ty's configs with no refusal (`4d`, `4e`). Cause in the code: `_interactionToll` returns ok/free when it isn't the player's turn, and only the slot-pick path has the new turn check |
| 5 | Quick regression | **PASS**: party bar faces (Lo + Kael) (`5a`); hidden droid off the Map (`5b`); "Buyer Crystal" (`5c`); sell list offers only Adrenal and Medpac, no Torch or Comlink (`5d`); bought Treads, boots on/off/on (`5e`); Escape+F4 ×3: one quick.mark each, no other file touched |

## Notes (not failures)

- **A chargen Soldier can't re-equip its own starting weapons.** Ty Ash (scripted Soldier) starts with a Short Sword and a Blaster Rifle but lacks Melee and Blaster Rifle proficiency. Both attack fine while worn, but once put away they're red and refused: "You cannot equip this item. You don't have the prerequisites." (`4j`).
- Kael can't be re-recruited after "Dismiss from party" in Precognition Ambush ("nothing to do there"). For item 1 I used a fresh character instead.
- Continue in Store Bed opens T3-46 (the most recent Store Bed character), not the seller; I loaded it through Switch Characters.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
