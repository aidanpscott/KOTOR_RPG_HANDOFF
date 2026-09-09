# BUILD 69 — `PT-1501`: the sentence was there and the render ate it

**721 green** — Lodestar 321 · Lens 4 · Loom 122 · app 274.

---

## ⚠⚠ `PT-1499` was built last slice and Tester was still right

The fix was in `combatantsIn` **and** wired to the panel. **It was the render.**

The panel is **one `Text`, `maxLines: 2`**, joining every line with `  ·  `.
Measured with `TextPainter` at the play screen's real width rather than
reasoned about:

    one 203-character sentence   fits
    ⚠ two                        DO NOT

`Tester`'s room had **two** malformed placements, so the second vanished
entirely — standing on that marker, nothing was said.

⚠ **That is my own `maxLines: 2` from `BUILD 62`**, added to stop a 15px
overflow, now eating the sentence `PT-1499` added.

### ⚠⚠ And a `find.textContaining` test passes on ellipsed text

The widget's `data` is whole; the **render** truncates. **Every test I had
would have passed while a player saw nothing.** That is `PT-1464`'s shape one
step along: computed, rendered, and truncated to invisibility.

### The fix, and the rule worth keeping

The sentences are **short** — tag first, then the fact — and:

    ⚠ 2 drawn and not present — old.a.01 — not a creature path · …

**WHEN A LIST CAN BE ELLIPSED, LEAD WITH THE COUNT.** Truncation can then hide
**which**, never **that**.

The new test **measures the layout**, at the real width, for Tester's exact
case of two.

---

## `equipmentMissing` walks `blueprints/` — and the fourth instance was beside it

`validateBlueprints` walks `blueprints/characters/` directly, so a blueprint
**authored and not yet placed** — the normal state between being made and being
used — has its equipment checked. `§4` bars the *engine* from browsing to
resolve a reference; a validator asked to look at a package is doing what it
was asked.

### ⚠⚠ The fourth instance was in the same file

A character blueprint names **three** kinds of path — `equipment`, `doctrine`,
`conversation` — and **verify checked exactly one.** The rule was already
written; two fields beside it were never handed to it.

⚠ **And they do not share a root.** A `doctrine` is relative to `blueprints/`
(`PT-1441` ruled it a PATH); a `conversation` is relative to the **package**,
because `dialogue/` is not a blueprint folder. **Checking both under one root
would report every conversation missing — which is how a check comes to be
switched off.** A test asserts both resolve under their own roots.

`endar-spire` and `base-rules` both verify at **0 faults**.

## Still open

- ⚠ **`PT-1500` — the palette.** Ruled and unstarted.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 48 annotation cells.
