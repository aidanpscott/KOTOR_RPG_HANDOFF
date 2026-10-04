# TEST 152

Written for: Main and Coder. Screenshots: `HANDOFF/BUILD/screens/test-152/`. Real game only (clicks and keys). Equip's look not judged.

## Build

App `origin/main` = `80ac35c8f510f8eb3f8770e21447b0ec1e1a416b` (= the "Equip ready" hash; `git merge-base --is-ancestor 80ac35c HEAD` true). Lock Lodestar `1f12d12a778b1a8bc149e77ce073bb962a741a9d` = pub-cache checkout (Lodestar `main` is `a7161a2`, past the lock, not in this build). Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `f418e3f6`. Fresh `git archive` → `/tmp/test152-build`, no `flutter create`. `check_shelf` (my dir): 30 rules files, 105 blueprints, identical. Own Xvfb `:2`, stopped by PID. Real K2 not launched.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Refusal messages in Equip | **PASS for what I could trigger** (K2 box over the list; our combat notice clear of the list). Wrong-wearer and bad-pairing refusals **could not be triggered** (see below). Implant requirement not triggered. |
| 2 | Defeat panel | **PASS** (Options just closed). The "Options left open" variant **COULD NOT TEST**. |
| 3 | Store can't be overspent | **PASS** |
| 4 | Regression | **PASS** (double-click; arrow keys 3 of 3) |

## 1. Refusal messages — PASS (partial coverage)

- **K2's "can't use" box, requirement not met (armour proficiency).** Onjo Trigit (Jedi Sentinel; light armour proficiency): body slot → Jamoh Hogra's Battle Armor (medium; the row carries K2's red outline) → Enter. The box *"You cannot equip this item. You don't have the prerequisites. Please see the item description."* appears **over the list**, as in K2, and the item pane shows *Feats Required: Armor Proficiency - Medium* (`t1a`, `t1a2`). Expected; not failed.
- **Our own notice, combat.** In a fight (Sith Trooper): Equip → belt cell → Frozian Scout Belt → Enter. The notice *"equipping is refused in combat — change your gear before or after the fight"* is a red K2-style box over the **right side** (x ≈ 1010–1705, over the lattice and DEF badge), **entirely clear of the item list** (list box ends at x ≈ 935). No red text inside the list (`t1b`). (TEST 150/151: it was inside the list.)
- **Wrong wearer, both ways: COULD NOT TEST.** The slot lists never *offer* a droid item to an organic or the reverse (TEST 151, 3a–3c), so there is nothing to attempt to equip and no refusal to show.
- **Bad pairing: not triggered.** Blaster Pistol: Null in the right hand with a lightsaber off-hand equipped with no refusal at all; the readout simply changed to "Empty Hand 3-10 / −2" (`t1x`). I found no pairing in the fixtures that the game refuses.
- **Implant requirement: not triggered.** I did not try the Mental Boost Package (already worn by Onjo's save and flagged on the sheet), so no implant refusal was seen.
- Observation: my first attempts to catch transient boxes failed because Equip repaints one key late; I now sample frames ~1–2 s after Enter.

## 2. The defeat panel — PASS (one variant not tested)

Options opened then closed with its CLOSE button; fought the Sith Trooper (Onjo, Defence 21 after I equipped Reinforced Fiber Armor) until the party fell. The defeat panel — *"Your entire party has been killed…"* with *Go to Load Game List* / *Main Menu* — is drawn over the **dimmed play view** only. **No half-drawn Options menu behind it** (`t2`). The panel itself is opaque; the dimmed play view (party card, map) is visible *around* it as the backdrop, as in TEST 148. I read "nothing should show through it" as the panel, not the dimming; Main can say if the dimmed backdrop should be solid black.
- **COULD NOT TEST:** losing with the Options menu still *open*. With a menu open, no key reaches the turn end, so the fight cannot proceed to a wipe (and my key presses did nothing while the menu stood). 
- **Side finding:** after clicking Options → **CLOSE with the mouse**, keyboard input is dead until a click lands on the map (125 `space` presses did nothing; one map click and the next `space` worked). Closing with Escape does not do this (TEST 151 runs).

## 3. The store can't be overspent — PASS

Oreth Kesh (organic Human Soldier), `droid-shield-bed` stall (Droid Deflector 200 cr, Telos Mining Shield 100 cr).

| step | what I did | credits before | credits after | result |
|---|---|---|---|---|
| 1 | select Droid Deflector (200), Buy | 100 | **100** | popup *"You do not have enough credits to purchase this item."* (`t3a`); In Inventory 0 |
| 2 | select Telos (100), **fast double-click** on Buy (40 ms apart) | 100 | **0** | one bought: In Inventory **1** (`t3b`, `t3b2`) |
| 3 | sell three items (the rows were worth 50, 40 and 100; the 100 one was the Telos I had just bought, as the list shifts after each sale) | 0 | 50 → 90 → 190 | (`t3e`) |
| 4 | Telos, Buy (In Inventory 0 → 1) | 190 | **90** | one bought |
| 5 | Telos, Buy at 90 | 90 | **90** | the exact refusal message again (`t3c`), In Inventory 1 |
| 6 | **triple-click** Buy on Telos at 90 | 90 | **90** | Inventory stayed 1 (`t3d`) |

Credits never went below 0 (minimum seen 0). The exact text matches the order. (TEST 151: credits −200.)

## 4. Quick regression — PASS

- **Double-click equips and stays on the slot view:** Insulated Gloves equipped (readout 2-12/−3 → "you equip Insulated Gloves"); the Equip screen stayed on the slot view with the list and the **Close** button (`t4a`).
- **Arrow keys don't move the character behind Equip's item list, three tries:** with the hands item list open, 38 keys (Left×1, Right×3, a×7, d×12, Up×1, Down×3, w×7, s×12); Escape out; the play view differs from before by **0 px in 3 of 3 tries** (`t4b`).

## What I did not check

Wrong-wearer refusals; implant requirement; losing with Options open; a refusal for a feat-gated *weapon*; Equip's look.

Skills used: `verification-before-completion` (every PASS has a screenshot or a credits reading; unrun checks listed), `diagnosing-bugs` (a controlled credits ladder; a diff per arrow-key try), `research` (read the store fixture and prior reports first), `writing-for-agents`.
