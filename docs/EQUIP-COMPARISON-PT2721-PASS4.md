# EQUIP COMPARISON — PASS 4 (PT-2725)

K2 started by CODER again (read-only, `000008 - game7` and the stocked save, no slot written, left through Options → Exit Game → Quit). Captures: `HANDOFF/BUILD/screens/pt2721-equip-loop/pass-4/` (`k2-*` K2, `app-*` ours); the K2 panes for the three weapons and Jamoh Hogra's are the pass-3 captures taken the same day in the same game (`pass-3/`, copied here).

## 1. The armour Defence change — a DATA FIX, kept

**Ruling found: `PT-303`** (`PLAYTEST-RULINGS-01`, "Phase 1 tested against the wiki"): *"`Armor 4` plus heavy armour's base 9 is 13. The wiki's number is the TOTAL; the blueprint's is the item's contribution. So `Armor 5` does NOT mean Defence 5. It means +5 on top of the base item's class."* With `EQUIPMENT-01 §5` (Defence = 10 + armour bonus + capped Dexterity, the armour bonus being the class) and `PT-2144` (an item whose Defence is not its class's carries the finished number on its blueprint), the generator simply never wrote `Armor N` — exactly the 36b shape. Not a rules change. K2 agrees on three items (3, 7, 11). **Before/after for every armour: `rules/EQUIP-ARMOUR-DEFENCE-PT2725.md`.** Only **three shipped blueprints** change (Light Combat Suit 4→3, Reinforced Fiber 5→7, Jamoh Hogra's 7→11); no starting kit or standard blueprint carries an `Armor N`. **Case 1 applied** (ruling says Defence comes from the item's own property). Commits: shelf `42ef20a`, app `8049f16`, MAIN_WORK `f4267789`. ⚠ Five unique items carry more than one `Armor N` (sum taken, K2's stacking not observed; none is a shipped blueprint).

## 2. Row states — measured, built, mutation-checked

| state | K2 (measured) | ours |
|---|---|---|
| can't use | red-orange (204,51,0) border; stays red when selected; selecting it raises a popup box (196,0,0) border, (0,12,10) fill, "You cannot equip this item. You don't have the prerequisites. Please see the item description."; OK greyed (text (28,119,98), border (131,131,106)) | same; popup at (171,246) 190×119 canvas units; OK greyed and **cannot commit** (`_leave` refuses a blocked item) |
| rule | `baseitems.2da` `reqfeat0..4`, all required; Onjo (feat list read from the save: Light armour, blaster pistol/rifle, lightsaber, melee, Jedi Defense) lacks Medium | `unmetFeat` — one rule, K2's names joined to our feat ids (K2's "Armor" is our "Armour", K2's "Blaster Pistol" is our "Blaster"); an unmapped feat is unenforced |
| hover / focus | the focused or selected row is white (187,188,168); K2's **pointer** hover could not be provoked under xdotool (a pointer over a row changed nothing in four tries) | pointer hover and selection both white (owner: "everything turns white under the pointer") — **not pixel-verified against K2's pointer** |
| new item | amber (149,122,71) 2 px, fill (5,24,21), on the **Inventory** screen, `NewItem`=1 on all 14 bagged items of the save; cleared to the plain line as focus passes (Down key) | **Equip's lists draw them plain** (fresh capture) and so does ours. Not built: needs the Inventory screen (unbuilt); K2 keeps the flag in the item instance, we have no event kind for it |

## 3. The weapon lines — sources named

| line | source |
|---|---|
| `Range: 23m` | `baseitems.2da` **`maxattackrange`** (Blaster_Pistol 23, Blaster_Rifle 28; blank on melee → no Range line). Our wiki `range` "24 m" is not the game's |
| `Critical Threat:` / `20-20,x2` | **`critthreat`** (1 → 20-20, 2 → 19-20) and **`crithitmult`** |
| `Balanced: +2/+0 vs. two-weapon penalty if used in the off hand` | **`weaponsize` 2** (Small): the one column that separates the captured panes with the line (Short_Lightsaber, Blaster_Pistol) from the one without (Lightsaber, size 3); text = `dialog.tlk` 42145. Vibro_Blade/Short_Sword are inferred by the same column |
| `No Description Set` | `dialog.tlk` 32172, printed when the item's description is empty |

## Table (fresh K2 vs ours)

| Row | Status |
|---|---|
| armour panes (Light Combat Suit, Jedi Robe, Reinforced Fiber, Jamoh Hogra's) | **PASS** (pass 3) |
| Short Lightsaber, Blaster Pistol: Null panes | **PASS** — byte for byte (Blaster Pistol: `Feats` · `Damage: Energy, 1-8` · `Range: 23m` · `Critical Threat: 20-20,x2` · Balanced · `No Description Set`) |
| can't-use row, popup, greyed OK, never equippable | **PASS** (popup text size within a point of K2's) |
| row focus/hover white | **FAIL until K2's pointer hover is observed** — set from the owner's description |
| non-energy damage line | **FAIL — not reachable**: `000008` and the stocked save hold only the two lightsabers and the blaster; nothing in reach is picked up without moving through the Peragus level, and nothing may be saved. The owner can supply a K2 save that carries a vibroblade or a sonic/ion weapon |
| EXCUSED rows 1, 13, 14 | unchanged (named rulings) |

NOT READY FOR SIGN-OFF while the two FAIL rows stand; closing suites not run.
