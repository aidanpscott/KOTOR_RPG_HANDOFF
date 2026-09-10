# BUILD 105 — the left pane empties, and the palette takes it

Loom `2e78da7`. Loom 225 · Lodestar 452 · Lens 7 · app 367 — **1,051 green.**
Pins level. Gate SENDABLE.

---

# ⚠⚠ `PT-1609` — A REMOVAL, AND IT IS ELEVEN ROWS

    row('blueprints', expanded: true)
    for (final k in blueprintKinds) row(k, depth: 1)      ← ten
    row('scripts')

**Gone.** The left pane is areas with their placements, and conversations.

## ⚠ AND I HAD ALREADY WRITTEN THE RULE IN THE SAME FILE

`module_tree.dart` has carried *"the PALETTE enumerates the kind space, the TREE
enumerates what exists"* since slice one — **my own words, three inches above
eleven kind-space rows.** `PT-1609` makes it a ruling; this makes the file agree
with its own comment.

> **The owner's reason is the one that made it urgent rather than tidy: a left
> pane keyed to KINDS gets longer every time we add one; a left pane keyed to
> AREAS gets longer only when an author builds something.** Thirteen roots did
> not grow with a module — it grew with the FORMAT.

## ⚠ AND `scripts` WENT WITH THEM

The ruling says *"scripts when there are any."* There is **no script concept in
this build**, so the row was a heading over a thing that cannot exist —
`PT-1500`'s shape, a constant standing in for a fact. It comes back the day
something can be under it.

**⚠ And conversations keep their root**, because `dialogue/` is not a blueprint
folder — the reason `Created.blueprintPath` is null for one — so a conversation
is **neither a blueprint nor a placement.**

---

# ⚠⚠ THE PALETTE WAS A LIST AND I HAD BUILT IT THAT WAY

`STUDY 27 §3`: **mode selector → Standard/Custom → category tree → blueprints**,
identical across all nine.

**Mine rendered all ten categories down one scroll.** That is the shape slice
two was told not to build, in a longer form — and **the tell was already in the
tests, written by me and asserted around:**

> `new_package_test`: *"`PT-1441`'s TENTH KIND PUSHED THE LAST ONE BELOW THE
> FOLD … a pane that fitted nine categories does not fit ten"* — and the case
> was narrowed to the ones that still fitted.

**A mode selector is ten short rows and one page.** The thing that did not fit
was the list.

## What it is now

    terrain        ▦   the one mode that paints a TYPE rather than places a THING
    creatures
    doctrines
    doors              a doorway, painted
    encounters
    items
    placeables
    sounds
    stores
    triggers
    waypoints          an arrival point, painted

Then, for the mode you are in: **`standard` | `custom`**, then the taxonomy at
whatever depth the author made (`PT-1567`).

## ⚠⚠ CHANGING MODE DISARMS, AND THAT IS WHAT *MODE* MEANS

`PaintMode` is what the next click paints; the page is what the pane shows.
**Leaving them independent would let the board paint a creature while the pane
displays items** — two surfaces disagreeing about one selection, which is the
defect this project has found in three panes already. Re-picking the page you
are on is not a change and costs you nothing.

## ⚠⚠ AND `doors` AND `waypoints` STOPPED BEING SAID TWICE

The pane had a `ways` heading with `arrival point` and `doorway` under it, **and
`doors`/`waypoints` categories eight rows down saying *"painted as … above"*.**
The same two things, listed twice, three inches apart — `PT-1566` found the
contradiction and I answered it with a cross-reference. **A selector has one row
per thing**, so entering `doors` paints a doorway.

`palette_test`'s counts moved with it: **five cannot-list, not seven** — the two
that left are modes that PAINT and have no list to fail at.

---

# ⚠⚠ AND THE STANDARD SIDE IS SHOWN RATHER THAN ASSERTED

The pane carried a sentence — *"only items have a standard side"* — and
displayed nothing on either side of the axis. **An axis stated in prose and
shown nowhere is `PT-1500`'s shape one axis over.**

    nine categories   "base-rules ships rules/ and no blueprints/ at all, so
                      there is no standard X — absent rather than empty"
    items             the base types, LISTED, and not armable:
                      "what a custom item is MADE FROM, not something you place"
    a way             no axis at all — there is nothing on either side of it

`base-rules` not installed says **"that is the shelf, not this package"**, which
is the third sentence in the same family.

---

# ⚠⚠ WHAT SHAPE AN ICON SLOT WANTS — decided before the art exists

    a square, side = the row's own text height
    LEADING the label, never above it or instead of it
    the same box on every row, occupied or not
    the label stays when the icon arrives

**The size is derived from the type size rather than chosen**, so a row never
changes height when art lands and the column never changes width. **The slot is
occupied today** — a glyph for a tile, a spacer for a kind — because a box that
appears later moves every label sideways, which is a relayout disguised as a
decoration.

> **⚠ And the label is not replaced by the icon.** `STUDY 27` had to hover all
> nine of Aurora's icons to write down what they were. **An icon that must be
> hovered to be read is a label you have hidden.**

---

# ⚠⚠ WHAT ASSUMED THE OLD SHAPE — ELEVEN, AND THE COUNT IS RISING

Seven at slice one, eight at two, eleven at three, **eleven again here.**
`PT-1553` names this as the standing risk of an in-place rebuild, and it is the
part of each slice worth reading.

    palette_test          6 cases saw all ten categories on one scroll
    broken_blueprint      the broken creature was reachable without a mode
    one_mapping           both halves of one case are two modes now
    two_trees             asserted the blueprint CATEGORY row survived in the
                          tree — it is the row `PT-1609` removed
    new_package           asserted `blueprints` and `scripts` as roots, and
                          `findsNWidgets(2)` for every kind — *one list, two
                          jobs*. It is one list and ONE job.

**⚠ AND ONE OF THEM WAS A DEFECT RATHER THAN AN ASSUMPTION.** `two_trees`'
reason string read *"only the blueprint CATEGORY row, not a group under the
area"* — **it was asserting the presence of the thing the ruling removes**, and
it passed for three slices because it was true.

**⚠ AND ONE MORE FELL OUT OF THE DISARM.** Two cases counted `PaintMode`
emissions and now see a `null` first, because entering a mode clears the brush.
Both were narrowed to *what must not appear is a `PaintMode`* rather than *the
list must be empty* — **a check aimed at the channel when its subject is one
kind of message on it.**

---

# STILL OPEN

The icons themselves, which `PT-1366` makes separate work · `§5` has no second
interaction the product can reach · the two deferrals in `STATE.md` · and
everything carried from `BUILD 104`.
