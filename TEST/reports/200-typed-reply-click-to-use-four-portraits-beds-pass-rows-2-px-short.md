# TEST 200: Tab for the typed reply, click to use, four portraits, the small fixes, and the beds

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots are in `KOTOR_RPG_MAIN_WORK/media/screens/test-200/` (MAIN_WORK `0b43bb0c`). The step-by-step log is `TEST/reports/200-running-log.md`.

## Build

App main `184bdc2`, a git worktree beside my own clone. `gate.py --at 184bdc2`: "FOR TESTER — CORE at 184bdc2, 5141 tests, 0 failed"; ARCHIVE last green at 184bdc2. Lodestar `e1b6ed9` (on origin/main) = lock = compiled. Lens `5fe60a9`. Shelf `b2de52b`; check_shelf clean (33 rules files, 125 blueprints). The build (12.9 s) and every `dart run` went through the lock, and `pubspec.lock` was unchanged.

Settings: no settings.json was present, so everything ran at the defaults. Brightness: default.

Packages: I synced every Shelf package in my data to `b2de52b`, keeping the old copies in `notes/`:
- rx-two-triggers: gains energy-shield.item.
- base-rules: my copy lacked the party.locked/unlocked event kinds.
- precognition-ambush: my copy had extra motivator items.

Beds:
- Coder's tool wrote gear-hand.sav and no-pool.sav.
- My own (`specs200/`): Four Up (a Soldier with three Velas) and Tab Ten (a copy of Pool One).

## Summary: everything passes; one small measurement remains

| # | Check | Result |
|---|---|---|
| 1 | Typed reply | **PASS**: "[Type a reply.]" is unnumbered. Tab lights it, and so does a click. With the row focused, digit 2 still pressed "[Continue]" and digit 1 "[Leave.]", and neither typed. Letters ("wh") start typing and light the row |
| 2 | Click to use | **PASS**. A plain click on the console from 2 squares away walks beside it and opens the terminal. On the locked footlocker it tries Open Lock first ("you cannot use Security untrained — it needs at least one rank"). On the crate it walks beside it and examines it ("examine Shipping Crate — d20 20 + Science 0 + Intelligence 1 = 21 …"). Stepping into the crate is refused ("the Shipping Crate is in the way"). The doors: locked ones refuse as before, and on Endar Spire a plain click on the door crosses ("Starboard Hold — arrived at north · saved") |
| 3 | Four portraits | **PASS**. Four Up's HUD shows four (the active member large, three stacked); parties of two and three show two and three. Bars: Vela at 25/40 shows about 60% red from the foot, and the downed player (0/12) shows an empty bar. On Tester Bolt the fourth slot sits right of the board, not over its corner, because the board ends left of it |
| 4 | "[Leave.]" | **PASS**: one full stop in the terminal and in conversations |
| 5 | Rows | **Measured** (below): our row line still ends 2 px nearer the list line than K2's |
| 6 | Beds | **PASS**. gear-hand: G then 1 gives "Energy Shield up, 40 …", and Gear dims (brightness 27 → 8). Yes to "Backer leaves your reach" hit (Backer 30 → 26) and No to Kael's question; the line then reads "Reactions (out of turn): none". no-pool: in the fight there's no reactions line, only "Defense base 10 = 10" |
| 7 | Dice, regression | **PASS**: from Dice One's Quick Save, Messages > Combat rounds 1–3 match TEST 185 line for line. Regression: Save (slot 36, "reg200"), Escape then F4 (one quick save), Load, and a fight to its end |

## Item 5: the x values (Abilities > Skills, 1920, same y on the row and on the list line, against K2's 05c)

| | row line (lit pixels) | dark gap | list line |
|---|---|---|---|
| Ours, y 258 | 925 (88,99,88), **926** (140,147,132), **927** (124,133,118) | 928–931 | 932–933 |
| Ours, y 300 | 925, **926**, 927 | 928–931 | 932–933 |
| K2, y 258 | 923 (93,102,92), **924** (121,129,116), **925** (97,109,97); 926 faint | 927–930 (931 faint) | 932–933 |
| K2, y 300 | 923, **924**, 925 | 926–930 | 932–933 |

Our row line's last lit pixel is 927, and K2's is 925. Coder's "925" matches the first pixel of our 3 px row line, not its last. So our rows still reach 2 px nearer the list line than K2's (a 4 px dark gap against K2's 6).

## Small

- At load, a companion placed by the area draws as a red party disc while joined ones draw as "V" circles (Four Up, Fight Nine). After a remove and re-add they become one look (the TEST 199 fix holds for that path).

Known and not filed: digits inside the typed field; "[Continue]" without a full stop; no K2 capture of the combat bar. Down at exactly 0 wasn't hunted, as told.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
