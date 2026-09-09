# BUILD 66 — `PT-1491`: the gate stops blessing on half the question

**702 green** — Lodestar 306 · Lens 4 · Loom 120 · app 272.

---

## The `affects` gap, fixed before the column exists

`targets` and `excludes` answer **what may be affected**. `affects` answers
**who it is aimed at**. The gate had only the first and said `permitted`
anyway — so it would have let you Force Push an ally and Heal a trooper with
equal confidence.

⚠⚠ **It will not say `permitted` on kind alone now.** A kind that agrees
returns **silent**, with the reason: *"does not say whether it is aimed at a
friend or an enemy, so only its kind could be checked."*

⚠ **And it tightens the day `PT-1489` authors the column** — a test builds the
authored shape by hand, so that day is a **change rather than a discovery**:

    Heal · affects "ally" · at an ally      → permitted
    Heal · affects "ally" · at the trooper  → EXCLUDED, and says why

An unknown **relation** is silent for the same reason an unknown **kind** is:
the gate declines rather than blessing on half. The cast states
`relation: enemy`, because the only target is the thing you are fighting; when
a power can be aimed elsewhere, that is where the choice arrives.

---

## ⚠ Batch one: 22 is enough — **plus nine rows, and I measured which**

Twelve shapes the columns must carry, counted in the 22 and in all 104.
**Ten of twelve are exercised**, several by a single row, which is enough to
find a shape that does not fit.

⚠⚠ **But the two it misses are not random.**

| ⚠ | in the 22 | in all 104 |
|---|---|---|
| **heals — i.e. `affects`** | **0** | 6 |
| `damage_scale` character levels | **0** | 3 |

**No row in the 22 heals**, so `affects` would read `enemy` on all 22 and **the
column would look unnecessary** — the one I argued hardest for, untested by the
batch chosen to test the shape. `damage_scale` would be `force_levels` on all
22, so a second value would never be written.

**A shape that survives 22 rows chosen by REACHABILITY is not the same as one
that survives 22 rows chosen to EXERCISE it.**

### So: 31 rows, and the nine are named

`Heal` · `Improved Heal` · `Master Heal` → `affects = "ally"`;
`Dark Healing` → `"self"`; the three that scale on character levels; and

⚠ **`Death Field` and `Drain Life` first of the nine.** They **harm an enemy
and heal the caster**, and may not fit `affects` at all. **I would rather learn
that on row 23 than row 104** — and `not_modelled` is a perfectly good answer
there.

## Still open

- The columns — batch one is specified, and the shape is filed.
- `PT-1484` unblocked; `PT-1485`; 45 annotation cells; conditional damage.
