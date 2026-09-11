# BUILD 137 — three from `TEST 063`, and one of them was the environment

---

## 1 · ⚠ THE MELEE UPGRADE — NOT BROKEN, NOT BUILT, AND THE SCREEN NOW SAYS SO

The log has recorded `item_unresolved: "nothing applies it yet"` since it was
written. **The screen did not.** It read *"an upgrade on the gear you already
have"*, which a player takes as a promise — they accept it and their weapon
does not change.

> **A save that is honest and a screen that is not is the worse half of the
> pair**, because only one of the two is read while the choice is being made.

**⚠ WHY IT IS NOT BUILT, MEASURED RATHER THAN ASSUMED.**
`STARTING-EQUIPMENT-01 §4a` is nineteen classes, a **different upgrade per
profession** (`Hunter`, `Veteran`, and rows that read **BOTH**), and most rows
are a **choice** — *"Long Sword + Short Sword **or** a Double-Bladed Sword"*.
The grant row in the data is **one prose string** carrying three of those
classes.

**It needs `§4a` extracted and a second offer on that screen. That is a slice,
not a line**, and parsing that prose into items would be inventing the
semantics the table already states.

## 2 · ⚠⚠ A CLASS'S STOCK WEAPON MUST EXIST IN THE PACKAGE — AND IT IS LIVE ON THE SHELF

`taris-undercity` carries **zero** item blueprints. `endar-spire` carries
eleven. **Every class a player picks in the first strands them mid-fight**,
which is where `TEST 063` met it: *"equips `items/weapons/blaster-carbine`,
which will not open: There is no item here."*

**⚠ NOTHING ABOVE COULD HAVE CAUGHT IT.** `equipmentMissing` walks what a
**blueprint** equips; this path comes from a **class array in `base-rules`**.
Nothing in the package names it, so nothing in the package could have been
checked against it.

### ⚠⚠ And it is its own validator because I put it in the wrong one first

I placed the check inside `validateBlueprints`, which **returns early when the
package has no `blueprints/characters` folder.** A correct gate for character
blueprints and the wrong one for this:

> **A package with no characters is exactly the package most likely to carry no
> items either.** The check was hidden behind a precondition belonging to a
> different subject — **a check aimed at the wrong subject**, which is the shape
> this corpus keeps finding, and this was one of mine.

The test caught it by returning **no fault at all** where it should have
returned one.

**⚠ ONLY FOR A PACKAGE SOMEBODY CAN START IN** — `base-rules` has no entry
(`PT-1380`), and a package nobody can make a character in cannot strand one.
`Loom` computes the paths by resolving the class arrays against the equipment
table, since only something that can read **both** files can produce them.

## 3 · ⚠ `PT-1719` — THE NAME BECOMES A PROMPT, AND ONLY THAT

`TEST 063`'s narrowing saved the larger half of this: **portrait-first was
already true**, so no step order moved. `PT-1728` keeps name where Identity
already sat — **only the shape changes.**

**⚠ `ChargenFrame.overlay` ALREADY EXISTED FOR EXACTLY THIS** —
`BUILDER-VISION-01 §6a`, *"an in-window overlay, not a new screen"* — so the
prompt copies `_RelockWarning` rather than inventing a second dialog idiom
beside it.

**⚠ THE FRAME BENEATH STAYS THE PORTRAIT STEP IN EVERY RESPECT**: same header,
same footer. That is what *an overlay, not a new screen* means — and it also
stops **a second `BACK` existing in the tree with one of the two unreachable**,
which a finder cannot tell apart.

**⚠ THE SCRIM DOES NOT DISMISS.** `_RelockWarning` cancels on its scrim because
cancelling a re-open is a real answer; **here there is no answer but a name.**

## 4 · ⚠⚠ AND THREE TESTS WERE FAILING ON THE ENVIRONMENT, NOT THE CODE

`whole_loop_test` could not find `Endar Spire` to tap. **The shared shelf has
grown to nine packages** and the library is a **horizontally scrolling row**, so
the tile sat past the fold.

> Its helper dragged `Offset(0, -120)` at whichever scrollable came first —
> **every list in chargen is vertical and the library is not.**

**⚠ `base_rules_test` MET THIS EXACT WALL AND RECORDED IT** — *"at seven
packages `Taris Undercity` is not built at all, so `find.text` was measuring
does this tile fit"* — and fixed it there by asking the row's contents instead.
**This file taps, so it has to scroll**, and the lesson had never been applied
to it. Each scrollable is dragged along **its own axis** now, from one helper
instead of four copies of a broken one.

**⚠ CONFIRMED AGAINST A CLEAN TREE BEFORE BLAMING THE SHELF**: stashed, and the
failures were there without my changes — **three of them, one more than with**.

## 5 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the stock-weapon check never fires | 1 |
| a package with no entry is faulted | 1 |
| Loom stops passing the paths | 1 |
| the scrim dismisses the prompt | 1 |
| an empty name may advance | 1 |
| `BACK` from the story goes to the portrait | 1 |
| the portrait is hidden behind the prompt | 1 |

## 6 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 615 | **619** |
| `Loom` | 256 | **258** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 492 | **493** |
| | 1,373 | **1,380** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

## 7 · ⚠ Not done, named

- **`§4a`'s upgrade table is unextracted**, and applying the grant waits on it
  plus a second offer on the Equipment screen. Named above with its real size.
- **`taris-undercity` will now fault once per class.** That is the check working
  — **the package really is unplayable for a fresh character** — but it is the
  owner's shelf, so I have not edited it. Eleven item blueprints copied from
  `endar-spire` would close it.
- **The out-of-bounds silent `_step` return**, `PT-1640`, `PT-1653` — unchanged.
