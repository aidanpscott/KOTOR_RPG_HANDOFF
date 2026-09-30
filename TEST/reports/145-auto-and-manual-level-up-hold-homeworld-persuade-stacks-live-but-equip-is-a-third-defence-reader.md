# TEST 145 — Auto and manual Level Up both grant correctly; homeworld Persuade stacks live; the Hunter grant reproduces — but the Equip screen is a third "one fold, three readers" reader PT-2711 didn't reach

## Build

- App: local HEAD `383e68a3d620e817c3e910963e6278782b4ac9de`, matching `origin/main` exactly, clean tree, at catch-up. **Built from a `git archive` snapshot of that HEAD**, per the work order — not a live checkout.
- `pubspec.lock`: Lodestar resolves to `f3e70e3e21736987fd4d6673c52dc7bff0c05b37`, Lens to `2bad745a53a1e741ab8d8ef94a954e6e3973b99b`. Both exact checkouts exist in the pub-cache (`~/.pub-cache/git/Lodestar-f3e70e…`, `Lens-2bad745a…`) — this is what actually compiled.
- Shelf: `~/.local/share/tester-data/kotor-rpg/packages` was a stale git clone (`c9f64b6`) at session start. **Pulled to `267101d`** mid-session (fast-forward, clean) to pick up `tester-xp-bed-arena` (PT-2710 item 10) and the feat-id/availability regeneration (PT-2711 item 3) — both needed for this list. `check_shelf.py` clean before and after.
- Own Xvfb `:2`, own PID each launch, never touched Coder's display.

## Verdict

**One severe finding, not previously reported: the Equip screen's own Defence badge is a third reader that still omits the class bonus PT-2711 just added to the other two.** Confirmed three ways on the same character at the same moment — Character Sheet 14, a real fight's own defence breakdown 14, Equip screen **11** — and traced to the exact line: `play_screen.dart:3147` calls Lodestar's `defence()` for the Equip screen's `DEF` badge without passing `classBonus:`, so it silently defaults to 0. This is the same shape PT-2711 titled "one fold, three readers" and fixed for the Character Sheet; the Equip screen is the reader that fix didn't reach.

Everything else on the list held. In particular: **the Hunter grant now reproduces live** — Soldier + Hunter + Two-Weapon Fighting correctly resolves to Long Sword *and* Short Sword, one per hand; Hunter *alone* (no TWF) correctly resolves to a single Long Sword, which is the rule working as designed (`BOTH` in `STARTING-EQUIPMENT-01` means profession *and* the feat, not profession alone) rather than the regression I first suspected.

## Results

### 1. Player-granted feats — CONFIRMED

Built a Human Brawler (`Isolde Vos`) in `tester-xp-bed`, killed the fixture's 1-vitality enemy for the guaranteed 3000 XP, and used **Auto Level Up** on the Character Sheet. Result: level 2, feats list gained `Unarmed Specialist I — granted` (distinct from `chosen`). Equip screen's unarmed damage read `3-6 +4` (1d4 + Str 2), matching the L2 grant exactly (L1 had read `3-5 +3` on the same character, i.e. 1d3 + Str 2).

Built a second Brawler (`Rennik Tarn`) in `tester-xp-bed + Arena`, same 3000 XP kill, this time used **Level Up** (manual). The manual screen states the grant explicitly before you accept it: *"granted — vitality d10; attack and saves — from Brawler's own table; feat — Unarmed Specialist I, granted by Brawler."* Spent the 3 skill points and 1 chosen feat, accepted. Confirmed in a **real fight** against the arena's Sparring Partner: `unarmed · rolled 20 — d20 16 + attack 2 + Strength 2 · needed 9 — hit · damage 5 — 1d4 3 + Strength 2 · 55 left` — 1d4 + Str, live.

Soldier's own L1 grants (`squad_tactics`, `both_hands`) also read `granted` on the sheet, correctly distinguished from a chosen feat (`Armour Proficiency: Light — chosen`) on the same character — confirms the granted/chosen distinction is class-blind, not Brawler-specific.

**Not separately exercised:** a level-4 grant on a second class (e.g. Soldier's `improved_squad_tactics` at class level 4). Reaching level 4 needs more XP than one `tester-xp-bed` kill provides, and I judged the risk/time of grinding it not worth it once the mechanism was already confirmed class-blind via the L1 granted/chosen check above and via source (`grantedFeatsFor` is one function for every class). Flagging as unexercised rather than silently assuming it.

### 2. Seeds — COULD NOT TEST (only incidental data)

Not deliberately exercised. Incidentally, three separate `New Game` starts this session drew different first d20s (14, 1, 17 across Isolde Vos, Rennik Tarn, and Mira Sabek's first real rolls) — consistent with per-campaign seeding, but I never ran the actual paired check (same save reloaded vs. a fresh save from a later point in the same campaign) the item asks for.

### 3. Spikes (`SKILL-RESOLUTION-01 §5`) — COULD NOT TEST

Not exercised this session. None of the three characters built (Soldier ×2, Brawler ×2) carried a starting spike — the classes I happened to build don't get one in their array — and I didn't revisit `locked-and-trapped`.

### 4. Homeworld bonuses stack — CONFIRMED

Taris · Upper City · Persuade was visible as `+2` at the Origin step, correctly labelled `homeworld` (distinct from `class`) on the Skills step, and reached a **real dialogue check**: talking down the Command Deck's Sith Trooper produced `Persuade passed — 25 needed 14 (d20 17 +4 Persuade +2 Charisma +2 homeworld)`. All three terms present and separately labelled in the live roll breakdown.

### 5. The Credits route — COULD NOT TEST

Seen only in passing (the Equipment step's own text: *"You may also spend the value of this gear as credits instead, or take whatever your GM decides"*). Never selected it, never reached a Store, never confirmed a purchase arriving in Inventory.

### 6. A companion after a door — COULD NOT TEST (incidental data only)

Not deliberately exercised with the intended rigor. Incidentally, the henchman `Mate` crossed from `tester-xp-bed + Arena`'s `a01-room` into `a02-arena` with me, stayed listed in "your party" throughout, fought alongside me against the Sparring Partner, and was never attacked as if hostile nor did it attack the party — but I didn't specifically check its on-screen colour/rendering before and after the door, which is what "keeps its look" is really asking.

### 7. The skill cap at level 2+ — CONFIRMED

Level 1 Brawler: class skills read `1/rank · cap 4`. Same character after Auto/manual Level Up to level 2: `1/rank · cap 5` on the manual Level Up's own Skills step. Right value, right level.

### 8. Minor fixes — COULD NOT TEST

Not checked: Inventory stack counts, the Store inset, the initiative line's names, the level-up Feats footer count.

### 9. Boots and Sparring Gloves — CONFIRMED

Every Equipment step this session (Soldier ×2, Brawler ×2) showed `boots: Dockworker's Treads — the catalogue gives it no base type, so no item can be made of it`, dimmed like the rest of the unresolved-item text, never presented as if deliverable. Same pattern for `Sparring Gloves` in the Brawler's kit line. Consistent with a real, honestly-reported content gap rather than a UI bug.

### 10. The Hunter upgrade grant, live — CONFIRMED (closes PT-2688)

Built a Human Soldier (`Mira Sabek`), Taris origin, Hunter background, **Two-Weapon Fighting** as the level-1 feat. At Equipment, the melee-upgrade offer correctly expanded to two choices (`"and now you choose which"`, plural, only appears when `upgrades.length > 1`): **Long Sword + Short Sword** (`2 objects`) and **Double-Bladed Sword**. Picked the pair. Save log confirmed both weapons: `weapon_r_1: items/weapons/long-sword, weapon_l_1: items/weapons/short-sword`. Equip screen showed both in Config 1, one per hand. No `'upgrade' will not open` anywhere.

For comparison, built a second Soldier (`Rennik Tarn`, reused for item 1) with Hunter but **without** Two-Weapon Fighting: the offer correctly showed only **one** choice, a single Long Sword, with the note *"one weapon — wield 3, and it IS the pair."* This is correct per `STARTING-EQUIPMENT-01`'s own ruling (line ~575): `BOTH` means the profession grant **and** the Two-Weapon Fighting feat together; `Hunter` alone gives the class's single-weapon upgrade. My first read of this (before re-checking the source doc) was that the pair was missing — it isn't; the character just hadn't taken the feat the pair requires. Correcting myself here rather than filing it.

**Character Sheet, Equip, and a real fight do *not* show the same Defence** — see the severe finding above. Character Sheet 14, real fight 14, Equip 11, same Soldier, same moment.

### 11. From PT-2709 — PARTIAL

- **Start square:** confirmed. Endar Spire's Command Deck: the player's token renders exactly on the teal `aft`-labelled square on first frame, matching the package's declared `[[arrivals]] at = [1, 3]`. (Caveat below.)
- **Config 2:** confirmed for the second-weapon-in-main-hand shape, via item 10's dual-wield Equip screen — Config 1 showed `short-sword` in the **left** slot and `long-sword` in the **right (main)** slot.
- **Confirmation rolls, mine DCs, companion sheet:** not tested this session.

**Methodology note, not a defect:** clicking anywhere on the game floor — including a click meant only to give the window focus — registers as click-to-move and can silently relocate the player before you've looked. I did this to myself once (moved the player one square off `aft` by clicking to focus, which very nearly read as a start-square defect until I checked the save-writer's own status line and the arrival declaration directly). Recommend focusing via a UI element off the floor (sidebar, party panel) rather than the canvas when precision matters.

### 12. The arena fixture (`tester-xp-bed-arena`) — CONFIRMED, opens and plays

This package only reached `Shelf main` after my catch-up sync (pulled mid-session, see Build). Opened it, played the `a01-room` dummy kill for XP, walked through the door at the correct approximate position into `a02-arena` (once routed around the henchman, who blocked the direct path — expected, not a bug), and fought the Sparring Partner in real combat (see item 1's damage confirmation). Took the fight down to 3/18 HP through my own overextension, disengaged cleanly (`disengaging — your movement provokes nothing this turn`), and left the session safely. No defect in the retreat mechanism itself, once I read it correctly (`d` disengages before moving; movement toward an adjacent enemy square attacks rather than repositions).

## Severe, reported first

**The Equip screen's `DEF` badge omits the class Defence bonus.** `play_screen.dart:3147` calls Lodestar's `defence()` — the same function PT-2711 just added `classBonus` to — passing only `armourBonus`, `maxDex`, `dexterity`, `size`. No `classBonus:` argument, so it silently defaults to 0. Confirmed on `Mira Sabek` (Soldier, level 1, class bonus +3): Character Sheet `Defence: 14`, a real fight's own printed breakdown `defence base 10 + Dexterity 1 + class 3 = 14`, Equip screen `DEF 11` — same character, same moment, three readers, two agree. Confirmed the mechanism (not merely the symptom) by reading Lodestar's `defence.dart` directly: `classBonus` defaults to `0` and PT-2711's own comment names exactly this shape — *"one fold, three readers"* — for the Character-Sheet/fight pair it fixed. The Equip screen is the reader that fix didn't reach.
