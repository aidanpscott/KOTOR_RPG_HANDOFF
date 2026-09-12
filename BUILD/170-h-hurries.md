# BUILD 170 — `h` hurries, and hiding costs you the run

---

## 1 · ⚠ `PT-1851` — DASH

`ACTION-ECONOMY-01 §1`: *"Double your movement this round."* One line in the
document and no elaboration anywhere in the corpus. The **second** Action in
this product that is not Attack, after Disengage.

**⚠⚠ IT ADDS A SPEED, IT DOES NOT DOUBLE WHAT IS LEFT**, and the document's own
words decide it. *"Your movement this round"* is `speed`; doubling that gives
two speeds for the round — so a creature that has already walked six of ten
gets **fourteen**, not eight.

Doubling `moveLeft` is a different rule — *double what remains* — and **it
reads identically only for somebody who has not moved yet**, which is exactly
the case a test reaches for first. Guarded, and watched failing against that
mutation.

⚠ The Action pays for it through `spendAction`, so surprised, already-acted and
turn-over stay one question with one answer: `canAct`.

## 2 · ⚠⚠ `PT-1108` — AND HIDING NOW COSTS YOU THE RUN

`BUILD 162` had to ship this half as *"nothing to disable"*:

> *"Hidden disables running, restoring a real cost the source had that a bare
> opposed roll doesn't otherwise carry."*

Running is **Dash**, and Dash did not exist. It does now, so the rule is real.

**⚠ THE CONDITION IS CHECKED BEFORE THE SPEND**, so a refused Hustle costs
nothing — the shape `BUILD 164` had to correct on the swing — **and before the
budget**, so the refusal names the rule rather than the Action.

**⚠ AND THE TEST ENDS THE TURN FIRST, DELIBERATELY.** Hiding spends the Action,
so on the same turn `h` would be refused for *having already acted* — and the
test would pass on the **budget** rather than on the rule. A fresh turn leaves
the Action available and the condition is the only thing in the way. It asserts
both: the hidden refusal appears **and** the already-acted one does not.

⚠ And a refused Hustle does not break cover either — asserted, because reveal
placement is the thing this feature keeps getting wrong.

## 3 · ⚠⚠ A REAL GAP, NAMED AND NOT FIXED: NO KEY IS DISCOVERABLE

Four Actions are now bound to keys — **`f` cast · `d` disengage · `s` hide ·
`h` hurry** — and **not one of them appears in any on-screen legend.**

    exploration   arrows to move · m map · i carrying · esc to leave
    combat        space to end your turn

`PT-1443`'s own reason for the keyboard path is that **it reaches everything the
pointer does**; a key nobody can discover reaches nothing. Pre-existing, and it
grows with every Action added. The wording and placement are a UI decision
rather than something to take inside a build slice.

---

## Tests

    Lodestar   734 pass   (dash_test +7)
    App        595 pass   (hide_test +3)

Mutation-checked: doubling `moveLeft` fails the reading case; removing the
hidden check fails the stealth case alone.

## Still open

- ⚠ **No action key appears in any legend** — four and counting.
- **A real target picker**, before power effects resolve — `PT-1847`.
- `§2`'s character screen (the click, `PT-1443`'s) · `Scan`, `Slice`, `Treat`,
  `Repair` unblocked and unbuilt · the stealth field generator has no item.
- **22 unresolved rows** in `Armory` Chapter Seven.
- ⚠ The suite is flaky under load — `BUILD 167`.
