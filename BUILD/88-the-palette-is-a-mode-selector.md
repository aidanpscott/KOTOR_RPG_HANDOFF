# BUILD 88 — `PT-1560`, slice two: the palette is a mode selector, not a list

**920 green** — Lodestar 395 · Lens 7 · Loom 187 · app 331.

Lodestar `61e2849` · Lens `6b55219` · Loom `bcb585f` · app `f453601`.

⚠ **Loom only.** No reader, no writer, no editor, no wizard, and **no two-row
tab bar** — `STUDY 29` found clicking a back-row tab SWAPS THE ROWS, so `Tester`
aimed at Statistics and hit Feats.

---

## ⚠⚠ ONE SELECTION, BY CONSTRUCTION

`PT-1543`: Aurora's palette is a **nine-way selector matching the nine kinds one
to one**, and picking one changes what a click on the board DOES.

**Ours held three selections** — a tile, a way and a blueprint — in three
fields, **nulled against each other in three separate closures**, each
remembering the other two:

    onSelectTile       if (t != null) _placing = null;
    onSelectBlueprint  if (b != null) { _painting = null; _placingWay = null; }
    onSelectWay        if (w != null) { _painting = null; _placing = null; }

> **Add a fourth and somebody has to remember.** A selector has one selection by
> construction, which is the difference between a rule and a habit.

There is one `PaintMode` now — `PaintTile` · `PaintWay` · `PaintBlueprint` —
and the three values `AreaTab` still takes are **derived from it in one place**,
so they cannot disagree.

---

# ⚠⚠ THE FINDING: TWO OF THE SEVEN ARE ALREADY PAINTABLE

The ruling said *"our eight inert kinds do not need eight dialogs, they need to
be paintable."* **Two of them already were, and the palette hid it.**

The pane called `doors` and `waypoints` **cannot list** — three inches below a
`ways` section offering **`doorway`** and **`arrival point`**, both of which
paint onto a square and work today.

    doors      `§4a` makes a connection's `from` OPTIONAL —
               *"no template means an opening you walk through"*
    waypoints  `§4·0` makes an arrival *"a name and a coordinate"*,
               with NO template and NO tag

> **`blueprints/doors/` is the folder with no format behind it. The DOORWAY
> never needed one.**

**They are the same two concepts under two names**, and nothing on the pane said
so. Each category now carries the line *"painted as `doorway` above — §4a and
§4·0 make it a way, not a blueprint."*

## ⚠ AND THE OTHER FIVE CANNOT BE PAINTED, AND IT IS NOT A UI GAP

`encounters`, `placeables`, `sounds`, `stores`, `triggers`.

A `[[contents]]` row **names a blueprint by path** (`§3`). Painting one of these
would write a `from` naming a file that does not exist and cannot exist — **the
placement `PT-1493` found**, where a creature was *drawn and was not there*:
`combatantsIn` skipped it, `Lens` drew it anyway, and you could walk through it.

> **`PT-1379`: the Builder must not be able to CREATE the fault its own
> validator detects.**

So the pane says that, in those words, instead of offering the click. **Five
rows, asserted.**

---

## ⚠ FOUR LEVELS OF TAXONOMY — `PT-1543`

`Monsters → Humanoid → Goblin → leaves` is Aurora's shape. **Ours is the folders
an author actually made**, at whatever depth they made them: `Listed.names`
returns `weapons/blaster-rifle` and `nest()` splits on `/` and nothing else,
because the separator **is** the taxonomy.

    ▾ items
      ▾ weapons
          blaster-rifle          ← the LABEL is the leaf
                                   the IDENTITY is items/weapons/blaster-rifle

**⚠ A grouping node is a folder, not a thing**, so it is not selectable —
selecting one would load a placement whose `from` names a directory.

**⚠ AND THE RULING'S EXAMPLES ARE NOT IN THIS PANE.** *271 worlds, 320 feats and
104 powers* are **chargen data**, read by the app from `base-rules/rules/`, and
they never appear in Loom's palette. **The SHAPE the ruling asks for is here;
the three flat lists it names are somewhere else**, and saying otherwise would
be claiming a fix for something this slice did not touch.

---

## ⚠ WHAT `STANDARD` MEANS FOR US

Aurora's split is *"ships with the game"* against *"made in this module"*.

> **Ours is `base-rules` against the package being edited** — and `PT-1386`'s
> per-record merge already turns on exactly that difference: a repeated `id`
> replaces, a new one adds.

**⚠⚠ AND IT IS MOSTLY ABSENT RATHER THAN EMPTY.** `base-rules` ships `rules/`
and **no `blueprints/` directory at all** — checked, not assumed. So nine
categories have **no standard side**, which is *absent*, not *none*: nothing
ships a standard creature or a standard doctrine.

**`items` is the exception and the proof the axis is real.** An item names a
**base type** and the base types come from `base-rules` (`PT-1497`, `PT-1452`) —
standard content, in this program, today. **It is what a custom item is MADE
FROM rather than something you place**, because `PT-1452` rules that
`[equipment]` names a blueprint path *"always. There is no second form."*

The pane says the short form in one line, once, where it applies — **a paragraph
at the top of a narrow column pushed every category below the fold, and
`new_package_test` measured it by failing to find `creatures`.**

---

## ⚠⚠ `PT-1546` IN OUR OWN PALETTE

> **A category is where a thing lives; a property is what a thing is. A category
> must never be mechanical.**

Aurora's **Trigger** category SETS the trigger type and is then immutable; its
**Encounter** category is decorative. **Nothing in the UI distinguished the
two**, and `Tester` filed one under Hard, named *"Hard 001"*, with Difficulty
*"Easy"*.

**Ours, checked:**

    the tile HEADING     the TYPE — mechanical. `difficult` costs double
                         (`PT-1513`), and the cost lives on the type
    the entries beneath  VARIETIES — art. `§2·0e`. With no tileset there is
                         exactly one per type, so the two read as one row and
                         the rule is invisible until a tileset arrives
    a blueprint mode     a kind and a path and NOTHING ELSE. No difficulty,
                         no tier, no type

⚠ **AND I NEARLY SHIPPED THE DEFECT WHILE STATING THE RULE.** `PaintTile` was
written with a `variety` field, defaulted to `'drawn'` — **declared, defaulted,
and read by nothing.** `PT-1523`'s exact shape, authored deliberately this time.
**It is removed**; it arrives with the tileset that gives it values, and the rule
holds without it.

---

## ⚠ SLICE ONE'S FINDINGS 5 AND 3, BOTH SETTLED HERE

**5 · SELECT WHAT YOU JUST MADE — now possible for all three.**
Every create dialog returns `Created { kind, id }`, so the blueprint you
authored is **loaded and ready to place** the moment the dialog closes. **It
could not be done before**: two of the three returned a bare handle, and
`selectedBlueprint` is a PATH — there was nothing to select *with* for two kinds
of three. **The palette's exact analogue of what slice one did for placements.**

**3 · ONE ROUTE TO `+` — RESOLVED, AND THE DIFFERENCE STAYS.**
The three situations were real: **seven of ten kinds have no file format.** The
route is one callback now (`onNew(kind)`), and *which* kinds can be made lives
in `newableKindsInPalette` **with a reason a person can read.**

> **The situations were real; the three code paths were not.**

⚠ **And the split was worse than reported.** `newableKinds` said
`{doctrines, items}` while `creatures` was special-cased in the widget beside
it — **which kinds can be made was stated in two places and neither was
complete.**

---

# ⚠⚠ WHAT I FOUND ASSUMING THE OLD SHAPE

## ✓ FIXED HERE

    1  THREE SELECTIONS, NULLED IN THREE CLOSURES. Each remembered the other
       two. One `PaintMode` now.
    2  `doors` AND `waypoints` CALLED UNLISTABLE while the same two concepts
       sat eight rows above, paintable and working, under different names.
    3  WHICH KINDS CAN BE MADE, STATED TWICE — `newableKinds` plus a
       `creatures` special case, and neither was complete.
    4  THE BLUEPRINT LISTS WERE FLAT. `weapons/blaster-rifle` was one row,
       so the folder an author made was invisible.
    5  A `variety` FIELD, DECLARED AND READ BY NOTHING — mine, caught before
       it shipped.

## ⚠ FOUND, NOT FIXED — REPORTED

    6  `AreaTab` STILL TAKES THREE PARAMETERS — `painting`, `placing`,
       `placingWay`. They are DERIVED from one mode in one place now, so the
       remembering defect is gone, but the editor's signature still describes
       the old shape. It is editor work and this slice was told not to.
    7  ⚠ `NewItemDialog` FORCES EXACTLY ONE LEVEL OF NESTING — "two levels
       under `items/`", from `PACKAGE-NAMING-01`'s worked example. The palette
       now renders whatever depth exists and the dialog can only write one.
       **Not a defect — the rule is the document's — but the reader, the pane
       and the dialog now disagree about how deep a taxonomy may go, and only
       the dialog is narrow.**
    8  ⚠ THE `assistant` TAB STILL SAYS "not built yet". A tab that is a
       placeholder is a tab that will be forgotten; it is untouched because
       nothing in this slice is about it.
