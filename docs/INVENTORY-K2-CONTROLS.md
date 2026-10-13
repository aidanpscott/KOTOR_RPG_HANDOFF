# INVENTORY-K2-CONTROLS — every part of K2's Inventory screen, and whether ours can have it

**For the owner (PT-2742 item 1, sent before building the parts that differ).** Source: K2 itself, read-only, captured live 2026-10-10 (`MAIN_WORK media/screens/pt2741-k2-session/`, a save with 22 items, every count 1, the player alone), and K2's layout file `inventory_p.gui` with its strings from `dialog.tlk`.

Legend: **YES** we build it as K2 has it · **MEANS** we build it, with a meaning that differs · **CANNOT** the thing does not exist here · **RULE** the owner decides. The recommendation is mine. Everything marked YES is being built now.

## The screen
| K2 | Ours | Status / recommendation |
|---|---|---|
| Title "Inventory", the eight quick-menu icons, Close | the shared K2 chrome (as Options and Equip) | YES |
| The FILTER block and the tab strip between two thin rules | ours has them, drawn plainly | YES, redrawn with K2's art and font |
| The portrait footer: name, class and level, portrait | shared with Options and Equip | YES |
| The list: an icon cell beside each name, K2's row border, a scroll bar | ours: names only, an empty box where the icon goes | YES: K2's rows and scroll bar; icons from the Equip pipeline |
| On opening, the first row is selected and its description shown | ours opens with nothing selected | YES |
| Hover: the row under the pointer gets a bright border | none | YES |

## The filter tabs (K2's order: All, Datapads, Weapons, Armor, Useable, Quests, Misc)
Our game's item list (1424 items) sorts into them as: Weapons 356, Armor 197, Useable 110, Quests 13, Datapads 2, Misc 746.
| Tab | Do we have items for it? | Status / recommendation |
|---|---|---|
| All | yes | YES |
| **New** (owner addition, ruled) | items picked up and not yet selected in the Inventory | YES, right after All, K2's tab art, K2's own word "NEW" (string 238). Recorded as an owner-ruled difference. The starting kit is not "picked up", so it does not start as new; bought, looted and recovered items do |
| Datapads | 2 datapads exist in the item list, but no adventure gives one yet | YES: the tab stays, empty until an adventure gives a datapad |
| Weapons | yes | YES |
| Armor | yes | YES |
| Useable | yes: medpacs, adrenals, shield generators, grenades, mines, rockets | YES |
| Quests | 13 quest items exist (Keycard, Comlink, ...), but no adventure gives one yet | **RULE:** the Strongroom's Sith Keycard opens a door but is filed as an ordinary item, so it lands in Misc. In K2 keycards are quest items. Recommend: an item that opens a door counts as a quest item and goes under Quests |
| Misc | yes | YES. **Found while checking:** items from the starting kit and stores all land in Misc today, whatever they are (the screen looks up their type the old way). Fixed as part of the build |

## What the list holds
| K2 | Ours | Status / recommendation |
|---|---|---|
| K2's help box says the Inventory lists "all the items **not currently equipped**". Worn items are not in it | ours lists worn items too, marked "(Equipped)" (`PT-1251`) | **RULE:** recommend K2: leave worn items out (the Equip screen shows them). One less thing in the list |
| An empty tab: both panes simply blank | ours prints "nothing here under WEAPONS — the filter is hiding 4 other things" (`PT-2493`) | **RULE:** recommend K2's blank panes. The New tab's empty state is ruled to look like K2's, and one empty look for every tab is simpler |
| Stacks (a count on one row) | ours shows the count on the icon | **BUILT (2026-10-13):** K2 prints a stack's number on the item's icon, bottom right, in teal, and leaves the name alone (captured after all: `signoff-saveload-options/k2-medpac/k2-medpac-inventory-description.png`, Adrenaline Amplifier with a "5"). Ours matches without the dark box K2 draws behind the digit (owner). |

## The first-open help box
"The PARTY INVENTORY screen shows a list of all the items not currently equipped by other party members or the companions back at your base. This inventory is shared by all party members." (string 42136), with OK.
**CANNOT / leave out.** It is a tutorial popup, and Tutorial Popups were ruled out at `PT-2734`. Its words also describe a base and a shared party bag we do not have. Recommend leave it out.

## Use Item
K2 uses the selected item on the character whose screen is open (a medpac heals them). Grenades and mines are not used from here in K2. They are thrown or set from the action menu.
What counts as usable in our rules today: medpacs, adrenals, shield generators, grenades (charges), mines, rockets. Today none is used from this screen: the button says "not built yet" and the board's keys spend them.
| Item | How it is spent today (board keys) | Status / recommendation |
|---|---|---|
| Medpac | `t` Treat (the Medicine action, on a hurt ally, costs the Action, refused outside a fight) spends one. **The rules' other use, a medpac as Gear on yourself or an ally (ACTION-ECONOMY-01 §3, one Gear per round), is not built**: the Gear key only works shields | **RULE:** recommend Use Item is that Gear use, on the character whose Inventory is open: free outside a fight (as K2), one Gear inside it. Treat stays as it is |
| Adrenal | no key spends it at all (the rules make it Gear) | **RULE:** recommend the same as the medpac |
| Shield generator | `g` Gear: costs Gear | YES: Use Item does the same |
| Grenade, rocket, mine | thrown with `o` (costs the Action today; the rules call it an Attack) or set as a mine (no cost today; the rules say an Action) | **CANNOT from here, as K2:** Use Item stays dim for them (they need a target or a square) |
| Use Item with nothing usable selected | dim | YES (K2 draws it dim) |

## The description pane (K2's Examine)
K2 shows what the item needs and does: "Feats Required: Weapon Proficiency - Lightsaber", "Damage: Energy, 2-20", "Critical Threat: 19-20,x2", then the flavour text. There is no separate Examine button. The pane is the examine.
**MEANS:** K2's pane and layout, filled with OUR rules' numbers (our damage dice, our requirements), which differ from K2's. Recommend yes.

## Credits
K2: "Credits" (string 5766) and the amount, under the description. Ours: the same, folded from everything bought and sold (`PT-2566`).
**YES.** One difference: with no purse ever recorded ours shows "—" (`PT-2491`: no purse is not a purse of zero) where K2 always has a number. Recommend keep `PT-2491`.

## Options that touch this screen
Hide Unequippable: K2's own help text says it applies to the EQUIP screen only. **Ours already does the same:** the Inventory ignores it.

## Waits on the owner's Telos save (Force back, Kreia and T3-M4 in the party, a stack)
- ~~**Stacks** and how K2 shows a count.~~ Built from an existing capture (see the table).
- **Party switching** in the footer (K2's arrows) and whose inventory is shown.
- **A droid's inventory** (T3-M4).
Built the moment the save arrives.

## The owner's short list
1. Keycards (items that open doors) under Quests? (recommend yes)
2. Leave worn items out of the list, as K2? (recommend yes)
3. Empty tabs blank, as K2, instead of our sentence? (recommend yes)
4. Use Item for medpacs and adrenals: the rules' Gear use, on the character whose Inventory is open, free outside a fight and one Gear inside it? (recommend yes)
5. Leave out the first-open help box? (recommend yes; follows the Tutorial Popups ruling)
6. Keep "—" for no purse? (recommend yes)
