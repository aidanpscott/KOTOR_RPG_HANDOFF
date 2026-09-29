# TEST 144 — PT-2708 holds in real play; one class grant still never reaches the player

## Build

```
app main                b34f45b  "The turn order says names; level-up Skills and Feats state the
                        level's own arithmetic -- PT-2708 (10)"
snapshot                `git archive HEAD` → ~/tester-build144 (+ `flutter create --platforms=linux .`)
pubspec.lock resolves   lodestar 7b6c97f5b70aa46cf2f7d89baeafca1f8d65df4f
                        lens     2bad745a53a1e741ab8d8ef94a954e6e3973b99b
pub-cache checkout      ~/.pub-cache/git/Lodestar-7b6c97f… rev-parse = 7b6c97f ✓ (= Lodestar origin/main)
                        pubspec.lock byte-identical after `pub get` ✓; no dependency_overrides
Shelf                   be87ee9, seeded by `git archive` into a FRESH XDG_DATA_HOME=~/tester-data144
display                 own Xvfb :2; app and Xvfb killed by recorded PID at the end
purse player            `XDG_DATA_HOME=~/tester-data144 dart run tool/author_tester_purse_save.dart`
                        → "Purser · level 4 · credits 500 · 2 vibroblades carried"
```

**Local-only fixture change (not on Shelf, committed nowhere).** In my copy of `tester-xp-bed`, room
`a01-room` gained a door at [5,1] to a new `a02-arena`. The arena holds one enemy, "Sparring Partner":
Soldier 1, `challenge = 1`, vitality 60. I needed it because item 2 asks for Mate's level **in combat**,
and the bed's only enemy is dead after the first kill. It also gave the dual-wield checks an enemy that
survives several rounds. It passed `validatePackage` clean.

## Verdict

**PT-2708 holds in real play on every item I could reach:**
- XP and companion levels, through three reloads, on the sheet, the sidebar and in combat.
- Equipping, the in-combat refusal and Switch Weapons' action cost.
- Dual-wield at −4, and the two-hander refusal.
- Skill checks with the key ability, and criticals multiplying the whole damage.
- Dismissal, granted/chosen marks, Store labels, the purse gates, and names in the turn order.

**One real FAILED, narrowed:** a **player** Brawler reaching level 2 never receives Unarmed Specialist I.
This happens on both Auto and manual Level Up, even though the manual summary names it. A companion's
level-up does write grants.

**Three partials:**
- Boots and Sparring Gloves never arrive. The save says why.
- The terminal opens and draws cleanly, but both kit spikes go on unlock attempts, so no terminal action
  was ever affordable.
- Persuade adds Charisma but not the homeworld's +2.

Nothing severe.

---

## 1. XP — CONFIRMED

`XP Brawler` (Brawler 1) and Mate killed the CR-9 dummy. The save logs 3000 each. On the sheets, the
player shows Experience **3000**, Needed 0, Level Up offered, and Mate shows **3000** (`04`, `05`). The
same numbers held after Leave Session → Load Game (`06`).

## 2. Companion levels — CONFIRMED (sheet, sidebar, combat)

Mate was levelled through the real flow (Soldier, Alertness +3, Cautious). The sidebar reads "Soldier · 2"
right away (`10`). After three reloads, each time the sheet reads "Soldier · level 2" with 3000 XP and
Level Up offered, which is correct because L3 costs 3000. The sidebar reads "Soldier · 2" (`11`, `12`).

**In combat:** walking through the local door into the arena, the fight panel shows "Mate · Soldier · 2 ·
60 of 60" (`13`). The player's record was unchanged across all three reloads.

## 3. Equipping — CONFIRMED (every slot that has an item)

- **Out of combat, free.** Checked on the Smuggler:
  - Short Sword → Config 1 off-hand: "you equip short-sword".
  - Body → None: "you take off clothing". Clothing back on: "you equip clothing".
  - Pistol → off-hand. It *moved* there and was not duplicated; the main hand fell back to unarmed
    (`22`, `23`).
  - Head, hands, arms, belt, implant and boots: **not checked**, because no class's inventory holds an
    item for them.
- **In combat, refused:** "equipping is refused in combat — change your gear before or after the fight".
  The clothing stayed on (`24`).
- **Switch Weapons in combat.**
  - 1st switch: "you switch weapons". The configurations traded places and the action pip stayed lit.
  - 2nd switch the same turn: "switching weapons — your second interaction this turn, so it cost your
    Action", and the action pip went grey (`26`, `27`).

Minor: each time Equip opens in combat it draws a little smaller.

## 4. Dual-wield with no feat — CONFIRMED, −4 on every attack

The Smuggler held a Blaster Pistol (main) and a Short Sword (off-hand); Smugglers get no Two-Weapon feat.
- **Equip readout:** main +2 → −2, off-hand −2 (`22`).
- **Real fight (`25`):**

```
Blaster Pistol · rolled 14 — d20 20 + attack 0 + Dexterity 2 − dual-wield 4 − point blank 4 · needed 9 … hit
off-hand: Short Sword · rolled 7 — d20 9 + attack 0 + Strength 2 − dual-wield 4 · needed 9 — miss
```

## 5. Pairing refusal — CONFIRMED

Soldier, Blaster Rifle in Config 1 main, Short Sword into Config 1 off-hand:

> **blaster-rifle takes both hands — it cannot be held with a second weapon**

The slot stays empty (`28`).

## 6. Starting inventory — MOSTLY CONFIRMED; boots and gloves never arrive

| class | arrived (save `item.acquired`, Inventory) | missing |
|---|---|---|
| Soldier | Blaster Rifle, Short Sword, Adrenal Strength, 2 Frag Grenades, 2 medpacs, the chosen 2 Advanced Medpacs, clothing | Dockworker's Treads |
| Engineer | Ion Blaster, **2 Computer Spikes**, 2 medpacs, 2 Advanced Medpacs, clothing | Dockworker's Treads |
| Brawler | Adrenal Strength, 2 medpacs, 2 Advanced Medpacs, clothing | **Sparring Gloves**, Dockworker's Treads |
| Smuggler | Blaster Pistol, Short Sword, Adrenal Alacrity, medpacs, Advanced Medpacs | Dockworker's Treads |

- **The save is honest about the gap:** `items_unresolved: "boots — Dockworker's Treads (a_boots_01): the
  catalogue gives it no base type, so no item can be made of it"`, and the same for `a_gloves_00`. The
  chargen Equipment step still lists both without saying so.
- **Second weapon:** it already sits in **Config 2's main hand** (Soldier's Short Sword and the Smuggler's
  Short Sword; `21`). Recorded, not judged, since placement is PT-2709.
- **Credits-route purchases:** not testable. The screen still says *"Neither is offered yet."*
- **Minor:** Inventory shows one row per item with no count. Two medpacs are one "medpac" row, and the sell
  list shows one Vibroblade row while "In Inventory 2".

## 7. Terminal — PARTLY CONFIRMED; no terminal action was ever affordable

`locked-and-trapped`: I noticed the mine ("15 against 12"), walked round it, and sliced the locked console
(15).

| character | attempt 1 | attempt 2 | result |
|---|---|---|---|
| Spike Engineer | d20 8 + Slicing 4 + Int 1 = 13 vs 15 · it holds | d20 16 + 4 + 1 = 21 · in | terminal opens with 0 spikes |
| Sharp Engineer (INT 16) | d20 5 + 4 + 3 = 12 · it holds | — | — |

- **Every unlock attempt spends a spike.** The save logs `item.lost computer-spike` per attempt. The kit
  holds 2, so after one failed unlock and one success, the panel offers "Unseal the vault door (2 spikes) ⚠
  you have 0 spikes" and "Cycle the corridor lights (1 spike) ⚠ you have 0 spikes".
- A real terminal action could not be performed. Clicking an unaffordable option closed the panel without
  a message.
- **The panel itself is clean** (`33`): the frames draw outward, nothing is inside out, and no readout is
  struck through (Slicing 5, Spikes 0, Repair 1, Parts 0).
- **Question for Main:** should a failed unlock cost a spike? With a 2-spike kit, one bad roll leaves the
  terminal unusable, and the Shelf offers no other spike source.

## 8. Skill checks add the key ability — CONFIRMED; one bonus missing

- **Examine:** "d20 5 + Science 4 + **Intelligence 1** = 10" (`30`).
- **Slicing:** "+ Intelligence 1" or "+ Intelligence 3", matching each character's INT.
- **Persuade (Cha):** "⚠ Persuade failed — 6 needed 14 (d20 5 **+1 Charisma**)" (`29`). Charisma is
  there, **but** this Smuggler's origin granted *"Persuade +2"* (Taris, Upper City, shown on the hub), and
  it isn't in the roll. SKILLS-01 §10.0 says species and homeworld bonuses stack.

## 9. Critical damage — CONFIRMED (whole roll ×2); no confirmation roll today

- Unarmed: "damage 9 — 2d3 2+1 + Strength 3×2 × 2 critical" (`03`).
- Pistol: "damage 14 — 2d8 4+6 + Dexterity 2×2 × 2 critical".
- The Sith trooper's rifle: "damage 18 — 2d12 8+10 × 2 critical".
- **A natural 20 went straight to critical in every case. No confirmation roll happens today.**
- Note: the first d20 in most sessions was a 20, which will matter for PT-2709's seeds. That trooper crit
  killed my 8-HP Smuggler on its first shot (`40`).

## 10. Dismissal — CONFIRMED, including after reload

`Dismiss Brawler` chose Dismiss from party, then fought.
- **Fight:** Mate isn't in the turn order and stays a neutral "M" token (`19`).
- **XP:** the only award is to the player (`xp-awarded` 3000, subject "Dismiss Brawler").
- **After reload:** the party is the player alone, and Mate is still a neutral "M" (`20`).

## 11. Granted feats — sheet and summary CONFIRMED; the player's own L2 grant FAILED

- **Sheet:** a new "feats" block reads "Nothing In My Hands · granted", "Conditioning · chosen" (`04`).
- **Level-up summary:** it names grants. Mate: "feat — Squad Tactics, granted by Soldier", "feat — Both
  Hands, granted by Soldier" (the L1 backfill, `07`). Player Brawler L2: "**feat — Unarmed Specialist I,
  granted by Brawler**" (`15`).
- **FAILED, narrowed:** the player never actually receives Unarmed Specialist I.

  | path | save after level 2 | sheet feats | Equip unarmed | real fight |
  |---|---|---|---|---|
  | Auto Level Up (XP Brawler) | `levelled 2 brawler`, no `unarmed_specialist_i` | Nothing In My Hands, Conditioning | 4–6 +5 | "1d3 1 + Strength 3", "1d3 3 + Strength 3" |
  | Manual Level Up (Dismiss Brawler), summary promised it | `levelled 2`, `cautious (chosen, 2)`, no `unarmed_specialist_i` | + Cautious only | 4–6 +5 | — |

  Mate's own manual level-up did write grants (`squad_tactics` and `both_hands`, `source: granted`). So
  the grant step runs for a companion and not for the player. That's the same shape as the PT-2708 subject
  convention, though I haven't traced it in code.
- **TEST 142 5c** (Brawler L2 does 1d4 + STR) therefore still fails: 4–6 on Equip and 1d3 in the fight
  (`16`–`18`).

## 12. Store and Terminal frames — CONFIRMED, one misplaced fill

- **Store (`36`):** the footer reads "Close", "Buying/Selling Items", "Show Sell List/Show Buy List", and
  the frames draw outward.
- **The readout box** has a dark inset fill spanning the Credits and In Stock rows. Its top edge runs along
  the Credits line, so the value "600" sits on the edge (`37`). It isn't a line through the text, but it
  looks misplaced.
- **Terminal:** see §7 (`33`).

## 13. The purse — CONFIRMED, all three readers agree

- **Before, 500 cr:** "[Bribe · 400 credits] I can cover four hundred." is shown; the 600 reply is absent
  (`35`).
- **Sold one vibroblade:** the Store's Credits went 500 → 600 ("In Inventory 2" before).
- **After:** the 400 reply is still shown, "**[Bribe · 600 credits] I can cover six hundred.**" now
  appears, and Inventory reads CREDITS 600 (`38`, `39`).

## 14. Turn order and level-up text — CONFIRMED, three small leftovers

- **Turn order** shows names (Mate / XP Brawler / Veteran Dummy, `02`).
- **Level-up Skills** reads "3 from your class + 0 for Intelligence" (the ×4 is gone). Feats reads "A
  Soldier gains a feat at level 2."
- **Leftovers:**
  1. The initiative status line still says "Dismiss Brawler 7 · **dummy.room.02** 4".
  2. At level 2 the skill rows read "cap 4", where SKILLS-01's level + 3 would be 5 (`08`).
  3. The level-up Feats footer says "0 feats are granted" while the summary lists two (`09`).

## Other observations (unruled)

- After crossing a door, Mate is drawn as a small ringless red dot, like an enemy token.
- The attack footer's last line runs into the character name ("× 2XP Brawler").

## Not checked, named

- Head, hands, arms, belt, implant and boots slots (no items exist).
- Credits-route purchases (not offered).
- A performed terminal action (no spikes left).
- Anything on the PT-2709 list: start square, confirmation rolls, mine DCs, Config 2 placement as a rule,
  seeds, the companion sheet's empty abilities.

Screens: `BUILD/screens/test-144/01`–`40`.
