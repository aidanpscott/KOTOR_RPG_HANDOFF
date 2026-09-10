# BUILD 106 — a check hiding from itself, a state with no name, and the rows

Lodestar `2b75092` · Loom `323c3b5` · MAIN_WORK `88de5ef`.
Lodestar 456 · Lens 7 · Loom 233 · app 368. Pins level. Gate SENDABLE.

---

# ⚠⚠ `PT-1619` — `connectionUnreachable` WAS HIDING FROM ITSELF

`Tester` measured it on one variable: **the same walls twice, one line apart.**
With a second standable arrival, 13 problems; without it, 11 — and removing it
silenced **both** `connectionUnreachable` and `areaHasNoWayOut`.

    if (seeds.isEmpty) { seed from every floor square }

The seed is *anywhere a character can arrive*. With every arrival walled, that
fell back to every floor square — **which in that fixture is the isolated door.
The door trivially reached a place a character can arrive, because it WAS that
place.**

> **⚠⚠ AND THE PAIRING IS THE ORDINARY ONE.** Walling an arrival is exactly what
> a brush does by accident — it is the case `landingNotStandable` exists for —
> **so the moment that fault fired, the two that say THIS AREA IS A TRAP went
> quiet.** The severity collapsed rather than the package going silent: *"your
> arrival is in a wall"* reads as a placement slip and *"there is no way out"*
> reads as a soft-lock, and the second one is the true one.

**The fallback is now only for an area that declares NO arrivals.** It exists so
the RUNTIME can put a player somewhere (`PT-1605`, `_firstStandable`); **the
validator does not need it.** An area that declares arrivals and has none
standable seeds from nothing and reports every connection unreachable — which is
what the player will actually experience — **and the sentence says which repair
it is**: *"Every arrival this area declares is unstandable, so there is nowhere
to walk FROM."*

---

# ⚠⚠ `PT-1618` — AND `dying` HAD NO NAME AT ALL

`down` is reached **only at exactly zero**; `revived` is written for the whole
band. `Tester` counted twenty saves: **125 crossings at or below zero, 40
exactly zero and 85 negative.** A writer where `PT-1616` put it would emit ~92
events for a population of at most 40 — **the log would have stopped being
silent and started being wrong.**

## Where it goes

**`applyDamage`, where before and after are both known.** `_writeOutcome`'s own
comment says why it is not the site: *"`PT-1421` is ONE CROSSING ONE EVENT and
this wrote one per FIGHT."*

`applyDamage` has produced `downed` since combat was built and the app **carried
it to a status line and no further.** The writer is at the crossing now, on
**both** sides — the player's blow and the enemy's — because 85 of 125 is the
player going down, and a writer on one path only would be the twelfth instance.

## ⚠⚠ WHICH LIFETIME `dying` TAKES, AND WHY — `transient`

    a fight is not a fact; its outcome is        PT-1427, the rule PT-1612 used

The fight resolves it: you stand at 1 when combat ends, you are healed, or you
die. **Whatever survives is already `encounter.ended`, `character.died` or
`character.revived`.**

- **Its neighbour already says it.** `character.damaged / .healed` is *transient
  — until the encounter ends*, and dying is a consequence of damage in the same
  band, ending at the same boundary.
- **A `campaign` one would be folded by nothing.** `projectPlayState` folds
  `died` and `revived`; a third unfolded campaign kind is `PT-1606`'s fifth
  state again.
- **And 85 of 125 is a frequency argument FOR transient**, not against it. A
  kind firing in two thirds of crossings and read by nobody would be the largest
  thing in the save — the case `SAVE-LOAD-01 §4` gives lifetimes their job for.

> **⚠⚠ AND THE TENSION IS NAMED RATHER THAN SMOOTHED.** `character.downed` is
> `campaign` and is the same shape — a crossing inside a fight that the fight
> resolves — **and it is folded by nothing either.** If `dying` is transient
> then `downed`'s lifetime is the anomaly, not this one. `PT-1618` preserved
> `downed` explicitly, so it stands and the question is recorded in the
> document.

**⚠ And nothing in the code decides any of that.** `_persist` filters by the
declared lifetime, so `downed` lands in the save and `dying` does not, **and no
line in the writer knows which** — `PT-1612`'s mechanism, used a second time.

---

# ⚠⚠ THE TREE MARKED ONLY WHAT IT COULD NOT FILE

`Tester`'s finding, and it is exact: the sole alert in the left pane was
`unknownKind` — **a side effect of failing to classify a path.** It marked what
it CANNOT file and nothing it CAN, however broken.

**Every fault already names a row.** A `PackageFault` carries `areaId` AND
`tag`, which together ARE the row:

    areaId + tag    a placement, a connection, or an arrival
    areaId alone    the area
    neither         the package, whose row already carries the count

**Not one needed a new row**, which is why this is a filing function and not a
new surface.

## Three decisions inside it

**⚠ An arrival is filed by its HANDLE, not its name.** `§4·0` makes an arrival a
name and a coordinate — it has no tag — so the row's handle is
`$arrivalHandle$name`. Matching a fault's tag against a row's handle **or** its
label would let a placement tagged the same as an arrival name take the
arrival's mark: **a value used as a key**, the family this corpus has found nine
times. An explicit set of the problems that name an arrival instead.

**⚠ The reason is on the row, not a mark.** `PT-1575`'s discipline one pane
over: the palette shows a broken blueprint with **the reader's own sentence**,
because *"an author who cannot see their file cannot fix it."* **A red row that
does not say why is a mark you then have to go and look up.**

**⚠ And a fault outranks both the selection and the entry amber.** An ENTRY area
with no way out is the worst row in the package, and drawing it amber would say
*this is the special one* while withholding *and it is a trap*.

## ⚠ AND THE RATCHET WALKS THE WHOLE ENUM

A case files every `PackageProblem` member and asserts it lands. **A new one
that nobody files would be this defect again, one member later.**

---

# ⚠ AND THREE COUNTS MOVED, WHICH IS THREE CHECKS DOING THEIR JOB

    event_kinds_test    15 creation kinds — `dying` classified as a PLAY kind
    emitted_kinds_test  50 → 51 declared
    base_rules_test     2549 → 2550 records shipped

**None was narrowed.** Each names what moved it and why, which is the difference
between a total that is doing its job and one that has been frozen.

---

# STILL OPEN

`character.downed`'s `campaign` lifetime, now that `dying` sits beside it at a
different one · the icons, which `PT-1366` makes separate work · `§5` has no
second interaction the product can reach · the two deferrals in `STATE.md`.
