# TEST 113 — the anchors are right, and Force Body never attaches

**Build.** App **`398e037`** (PT-2391), built from `git archive`, compiling
against Lodestar **`81ed32af`** — the ref HEAD's *committed* `pubspec.lock`
pins. `check_shelf.py` clean: 29 rules files and 65 standard blueprints.

⚠ **The working tree was dirty when I started** and one of the modified files
is `pubspec.lock` itself: Coder has an uncommitted bump to Lodestar
`5c48700a` (PT-2392) in flight, alongside an edit to
`test/on_hit_condition_test.dart`. I tested the committed state, not the
in-flight one. The only difference between the two engines is
`conditions.dart` — PT-2392 adds `paralysed` as a twenty-first condition —
so it cannot touch either item in this batch.

**Verdict.** Item 1 is confirmed, with one correction to the routing: Force
Lightning is **caster**-anchored, not target-anchored. Item 2 is a **defect**:
Force Body's three tiers are inert in play. The arithmetic behind them is
correct and tested; the cast never attaches the effect, so nothing ever
reaches that arithmetic.

---

## How the boards were built

A cluster of enemies standing near the caster is caught identically whether
the sweep is centred on the caster or on the target, so it confirms nothing.
Every board here holds an enemy that the two anchors **disagree** about.

Two constraints shaped them:

* **A far enemy must still be in the encounter.** `_reachedBy` filters on
  `f.encounter.combatants`, so a mark beyond `_detectAtRange`'s ten squares
  would be spared for *not being in the fight* and the negative would be
  confounded. The far marks sit at 9–10.
* **The aim cannot be the discriminator for this family.** At HEAD
  `asksWho = p.anchor != 'caster'`, so a caster-anchored power never opens
  the picker and auto-aims. Deliberately aiming at a far creature — the
  obvious way to separate the anchors — is not something the interface
  permits for exactly these powers. So the discriminator is **direction**.

## 1a. Force Lightning — caster-anchored, and the routing has it the wrong way round

The shelf gives `force_lightning` **`cone_squares = 8`, `anchor = 'caster'`**,
and `_reachedBy` computes `radius = radiusSquares ?? coneSquares` — so a
"cone" is a plain distance from the caster. **There is no angle anywhere in
the implementation.**

Cast from (1,2) with three marks in the fight at 1, 4 and 9 squares:

```
Force Lightning · 14f — 263 → 249 · ceiling −3 to 260 · at near.lg.01
  near.lg.01 — 20d6 80        (1 square)
  mid.lg.02  — 20d6 61        (4 squares)
far.lg.03: 400 of 400 · Bench Caster: 122 of 122
```

| mark | from caster | from the far mark | caught |
|---|---|---|---|
| near | 1 | 9 | **yes** |
| mid | 4 | 5 | **yes** |
| far | 9 | 0 | **no** |

A target-anchored sweep of 8 centred on the far mark predicts the exact
opposite for *near* and *far*. Two of the three readings are inconsistent
with it, so no target-anchored reading fits.

**The routing's first bullet does not match the build.** It asks for "a
target with at least one other enemy within ~8-9 squares of *them*" and calls
it a 17m cylinder anchored on the chosen target. What the build does — and
what the shelf row says — is 8 squares from **you**. Worth noting that the
test as described would have *passed* anyway: a target and its neighbour both
standing near the caster are caught under either anchor.

## 1b. Death Field — the decisive one

Radius 5, `anchor = 'caster'`. Two marks on **opposite sides** of the caster,
6 squares apart from each other:

```
Death Field · 20f — 263 → 243 · ceiling −4 to 259 · at west.sp.01
  west.sp.01 — 20d4 41        (5 squares west)
  east.sp.02 — 20d4 53        (1 square east)
  Bench Caster — drained 53 · 122 → 122
```

Both caught. They are **6 apart, and the radius is 5** — so neither of them
can be the centre, whichever one is nominally aimed at. Only the caster can
be. This one does not depend on which creature the auto-aim picked.

The `heals: caster` arm fired too (drained 53, capped at full).

## 1c. Force Wave — consistent

```
Force Wave · 22f — 243 → 221 · at west.sp.01
  west.sp.01 — d20 4 = 4 vs 33 · stunned · 10d6 32
  east.sp.02 — d20 4 = 4 vs 33 · stunned · 10d6 43
```

Both sides caught and stunned from a radius of 7 centred on me. Weaker than
Death Field as a discriminator — at 6 apart the two marks are inside each
other's 7 as well — but consistent, and Death Field already settles it.

## 1d. The Scream family — the tier shift is real in the data and invisible in play

All three are `anchor = 'caster'`, and all three reduce to **distance 5**:
`force_scream` cone 5, `improved_force_scream` cone 5,
`master_force_scream` **radius** 5. Because `_reachedBy` computes
`radiusSquares ?? coneSquares`, a cone and a sphere of the same number are
the same set of squares.

Both cast on **turn one**, from the same square, against identical untouched
positions (marks at 1 and 6):

```
Force Scream        ·  8f — at in.sc.01 · in.sc.01 — 3d6 13 · −2 to all six abilities
                       out.sc.02: 400 of 400
Master Force Scream · 24f — at in.sc.01 · in.sc.01 — 7d6 27 · −6 to all six abilities
                       out.sc.02: 400 of 400
```

Identical catch sets. The tiers differ in dice (3d6 → 7d6) and in penalty
(−2 → −6), both observed; **the shape does not differ at all**, so the
cone→sphere inversion has nothing in play that could distinguish it. It is
correct in the data and unobservable in the product.

⚠ My first attempt at this comparison was invalid and I discarded it: I ended
a turn between the two casts, the far mark walked five squares closer, and
Master Force Scream "caught both" for no reason but its new position.

## 1e. The picker, and the enemy-only filter

* **The picker.** At HEAD the gate is `asksWho = p.anchor != 'caster'`.
  Every power named in the routing — Lightning, Wave, Death Field and all
  three Screams — is `anchor = 'caster'`, so **none of them opens a target
  menu, correctly**: a caster-anchored sweep has no creature to centre on.
  The routing's last bullet asks to confirm the menu opens for exactly the
  family that must not ask. (The menu opening for a *target*-anchored power
  is real — I saw Horror and Fear open it in TEST 112's follow-up — it is
  simply not these powers.)
* **Enemy-only.** The player sat at the **exact centre** of four
  caster-anchored blasts — Lightning, Death Field, Force Wave, two Screams —
  and finished every one of them at `122 of 122`, unstunned. Distance 0 is
  the strictly hardest case for a membership filter, harder than the ally the
  routing suggests (an ally would need a party-join event; the player needs
  none and is closer).

## 2. Force Body — the whole mechanism is inert

**Observed, twice, at two different tiers:**

```
Force Body        · 15f — 239 → 224   (tier 1, 50%)
  then Master Force Scream · 24f — 224 → 200 · Bench Caster: 122 of 122

Master Force Body · 25f — 200 → 175   (tier 3, 30%)
  then Master Force Scream · 24f — 175 → 151 · Bench Caster: 122 of 122
```

Under tier 1 the 24-cost power should have taken 12 from the pool and 12 from
vitality; under tier 3, 8 and 8. It took **the full 24 from the pool and
nothing from vitality**, both times.

**Cause.** The attachment is nested inside a guard it can never satisfy:

```dart
final mods = p.modifiers;                     // play_screen.dart:9802
...
if (mods.isNotEmpty) {                        // :9997
  ...
  if (p.forceBodyPercent case final pc? when caster != null) {   // :10008
    caster.forceBody = [ForceBody(percent: pc, ...)];
  }
```

`caster.forceBody` is assigned in exactly one place in the app, and it is
inside that block. **No Force Body row carries `modifiers`** — all three have
`modifiers = None` and only `force_body_percent` — so `mods` is always empty,
the block never runs, `forceBodyPercent` returns null, and `splitCost` hands
back the whole cost from the pool.

**Both sub-claims are unreachable for the same reason**, not merely
unconfirmed:

* *Replaces rather than stacks* — the single-element `caster.forceBody = [...]`
  assignment that implements it is in the same unreached block.
* *Refuses rather than killing you* — that branch is guarded by
  `if (price.fromVitality > 0)`, and `fromVitality` is always 0. I built a
  frail caster to reach it and did not run it: there is nothing there to
  reach.

**Why the suite is green.** `force_body_is_paid_from_two_purses_test.dart`
calls `splitCost(...)` directly, with the percentages read off the shelf
rows. The arithmetic it checks is correct — I verified the intended numbers
by hand: at a cost of 24 the tiers give 12/12, 10/10 and 8/8, each half
`ceil`ed independently. Nothing in it goes through a cast, so nothing can see
that the cast never attaches the effect. The unit is right and the seam is
empty.

**What a player meets:** a power that costs 15, 20 or 25 Force, prints its
own prose, and changes nothing whatsoever about the next cast.

## Noticed in passing — a measurement, not an anecdote

`⚠ <power> does not say what it may be aimed at` printed on Lightning, Wave
and both Force Bodies. It is not a handful of rows: **84 of the 106 powers
carry no `targets` field, and 38 of those are enemy-aimed**, so the warning
fires on cast for 38 powers. The product announcing the gap is right; the
gap is large. (Same warning I reported on Force Mire in TEST 112 — it is
family-wide, not a one-off.)

## Fixtures

`tester-anchor` on the shelf: three boards and one 400-vitality mark
blueprint. Saves `t113-*` written one at a time. The caster is a Consular 20
whose pool came up `263 of 263`, matching the documented formula exactly —
an incidental re-confirmation of `PT-2215`'s two bands.
