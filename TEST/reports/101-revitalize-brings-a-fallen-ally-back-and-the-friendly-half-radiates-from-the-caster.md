# TEST 101 — Revitalize brings a fallen ally back, and the friendly half radiates from the caster

**Build under test.** KOTOR-RPG-APP `6306f5d` *"PT-2290: a healing power deals no damage"*, working
tree clean. Lodestar `c9ddd86`; `pubspec.lock`'s resolved ref matches the pub-cache checkout that
compiled (`Lodestar-c9ddd867…`, `Lens-32b77e3b…`). `fresh.py --debug --build` printed
`✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29 rules files, 65 standard
blueprints. Built from a `git archive` of `6306f5d` into my own tree.

Both routed items confirmed. Fixture: `ally-ward`, two new areas.

---

## 1. Revitalize revives a genuinely fallen ally, at all three tiers

The ally was dropped **in play** — a `never-player` brute with a 2d8 two-attack weapon ground a
60-vitality companion down over four rounds while the caster stood clear. No authored starting
state below 1 vitality is involved.

| tier | cost | before → after | restored | lines printed |
|---|---|---|---|---|
| Revitalize | 12f | **−6 → 4** | 10 | one heal line, no damage line |
| Improved Revitalize | 20f | **−13 → 12** | 25 | one heal line, no damage line |
| Master Revitalize | 28f | **0 → 50** | 50 | one heal line, no damage line |

Each came back to **positive vitality** and back on its feet. Master's reading is taken from
exactly `0`, the `VitalityState.down` boundary.

```
Revitalize · 12f — 159 → 147 · at ward-fallen.fallen.01 · ward-fallen.fallen.01 — healed 10 10 · -6 → 4
Improved Revitalize · 20f — 147 → 127 · at ward-fallen.fallen.01 · ward-fallen.fallen.01 — healed 25 25 · -13 → 12
Master Revitalize · 28f — 127 → 99 · at ward-fallen.fallen.01 · ward-fallen.fallen.01 — healed 50 50 · 0 → 50
```

**The caster was never touched.** Improved and Master Revitalize are radius 7 and the caster stood
inside their own radius, which is precisely where TEST 100's defect struck: there, one Improved
Revitalize took 25 off every standing party member including the caster. Here the caster read
`74 of 74` before and after every one of the three casts.

### Revitalize on a standing ally

```
Revitalize · 12f — 99 → 87 · ceiling −2 to 142 · at ward-fallen.fallen.01 · This power allows the
Jedi to rekindle the life energies of any non-droid fallen ally…
```

The ally sat at `37 of 60` before and `37 of 60` after. **No damage line and no heal line** — the
`only_if_fallen` gate skips the heal and there is no longer a damage half to leave behind. This is
the exact case that was defective and it is now inert, as specified.

⚠ One presentational note, not a defect and not something I can call: the pool is still spent and
the player is told nothing about why nothing happened. With no outcome to report the status line
falls back to printing the power's full effect prose, which reads as though something occurred.

### And a Heal now moves vitality upward

The other half of `PT-2290`. In TEST 100 every heal netted exactly zero, and the heal's *before*
was always exactly the amount below the pre-cast frame. Measured against an independent pre-cast
frame this time:

```
frame before the cast   ward-fallen.fallen.01: 18 of 60
Heal · 8f — at ward-fallen.fallen.01 · ward-fallen.fallen.01 — healed 5 +4 cha +4 wis +12 level 25 · 18 → 43
```

The pre-cast frame and the heal's `before` **agree at 18**. A real +25, with no intermediate dip.

---

## 2. The friendly half radiates from the caster — `PT-2288` confirmed

`PT-2288` is at this commit (`a4b73ad`): the non-ally branch of `buffed` now reads
`_reachedBy(p, at, asParty: true, centreOn: _me?.handle ?? '')`.

A buff names nobody in the UI — both halves print `'the party — …'` — so the reading is taken off
the **terms of an ally's attack roll**, and the fixture is a corridor one tile high with the enemy
standing between the caster and the ally:

```
(0,0) caster        (6,0) foe-off  <- the aim        (7,0) ally-off  HENCHMAN
```

Ally is **7 from the caster** and **1 from the aim**. Improved is radius 5, Master is radius 7. Both
casts were made from the identical board, with positions screenshotted at each cast and confirmed
unchanged.

```
Improved Battle Meditation · 20f · at foe-off.med.01 · the party — +2 attack · +2 damage · +2 will
                                                    · foe-off.med.01 — -2 attack · -2 damage · -2 will
  ally-off.med.02: unarmed · rolled 20 — d20 15 + attack 3 + Strength 2 ·
                   needed 18 — hit · damage 5 — 1d3 3 + Strength 2

Master Battle Meditation · 28f · at foe-off.med.01 · the party — +4 attack · +4 damage · +4 will
                                                   · foe-off.med.01 — -4 attack · -4 damage · -4 will
  ally-off.med.02: unarmed · rolled 21 — d20 12 + attack 3 + Strength 2 + power 4 ·
                   needed 18 — hit · damage 9 — 1d3 3 + Strength 2 + power 4
```

**Radius 5 reached the ally with nothing. Radius 7 put `power 4` into both the attack terms and the
damage terms**, exactly the authored `+4 attack` / `+4 damage`.

Three readings follow, and each rules something out:

- **The friendly half honours a radius at all.** The same ally on the same square was in for one
  cast and out for the other.
- **The radius is measured from the CASTER.** From the aim the ally is 1 square away, so it is
  inside radius 5 *and* radius 7 — a friendly half centred on the target would have buffed it in
  both casts, and a friendly half with no geometry (the pre-`PT-2288` behaviour) would also have
  buffed it in both. Only caster-centring produces the split observed.
- **Line of sight is not the explanation.** A creature stands between the caster and the ally in
  both casts, and `blastReaches` filters on sight from the centre — but sight is identical across
  the pair, and Master reached the ally. The radius is the only variable left.

The **enemy half centres on the target** in the same casts: both debuffed `foe-off.med.01`, the
square aimed at, and in the earlier four-creature build of this fixture a second enemy standing 7
squares from the aim was left alone while the aimed one was debuffed. The two halves of one cast
are centred on different squares, which is the whole of what `PT-2288` claims.

⚠ Both tiers print a warning of their own: *"Improved Battle Meditation does not say whether it is
aimed at a friend or an enemy, so only its kind could be checked."* That is the two-sided shape
being reported honestly, not a fault — noting it so it is not read as new.

---

## Fixture notes — four hazards, three of which invalidated a build of this test

- ⚠⚠ **A companion walks to the player every round, and "Wait here" does not hold it in combat.**
  Three successive builds of the Battle Meditation fixture were thrown away to this: the ally was
  placed outside the radius, the fight opened, and the ally closed on the caster before the cast,
  so any reach it showed was because it had **moved**. Standing still does not help — it comes to
  you. The corridor above exists only because the enemy standing between them is the one thing
  that holds the separation. This is the same hazard that spoiled the first radius reading in
  TEST 100; it is worth knowing it cannot be worked around by keeping the caster still.
- ⚠ **`_enemyTurns` overwrites the status line for every actor in a round**, so only the LAST
  non-player actor can be read. Reading an ally at all required arranging for it to be last —
  a 1-vitality creature opens the fight from the arrival square and is struck down, which both
  avoids walking the caster and clears the turn order.
- ⚠ **A companion joins the party and travels between areas.** The previous run's ally arrived in
  the next fixture and appeared in its turn order. Re-authoring the save from scratch is what
  clears it; deleting the app's rewritten copy first matters, because it saves on exit.
- ⚠ **A Load Game row's hit area is the width of its text.** A short character name ("Aurist")
  silently swallows a click that lands where a longer name would have been.

`ally-ward` now carries four areas and no doors between them, which is the whole of its
"4 problems" — one connectivity complaint per area, the same benign shape as `force-gate` in
TEST 098.
