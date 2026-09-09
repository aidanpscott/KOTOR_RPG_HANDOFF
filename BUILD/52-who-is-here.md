# BUILD 52 — `PT-1468`: who is here is placements plus the player

**One root, three surfacings, fixed once. And death is said.**

---

## The root

`_here` is built from an area's `[[contents]]`. **The player is not in an
area's contents.** Everything that asked *who is taking part* asked `_here`,
so:

| surfacing | what it looked like |
|---|---|
| `f.weapons[playerTag]` | always missed → **a fist for every class** |
| `_workingLines()` outside a fight | the panel named the TROOPER's vitality and nothing about yours |
| `_drawMarker` | a placement's marker has been hollow-when-down since it was drawn; **yours could not be** |

`Present` is the runtime's participant. **The player is not made into a
placement** — `placement` is nullable and null means the player. `_here` stays
for what is genuinely about placement: which square is occupied, which markers
an author put in the room.

## ⚠ The player fires what they carry — proved

The player now resolves `[equipment]` by **the same three hops a placement
uses**, so there is one resolver and no second form. `PT-1452`'s ruling is not
weakened for the player's sake.

    a record naming items/weapons/blaster-rifle
      → Blaster Rifle · rolled 17 — d20 16 + attack 1 · needed 10
        — hit · 10 damage · 8 left

## ⚠⚠ BUT THE ENGINEER WILL STILL SWING A FIST, AND HERE IS WHY

**The runtime is fixed and there is nothing to read.**

`EquipmentChoice` is a single `bool takesItem`, and `hub.dart` writes
`items: const <String>[]` — hardcoded. **Which item you took is recorded
nowhere.**

⚠ Scoped negative, and it is the whole shelf: **all seven of the owner's saves**
— `kaeda-vos`, `probe-walker`, `rell-vantt`, `second-fight`, `t3-k9`,
`t3-m4-probe`, `vess-taran` — carry exactly

    {"kind":"character.equipment-set","payload":{"route":"standard","items":[],"credits":100}}

Not one has a weapon slot. So the screen now **says why** rather than swinging
in silence — *"unarmed — your record carries no [equipment]: chargen records
THAT you took the grant, not WHICH item"* — which is `PT-1452`'s rule for a
placement applied to the player unchanged.

**⚠ NEED, not a proposed solution.** Two things are missing and they are
separable:

1. **A producer.** Nothing records the item's identity at chargen.
2. **The content to point at.** `endar-spire` ships **one** item blueprint,
   `items/weapons/blaster-rifle`. There is no Ion Blaster to reference even if
   something wrote the reference.

`ITEM-DISAMBIGUATION` may be the other half of (2): the arrays name items in
prose, 18 of 41 resolve to exactly one catalogue row, and `§2c` covers 14 more
— and `item_disambiguation.toml` still has **zero readers**.

## Death is said

It said **`it is over`** — *which reads as the FIGHT being over* — and `PT-559`'s
revive surfaced **retroactively, in the past tense, during the NEXT fight**.

Now, at the moment it happens and in the present tense:

    YOU FALL. The fight ends and you stand at 1 — PT-559: anyone left down
    stands at 1 when combat ends.

⚠ **And a condition is STATE, not a log line.** `_said` is a log tail and the
next thing that happens overwrites it, so **two arrow presses replaced the only
trace of a death with a position readout.** The condition is folded into the
panel and survives walking. Tested by pressing two arrows.

Everyone is also re-folded from the log the instant the outcome is written, so
the revive is true *now* rather than next fight.

---

## ⚠ A defect found while testing it, and it is a shape

    unawaited(widget.onAppend?.call(_writeOutcome(f)))

**Dart does not evaluate the argument when the receiver is null.** With no
listener, `_writeOutcome` never ran — so the session log received neither the
`encounter.ended` nor the `character.revived` that `PT-559` requires. **A
producer that only fires when somebody subscribes.**

Latent in the product, because `main.dart` always passes `onAppend`. Fixed at
all three sites: the outcome is computed, then handed over.

## Tests

**653 green** — Lodestar 297 · Lens 4 · Loom 115 · app 237.

⚠ **Three of the four new tests were verified red with the root fix reverted.**
The fourth is the control that stays green either way: it asserts the *unarmed*
case still explains itself.

⚠ And one honest note on my own first attempt: adding a second panel row
overflowed the column by 15px. `BUILD 44`'s lesson — this screen has no spare
vertical and a row is not free. It is one row.
