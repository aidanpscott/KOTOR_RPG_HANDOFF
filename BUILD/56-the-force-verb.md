# BUILD 56 — `PT-1477` / `PT-1478` / `PT-1479`

**One hyphen, one missing verb, and one test that was right about the only case it ever saw.**

---

## 1 — `PT-1477`: the hyphen

Re-extracted. The base type id was already the slug, so **the blueprint path did
not move and the bed needed no change.**

**27 of 28 arrays arm a character**, 1 is the Brawler's `NONE` — a value — and
**0 refuse.** Agent and Medic, organic and droid, are armed.

⚠ **Both tests went red when the ruling landed, which is them working.** They
asserted the defect on purpose so correcting the data could not pass silently.
The exact-match test is **kept**: the hyphen was fixed in the *document* rather
than absorbed by a matcher, and the old spelling now refuses like any other
name that is not a base type.

## 2 — `PT-1478`: a power can be cast

Your framing was the diagnosis: **not a value read wrongly, but no verb to read
it into, with both ends already written.**

| built already | and never joined |
|---|---|
| `ForcePool` · `cast` · `restore` · `sleep` · `meditate` | `play/` had **zero** mentions of `power` |
| `projectPlayState(forceCapacity:)` | the app called it **three times** and passed it in **none** |

- **`ClassRecord` now parses `force_die`**, which it never did.
- The pool is computed from `FORCE-POOL-01-v3 §2`, **shown**, and folded back
  from the log.
- **`f` opens the powers you took; a number casts one.** The line is the
  derivation — what was spent, what it cost the ceiling, and the effect.
- `encounter.ended` carries `force` and `force_ceiling`. The projection has
  read both since it was written and **nothing ever wrote them**, so a cast
  could not survive the fight it happened in.
- **Every refusal is a sentence.** `Tester` pressed nine keys against a screen
  that answered none of them; `f` with no powers, no pool, an unpriced power or
  too little in the pool each say which.

⚠ **And one I nearly shipped.** Restoring the ceiling from `PoolState.capacity`
would have **silently un-degraded the pool on every re-entry** — `capacity` is
the true maximum this call passes in and `workingMaximum` is the degraded
ceiling. *"You cannot rest off exhaustion"*, refunded by a field name.

### ⚠⚠ NEED: three Force classes have no Force die

`CLASSES-FORCE-PHB` states three — **Guardian d4, Sentinel d6, Consular d8** —
and **`sith_warrior`, `sith_assassin` and `sith_inquisitor` carry none.** That
is the corpus, not the extraction.

`forcePoolFor` **refuses rather than mirroring the Jedi.** A Sith Warrior
mirrors a Guardian in every other column and the mapping is obvious — and
obvious is not stated. **A Sith cannot have a pool until you rule it**, and the
screen says so instead of inventing one.

## 3 — `PT-1479`: true of the only case anybody gave it

`ledger_test`'s droid case asserted **"a droid has no gender"**. `§2` is
four-way: organic → GENDER, **Assassin/Battle → VOICE**, Astromech/Remote →
absent. **True for two bodies and false for two**, and the case has only ever
been given an Astromech.

⚠ **The product was already right.** `step_strip.dart` has read
`!result.isDroid || _hasVoice` since it was written. **It is the test that
encoded the wrong rule** — `PT-1466`'s family exactly.

The voiced half is now its own case, naming all four chassis, and was
**verified red with the product reverted to the rule the old test implied.**

⚠ And `model` is now recorded as a **fixture choice rather than a finding**:
the fixture passes `model: null`, so null is what the fixture chose and not
something the test has shown about droids. **A case given one value cannot tell
you what the other does.**

## Tests

**677 green** — Lodestar 303 · Lens 4 · Loom 119 · app 251.

## Still open

- ⚠ **Three Sith base classes have no Force die.**
- `§4a`'s grant offer reaching classes it does not name.
- `equipment.section` — a value used as a key.
- Conditional damage (`1d4 + 1d10 vs droid`) — costed at `BUILD 55`, unbuilt.
- 48 cells where a citation is load-bearing in a sentence.
