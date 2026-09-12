# BUILD 175 — Scan gets its exploration half

---

## 1 · ⚠ `PT-1857` — THE RULING, BUILT

> *"What it's for — finding what an author hid — mostly matters before a fight
> starts, and locking it to combat turns undercuts the whole stealth system."*

`c` now scans outside a fight as well as inside it.

## 2 · ⚠⚠ AND OUTSIDE A FIGHT THERE IS NO ACTION TO SPEND

`PT-1123` is explicit that the exploration catalogue is *"a table plus a filter,
**not a sixth budget**"* — so a free, repeatable Scan is a player pressing one
key until a d20 comes up. And `AREA-FORMAT-01 §3b` already refuses exactly that
for the passive look: *"a second evaluation with the same numbers is not a
second chance."*

**The limit is borrowed rather than invented.** `BEASTS-NATURE-01`:

> *"One attempt per order. You may try again next round; you may not roll twice
> on the same command."*

**A visit is exploration's round** — `_settled` and `_revealed` are already
per-visit — so: **one attempt per hidden thing per visit, and you may try again
when you come back.** Cleared with the room, or *"come back and look again"*
would not be true.

**⚠ IT IS A READING AND NOT A RULING.** Nothing rules what an exploration Scan
costs; this is two existing rules meeting, said out loud.

## 3 · ⚠⚠ AND IT IS TESTABLE WHERE THE COMBAT HALF WAS NOT

`BUILD 173` had to ship the combat half **unexercised**: no fixture in the suite
leaves a creature concealed while the player can act, and `two_enemies_test`
says so in its own comment.

**A lurker nineteen squares off is past the passive look's ten** — so it stays
concealed, and the exploration half has the state the combat half could never
reach. The test asserts the **derivation line**, so a scan that finds nothing
must still have *looked*, and the second attempt is refused.

⚠ Mutation-checked: removing the per-visit cost fails the case.

---

## Tests

    App  597 pass · no overflows

## Still open

- ⚠ **The combat half of Scan is still unexercised** — the fixture problem
  stands, and it is the rule rather than a coverage gap: a passive look takes
  10, so an active Scan only beats one on a roll above ten.
- ⚠ **`spendGear` has no callers**, so the Gear budget can never be spent.
- **168 no-subtype markers** in `Armory` Five and Six.
- **A real target picker** — `PT-1847` · `§2`'s character screen · `Slice`,
  `Treat`, `Repair` unbuilt · the stealth field generator has no item.
