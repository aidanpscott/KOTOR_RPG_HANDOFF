# TEST 159a (partial: PT-2738 only)

Written for: Main and Coder. Main's scope change: on app 5bc6af2, ONLY the PT-2738 Force-well checks. The rest of TEST 159 (PT-2739 items: Continue mid-fight, the Strongroom card, name-not-tag) is **HELD** until Main sends the hash that contains PT-2739. Screenshots: `HANDOFF/BUILD/screens/test-159a/` (10 images). Real game on my Xvfb `:2`, my own data dir; K2 not launched.

## Build

- App `5bc6af25af6774d404ea94bf3bf5c77e489c6896` (= origin/main when fetched; contains PT-2738 `9fc1bcb`; `git archive` into `/tmp/test159-build`, `flutter build linux --debug`; `pubspec.lock` unchanged by the build).
- Lodestar `e729d363c1f84904d5a0acd012bb2b90ba850e57` = lock = pub-cache.
- Lens `2bad745a53a1e741ab8d8ef94a954e6e3973b99b`, Shelf `8fa2475c79a1119b94def5700303481b09d4839f`, MAIN_WORK `362657694b2a68ef8f0c035c2645bd560abf4f4a`, HANDOFF `1d0cb60` at start.
- `check_shelf` clean (30 rules files, 105 blueprints). System clang/cmake/ninja, Flutter 3.47.2 on PATH (no `tool/env.sh`, see TEST 158).

## Summary

| # | Check | Result |
|---|---|---|
| 1 | Chargen droid: well in sidebar and footer, empty | **PASS for a droid made first in a session** (T3-91). **FAIL after another character was played in the same session**: the droid shows that character's pool (8 of 8) and stands on its square (2 of 2) |
| 2 | Non-Force human (Soldier): empty well | **PASS** (sidebar and footer) |
| 3 | Jedi control: real pool | **PASS** (8 of 8, full in both views) |
| 4 | Jedi and Soldier companions: own pools | **PASS** for companions that joined in play (Guardian 57 of 57 full, Grunt empty). A fixture-added copy shows 33 of 33 (see note) |
| 5 | Footer well position matches the sidebar | **PASS**: right of the portrait in both views; footer rect identical for Soldier, Jedi and droid |
| + | Owner's question: is it the existing bar, not a new one? | **YES**: same widget, same size, same border, same empty track as the vitality bar beside it, in both views (only colours differ) |

## 1. Chargen droid

**Clean case — PASS.** App restarted, Tester Save Bed → New Game → Droid → Astromech → T3-series → Engineer → hub (Repair Droid programming, fixed astromech abilities, 28 skill points, feat Cautious, Standard Gear, designation T3-91) → Play. T3-91 arrives on "in" (1,1); the sidebar shows the vitality bar left and the **Force well right, drawn and empty** (track colour (36,31,26), the same as the vitality bar's own empty part), with no "force" line (`f4`). The Options footer shows the well right of the portrait, framed, interior black = empty (`f5`).

**FAIL — a new character inherits the previous character's Force pool and square.** Smallest repro:
1. Launch the app; in Tester Save Bed load a Jedi (Onjo Proof or Onjo Hp, force 8 of 8) and let it stand anywhere but "in".
2. Options → Exit Game → OK → New Game → make a droid (any class) → Play.

Expected: an empty well, arrival on "in" (1,1). Got: the droid's sidebar reads **"force 8 of 8"** with a full blue well, the status line says "force 8 of 8", the footer well is filled (`f6`, `f7`, `f8`), and the droid stands on **the Jedi's last square** — (3,2) after Onjo Hp (T3-77), (4,4) after Onjo Proof (T3-21), not on "in". Seen 2 of 2 times after a Jedi; 0 of 1 for a droid made straight after an app restart (T3-91). The leak is then **written into the new character's own autosave**: after a restart, T3-77 still shows 8 of 8 and `t3-77.marks/autosave.world.json` reads `"force":{"current":8,"ceiling":8,"trueMax":8}`, `"at":[3,2]`, so the character is permanently wrong, not just the screen.

**Likely cause, not shown:** play-screen state (`_force`, the board position) is not reset between Exit Game and a New Game in the same session, and the first autosave writes it. Probably older than PT-2738 (the old sidebar drew the wing whenever `row.force` was non-null, which a leaked pool is), but now visible on every character; I did not run a845f96 to prove it. Related shape: TEST 148 (h), the last loaded character's "rules not checked" count shown on a New Game.

## 2. Non-Force human — PASS

Five-party game, player "Visual Pass Tester", Soldier 5: sidebar well drawn, empty (`f1`); Options footer well framed, interior black (`f2`).

## 3. Jedi control — PASS

Onjo Hp, Jedi Sentinel 1, force 8 of 8: sidebar well full blue; footer well filled (interior (12,54,46) against black for empty) (`f3`). The vitality bar beside it was partly full (47 of 103) in both views, so both bars track their values.

## 4. Companions — PASS (with a fixture note)

Same five-party game (`f1`): **Guardian (Jedi Consular 6): "force 57 of 57", well full**; **Grunt (Soldier 4): empty well**, no force line. 57 is right by `forcePoolFor`: d8 at level 6 = 33, plus (WIS +2 + CHA +2) × 6 = 24.

Note, not a filing: the **second Guardian** (same blueprint, same class and level) reads **"force 33 of 33"**: the die alone, as if WIS and CHA were 10. It is one of the two companions `tool/author_five_party_fixture.dart` adds with only a `partyJoined` event; `_companionRecordFor` replays a companion's own logged events, and that tag has none with scores. So this is likely the fixture, not the game, but it shows the pool reader trusts the log while the companion sheet reads the combatant (14/14): the two would disagree for any companion whose scores were never logged. The companion tiles in the footer carry no bars (only the active member's portrait does).

## 5. Position — PASS

Footer, measured on Soldier, Jedi and droid screenshots: vitality frame x 1286–1312, Force frame x 1487–1513 (its left border runs into the portrait frame's at 1484), **both y 859–990, 3 px borders, the same rect in all three**. Sidebar: vitality bar x 170–178, Force well x 283–291, both 9 px wide with the same vertical extent in every card. Right of the portrait in both views.

## Owner's question: the same bar, not a new one — YES

- **Footer:** both bars are one widget, `PartyPortraitFooter._gaugeBar` (`equip-vitality-bar` and `equip-force-bar`), same size and border; the Force call differs only by colours (teal outline `K2Border.lineColour`, fill `0xFF0C362E`) and a wider left edge where it shares the portrait border. Empty part: black in both.
- **Sidebar:** both are `_Wing` (`_forceWing` → `_Wing`), same 9 px capsule, same empty track (36,31,26); vitality fills green, Force blue (`f9`, `f10` zoomed).
- Observation: the footer's **full** Force fill (12,54,46) is very close to the empty black; a full and an empty well are hard to tell apart at a glance (`f10`). Vitality's fill (97,53,34) reads clearly. Not compared with K2's colours.

## Fixtures

New this session (my data dir): `t3-77` (droid, **contaminated**: carries Onjo Hp's pool and square), `t3-91` (clean droid), `t3-21` (droid, contaminated by Onjo Proof). Existing: `five-party`, `onjo-hp`, `onjo-proof`, `onjo-bed`, `tee-three`, `tester-visual-4`, package `tester-save-bed`. Helper `run/cgdroid.sh` (droid chargen path; the Skills and Feats rows shift ~24 px when the "no recommended allocation" warning is absent, which it was on every run after the first).

## Held for the PT-2739 hash

Continue after leaving mid-fight resumes the same fight (same initiative and round); the Tester Strongroom card text; name-not-tag in the speaker line and combat log.

Skills used: `verification-before-completion` (every PASS is a pixel measurement, an on-screen value or an autosave field), `diagnosing-bugs` (the leak reproduced twice with two different Jedi, a clean control after a restart, and the persisted autosave read), `research` (Coder's 9fc1bcb message and `forcePoolFor`), `writing-for-agents`. `handoff`: `TESTER-STATE.md` updated.
