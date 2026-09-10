# BUILD 90 — `PT-1553`/`PT-1565`: the old shape as parameters, and the eight as a list

> **⚠⚠ CORRECTED. This shipped citing `PT-1553` and `PT-1565`, two numbers I
> minted. `PT-1508` rules that ruling numbers are the owner's — and one of mine
> collided with the real `PT-1565`, the perception ruling, within the day.**
> **That is the cost, and it is not a rule about tidiness.** Both now cite the
> ruling that governs them: `PT-1553`'s named risk, and `PT-1565`'s gap.

**982 green** — Lodestar 397 · Lens 7 · Loom 201 · app 331 · `+33`.

Lodestar `bce8221` · Lens `6b55219` · Loom `4d8be62` · app `d3c1dd5`.

⚠ **`hidden` is untouched** — blocked on the range, and `Researcher` is reading
`.utc PerceptionRange`.

---

# ⚠⚠ `PT-1553` — EIGHT RE-DERIVED FIELDS, ACROSS TWO WIDGETS

> **The old shape survives as parameters describing it.**

`PT-1553` names that as the standing risk of an in-place rebuild, and this is
its **third costume**: a second copy of a mapping (`BUILD 86`), then a special
case (`BUILD 88`), now a signature.

## `ModuleTree` — three fields of one object, and a count

    packageName    _open.name
    areas          _open.areaOrder
    entryArea      _open.entryArea
    problemCount   _report.faults.length

**Pulled apart at the call site and put back together in the widget.** A fourth
would have to be remembered — and **three of them could be given from three
different packages** and nothing anywhere would notice.

⚠ **AND `problemCount` IS THE SHARPER HALF.** *A count is not a smaller report;
it is the report with the reasons removed*, and the row that renders it is the
one place that could ever want them. It takes the `PackageReport`.

⚠ **And `areaOrder` is the manifest's `[order].areas`, never the folder** —
`PACKAGE-FORMAT-01 §1`: *"nothing is discovered by scanning."* **Reading it off
the package is what keeps that true**; a `List<String>` at a call site could
have come from anywhere.

## `_SelectionBar` — the same object twice, in two shapes

It took a record `(tag, what, x, y)` **and** a `PlacedThing`, built by **two
separate traversals of `a.contents`**. `tag`, `x` and `y` were on both sides,
from two lookups, **with nothing to stop them disagreeing.**

`_describe` carries the placement it found. **One traversal, one value.**

⚠ **The cost lands on the tests, and it is the point.** `verify_test`,
`entry_asked_test` and `two_trees_test` now build an `OpenedPackage` instead of
passing three loose strings — **which is exactly the thing three loose strings
could not be checked for.**

---

# ⚠⚠ `PT-1565` — THE EIGHT, AND WHAT THE CORPUS ACTUALLY SAYS ABOUT THEM

`TRACE-12` surveyed the whole of `dialog.tlk`: **2,509 bracketed lines across
256 distinct strings expressing ~25 actual concepts** — a tenfold inflation,
**entirely typo and case drift, not real variety** — reduced to **eight checks,
one manner tag and one retirement.**

> **A closed vocabulary that exists only in prose is one nothing can enforce.**

`§4` closed the gate KEYS in code at `PT-1430`; **the SKILL a check names had
nothing to check it against**, so the wizard took a typed string.

## ⚠⚠ AND THE WORK WAS THE MAPPING, NOT THE TRANSCRIPTION

**The eight are KOTOR's names. Ours are the 26 in
`base-rules/rules/skills.toml`** — shipped, machine-readable, already there.
`SKILLS-01 §8`: *"four map straight across. Security was a rename. Three were
consolidations of nine RCR skills — Stealth from two, Awareness from three,
Persuade from four."*

    Demolitions  → demolitions      Stealth      → stealth
    Awareness    → awareness        Persuade     → persuade
    Repair       → repair           Security     → security   (a rename)

    ⚠ Computer Use  → NOTHING       ⚠ Treat Injury → NOTHING

## ⚠⚠ TWO OF THE EIGHT MAP TO NO SKILL OF OURS, AND THE CORPUS FORBIDS FIXING IT SILENTLY

**`SKILLS-01`, in terms:**

> *"⚠ `Treat Injury` is not `Medicine` and `Knowledge` is not `Science`; they
> are different skills that happen to overlap. **Report it as a gap rather than
> mapping it silently.**"*

and

> *"`Slicing` ⚠ **NOT A SKILL in RCR** — an application of Computer Use."*

**So `null` in `checkTagVocabulary` is a NAMED GAP, not a missing entry.**
Writing `Treat Injury → medicine` would have been **the silent mapping that
document refuses, put into code, where nobody would read the refusal again** —
and it is the exact move `PT-1547` caught in a different costume.

**The suite asserts the two gaps by name, and asserts the silent mappings
ABSENT.**

## ⚠ AND `§4c` COUNTS EIGHT WHILE NAMING A NINTH

> *"`THREATEN` folds into `INTIMIDATE`, **which we run as a real check** —
> KOTOR never did; its own `Intimidate` was manner-only, no roll, ever. **Ours.
> Stated plainly, not assumed sourced.**"*

**Recorded rather than resolved.** The eight are what `TRACE-12` measured;
`intimidate` is ours by ruling — **and it IS one of our 26**, so saying so costs
nothing.

## ⚠ SO THE LIST THE WIZARD OFFERS IS OURS, READ FROM DATA

`skillNames()` reads `base-rules/rules/skills.toml` through **`openRules`** —
the same route `NewItemDialog` reads base types by, and for the same reason:
**Loom still has no parser.** *"A reader in Lodestar removes a second parser; a
reader in Loom would have added a third."*

⚠ **AND AN UNINSTALLED `base-rules` SAYS SO** rather than showing an empty
dropdown — `PT-1500`'s distinction in a third pane. **A list with no entries
reads as "this character has no skills."**

## ⚠ AND `whatItCannotAsk` LOST AN ENTRY, AND THE COUNT NOTICED

*"Which of the eight skills"* was **the only entry there that was a GAP rather
than a choice.** It is closed, the entry is gone, and the test that asserted a
minimum length failed until it was.

> **An entry that is no longer true is the same defect as an excuse that
> outlives its exception** — permission nobody is using any more.

---

## ⚠ WHAT IS STILL OPEN

    ⚠⚠ hidden's RANGE    "on approach" needs a distance and no document
                         carries one. Researcher is on `.utc
                         PerceptionRange` — RCR gave nothing: no sight
                         range, no hearing range, no droid perception rule
    ⚠⚠ new_creature      HAS NO `species` FIELD while `CharacterWriter`
                         takes one. A Loom-authored creature is always
                         species-less — the `PT-1533` shape inside the
                         Builder
    ⚠  PlaceWayDialog    the only dialog that asks before writing
    ⚠  the assistant tab still says "not built yet" — fourth slice running
