# TEST 141 — companion contamination holds fixed; item-loading does not, and it's narrower than it looked

**Build.**

```
local HEAD              478c60ce42d9209653dd2ea17f61cd036b8660b5
                        "Unarmed Specialist's own damage ladder reaches
                        the fight, not the flat 1d3"
working tree            one uncommitted change (lib/play/attack.dart) and
                        one untracked file (lib/chargen/granted_feats.dart)
                        found at session start — Coder's own live work,
                        confirmed by nothing in this report touching
                        either; archived from the COMMITTED tree via
                        `git archive HEAD`
pubspec.lock resolves   lodestar  496d5e79088e5fbc2160ce4cb60da86a5d813594
pub-cache checkout      ~/.pub-cache/git/Lodestar-496d5e79.../ — present,
                        confirmed against the committed lock
```

**Environment, per the work order.**

- Own data directory: `XDG_DATA_HOME=~/.local/share/tester-data`, seeded
  with a copy of the shared shelf's `packages/`. Confirmed on first
  launch — saves land under `tester-data/kotor-rpg/saves/`, and the
  shared directory's own file count (1913) was unchanged by anything in
  this pass, checked again at the end (still 1913; `tester-data` grew
  from 1747 to 1750, the three saves this pass wrote).
- Own display: `Xvfb :2`, no window manager (this build's window was the
  only one on that display, so none was needed for input to reach it —
  confirmed working throughout). Killed cleanly by its own PID at the end
  of the pass, same as the app process.
- `linux/` is gitignored and absent from a fresh `git archive`; rebuilt
  with `flutter create --platforms=linux .` before building, same as
  TEST 140.
- `HANDOFF/BUILD/screens/51-equip-slot-view.png` and
  `52-equip-item-selected.png`: **not mine.** Checked before touching
  anything — both are Equip-screen screenshots, mtime today, last real
  commit yesterday (`945c8dc`, "Mirror PT-2696, refresh screens with the
  tpc.py flip fix applied"). Matches Coder's own listed "mid-change, not
  yet" item (Equip's visual layout) exactly. Left untouched, staged and
  committed nothing from `BUILD/` this pass.

**Verdict — the contamination fix (PT-2687/2690/2693/2698) holds up in
real play. The item-loading defect (PT-2688) does not, but it's narrower
than TEST 140 could tell: it's specific to the Hunter background's own
melee-upgrade grant, not the ordinary starting array, which resolves and
displays cleanly on every screen checked.** Dual-wielding's mechanics are
confirmed correct with real numbers from a real fight. Store buying and
selling both round-tripped correctly. Two items not reached this pass:
terminal interaction, and the no-feat dual-wield tier.

---

## 1. Companion data no longer leaks into the player — CONFIRMED

Built a fresh character through real chargen (`Isolde Vestic`, Human
Soldier — every step driven by mouse, including the Skills "+" stepper
that stalled a large part of TEST 140 before its root cause turned out to
be this session's own tooling, not the app), then entered the
`0 AAA Visual Pass` package's hall, where Guardian (Jedi Consular ·6) and
Grunt (Soldier ·4) auto-join as henchmen on arrival.

Character Sheet immediately after entering, both companions already
joined:

```
Isolde Vestic — Soldier · level 1
STR 14  DEX 14  CON 14  INT 12  WIS 12  CHA 12
```

Exactly what chargen wrote. No trace of either companion's class,
level, or ability scores — the exact shape PT-2687 found broken (a
joined companion's data overwriting the player's own display) does not
reproduce here.

**Reloading — confirmed stable, not exhaustively to the letter of the
ask.** Loaded this same character through "Leave Session → Load Game"
repeatedly across this pass (building the store-bed character separately
required leaving and returning to the package menu twice more). No
"class levels add to N" refusal appeared on any reload. I did not
specifically level a companion up first and then reload three times in a
row as its own isolated step — everything else this pass needed the
reload path anyway, and it held every time it was exercised, but that
specific sequence is worth a dedicated five-minute check before calling
it exhaustively proven.

**Alignment and combat-log attribution — COULD NOT TEST, and the reason
traces straight back to a TEST 140 finding.** Both asks need a companion
that can cast a power (a dark-side one, for alignment; any, for the log
line). TEST 140 found that `blueprints/characters/*.toml` — the format
every henchman auto-joined via an area's `[[contents]]` uses — has no
field anywhere for granting known Force powers, confirmed by reading
`character_open.dart` line by line. Guardian is authored as a level 6
Jedi Consular in exactly this format and knows nothing, confirmed again
this pass (pressed `f` during its own turn: *"Guardian knows no Force
powers"*, an honest refusal, not a bug). Without a companion that can
even attempt a cast, neither the alignment check nor the log-attribution
check has anything to observe. This isn't a new defect — it's the same
gap TEST 140 named, now blocking two more items on its account.

## 2. The "0 AAA Visual Pass" package — CONFIRMED, fresh character

Entering it fresh (Isolde, above) produced no corruption on entry or
after saving and reloading. Did not separately test entering it with an
*already*-companion-bearing character built elsewhere and imported in —
every character this pass met its companions by joining the same package
fresh, which is the more common real path but not the literal second
half of the ask.

## 3. Starting gear and Defence — mixed, and the mixing has a clear edge

Built two characters specifically to separate two things TEST 140 had
found tangled together: the item-loading defect, and the companion
contamination defect. Both are Human Soldiers; one took the Hunter
background's melee-upgrade grant (replacing the array with Long Sword +
Short Sword), the other kept the plain default array (Blaster Rifle +
Short Sword) via the Doctor background instead.

**Default array (Dalen Lhent) — Defence matches, and a real weapon rolls
its own dice:**

```
Character Sheet: Defence 12
Equip:            DEF 12
```

Agree exactly. Equip's own damage readout for the equipped blaster-rifle:
`ATKR 3-14, +3` — a twelve-value spread (3 to 14), exactly `1d12 +2`.
Confirmed via the Equip screen's own numbers, not a live fight — Dalen
never got into combat this pass (the store-bed package's market has no
hostile in it). Worth a live confirmation next pass, but the die size
itself is not in doubt from this reading.

**A real, separate gap found here: the array's second weapon never
equips at all.** The Equipment step's own preview text names
`weapon: Blaster Rifle · Short Sword` for the default array — and the
melee-upgrade text elsewhere states outright that *"a two-weapon start is
an alternative to the array, not an addition to it,"* which only makes
sense if the array itself is normally two weapons. Checked Dalen's
Inventory under every filter (`ALL`, `WEAPONS`): only `blaster-rifle`
exists. No short-sword anywhere, equipped or not. Equip's own weapon
slots show one filled, one genuinely empty — not hidden, not
mis-labelled. Whether this is meant to be a single-weapon array with
stale preview text, or a real second weapon that silently never gets
created, I don't know from the outside; it's not the same shape as
PT-2688 (that's an item resolving with confidence and then refusing to
open — this is an item never appearing to have been created at all), so
flagging it as its own finding rather than folding it into that one.

**Melee-upgrade array (Isolde Vestic) — Defence disagrees across all
three places it's shown, and PT-2688 is confirmed still open:**

```
Character Sheet:  Defence  —
                   'upgrade' will not open: There is no item here.
                   'soldier-both-0' will not open: There is no item here.
Equip:             DEF 12
Live combat log:   defence base 10 + Dexterity 2 + class 3 = 15
```

Three screens, three different answers (blank, 12, 15) for the same
character at the same moment. Sent this the moment it was found
(TESTER → MAIN, mid-pass) rather than waiting for this report — this is
the failure MAIN's checklist named directly ("the Character Sheet and
Equip must show the same Defence"), and it does not hold.

**The important refinement over TEST 140's own finding: this is scoped to
the Hunter background's own melee-upgrade grant, not item-loading in
general.** The default array, checked minutes apart on a nearly-identical
character, resolved and displayed perfectly on every screen. Both
`'upgrade'` and `'soldier-both-0'` read like internal ids from however the
melee-upgrade grant resolves its own two items, not blueprint paths like
the ones TEST 140 saw fail for a hand-authored save's armour and weapon.
Worth Coder checking specifically that resolution path rather than
re-checking `resolveStartingWeapon`/`resolveStartingArmour` broadly —
those two are exactly what produced Dalen's clean, matching Defence.

**Weapon dice, confirmed live for melee:** Isolde's own fight (below)
landed a real hit with `Long Sword: 1d8 (rolled 8) + Strength 2 = 10
damage` — a real per-weapon die, not a flat fist, confirmed by an actual
roll rather than only a resolved description.

## 4. Dual-wielding, player side — CONFIRMED on every mechanic checked live

Isolde (Long Sword main, Short Sword off-hand, `Two-Weapon Fighting`
taken at 1st level) walked into Hostile in the `0 AAA Visual Pass` hall.
Two real rounds:

```
Long Sword · rolled 9 — d20 9 + attack 1 + Strength 2 − dual-wield 3 ·
  needed 15 — miss
off-hand: Short Sword · rolled 10 — d20 10 + attack 1 + Strength 2 −
  dual-wield 3 · needed 15 — miss

Long Sword · rolled 15 — d20 15 + attack 1 + Strength 2 − dual-wield 3 ·
  needed 15 — hit · damage 10 — 1d8 8 + Strength 2 · 11 left
off-hand: Short Sword · rolled 14 — d20 14 + attack 1 + Strength 2 −
  dual-wield 3 · needed 15 — miss
```

- **Two attacks, main hand then off-hand, each named by its own
  weapon** — confirmed, every round, in that order.
- **Every attack that round takes the penalty** — confirmed, both hands,
  both rounds.
- **The penalty tier with Two-Weapon Fighting is −3** — confirmed exactly,
  matching MAIN's own stated tier. **This directly contradicts the
  feat's own description text**, read during Feats selection at chargen:
  *"Dual-wield penalty reduced from −6/−10 to −6 main / −6 off."* The
  real fight applies −3/−3, not −6/−6. The mechanic is right; the feat's
  own chargen-time description of what it does is wrong. Worth a
  content fix independent of anything else in this report.
- **Equip's readout matches what the fight actually rolled** — confirmed
  for the Long Sword: Equip showed `3-10` before combat, and the real hit
  landed exactly inside that range (`1d8 + Strength 2` = 3 to 10).
- **Two-handed weapon cannot be paired** — **could not test.** Isolde's
  melee-upgrade grant replaces the array outright with two one-handed
  weapons; nothing two-handed was ever in her inventory to try equipping
  into the second slot, and this pass didn't have time to author or buy
  one specifically to force the refusal.
- **The no-feat tier (−4)** — **could not test** this pass; would need a
  second character built without Two-Weapon Fighting and put through the
  same fight. The −3 tier is the one directly confirmed.

## 5. Terminal and Store — Store confirmed working; Terminal not reached

Used `store-bed` — a real shelf package built specifically for this
("a merchant, a conversation that opens their store, and a real
catalogue of items... the way it is actually reached"). Spoke to the
merchant, picked `[Opens-store]`, bought a Vibroblade (Credits 100 → 0,
item appeared in Inventory), then sold it back (Credits 0 → 100, item
removed). Both round-tripped cleanly, no errors either direction.

**Could not judge the texture-orientation fix (PT-2696) either way.**
Every item's icon panel in this store rendered as an empty box — no art
at all, not a flipped or garbled one. Consistent with the same
"placeholder, not imported" behaviour seen everywhere else in this app
(portraits, for one), not a sign of anything broken specifically here.
There was simply nothing to look at and judge upside-down or not.

**Terminal interaction — not reached this pass.** Ran out of time before
finding or building a fixture with an actual computer-terminal
interaction distinct from the merchant conversation; `locked-and-trapped`
and its rebuilt variants reference one and are the likely next place to
look.

---

## Fixtures

- `~/.local/share/tester-data/kotor-rpg/packages/store-bed/` — a real,
  pre-existing shelf package (not authored this pass), renamed locally
  (`0 AA Store Bed`) only in this isolated `tester-data` copy to work
  around the still-unsolved horizontal-scroll problem on the console
  home library row — the shared shelf's own copy was never touched.
- Both characters built this pass (`Isolde Vestic`, `Dalen Lhent`) are
  autosaves under `tester-data`'s own `saves/`, not the shared directory.

No stray processes: the app (isolated display, own PID) and the `Xvfb`
instance it ran on were both killed by their own recorded PIDs at the
end of this pass, neither by name nor pattern, and never shared the
display Coder's own screenshot loops were using.
