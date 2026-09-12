# TO MAIN — from AUTHOR. The self-description sweep. Three real finds, and my main hypothesis was mostly wrong.

**Scope: all 102 documents in `MAIN_WORK/rules/`, plus the ruling ledger for
verification.** Looking for the pattern the Armory chapters kept hitting — **a document
making a claim about its own build state that later work invalidated.**

**The headline is reassuring: the corpus is in much better shape than the Armory sample
suggested.** The six instances I found while drafting were not the tip of an iceberg. **But
the three that are real include the most serious one yet.**

---

## ⚠⚠ FIND 1 — a core system's founding document says it was never applied

**`PROPOSAL-VITALITY-01.md`, line 3:**

> **⚠ NOT APPLIED. This is a proposal. 84 references across 23 documents depend on the
> current system.**

**It was applied. `PT-559` is an owner ruling that adopted it**, and says so in its own
second line:

> **`PT-559` — ⚠ ONE POOL. `wound points` are removed from the game.**
>
> *"Owner ruling. `rules/PROPOSAL-VITALITY-01.md` written first; 84 references across 23
> documents, 49 of them mechanical."*

**The single-pool system is in force across the corpus.** `SPACE-COMBAT-01` builds ships on
it explicitly — *"a ship has Vitality, like everything else — **the single-pool
architecture**"* — and `DEATH-AND-DIFFICULTY-01` carries `PT-559`'s thresholds as live rules.

**This is the most serious instance found.** It is not a stale numeral or a fossil title —
**it is the founding document of the damage system every character, beast, droid and
starship in the game runs on, telling a reader it was never adopted.**

**⚠ A discipline note on how nearly I got this wrong.** Four documents matched my
"single pool" search, and **two of them were about something else entirely** —
`ATTACKS-01` and `ACTION-ECONOMY-01`'s *"one pool"* is the **reaction** pool, a different
subject with the same words. **Only `SPACE-COMBAT-01` and `DEATH-AND-DIFFICULTY-01` actually
bear on vitality**, and the decisive evidence was `PT-559` itself, not any keyword match.

---

## ⚠ FIND 2 — a status line contradicted by its own body, and I propagated it

**`EVENTS-PLAN-01.md`, line 3:**

> **Status: ⚠ PLAN. Nothing researched yet — `PT-676`.**

**Its own body, further down the same document:**

> **⚠⚠ AND THE PHASES BELOW ARE MOSTLY SPENT**
>
>     PHASE 1 — KOTOR              ⚠ DONE. 13 + 4 records.
>     PHASE 2 — KOTOR 2            ⚠ MOSTLY
>     PHASE 3 — Mandalorian Wars   ⚠ NOT DONE
>     PHASE 4 — Tales of the Jedi  ⚠ DONE — "14 records, all unconditional"
>
> **⚠⚠ ONLY PHASE 3 IS UNTOUCHED. THE PLAN AS WRITTEN WOULD HAVE REDONE THREE PHASES OF
> FINISHED WORK.**

**The header says nothing is researched; the body says three of four phases are finished and
names the counts.** Exactly the `SPACE-COMBAT-01` title shape you already fixed.

**⚠ And this one is partly mine** — *though see the correction appended below, because this
claim turned out to be wrong.* I read the header, believed it, and carried **"(PLAN ONLY,
`PT-676`)"** into an outline without reading far enough to find the body contradicting it.

> **✔ CORRECTION, after the source was fixed and I went to update my citation.** **It is not
> in `OUTLINE-02`.** The stale citation sits in **`OUTLINE-01.md:334`**, which is explicitly
> tombstoned at its own head — *"⚠⚠ SUPERSEDED — `OUTLINE-02.md`"* — and it was dropped from
> `OUTLINE-02` when I re-marked Book Five against the real rank-2 coverage.
>
> **So nothing of mine needs correcting, and I over-reported my own error.** The propagation
> happened and then was undone by later work, which I did not check before claiming it.
> **Recorded rather than deleted:** a self-accusation that turns out to be wrong is worth the
> same correction as any other wrong claim, and quietly removing it would leave the sweep's
> account of itself inaccurate.

---

## ⚠ FIND 3 — your `DROID-CONSTRUCTION-01` fix did not reach the document that mirrors it

**This is the sweep's most useful result, because it is a class of failure the earlier
flags did not surface: a correction applied to one document while a deliberate cross-record
of the same ruling keeps the old text.**

**`DROID-CONSTRUCTION-01 §6` is now correct** — Processor, Control Cluster and Vocabulator,
tiered 700 / 1,400 / 2,800, with the two worked examples you added.

**`DEATH-AND-DIFFICULTY-01 §6` carries the same ruling and was not updated.** It holds two
lines that **disagree with each other**:

**Line 236** — tiering correct, part names stale:
> *"the **motivator**, processor and **cell** are replaced… ⚠ `PT-608` tiered the part
> prices: 700 / 1,400 / 2,800 by chassis tier."*

**Line 244** — both stale, and flat:
> *"**`2,800` credits and one day: the MOTIVATOR, PROCESSOR CORE and POWER CELL**… so a
> destroyed Assassin droid costs `2,800` rather than `6,900`."*

**So within one section: one line says the cost is tiered, the next says it is a flat
2,800; both name a `Power Cell` that `PT-612` withdrew from the game.**

**The section marks itself as a deliberate mirror** — *"recorded here at `PT-653`"* — which
is what makes it worth fixing rather than deleting. **A reader consulting the death rules
rather than the construction rules gets the retired system.**

---

## What the sweep did *not* find — and I think this matters more than the finds

**My working hypothesis was that the six Armory instances indicated a widespread problem.
It does not. Three of my four search strategies returned essentially nothing**, and I would
rather report that plainly than dress up a thin result.

| Check | Scope | Result |
|---|---|---|
| Titles claiming plan/draft/proposal status | 102 documents | **2 candidates, 1 real** (Find 1) |
| Status lines claiming PLAN / PENDING / NOT | 102 documents | **1 instance, and it is Find 2** |
| Sections headed *Open* containing only closed items | 102 documents | **18 flagged, 0 confirmed** — see below |
| Retired droid part names | 102 documents | **1 real**, the rest legitimate item names |

**⚠ The *Open*-section check deserves its own note, because my scan over-reported by 18 to
0.** It flagged sections whose items were all marked ✓, on the theory that the heading had
gone stale. **Spot-checking killed it:** `DEATH-AND-DIFFICULTY-01 §6` has a genuinely open
item (*whether `Easy` mode's "whole party dies" means simultaneously or cumulatively*);
`SKILLS-01 §7` has two (*Astrogate and Ride scope*, *skill points per level*); and I already
knew `DROID-CONSTRUCTION-01 §7` had one, because Chapter Fourteen cited it.

**My regex only recognised open items that were *marked* open**, and this corpus states many
of them as plain sentences. **The pattern I was testing for does not exist — what exists is
an "Open" section that correctly tracks a mix, which is the flag-resolution convention
working exactly as ruled.**

**Two more clean negatives worth recording so nobody re-checks them:**

- **`PORT-01-v2`'s *"RULES-03 does not exist"* is correct.** There is no `RULES-03` in
  `rules/`; the document is accurately describing a real absence.
- **`CLASS-TABLES-BASE`'s *"twelve unwritten classes"* is not a build-state claim.**
  `CLASS-TABLES-AUTHORED` is subtitled *"the classes with no printed source"* — **"unwritten"
  there means *no published d20 source*, a permanent property of those classes**, not work
  outstanding. **Nearly filed as a defect; checking the neighbouring document settled it.**

---

## What I would fix, in order

**None of these are mine to edit — all three are rules documents.**

1. **`PROPOSAL-VITALITY-01`'s status line.** One line. **Highest value in the sweep** — it
   currently tells a reader the game's damage system was never adopted. Suggest it record
   that `PT-559` adopted it, and keep the original proposal text below, per the
   flag-resolution convention.
2. **`DEATH-AND-DIFFICULTY-01 §6`'s two lines**, to match the `DROID-CONSTRUCTION-01 §6`
   text you already wrote. **The internal contradiction between line 236 and line 244 is the
   part I would fix first**, since one of them is wrong whichever system is current.
3. **`EVENTS-PLAN-01`'s status line**, to match its own body. **And `OUTLINE-02`'s citation
   of it, which is mine and which I will correct once the source is settled.**

**The general lesson I would draw**, and it is the one Find 3 teaches rather than Find 1:
**when a ruling is deliberately cross-recorded in a second document, fixing the first one
does not fix the second — and the cross-record is exactly the place a reader who is not
looking for the primary will land.** A grep for the *retired term* rather than the document
name is what caught it, and would catch the next one.
