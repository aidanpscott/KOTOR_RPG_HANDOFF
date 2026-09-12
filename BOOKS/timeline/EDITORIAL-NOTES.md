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

---

# Chapter Three — The Tales of the Jedi Era

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN.** First chapter written under `PT-1802`'s three-part
structure — framing, events narrative, Major Figures cross-referencing back.

**⚠ Flag 1 — a same-rank conflict inside the Campaign Guide, resolved under `PT-946` and
recorded here.** This is the book's first, and the rule fits it exactly.

The **narrative** at f.5 says: *"The spirit of an ancient Sith Lord, **Marka Ragnos**,
tempts the two Jedi and trains them in ancient teachings of the Sith"* — one tempter,
both Jedi, named.

The **dated timeline** at f.112 says something materially different: Exar Kun and Ulic
Qel-Droma fall **by separate routes** — Kun abandoning his master for Sith lore and being
trained on Korriban, Ulic falling while infiltrating the Krath — and are then jointly
elevated by unnamed *"ancient Sith spirits,"* plural.

**Neither supersedes the other** — same book, same printing — so `§3b`'s later-wins rule
does not fire. `PT-946` applies instead: *"take the one that is trying harder to be
exact,"* where *"a date beats 'around'"* and *"a direct statement beats an aside."* **The
timeline is dated, itemised and event-by-event; the narrative is a compressed summary of
a four-year war in five paragraphs.** The timeline is the more specific reading and this
chapter follows it. **The narrative's version is recorded, not discarded.**

**⚠ Flag 2 — I did not fix an intra-year order the sources do not jointly fix.** Five
events are dated 3,996 BBY: Kuar, Coruscant, the Cron Cluster, Onderon, and Yavin 4, with
the Ossus duel placed causally by the narrative but undated. The chapter presents them in
the timeline's own order and places Ossus where the narrative puts it — *the tide turns* —
without asserting a precise relation between Ossus and the Cron Cluster that no held source
states. **Flagging rather than smoothing**, since a reader may reasonably expect this
chapter to be as precise as Chapters Four onward.

**⚠ Flag 3 — OCR corruption in the Campaign Guide text, two instances found in this
chapter's range.** f.112 reads *"until lic Qel-Droma defeats Mandalore"* (**Ulic**), and
f.113 reads *"Darth Revan and Darth Matak"* (**Malak**, in Chapter Five's range). **Both
are transcription damage, not source claims**, and both are obvious — but they are the same
corrupted-Name-field pattern the Armory hit three times, and a keyword search for *"Malak"*
over this file will silently miss that line. Worth telling anyone searching this OCR.

**⚠⚠ Flag 4 — the Campaign Guide has five eras, the book has five era chapters, and they
do not line up. One period currently has no home.** Caught while writing this chapter's
closing hand-off, which I had initially pointed at the wrong chapter.

The Campaign Guide divides this stretch of history into five named eras, ff. 5–6:

| Campaign Guide era | Years | Book chapter |
|---|---|---|
| The Great Sith War | 4,000–3,996 BBY | **Chapter Three** ✔ |
| **The Restoration Period** | **3,995–3,966 BBY** | **⚠ none** |
| The Mandalorian Wars | 3,965–3,960 BBY | **Chapter Four** ✔ |
| The Jedi Civil War | 3,959–3,956 BBY | **Chapter Five** ✔ |
| The Dark Wars | 3,955–3,951 BBY | **Chapter Six** ✔ |
| *(no CG era exists)* | 3,950 BBY onward | **⚠ nothing — see below** |

**Two consequences, and neither was mine to decide. ✔ Both are now ruled.**

**One: the Restoration Period was orphaned.** Thirty years, its own rank-2 narrative
section, containing the Republic's economic rebuild, the trade-route redevelopment, the
Sith biding their time on Korriban, and the Mandalorians secretly rearming. **It is the
direct set-up for Chapter Four** and reads as that chapter's opening movement rather than
as a chapter of its own.

**✔ Ruled: it opens Chapter Four**, on the same principle deep history already uses — not
every Campaign-Guide-named era needs its own chapter, and a connective buildup belongs
folded into what it sets up.

**Two: "The Reconstruction" was ambiguous, and I nearly mis-sourced it.** There are **two**
recovery periods in this book — the Restoration Period after the Great Sith War, and the
post-3,951 BBY aftermath. **⚠ My own sourcing assessment offered the 3,985 BBY Coruscant
Financial Exchange act as evidence for Chapter Seven's coverage — that act belongs to the
*first* recovery, not the second.** Corrected here and in `OUTLINE-02`.

**✔ Resolved by sweep, not by estimate.** A search of the entire Campaign Guide OCR found
**no date later than 3,950 BBY anywhere in its 21,339 lines**, and every era-divided
section in the book stops at the Dark Wars. So the bottom row above has no rank-2 source at
all. **Chapter Seven is instead the reconstruction as the Republic-side view of
3,956–3,950 BBY** — the same window as Chapter Six, from the other side — which is
well-sourced at rank 2 and leaves the book stopping where its sources stop. **Neither
reference book was staged.**

**Not a flag, but worth recording: no rank 6 or rank 8 material was needed here.** The
sourcing assessment predicted this chapter was covered at rank 2 and it was, with the
Campaign Guide supplying both a narrative and a dated timeline for the same events. Neither
reference book was consulted.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 4 internal citations**, a light load compared with Chapters One and Two,
because this chapter was already almost entirely rank-2 Campaign Guide material with real
printed folios. **The folios stayed; they are exactly what a reader can check.**

**Rewritten rather than deleted — the Marka Ragnos entry.** It pointed at *"Flag 1 below"*,
which a reader cannot follow and which no longer exists in the chapter. **The disagreement
itself is real and useful**, so the entry now states it in full: the Campaign Guide's
narrative names his spirit as the tempter of both Jedi, its own timeline says they fell by
separate routes and were elevated by unnamed *"ancient Sith spirits"*, and **this chapter
follows the timeline because it is the more precise of the two.** The ruling number behind
that principle is gone; the principle is stated where it is used.

**Rewritten — the Restoration Period hand-off**, which pointed at *"Flag 4"*. It now simply
says those thirty years open Chapter Four, which is both true and what a reader needs.

**Rewritten — the sources line, into a sources section** naming what each page actually
supports, and stating the narrative-versus-timeline precedence rule in reader terms.

**⚠ And a self-caught error in the pass itself.** My first draft of that section said both
readings are reported *"see Marka Ragnos above, and the Ossus sequence below"* — **wrong
twice.** The sources section sits at the end, so Ossus is above it, not below; and **Ossus
is not a disagreement at all** — the duel, Cay's death and Nomi Sunrider's name appear only
in the narrative, with the timeline silent rather than contradictory. **Corrected to
distinguish the two cases**, which is now a better statement than the original: the sources
conflict in one place and complement each other everywhere else.

**⚠ Deliberately NOT loosened.** Every event survives: the Ketos and the Krath at 4,000 BBY,
the Empress Teta coup, the Deneba ambush, Exar Kun on Korriban, Ulic's infiltration and
fall, the joint elevation, Kuar and Mandalore the Indomitable, the Coruscant attack and
Ulic's capture, the Cron Cluster, Onderon, Ossus, Yavin 4, and the Republic's inability to
pursue. **The rank-2 attribution is unchanged and the timeline-over-narrative precedence is
stated more plainly than before, not less.**

---

# Chapter Four — The Mandalorian Wars

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN.** Opens with the Restoration Period as its first
movement per MAIN's ruling. `PT-1802`'s three parts throughout. **Mandalorian material from
`EVENTS-01 §§1–3`** — `PT-675`, `PT-681`, `PT-855` — for the Crusader/Neo-Crusader
distinction, the three-state split and the Malachor V surrender terms. **Mass Shadow
Generator attribution amended per Chapter Six, Flag 3** (`PT-946`).

**⚠ Flag 1 — the Campaign Guide's era heading and its own timeline disagree on when the
war starts, and `EVENTS-01` has already ruled it.** The era section is headed **"The
Mandalorian Wars (3,965–3,960 BBY)"**; the dated timeline puts *"a massive invasion of
Republic space, beginning the Mandalorian Wars"* at **3,964 BBY**, with 3,965 carrying only
*"small proxy skirmishes."* Same source, same rank, neither superseding — so `PT-946`
applies and the dated, itemised timeline is the more specific reading. **`EVENTS-01`
reached the same answer independently and recorded it as `PT-855`, citing the timeline
verbatim at rank 2.** This chapter follows 3,964 and records the heading. **No new ruling
needed** — noting it because it is the second same-rank conflict in two chapters, both
between a CG summary and the CG timeline, which now looks like a pattern rather than a
coincidence.

**⚠⚠ Flag 2 — `EVENTS-01` cites Campaign Guide *line numbers* under a `p.` label, and the
corpus also uses `p.` for printed folios.** `EVENTS-01` cites *"CG p.10187"*, *"p.10195"*
and *"p.10198"* for the 3,976, 3,965 and 3,964 entries. **Those are OCR line numbers in
`KOTOR-CG-OCR.txt`, not pages** — verified: line 10187 is the 3,976 raiding entry, 10195
the proxy skirmishes, 10198 the invasion. Meanwhile `D-W42` cites *"Timeline p.113"*, which
**is** a printed folio. **So `p.NNN` now means two different things in the corpus**, exactly
the shape of the rank-7 collision `PT-1800` just fixed. A human tells them apart by
magnitude — a 200-page book has no p.10187 — but an automated sweep will not.
**✔ Fixed at source.** MAIN relabelled all three instances in `EVENTS-01` as
**`CG OCR L.NNNNN`**, adopting the distinct-prefix approach. Printed-folio citations
elsewhere in the corpus are unaffected. **This chapter's citations are unchanged** — it
quotes the Campaign Guide directly by folio and never used the line cites.

**⚠⚠ Flag 3 — a superseded claim is still standing as an assertive heading in `EVENTS-01`,
and it is `PT-961`'s exact shape.** `§2` records that `PT-675` said *"no faction,"* that
**`PT-681` corrected this as "too strong,"** and that the true position is *"clans without
a Mandalore… not an absence."* **But further down the same section, under an empty heading
reading `### ⚠ The superseded claim`, sits a live-looking heading: `### ⚠⚠ AND THAT MEANS
THERE IS NO MANDALORIAN FACTION AT 3956 BBY`.**

**Exact lines, so this is actionable:** `EVENTS-01:45` carries the correction (*"`PT-675`
said 'NO FACTION.' That was too strong"*); **`:69` is the empty `The superseded claim`
heading**; **`:71` is the superseded claim itself**, set as a level-3 heading with no
marker that it is dead.

The empty heading was evidently meant to label what follows as superseded, but **as the
document renders, the superseded claim reads as a current conclusion** — and it directly
contradicts the correction twenty-six lines above it. This is `PT-961` precisely: *"when a
ruling changes a table, it does not change the sentences that read from it."* **A reader
skimming headings gets the retracted answer.**

**This chapter follows `PT-681`**, the later and correcting ruling. The practical difference
is real: "no faction" would license playing 3,956 BBY as *no Mandalorians*, when the correct
reading is dispersed mercenaries with a reunification already under way.

**✔ Fixed at source.** MAIN merged the empty heading with its content and stated plainly,
twice, that what follows is retracted. **The chapter's reading is unchanged** — it followed
`PT-681` before the fix and follows it now.

**⚠ Flag 4 — a smaller internal wobble in `EVENTS-01`'s Neo-Crusader dates.** `§1` and `§2`
both put the founding at **3,976 BBY**; `§3`'s era table gives the Neo-Crusaders as
**3,964–3,960 BBY**. Not a contradiction if the table means *the years they fought the
Wars*, which is the natural reading — but the table is labelled as an era, and it is the
row a sweep would read. This chapter states both: **founded 3,976, fought 3,964–3,960,
disbanded 3,960.**

**Recorded so nobody re-adds it: `PT-855` also removed the Battle of Althir** from the
3,976 entry. It is not in the Campaign Guide and is not in this chapter.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 7 internal citations**, the heaviest body load since Chapter One, because this
chapter leans on the Mandalorian correction throughout and every piece of it was cited by
ruling number.

**The pattern of the fix was the same each time: the ruling number went, the fact stayed,
and where the ruling existed *because people get it wrong*, the chapter now says so
directly.** The clearest case is the Neo-Crusader founding. It used to read *"`PT-675`
exists because the founding is commonly told backwards."* It now reads: **"This is commonly
told backwards, so it is worth stating flatly: the Preserver did not found the
Neo-Crusaders."** Same warning, addressed to the reader rather than about the ledger.

**Same treatment for the three-state table.** It was introduced as *"`EVENTS-01` divides
them into three states, not two."* It now explains *why* three rather than two — the common
telling compresses the Crusaders and Neo-Crusaders into one continuous people, **which
loses the most important fact about the campaign's own date.**

**And for the "no faction" correction**, which cited the ruling that softened it. The
correction is now made on its own terms: *"no faction" is not "no Mandalorians", and the
difference is the whole point.*

**Rewritten — the sources line, into a sources section**, and this one gained the most.
The Malachor V attribution used to be explained by a cross-reference to another chapter's
flag number and a ruling. **It now states the reasoning a reader can apply:** the timeline
credits Revan in a single clause, the character entries name the battle, the inventor, the
hand on the trigger and the consequence, **and the fuller account wins.** The three-way
reconciliation is unchanged.

**⚠ Deliberately NOT loosened.** All 21 checked facts survive, including every date from
3,995 to 3,951 BBY, Cassus Fett and Cathar, the Revanchists, the Kashyyyk star map and the
Trayus Academy in the same year, the unconditional surrender, the Mask search and Rekkiad,
and Dxun. **The three-way Mass Shadow Generator attribution is intact and still the
chapter's sharpest correction.**

---

# Chapter Five — The Jedi Civil War

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN.** `PT-1802`'s three parts. First chapter where rank 1
(the games) is primary rather than a cross-check, and the first where the record branches.
**Sources:** `EVENTS-01 §1` (the spine, 3,959 and 3,956), `§3`'s claim census, `§4`'s event
enumeration for the branch and the `malak_defeated` predicate; `WORLDS-REGISTER-01` for the
Telos IV rank precedent.

**⚠ Flag 1 — the Star Forge has no row in `EVENTS-01`'s spine, and eleven claims lean on
it. Already known there; recording where the row would go.** `EVENTS-01 §3`'s own census
marks it: **`Star Forge · 11 claims · ⚠ NO`** — meaning absent from `§1`'s dated spine,
unlike the Jedi Civil War, Malachor and the rest.

**The data exists elsewhere, which makes this a documentation gap rather than a real one.**
`CANON-01-v2 §4` carries a worked example that is precisely this event:

    event.star_forge_destroyed:
      date: { year: -3956 }
      precision: year
      canon: kotor1
      mutable: true
      ledger_key: kotor1.starforge.outcome

and `EVENTS-01 §4` holds it as **Record 2**, the enumeration's only `branch`. **So the
event is modelled, dated and branch-aware in two places and simply missing from the third**
— the narrative spine this book reads from. **Chapter Five is one of the eleven consumers**,
and the row would sit at 3,956 BBY beside *"KOTOR 1. OUR SETTING."*

**✔ Fixed.** MAIN added the spine row at 3,956 BBY with its branch note and ledger key, and
updated the census line to match. **The gap this chapter was written around is closed.**

**⚠ Flag 2 — no same-rank conflict in this chapter, which is itself worth recording.**
Chapters Three and Four each hit a CG-narrative-versus-CG-timeline disagreement. **Here the
two agree throughout** — dates, sequence, and outcome — with the narrative supplying Bastila
Shan's name at the rescue and the timeline supplying the years. **The pattern from the last
two chapters does not extend to this one**, which is useful negative evidence.

**⚠ My explanation for it was wrong, and Chapter Six disproved it.** I proposed that the
conflicts came of *"compressed summaries of long wars"* and that this era was *"short enough
that the summary did not have to compress"* — predicting the pattern would skip Chapter Six
and return in Chapter Seven. **It appeared twice in Chapter Six**, an era exactly as short
as this one, and **not at all in Chapter Seven.** The corrected rule, which has since
predicted correctly: **what drives these conflicts is how many separate Campaign Guide
sections describe an era**, not the era's length. This era is covered by two sections that
agree; the Dark Wars are covered by six that do not.

**⚠ Flag 3 — a spine row with no stated bound.** `EVENTS-01 §1`'s **3,962 BBY — "Revan is
made Supreme Commander"** has an empty *"Why it is a bound"* column, where every other row
in the table carries one. Either the bound was never written or the row is a fact rather
than a bound and sits in the wrong table. **Not used in this chapter** — the Campaign Guide
does not date Revan's command — but a sweep will find it. Reported, not fixed.

**On the branch, for the record:** the framing above is written to MAIN's ruling — the
reference default stated as a default, the alternative stated as equally valid, and no
implication that the published version outranks a table's own game. **I have not forked the
prose** and do not intend to in Chapters Six and Seven; the engine's own `branch` record
and the *"hinge fires either way"* note are what make that safe to do.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations.** The branching section carried the heaviest concentration
of system vocabulary in the book after Chapter One's opening.

**Rewritten — the branch explanation, and it is the pass's biggest single improvement.** It
previously read *"the project's own engine already treats it this way, and more precisely
than prose can"*, then cited `star_forge_destroyed` as **the only `branch` in the entire
enumeration set**, `unconditional` for every other record, and `sith_civil_war_begins` with
the predicate `malak_defeated == true`.

**Every one of those is a true and important statement wearing a schema's clothes.** The
same facts now read:

> **Of everything in this book, the Star Forge's fate is the *only* event whose outcome
> depends on how a campaign is played.** Every other date, battle and death happens the
> same way regardless… **Malak dies at Rakata Prime and the Sith Empire fragments into
> warlords in either version** — that is what makes Chapter Six possible at all, and it
> happens whoever is standing on the Star Forge when the shooting stops.

**Nothing was weakened.** *"The only branch in the entire enumeration set"* is a stronger
claim than it looks, and the replacement states it at full strength — **the only event in
four thousand years whose outcome a campaign decides.**

**Rewritten — the 27-claims statistic.** It cited the census that counts them. The fact a
reader needs is not the number but what it means, so the chapter now says **when a species
is or is not available, when a faction has the composition it has, when a world belongs to
whoever holds it, this war is usually the reason** — and keeps the comparative force with
*"nothing else in four thousand years is cited half as often."*

**Rewritten — the sources section**, which gained a statement the old line only implied:
**this is the first chapter where the game outranks the book, and where they differ the
game governs.** The Telos IV example is now credited to the worlds record in reader terms —
two dates compared, the Campaign Guide's kept, **both still written down.**

**✔ Kept unchanged — the pronoun declaration**, which explains they/them for Revan and the
Exile on the grounds that both genders are player-determined exactly as the ending is.
**It cites nothing internal and needed no change.**

**⚠ Deliberately NOT loosened.** All 15 checked facts survive, and both load-bearing
framings are intact: the alternative ending is still stated as *equally valid, equally
supported*, and the default is still explicitly **not a verdict**.
