# 07 · Backstory collapses to one tab, and Abilities

**`KOTOR-RPG-APP` `b1e57ae`.** 94 tests pass. **One stop, and it is droids only.**

---

## `PT-1401` — the stop dissolved, and the answer came from the data

Backstory is **one tab**. Lifestyle and profession are one field: `grant` is the
credits-or-item half, `teaches` is the aptitude half, **both on the same record**.
`CHARACTER-CREATION-01`'s *"lifestyle touches starting credits, not aptitude"* is
the `grant` column.

**There was never a second roster.** The second tab is gone, `_Lifestyle` is
deleted, and an organic completes Backstory now.

> **`PT-692`'s *"NOT SOME. NOT CHASSIS-DEPENDENT. NONE."* was never wrong — it
> answered a question that turned out not to be asked.** A droid's Backstory now
> differs from an organic's only in offering programmings rather than
> professions.

## Abilities — `PT-1197`, `PT-1227`, `PT-1229`, `PT-1260`

Six rows at **8**, a **30-point** budget, ladder **1/2/3**, ceiling **18**.

**`PT-1227`'s spend controls are real**: the minus renders **only above the
floor** — nothing to sell back at 8, so none is drawn — and the plus **disappears
at the cap** rather than greying. Space for each is reserved so rows never shift.

**A zero modifier renders as `-`, never `+0`.** Source detail, easy to get wrong,
and pinned by a test.

**The class's priority abilities are marked in amber** — the payoff `PT-1098`
moved Class ahead of this step to get.

**OK is refused until the budget is spent.** Unspent points are not a legal sheet.

## ⚠ Adjustments apply AFTER generation

`PT-1260` corrected an arrow notation that implied a base of 10 and *"a sequence
that does not happen"*. So the row shows **bought · modifier · result**, and the
**budget never sees the modifier**. `CHARACTER-RECORD-01` agrees: `abilities`
holds the bought scores and the species modifier is applied on read.

**The subrace's line wins where it has one**, because `§4`'s graph makes the
subrace what resolves the mechanical values — and `Aquala`'s line restates its
parent's two and adds its own.

## ⚠ The adjustment line is PROSE, and the parse is strict

`ability_adjustments` reads *"+2 Constitution, −2 Wisdom, −2 Charisma."* —
regular, but authored as a sentence with trailing flavour. The parser takes only
well-formed signed pairs.

**Anything it cannot read is reported on screen, never dropped.** `Aqualish`'s
parent line says *"set by subrace. See each entry."* — that must not become "no
adjustment", which is `PT-1238`'s rule about absence carrying two meanings.

## ⚠ Where the ladder's bands change is MY reading

The ruling says **"ladder 1/2/3 per step"** and does not say at which scores the
cost rises. This uses KOTOR's own boundaries — **1 per step to 14, 2 to 16,
3 to 18** — which make an 18 cost **16 of the 30**. Flagged in source and pinned
by test so a correction is one number.

## ⚠ THE STOP — a droid cannot complete Abilities

`SPECIES-CHAPTER-v2 §399`: *"Droids are built rather than generated. They do not
use the 30-point buy — their abilities come off the assembly line and vary by
manufacturer, so the values below are the standard production spread for each
chassis."*

**But the chassis record does not carry a spread. It carries ADJUSTMENTS.**

    Droid, Battle      +2 Strength, +2 Constitution, −2 Intelligence, −2 Charisma
    Droid, Astromech   +2 Intelligence, −2 Strength, −2 Charisma

**`+2` with no base to add it to.** A droid does not buy, so there is no bought
score for the modifier to attach to — which is exactly the sequence `PT-1260`
ruled for organics and which has no counterpart here.

**The models help and do not close it.** `models.toml` carries `str · dex · con`
for **18 of 38** models, and those look like absolute scores. **20 models carry
none, and Intelligence, Wisdom and Charisma have no source anywhere.**

The screen shows what exists — the chassis adjustments, the model's three where
it has them — and refuses, naming what is absent.

**THE NEED:** either the standard production spread per chassis as six absolute
scores, or a ruling that a droid's base is something specific for the chassis
adjustments to modify.

## Not built

Steps 5 through 9 — Skills, Feats, Powers, Equipment, Identity. No character
record, no save; `Continue` stays disabled. No explanatory popup — `§6` gives
this screen a question-mark glyph and one needs a seen-once store.
