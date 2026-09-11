# BUILD 135 — the droid that could not swing

`PT-1713`, both layers. The ruling took my own recommendation, so the interesting
part is not *what* was built but **where**, and one thing I got wrong on the way.

---

## 1 · ⚠⚠ THE VALIDATOR IS THE FIX; THE RUNTIME GATE IS THE SECOND LAYER

> *"Enforcing the gate without a validator would mean a droid holding a melee
> weapon simply never acts, discovered by a player watching it stand inert turn
> after turn rather than by an author before the package ships."*

`PackageProblem.droidHoldsMelee` fires for a **placed** creature and for one
**authored and never placed** alike — `PT-1646`'s case, *"nothing else would
have looked."* It names what to do about it, because **a fault an author cannot
act on is one they learn to scroll past.**

The gate ships alongside it in `Fight.enemyTurn` and in the player's own strike,
and it **says why out loud**. A silent hold is the outcome the ruling declined.

**⚠ CHECKED BEFORE THE MOVE AND BEFORE THE ACTION IS PEEKED AT**, so a creature
with no legal attack does not spend a turn walking into range to discover it —
and `PT-1618` keeps the Action unspent when nothing resolved.

**⚠ THE PLAYER'S PATH IS GATED TOO.** A rule applied to the creature's path and
not the player's is the pair this corpus has found wrong fourteen times.

## 2 · ⚠ A lightsaber is closed too, and NOT because it is melee

`ATTACKS-01 §12.5` keeps a lightsaber its own kind — so a check written as
*"is it melee"* would let a droid hold one. `FEATS-UNIVERSAL-01` closes it
separately: *"lightsaber proficiency is not universal — it is Force-class only,
and **droids cannot take it at all**."*

**Two rules, one answer**, and `droidMayWield` is written as *ranged only*
rather than *not melee* for exactly that reason. The mutation to `!= melee`
fails one case and only one.

## 3 · ⚠⚠ `kindFromSection` HAD TO MOVE, AND THAT IS THE STRUCTURAL HALF

It lived in the play screen's `attack.dart`. **The moment a second program
needed the answer it stopped being a play-screen concern** — *which section is
melee* is a rules question. `PT-1497`'s sentence, one field over: *"a reader in
Lodestar removes a second parser; a reader in Loom would have added a third."*

## 4 · ⚠⚠ THE CHECK NEEDS THE SHELF, AND AN EMPTY MAP DISABLES IT SILENTLY

Which section is melee lives in `base-rules`' `equipment.toml` — **a sibling
package** — and `ENGINE-INTERFACE-01 §4` bars the engine from browsing for it.
So `validatePackage` takes `weaponSections` from its caller.

> **That is a check that can quietly not fire**, which is the shape this corpus
> keeps finding. It is stated at `validatePackage`, `Loom` passes the map, and
> **two tests hold the pair**: one that the sections come back at all, one that
> the same package is clean of the fault **without** them.

`weaponBaseTypes` returns `sections` beside `types` — one read, two derivations.
A second loader would have been a second answer.

### ⚠ And there was a race I would not have seen in play

The shelf read is asynchronous and `_verify` fires **on open**, so a package
opened before the shelf answered was validated **without the sections** — the
droid fault silently absent, and nothing on screen to say so. Anything already
open is re-verified when the read lands. **A small race with an invisible
failure is the pair worth closing rather than timing.**

## 5 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the validator never checks a droid | 4 |
| a lightsaber counts as wieldable | 1 |
| an unknown base type is judged melee | 1 |
| only PLACED droids are checked | 1 |
| the runtime gate never fires | 3 |
| it fires for everybody, droid or not | 3 |
| the refused turn spends the Action | 1 |

## 6 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 607 | **615** |
| `Loom` | 254 | **256** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 482 | **487** |
| | 1,353 | **1,368** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 7 · ⚠ Not done, named

- **Nothing stops chargen handing a droid PLAYER a melee weapon.**
  `DROID-SKILLS-01`'s gate runs on skills, not on equipment, and
  `STARTING-EQUIPMENT-01`'s six kits are not chassis-aware. The runtime gate
  catches it **with a sentence** rather than silently, which is why this is a
  gap and not a defect — but the authoring-time half of the ruling is only true
  for **packages**, not for characters. Worth its own slice.
- **The out-of-bounds silent `_step` return** — `PT-1610`'s shape, still one
  line, still its own slice. It changes what every edge press prints.
- **`PT-1640` and `PT-1653`** stay named, not built.
