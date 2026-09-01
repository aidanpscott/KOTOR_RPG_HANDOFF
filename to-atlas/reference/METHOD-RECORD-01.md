# METHOD-RECORD-01 — The Rule Families

**What this is.** Every method rule this project has derived, in one place, with the instance that produced it.

**Why it exists.** These were discovered in the documents where the work happened — the warrant rules in `ENGINE-SHAPES-01`, the adjacency rule in `CANON-FINDINGS-01`, the collision rule in `DECISION-GAP-001b`. That is the highest-value material in the project sitting in the places it happened to occur, and it is the first thing lost when a thread reseeds.

**How to use it.** Three families, eight rules. **The families matter more than the rules**, because each one names a *kind* of failure and therefore a *kind* of check. A new failure that does not fit any family is worth stopping for.

---

## Family 1 — Warrant

> **Something acquiring a warrant it did not earn** — by proximity, by carriage between documents, by naming an existing element, by association with a rejected one, or by relay.

**The check: *where did this come from?*** A provenance trace. Expensive, and the only thing that catches these.

**And for `§1.5`, a second check: *who actually read it?*** A relay can name the source correctly and still be a relay, so provenance alone does not catch it.

### 1.1 The citation rule

> **A citation may be attached only at the point the source was read.**

**Instance:** a page citation was carried from one document into another and attached to a claim the source did not make. The citation looked correct because it was correct *somewhere else*.

### 1.2 The conversion-adoption rule

> **A conversion targeting a named element of the destination ruleset adopts that element's full semantics, including the ones the source did not specify. Name what is being adopted, or the adoption is silent.**

**Instance:** mapping Rakata's rage aftereffect onto `fatigued` looks like a translation and is a design decision — it imports Revised's timed clearing and discards Saga's clears-on-action. **Neither clearing rule is written in the record being converted**, which is why the adoption would go unnoticed.

**This is the most dangerous of the warrant rules**, because Saga is the same game line with overlapping vocabulary. The failure does not look like contamination. It looks like a rules detail.

### 1.3 The adjacency rule

> **When a source presents a number beside a narrative claim, establish which one carries the finding before generalising either. Adjacency is not support.**

**Instance:** Korriban's *1% Kissai* came packaged with a narrative result — a few settlements remaining scattered in isolation. **That sentence carried the status claim; the percentage did not.** The pair were read together, the wrong element credited, and the wrong element generalised to four records.

**This rule has the highest instance count.** It fired **three times on a single rule** — RCR's `+4/−8` — producing three successive verdicts, each correct against the evidence held, each resting on evidence that did not say what it was read as saying. First a ratio without populations, then a table's markers read as a taxonomy.

> **Corollary: a rule whose terms are defined elsewhere gets reconstructed from whatever is nearest, and the nearest thing looks authoritative because it is adjacent.**

### 1.4 The lineage rule

> **A first-party book consulting a rejected source does not inherit the rejection. What is rejected is the derivative artifact, not everything it touched — the rejection attaches to who assembled it, not to what they read.**

**Instance:** UAA's reference list names two West End Games D6 titles, and the D6 conversion this project rejected cites one of them for two species. Same material, two routes. **UAA's version is citable; the conversion's is not** — and otherwise RCR falls too, since its own credits thank the West End Games designers by name.

### 1.5 The relay rule — a claim carries the warrant of its reading, not of its relay

> **A claim passed between agents carries the warrant of whoever read the source, not of whoever passed it on. A relay is not a reading, however accurately it names the source.**

**The check is distinct from the family's other four.** They ask *where did this come from?* **This one asks *who actually read it?*** — and a relay can name the source correctly, cite the right page, and still be a relay.

**Three instances, and they fail in different directions.**

**A negative relayed and acted on.** Bith was cut under D-P on a claim of *no source in any of the three books*, **relayed from an extractor and acted on without anyone asking what reading produced it.** There was none. Reversed by D-U. **See `§3.3` and the negative-scope standing check** — the same event, seen from the capture side and from the negative-findings side.

**A reading refused because the relay was unavailable.** The wiki researcher declined to source the Dashade `+10` Will bonus from an aggregator, **which was correct.** But the figure had **already been read from UAA pp.43–44 by the rulebook extractor, with the book in hand.** Neither agent knew. **The relay failed by not happening**, and a book-grade value was treated as unobtainable for want of a route between two agents.

**A specification cited by everyone and held by nobody.** `RULES-01 v2` was pasted into a conversation, never saved, and **cited across twenty documents and twenty-four sections by agents who had never held it.** When it was recovered, every claim tested against it was exact — **so the carriage was sound and the custody was not.** That is the rule's best case and its clearest warning: **an accurate relay is still a relay, and it fails silently the moment the source is gone.**

### The countermeasures, and they differ by direction

> **State the proximity, not just the source.** *Read at UAA p.43* and *relayed from the extractor, who read UAA p.43* are different claims and should not look identical on the page. The temporal work already does this with `proximity: wiki_summary_of_cited_source`; **the rest of the corpus does not.**

> **Before treating a value as unobtainable, ask whether another agent already holds it.** B28's figure was book-sourced and sitting in a species record while a second agent recorded it as unverifiable.

> **Save the source, not the relay.** A document cited across a long engagement is saved as a file the moment it is first read. **Pasting it into a conversation is custody by accident.**

---

## Family 2 — Collision

> **Two things sharing an identifier.**

**The check: *what else is called this?*** A corpus search rather than a provenance trace — **cheap and automatable**, unlike Family 1.

### 2.1 The collision rule

> **Check any new mechanic name against the corpus before adopting it.**

**Four instances, all found by noticing. The fifth should not need noticing.**

| Name | Referents |
|---|---|
| `Rage` | RCR Force feat p.114 / Wookiee species trait p.33 / a descriptor |
| `Pureblood` | Arkanian baseline (Campaign Guide) / **struck SWTOR species** |
| `Force Sight` | **Miraluka species trait, record one** / KOTOR 2 power |
| `Determination` | **Arkanian Offshoot trait, record twenty-two** / KOTOR 2 lightsaber form |

**Two of the four are already on written records.** This is not a hypothetical check.

**Symptoms differ from Family 1.** Not a wrong value — a **right value found under the wrong name**, or a search returning two answers where one was deliberately excluded.

**The corpus is incomplete and the check should say so.** `Force Sight` as a KOTOR 2 power came from a web index and is in no file, so a grep is **partial rather than exhaustive.**

### 2.2 The remedy — what to do once a collision is found

**The rule above says to check. This says what to do about it.**

> **Disambiguate the identifier, never the display name.**

A record carries two things: an **ID**, which is ours to author, and a **display name**, which the book supplies. **The ID may be namespaced and qualified freely. The display name stays verbatim with its locator**, or the record misrepresents its own source.

```yaml
feat:
  id: feat.rage                  # ours — disambiguated
  display_name: "Rage"           # RCR p.114 — verbatim
  collision_note: "See trait.wookiee_rage (RCR p.33); descriptor.rage"

species_trait:
  id: trait.wookiee_rage         # ours
  display_name: "Rage"           # RCR p.33 — verbatim
```

**Namespacing alone is not sufficient.** `feat:rage` and `trait:rage` are technically distinct, but **the failure a collision produces is a search returning two answers**, and only a qualified identifier fixes that.

> **Record the collision on every colliding record, not just the one being written.**

Otherwise the second record's author repeats the discovery. **Two of the four known collisions are already on written records** — `Force Sight` on Miraluka, `Determination` on the Arkanian Offshoot — and neither carried a note at the time.

> **Descriptors are exempt. They are the book's vocabulary and stacking depends on them.**

`rage` is a descriptor — Wookiee Rage grants *+2 rage bonus on Fortitude and Will* — and it is one of two observed descriptors absent from the stacking sidebar's fifteen. **Rename it and the same-descriptor non-stacking rule stops matching the book's text.** A descriptor lives in its own namespace and keeps its name unchanged.

**This is the clause most likely to be broken by a well-meaning tidy-up pass**, which is why it is written down.

**And `Rage` has four referents, not three:** `feat.rage` (RCR p.114), `trait.wookiee_rage` (RCR p.33), `trait.rakata_rage` (Saga, unconverted), and `descriptor.rage`. **The Rakata one is the record whose `fatigued` mapping is still pending a decision ID**, so it should be disambiguated in the same pass.

*Open: whether RCR's Force feat at p.114 is named simply `Rage` or carries a longer name. Only its index entry has been read. If it has a longer name, the display name changes and the collision is less severe than it appears.*

---

## Family 3 — Capture

> **A value in hand and not in the record.**

**The check: *has this page already been read?*** Neither evidence nor naming — this is about extraction.

> **Reading is directed; marking is per-field. So a page-read can satisfy zero, one, or many field-needs, and nothing tracks the gap.**

### 3.1 Directed reading

> **When a page is opened for one field, extract every field the record wants from that page before leaving. The page is the expensive unit; the field is free once it is there.**

**But the rule presumes a stable schema, and this project's is not.** *Extract every field the record wants* assumes the record knows what it wants — and a single batch of seven species records raised **six schema questions**, one from a field nobody had anticipated.

> **A page extracted completely against today's schema is still incomplete against tomorrow's.**

**So the rule reduces re-reads rather than eliminating them**, and the honest form says so. Otherwise the first time a field is added, someone assumes the pages are mined, marks values `UNRETRIEVED` that are sitting in context, and **reproduces the exact failure the rule was written to prevent, one schema revision later.**

**The hardening is cheap, and it mirrors machinery the project already has.**

> **Record which pages each extraction pass covered, against the schema version in force. *Pages are exhausted* becomes *pages were exhausted as of schema version N*, which is checkable.**

A later field addition then identifies **exactly which pages need revisiting**, rather than re-reading everything or trusting they were done.

**This is `search_scope` applied to extraction rather than to search.** D-H already holds that a negative finding is only as strong as the places searched, and records the scope with the finding.

**And it marks a real difference between the families.** A warrant failure or a collision is true or false at a point in time. **Coverage is true only against a stated version, and decays silently as the schema grows.**

**Instance:** three species records carried `UNRETRIEVED` age bands, and **four page-reads were spent hunting values already present in pages read** — Devaronian's directly above the traits block, Gand's in the adjacent column, Weequay's in the left column of a page whose right column had been transcribed.

### 3.2 A roster that grows under prior reads

> **When the roster grows, re-check prior reads against the new record.**

**Instance:** Ithorian's traits were read in one session and never recorded, **because Ithorian was not on the roster at the time.**

**Live rather than hypothetical.** Gamorrean was admitted mid-stream under D-I, the Arkanian Offshoot under D-M, and Arcona and Ayrou were considered and declined. **Every admission makes earlier reads potentially relevant to a record that did not exist when they happened.**

### 3.3 A wanted-list is not a search

> **An absence produced by an extraction wanted-list is not a finding. The list defines what was looked for, so *not found* and *never sought* are indistinguishable in its output.**

**Instance, and it produced a wrong decision rather than a missing field.** Bith was reported as having **no confirmed source in any of the three books**, and was cut on that basis under D-P.

**Bith is in UAA at p.24 with a full traits block.** The absence claim came from an extraction wanted-list that never included Bith — **not from the book.**

**Two things failed at once.** The extractor's wanted-list had diverged from the roster, so a record that existed was never a target. And the absence was **passed on and acted upon without its scope being asked for**, which is the standing check in §*Negative findings carry their search scope* going unrun by the party receiving the claim rather than the party making it.

> **Corollary: the obligation to name a scope falls on whoever states the negative. The obligation to ask for one falls on whoever acts on it.**

**Distinct from §3.2.** There, the roster grew under prior reads and the record did not yet exist. **Here the record existed and the extraction target list did not contain it** — the roster and the wanted-list diverged silently, and nothing reconciles them.

> **Countermeasure: reconcile the extraction wanted-list against the roster before treating any absence as a finding.**

### 3.4 The operational form

> **`UNRETRIEVED` means *not extracted*, not *not read*. Before spending a read to fill one, check whether its page is already in hand.**

That check alone would have saved four reads.

---

## Standing checks that are not rule families

**These are single findings that became standing practice. Recorded here so they are not rediscovered.**

### The date-before-relevance check

> **Establish a name's date before proposing its relevance. A name attached to a roster species reads as campaign-relevant before anyone has checked when it lived.**

**Three instances in a single sweep**, all carried forward on species and role alone:

| Name | Carried as | Actually |
|---|---|---|
| **Snar Extruct** | A Dashade in the Jedi Temple, cutting against the Sith-aligned reading | **~2,000 years post-campaign** |
| **Akriss Veng** | A named Shadow Killer | **~300 years post-campaign** |
| **Jerbhen Hulis** | One of Noab Hulis's three daughters | **Male, and 1,300 years later** |

**The check is mechanical and cheap:** a carried name gets a date **before** it enters a carryover list. **If the date is post-campaign it goes straight to seen-and-rejected.** Applying it retroactively to one outstanding list would have removed three of five entries before the sweep began.

**This is a fourth question alongside the three families' checks**, and it is specific to a project with a bounded window:

| Family | The check |
|---|---|
| Warrant | *Where did this come from?* |
| Collision | *What else is called this?* |
| Capture | *Has this page already been read?* |
| **Date** | ***When is this?*** |

### The content-before-resource check

> **Before deciding a resource question, ask which content it is being decided against, and whether that content is settled.**

**Three instances**, and it is a structural property of porting a hybrid: **resource questions look like design decisions and get framed as decisions; content questions look like data entry and get deferred. Then the content determines the resource.**

| Framed as primary | Actually decided by |
|---|---|
| replace / layer / rename-only | the temptation curve |
| the alignment ratio's verdict | list composition |
| the pool shape | the acquisition model |

### The undefined-category check

> **An RCR rule referencing a category should be checked for whether the category is defined. The book gestures at categories and does not always close them.**

**Three instances:** *skills requiring patience and concentration*; *dark-side and light-side Force skills*; *mind-influencing Force skills*. **Each names examples and closes nothing**, and each becomes an authored partition the port must supply and mark.

### The exclusion rules — a dependency test, not a source ban

**Four rules. The first was rewritten once the source-level version proved both too broad and imprecise about what it was protecting.**

#### 1. The dependency test — what SWTOR exclusion actually means

> **SWTOR is excluded on the basis that the events of that game did not occur.**
>
> **That is a rejection of its events, not of the material as a source of ideas — and especially not of history it establishes as already having happened before the campaign date.**

**What is excluded is the events.** Revan's arc after KOTOR 2, the Exile's fate, Vitiate, the resurgent Sith Empire, the Great Galactic War — **everything establishing what happened after 3951 BBY.** KOTOR 3 was never made and nothing has filled that gap. **The exclusion protects the gap.**

**What is not excluded** is the incidental fact that SWTOR-era material mentions a species existed, dates a war three millennia earlier, or names where a planet sits — **or that it attests a piece of history already settled at 3956.**

> **But nothing on that basis is admitted by default.** A SWTOR-attested fact about the pre-campaign past may be **proposed** for admission, one item at a time, **and it is admitted only if and when the owner approves it.** See D-R for the first instance.

> **The test in practice: strip SWTOR's events out and ask whether the claim survives.**

| Claim | Verdict |
|---|---|
| The Quarren War is dated ~4500 BBY | **Admitted.** Predates SWTOR's period by three millennia, depends on no SWTOR event, establishes nothing after KOTOR 2 |
| Kaleesh were *recently arrived* and newly recognised by the Republic and **the Sith Empire** by ~3640 BBY | **Rejected.** Dated by SWTOR's war, framed by SWTOR's factions. **There is no Sith Empire without SWTOR** |

**This subsumes the geography carve-out rather than sitting beside it.** Planets were usable because a coordinate is not a claim about the story — the same reasoning, now general.

**Burden note:** anything dated inside SWTOR's own window, roughly **3681–3600 BBY**, is **presumptively excluded**, because claims from that period are usually *about* it. Not automatic, but the burden flips.

**And the setting/rules split is still not a route back in.** It governs what kind of claim an **in-window** source may supply. A source that fails the dependency test supplies nothing of either kind.

#### 2. The source hierarchy — two orders for two kinds of claim

**For setting and timeline facts, in rank order:**

1. **KOTOR 1 and KOTOR 2**
2. **KOTOR Campaign Guide**
3. **KOTOR comics and Tales of the Jedi**
4. **The Essential Atlas**
5. **Dark Empire**
6. **The New Essential Chronology**

**Where sources disagree, the higher rank governs.** Record the disagreement; never silently take the lower.

**For rules, the games rank nowhere.** RCR governs; the Ultimate Alien Anthology sits inside the Revised boundary and governs on conflict; the Campaign Guide is conversion input. **Game data is never rules input.**

> **A game supplies what happened in the galaxy. It never supplies what a mechanic does.**

#### 3. The deep-history rule — pre-campaign material is a different kind of thing

> **Material describing events well before the campaign window may be admitted on looser terms, because it cannot contradict the campaign date.**

**The distinction that licenses this:** a claim about 5000 BBY **produces no temporal facts.** Nothing at the founding of the Sith Empire changes state during play. It cannot be pending, cannot fire, cannot leak, and cannot be averted.

**So deep history is world-bible content, not timeline content**, and the entire scheduling apparatus is irrelevant to it. It needs to be plausible and evocative rather than dated and tracked.

**The window.** Material describing events **before roughly 4000 BBY** — the Infinite Empire and the Rakata, the Great Hyperspace War, Tython and the early Jedi, the ancient Sith and Korriban's tombs, Naga Sadow, the origins of species and worlds.

**The publication bound: everything published as Legends.** That is, material published **before Lucasfilm discontinued the Expanded Universe in April 2014.**

> **The bound is a continuity, not a year.** Legends is one coherent body of material that was written to fit together. Post-reboot canon is a different one, and it makes no claims this project wants.

**This replaces an earlier 2010 bound**, which was a proxy for *before SWTOR's lore programme* and **produced a false positive on its first real test.** *Star Wars: Dawn of the Jedi* ran February 2012 to March 2014, is set at 25,793 BBY, and takes the **Rakatan Infinite Empire as its antagonist** — including Force Hounds, the Rakata's trained Force-sensitive slaves, which the project's own Rakata material already touches. **It is post-SWTOR by publication and 22,000 years clear of it by subject.**

> **The dependency test was always the rule and the date was always the proxy.** When the two disagree, the test governs.

**Note what this bound does not exclude.** The **KOTOR Campaign Guide** (2008), the **KOTOR comic series** (2006–2010), **Unknown Regions** (2010) and **Dark Empire** (1991) are all Legends and all in bound. **Nothing published after the April 2014 reboot is admitted at any depth.**

**Consequences of adopting it:**

- **The New Essential Chronology becomes genuinely useful**, despite ranking fifth. Deep history is the part of it **least likely to conflict** with anything the project holds, because nothing the project holds covers it.
- **Dark Empire's Ossus material becomes admissible for its deep-history content** — a 1991 comic making a claim about 3996 BBY. The Ysanna's *later* development across millennia is out of window in the other direction and stays out.

**Recorded separately from the temporal enumeration.** Deep history goes in the world bible as background; it does not enter `TEMPORAL-ENUM` or the scheduling system, because it has nothing to schedule.

**And the campaign-window rules are untouched.** Anything describing roughly 4000–3950 BBY is governed by the five-rank hierarchy and the dependency test as before. **Looser terms apply to distance, not to the window.**

#### 4. The out-of-window rule — distance forward, not contradiction

> **Out-of-window lore may inform an authored record. It may not be cited as a source for one. Physiological claims travel across eras; cultural and historical claims do not.**

**Distinct from the deep-history rule above, and it runs the other way.** Deep history is material about the era's *past*, which cannot contradict the campaign date. This rule governs material about the era's *future* — Kaleesh lore built around Grievous, roughly 3,500 years late — which cannot be cited because the culture it describes has not happened yet.

**A different problem from the dependency test.** Kaleesh lore built around Grievous is roughly 3,500 years late and makes **no claims about this period at all.** It is **distant, not contradictory**, and distance needs its own treatment.

**Species biology is among the most temporally stable facts in a setting** — Wookiees are strong in every era. **Culture is the opposite**, and the Gazetteer already taught this: worlds change inside a five-year window, so cultures certainly change across millennia.

**Instance of the cost of ignoring it.** A search for Echani lifespan returned **three incompatible figures**, all from fan sources — 95–150 years, *around 200 human years normally unsullied by frailty* from a page whose own title says *fannon*, and human-equivalent. **Had the search been for a number rather than for whether one exists, three were waiting.**

### Negative findings carry their search scope

> **The absence of a thing in a book is a finding only if the places searched are named.**
>
> **And the obligation runs both ways. Whoever states a negative must name its scope. Whoever acts on one must ask for it.**

**Instance of the first half:** RCR's `+4/−8` rule has no stated referent. That is recorded as **five locations checked** — Table 4-5's markers, the skill description format at two samples, the Force chapter's opening, and both remaining pages of pp.177–180 — not as *it isn't in the book*.

**Instance of the second half, and it cost a species:** Bith was reported as having no source in any of the three books and was **cut on that basis**, under D-P, **without anyone asking what scope produced the claim.** There was none — the absence came from an extraction wanted-list, not from the book. **Bith is in UAA at p.24 with a full traits block.** See `§3.3`, where the same failure is recorded from the capture side.

> **The receiving obligation is the one that gets skipped**, because a negative arrives sounding like a finding and nothing about its phrasing reveals that it isn't one.

### Temporal assertions need validity bounds

> **A world or species description true at the campaign date may be false five years either side of it.**

**Seven world instances and one species instance**, and the world bible's assertion format cannot express any of them. **Distinct from the omission hazard**, which is an entry silent about a *completed* change — that is rare, one instance in nine.

---

## What to attach this to

**Any new thread.** These rules cost roughly forty review batches to derive and a paragraph each to carry. **The findings are recoverable from the record documents; the rules are not, because they are conclusions about how the work goes wrong rather than about the subject matter.**

