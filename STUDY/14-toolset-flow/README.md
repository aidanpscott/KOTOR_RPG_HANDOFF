# STUDY 14 — Aurora's flow: launch to a placed creature

**`STUDY 12` catalogued Aurora's forms. This traces its path.** Same binary,
same 105 parsed DFM streams; the question is what happens in what order, and how
many times the software stops and waits for a person.

---

## The number

> **Two pieces of typing and one list selection stand between double-clicking
> the icon and having a creature standing in an area. Everything else on that
> path has a default you can press past.**

Eight decision points, four defaulted, **two undefaultable — a module name and
an area name** — and two that live in runtime code I could not read. The honest
range is **two to three**.

## The shape

```
 1  Welcome dialog     "What would you like to do?"     ← launch opens on a QUESTION
 2  Module Wizard      tsStart            nothing       → Next
 3                     tsModuleCreation   TYPE a name   → Next
 4                     tsAreaCreation     "New Area"    → launches the Area Wizard
 5    Area Wizard      name + tileset     TYPE, PICK    → Next
 6                     size               2 × 2 filled  → Next
 7                     finish             defaults set  → Finish
 8  Module Wizard      area now listed                  → Next
 9                     tsFinish           nothing       → Finish
10  Main window — the area is ALREADY OPEN in the viewer
11  Palette → Creatures → place one
```

**Four windows. Nine page-views. Four of them ask nothing at all.**

## Reading order

- **`RECORDS.md`** — description only, `R14.01`–`R14.10`.
- **`FLAWS.md`** — judgement, `F14.01`–`F14.07`, including where our situation
  differs.

## The three findings that matter most

**It never shows you an empty tool.** Launch opens on a question whose third
option is literally *"Start normally"*, and the Area Wizard's
`Open Area in the Area Viewer` defaults ON. The empty state is engineered away
at both ends. (`F14.02`)

**The wizard is a corridor with two blanks in it**, not a questionnaire. Four of
nine page-views are labels and a `Next` button, and they carry the explaining.
(`F14.01`)

**It delegates rather than absorbs.** The Module Wizard does not ask about
areas — it launches the Area Wizard and lists what came back. That is why the
two wizards on the critical path are the two smallest in a program whose Script
Wizard runs to 19 pages and 107 inputs. (`F14.03`)

## Where we differ

**Aurora asks one thing we do not need at all: the tileset.** `AREA-FORMAT-01`
has no geometry — no heightmap, no mesh, no walkmesh — so one of Aurora's three
real questions does not exist for us.

**We need four things it never asks:** an `id` distinct from the display name,
with `PACKAGE-NAMING-01 §5a`'s four refusal rules enforced on it; a `version`;
and declared dependencies whose **order is the precedence**. Aurora put its
equivalent of the last one behind a properties screen and kept the creation path
at two questions — **that is evidence for deferring it, not for including it.**

Our reachable count is **two names**, the same as Aurora's, but only if the `id`
field derives itself from the name and stays correctable. (`F14.06`)

## ⚠ Scope

Binary inspection of Beamdog EE `1.5.0.5`, plus the shipped changelogs. **The
toolset was not run.** A DFM records what a property is when the form loads, not
after its code runs — so every enable rule, list population and "Next is blocked
until…" is code that was **not disassembled**. Four such unknowns sit on the
critical path and two of them move the headline number; they are named in
`F14.05`.
