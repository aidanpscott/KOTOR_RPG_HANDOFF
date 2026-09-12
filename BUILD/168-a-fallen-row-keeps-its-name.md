# BUILD 168 — a fallen row keeps its name

---

## 1 · ⚠⚠ `PT-1849` — THE DISMISSED CAUSE WAS THE CAUSE, AT A CALL SITE NOBODY LOOKS AT

`Tester` reported a fallen creature's row reverting to its raw tag, and said
the obvious explanation — *falling drops it out of `_here`* — **did not hold
against the source.**

It holds. There are **four** `_stillHere` call sites, and `_endFight` is the
obvious one and **is not the one that does this**:

    _theFallenLeaveTheBoard()   drops a dead creature the MOMENT it falls
                                — mid-fight, `PT-1538`

The fight keeps it in `f.order` so the panel can still show it (`PT-1672`). So
for the whole window between the killing blow and the outcome, **the row exists
and its placement does not** — and `placed[h]?.name` was null.

**⚠ `PT-1795`'s DEFECT IN A STATE NOTHING HAD LOOKED AT.** That ruling put the
tag behind the name as a fallback for *a placement whose blueprint would not
open*. Here the blueprint opened fine and **the placement was simply gone**.

`_nameOf` remembers what every placement is called — filled where placements
**arrive** rather than where they leave, because the leaving is exactly the
moment the name stops being reachable, and cleared with the room because a tag
belongs to an area (`PT-1331`). The tag is still the last answer.

⚠ Reproduced **first**: the assertion went into `two_enemies_test`, which
already drives that window, and it failed showing `droid.command-deck.50`.

## 2 · ⚠⚠ THE PARTY QUESTION HAS A REAL ANSWER, AND IT IS NOT "SAME BUG"

`Tester` was right that the chain differs. So does **the state**:

    an enemy    stateOf → dead at 0   → `_stillHere` drops it  → tag
    the party   stateOf → DOWN at 0   → it stays               → name

`PT-559`/`PT-1633`: *"neither of them kills a party member"* at zero — a party
member is `dead` only past **−Constitution**. **So the reported defect cannot
arise for a companion at zero at all.**

**⚠ THE GENUINELY DEAD COMPANION IS COVERED BY CONSTRUCTION AND UNOBSERVED.**
`_nameOf` is filled from every placement regardless of role. I could not
construct the state: a trooper feeble enough to leave the player standing
cannot drive anyone past −Constitution, and one strong enough **wipes the party
and ends the fight.**

**Two attempts at that test passed for the wrong reason** — the first watched
for `struck down` and matched the **player's** *"you were struck down here"* —
and both were caught by mutation-checking. **Neither is shipped.** Saying it is
unobserved is worth more than a green test that proves nothing.

---

## Tests

    App  590 pass   (two_enemies +1 assertion)

Mutation-checked: removing `_nameOf` from the chain fails the two-enemy case.

## Still open

- **A fallen party member past −Constitution** — covered by construction,
  unobserved. Reachable only with a fixture that survives a strong enemy.
- **A real target picker**, before power effects resolve — `PT-1847`.
- `§2`'s character screen (the click, `PT-1443`'s) · `Dash`/Hustle unbuilt ·
  `Scan`, `Slice`, `Treat`, `Repair` unblocked and unbuilt · the stealth field
  generator has no item.
- ⚠ The suite is flaky under load — see `BUILD 167`. `acceptance_test` failed
  in this slice's full run and passes alone.
