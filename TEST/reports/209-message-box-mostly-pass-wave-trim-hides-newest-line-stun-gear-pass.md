# TEST 209: the message box, a stunned character's Gear

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-209/` (MAIN_WORK `878532da`). The step-by-step log is `TEST/reports/209-running-log.md`.

## Build

- **App**: main `cab0e62`, a git worktree beside my own clone. `gate.py --at cab0e62`: "FOR TESTER — CORE at cab0e62, 5237 tests, 0 failed"; ARCHIVE last green at cab0e62. Lodestar `5b1a90e` = lock = compiled. The build (10.0 s) went through the lock, and git status was clean.
- **Settings**: defaults. Brightness: default.
- **Shelf** `553002b`: unchanged; all packages identical.

There was no bed tool for this hash, so I made my own (`specs209/`):

- stun-209: a Soldier carrying an Energy Shield, on rx-stun-bed's mine.
- nade-209: a Soldier with three Frag Grenades, in the push yard.
- wave-209: Push Jedi in a local package, `tester-wave`, which is the push yard plus ten more targets (16 in all).
- bm-209: a Jedi with Battle Meditation and Force Valor.

## Summary: most pass; one finding

| # | Check | Result |
|---|---|---|
| 1a | Layout | **PASS** at 1920 and 1280: the prompt sits on its own row at the box's full width, with the name on a row beneath |
| 1b | Wave in a fight | **FINDING** (below). The front parts are dropped as meant, the box stays under 45% (41% at 1920, 40% at 1280), and the full text is in Messages > Combat. But the newest part is hidden below the box's edge. With the yard's 6 targets everything fits (26% / 24%), so nothing needs trimming |
| 1c | Grenade | **PASS**: one throw caught five (four enemies and the thrower), and the prompt is whole, ending "· 2 left" |
| 1d | Outside a fight | **PASS** for a long description: Battle Meditation's (1920) and Force Valor's (1280) are whole. **Not reached**: a prompt tall enough to scroll outside a fight; I found no way to produce one in play |
| 2 | Stunned and Gear | **PASS**: stunned by the mine in a fight, G is refused and a move works. The queue shows Move lit, Action and Gear dim. **Small**: the refusal reads "gear — Energy Shield cannot be used — gear has already been used this turn", though nothing was used; the stun is the reason |
| 3 | Dice, regression | **PASS**. All 17 Round, attack and damage lines match `dice-baseline-206.txt`; the only difference is OCR on line 1, as in TEST 208. Regression: Save (slot 46, "reg209"), Escape then F4 (one quick save), Load, and a fight won |

## Finding: in a fight, Wave's trimmed prompt hides its newest part

With Force Wave on 16 targets:

- **At 1920**, the prompt starts "… stunned · Slowpoke — 8d6 21 · Quickstep — …" but its last visible line ends "Slowpoke — d20 10 =". Scrolling the prompt shows the hidden tail, "6 vs 30 · stunned · Slowpoke — 8d6 36".
- **At 1280×720**, the bottom line is sliced through horizontally, and about a line and a half more lies below.

So the trim keeps one or two lines more than the prompt's share holds, and the box clips them instead of dropping more parts from the front. The newest result is the part that's lost.

Frames: `wv-1920.png`, `wv-1920-scrolled.png`, `wv-1280-zoom.png`, `wv-1280-scrolled-zoom.png`.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
