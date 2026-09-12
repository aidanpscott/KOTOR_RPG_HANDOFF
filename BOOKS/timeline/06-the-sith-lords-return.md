# Chapter Six — The Sith Lords' Return

**Status: DRAFT, for review.** `PT-1802`'s three parts. The Campaign Guide calls this era
**the Dark Wars**, 3,955–3,951 BBY.

---

## ⚠ A different reading contract from here on

**Every chapter before this one described the reader's past. This one describes their
future.**

The campaign's default clock is **3,956 BBY** — `EVENTS-01`'s spine marks it *"KOTOR 1. OUR
SETTING."* **The Dark Wars begin the year after it and end five years later.** So a
Gamemaster running the default date is reading, here, an account of things that **have not
happened yet** and which their table may well prevent, cause, or replace.

**Treat this chapter as the setting's own forecast rather than its record.** It is what the
sources say becomes of the galaxy if nobody at your table intervenes — and the whole point
of running a campaign in 3,956 BBY is that somebody is about to.

Chapters Three through Five constrain play. **This one is raw material for it.**

---

## The events

### 3,955 BBY — an empire with no one left to hold it

Malak's defeat does not end the Sith. It removes the only thing holding them together.

> After Darth Malak's defeat at the Battle of Rakata Prime, the forces of the Sith fall
> into chaos. Retreating from continued attacks by the Republic, **the Sith Empire
> fragments into hundreds of smaller territories ruled over by Sith warlords.**

*"Sith Lords, formerly loyal to Darth Revan and Malak, begin breaking the Sith Empire into
smaller domains, declaring themselves sovereign warlords."*

**This is the predicate from Chapter Five firing.** `sith_civil_war_begins` has the
condition `malak_defeated == true`, and `EVENTS-01` calls it *"the event that turns Malak's
Empire into the warlords — one row in an event table is the hinge of an entire faction
tree."* **The chapter you are reading is what that row expands into.**

And for a moment it looks like good news: *"The few remaining Dark Lords of the Sith fight
with one another over the scraps of their Empire, damaging themselves as much as the
Republic. While the Republic rebuilds its forces, **the Sith seem content to eradicate
themselves.**"*

**The Republic's mistake is understandable and total.** An enemy tearing itself apart looks
like an enemy solving your problem.

### 3,954 BBY — the hunt

What the fragmentation actually produced was a selection process. *"Sith survivors wage
civil war, **culling the weak and electing leadership by the lightsaber's blade.**"* What
came out the other side was smaller, harder, and pointed somewhere new:

> This new Sith blood executes a **divide-and-conquer tactic, targeting the Jedi for
> eradication**, while the Republic, also reeling, is unable to defend them.

*"Sith assassins, under orders from **Darth Sion**, begin a widespread assassination
campaign against the Jedi."* The result is stated without hedging: *"The Jedi are all but
wiped out, and **the Republic is left without its Jedi defenders for the first time in
centuries.**"*

**Read that against Chapter Three.** The Order that survived the Great Sith War by turning
inward for thirty years, and preserved itself through the Mandalorian Wars by refusing to
fight, is destroyed here — **by a campaign of individual murders**, without a single battle
worth the name.

### Katarr — the worst decision anyone in this book makes

**About a hundred Jedi were left alive in the galaxy.** Nearly all of them went to one
planet, and one Sith Lord killed all of them at once.

The Campaign Guide gives the gathering's purpose plainly: *"To divine the identities of
their hunters, **Master Vandar Tokare** meets with most of the hundred surviving Jedi on
the planet Katarr."*

> It is just the moment that the Sith Lord **Darth Nihilus** has been waiting for. Through
> an unholy dark-side technique, **Nihilus murders every living being on Katarr**, including
> Master Tokare.

**Every living being.** Not the Jedi — the planet. `TIMELINE-01` carries Katarr as a
Miraluka colony *"consumed by Nihilus"* after the Jedi Civil War, and `EVENTS-01` holds
`katarr_consumed` as an unconditional event record. **Nihilus obliterates all life on
Katarr — all but Visas Marr**, who wakes aboard his ship afterward.

**⚠ And the Campaign Guide gives a second, harder account of why the Jedi were there at
all** — see Flag 2, because the two do not sit easily together. In the Atris entry, the
conclave is **bait**:

> Orchestrating an irresistible lure, **Atris** calls a Jedi conclave on Katarr, where most
> of the one hundred remaining Jedi meet. **She then leaks knowledge of the session to bait
> their killer into the open.** Atris gets what she wanted — at the expense of her Jedi
> comrades — when Darth Nihilus razes Katarr.

**Atris survived because she did not attend.** She *"flees to Telos IV with the most
important items from the Jedi Library, including Sith holocrons,"* and sets up *"a would-be
Jedi praxeum"* there. **Telos IV is a place a 3,956 BBY campaign can reach**, which makes
this the single most immediately usable paragraph in the chapter.

### 3,954 BBY — the Triumvirate

*"The remnants of the Sith Empire are largely unified by **Darth Sion** and **Darth
Nihilus**. Though some Sith warlords continue to squabble over territory, Sion and Nihilus
represent the most unified front for the Sith during this time."*

The era narrative names a third: *"Three Sith Lords, **Darth Nihilus, Darth Sion, and Darth
Traya**, decide to restore their former power by eliminating the greatest threat facing the
Sith: the Jedi Order."* **⚠ The two accounts differ on Traya's place in this, and the
chapter does not flatten them — Flag 1.**

Either way the outcome is the same: *"In the middle of the Dark Wars, **the Jedi Order
collapses** and only a few survivors escape death at the hands of the Sith. The Sith
Triumvirate eliminates the Jedi and seizes control of the failing Sith Empire, planning to
reclaim lost territory and launch a united offensive once more."*

### 3,951 BBY — the Mandalorians come back

*"**Canderous Ordo**, now the Mandalore, reunites the Mandalorian clans and aids in the
fight against the remnants of the Sith Empire."*

**This closes the gap Chapter Four left open.** The Neo-Crusaders disbanded at Malachor V in
3,960; the search for the Mask ran through the campaign's own year and reached *"over a
hundred clans"* by Rekkiad in 3,954; and here it completes. `EVENTS-01` records the moment
exactly: **Mandalore the Preserver regroups the Neo-Crusaders on Dxun, and the Preserver
era opens.**

**The hired gun a party meets on Taris in 3,956 BBY becomes Mandalore five years later.**
There is no better single illustration of what this chapter is for.

### 3,951 BBY — Malachor V, again

*"Under the guidance of a disguised Darth Traya, **the Jedi Exile** defeats Darth Sion and
Darth Nihilus. **Bao-Dur activates the Mass Shadow Generator on Malachor V again**,
destroying what is left of the planet, and Traya is defeated."*

**The same weapon, the same world, a second time.** `EVENTS-01` holds
`malachor_v_second_destruction` at 3,951 as an unconditional record. Chapter Four's
victory and Chapter Six's are the same act performed twice, and the person at the centre of
both is the Exile — **which is the fact the Campaign Guide's dedicated entry makes
unavoidable, and which changes how Chapter Four should be read (Flag 3).**

### 3,950 BBY — what it cost

*"The last remnants of the Sith Empire crumble, and the Republic once again establishes
control over worlds that have been under Sith rule **since the Great Sith War.**"*

**Four words carry fifty years.** Worlds taken in 3,996 BBY are returned in 3,950 — the
Great Sith War's territorial losses are not reversed until the generation after the
generation that lost them.

The era narrative's closing is markedly sunnier: *"the Jedi survivors begin to rebuild their
Order, the Republic solidifies its forces, and the galaxy is once again peaceful and
prosperous."* **⚠ That is the most optimistic sentence in the Campaign Guide's historical
section, and it sits directly on top of an Order reduced to a handful of survivors.** It is
quoted here because it is the source's own conclusion, not because this book endorses the
adjective.

---

## Major Figures

*Short entries. Each points back into the narrative above rather than re-telling it.*

**The Jedi Exile** — **the Campaign Guide gives them a dedicated entry, and it reframes
Chapter Four.** Trained on Dantooine as Kavar's informal apprentice, then under **Vima
Sunrider**, who *"cautions the Jedi Exile to be mindful of her powers, particularly her
aptitude for severing another's connection to the Force."* Rallied to Revan in the
Mandalorian Wars and became *"his most trusted general besides Malak."*

**At Malachor V it was the Exile's hand on the trigger.** In the *Ani'la Akaan*, the "Great
Last Battle," *"the Jedi Exile springs the trap, unleashing an apocalyptic weapon called the
Mass Shadow Generator,"* which killed the Mandalorian navy *"as is the Republic fleet —
thousands of soldiers the Exile had led in battle and befriended… killed instantly."* **The
Exile then severed themselves from the Force** to survive the backlash, returned alone *"to
answer for herself and, by extension, Revan and his errant Jedi,"* and was exiled. *"Though
her name is lost to history, she becomes known as the Jedi Exile."* **She saves the Jedi
from extinction.**

**Darth Nihilus** — killed every living thing on Katarr (*see above*), leaving only Visas
Marr. Defeated by the Exile in 3,951 BBY. **The only figure in this book who destroys a
world by technique rather than by weapon**, which is why Katarr reads differently from the
Cron Cluster or Malachor V.

**Darth Sion** — ordered the assassination campaign of 3,954 BBY that all but ended the
Jedi Order (*see above*), and co-unified the Sith remnant with Nihilus. Defeated by the
Exile in 3,951.

**Darth Traya** — **⚠ her role is the chapter's one genuine same-rank conflict; see Flag
1.** The era narrative makes her a founding third of the Triumvirate; the dated timeline has
the Exile defeat Sion and Nihilus *"under the guidance of a disguised Darth Traya"* before
Traya herself is defeated. **The chapter follows the timeline and records the narrative.**

**Atris** — called the Katarr conclave and leaked it as bait (*see above*); survived by not
attending; fled to **Telos IV** with the Jedi Library and Sith holocrons to found her own
praxeum. **The most campaign-reachable consequence in the chapter.**

**Vandar Tokare** — met the surviving Jedi at Katarr and died there with them.

**Canderous Ordo → Mandalore the Preserver** — Chapter Four's hired gun on Taris; reunites
the clans and regroups the Neo-Crusaders on Dxun in 3,951 BBY (*see above*). **The single
clearest line this book draws between the campaign's present and its future.**

**Bao-Dur** — activated the Mass Shadow Generator at Malachor V in 3,951 BBY, the second
destruction.

---

*Sources: KOTOR Campaign Guide — "The Dark Wars" f. 6; the dated timeline f. 113; the Jedi
Exile and Darth Nihilus entries f. 140; Vandar Tokare f. 139; Atris f. 141. `EVENTS-01 §1`
(3,951, the Preserver era opening), `§4` (`katarr_consumed`,
`malachor_v_second_destruction`). `TIMELINE-01` for Katarr as a Miraluka colony consumed by
Nihilus. KOTOR 2 at rank 1. Folios are printed page numbers; the OCR's page markers run
three higher. No rank 6 or 8 material needed.*

## Open items, carried from review

**⚠ Flag 1 — same-rank conflict on Darth Traya's role, resolved under `PT-946`.** The era
narrative (f. 6) makes Traya one of three Sith Lords who *"decide to restore their former
power"* together and has *"a Jedi survivor slay all three members of the Sith
Triumvirate."* The dated timeline (f. 113) instead has the Sith remnant *"largely unified by
Darth Sion and Darth Nihilus"* — Traya absent from the unification — and then, in 3,951,
*"under the guidance of a **disguised** Darth Traya, the Jedi Exile defeats Darth Sion and
Darth Nihilus,"* with *"Traya is defeated"* recorded separately.

**Neither supersedes; `PT-946`'s more-specific rule applies.** The timeline is dated,
itemised, distinguishes Traya's role from the other two, and names Bao-Dur and the
mechanism. The narrative is a five-paragraph summary. **The timeline governs and the
narrative is recorded.** This also happens to be the reading consistent with **KOTOR 2 at
rank 1**, which outranks both — noted as corroboration, not as the basis for the call.

**⚠ Flag 2 — a second same-rank conflict, on who convened Katarr, where `PT-946` gives no
winner.** Two Campaign Guide character entries, comparable in specificity:

- **Vandar Tokare, f. 139:** *"To divine the identities of their hunters, Master Tokare
  meets with most of the hundred surviving Jedi on the planet Katarr."*
- **Atris, f. 141:** *"Orchestrating an irresistible lure, Atris calls a Jedi conclave on
  Katarr… She then leaks knowledge of the session to bait their killer into the open."*

**These are not the same claim.** One is a Jedi Master convening peers to identify a threat;
the other is a deliberate use of a hundred Jedi as bait, which the entry itself scores as
*"at the expense of her Jedi comrades."* They can be stacked — Atris convening, Tokare
presiding — but neither entry says so, and the difference in moral weight is the whole
point of the episode.

**`PT-946`'s third branch applies: where specificity is equal, record both and mark it
unresolved.** *"An unresolved pair that says so is safe; a forced resolution that looks
settled is not."* **The chapter carries both accounts and does not pick.** First use of that
branch in this book.

**⚠⚠ Flag 3 — this chapter's sources amend Chapter Four, and I have not silently rewritten
it.** Chapter Four quotes the CG timeline verbatim: *"Revan lures the Mandalorians to
Malachor V… activates the superweapon known as the Mass Shadow Generator."* **The Campaign
Guide's dedicated Jedi Exile entry at f. 140 attributes the activation to the Exile** — it
was *"Revan's carefully choreographed gambit,"* but *"the Jedi Exile springs the trap,
unleashing an apocalyptic weapon called the Mass Shadow Generator."*

**Under `PT-946` the character entry is the more specific source on this one point** — it
names the battle (*Ani'la Akaan*), the agent, the mechanism, and the consequence, against
the timeline's single clause. **The reconciliation is almost certainly "Revan planned it,
the Exile executed it,"** and both sources are satisfied by that reading.

**What I have done:** flagged it here and left Chapter Four's verbatim quotation intact.
**What I recommend:** a one-sentence amendment to Chapter Four crediting the Exile with the
activation inside Revan's plan, since as it stands Chapter Four leaves a reader thinking
Revan pulled the trigger, and **the Exile's entire character — the severing, the exile, the
return in 3,951 — descends from having pulled it themselves.** Say the word and I will make
it; it is one sentence and a source line.

**⚠ Flag 4 — my Chapter Five prediction was wrong, and the correction is worth more than the
prediction.** I reported that the CG-narrative-versus-CG-timeline conflict pattern was
*"bounded"* to long compressed wars and said I would *"expect it back in Chapter Seven
rather than Chapter Six."* **It is back in Chapter Six, twice.** The bound I proposed does
not hold: the Dark Wars are four years, the same length as the Jedi Civil War, and they
produced two conflicts where that war produced none. **The real variable is not the era's
length but how many separate CG sections describe it** — this era is covered by an era
narrative, a timeline, and at least four character entries, and the conflicts are between
those, not within any one.

**Corrected expectation for Chapter Seven:** it has the *fewest* CG sections of any chapter
in the book, so on this revised reading it should produce few conflicts and a thin chapter
— which matches what I already flagged about its sourcing.

**Worth recording for Chapter Eight — an epigraph the Campaign Guide hands us.** Closing
the historical section at f. 6, attributed to **Jolee Bindo**: *"Look, everybody always
figures the time they live in is the most epic, most important age to end all ages. But
tyrants and heroes rise and fall, and historians sort out the pieces."* **That is Chapter
Eight's thesis, written by the source material, in the voice of a KOTOR 1 character a party
can actually meet.** Not using it here; flagging it so it is not lost.
