# BUILD 166 — the fallen, in their own words

---

## 1 · ⚠⚠ `PT-1846` — ONE CREATURE, TWO QUESTIONS, ONE ANSWER

`_concealed` is the **board's** question and its answer is *do not paint this*:
a creature the author hid (`PT-1550`), plus the fallen, who leave nothing
behind (`PT-1521`, `PT-1525`). **One set, one consumer, and it was right.**

The sidebar asked that same set a **different** question and printed the answer
as the word `hidden` — so a dead combatant's row read *hidden*, which is true
of the board and false of the creature.

`PT-1468`'s shape exactly. And it surfaced only because `PT-1108` had just
given that word a second, real meaning worth reading.

> *"Separate the display language from the underlying not-drawn mechanism even
> if the set membership stays shared."*

**⚠ SO THE MEMBERSHIP IS STILL SHARED.** `_concealed` is built **from**
`_unseen` rather than beside it — a second walk over `_here` is how two sets
come to disagree about one creature.

**⚠ AND THE WORD IS THE PRODUCT'S OWN.** `_condition` already says *"you were
struck down here"* when the player reaches zero, so nothing is invented to name
a state the screen can already name. Derived from `standing`, which the row
already carries, rather than from a new field.

## 2 · ⚠⚠ AND MY FIRST SCREEN TEST PROVED NOTHING — THE THIRD THIS SESSION

It killed the only enemy, so **the fight ended**, the list fell back to the
party, and the corpse had no row at all to be wrong about. Green, and worthless.

Mutation-checking caught it, as it caught the other two. The real assertion went
where the state already exists: `two_enemies_test` already drives *the window
between a killing blow and the end of a fight*, and already asserts the **board**
still conceals the body. The row assertion now sits beside it —

    expect(board(t).concealed, contains(dead.subject));  // do not paint it
    expect(dead.hidden, isFalse);                        // it can be seen

— one creature, two questions, two answers, in one place.

---

## Tests

    App  590 pass   (party_sidebar +3 · two_enemies +2 assertions)

Both halves mutation-checked: restoring `_concealed` as the row's source fails
the two-enemy case; removing the word fails the widget case.

## Still open

- `§2`'s character screen (the click, `PT-1443`'s) · `Dash`/Hustle unbuilt ·
  `Scan`, `Slice`, `Treat`, `Repair` unblocked and unbuilt · the stealth field
  generator has no item.
- ⚠ The `whole_loop_test` flake, one sighting at `BUILD 162`.
