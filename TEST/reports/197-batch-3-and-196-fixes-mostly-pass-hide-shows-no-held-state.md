# TEST 197: in-game batch 3 and the TEST 196 fixes

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-197/` (MAIN_WORK `ab43d5ea`). The step-by-step log is `TEST/reports/197-running-log.md`. Compared against `MAIN_WORK/media/study/pt2752/` and `rules/K2-PARITY-INGAME-BATCH3-PT2752.md`. The run was paused for MAIN's hold and resumed on the same build.

## Build

App `47fe0ea`, git archive from my own clone. `gate.py --at 47fe0ea`: "FOR TESTER — CORE at 47fe0ea, 5053 tests, 0 failed"; ARCHIVE last green at 47fe0ea. Lodestar `240bc46` = lock = compiled. Lens `5fe60a9`. Loom has no entry in the lock. Shelf `9706207`; check_shelf clean (33 rules files, 125 blueprints). The build (10.1 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Characters: Coder's "Gear Note" and "Saber Hand" (`author_tester_test197_saves.dart`, Endar Spire). Lang Two (authored Twi'lek, Store Bed). Made through chargen: Twi Seven (Twi'lek Soldier, Tester Bolt) and throwaway Scout and Smuggler (Endar Spire). Earlier fixtures: RX-196, Frame One, Watch Four, Dice One, Icon Nine.

## Summary: most pass; one finding

| # | Check | Result |
|---|---|---|
| 1 | Options | **PASS**, from the main menu and in play. Only real rows are drawn, closed up. The spinners go Ask → Never → Always with plus and back with minus. The check boxes toggle. Brightness darkens and lightens the whole screen. The lit row is pale. Every change was written at once and read back after a restart |
| 2 | Save/Load | **PASS**: no Cloud Save and no line under the title; New Slot with its empty bar; the name box is K2's popup. Save ("31 : sl197"), overwrite (K2's "Are you sure…" then saved, row time 17:43:46 → 17:44:07) and load each worked |
| 3 | Party Selection | **PASS** at the time: ring with portraits, white in-field ring, Cancel and Escape both discard, OK applies, Doctrine right of OK. Superseded by the owner's return to a scrolling list. Page arrows and a refused pick's reason weren't reached (one companion) |
| 4 | HUD | **PASS**: menu buttons top right. The party bottom right: Vela at 25/40 shows her red bar at 63% (25/40 = 62.5%). Six columns cycled by the arrows, each key on hover ("Rest (e)"), attacks box empty. The sidebar sits in the K2 pane. A board tap moves the player there; a tap on a creature gives the "walk into them to act" prompt. Force spending wasn't reached (Vela knows no powers). **Finding**: Hide shows no held state (below) |
| 5 | In a fight | **PASS**: the queue holds the budget and "Defense base 10 + Dexterity 3 + cover 5 = 18". END TURN in red in Cancel Combat's place ends the turn. The red message box carries the prompts and grows for an attack line. The log is only in Messages > Combat, under "Round 1/2/3". In a conversation the HUD hides and the box stays (its clipping is ruled for the letterbox retest) |
| 6 | Twi'lek | **PASS**, authored (Lang Two) and from chargen (Twi Seven): Species "Twi'lek"; Languages "Speak and read/write Ryl and Basic. Bonus language: Lekku (the head-tail language)." |
| 7 | Gear Note | **PASS**: Defense "—" on Stats. Character Info shows both red lines: "Defense: No Such Visor will not open: there is no item here." and "Mental Boost Package has no effect: it needs the Cybernetic Implantation, Advanced Cybernetic Implantation or Master Cybernetic Implantation feat." |
| 8 | Purchase Gear Armor | **PASS** for Soldier, Scout and Smuggler: Clothing only, Item Cost 0, no robes; Standard Gear lists Clothing first |
| 9 | Portrait edge | **PASS** at 1920 and 1280×720 (RX-196): the portrait meets the bar's ends. The bar's curve bows away by up to 36 px at its middle, which is the bar's shape. Light and Dark are whole |
| 10 | Small fixes | **PASS**: "Map — ⟨Market⟩"; the level-up hub shows RX-196's portrait; "0 (replaces Blaster Rifle)" (and "0 (You cannot use this item.)" for a droid) |
| 11 | Saber Hand | **PASS**: with the saber equipped, Forms > Determination ("Lightsaber Form") opens with "Current stance". After unequipping (damage 3–17 → 2–4) the line is gone. The form's name is in the header, not "Current stance: Form I" |
| 12 | Dice, regression | **PASS**: from Dice One's Quick Save, rounds 1–3 in Messages > Combat match TEST 185 line for line, with the same initiative (19, 13, 11, 10, 2). Regression: Escape > Save (slot 32, "reg197"), Escape then F4 (one quick save), Load, and a fight to its end (total party defeat box) |

## Finding

1. **Hide never shows a held state.** Watch Four (Stealth 8) pressed Hide on her turn: "hidden — 17 beat 9", and her card reads "hidden". The toggle then went **dim** instead of pressed. `k2_hud.dart:212` draws it held (`isDefault: hidden`) only while it's also enabled (`refusal == null`), and once the action is spent it's refused, so the held look can't appear. (Switch Weapons has no held state either; it's listed below.)

## Small

- The Doctrine chooser survives Escape: Party Selection closes and the chooser floats over play, and over Options after another Escape. Only a click outside closes it.
- A stale "V" token: after removing Vela with OK and adding her back, she's drawn twice (her party disc beside me and the "V" where she stood) until the party moves.
- Switch Weapons works mid-fight ("you switch weapons") but shows no pressed state.
- The queue's two lines run across its red arrow and oval rather than inside them.
- After End Turn passed to Twi Seven, the box still read "Vela is waiting on you" until the next prompt.
- "A fight begins." appears five times at the top of the Combat tab.
- Column 2's hover box ("Use the Force (f)") is clipped at the screen's left edge.
- A species id: species.toml's `id = "twi-lek"` is refused at load ("…a species this package does not have: "twi-lek""). The app keys species by lower-cased name (`main.dart:244`), so a save must say "twi'lek". Chargen writes the right one; only authored saves are affected.
- Process note: my dice script read the log off the play view, which batch 3 removed, so it saw nothing (its md5 differed for that reason). I re-ran the replay and read Messages > Combat instead.

Ruled since the hold, not filed: Party Selection becomes a scrolling list with a party lock; the mid-fight swap is being fixed; conversation clipping to be retested on the new letterbox; the scroll bar becomes 8 px.

Known and not filed: dialogue, computer, game over, pause, area transition and confirm screens on old frames (batch 4); the store's gold, lit rows, the combat bar and the white ring are reasoned; list boxes short at the right edge.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
