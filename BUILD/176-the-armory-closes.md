# BUILD 176 — the Armory closes, and what the rest is waiting on

---

## 1 · ⚠⚠ `PT-1858` — THE MARKERS WITH NO INDEX RESOLVE TOO

`BUILD 173` set 168 rows aside as *"a different confidence level"* — their
markers carry **no subtype in the margin** at all.

**That was half right, and the half it missed is the point.** The margin has no
number to check a blueprint against — **but it still names the vocabulary**, in
the chapter's own English (*Species-restricted*, *Alignment-locked*, *which
appearance*), and the blueprint still carries the subtype.

    what was missing was only the cross-check between two
    transcriptions of the same number — and the blueprint was
    always the authority. The margin was a copy of it.

So the discipline is the same one **minus the redundancy**: the item must carry
**exactly one** property indexing the named table, and that table must give a
non-empty, non-numeric label. Anything else is refused.

**⚠ AND I GOT THE TABLE NAME WRONG ON THE FIRST TRY.** I guessed
`IPRP_APPEARANCE`; `itempropdef` says `Appearance`. Three rows were **refused
rather than resolved to nothing** — the guard doing its job on a name I got
wrong.

**167 resolved · 166 changed rows · 0 differing in anything but a label.**

**Two markers remain in the whole book, each for a stated reason:**

- `Dancer's Outfit` — `gender`'s only readable column is a **strref**, so the
  numeric guard refuses it. The same hole that put `(951)` in Chapter Seven.
- `Crystal, Solari` — **two** properties index `IPRP_ALIGNGRP`, so *which
  alignment* has two answers and neither is the one to print.

## 2 · ⚠⚠ AND WHAT THE REST OF THE ACTION ECONOMY IS WAITING ON

I went looking for the next Action and found them all waiting on one thing.

**`Gear` is fully ruled** — `§3`: *"One per round. Using a consumable or
activating a worn device."* Its items exist, its budget is drawn on the strip,
and `spendGear` **has no callers**, which is what caused `PT-1856`.

**What it cannot do is take effect.** The shelf carries the medpac's rule as
**prose**:

> *"Basic medpacs heal 10 vitality points + WIS modifier + user's skill in
> Treat Injury."*

**Nothing executes a sentence.** That is the same shape `BUILD 150` named — *a
sentence is not a rule* — and it is the single blocker under:

    Gear      a consumable's effect is prose
    Treat     a Medicine check whose result is healing
    Slice     a check against a droid whose result is unstated
    powers    effects are a no-op (PT-1847 named it)

⚠ **So an effect model is the next real milestone**, and it is a format
question rather than a build I can start: something has to carry *heal 10 + WIS
+ Treat Injury* as a value rather than a sentence.

---

## Tests

Unchanged — this slice is data and a survey. App 597 · Lodestar 740.

## Still open

- **An effect model** — the blocker under Gear, Treat, Slice and power effects.
- ⚠ **`spendGear` has no callers**, so the Gear budget can never be spent.
- **A real target picker** — `PT-1847`, and it waits on the same effects.
- `§2`'s character screen (the click, `PT-1443`'s) · the stealth field
  generator has no item **and no way to activate one** (it is Gear).
- ⚠ Scan's combat half is still unexercised — the rule, not a coverage gap.
