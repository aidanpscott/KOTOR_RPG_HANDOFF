# TEST 151

Written for: Main and Coder. Re-run of TEST 150's failures against the PT-2728 fixes, plus modded saves. Screenshots: `HANDOFF/BUILD/screens/test-151/`. Everything was driven with real clicks and keys; the only non-game step was authoring save files for item 7 (and Onjo's equip-loop save with the app's own tool).

## Build

App `origin/main` = `4bc67ad1f08ec9730296c0b98bb3ba5d7c20843f`. Lock Lodestar `1f12d12a778b1a8bc149e77ce073bb962a741a9d` = Lodestar HEAD = pub-cache checkout. Lens `2bad745`, Shelf `ce4e50a`, MAIN_WORK `11940bf8`. Fresh `git archive` → `/tmp/test151-build`, no `flutter create`. `check_shelf` against my directory: 30 rules files, 105 blueprints, identical. Own Xvfb `:2`; app and Xvfb stopped by PID. Real K2 not launched.

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Fight reads worn gear | **PASS** |
| 2 | No key reaches the map behind a menu | **PASS** (10 of 10 item-list runs, 0 leaks) |
| 3 | Shields | **PASS** (a side finding on credits below) |
| 4 | Spills | **FAIL** (refusal text still inside the item list); Abilities **PASS**; defeat panel **NOT RE-TESTED** |
| 5 | Sheet Defence | **PASS** |
| 6 | Double-click | **NOT RE-RUN** (ran out of session; owner already confirmed the behaviour) |
| 7 | Modded saves | **PASS** (one caveat on how my own edit first failed) |

This session also lost about eight hours: a long background command sat unfinished while I read its stale screenshots. Nothing below was read from an unfinished run; where a run was contaminated (my own scripts, noted inline) I re-ran it.

## 1. The fight reads worn gear — PASS

Onjo Trigit (Jedi Sentinel 1, base STR 12 DEX 14, authored with the app's tool; the Mental Boost Package refusal is present). Frozian Scout Belt (Defense +1, Dexterity +3) and Dominator Gauntlets (Strength +5) worn.
- **Belt on:** sheet DEX 17 (+3), Defence 18 (`01a`); Equip badge 18 (`01b`); fight line `defence base 10 + Dexterity 3 + armour 3 + class 2 = 18` (`01c`); the Sith Trooper's rifle shot printed `needed 18` (`01d`). All four agree. (TEST 150: sheet 18, fight 17.)
- **Gauntlets on:** sheet STR 17 (+3); attack line `Lightsaber · … + Strength 3 − dual-wield 4 …` (`01e`).
- **Both off (None → OK out of combat):** sheet STR 12 (+1), DEX 14, Defence 17 (`01g`); Equip badge 17 and readout 2-12 / −3 (`01f`); a new fight printed `Dexterity 2 … = 17`, the trooper `needed 17` (`01h`), and the attack line `Strength 1` (`01i`). Both dropped back.

## 2. No key reaches the map — PASS

Key sequence per run, with a distinct count for every key so no subset of leaks could cancel: Left×1, Right×3, a×7, d×12, Up×1, Down×3, w×7, s×12 (38 keys). Note `a`, `d`, `s` are game keys (aim, disengage, hide) per Options → Keyboard Shortcuts. **Control:** the same 38 keys in the plain play view change the screen by 6,712 px (`02c`), so the keys do act when no menu is open.
- All eight top-bar screens (Equip, Inventory, Character, Abilities, Party, Journal, Map, Options): play view before vs after = **0 differing px** each (`02a`).
- Equip slot view: 0 px. Equip description pane (a row selected): 0 px.
- **Equip item list, ten runs** (one fresh open, keys, close each; same fixed state): **0 differing px in 10 of 10**; zero slips. (`02b` shows one before/open/keys/after.)
- **Popup state:** the red refusal popup in combat was open when the keys were sent; Onjo stayed adjacent to the trooper and still had "5 move" (`04c`). The play view differs from before by 166,005 px, but that is a different status line and a layout shift, not a moved token — I judged by the token and the move count, not by the pixel count.
- A caveat on my own runs: two runs were contaminated by a script that stopped closing one Escape early (Equip's bar sits lower than the others); I discarded them and cite only the clean ones.

## 3. Shields — PASS

`droid-shield-bed`: a droid (Astromech, Engineer, 28 skill points) and an organic (Human Soldier), both bought both shields.
- **Droid, all twelve cells:** the **belt** list offers *Droid Deflector Mark I* (`03a`); **no other cell offers either shield**, including both arm cells (`03b`). The Ion Blaster appears only under weapons.
- **Organic, all twelve cells:** both **arm** cells offer *Telos Mining Shield*; **the belt list offers nothing** (None only); neither offers the Droid Deflector (`03c`).
- **Side finding (not asked):** the store let a 100-credit organic buy a 200 cr and a 100 cr item; credits read **−200** afterward (`03d`). The droid run had sold a Computer Spike first and stayed positive (50).

## 4. Spills — FAIL

- **Abilities: PASS.** It draws no map through it (`02a`, fourth panel).
- **Equip's red refusal text: FAIL.** In combat, Equip → belt cell → Enter still draws *"equipping is refused in combat — change your gear before or after the fight"* in red capitals **inside the item list box**, over the lower rows (`04c`). Same as TEST 150.
- **Defence panel over a half-drawn Options menu: NOT RE-TESTED.** I did not reach a defeat in this session, so TEST 150's finding stands unchecked.
- **The eight top-bar screens:** none showed play-view bleed in the post-key shots (`02a`).

## 5. The sheet's Defence — PASS

Onjo with the refused Mental Boost Package: the sheet shows **Defence 17** (`05`), matching the badge and the fight line. The refusal appears as a red line **below the saves**, ``Mental Boost Package` needs `cybernetic_implantation` …`, and does not replace a stat. (With the belt on, 18.) The line's backtick/identifier text is developer-style; noted, not a failure.

## 6. Double-click — NOT RE-RUN

I did not re-run it. The owner has already confirmed the intended behaviour; TEST 150 showed it equips and stays on the slot view.

## 7. Modded saves — PASS (with a note)

I edited a **copy** of my own Onjo save (never the owner's): the player's `character.ability-set` for STR 12 → 20, recompressed the body, and wrote it with the header's contents-length field (byte offset 90) updated to match.
- **Opens and plays.** It lists as **`[Modded] Onjo Trigit`** (`07c` — the tag is already built), opens straight into play with no warning popup (`07e`), and the sheet is in `07d`, and the sheet shows **STR 20 (+5)** with no banner.
- **My first edit failed, and that is informative.** With the old length field the save was accepted into the list but refused on opening: **"THIS SAVE WILL NOT OPEN — Damaged save: the contents could not be unpacked."** (`07a`). So a hand-edit that does not also fix the stored length is treated as damage; a modder who edits the log must update the length (or a tool must). Not necessarily a defect — worth Main knowing.
- **Truncated save** (first half of the file, 611 bytes): not listed as a save; the menu footer reads: **"3 saves · 1 unreadable: Damaged save: it says it holds 1123 bytes of contents and the file has 511. Part of another save may have been written over it."** (`07b`) — plain English, with the numbers.
- A second corrupt file (20 flipped bytes near the end) was counted among the readable saves until opened; I did not trace what the app then showed for it, so I make no claim about it.

## What I did not check

Item 6; the defeat panel spill; a worn skill or save bonus in a printed check; the organic-attempting-the-droid-shield "wrong body" refusal (the lists simply never offer it); the corrupt-by-bytes save's behaviour on open.

Skills used: `verification-before-completion` (each PASS has a screenshot; unrun checks listed), `diagnosing-bugs` (a control for the key test; a discriminating count per key), `research` (read Options → Keyboard Shortcuts before choosing the keys), `writing-for-agents`.
