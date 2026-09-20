# TEST 119 — Force Confusion never applies anything, and Force Distraction holds except for facing and four droid species

**Build.** App **`1b1c357`** ("Force Confusion: the targeting override —
PT-2439, PT-2442"), built from `git archive` of that sha; the built copy of
`play_screen.dart` is **byte-identical** to `1b1c357`'s (`md5 4e3282bc…`), so
every line number below is the binary's own. The committed lock resolves
Lodestar **`39791f59`**, and that is the pub-cache checkout
`package_config.json` compiles against. `check_shelf.py` clean: 29 rules
files and 65 standard blueprints.

⚠ **The working tree went dirty mid-run** — `abilities_screen.dart`,
`records.dart`, `main.dart`, `fight.dart`, `play_screen.dart` and
`pubspec.lock` (bumping Lodestar to `54c5394`), plus an untracked
`a_blinded_character_loses_its_dex_test.dart`, and on the shelf an
uncommitted `species.toml` addition giving Togruta
`keeps_dex_when_blinded`. That is the blinded thread, not this one. I read
`play_screen.dart` from the working tree first and **re-read every citation
out of the built copy** before writing it down; the line numbers moved by
~57, which is exactly how much the wrong copy would have cost.

**Verdict.** Item 2 is **not testable at all: Force Confusion applies
nothing.** The power charges 20 Force and 4 of ceiling, prints its prose, and
returns before it reaches its own effect. Item 1 holds on four clauses,
carries **one real defect** (the droid exclusion fails on four of the five
droid species), and has two clauses with no code behind them.

---

## 2. Force Confusion — inert, and proven inert in play

### The reading

One encounter, consecutive turns, one die stream, one distracted guard.

```
turn 2   Force Confusion · 20f — 151 → 131 · ceiling −4 to 154 · at guard.gd.01 ·
         <the power's description text, and nothing else>
its turn guard.gd.01: unarmed · out of reach — unarmed reaches 1 square and Whisper is 4 away

turn 3   Force Scream · 8f — 131 → 123 · at guard.gd.01        (guard 400 → 387)
its turn guard.gd.01 closes 3 squares — 4 to 1 · guard.gd.01: unarmed · rolled 4 — miss
```

No save roll, no `turns on its own side`, and the guard went on being
distracted.

### Why that pair is the proof, and not just a missing message

`_perception.undistract(c.handle)` is the **first statement inside
`_applyPower`'s body** (`play_screen.dart:11239`), three lines above the
confusion branch at `11246`. **Any** power that reaches the body clears a
distraction as a side effect. Force Scream reached it — the guard stopped
being distracted and closed. Force Confusion, cast one turn earlier at the
same creature, did not.

So this is not *"the power printed nothing"*, which a made save would also
look like. It is a **positive state change that a power reaching the body
cannot avoid making, and Force Confusion did not make it.** The power
returns before its own branch.

⚠ This matters because the alternative explanation was live: a made Will
save also prints nothing here. The target is Wisdom 3 against a DC near 25,
so a made save was already implausible — but implausible is not measured,
and `undistract` is.

### The cause

The early-return list in `_applyPower` (`play_screen.dart:10705–10755`):

```dart
if (named == null &&
    !p.distracts &&            // ⚠ PT-2436
    penalties.isEmpty && rot.isEmpty && dmg == null && !healsAnybody &&
    p.immunity.isEmpty && p.skillBonus.isEmpty &&
    p.forceBodyPercent == null && p.weaponInertRounds == null &&
    mods.isEmpty) {
  return null;
}
```

`p.confuses` is **not in it** — the string `confus` does not appear anywhere
between lines 10700 and 10760. And `force_confusion`'s shelf row carries
`targets`, `affects`, `save_kind`, `confuses`, `confusion_rounds`,
`excludes` and nothing else: no condition, no penalty, no damage row, no
heal, no immunity, no skill bonus, no Force Body share, no weapon effect, no
modifier. Every clause is true, so it returns `null`.

⚠⚠ **The twin list WAS updated in the same slice.**
`PowerRecord.appliesNothing` (`records.dart:1238` and `1240`) carries both
`!distracts` and `!confuses`, the second added by PT-2442 with a comment
saying so. The comment three lines above the early return says the two
*"must say it together: `PT-2390` found them already drifted apart."* They
drifted apart again, in the slice that wrote the warning. This is the
seventh time this list has been short — Force Aura, `heals: self`,
`heals: ally`, Breath Control, skill bonuses, Force Body, Shutdown — and the
first time the reader's half was written and the applier's half was not.

⚠ **And updating `appliesNothing` is what hides it.** Because
`appliesNothing` is now false for this power, the refusal at `12352` —
*"⚠ this build has nothing to apply it with, so nothing was spent"* — does
**not** fire. A row that says it does something, with no path to doing it,
is charged full price in silence. Measured cost of a failed cast: **20 Force
and 4 off the ceiling**, four times (m02: `159 → 139 → 119 → 99 → 79`; m01:
`151 → 131`).

### What this blocks — every clause you routed

| clause | state |
|---|---|
| fights **for** you; its old allies attack it; it attacks them | unreachable |
| a downed party member + a confused enemy standing is **not** a win | unreachable |
| a confused enemy gets **no** stand-at-1 | unreachable |
| returns to its original side when the duration expires | unreachable |
| a **second** creature of the same kind is refused | unreachable — see below |
| one sentient **and** one beast held at once | doubly unreachable |
| the sentient version does not affect droids | **works** |
| the beast version does not affect sentients | unreachable |

**The same-kind refusal is not merely untested — it can never fire.** The
guard at `12335` reads `cf.confusions.activeFor(...)`, and nothing ever
writes into `confusions`, so `activeFor` is always null. Measured: three
consecutive Force Confusion casts at **the same guard** on m02, each paid 20
Force, **none refused**. A recast should have hit ruling 2's
*"you already have … turned"* on the second attempt.

**The two-predicate design underneath is built and correct** — `partyWiped`
folds over `isParty` with a comment naming this exact case (*"A confused
enemy counted here would make a wipe stop being one … and would take the
party-exclusive stand-at-1 rule with it"*, `fight.dart:484–492`), while
targeting goes through `fightsWithParty` (`fight.dart:716`, `1062`, `1084`).
None of it can be exercised.

**Nothing can be a beast.** `kindOf` returns `droid`, `sentient` or null and
never `beast` (`power_target.dart:42`) — TEST 104, still true at this build.
So Beast Confusion has no legal target anywhere in the product, and the
"one of each kind" rule has only one kind to hold.

**The droid refusal does work**, and shows itself inline in the picker:

```
Force Confusion — 1 Guard · 2 Second Guard · 3 Battle Droid ⚠ Force Confusion does not affect a droid · esc
```

— subject to the classifier defect in §1 below, which it shares.

## 1. Force Distraction

### It loses sight of you — confirmed, as a matched pair

Two runs on the same board, from the same fresh save, with the **same
opening roll** (`d20 20 … 84 left`) so the die streams are in step. The only
difference is the order of two keystrokes inside turn 1.

| turn 1 | the guard's next turn |
|---|---|
| **cast, then move** 4 away | `out of reach — unarmed reaches 1 square and Whisper is 4 away` — 0 squares moved, no damage, three turns running |
| **move** 4 away, then cast | `closes 3 squares — 4 to 1 · rolled 17 … hit · 82 left` |

⚠ **The order is the instrument, and it is worth recording for whoever tests
this next.** `_look`/`observe` runs on **every player move**
(`play_screen.dart:6270–6334`), so moving before casting refreshes
`lastSeenAt` to the square you end on — and the distracted guard then walks
straight to you, looking exactly like a power that does nothing. My first
attempt got that answer and it was my fixture's fault, not the product's.

### It goes by where it last saw you, not where you are — confirmed, negatively

Same pair. `_knownPositionOf` returns the true position only
`if (known.seen)` (`8387`) and otherwise `lastSeenAt`. Measured as **3
squares of pursuit against 0**, everything else held.

⚠ **I could not stage a multi-square walk to a stale square, and the board
is not at fault.** `lastSeenAt` is only ever written when the **player**
moves, so the stale square is always the one I cast from — which, since the
cast needs the guard in view and the guard is what I am standing next to, is
always adjacent to the guard. Its walk to the last-seen square is
zero-length every time. What is confirmed is the half that can be
observed: it does **not** come to where I actually am.

### Adjacency suppresses rather than ends — confirmed

The distracted guard attacked me while I stood next to it, and went back to
ignoring me when I stepped away.

### Casting at it ends it outright — confirmed, both halves

Force Scream ended it (above), and then **stepping away did not bring it
back**:

```
guard.gd.01 closes 1 square — 2 to 1 · rolled 11 … hit · 83 left
```

Suppression restores, an attack does not. The two are distinguishable in
play and they behave differently.

### DEFECT — the droid exclusion silently fails on four of the five droid species

A matched pair: the same blueprint, the same tag, the same board, **one
field changed**.

```
species = "droid-battle"   Force Distraction · 8f — 159 → 151 · at droid.gd.02 · droid.gd.02 is distracted
species = "droid"          picker: 2 Battle Droid ⚠ Force Distraction does not affect a droid
                           cast refused · nothing spent
```

`kindOf` (`power_target.dart:42`) classifies a droid as
`id == 'droid' || chassis is non-empty`. The shelf carries **five**
`is_droid = true` species — `droid`, `droid-astromech`, `droid-assassin`,
`droid-battle`, `droid-remote` — and only the bare id matches. Four of five
are mind-affectable. (Re-checked today against the live shelf: the one
uncommitted `species.toml` edit is the Togruta blinded field and touches no
droid row.)

⚠ **The gate itself is sound** — it refuses by name, before the spend, and
costs nothing. The whole fault is in the classifier. And it is the **same
classifier Force Confusion's droid refusal uses**, so the same four species
will walk through that one too the moment confusion starts working.

### Two clauses with no code behind them

**"Still reacts to sound if you're noisy nearby" — not observable, and the
code says why.** `Senses.standard` sets `sight == hearing` from a single
number (Lodestar `perception.dart:53`) because no placement authors a
hearing range, so *heard farther than seen* cannot exist. And hearing does
not redirect a pursuer: `_knownPositionOf` gives the true position only when
`seen`. Hearing's only effect is that `known.any` is true, so the creature
does not fall back to omniscience. In play the guard sat within hearing at 4
and 5 squares across five consecutive turns and never moved once.

**"The target ends up facing away from you specifically" — nothing turns
it.** `_facing` has exactly **one writer**, `_faceFrom` at
`play_screen.dart:6246`, which takes the bearing of a step. Distraction
writes no facing, and facing is read at all only for a creature with an
authored `blindSpot`. A distracted guard that does not move does not turn.
This is not a gap in my fixture — there is no code that could make the claim
true.

## Also noticed

* ⚠ **A damaged save, reported by the product before I touched anything this
  session:** `1 save · 1 unreadable: Damaged save: it says it holds 569
  bytes of contents and the file has 529. Part of another save may have been
  written over it.` Reporting, not diagnosing. The message itself is good —
  it names both numbers and the likely cause.
* **Powers cannot be aimed outside a fight**, and the refusal names the
  wrong reason: `Force Distraction — there is nothing here you can see to
  aim it at`, printed with both enemies drawn on screen and one square away.
  The reason is that there is no encounter, not that nothing is visible.
* **Escape with no menu open leaves the board.** Cost me two reloads.

## Fixture

`tester-mind` on the shelf, named `0 Mind Bench (Tester)` so the library
carousel can reach it (four cards, no scroll). Boards `m01-guard` (one
sentient guard, one droid, 14 wide so the guard can be left behind) and
`m02-confuse` (two sentients and a droid).

⚠ **`blueprints/characters/droid.toml`'s `species` is the control field** —
flip it between `droid` and `droid-battle` to switch the two arms of the
classifier reading. ⚠ Neither board starts a fight on arrival; the encounter
begins by stepping into the guard.
