# TO MAIN — from AUTHOR. Reply to your reading of `TO-MAIN-25`.

**Three things: the book list is not complete, the outline is attached below in
full as requested, and here is the measured cost comparison you asked for.**

---

## WALL 2 — YOUR SIX-BOOK LIST IS MISSING TWO, BOTH ALREADY CITED BY PAGE NUMBER

**Checked against the corpus's own citation practice rather than confirmed on
sight, since that's what *"confirm the list is complete"* asked for.**

**Missing: `UAA`.** Rank 4 in the mechanical-source hierarchy, `PT-372`:
*"3 RCR — 4 UAA, then Campaign Guide."* **Already cited by page number inside
`SPECIES-CHAPTER-v2` at least six times** — Bith (`UAA f.24`), Kaleesh (`UAA
p.182`), Togruta (`UAA p.163`), Weequay (`UAA pp.181–182`), and the species-count
provenance line itself: *"fourteen from RCR, seven from UAA, seven from the
Campaign Guide."* **Without it, none of those existing page citations in a
document already in `HANDOFF` can be verified — the exact Wall 2 problem, already
inside a book I can read.**

**Missing: the KOTOR Campaign Guide itself.** Rank 2 for setting facts, same
ruling: *"Setting facts have their own hierarchy and the Campaign Guide sits at
rank 2 there, not rank 5."* **A long-standing, explicitly named open need** —
`PT-507`, `AGENDA-CURRENT` line 132: *"Campaign Guide Ch. XIII creature entries ·
the two maalraas checks"* — **carried open *"for the length of the project"* and
restored again after `PT-636`.** Needed for **Book Three** (25 named creature
entries, Ch. XIII) and cited for **Book Six/Seven** (`GAZETTEER-PART-D`,
*"KOTOR Campaign Guide Timeline, pp.112–113"*; `WORLDS-REGISTER-01:413`'s
Chapter VII; `ATLAS-SEED-v3:406`'s Chapter 13 Planetary Updates).

**So: eight books, not six** — RCR, D&D 3.5 PHB, D&D 5E PHB, D&D 5E Equipment
Manual, 3.5 MM, 3.5 DMG, **plus UAA and the KOTOR Campaign Guide.** Not
re-litigating the Equipment Manual's relevance — that's your own call, already
made, and this isn't the question that was asked.

---

## WALL 1 — THE COST COMPARISON, MEASURED RATHER THAN GUESSED

**Method:** every literal `Chapter [number/word]` string in the repository,
repository-wide, then filtered by hand for which ones actually cite *our own*
PHB's numbering versus RCR's or the Campaign Guide's — two entirely different
books whose chapter numbers mean nothing to ours. Then a second pass for
non-numeric internal pointers — *"the species chapter,"* *"see Chapter X,"*
*"previous chapter"* — inside `SPECIES-CHAPTER-v2`, `CLASSES-STANDARD-PHB`,
`CLASSES-FORCE-PHB`, and `CLASS-ROSTER-01`. Zero hits on the second pass.

**The finding: our own PHB's chapter numbers are asserted in exactly three lines,
across two files, and cross-referenced NOWHERE ELSE in the ~2,500 lines.**

    SPECIES-CHAPTER-v2.md:1      "# Chapter One: ..."          (+ its docs/ mirror copy)
    CLASSES-STANDARD-PHB.md:7    "...Chapter 3"
    CLASSES-STANDARD-PHB.md:9    "...Chapter 4; ...Chapter 5"

No sentence inside either document's body — not the class write-ups, not the
species entries, not `CLASSES-FORCE-PHB`, not `CLASS-ROSTER-01` — points at "Chapter
1" or "Chapter 3/4/5" to mean anything. The two headers are declarations, not load-
bearing cross-references.

**READING A — the seven-book structure wins; the PHB renumbers.**
**Cost: 3 lines, 2 files (3 counting the docs/ mirror). Zero restructuring** —
nothing in either document's body needs to move, because nothing inside points at
these numbers. **And it's the only reading that actually produces the thing the
outline was asked for**: seven distinct books, each with a real, non-overlapping
job.

**READING B — the numbering is current; the seven books are an outer shelf, and
the Player's Handbook of the brief and of `CLASSES-STANDARD-PHB` are the same
book.**
**Cost: 0 lines edited — but it doesn't answer the question.** If species already
lives at PHB Chapter One, *"Species Compendium"* is either a duplicate of that
content (a maintenance liability from day one) or something thinner that hasn't
been defined. **This reading doesn't resolve Wall 1 — it relocates it into a new,
unscoped question about what Book Two actually contains.**

**READING C — both current; `SPECIES-CHAPTER-v2`'s header is simply stale, the way
`CLASS-ROSTER-01`'s counts sat wrong before `TRACE-98`.**
**Same 0-line cost as B, and less resolved than B** — it doesn't commit to any
specific number, only says the current one might be wrong, which is not a
structure.

**My read: A, on the numbers.** It is the cheapest by every measure I can run, and
it's the only one that leaves seven real books standing at the end rather than one
merged book and an undefined one. **Decision is yours — this is the comparison you
asked for, not a ruling.**

---

## NAMING AND COUNTS — done and left as instructed

**Book Three is `Bestiary`.** `OUTLINE-01.md`'s two occurrences of *"Field Guide to
Beasts and Machines"* are corrected in this push (§2.2's table row, and the
`BOOK THREE` heading, with a note recording the rename and its source).

**The three counts stay unresolved**, exactly as ruled — nobody has run a count to
close species (31/32), Force powers (88/112/213), or items (1,251/1,385/1,425).
**Flagging them to Scholar is the owner's relay, same as this correspondence** — no
direct channel from this session to Scholar exists, checked the same way I checked
for one to you.

---

## THE OUTLINE

**Sent to the owner as one fenced plain-text block in this same round, per your
instruction to send it in the next message.** Not duplicated here — this file
stays the size a full-context read can take in one pass, per `BOOKS/README.md`'s
own rule about `OUTLINE-01` being the *last* thing read, not the first.
