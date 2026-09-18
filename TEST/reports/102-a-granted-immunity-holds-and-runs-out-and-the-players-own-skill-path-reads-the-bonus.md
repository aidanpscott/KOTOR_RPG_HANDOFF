# TEST 102 — A granted immunity holds and runs out, and the player's own skill path reads the bonus

**Build under test.** KOTOR-RPG-APP `2b9f7aa` *"PT-2294: a power helps a skill, on both of the paths
that read one"*, working tree clean. Lodestar `2d5d696b` — `package_config.json` resolves to
`Lodestar-2d5d696b39b8ede3aa5507432cc0b699410a11e0`, which is the checkout I read the engine from,
and `Lens-32b77e3b`. `fresh.py --debug --build` printed `✓ FRESH — built from exactly this source`.
`check_shelf.py` green: 29 rules files, 65 standard blueprints.

Both routed items confirmed. Poison source throughout is `geno_blade`, the GenoHaradan Poison
Blade — `OnHit (ItemPoison: POISON_DAMAGE_MILD) 14` on a `vibrosword` base.

---

## 1a. Breath Control — confirmed, control and test on one creature in one fight

`attack.dart` returns early when the target is immune and **deliberately rolls no save**, so the
immune case is distinguishable from a made save rather than merely quieter than one. Both readings
came off the same character, the same weapon and the same fight:

```
round 1  poison — d20 16 + fortitude 8 = 24 vs 14 · resisted        <- a save IS rolled
round 3  poison — d20  5 + fortitude 8 = 13 vs 14 · takes hold      <- the poison LANDS

Breath Control · 6f — 159 → 153 · ceiling −1 to 158 · at Toxin
  Toxin — immune to poison for 80 rounds

round 4  GenoHaradan Poison Blade: poison — the target is immune    <- no save rolled at all
```

The control is not "the poison might have landed" — it did land, on this character, three rounds
before the cast. After the cast the same weapon on the same target produces the early-return
string and consumes no die.

⚠ I died on that last blow (total party defeat at −2 vitality). The reading is unaffected — the
immune note is printed by the same strike that killed me — but it is why this run stops there.

## 1b. Knight Valor's poison immunity, granted mid-fight — confirmed, **and it runs out**

This is the snapshot question. `Fight.immuneEffects` is built when the fight is made, off what
everybody is wearing, so the map predates the cast by construction. `immuneEffectsFor` now unions
it live off the combatant:

```dart
Set<String> immuneEffectsFor(String handle) => immunitiesStanding(
      encounter.combatants.where((c) => c.handle == handle).expand((c) => c.immunities),
      worn: immuneEffects[handle] ?? const <String>{},
    );
```

Read on a **companion**, not the caster — Knight Valor is `affects: ally` radius 7 and covers the
caster too, so a reading taken on the caster could not be told apart from Breath Control's grant.
The readout is the party sidebar, which colours a poisoned creature's bar green.

Same board, same creatures, one variable — whether the cast happens:

| run | cast | Ward Tox after | bar |
|---|---|---|---|
| control | none | 3 rounds, 107/120 | **green — poisoned** |
| test | Knight Valor, after the fight opened | 5 rounds, 104/120 | **teal — not poisoned** |

```
Knight Valor · 15f — 159 → 144 · ceiling −3 to 156 · at ward-tox.val.01
  the party — +3 saves · the party — +3 str 6r · +3 dex 6r · +3 con 6r
  the party — immune to poison for 6 rounds
```

**And the clock runs.** Continuing the same fight past the six rounds, on the same creature:

- round 5 — `ward-tox.val.01: ... + Strength 1 · damage 4 — 1d3 3 + Strength 1`, bar teal
- round 10 — `ward-tox.val.01: ... + Strength 0`, the `+3 str` from that same cast has **expired**
- round 12 — 62/120, bar **green again — poisoned**

So one creature in one fight shows all three states: poisoned without the grant, not poisoned
while it stands, and poisoned again once it lapses. The `+3 str` reverting is what dates the
expiry independently of the poison dice — without it, "still not poisoned" and "the clock never
ran" would be the same reading.

⚠ A reading hazard worth knowing: below roughly a third vitality the bar switches to the
near-death colour, which by design outranks the poison colour (`party_sidebar.dart:498` — *"poisoned
and nearly dead are two facts and the one that kills you wins"*). At 44/120 Ward Tox showed pale,
not green, while still poisoned. The round-12 reading above is taken at 62/120, above that point.

---

## 2. Force Camouflage's Stealth bonus, on the player's own path — confirmed exactly

`_hide` rolls the player through `_rank('stealth')`, which is the reader that does **not** go
through `Fight` and the one `PT-2294` names as the silent-failure risk. The line prints only the
total (`seen — your 16 against their 58`), so a single roll cannot separate the die from the rank.

It did not have to be statistical. Both totals come from the fight's one injected die source, and
the watcher's total is printed too — so **the watcher's number is an alignment key**. Three runs on
the same board, same save, same watcher (Awareness 40, so the check is unwinnable and the roll can
be repeated every turn):

| watcher's total | control | Improved (+4) | Master (+8) |
|---|---|---|---|
| 44 | 15 | **19** | **23** |
| 59 | 12 | **16** | **20** |
| 60 | 20 | **24** | **28** |
| 49 |  9 | **13** | **17** |

Four exactly-aligned pairs per tier, every one off by exactly the authored bonus. The watcher's
die matching to the unit is what proves the rows are the same roll rather than a coincidence of
averages.

An independent cross-check falls out of it: the Improved and Master runs produced the *same*
watcher sequence (50, 44, 59, 60, 49, 42), so the two tiers compare row for row without any
alignment argument — `17,23,20,28,17,27` against `13,19,16,24,13,23`, **+4 on all six**.

The grant is named on the player at the cast site:

```
Improved Force Camouflage · 14f — 159 → 145 · at Stealther · Stealther — +4 Stealth
Master   Force Camouflage · 20f — 159 → 139 · at Stealther · Stealther — +8 Stealth
```

### ⚠ The companion half cannot be reached from play, so "both match" could not be tested

`skill_bonus` appears on exactly two rows in the corpus and **both are `affects = "self"`**:

```
improved_force_camouflage   affects=self   [('Stealth', '4')]
master_force_camouflage     affects=self   [('Stealth', '8')]
```

The grant site reads `final granted = side == 'self' || side == 'ally' ? caught : []`, and for a
self-aimed power `caught` is `[at]`, which `_cast` has already fixed to the player. So no cast in
the product today can put a skill bonus on a companion, and the `Fight.skillRankFor` half of
`PT-2294` — real code, and correct as far as I can read it — has no caster-reachable route.

This is not a defect and I am not filing it as one; both halves were right to change together. But
it means the asymmetry can only be observed from one side at present, and the side that IS
reachable is the one the ruling calls the risk: *"a grant wired into only Fight would have worked
for every companion and silently failed for the one character who can cast this power."* That
character is the one measured above.

⚠ A source reading I did **not** test: the grant strips only same-id rows
(`if (b.from != p.id)`), so holding Improved and Master together would appear to stack to +12
rather than replace. The Camouflage prose says nothing about replacing — unlike the Valor chain,
which states it outright — so this may well be intended. Flagging it as unverified, not as a
finding.

## Not tested

- Master Valor's poison immunity specifically. Same `immunity` row shape and same cast path as
  Knight Valor at a different magnitude; I stopped once the mid-fight grant and its expiry were
  both established.
- Breath Control's 80-round expiry. The clock mechanism is confirmed by Knight Valor's six rounds
  above; 80 rounds of a live fight was not a good use of the slice.
