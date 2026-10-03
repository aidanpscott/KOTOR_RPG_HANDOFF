# TEST 150

Written for: Main (to rule) and Coder. Re-check of what landed since TEST 149. **Equip's look was not judged.** Screenshots: `HANDOFF/BUILD/screens/test-150/` (paths relative to it).

## Build

- App `KOTOR-RPG-APP` `origin/main` = `5081698787dd01f06c06001d92f6b3fdaab9f555`. Lock Lodestar `df81340ec1278f1dd4ab0192969070a3667cda90` = `~/.pub-cache/git/Lodestar-df81340…` (present). **Lodestar `main` is `2db6df6`, one commit past the lock** — PT-2727 item 1 (off-hand half Strength), out of scope here — so this build does **not** contain that change. Lens `2bad745`. Shelf `92e305b`, MAIN_WORK `d53982e5`.
- Fresh `git archive origin/main` → `/tmp/test150-build`, `flutter build linux --debug`, no `flutter create`. `check_shelf.py` against **my** directory: `✓ 30 rules files and 105 standard blueprints, all identical`. Own Xvfb `:2` (PID 420560) and app, both stopped by PID at the end. Real K2 not launched. Equip-loop saves were authored with the app's own `tool/author_pt2721_equip_save.dart` (Onjo Trigit, Jedi Sentinel 1, endar-spire) into my directory only.

## Verdict

Nothing severe. Two behaviours need a ruling and one is a plain defect.
1. **Menus (item 1): CONFIRMED for Character, Inventory and Equip in four states.** No status line, party column, turn order, fight HUD, area name or hint line on any; Character and Inventory are pixel-identical across clean play, a dialogue open, and a fight; Equip is identical except a pulsing nav icon. **Two things still show the play view:** the **Abilities** screen draws the map straight through itself, and the **defeat panel** is drawn over a half-visible Options menu.
2. **Droid shield (item 2): FAILED, cause not shown.** Both shields bought and in the bag. **No slot list ever offers either** — the droid's belt list, its arm lists, every other droid cell, and the organic's slots.
3. **Worn gear (item 3): PARTIAL.** The sheet and Equip's readout use worn Strength, Dexterity and Defence bonuses and drop back when the item is removed. **A real fight roll does not use the worn Dexterity/Defence**: the printed Defence line stayed at 17 while the sheet and Equip badge read 18.
4. **Controls (item 4): PARTIAL.** Wrap, Enter, double-click, Escape order and one-white-row all work. **The arrow keys still move the character on the map while Equip is open** (4,3 → 2,3).

## 1. Menus take the whole frame — CONFIRMED (two spill-overs listed)

Four states captured for Character, Inventory and Equip, each shot after the screen settled:

| state | evidence |
|---|---|
| status message pending (the *"walk into them to act…"* line was showing before the menu opened) | `10-…`, `11-…`, `12-…`, `13-…` |
| clean play, no message | `14-…`, `15-…`, `16-…` |
| a dialogue open | `17-…`, `18-…`, `19-…` |
| in a fight | `20-…`, `21-…`, `22-…` |

Nothing from the play view is drawn on any of them: no left party column or turn order, no status or HP line, no fight legend or Defence line or hotkey line, no area name, no hint line. **Pixel comparison** (`compare -metric AE -fuzz 2%`): Character, clean vs dialogue vs fight: **0 / 0 / 0** differing pixels. Inventory: **0 / 0 / 0**. Equip clean vs dialogue: **0**; Equip dialogue vs fight: **0**; Equip clean vs fight: **1,783**, all inside a 57×56 patch at (994,112) — the Inventory nav icon, which **pulses in brightness over time** on that screen (six shots of one fixed state differ by ~2,000 px from each other, `23-…`), so this is the pulse, not a fight-state layout difference. The status-pending set was taken on a different character, so I compared it only against the clean droid-session shots: Character 0 differing, Equip 1,927 (the same patch), Inventory 3,872 (not located; likely the credits row, same icon pulse — *not shown*).

**Still showing the play view:**
- **The Abilities screen** (nav icon 4) draws the **map and its tokens straight through the Skills list** (`24-…`). It is not one of the three you named, but it is reachable by one misclick from the same bar.
- **The defeat panel** after a wipe is drawn over a dimmed **Options** menu left open behind it (`25-…`), where TEST 148's panel sat on the play view.
- **Equip prints its refusals inside the item list box**, in red capitals over the bottom rows: *"equipping is refused in combat — change your gear before or after the fight"* (`26-…`). It is real text, not the old status-line spill, but it is drawn on top of list rows.

## 2. Droid-only items, in play — FAILED (cause not shown)

`droid-shield-bed` loaded from the library as a package; built **T3-18** (Droid · Astromech · T3-series · Engineer, 28 skill points, Self-Diagnostic) and bought from its stall.
- **Purchase CONFIRMED.** Stall lists *Droid Deflector Mark I* (200 cr, in stock 2) and *Telos Mining Shield* (100 cr, in stock 2) (`30-…`, `31-…`, `32-…`), described "this item carries no description". Starting credits 100; selling one Computer Spike (its row read *Item Cost 250*; credits went 100 → 350, `33-…`) paid for both: 350 → 150 → 50 (`34-…`). Inventory lists `droid-deflector` and `forearm-shield` as raw ids (`35-…`).
- **Neither shield is offered in any slot.** On the droid I opened **every one of the twelve lattice cells** (head, both shoulders, implant, both arm cells, hands, belt, boots, weapon R, weapon L) from the slot view and read the list each time: **only "None"** appears in every non-weapon cell, with "nothing equipped in this slot" (`36-…` belt cell with the BELT header, `37-…` all twelve, `38-…` arm). The Ion Blaster alone appears under the weapon cells. So **the droid's belt list does not offer the Droid Deflector**, and **no arm list offers the Telos Mining Shield**.
- **The organic half could not be completed.** I did not build the organic character after this result, so "the organic's lists never offer the droid shield" is **not shown**, and the second half of the order ("try equipping each on the wrong body") **COULD NOT TEST**: there is no way to attempt it when the right body's own list is empty. An earlier-session check (TEST 149) showed an organic's arm list with only "None" as well, with no shield in the bag.
- *Likely cause, not shown:* shield items made from the fixture's `shield-generator` base with a catalogue id are not mapped to a wearable slot; I read none of that code.

## 3. Worn gear reaches the numbers — PARTIAL

Onjo Trigit (base STR 14 DEX 14, Sentinel 1). **Dominator Gauntlets** (description: "Strength: +5").

| reader | gauntlets worn | gauntlets off (None → OK) | back on (Enter) |
|---|---|---|---|
| Character Sheet STR | **19 (+4)** (`40-…`) | **14 (+2)** (`43-…`) | not re-read |
| Equip readout (lightsaber, melee) | **6-16 / +0 ; 6-20 / +0** (`41-…`) | **4-14 / −2 ; 4-18 / −2** (`44-…`) | **6-16 / +0 ; 6-20 / +0** (`51-…`) |
| a real roll | `Lightsaber · rolled 9 — d20 7 + attack 0 + **Strength 4** − dual-wield 4 + closed on a ranged weapon 2 · needed 10` (`42-…`) | not rolled | — |

So **Strength reaches all three, and drops back** on the sheet and Equip. The real-roll term is the **worn** Strength (+4 = (19−10)/2), as wanted; I did not repeat the roll with the gauntlets off, so the roll-side drop-back is **not shown**. The Equip readout also showed a half-Strength term on the off-hand (PT-2727), not tested.

**Frozian Scout Belt** (description: "Defense Bonus: 1 · Skills: Stealth +3 · Dexterity: +3", `45-…`), equipped out of combat on a freshly authored save:
- **Sheet:** DEX **14 → 17 (+3)**; Reflex **+4 → +5**; Fortitude, Will unchanged (`46-…`). The Defence row reads "—" with a red line *"`Mental Boost Package` needs `cybernetic_implantation` or …"* (the same gear mis-gate I saw in the sheet before wearing anything, `40-…`).
- **Equip:** the DEF badge **17 → 18** (`47-…`).
- **A real roll does not include it. FAILED.** The same character's fight prints `defence base 10 + Dexterity 2 + armour 3 + class 2 = 17` (`48-…`) **with the belt on**, and an enemy rifle shot printed *"needed 17"* (`49-…`). The roll uses base Dexterity (+2), not the worn +3, and no +1 Defence. So the sheet and Equip show **18** and the engine rolls against **17**.
- I did not test a worn **skill** bonus (Stealth +3) or a worn **save** (Cardio-Regulator Fortitude +2, Adrenaline Amplifier Reflex +2, descriptions read in `45-…`) in a printed check, so those two kinds are **COULD NOT TEST** as asked ("a save, or a skill check's printed line"): no check that rolls them was reachable in the time I had. The belt's Reflex +5 on the sheet is the DEX modifier, not the item's own save line.
- Cause not shown. Taking the belt off was not tested for the last two readers.

## 4. The equip controls — PARTIAL

Hands slot, six rows; screenshots wait ~2 s after each key because the screen repaints one press late (a shot taken straight after a key shows the previous state; I noticed this on the first try and re-took every shot).
- **Up/Down wrap — CONFIRMED.** From "None", Up lands on the last row (Taris Survival Gloves), Down from there lands on "None" (`50-…`).
- **Enter equips — CONFIRMED.** Enter on Dominator Gauntlets equips it immediately and the readout moves (`51-…`; status "you equip Dominator Gauntlets"). Pick mode ends and the slot view shows.
- **Double-click equips — CONFIRMED.** Double-click on Insulated Gloves equips it ("you equip Insulated Gloves"); the screen then **stays on the slot view** (list open, not closed): the work order said "equips and closes". PARTIAL against that wording. (`52-…`)
- **Escape steps back — CONFIRMED.** From the item list: Escape → slot view with Close/…; Escape → closed (play view); third Escape → Options (`53-…`).
- **Only one white row — CONFIRMED.** With a row keyboard-selected, moving the mouse over another row made the hovered row the white one and the keyboard row lose its highlight (`55-…`, last row alone white).
- **The arrow keys never move the character — FAILED, cause shown.** Clean test from a freshly authored save: the character stood at **(4,3)** (status `a01-command-deck · 4, 3`, `54-…`); I opened Equip, clicked the hands cell (item list open, `55-…`), pressed **Left, Left, Up**, closed Equip with Escape ×2; the character stood at **(2,3)** (`56-…`). The two Lefts moved it two squares; the Up did not move it (no square above was free or it went to the list — not shown). An earlier, less clean run showed the same one-square shift and is not cited.

## Seen, not in the order

- The sheet's Defence row reads "—" with the red `Mental Boost Package needs cybernetic_implantation…` line for Onjo (an implant gate); the fight line and Equip badge show 17 for the same character.
- Inventory is still raw ids (`dominator-gauntlets ×2 (Equipped)`, `light-combat-suit ×2`, `lightsaber ×2`, `droid-deflector`): in scope of PT-2723, not tested.
- Dialogue "Stand aside." and walking into an NPC both start a fight; "Persuade/Lie/Bribe" options were not tried.
- A stray click on a different bar than I expected moved my character three times during this session; the menu bar's icon x-positions differ between screens (Equip's bar is drawn larger than the others), which is why a blind click lands on a neighbour icon. A fixed set per screen is in `TESTER-STATE.md`.

## What I did not check

The organic character and the wrong-body equip attempts (item 2); a worn skill or save in a printed roll; Defence/Dexterity drop-back after taking the belt off; PT-2727's off-hand half Strength, trained-only skills, Inventory raw ids (told not to); Equip's look.

## Method notes

My slips, each caught before the numbers above: screenshots taken immediately after a key show the **previous** frame — I re-took every control test after settling; a blind key loop ("Right, space ×N") twice ended my own fight and killed the Jedi, and once opened Options; a click on the Equip bar's Abilities icon (the bar's icons sit at different x on that screen) twice took me to the wrong screen; and the first arrow-key run was contaminated by stray clicks, so I re-ran it clean and cite only the clean one.

Skills used: `verification-before-completion` (every CONFIRMED has a screenshot path or a printed line; causes labelled "shown" only for the arrow keys; the roll side of the worn belt and the droid-shield list are behaviours, causes not shown); `diagnosing-bugs` (one fixed state per comparison; the pulse isolated by six shots of one state); `research` (read the fixture's package, store, items and the item descriptions before judging); `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
