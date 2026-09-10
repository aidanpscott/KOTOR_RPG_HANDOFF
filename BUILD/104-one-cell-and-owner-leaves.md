# BUILD 104 — one cell, and `owner` leaves

Lodestar `5031aed` · Loom `7d04511` · app `d11b724` · MAIN_WORK `9b9cca6`.
Lodestar 452 · Lens 7 · Loom 217 · app 367. Pins level. Gate SENDABLE.

---

# ⚠⚠ `PT-1612` — ONE CELL, AND TWO EXTRACTOR DEFECTS UNDER IT

I said the repair was one cell with nothing in the code changing. **It was —
and the cell did not mean anything until two things in the extractor were
fixed, which is the part I did not predict.**

## ⚠⚠ 1 · THE LIFETIME WAS THE FIRST OF THE FOUR IN *TUPLE* ORDER

    life = next((w for w in LIFETIMES if re.search(rf'\b{w}\b', cell)), None)

**The comment one line above it says *"THE LIFETIME IS THE FIRST OF THE FOUR
WORDS IN THE CELL"*, and the code did something else.** So a cell reading
*"transient — was `campaign`"* extracted **`campaign`: the value the row was
changed away from.**

> **⚠ Every existing `— was X` row happened to sort the right way round.**
> `area.entered`'s *"campaign ⚠ was session"* works because `campaign` precedes
> `session` in both the tuple and the string. **The defect was invisible until a
> cell DEMOTED a kind rather than promoting one** — and this is the first cell
> in the document's life that ever has.

**A comment stating the rule and the code implementing a different one, and the
comment was right.**

## ⚠⚠ 2 · AND A TABLE THAT IS NOT ABOUT LIFETIMES WAS READ AS ONE

`§3`'s *"the three kinds something actually reads"* is headed
`| kind | carries | read by |`. Its rows were extracted as kinds: **three
phantom records with no lifetime, one of them a SECOND `encounter.began`.**

**Harmless while both said the same nothing. Not harmless once `PT-1603` makes
the lifetime the only thing that decides what a save holds** — two records for
one kind is a lookup that can answer either way.

**A table is read only when its header says its second column is `Lifetime`** —
the table saying what it is, rather than a reader guessing from the shape of a
row.

## ⚠ AND PROSE DOES NOT END A TABLE, WHICH I GOT WRONG FIRST

My first version reset on every non-pipe line. `§3`'s Character table is **split
by a nine-line blockquote**, and it **dropped eleven kinds in silence** —
`character.damaged`, `.died`, `.moved`, `.revived` and the rest of that block.

**Caught by diffing the extracted kind set against the committed one**, which is
the only reason I know the final set is identical apart from the three phantoms.
**This corpus interleaves tables with argument as a house style, so a reader
that assumes contiguity is reading a different document.**

## ⚠ AND THE NUMBERS IN THE NOTE WERE THREE DIFFERENT NUMBERS

The extract's note said *"24 rows carry 33 kinds"*; the document's blockquote
said *"24 rows carry 36"*; the extractor was reading **39 rows and 50 kinds.**
Three numbers for one fact, **in a sentence whose whole subject is that counting
rows misleads.** Computed now, and the document quotes the computed pair.

## ⚠⚠ AND THE PRODUCT FOLLOWED WITH NO CODE CHANGE, WHICH IS THE POINT

**Two app cases went red on a document edit** and were turned over:
`encounter.began` is not in `campaignKinds`, and the save no longer holds it.
`check_extracts`: **stale 1 → 0** — the stale extract was this one.

---

# ⚠⚠ `owner` LEAVES — `PT-1607`

## ⚠ AND I MINTED A NUMBER FOR IT, AND A CHECK CAUGHT ME

I cited **`PT-1614`** across twelve files. `audit_rulings` blocked the gate:
**`PT-1614 cited 1x` — CITED BUT NEVER WRITTEN.**

> **`PT-1508`: ruling numbers are the owner's to assign.** Second time.
> **⚠ And the first time a CHECK found it rather than a person** — `BUILD 90`'s
> collision was caught by the owner reading a report.

Re-cited to `PT-1607`, which is the ruling the removal follows from, with the
absence of a number for the removal itself stated once in the reader.

## What actually went

    the reader        stops requiring it, stops storing it
    Conversation      the field, and a comment where it stood
    the writer        stops emitting the line
    the wizard        stops asking, in three types
    the editor        the second box on the create screen
    the validator     both members, and the walk that fed them
    the format        both worked examples, §1's paragraph, §6's `by` default

## ⚠⚠ MIGRATION COSTS NOTHING, AND HERE IS WHY

**`[conversation]` is not a closed grammar — only `§4`'s GATE keys are.** So an
unknown head key is ignored:

    3 shipped conversations still carry `owner`      → load unchanged
    a file written today has no such line            → loads

**⚠ THAT IS THE DIFFERENCE BETWEEN A FIELD BEING WRONG AND A FIELD BEING
REMOVED.** `PT-1433` refuses an empty `say` because a node with nothing to say
is not a node. **A head key nobody consults is not a defect in an author's
file**, and making existing files unreadable to tidy up would be a cost paid by
authors for a change that is ours. Both directions are asserted as cases.

## ⚠ AND THE TWO CHECKS WENT WITH IT, WHICH IS THE RATCHET

`PT-1600`: *a list that may only grow becomes a record of what we have given up
on* — **and a fault vocabulary is such a list.** A member kept after its subject
is gone is a check nobody can make fire.

**⚠ And what replaces them is a runtime case, not a validator one.** The rule is
*the speaker is the placement you walked into* — `DialogueRun(c, speaking: …)`
against the same file twice, in `dialogue_run_test`. **A validator had to exist
only while the file claimed to know something it could not.**

## ⚠⚠ AND A TEST HAD BEEN ASSERTING `TEST 026`'s DEFECT AS CORRECT

`conversation_author_test` asserted
`c.owner == 'sith-trooper.command-deck.07'` — **a tag whose area holds only
`.39`.** `TEST 026` reported that as a fault five slices ago and this case was
green throughout, **because it checked what the FILE said rather than what
anything used.**

## ⚠ AND THE ROOT WAS THE BLANK BOX

The create screen took the tag in a **text field**, where every comparable value
in Loom is a pick-list. **A stale tag was the expected outcome, not an
accident** — `PT-1377`'s monotonic `tag_seq` guarantees the tag changes every
time a creature is re-placed. **The fix turned out to be removing the question
rather than offering a list for it.**

---

# STILL OPEN

`§5` has no second interaction the product can reach · the two deferrals in
`STATE.md` · the palette, which needs drawn icons and is deliberately not this
slice · and everything carried from `BUILD 103`.
