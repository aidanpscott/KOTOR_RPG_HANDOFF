# TEST 181: the TEST 180 fixes and the attack-of-opportunity rework

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-181/` (MAIN_WORK `f397ca25`), one prefix per item. The step-by-step log is `TEST/reports/181-running-log.md`.

## Build

App `5cde10d`, git archive to `~/kotor-tester/builds/test181`. Lodestar `29b139f22e7aeafd52867a1be390bd2bd4558b9c` = lock = compiled. Lens `fe10327793b1a28882b088d2fbf8148e83ead926` = lock = compiled. Loom has no entry in the lock. Shelf `1e3ffb4` (= origin), check_shelf clean (118 blueprints). `tool/env.sh` sourced. The build went through `tool/one_at_a_time.sh` (2298 s, nearly all of it waiting on Coder's `flutter test`), and `pubspec.lock` was unchanged. My fixture `dart run` also went through the lock. The bundle was launched with `&` outside the lock.

Fresh fixtures: chargen characters plus four authored saves (specs in `~/kotor-tester/notes/fixtures/specs181/`). New local beds in my data dir: `tester-pass`, `tester-minek`, `tester-minesolo`. `tester-mines` got a findable hidden crate, and `tester-lshape` went back to TEST 180's two-target layout.

## Summary: nine pass, one recorded

| # | Check | Result |
|---|---|---|
| 1 | Opportunity attacks | **PASS, (a)–(h)**. (a) walk up and stop: none from the target. (b) beside to diagonal, and round while adjacent: none. (c) step away: one. (d) walk past: one, at the leaving step. (e) Disengage: none. (f) the droid: none ("melee is closed to every droid chassis"); the gunman with a rifle: none, no provoke line; the empty-handed droids threaten. (g) move-and-attack approach: none from the target. (h) an enemy chasing Kael past me: "Opportunity attack: Aoo One attacks Sentry Droid : *miss* : (3 + 5 = 8)". The "Provokes an attack" line showed only on paths that did provoke |
| 2 | Combat log | **PASS**: its own column right of the board at 1920x1080 and at 1280x720, never over a square. It scrolls back to Round 1 after 13 rounds. Flanking reads "… : (13 + 3 = 16) · Flanking +2". A kill reads "Sentry Droid dies" (status "· -3 left · dies"). No dotted kind seen |
| 3 | Hidden placeables | **PASS**: an unfound one is not drawn. A stealth-1 crate is drawn once "you notice Shipping Crate — 15 against 1". A stealth-60 crate is never drawn |
| 4 | Continue after a hard kill | **PASS** for F4, for F5 (quick load) and for Escape > Save: after `kill -9`, restart and Continue, I'm on the saved square each time. **Finding**: after the Escape > Save run, the crate I'd found earlier is no longer drawn |
| 5 | Targeting | **PASS**: in TEST 180's layout, the (5,0) droid chose Kael, reached him in round 2, and attacked him every round to round 8 |
| 6 | Move preview | **PASS**: "5 move" at a turn start beside rough ground with the pointer off the board; "5 → 3" only while hovering |
| 7 | Mine saves | **PASS**: Kael (Evasion) made the save and took nothing: "d20 12 + Dexterity 1 = 13 vs 5 · you are clear". The player, without Evasion, made it and took half: "… = 13 vs 5 · 3 damage". Each rolls with their own bonus. **Content note** below about mines with no save kind |
| 8 | A mine to 0, outside a fight | **PASS**: (a) alone: the game-over box, and after a restart Continue goes straight back to it. (b) with Kael standing: the player is back at 1, and still 1 after reload. (c) Kael under control: Kael takes it, "revived at 1", the player is untouched, and Kael is still 1 after reload |
| 9 | K2 log lines | **Recorded**, all four (verbatim below) |
| 10 | Quick regression | **PASS**: numpad diagonals do nothing, melee and ranged flanking +2 at half range, Vanguard Assault Boots DEF 17 → 20, stack numbers, the path line, and Escape + F4 rewrites one quick save |

## Findings and notes, most useful first

1. **A found hidden placeable is forgotten after Escape > Save.** In Tester Mines I found the stealth-1 crate ("you notice Shipping Crate"). It stayed drawn after F4 + kill + Continue and after F5 + kill + Continue. After walking away, Escape > Save > New Slot, kill and Continue, it is gone from the board (`i04c-escape-save-kill-continue.png` against `i04b`).
2. **Mines with no save `kind` roll a bare d20 and ignore Evasion.** My first bed copied Locked and Trapped's mine (`save = { dc = 15, on_save = "half" }`, no `kind`). There Kael rolled "d20 19 = 19 vs 15 · 3 damage" with no bonus and no Evasion (`i07d`). `evasionApplies` needs `kind = "reflex"`. The shipped Locked and Trapped and Tester Strongroom mines carry no kind, so every save on them is bare. That's content, not app code, but worth a check_shelf rule or a default.
3. **A companion's square is not restored.** After F4, kill and Continue, Kael stands on his start square (0,4), not where he was (item 8).
4. **The grenade key throws at once.** 'o' threw the frag grenade at the nearest droid with no aiming step, and the blast took Kael and me too (20 each).
5. **Wording**: Kael's made save reads "you are clear" (second person). The status form of a save drops a bonus ("Sentry Droid — d20 18 = 20 vs 18", where the log reads "(18 + 2 = 20 vs. 18)"). A dead droid's card reads "struck down 0 of 24" while the bottom line reads "-3 of 24". The enemy action banner can sit over the top of the log column. The hit-chance tooltip and an enemy's hover banner overlap on a move-and-attack hover.
6. **"has been affected by" on a resisted save**: Force Stun resisted, yet "Sentry Droid has been affected by Force Stun" (the lesser effect, slowed). Probably intended; flagging so it's a choice.
7. Droid B ("noticing") took no action in round 1 of three identical fights, even after being hit.
8. After a load, the first d20 is the same every time (1 in Mine Lane), so a test must spend a roll to vary it.

## K2 log lines, verbatim (item 9)

- `Pwr One attempts Force Stun on Sentry Droid : *resisted* : (18 + 2 = 20 vs. 18)` (1405)
- `Sentry Droid has been affected by Force Stun` (47873)
- `Pwr One uses Frag Grenade.` (32292), then `Kael damaged: 20`, `Sentry Droid damaged: 20`, `Sentry Droid damaged: 20`, `Pwr One damaged: 20` (1402)
- `Pwr One uses Medpac.`, then `Pwr One : Healed 10 hit points.` (1495)
- Others seen: `Opportunity attack: Sentry Droid attacks Aoo One : *miss* : (7 + 1 = 8)`; `Sentry Droid attacks Aoo One : *hit* : (13 + 3 = 16) · Flanking +2`; `Sentry Droid dies`; `OA Droid is a droid holding unarmed — melee is closed to every droid chassis, so it has no attack it can make`

## How the AoO cases were run

Each creature has one reaction per encounter, so the cases were spread over three fights from one pre-fight quick save in `tester-pass` (me beside droid A, droid B at (9,0), Kael at (6,0)), plus separate beds for the droid, the gunman and the walk-past.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
