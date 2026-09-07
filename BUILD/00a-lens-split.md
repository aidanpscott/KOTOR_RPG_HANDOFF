# 00a · The Lens split — why a fourth package exists

**Backfilled.** `Lens` `d532c0a`. The slice ran before `BUILD/` existed.

---

## The problem, and why it had no home

`AREA-FORMAT-01 §2b` is **one ruling about how an area LOOKS** — walls are mass,
floor is a lit surface, grid lines are a whisper inside it — and it governs
**both** the Builder and the play client. An author paints a room in Loom in
order to see what a player will see. **If the two draw differently, the Builder
is lying**, and that is the whole promise of a Builder.

There was nowhere for one implementation to live:

- **`Lodestar` is barred.** `ENGINE-INTERFACE-01 §4`, verbatim: *"No renderer,
  no layout, no widget. The engine says a character has 38 of 47 vitality. It
  does not know there is a bar."*
- **Neither program may depend on the other** — worse coupling than the problem.

So step 6 **duplicated the renderer and flagged the duplicate in the file**
rather than letting it be silent. `PT-1381` ruled the fourth package instead.

> **⚠ The alternative was accepting drift, and the drift was predictable rather
> than hypothetical: the first amendment to `§2b` reaches one implementation and
> not the other.**

## What moved, and what deliberately did not

**Moved:** the palette, the board itself (floor, water, difficult, hazard, walls,
the single outline, tokens, arrivals, doorways), `BoardMetrics`, and the pan/zoom
viewport — because both programs pan and zoom identically, including the
pointer-down anchor fix a drag needs.

**Did not move:** Loom's palette gestures, its drag-to-fill preview and size
label, its selection behaviour; the app's marker and its movement.

**The seam is `AreaViewport.overlay`.** Each program draws its own extras on top
and nothing program-specific enters the board.

## ⚠ Why "selection" became "emphasised"

Loom's selected tag changed a colour **inside the shared drawing**. Moving that
as-is would have put an authoring concept into a package the play client also
uses — the play client has no selection and never will.

> **So the board takes a set of `emphasised` tags.** Loom puts its selection in
> it; the app puts nothing in it. Neither program's vocabulary leaks into the
> other.

Later, arrivals needed the same treatment and got a **separate set keyed by
name**, because `AREA-FORMAT-01 §4·0` makes an arrival a name and a coordinate
with **no tag** — so a tag and an arrival name can never collide.

## The evidence the move cost nothing

Command Deck was captured before and after and the decoded pixels compared.
**Every differing pixel lay inside a 53-pixel box around the marker** on square
0,0 — the app's own overlay, which was rewritten. The board itself was **byte for
byte identical**.
