# BUILD 81 — `PT-1539`/`PT-1541`/`PT-1544`: 38 of 38, and a track

**843 green** — Lodestar 389 · Lens 5 · Loom 131 · app 321.

---

## ✅ THE SABOTEUR — **38 of 38**

Ruled three-quarters, `CLS_ATK_2`, and **not from its rate word**: `STUDY 25`
showed a rate word does not give a ladder. **The Smuggler is its exact twin —
`Specialist` AND `d6` — matched on the whole profile rather than one field.**

⚠ **AND IT POINTS AT THE TWIN'S LADDER RATHER THAN CARRYING A COPY.** The
extractor reads the Smuggler's rows; **if that table is ever corrected the
Saboteur follows.** That is `PT-1544`'s principle applied to the field it was
not written about.

---

## ⚠⚠ THE DEFENCE TRACK — **the structure, and two curves rather than three**

    a track is a NAMED LADDER classes point at        — PT-1544
    the Consular is the Noble +1, so it is an OFFSET  — PT-1541
    the Soldier is a RULE, so it is COMPUTED          — PT-1541
    the Noble's interior is UNREAD, so it is NULL     — PT-1541

⚠⚠ **THE GAMES GAVE US THE SHAPE:** `classes.2da`'s `armorclasscolumn` names a
**COLUMN** in `acbonus.2da`. **Attack is three TABLES by table name; defence is
ONE table by COLUMN name.** `TRACE-85`'s *"class 4"* is a lookup into it.

### ⚠ What each of the three does, and why they differ

**The Consular carries no numbers at all** — it carries `sameCurveAs: noble,
offset: 1`, verified row by row across twenty levels. **The day the Noble's
interior is read, the Consular's follows.** Cannot-drift **expressed** rather
than promised.

**The Soldier is computed** because the source states it as a rule — *linear,
+1 every two levels* — and it lands on **both** attested endpoints (+3 at 1st,
+12 at 20th). ⚠ **Clamped past 20, not extrapolated.**

**The Noble is endpoints only.** The irregular curve *"holds three levels then
two then three then two throughout and no single formula reproduces it."*
**`bonusAt` does not interpolate** — a level-7 Noble gets **no class term at
all**, which is `PT-1531`'s rule at a finer grain than a whole class.

⚠ **AN OFFSET FROM NOTHING IS NOTHING.** Where the Noble is unread the Consular
is too, rather than a bare `+1`.

### ⚠⚠ ZERO IS A VALUE AND ABSENCE IS NOT

*"This class deliberately gets none"* must be distinguishable from *"nobody
filled it in"* — **the eighteenth instance of that family and the first a
shipped game solves for us**, since KOTOR ships explicit zero columns.

### ⚠ And the sixteen are left alone

A small roster **under-counts tracks** — two from six classes in K1, **six from
seventeen in K2** — so three `RCR` classes giving two curves is consistent with
two *and* with six. **A class on the wrong ladder is worse than a class with
none.**

⚠ **The two sources are not mixed.** `RCR` gives the Soldier the strongest of
the three; **K1 gives it zero at every level.** A light-armour compensation and
a universal track are two numbers that look like one field.

---

## ⚠ I COULD NOT REACH THE BOOK, AND SAY SO

`PT-1541` reports the RCR PDF on the owner's machine, verified from the title
page. **It is not on any path this build can read** — searched by filename
(`360425628`) and by title across the home and library trees; `MAIN_WORK/data/books/`
holds three files and not that one. **The interiors stay unread here until it
is**, and the structure is built so that reading them is a data change and not a
code change.

## ⚠⚠ `PT-1543` — COMPONENTS AND TOTAL, ON ONE ROW

`Tester`'s Aurora run **diagnosed `PT-1533`**: Aurora's creature sheet puts
`SCORE + RACIAL MODIFIER = TOTAL` on one row, and **every group shows components
AND total, never one without the other.**

> **No screen of ours showed `bought + racial = total` together, and that is why
> the bug went unseen.**

The defence row reads **`base 10 + Dexterity 2 + class 3 = 15`**. A total alone
cannot be checked; components alone leave the arithmetic to the reader. ⚠ **And
a term the rules cannot answer is simply not in the row** — `base 10 = 10`.

## Still open

- ⚠⚠ **The Noble's interior** — an RCR Chapter 3 read, on a machine I cannot
  reach.
- ⚠ `PT-1540` (the turn does not end itself), `PT-1542` (blueprints vs
  instances), `PT-1509`'s perception half, `PT-1532`, `PT-1537`.
- ⚠ `tester-probe`'s failure node; no `unlink` button; `PT-1484`, `PT-1485`,
  effect columns, 45 annotation cells.
