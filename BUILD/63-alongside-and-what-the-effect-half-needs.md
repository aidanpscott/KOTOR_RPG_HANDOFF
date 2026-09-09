# BUILD 63 — `TEST 013`: alongside, and what the effect half actually needs

**No code this slice.** Everything `TEST 013` names that is mine was built at
`BUILD 62` — the cast menu marks what you cannot afford, and `Tester`'s two
corrected counts match `starting_weapon_test` exactly (27 armed, **1**
barehanded — the Brawler's `NONE` — 0 refused).

---

## ⚠ Should `excludes` come first or alongside? **Alongside — and neither is first.**

**The first thing is a target.** Casting has none:

    void _cast(PowerRecord p)      // ← there is no target parameter

You press `f`, pick a number, and the pool moves. **There is nothing for a gate
to gate and nothing for an effect to land on.**

- `excludes` **first** is a gate with no input — untestable, and invisible on
  screen. It would pass every test and change nothing a player sees.
- effects **first** pushes a droid it should not push.

So they belong in **one slice whose subject is the target**: choose one, check
eligibility, then resolve. `excludes` landing at `PT-1486` was right *because*
it is data rather than behaviour — **it was the half that could land early
without pretending to work.**

### ⚠ And the gate must answer SILENT for most of what a player can cast

| powers open at 1st level | **22** |
|---|---|
| with `excludes` | 4 |
| with `targets` | 3 |
| ⚠ **silent on both** | **15** |

**Seven of twenty-two.** A gate that treated silence as permission would be
wrong about fifteen; one that treated it as refusal would be wrong about
fifteen the other way. **Silent has to stay a real third answer** — which is
the whole reason `excludes` was transcription and not inference.

---

## ⚠⚠ And the effect half is NOT the same kind of work

`targets` and `excludes` were cheap because the prose states them in a **fixed
phrase**. The effect half does not, and the numbers say so.

| the prose states | powers | |
|---|---|---|
| a duration | 67 | 64% |
| a save | 53 | 51% |
| damage dice | 25 | 24% |
| a condition | 11 | 10% |
| movement | **3** | 3% |

⚠ **The 53 saves are written in NINETEEN distinct phrasings**, and at least
three are genuine formulas rather than wording:

    DC 5  + the character's level + Wis + Cha     the majority
    DC 10 + the attacker's level  + Wis + Cha     ⚠ the Force Scream chain, ×3
    DC 5  + FORCE levels          + Wis + Cha     ⚠ Affliction, Contagion, Plague

⚠ **And one is not a save at all.** `Force Resistance` is an **opposed roll** —
*"d20 + his or her level versus a DC of 10 + the defending character's
level"* — a different mechanic wearing the same words.

**So the effect half needs authored columns before any code**: save type, DC
base, DC scale, damage, duration, condition. Extracting it from prose would be
inference across nineteen phrasings, and the two exceptions are exactly the
rows a normaliser would flatten. ⚠ **That is a rules-authoring slice, and it
is yours, not mine.**

⚠ And `movement` at **3 of 104** is worth seeing: Force Push's *"pushed back 4
metres — 2 squares"* is nearly unique, so building a push system serves three
powers. **The promise a player reads is mostly damage and duration.**

## Still open

- ⚠ **The effect half** — needs authored columns first. The cost half is
  complete and the prose promises an outcome.
- ⚠ **`PT-1484` is unblocked** by the Guardian confirmation.
- `PT-1485`; 45 annotation cells; conditional damage; a citation assembled at
  runtime.
