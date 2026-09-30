# TEST 146

## Build

- App repo (`KOTOR-RPG-APP`) local HEAD: `6064913074921c01c60ad88891b7db80fbf84a25`
- `pubspec.lock` lodestar `resolved-ref`: `888d8ea9595a6c6f74517e448d80a6a5c9d9bf64`
- pub-cache checkout: `~/.pub-cache/git/Lodestar-888d8ea9595a6c6f74517e448d80a6a5c9d9bf64` — present, matches the lock
- Built from a fresh `git archive` of the app HEAD above into `/tmp/test146-build`, `flutter create --platforms=linux .`, `./scripts/run.sh debug`, own Xvfb `:2`. `check_shelf.py` run before writing this report: clean (30 rules files, 82 blueprints, all identical to the extracts).
- Data directory reinstalled from Shelf `main` before testing.
- Real KOTOR II was not launched.

## Verdict

PT-2712 item 1 and PT-2713 both hold. **The Defence three-screen split is fixed**: Character Sheet, Equip's DEF badge, and a real fight's printed breakdown now agree, confirmed for a Soldier and an Engineer, and again after an armour change was attempted (see item 1's own note on what could not be changed). **Auto Level Up's interim guard works exactly as specified.** Mine mechanics, spike accounting, and the Minor Frag Mine's set/disarm DCs are all confirmed correct. Two items could not be completed as asked: the companion sheet with real data (the one non-Dummy fight available grants nowhere near enough XP for a level, and the manual save door is explicitly unbuilt), and the full mine tier table (only the Minor tier is reachable anywhere this session). Nothing severe found.

## 1. Defence, three screens — CONFIRMED

Built a Soldier and separately an Engineer. For both, Character Sheet, Equip's DEF badge, and a real fight's printed Defence breakdown agreed at the moment of the check: 15 for the Soldier (`10 + Dexterity 2 + class 3`), 12 for the Engineer (no class bonus applies there). Re-checked after combat continued; no drift.

Could not change armour and re-check all three, as asked: no class starting kit includes non-`clothing` body armour (confirmed by grepping `starting_items.toml` for `items/armour/`), and no Store fixture reached this session stocked armour — Store Bed's own merchant sells only a Vibroblade and a Medpac, confirmed via its Armour filter tab returning nothing. Reporting as a fixture limitation, not a defect; the primary three-way match was already confirmed cleanly before this sub-step, on the figures above.

## 2. The ally ring after a door — CONFIRMED

Mate's teal ring persists across a01-room → a02-arena → back, both directions, in the `tester-xp-bed-arena` package. Screenshotted both sides of both crossings. The ring now also carries an "M" letter label inside it, an improvement over what TEST 145 saw.

## 3. The Credits route — CONFIRMED (2 of 2 classes checked)

Purchase Gear renders for a Soldier and, checked again this session, for an Engineer. A Soldier took the route, bought a weapon, and confirmed it landed in Inventory with a clean four-row Store inset. No class was found this session where the route renders disabled with a reason — only Soldier and Engineer were actually checked against this specific ask, so a third class showing a disabled-with-reason case remains unobserved, not ruled out.

## 4. Spikes and mines — CONFIRMED

Read `_disarm`/`_setMine` in `play_screen.dart` and confirmed in play: a failed disarm attempt is a pure retry — no event is written and no Security/Computer spike is spent, matching the source's own comment ("a failure IS a retry — nothing happens"). A failed *set* attempt likewise leaves the charge in the bag untouched. A successful set correctly consumes the mine item itself.

Traced an apparent "mine destroys spikes" pattern in a save log back to its real cause: it wasn't the mine. Built a clean control character (Bevin Ordo) who never sprung the mine (HP stayed 10/10 throughout, confirmed via the save's event log — no `hazard.sprung` event at all), then sliced the terminal directly. Spikes were still spent, immediately after `session.started`. The true cause is `_slice()`'s own upfront entry cost (`costFor(terminalGrade(dc), skillTotal: Slicing)`), spent *before* the terminal panel opens, by design — the source comment explicitly flags this as intentional, matching the old gate's spend-before-roll order. Not a defect; the original hypothesis (mine triggers spike loss) was wrong and was corrected before being reported.

Confirmed separately that slicing a terminal open costs no roll, only the upfront spike cost, and that the same spikes remain available to spend again on a second slice (i.e. the terminal's own cost is genuinely per-attempt, not confused with the mine's resources).

## 5. Mine tier numbers — PARTIAL

Only the Minor Frag Mine was obtainable anywhere this session (Saboteur's own starting array, or the "survivor" profession grant — no other source found). Confirmed:

- set DC 15 — matches
- disarm DC 17 — matches

Average/Strong/Deadly/Devastating tiers (set 20/25/…, disarm 22/27/…) were never reached — no purchasable or grantable source for any of them was found in any fixture checked this session. Recovering a mine (the 20/25/30 row) was also never reachable: the "Recover" option only appears to exist for hazards carrying an authored `recovers` field, which no player-set or package-authored mine tested this session had. COULD NOT TEST for every row past the Minor tier's own two values.

## 6. Auto Level Up's interim guard — CONFIRMED

On a level owing an unrecommendable choice, Auto refused to consume it, set `_said` to the expected "…opening Level Up" message, and opened the manual flow directly with the choice still unresolved. Backing out of the manual flow fully preserved the pending level — XP and Needed unchanged, both Auto and manual buttons still present. The manual flow itself completed the level cleanly. Exactly as specified; this is the interim rule only, full Auto still waits on recommendations per the order.

## 7. Leftovers from TEST 145

### 7a. The companion sheet with real data — COULD NOT TEST

Built a fresh Human Soldier (Isolde Ordo, STR14/DEX14/CON12/INT12/WIS16/CHA8) in `tester-xp-bed-arena`, specifically to avoid the Veteran Dummy as instructed. Confirmed the Dummy's identity directly via Examine (`Xenology` check literally names it "Veteran Dummy") before routing carefully around it — moved along the bottom row of a01-room, never entering its tile or attacking it, through the door into a02-arena instead.

Fought the Arena's Sparring Partner (Soldier·1, 60 vitality, CR 1) to the death in real multi-round combat, controlling both Isolde and Mate manually. The kill is confirmed clean in the save log (`character.died`, `character.xp-awarded` for both `Isolde Ordo` and `mate.room.01`, 125 XP each, `cr: 1.0`). Per-companion XP awarding itself is confirmed working correctly — Mate really did receive its own 125 XP, separate from the player's.

125 XP is far short of a level (the sheet shows 875 more needed from a fresh level 1). With only one non-Dummy enemy in this fixture and no respawn, there is no further XP available here without the Dummy. Confirmed directly, not just inferred from XP arithmetic: right-clicking Mate's own portrait while Mate was the active-controlled character opened the Equipment screen, not the Character Sheet — by `_openPortrait`'s own logic (`play_screen.dart`) this happens precisely when `_levelWaitingFor` is false, i.e. no level is pending. The Sheet itself was never reachable this session under the "avoid the Dummy" constraint.

Bonus, positive confirmation along the way: the portrait-tap control-switch mechanic (`PT-1134`/`PT-2524`/`PT-2599`) works as designed outside combat — tapping a non-active companion's sidebar portrait switches control to them ("you are now controlling Mate"), and tapping the same portrait again while already active routes to Equipment-or-Sheet based on the pending-level check. The mechanism is sound; it simply never had a pending level to show through it this session.

Reporting as COULD NOT TEST, not a defect: a content/fixture gap (no second real enemy, no respawn) under the specific constraint given, not a bug in the game.

### 7b. Seeds, same campaign — PARTIAL / COULD NOT TEST AS SPECIFIED

The in-game "Save Game" menu entry is explicitly unbuilt this build — its own description reads "not built yet — the save format and its list exist, this door into them does not." There is no way through the UI to branch one continuous campaign into two distinct save checkpoints to compare what rolls follow each, which is what this item asks for literally.

As a substitute check, read two on-disk `.sav` files directly (the underlying save mechanism itself does work and auto-writes, independent of the unbuilt manual-save menu item) and confirmed each independent campaign carries its own distinct seed: Isolde Ordo (`tester-xp-bed-arena`) — `1787635955`; a `locked-and-trapped` character from earlier this session — `1165136493`. This reinforces TEST 145's already-confirmed finding (seed variety across six fresh new-game rolls) via the stored seed itself rather than eyeballed d20 results, but it answers "different saves draw different rolls" for *different* campaigns, not the literal "same campaign, two saves" framing — which this build's save system currently has no path to construct.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
