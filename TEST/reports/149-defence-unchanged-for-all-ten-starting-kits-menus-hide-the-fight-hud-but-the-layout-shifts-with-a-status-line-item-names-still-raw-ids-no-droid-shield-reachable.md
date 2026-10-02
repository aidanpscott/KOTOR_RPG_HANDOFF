# TEST 149

Written for: Main (to decide whether the armour change stays) and Coder. Short regression pass. Screenshots: `HANDOFF/BUILD/screens/test-149/`, paths below relative to it. **Equip's look was not judged.**

## Build

- App `KOTOR-RPG-APP` `origin/main` = `8049f16b26d17f3a4bb8e6ed06e7a9b99015af5b` (head subject: *PT-2725 pass 3: first feat only, class+Armor N defence, property lines, one droid/organic wearer filter*). Fresh `git archive` → `/tmp/test149-build`, `flutter build linux --debug`, no `flutter create`; window 1920×1080.
- Lock Lodestar `df81340ec1278f1dd4ab0192969070a3667cda90` = Lodestar HEAD = pub-cache checkout; Lens `2bad745`. Shelf `42ef20a` re-seeded; `check_shelf.py` against **my** directory: `✓ 30 rules files and 105 standard blueprints, all identical`. MAIN_WORK `612e5922`, HANDOFF `d3d8904` at clone.
- Own Xvfb `:2` (PID 215158), app PID 215162, stopped by PID at the end. My previous saves were moved to `~/.local/share/tester-data.old-148/` so this pass's list is clean. Real K2 not launched.

## Verdict

- **Item 2 (sent early): no class changed.** All ten starting kits in TEST 147's table read the same total and the same printed breakdown, sheet and fight line agreeing for each. No term moved.
- **Item 1: PARTIAL.** The fight HUD (move/action/gear legend, Defence line, hotkey line, HP summary) is gone under Character, Inventory and Equip. The layout is **not** identical in and out of a fight in one case I could narrow: it shifts by roughly 34 px whenever a bottom status line is present, in or out of a fight. The status line and the left turn-order/party column still show through.
- **Item 3: PARTIAL.** Item descriptions are clean (no "§", "PT-", "section:", ".2da"). **Inventory rows are still raw ids** on every row of two characters. A "§4a" authoring string is still on the **chargen** Equipment step.
- **Item 4: COULD NOT TEST** the positive case. No droid shield is reachable: nothing hands one out and nothing sells one. What I could show is that an organic's arm-slot list and a droid's arm-slot list both offer only "None".

## 1. Menus hide the play view — PARTIAL

Opened Character, Inventory and Equip from play (out of a fight), then mid-fight (Escape, then the icon). Pairs: `13/14/15-ooc-*` against `10/11/12-fight-no-status-*` and `16/17/18-fight-with-status-*`.

- **Gone from all three, in a fight (CONFIRMED):** the move / action / gear / reaction legend, the "defence base … = N" line, the hotkey line (`f powers · c scan …`), the HP summary line (`name: 8 of 8 · …`). Compare the same fight's screen with the menu closed (`21-soldier-fight-line-14.png`).
- **Equip (CONFIRMED hidden):** the Equip screen is full-screen and draws none of the play view in or out of a fight.
- **Still showing through:**
  - **The left column.** In a fight: "in this fight / turn order" with every combatant and a card per party member, enemy included (`10-…`, `11-…`, `16-…`). Out of a fight: "your party" and the cards (`13-…`, `14-…`). This is on Character and Inventory, not Equip.
  - **The last status line, on Character and Inventory** when one exists: `walk into them to act — choose an action first to aim at somebody` (`16-…`, `17-…`); and **on Equip it is drawn inside the item list box**, in red capitals at the bottom of the list (`18-fight-with-status-equip-text-in-list.png`).
- **Layout identical in and out of a fight? Not in every case (FAILED for that case).** With **no** status line under the menu, the fight and out-of-fight icon bars and panes sit at the same coordinates: Character and Inventory icon bar x≈1103–1653, y≈122 in both (`10/11` vs `13/14`; `compare -metric AE -fuzz 3%` on the pair: 44,294 differing pixels out of 2,073,600; I did not map where they are, and by eye the visible difference is the left column's contents). With a status line present, **everything shifts**: icon bar x≈1137–1660, y≈120 and the panes move too (`16-…` vs `10-…`; same for Options, `19-…`). So the layout follows whether a bottom status line exists, not whether a fight is on. *Cause not shown;* a bottom row that pushes the menu body up is the likely candidate.
- Equip's first open in a session had empty icon cells (`12-…`) and filled ones afterwards (`15-…`): a loading effect, not a layout difference. The 571,975-pixel diff between the two is that, not position.
- A helper note for the next reader: the icon-bar x coordinates in play are not fixed, so a fixed-position click can hit the wrong icon (it hit Abilities for me once).

## 2. Defence regression — CONFIRMED unchanged

Same builds as TEST 147 (Human, STR 14 DEX 18 CON 14 INT 10 WIS 8 CHA 8 unless noted), level 1, starting gear, each read on the Character Sheet and from the Defence line printed in one real fight. TEST 147's numbers beside today's:

| class (DEX) | starting body item | TEST 147 | TEST 149 (sheet / printed line) | moved |
|---|---|---|---|---|
| Soldier (18) | clothing | 14 | 14 / `base 10 + Dexterity 4 = 14` | none |
| Scout (18) | clothing | 14 | 14 / `base 10 + Dexterity 4 = 14` | none |
| Bounty Hunter (18) | clothing | 14 | 14 / `base 10 + Dexterity 4 = 14` | none |
| Medic (18) | clothing | 14 | 14 / `base 10 + Dexterity 4 = 14` | none |
| Smuggler (12) | clothing | 13 | 13 / `base 10 + Dexterity 1 + class 2 = 13` | none |
| Agent (8) | clothing | 11 | 11 / `base 10 + Dexterity -1 + class 2 = 11` | none |
| Brawler (18) | clothing | 16 | 16 / `base 10 + Dexterity 4 + class 2 = 16` | none |
| Jedi Sentinel (18) | Padawan Robe | 17 | 17 / `base 10 + Dexterity 4 + armour 1 + class 2 = 17` | none |
| Jedi Guardian (18) | Padawan Robe (see note) | 17 | 17 (sheet) | none |
| Jedi Consular (18) | Padawan Robe | 17 | 17 / `base 10 + Dexterity 4 + armour 1 + class 2 = 17` | none |

Evidence: `20-…`, `21-…`, `2x-<class>-fight-line.png` / `2x-<class>-sheet.png`, `22-starting-body-item-per-class-crop.png` (Equipment-step "armour" row for nine of the ten: seven read `clothing`, two `Padawan Robe`), `23-…`. The Consular's Equip badge also reads **17** (`15-ooc-equip.png`), so the third reader agrees. A droid Engineer's badge reads **11** (`44-…`).
**Honest limits:** the Guardian's value is from its **Character Sheet only**; the fight line for that character was not captured because a run of mine was disturbed, and I did not repeat it (the Sentinel and Consular fight lines carry the same `armour 1 + class 2`). The work order said 11 classes; its table has 10 distinct rows once the three Jedi are listed separately. Not checked: any armour other than clothing and the Padawan Robe; levels above 1; the classes outside the table.

## 3. Item names and descriptions — PARTIAL

- **Raw ids in Inventory (FAILED, every row):** Jedi Consular `robe-1 (Equipped)`, `training-lightsaber ×2 (Equipped)` (`30-…`); Soldier `adrenal-strength`, `blaster-rifle ×2 (Equipped)`, `clothing (Equipped)`, `frag-grenade ×2`, `medpac ×2`, `short-sword ×2 (Equipped)` (`31-…`). Note the `×2` on weapons that the kit grants once: not investigated.
- **Equip lists use names (CONFIRMED, one inconsistency):** the Soldier's weapon list reads `Blaster Rifle (Equipped)` / `Short Sword` / `None` (`35-…`); the Consular's body list reads `Robe 1 (Equipped)`, while the chargen Equipment step calls the same item `Padawan Robe` (`23-…`).
- **Descriptions (CONFIRMED clean):** six read, none contains "§", "PT-", "section:" or ".2da". `32-…`: Adrenal Strength ("Attribute Bonus: Strength +4 / Duration: 120 secs / A shot of this enhancer …"), Blaster Rifle ("Feats Required: Weapon Proficiency - Blaster Rifle / Damage: Energy, 1-12 / Critical Threat: 19-20"), Frag Grenade (stat lines + "Fragmentation grenades are very basic …"), Medpac ("A medpac contains essential equipment … heal 10 vitality points + WIS modifier + user's skill in Treat Injury"). `33-…`: Robe = "Feats Required: Jedi Defense / Defense Bonus: 1" with **no flavour paragraph**; `34-…`: Training Lightsaber = "Damage: Energy, 1-8 / Critical Threat: 19-20,x2", **no name line and no flavour text**.
- **"§" still present, on chargen (not Inventory/Equip):** the Equipment step shows `TAKES THE CLASS'S OWN melee UPGRADE FROM §4a — Soldier → Long Sword + Short Sword or a Double-Bladed Sword; Scout → …` on every class (`36-…`, `23-…`). Same string as TEST 147's finding (d). Other chargen oddities on the same screen: `Dockworker's Treads — the catalogue gives it no base type, so no item can be made of it` (Soldier; the Sentinel shows it as a normal boots line), `Training Lightsaber  yellow` (two spaces).
- "Neural-Band" was not seen in anything I opened.

## 4. Droid-only items — COULD NOT TEST (positive half)

Built a droid: Droid · Astromech · T3-series · Engineer (at least Soldier, Marksman, Brawler and Saboteur are greyed with "no droid takes this class — nine of eighteen are open to a chassis", `41-…`). The shelf has a `droid-shield` blueprint (`Shelf/base-rules/blueprints/items/droid/droid-shield.item`; rule `equipment.toml: slot = ["belt"]`, so a shield is belt-slot).
- **No way to obtain one:** the Engineer's standard gear is an Ion Blaster, 2 × Computer Spike, 2 Repair Kits, 100 credits, "empty by design — implant · head · hands · arms · belt" (`42-…`); Purchase Gear lists weapons only, scrolled to the end (`43-…`); no package fixture references `droid-shield`/`droid/droid` (grep of `Shelf`: nothing but the blueprint file and the rule). I did not edit data to make one appear.
- **What I could show:** the droid's arm slot in Equip lists only `None` and "nothing equipped in this slot" (`45-…`), and so does an organic Soldier's (`46-…`). That is consistent with the filter but proves neither direction. The droid's Equip screen shows the droid slot icons (head, shoulders, arms, belt) with DEF 11 (`44-…`). I tried the Soldier's belt slot as well, but the screenshot does not show which slot was open, so I am not claiming it.

## What I did not check

The Guardian's fight line; the positive droid-shield filter; any armour but clothing/robe; Equip's look; whether `×2` on single-grant weapons is a merged party count.

## Method notes

Four slips of mine, none reached the numbers above: the Escape key toggles the menu, so my first mid-fight pass closed it and the clicks moved the character (re-ran); the in-play icon-bar position moves with the status line, so a fixed click twice opened Abilities; a stray extra click disturbed the Guardian's run; and I read a list header as the wrong character once (checked against the screenshot each time).

Skills used: `verification-before-completion` (every CONFIRMED has a screenshot path or a printed line; the Guardian gap is stated); `research` (read the `droid-shield` blueprint and rule before calling the droid case untestable); `diagnosing-bugs` (two identical-condition screens, with and without the status line, to narrow the layout shift to the status line); `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
