# BUILD 62 — `PT-1486`: `excludes`, and a third kind of field

**690 green** — Lodestar 303 · Lens 4 · Loom 120 · app 263.

---

## 1 — `excludes` transcribes the negative

**25 powers carry it.** A question about droids is now answerable for **41 of
104 rather than 17**, and **nothing was inferred**.

| | before | after |
|---|---|---|
| excluded — the prose says so | — | **25** |
| permitted — the column says so | 17 | 16 |
| ⚠ silent | 87 | **63** |

### ⚠ Three sentences are deliberately NOT transcribed

- **`Force Whirlwind`** — *"does not affect droids **equipped with energy
  shield hardware**"*. A **conditional** exclusion; recording it as a blanket
  one would over-claim.
- **`Force Static Field`** — *"Harmless to organics"*. `organics` is **not one
  of the four kinds**, and mapping it to sentient+beast is the inference this
  field exists to avoid. Its `targets: droid` already says it positively.
- **`Force Contagion`** — a **quotation** of the mod's own text, not a rule
  this document states.

⚠ **And a kind is never in both.** Where the column and the prose would
disagree, the record carries a note saying so rather than picking one. **No
power does today** — which is worth knowing, because it means the two halves
have never contradicted each other.

## 2 — `flavour`

    value      THE KEY                teaches = "Athletics"
    flavour    RENDERED, never a key  "they marched it into you…"
    note       NEVER rendered         an aside about the document

`professions.teaches` is the skill name and nothing else; ten flavours moved to
`teaches_flavour`, and the Equipment screen shows them **beside** the aptitude
rather than inside it. `Mysterious Stranger`'s `ANY SKILL` has no dash and
stays a value.

**The extractor transcribes and the test verifies** — every head resolves to a
real skill, 10 of 10, which is the check that catches a future row whose head
is not one.

⚠⚠ **And `flavour` is NOT exempt from `check_annotations`.** It is rendered, so
a citation in one reaches a player exactly as a citation in a value does. Only
`note`, `ruling` and `*_superseded_by` are exempt, **and they are exempt
because nothing shows them.**

---

## `PT-1487` arrived mid-slice

**Confirmed against my own work:** the Guardian resolves the open question the
same way I read it — *a build difference, not a class path* — and `Tester`'s
simulation of the resolver over both tables found **exactly one array that does
not arm, the Brawler's `NONE`**, which is what `starting_weapon_test` asserts
(27 armed, 1 barehanded, 0 refused). The other four were `PT-1477`'s.

**Taken now, because it is small and named:** ⚠ **the cast menu marks what you
cannot afford.** This app disables with a reason on every other screen; the
*pick* already refused with the numbers and the *menu* said nothing, so the
only way to learn a power was out of reach was to try it. The nine unpriced
powers say *"no cost authored"* rather than showing a blank where a number
goes.

⚠ **The test casts twice before looking** — a Consular's pool is 12 and Force
Push costs 6, so one cast still leaves enough and the fixture has to actually
run dry for the assertion to mean anything.

**Not taken:** the cast pays and does nothing. `Tester` filed it as the next
question rather than a regression, and that is right — the verb landed at
`PT-1478` and nothing claimed the effects did.

## Still open

- ⚠ **`PT-1484` is unblocked** — the Guardian confirmation has landed.
- ⚠ **The cast has no effect half.** The cost derivation is complete and the
  prose promises an outcome; `1d6 per two Force levels` reads as a promise.
- `PT-1485` — an Acolyte who is not a Force user.
- 45 annotation cells; conditional damage; a citation assembled at runtime.
