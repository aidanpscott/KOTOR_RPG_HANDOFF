# BUILD 80 — `PT-1535`/`PT-1538`: three classes, three unrelated typographic reasons

**837 green** — Lodestar 382 · Lens 5 · Loom 131 · app 319.

---

## ⚠⚠ TWO OF MY THREE "MISSING" CLASSES WERE NEVER MISSING — 35 → **37 of 38**

`Marksman` and `Engineer` have **complete BAB ladders** in
`CLASS-TABLES-DROID.md`, and they were unreachable for **three unrelated
reasons at once**:

    · THE FILENAME SAYS DROID and the contents are two CLASSES
    · TWO CLASSES SIDE BY SIDE, with a \multicolumn artifact row
      AND A BLANK LINE INSIDE THE TABLE
    · THE HEADERS ARE INITIALS — **CD** and **ED** — so "Marksman"
      matches the summary and the title and NEVER THE LADDER

**Any one of those alone would have hidden it.** I reported them absent after
searching for the class name, which is the search the third reason defeats.

### ⚠⚠ WHICH COLUMN IS WHICH IS **PROVED**, NOT ASSUMED FROM THE INITIALS

The summary states the rate per class; `CLASS-TABLES-BASE` gives the closed
forms — **full is `+20 at 20`, three-quarters is `+15 at 20`.** The extractor
checks both ladders against those endpoints and **refuses the pairing if they
disagree.**

> **Reading a column by its position is exactly how the wrong class gets a full
> ladder.**

⚠ **Controlled:** with the summary's rate altered it prints
*"level-20 endpoints (20, 15) do not match the summary's rates (15, 15) —
columns NOT read"* and extracts neither.

    Marksman  +1 → +20   full — CLS_ATK_1
    Engineer  +0 → +15   three-quarters — CLS_ATK_2

⚠ **And it is a K1 fact:** K2 flattens all seventeen classes to `CLS_ATK_1`, so
reading the Engineer from K2 would give it a full ladder.

## ⚠ THE SABOTEUR STAYS OMITTED — and the reason is not "we have not looked"

**Its ladder must NOT be derived from its rate word.** Rates come from
`FEAT-SCHEDULE-01`'s level-30 totals — **an attack-PICK rate from a FEAT
signal** — and `Engineer` (Middle), `Smuggler` (Specialist) and `Consular`
(Specialist) **all have three-quarters BAB. Three rate words, one ladder.**

**The survey settles the shape:** 36 tables give **8 full, 28 three-quarters,
zero half**, and `CLS_ATK_3` is used by no class in either game. **So it is a
choice between two ladders, not an open field — and that choice is the
owner's.**

---

## ⚠⚠ `PT-1538` — THE DUPLICATE-DEATH HALF, AND THE CAUSE WAS MINE

**`_here` was filtered in `_enter` alone.** So a creature killed *during a
visit* **stayed on the board** until you walked out and back: `_occupant` still
answered with it, bumping it started a **fresh initiative**, and the third
`died` fired at **vitality 0 with no new crossing at all.**

> **The rule was right and it was applied at ONE of the TWO moments a creature
> can die.** Arrival was the one I had a reason to think about.

`_stillHere` is one function called at both, and **`_hasDied` now guards the
DEATH loop as well as the revive** — they had the same cause at `022` and only
one half was closed. `PT-1530` attributed the whole symptom to `PT-1524`, and
that accounted for one half.

### ⚠ AND A FIXTURE DEPENDED ON THE DEFECT

`fightAndRead` keeps pressing after the fight, and **a corpse used to absorb
those presses as fresh fights** — so a roll line was always on screen at the
end. With the square empty those presses are **walking**, `_said` becomes a
position readout, and the derivation is gone.

**The frame the blow was on is remembered as it happens** rather than looked for
after the fact. A test that only passed because a defect kept the screen busy is
worth naming.

---

## ⚠ AND `hub.dart`'s COPY IS FOLDED IN

`§4`'s graph — *the variant's line wins where it has one, the parent fills
silence* — was written inline in `hub.dart` **and again** in `adjustmentsFor`.
`adjustmentLine` is the one expression now, **in the file that taught us the
shape.**

## Still open

- ⚠⚠ The **Saboteur's ladder** — a choice between two, and the owner's.
- ⚠⚠ The **class defence bonus** — an RCR Chapter 3 read, and the owner's.
- ⚠ `CLASS-ATTACKS-01` contradicts itself on the Marksman — `§2` Combat,
  `§2.2b` *"Specialist, not Combat"*, **twenty-four lines apart.** A PICK-rate
  dispute; it cannot affect BAB and did not block this.
- ⚠ `PT-1509`'s perception half; `PT-1532`; `PT-1537`; `tester-probe`'s failure
  node; no `unlink` button; `PT-1484`, `PT-1485`, effect columns, 45 annotation
  cells.
