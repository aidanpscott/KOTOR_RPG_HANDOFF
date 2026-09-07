# STUDY 14 — judgement

Records are in `RECORDS.md` and are cited by number.

---

## F14.01 · The accessibility number is two

**You asked for a measurable figure. It is this:**

> **Between double-clicking the icon and having a creature standing in an area,
> Aurora asks for exactly two pieces of typing and one list selection. Every
> other decision on that path has a default you can press past.**

Eight decision points, four defaulted, two undefaultable, two undetermined
(`R14.10`). The two that cannot be defaulted are **a module name and an area
name** — and no software can default a name, because the name is the one thing
only the author knows.

**⚠ That is the whole trick, and it is not the wizard.** `STUDY 12` found
accessibility came from having no verbs to learn. This traces the same property
through time rather than across the screen: **the wizard is not a questionnaire,
it is a corridor with two blanks in it.** Four of its nine page-views ask
nothing at all — `tsStart`, `tsFinish`, and the module wizard's area page and
finish page are labels and a `Next` button.

**A wizard is the opposite pressure to a palette, as your brief says.** Aurora
resolved that tension by making the wizard almost entirely empty.

## F14.02 · It never shows you an empty tool

**`R14.01`: launch opens on a question, not on the main window.** Three options,
one of which is literally *"Start normally"* — the toolset treats arriving at
its own empty main window as the unusual choice.

**And `R14.06`: `Open Area in the Area Viewer` defaults ON.** Finishing the Area
Wizard puts you in front of the thing you just made.

**Put those together and the empty state is engineered away at both ends.** You
are asked what you want before you see the tool, and you are dropped into
content the moment there is any. The `No Module` window in the caption is a
state Aurora goes out of its way to keep you out of.

**⚠ This is the finding I would act on first**, and it is not about layout at
all. It is about never making a person look at an empty frame and work out what
to do with it.

## F14.03 · The wizard delegates rather than absorbs, and that is why it stays small

**`R14.05`: the Module Wizard's third page is a listbox and a button.** It does
not ask about areas — it *launches the Area Wizard* and shows you what came
back. `R14.08` shows the consequence: the two wizards on the critical path are
the two smallest in the program, 4 pages / 2 inputs and 3 pages / 9 inputs,
against a Script Wizard of 19 pages and 107 inputs.

**Nesting one wizard inside another is how the module wizard avoided growing.**
The alternative — one wizard that also asks name, tileset and size — would be a
seven-page form, and every later area would need a different path anyway.

**⚠ And the same page tells you the door stays open:** *"You can always create
more areas later by accessing the wizard in the main menu."* The wizard is
explicit that it is not the only way in.

## F14.04 · The smallest legal area is also the default

**`R14.06`: `Min 2, Max 32, Position 2`, with `Text = 2` in both edits.** Press
through and you get 2×2 — the floor, not a middle.

**That is a real choice and I think it is the right one.** A 2×2 area is
instantly comprehensible and instantly fillable; a 16×16 default would be a
large empty grid the author now has to justify. **The default is the smallest
thing that works, not the most useful thing.**

**Ours has the same decision to make and the same shape to make it in.**
`AREA-FORMAT-01 §1` gives an area `size = [w, h]` in tiles, and `PT-1146` locks
zoom as one continuous range so a tile has no fixed screen size. Nothing
specifies a minimum, a maximum, or a default.

## F14.05 · What the DFM cannot tell us, and why it matters here more than in STUDY 12

`STUDY 12` was about structure, and structure is exactly what a DFM records.
**Flow is not.** Four things on the critical path are runtime code
(`R14.02`, `R14.05`, `R14.06`, `R14.09`):

- whether `Next` is blocked until a name is typed
- whether the Module Wizard refuses to finish with no areas, despite its page
  insisting every module needs one
- whether a tileset arrives pre-selected
- which Select Mode is active when the area opens

**⚠ Every one of those changes the count in `F14.01`.** If `Next` is not blocked
on an empty name, the irreducible count is **zero** and Aurora will make you a
module called nothing. If a tileset is pre-selected, the list selection
disappears and the count is two flat.

**I am reporting the number as two typed names plus one possibly-defaulted
selection, and that is the honest range: between two and three.**

## F14.06 · ⚠ Where our situation genuinely differs

You asked for this plainly. Three things Aurora asks that we do not need, and
four we need that it never asks.

### Aurora asks, we do not need

**TILESET.** `R14.06` makes it one of only three real questions in the whole
path. **We have no equivalent.** `AREA-FORMAT-01 §1` is explicit: *"No
heightmap, no terrain mesh, no walkmesh"*, and `PT-1319` settled that nothing
renders in three dimensions. Aurora needs a tileset because an area is 3D
geometry assembled from tile models. Ours is a grid with a text map and a
legend. **One of Aurora's three questions does not exist for us.**

**THE `Terrain` PALETTE TAB and the Terrain/Objects mode toggle** (`R14.03`,
`R14.04`, `R14.09`) are the same absence in the main window. Painting terrain is
painting tile geometry.

**THE LOCALISED-STRING BUTTON** beside the module name (`R14.05`'s `...`).
Aurora routes display names through a global string table. `PACKAGE-NAMING-01
§1` separates `path`, `tag` and `name` precisely so that ours does not, and
records that KOTOR *"collapsed the third into a global string table."*

### We need, and Aurora never asks

**⚠ AN ID DISTINCT FROM A NAME.** Aurora asks for one name and derives
everything from it. `PACKAGE-FORMAT-01 §4` requires `id`, `name` **and**
`version`; `PACKAGE-NAMING-01 §1` makes `path` identity and `name` the thing a
player reads, changing freely. **So our first wizard page has at least two
fields where Aurora has one**, and they cannot be the same field, because the
whole point is that one changes and the other does not.

**⚠ AND `id` HAS RULES A FIELD MUST ENFORCE.** `PACKAGE-NAMING-01 §2`:
lowercase, hyphens, no numbers. `§5a` names **four shapes the Builder must
refuse** — a stat in the name, a bare number, a category posing as a thing, a
trailing disambiguator — each drawn from labels BioWare actually shipped.
**Aurora's name box refuses nothing.** Ours has to, and `§5a` says so in those
words: *"the Builder is what keeps the content worth the scheme."*

**A VERSION.** `PACKAGE-FORMAT-01 §4` requires it and `§4a` makes a version *"the
package's own claim"* against a digest that is *"the fact"*. Aurora's module has
no version the wizard ever asks for. **This is a field with no Aurora precedent
at all**, and a default of `0.1.0` or `1.0.0` is available where a name default
is not.

**⚠ DEPENDENCIES, WHOSE ORDER IS THE PRECEDENCE.** `PACKAGE-FORMAT-01 §4`:
`[requires].packages` is one ordered list, later entries win, *"and that IS the
mechanism."* Aurora's equivalent is the hak list, and **the Module Wizard never
mentions it** — haks are set later, in module properties. `§4` also records that
NWN expressed precedence direction as a **naming convention** (`_top`, `_core`)
and calls that out: *"A convention is not a declaration."*

**⚠ So there is a decision here that Aurora cannot help with:** does our first
run ask about dependencies at all, or does it do what Aurora did and leave them
to a properties screen? Aurora's answer was to keep the creation path at two
questions and put everything else behind properties. **That is evidence for
deferring it, not for including it.**

## F14.07 · What I would reproduce, stated as the sequence rather than the screens

**The reproducible thing is not the wizard. It is the shape of the path:**

1. **Open on a question, not on an empty tool** (`F14.02`).
2. **Ask only what cannot be defaulted** — which turns out to be names, and in
   our case ids (`F14.01`, `F14.06`).
3. **Make the pages that ask nothing genuinely ask nothing** — four of Aurora's
   nine page-views are labels and `Next`, and they carry the explaining
   (`R14.05`).
4. **Delegate rather than absorb** — the second thing gets its own wizard,
   launched from the first, and the first just lists what came back (`F14.03`).
5. **Default to the smallest legal thing** (`F14.04`).
6. **End inside the content, not back at the frame** (`R14.06`).

**⚠ Our count will be higher than two and should be as close to it as the format
allows.** `id`, `name`, `version` for the package, then `name` and `size` for the
first area. **Three of those five have available defaults** — `id` can be
derived from `name`, `version` can start at a fixed value, `size` can default
the way Aurora's does. **That leaves two names, which is exactly Aurora's
number**, and it is reachable only if the id field derives itself and stays
correctable.

---

## Judgements about our own design, kept separate

**On deriving `id` from `name`.** It is the single decision that keeps our count
at Aurora's. It is also the one most likely to produce `§5a`'s failure shapes
by accident — a name like *"Armor Class 8"* derives to `armor-class-8`, which
`§5a` lists as the instructive bad case. **A derived id needs the refusal rules
applied to the derivation, not just to what the author types.**

**On the welcome dialog.** `R14.01` is the piece I am least sure we should copy
literally. Aurora opens on it because its main window is genuinely useless
empty. **Loom's equivalent question is already answered by Console Home** — the
app has a library screen whose whole job is "which package", and Loom is reached
from a package. Whether Loom needs its own front door or inherits one is a
question this study raises and cannot settle.

**A limit I want on the record.** This traces the path a DFM can see. **The four
runtime unknowns in `F14.05` are all on the critical path**, and two of them
change the headline number. If the accessibility figure is going to be used as a
target, someone should run the 1.69 or EE toolset once and watch what `Next`
does with an empty name box. **That is ten minutes of somebody's time and it
settles the only number in this study that matters.**
