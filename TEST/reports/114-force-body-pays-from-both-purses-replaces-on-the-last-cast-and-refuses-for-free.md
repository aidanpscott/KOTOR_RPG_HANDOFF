# TEST 114 — Force Body pays from both purses, replaces on the last cast, and refuses for free

**Build.** App **`98bd2d4`** (PT-2394), tree clean, built from `git archive`.
Committed and working `pubspec.lock` agree on Lodestar **`2b9c9140`**, and
that is the checkout `package_config.json` compiles against. `check_shelf.py`
clean: 29 rules files and 65 standard blueprints.

**Verdict.** All three items confirmed. Vitality genuinely moves, every tier
splits at the rate its shelf row states, the lower tier takes over rather
than stacking, and the refusal costs nothing.

**On the diagnosis:** TEST 113 named one of the two gates — the
`if (mods.isNotEmpty)` wrapper around the assignment. The upstream one,
`_applyPower` returning early for a power with no condition, penalty, damage,
heal, immunity, skill bonus or modifier, was Coder's find, and it would have
stopped the attach on its own even with the second removed. The observable
was the same either way, but the fix needed both and my report would have
bought only half of it.

---

## 1. Both purses move, at the rate each tier states

One known-cost power — Master Force Scream, **24f** — cast under each tier in
turn. The pool delta is read off the cast line's own arrow, the vitality
delta off the vitals line, and **both are taken inside a single turn**:
enemies act only after the turn ends, so nothing they do can be mistaken for
a payment. (Across the whole run the vitality deltas were exact to the point,
so no enemy blow landed on the caster at all.)

| Force Body running | pool | vitality | total | vs the 24 it costs |
|---|---|---|---|---|
| none — the control | −24 | 0 | 24 | full price, pool only |
| Force Body, 50% | **−12** | **−12** | 24 | same total, split evenly |
| Improved, 40% | **−10** | **−10** | 20 | cheaper |
| Master, 30% | **−8** | **−8** | 16 | cheaper |

```
control  Master Force Scream · 24f — 263 → 239 · Bench Caster: 122 of 122
50%      Master Force Scream · 24f — 224 → 212 · Bench Caster: 110 of 122
40%      Master Force Scream · 24f — 202 → 192 · Bench Caster:  90 of 122
30%      Master Force Scream · 24f — 182 → 174 · Bench Caster:  72 of 122
```

Every figure is `ceil(24 × percent / 100)` per purse — 12, 10 (from 9.6) and
8 (from 7.2), each half rounded up independently, which is the rule
`splitCost` documents as the project's own decision rather than the
document's. Tier 1 splits the full price and the two higher tiers genuinely
reduce the total, exactly as routed.

The control matters here: the same power on the same build with no Force Body
running took the whole 24 from the pool and no vitality, which is precisely
the reading TEST 113 got at *every* tier.

## 2. Replaces, and it is the last cast that governs

With **Master Force Body (30%) already running**, I cast **Force Body
(tier 1, 50%)** and then the same 24f power:

```
Master Force Scream · 24f — 169 → 157 · Bench Caster: 55 of 122   (was 67)
```

**−12 and −12: the 50% rate.** Not 8/8, which is what a 30% still in force
would have charged, and not any stacked figure. The lower tier took over.

⚠ **One latent divergence worth recording, not a defect.** Two rules could
decide this and they do not agree. The app replaces at the assignment —
`caster.forceBody = [ForceBody(...)]`, a single-element list — so the newest
cast wins. Lodestar's `forceBodyPercent` folds the list by the **smallest**
percent, documented as *"the best tier wins, and best is the smallest"*,
which would have kept 30%. The two never conflict today only because the list
can never hold more than one element. If a second producer ever appends
instead of replacing, the fold would silently keep the better tier while the
assignment's intent is that the last cast governs — and the observable
difference is exactly the reading above.

## 3. The refusal, and it costs nothing

Vitality was drained by repeated casting at 12 a time — `55 → 43 → 31 → 19 →
7`, each step exact — leaving **7 vitality** against a 24f power needing 12:

```
Master Force Scream — Force Body would take 12 vitality and you have 7 · nothing spent
```

And *nothing spent* is verified rather than taken on trust: the vitals line
reads `Bench Caster: 7 of 122 · force 109 of 175` both immediately before and
immediately after the attempt. **Neither purse moved, and the caster is
alive.** The guard is `<=`, so a caster with exactly 12 would also be refused
rather than dropped to zero.

## What this closes

Items 2 and 3 had never been reachable — both sat behind the dead gates, one
in the same unreached block and one downstream of a `fromVitality` that was
always 0. This is their first real confirmation, and both hold.

## Fixtures

`tester-anchor` on the shelf, `b02-sphere` board, save `t113-sphere`
(Consular 20, pool 263, vitality 122). The frail caster I built for the
refusal was not needed in the end: draining the level-20 one through five
casts reached the refusal more cleanly, because every step of the drain is
itself a reading.
