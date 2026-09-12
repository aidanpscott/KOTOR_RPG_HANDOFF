# BUILD 165 — casting gives you away, and a finding I had to withdraw

---

## 1 · ⚠ `PT-1845` — CASTING REVEALS, ALLY OR ENEMY

> *"The mechanism that breaks cover was never about hostility — it's the overt,
> observable act itself, same as a swing revealing whether or not it connects.
> A hidden character healing an ally is exactly as visible as one attacking an
> enemy."*

Placed **after every refusal and beside the spend** — the placement `BUILD 164`
had to correct on the swing. A power the pool cannot pay for, a target the gate
excludes, or no target at all are all acts never taken.

## 2 · ⚠⚠ WITHDRAWN — `BUILD 164`'s PANEL OVERFLOW WAS MY TEST BED

I reported `PartySidebar` overflowing by 7.4px in a fight and filed it as a
**pre-existing product defect**. It is not one.

    hide_test set MediaQuery(size: 1280×720)
    over flutter_test's default 800×600 SURFACE

— telling the app one size and the renderer another. Panels that fit in the
product overflowed in the bed. With the view actually sized, **neither that
overflow nor a 58px casting-menu one occurs anywhere.**

**⚠ AND I CAUSED IT IN THIS SESSION.** `BUILD 162` copied a `setUp` that sized
the view; I removed it as deprecated and **did not replace what it did.** The
analyzer was right about the API and I was wrong about the purpose.

`STATE.md` is corrected and `BUILD 164 §3` carries the withdrawal in place
rather than being deleted — a withdrawn finding that vanishes is a finding
nobody can check.

## 3 · ⚠⚠ AND THE FIRST CASTING TEST WAS A GUARD THAT COULD NOT FAIL

It passed against a build with the reveal **removed**. Casting adds the pool's
*exhausted from* line, the row grows, **the list scrolls it out of the
viewport**, and the default finder reports no `hidden` whether or not the
condition cleared.

Asked with `skipOffstage: false` now, with an assertion that the **row is still
there** so the check cannot pass on its absence. **Mutation-checking after
writing it is what caught this** — the test was green and worthless in between.

## 4 · ⚠ AND THE FIGHT-TO-THE-END TEST IS BACK, CORRECTLY

The first attempt let the thug kill an unarmed Jedi — and **a fallen combatant
is in `_concealed`, which the row reads as `hidden`.** It failed for a reason
that had nothing to do with the fight ending. The thug now has one vitality,
and the test asserts the player **won** before asserting the condition is gone.

---

## Tests

    App  587 pass   (hide_test +2)

Three guards in this slice were mutation-checked **and one of them failed the
check**, which is the only reason it is worth anything now.

## Still open

- `§2`'s character screen (the click, `PT-1443`'s) · `Dash`/Hustle unbuilt ·
  `Scan`, `Slice`, `Treat`, `Repair` unblocked and unbuilt · the stealth field
  generator has no item.
- ⚠ The `whole_loop_test` flake, one sighting at `BUILD 162`.
- ⚠ A fallen combatant's row reads `hidden`, **by construction**: `_concealed`
  means *not drawn* and carries the fallen. Right for an enemy, odd for a dead
  player. Named, not claimed as a defect.
