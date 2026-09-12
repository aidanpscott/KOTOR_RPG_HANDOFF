# Galactic Timeline — Editorial Notes

**⚠ NOT PART OF THE BOOK. Internal record, for MAIN, Coder and the owner.**

**This file exists because of `PT-1844`.** The chapters used to carry their findings in an
*"Open items, carried from review"* section at the foot of each one. **Those sections cited
internal development documents and ruling numbers a reader cannot look up**, so they are
being moved here as each chapter is passed — **preserved, not deleted**, per the standing
flag-resolution convention.

**The chapters themselves now contain no internal citations.** Everything below is the
record of how they were built and what was found while building them.

---

# Chapter One — What This Timeline Is, And Isn't

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN.** Written after the sourcing assessment at
`TO-MAIN-44-AUTHOR.md` and the rulings that closed it. **Sources it stands on:**
`CANON-01-v2 §§2, 2.1, 2.2, 4, 10.0`; `METHOD-RECORD-01 §§2–3`; `WORLDS-REGISTER-01`
(`D-W3`, `D-W32`, `D-W42`); `PT-1800` for ranks 7 and 8.

**⚠ Flag 1 — `D-W32` drift, instance one.** `METHOD-RECORD-01` line 310 argues the New
Essential Chronology's usefulness *"despite ranking fifth,"* while every ladder in the
corpus — including the one about thirty lines above it in the same document — places it
**sixth**. A stale numeral left behind when `D-T` inserted *Dark Empire* at rank 5. The
argument is unaffected. Reported, not fixed; editing a rules document to correct a numeral
is not this book's call.

**✔ Flag 2 — the "rank 7" collision, raised and now closed by `PT-1800`.**

`WORLDS-REGISTER-01`'s `D-W32` assigns **Wookieepedia** a *local* rank 7 — *"For Atlas
purposes only… a local extension, not a change to `D-AB`"* — and that rank is live in the
register, carrying the Bith and Glee Anselm warrants, with `D-W42` recording others
**upgraded off rank 7 to rank 2**. Placing the two Essential Guides at rank 7 as well
would have put **two very different things under one label**: a wiki route meant to be
escalated off as soon as an underlying source is named, and an admitted Legends reference
book with a stable citation and nothing pending. A warrant reading "rank 7" would have
been ambiguous, and the wiki sense carries an active *needs-escalating* connotation the
reference books should not inherit.

**`PT-1800` moves them to rank 8**, leaving rank 7 to `D-W32`'s local extension. The
labels now separate cleanly and `D-W42`'s escalation history keeps its meaning.

**⚠ Flag 3 — the Campaign Guide OCR's page markers are not printed folios, and citations
built on them will be wrong by three.** `data/books/KOTOR-CG-OCR.txt` marks pages
`=== PAGE n ===`, but pages 1–3 are the cover, title page and credits, which carry no
printed folio. **Printed folio = OCR marker − 3.** Verified against two existing corpus
citations, both exact: `D-W42` cites *"Timeline p.113"* for Aleema Keto and the Cron
Cluster, which sits at OCR `PAGE 116`; `OUTLINE-02` gives the Campaign Guide timeline as
**pp. 112–113**, which spans OCR `PAGE 115`–`116`. **⚠ I reported this file as
"page markers enabling folio citation" in `TO-MAIN-44-AUTHOR.md` without stating the
offset** — true but incomplete, and anyone acting on it would have cited three pages high.
This book's citations use printed folio.

**✔ Flag 4 — `OUTLINE-02` cited `CANON-01-v2 §3.4` for this chapter; §3.4 is the wrong
section.** It is *"`requires` is a predicate, not a list,"* about the canon ledger's
requires predicate — nothing to do with how the timeline was built. The sections this
chapter actually stands on are **§§2, 2.1, 2.2, 4 and 10.0**. Same class of error as the
`D-CURRENCY-01` currency miscitation found in the Armory. **Fixed** — `OUTLINE-02`'s Book
Five row now cites the correct sections and records the superseded citation.

**Correction to my own sourcing report.** `TO-MAIN-44-AUTHOR.md` stated the Campaign Guide
timeline runs *"4,000 BBY through 3,976 BBY."* **It runs 4,000 BBY through 3,950 BBY** —
fifty years, not twenty-four — on pp. 112–113, and it covers the Mandalorian Wars, the
Jedi Civil War, the Sith Triumvirate and the start of the Reconstruction in dated entries.
**Chapters Four through Seven are better sourced than I reported**, and none of them needs
the reference books.

## ⚠ What the `PT-1844` pass changed in this chapter, and what it deliberately did not

**Removed — 21 internal citations**, including every reference to `CANON-01-v2`,
`METHOD-RECORD-01`, `WORLDS-REGISTER-01`, `DECISION-RECORD-04`, `D-`-prefixed decisions and
`PT-` numbers, plus the status line naming MAIN and `TO-MAIN-44-AUTHOR.md`.

**Rewritten rather than cut — the "not the authority on dates" passage.** It previously
explained itself with *"engine state,"* *"queried, never recalled from prose"* and *"the
model's priors"* — language assuming the reader knows there is a software system behind the
book. **The underlying fact is unchanged and is stated at the same strength:** this book
does not decide dates, it reports decisions made from checkable sources, and **if it
contradicts them the sources win.**

**Also rewritten:** the inverted-hazard section, which described *the model's* priors and
now describes the reader's — **the same claim, and true of both**; and the
geography-without-history section, which quoted an instruction about how *"the AI will
import a planet together with its history"* and now states the rule itself.

**⚠ Deliberately NOT loosened.** Every fact survives at its original strength: the four
canon layers, the films-not-yet-news point, KOTOR 3 left open, all eight ranks, the Telos
worked example, the separate rules ladder, all five exclusion tests, the April 2014
continuity bound, the *Dawn of the Jedi* false positive, deep history's looser terms, and
the note that Chapter Two is a different kind of chapter. **Nothing was softened to make a
citation removable.**

**One thing made *more* accurate by the pass.** The old rank-7 row read *"reserved —
`D-W32`'s local Wookieepedia extension, worlds register only"*, which is meaningless to a
reader. It now says what rank 7 actually means for someone using the ladder: **Wookieepedia
is a route to whichever published source underlies a claim, and a fact that can only be
traced to the wiki is a fact still waiting for a source.** That is the same rule, stated so
it can be applied.

---

# Chapter Two — Deep History

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN.** Written under the deep-history exception
(`METHOD-RECORD-01 §3`), narrative only with no Major Figures section per `PT-1802`, which
scopes that structure to Chapters Three through Seven. `SPECIES-CHAPTER-v2` and
`DECISION-RECORD-04`'s `D-Q` carry the Flesh Raider / Rakata relation.

**⚠ Flag 1 — three claims rest on the relay alone and are not in any source held here.**
The **Force-negating plague** and its ~25,200 BBY date, the **Jedi Order's establishment on
Tython**, and the **Battle of Corbos**. I searched the Campaign Guide OCR in full for
*Tython* and *Corbos*: **zero occurrences of either.** That is a correctly scoped negative
over the one deep-history source actually in `data/books/`, not over the whole corpus.
**All three are marked in the text as rank 6.** If the Chronology is ever staged, these are
the three passages to read directly and cite properly.

**⚠ Flag 2 — the Campaign Guide covers this chapter far better than the outline recorded.**
`OUTLINE-02` marks Deep History **`RULED · NOT HELD`**, sourced to three Library-held
documents (`RULING-SWTOR-DEEP-HISTORY`, `ERA-VITIATE-01`, `D-VIT-01`). **The Campaign Guide
in fact carries Adas by name, the 28,000 BBY unification, the Rakatan invasion of Korriban
and its outcome, the dark side as the Infinite Empire's bequest, the Hundred-Year Darkness
exiles, Ajunta Pall, Jen'jidai and Jen'ari, Tund, and the interbreeding — all at rank 2.**
The chapter's spine is rank 2, with rank 6 filling two gaps. **The outline mark understated
what is held.**

**✔ Fixed.** MAIN confirmed the mark wrong and `OUTLINE-02`'s Book Five row is re-marked
`DRAFTED` against the rank-2 coverage above. This was the third outline correction from
this book, after the `§3.4` miscitation and the timeline's extent; a fourth followed at
Chapter Three, Flag 4.

**⚠ Flag 3 — a possible tension between the relay and rank 2 on the Rakatan invasion,
recorded rather than resolved.** The relay has Adas *repel* the Rakatan attack. The
Campaign Guide has him *"conquer the conquerors, sacrificing his life in the process,"*
with the Sith then taking Rakatan technology and the dark side from the encounter. **Rank 2
governs and the chapter follows it**, and the two are probably the same event told at
different resolutions rather than a real contradiction. Recorded because the ladder's rule
is that disagreements are written down, *"never silently resolved downward."*

**⚠ Flag 4 — the one-hundred-thousand-year figure is not reconciled with anything.** The
Campaign Guide opens the Sith story *"one hundred thousand years"* back, then gives Adas at
28,000 BBY. Nothing in the corpus describes the seventy-two thousand years between. Not a
gap this chapter can fill and probably not one worth filling — but it is a stated anchor
with nothing behind it, and a future sweep will trip over it.

**Not flagged, deliberately: the Republic's founding date.** The Campaign Guide dates the
Rakatan invasion *"three thousand years before the founding of the Republic"* without
giving that year, so this chapter keeps the relation rather than computing a date from a
figure no held source states. Under the evocative-not-tracked standard that is the correct
handling, not an omission.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 9 internal citations**, plus the status line naming MAIN, `METHOD-RECORD-01`
and `PT-1802`.

**Rewritten rather than cut — the deep-history standard itself.** It previously explained
the looser terms with *"produces no temporal facts… cannot be pending, cannot fire, cannot
leak, and cannot be averted"* and *"world-bible content"* — the scheduling vocabulary,
which assumes a reader knows there is a system with pending events in it. **The fact is
unchanged and stated at the same strength:** nothing before 4,000 BBY can come due during a
campaign set in 3,956 BBY, be set off by the party, or be prevented by them. **It is
background rather than chronology.**

**The no-Major-Figures note was kept but re-justified.** It used to cite the ruling that
scopes the structure; it now gives the reason — a formal roster would fight the looser
standard.

**Rewritten — the Chronology sourcing note.** *"Rests on the relayed Chronology account"*
told a reader nothing they could act on. It now names the volume, states that the whole
Campaign Guide text was searched for Tython and Corbos without a hit, and **tells the
reader which book to open if it matters to them.**

**Rewritten — the sources line, into a real sources section.** The Campaign Guide folios
were already checkable and are kept, now with what each page actually supports. The
internal document names are gone; the Flesh Raider relation is credited to this game's own
Species material without naming a file.

**✔ Kept deliberately — every rank marking**, five in total. A source-confidence flag tells
a reader something true about how far to trust a claim, and Chapter One now explains the
ladder they refer to. **These were never the problem.**

**⚠ Deliberately NOT loosened.** All sixteen checked facts survive at original strength:
the Infinite Empire and its Force-powered technology, the Star Forge and Lehon, the Flesh
Raiders' descent, the hundred-thousand-year Sith anchor, 28,000 BBY, King Adas and
Sith'ari, Tund, the Rakatan invasion and its outcome, the dark side as bequest, the
25,200 BBY plague at rank 6, Tython, Corbos, the Hundred-Year Darkness, Ajunta Pall,
Jen'jidai and Jen'ari, the interbreeding, and the Kashyyyk star map hand-off. **The rank-2
versus rank-6 distinction on the Rakatan collapse is stated exactly as before.**
