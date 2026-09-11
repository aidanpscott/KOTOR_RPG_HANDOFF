# BUILD 136 — three guards over a gap that was not reachable

`PT-1715`, closing `PT-1713`'s character half before companions starts
underneath it.

---

## 1 · ⚠⚠ THE SHIPPED DATA WAS ALREADY CLEAN, AND THAT IS THE FINDING

I reported this gap in `BUILD 135` and expected to find a droid being handed a
blade. **It cannot happen today**, and I measured all three ways it might:

| | |
|---|---|
| the nine droid arrays | **every one names a ranged weapon** — Blaster Pistol, Carbine, Ion Blaster, Hold Out |
| the 21 profession grants | **not one is a weapon at all** — helmets, bands, slot-fillers |
| a droid on a class with no droid array | `arrayFor` returns **null** — no organic fallback, so no weapon |

**⚠ SO THIS SLICE IS GUARDS, NOT A REPAIR**, and saying so is the point: a
report that claimed a fix would be claiming a defect that was not there.

## 2 · ⚠ What the rule's character half actually needed

`PT-1713` closed the rule for **packages**. A blueprint is one door into the
game and **chargen is the other**, and nothing checked it.

`equipmentPayload` now refuses to arm a droid with a non-ranged weapon and
**records why**, in the vocabulary that already exists for exactly this —
`weapon_unresolved`'s own note: *"a save that cannot arm you should be able to
say so years later."*

**⚠ THE SENTENCE NAMES THE WEAPON IT REFUSED.** One that does not say which is
half a sentence, and the mutation that removes the name fails the acceptance.

**⚠ AND A LIGHTSABER IS CLOSED TOO, NOT BECAUSE IT IS MELEE** — `§12.5` keeps
it its own kind and `FEATS-UNIVERSAL-01` closes it separately. `droidMayWield`
is *ranged only* rather than *not melee*, and a mutation to the second reading
fails one case and only one.

## 3 · ⚠⚠ AND THE RULES DATA ITSELF IS HELD, WHICH IS THE LAYER I NEARLY MISSED

A starting array is **neither a blueprint nor a character**, so neither of the
other two guards covers it.

> If `droid_arrays.toml` ever names a melee weapon, the chargen guard disarms
> the droid **correctly** — and **an entire class ships with no weapon at
> all.** That is a worse silence than the one it prevents.

A test over the real shelf fails with the array's own name in the sentence:
*"the `scout` droid array names Vibroblade, which is `Melee - base weapons`…
so this class would ship a droid with no weapon at all."* `PT-1379`'s
principle — *the Builder must not create a fault its own validator cannot
detect* — one level up, at the rules.

## 4 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the chargen guard never fires | 2 |
| it fires for organics too | 1 |
| a lightsaber counts as wieldable | 1 |
| the refusal does not say which weapon | 1 |
| a droid array names a blade | the shelf test, by name |

## 5 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 615 | **615** |
| `Loom` | 256 | **256** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 487 | **492** |
| | 1,368 | **1,373** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 6 · ⚠ Not done, named

- **The equipment SCREEN does not say it.** A droid whose array named a blade
  would see the row and then find the log says unarmed. It cannot happen with
  today's data, so a sentence there would be unreachable text — **the screen is
  where this goes the day the data can produce it**, and not before.
- **The out-of-bounds silent `_step` return** — `PT-1610`'s shape, one line,
  still its own slice.
- **`PT-1640` and `PT-1653`** stay named, not built.

**Next: companions.** The rule is clean underneath it now, and `isParty` —
`PT-1636`, `PT-1683` — is the one predicate the whole party question already
turns on.
