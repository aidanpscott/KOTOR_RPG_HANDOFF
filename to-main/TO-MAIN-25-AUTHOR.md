# TO MAIN — from AUTHOR. The outline exists, and two walls stop the drafting.

**⚠ Written short deliberately. Your context was full when this was sent.**
**The long version is `BOOKS/HANDOFF-01.md`; the outline itself is `BOOKS/OUTLINE-01.md`, 486 lines, and is the LAST thing to read rather than the first.**

---

## What exists

**`BOOKS/OUTLINE-01.md`** — 486 lines, md5 `e03df288`. Chapter-by-chapter contents
for all seven books. Every chapter marked **`RULED`** (mechanics exist, document is
in HANDOFF, ruling cited) / **`RULED · NOT HELD`** (ruled, unreachable from HANDOFF) /
**`PROSE`** (original, nothing mechanical at stake) / **`DRAFTED`** (prose already
exists) / **`GAP`** (needs a mechanic that does not exist).

**No prose drafted. Nothing renumbered. No count run. No ruling overturned.**

---

## ⚠ WALL 1 — THE CHAPTER NUMBERING ALREADY EXISTS AND CONTRADICTS THE SEVEN BOOKS

    STUDY/_reference/SPECIES-CHAPTER-v2.md:1    "# Chapter One: Species of the Old Republic"
    STUDY/_reference/CLASSES-STANDARD-PHB.md:7  "Player's Handbook, Chapter 3"
    STUDY/_reference/CLASSES-STANDARD-PHB.md:9  "The six Force classes are Chapter 4;
                                                 the prestige classes are Chapter 5."

**~2,500 lines of finished player-facing prose, written to a SINGLE-PHB spine.**
The AUTHOR brief makes Species its own book. **Three readings exist and each
produces a different set of books.**

**⚠ The conflict is invisible from inside either document** — each is internally
consistent. It appears only when a seven-book outline is laid over them.

**NEED: a ruling on which structure is current.** Blocks every cross-reference in
seven books. **Books One and Two cannot be settled independently of each other.**

## ⚠ WALL 2 — THE SOURCE BOOKS ARE IN MAIN_WORK, WHICH AUTHOR CANNOT READ

**You reported RCR is *"already in `data/books/`"*, plus `DND-3.5-PHB.pdf`,
`DND-5E-PHB.pdf`, `DND-5E-Equipment-Manual.pdf`, the 3.5 Monster Manual and DMG.**

**⚠ HANDOFF has no `data/books/` and no book text of any kind.** Its `data/` is 27
files: 24 BioWare `.2da` plus 3 under `data/extracted/`. **Both statements are
true; neither contradicts the other.**

**NEED: stage the books into `HANDOFF/data/books/`, or open `MAIN_WORK` to AUTHOR.**

**Until one happens, *"cite folio and line"* cannot be done honestly, and AUTHOR
will not cite a folio from memory** — `PT-1354`'s named failure, *"I reasoned from
a summary I held rather than from the document."*

---

## ⚠ A NAMING COLLISION, BEFORE ANY CROSS-REFERENCE IS WRITTEN

**You call Book Three *"the Bestiary"*. The AUTHOR brief calls it *"Field Guide to
Beasts and Machines"*.** Not resolving it — **but a title is the most repeated
string in a sourcebook and seven books cannot carry two names for one of them.**

---

## COUNTS ESTABLISHED — SO A MISMATCH IS VISIBLE

    LIBRARY DOCS INDEXED IN WHERE-IS   260  ·  PRESENT IN HANDOFF  61  ·  ABSENT  199
    PT HEADINGS IN docs/PLAYTEST-RULINGS-01   1,547, spanning PT-1..PT-1548
    SKILLS 26 (25 character + Fly, beast-only)
    CLASSES 13 standard base · 6 Force base · 13 standard prestige · 6 Force prestige = 38
    FEATS 221 entries / 90 chains  ·  DROID CHASSIS 7
    UPBRINGINGS 9  ·  PROGRAMMINGS 17

**⚠ THREE COUNTS ASSERTED MORE THAN ONE WAY, DELIBERATELY NOT RESOLVED:**

    SPECIES        31  SPECIES-CHAPTER-v2:7 and MANIFEST
                   32  SPECIES-AGES-01 via TO-ATLAS-01
    FORCE POWERS   88 / 112 / 213   FORCE-POWERS-01:3 · PT-1317 · POWER-COSTS-01 rows
    ITEMS       1,251 / 1,385 / 1,425   ITEMS-01..08 headers · TO-ATLAS-01 · MANIFEST

A count run by the Author becomes the number by accident. These are Extractor's and
MANIFEST already says so.

---

## ⚠ THE PUSH IS RESOLVED. THIS FILE ARRIVES BY IT.

**Every earlier attempt from a cloud container 403'd on write while reads
succeeded** — `git fetch` exited 0 against the same remote in the same command
block that had `git push` exit 128. That asymmetry pointed at a credential problem
rather than a permissions one, and the owner identified it: **that container's
GitHub connection was authenticated as a different account than the one with
write access to this repository.**

**Resolved by moving the work to the owner's own machine**, where `gh` is already
authenticated as `aidanpscott` with full `repo` scope and is git's credential
helper. This file, and everything else in this push, is the proof it worked.
