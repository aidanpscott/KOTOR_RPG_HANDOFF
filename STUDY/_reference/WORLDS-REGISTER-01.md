# WORLDS-REGISTER-01

**Status:** settled unless noted
**Scope:** admission, exclusion, and access control for worlds and sub-locations
**Supersedes:** the ban-list proposal (rejected — see D-W1)

---

## 1. Objects

### D-W1 — Fail-closed via admitted register, not a ban list

A negative list can only exclude worlds someone thought to name. The failure guarded against is narrator improvisation, which reaches for whatever is salient — including worlds nobody listed. **Only a permitted list constrains it.**

If a world is not in the register, it is not reachable. The engine refuses rather than narrates.

### D-W2 — Candidate register is primary; world records are a subset

The exclusion table cannot be derived from world records, because excluded worlds have no record. A thinner object holds every world the project has ever considered:

**Candidate register fields:** `id`, `name`, `alternate_names`, `type`, `parent`, `region`, `discovery`, `settlement`, `state_changes[]`, `first_publication`, `described_era`, `status`, per-claim locators.

Both the admitted register and the high-salience exclusion table derive from it by predicate. One place where a world's status is decided.

### D-W3 — High-salience exclusion table retained, reduced in role

Small, covering the attractors most likely to be improvised: Naboo, Kamino, Geonosis, Bespin, Hoth, Endor, Mustafar. Each entry carries its predicate, not a hand-written ban.

| Exclusion class | Predicate |
|---|---|
| Not yet settled | founding date > 3956 BBY |
| Not yet charted | discovery date > 3956 BBY |
| Out of continuity window | first publication after April 2014 |
| Contaminated era | SWTOR-era, ~3640 BBY |
| Exists, wrong state | state change crosses 3956 BBY |

The last class is not a ban. Those worlds are reachable — just not in the state the narrator's training data describes.

---

## 2. Evidence

### D-W4 — One-sided bounds suffice for admission

Founding dates are not required. Evidence a world existed *before* 3956 — a battle, a trade record, a passing reference in an earlier-set work — establishes admission. Exclusion is the mirror: evidence of first existence *after* 3956.

Date fields carry a value type:

| Type | Meaning | Sufficient for |
|---|---|---|
| `exact` | stated date, cited | anything |
| `bounded` | between X and Y | anything |
| `before` / `after` | one-sided | admission or exclusion |
| `inferred` | derived from an attested event, flagged | admission, provisionally |
| `absent` | nothing found, scope stated | nothing — see D-W5 |

### D-W5 — `absent` resolves to `unadjudicated`, not exclusion

Fail-closed on absence would exclude most of the ancient galaxy, since obscure worlds attested only in a passing panel will never have a founding date. `unadjudicated` is a third bucket: not admitted, not excluded, **visibly unresolved**.

Not reachable. Mentionable. Routes to Wiki Researcher as an explicit finding. It is a work queue, not a permanent category — most entries resolve on a single read.

### D-W6 — `attested_in` is separate from `read_at`

The wiki is a conduit to higher-rank material at least as often as it is a source. Taris's Undercity is rank 1 (KOTOR 1) but will be read on Wookieepedia (rank 3–5). Collapsing the two either downranks game-attested facts or launders wiki inference into rank 1.

**Rank flows from `attested_in`. Warrant flows from `read_at`.**

---

## 3. Sub-locations

### D-W7 — Inherit the parent's temporal envelope; date only for deltas

Default is coextensive-with-parent. A date is required only where the sub-location was built later, destroyed earlier, or changed state within the window. Keeps the dating discipline where it earns its keep.

**Scope cap:** admit sub-locations attested in KOTOR 1/2, named in a rank-2 source, or required by a campaign package. Nothing else.

### D-W8 — `improvisation` field carries the granularity control

Per world: `none | unnamed_only | free`.

- `none` — rank-1 attested worlds where invention risks contradicting the games (Taris, Dantooine, Manaan, Korriban, Telos, Peragus, Onderon, Dxun, Nar Shaddaa)
- `unnamed_only` — a cantina yes; a named cantina with a proprietor and a history, no
- `free` — narrator may invent

One field per world instead of a registry of alleys.

---

## 4. Permissions

### D-W9 — Four independent permissions

- `mentionable` — may be named in narration or NPC dialogue
- `birth_eligible` — may be a character homeworld
- `reachable` — party may travel there
- `improvisation` — per D-W8

Reachable implies mentionable. Birth_eligible implies mentionable. Reachable and birth_eligible are independent in both directions: an uninhabited but visitable world is reachable and not birth_eligible; a diaspora origin the campaign never visits is the reverse.

### D-W10 — `birth_eligible` is an authored allowlist, not a derived status

Homeworld is a player selection list with fixed cardinality. Unadjudicated worlds cannot appear because nobody put them there. The permission is curated, not computed.

### D-W11 — Spacer and Unknown are `type: origin_category`

Same lookup table as worlds, no special-case branch. Spacer = born shipboard or on a station. Unknown = the character does not know.

**Open:** Unknown cannot grant a fixed skill without telling the player something the character supposedly doesn't know. Either the player picks freely, or it grants nothing and compensates elsewhere. Deferred to skill assignment.

### D-W12 — Full lore records precede skill assignment

The +2 homeworld skill falls out of world records. Records first.

---

## 5. Refusal

### D-W13 — Three tiers, all in-fiction

| Tier | Fiction | Openable by play |
|---|---|---|
| `uncharted` | astrogation database returns no route; the place is real, no one here can plot a course | yes — this is the hook tier |
| `restricted` | route exists, transit doesn't: blockade, quarantine, permit, price | yes |
| `nonexistent` | no such world | no |

`nonexistent` covers Voss and anything first discovered after KOTOR 2.

### D-W14 — `nonexistent` forces `mentionable: false`

If the engine says "never heard of it" and an NPC references the place two sessions later, the denial is exposed as a mechanism. Nonexistence propagates through everything the world model can say, not just the travel check.

### D-W15 — Denial is never explained

No "that world isn't discovered yet" — that is the engine talking, not the galaxy. The NPC is **incurious rather than argumentative**: hasn't heard of it, doesn't care that the player has, does not defend the position. A player who knows Voss from SWTOR will push; the correct response is a shrug, not a rebuttal.

### D-W16 — Ontological and epistemic denial are distinct

| | Claim type | Form |
|---|---|---|
| World doesn't exist (Voss) | **ontological** — it isn't there | "There's no such world." |
| Location isn't registered | **epistemic** — I don't know of one | "I've never been down there." |

**The engine must never leak *unregistered* as *nonexistent*.** "There is no cantina in the Lower City" creates a false negative fact the engine then owns forever. "I've never been to the Lower City" creates a fact about the speaker and nothing about the world.

### D-W17 — Deflection ladder

**Redirect to registered → deflect if a plausible ignorant speaker exists → author it.**

Refusal never appears as itself.

Redirect is the default: deflect on the unregistered thing, then point at a registered one. Play moves, the player gets somewhere real, the register works unnoticed.

**Constraint:** deflection requires a plausible ignorant speaker. An Upper City commoner not knowing the Lower City works. A Lower City local pleading ignorance about a Lower City cantina collapses instantly — and a deflection the player sees through is worse than no gate. Where no such speaker exists, fall back to redirect-only, then to authoring.

Authoring is the last rung, not the common case.

---

## 6. Source findings

### D-W18 — Publication date and described era are separate gates

SWTOR reference material published before April 2014 passes the publication boundary. **Geography admitted, state excluded**: a world's location, sector, and hyperlane position are stable across three centuries; its government, population, and factional alignment are not.

SWTOR worlds now sourced via Wookieepedia. **This is Wiki Researcher's lane, not the Atlas agent's** — the Atlas agent's stated primary source is the Atlas.

### D-W19 — Atlas PDF is an image-only scan

257 pages, 216 MB, 200 DPI RGB JPEG throughout. `pdffonts` returns empty. No text layer.

- No grep, no full-text hold. ~1,600 tokens per page read; ~400K for the book.
- Negatives are expensive: "I searched the Gazetteer" means 100+ page reads.
- OCR is weak on map labels and grid coordinates — the highest-value content.
- **A low-DPI index sweep capturing world-name-to-page mapping should precede any world work.**

### D-W20 — Page offset is +13

PDF index 120 = printed page 107. **Cite printed folio, carry PDF index in brackets** — printed folio is verifiable against a different scan.

### D-W21 — The Gazetteer stat sidebar is structurally undated

The omission hazard is the format, not three unlucky worlds. Sample (Thyferra, p.107): grid location, terrain, diameter, day and year length are era-stable. Population, species mix, government, and major exports sit in the same visual block with the same authority and carry no date — the listed government dates to the Clone Wars and after; the entry's narrative runs to 36 ABY.

**Apply the undated-claim rule field-by-field within the stat block, not entry-by-entry.**

---

## 7. Chargen interface

Settled with the rules agent. Cross-references ENGINE-CORRECTIONS-01 E-10 (sequencing) and E-11 (homeworld load-bearing by transitivity).

### D-W22 — Rename, don't split

E-11 flagged that homeworld became mechanically load-bearing without being declared — it can determine subrace, and subrace carries adjustments. **Subrace is a species property, so the existing field is already semantically `origin_world` wearing the wrong label.**

Rename the existing field `origin_world`; every current behavior is preserved and nothing re-derives. Add `homeworld` as genuinely new. A symmetric split would wrongly imply both halves need re-derivation.

### D-W23 — Homeworld eligibility is a world property, not a species lock

Rejected: a species-level constraint locking homeworld to origin world where the origin world is closed. It collapses most species back to `homeworld == origin_world` and the two fields stop earning their existence.

**Rule: a species is homeworld-eligible on a world where that species has attested presence at 3956 BBY.** Diaspora, colony, slave population, single trading family — any attested presence qualifies.

This is the register's species-presence field doing the work it exists for. It produces the Rakata restriction without a special case: Rakata on Coruscant fails because nothing places Rakata off Lehon; Selkath on Taris passes because Selkath are attested off Manaan.

**First live test:** the species chapter attests Bith musicians and traders in the Lower City cantinas of Taris in 3956 BBY. Bith homeworld Taris is therefore legal, derived, with no authored permission.

### D-W24 — The two-field model is forced, not convenient

Four of thirty-one origin worlds are destroyed, abandoned, devastated, or unreachable at the campaign date:

| World | State at 3956 BBY | Species affected |
|---|---|---|
| Urkupp | destroyed, Cron Cluster supernova ~3996 BBY | Dashade |
| Korriban | largely abandoned; some Kissai resettled on Ziost | Kissai, Massassi |
| Cathar | ravaged 3973 BBY, rebuilding, no central authority | Cathar |
| Lehon | Unknown Regions, unreachable by accident | Rakata |

**A Dashade character cannot have homeworld Urkupp in 3956 — the world is not there.** For Dashade and probably Rakata, homeworld must differ from origin world. This is the justifying case for the split, ahead of the Selkath-on-Taris case.

All four are omission-hazard candidates and require verification against event timing before any record is written.

### D-W25 — Chargen sequence

| Step | |
|---|---|
| 1 | Roll ability scores |
| 2 | Choose species → sets origin world, racial affinities |
| 3 | Species-internal choices (E-10 ordinal — e.g. Offshoot Dex-or-Str) |
| 4 | Apply adjustments |
| 5 | Choose homeworld → +2, gated by D-W23 |
| 6 | Choose profession |
| 7 | Choose class → class skills, skill points |
| 8 | Allocate skills |
| 9 | Feats |

Homeworld must precede 8 because the +2 lands on the skill list, and should precede 7 so the player sees all cheap-skill sources before spending points. Step 2 gates step 5 via species-presence.

### D-W26 — `Unknown` homeworld: hidden value, not deferred grant

Rejected: player picks a placeholder and the GM retcons once. If the player picks the placeholder, the player picks the skill — free choice with extra steps.

**The GM sets the homeworld at chargen. The player never sees it.**

One value, settled at step 5, nothing deferred, fully E-10 compliant. The player sees a +2 on the sheet with no listed source — an unexplained aptitude. The character has a past that shaped them and does not know what it was; the fiction and the mechanic are the same object.

Reveal occurs when the backstory surfaces, and reveals information rather than granting anything.

### D-W27 — `Spacer` tolerates a null world

Raised shipboard or on a station is a real upbringing and breaks nothing mechanically, but it is not a place. Anything performing a world-record lookup must tolerate a null. Skill grant not yet assigned.

### D-W28 — Negatives: both obligations, not just the first

Imported from `METHOD-RECORD-01 §3.3` via the D-P/D-U reversal, whose worked instance is directly analogous to Atlas's situation.

**An absence produced by a wanted-list is not a finding.** The list defines what was looked for, so *not found* is indistinguishable from *never sought*. Atlas will generate exactly this shape of negative: searching a Gazetteer against a list of worlds someone chose in advance.

**Two obligations, and the seed currently carries only the first:**

- Whoever states a negative must name its scope — which chapters, which maps, which appendices.
- **Whoever acts on a negative must ask for its scope** before acting.

### D-W29 — Secondhand warrants are a distinct failure route

The D-P snapshot's "Visible to me" column records D-P as `Secondhand` — the agent who recorded Bith's exclusion never saw the source.

This is the project's named false-negative pattern arriving by a route the existing formulation does not catch: not a claim acquiring a warrant by moving between *documents*, but by moving between *agents*. A relayed claim carries the warrant of the relay, not of the reading.

**Atlas records must mark any claim not read by the recording agent as secondhand**, with the relaying agent named. Same discipline as `read_at` in D-W6, extended to inter-agent transfer.

### D-W30 — Homeworld offers a skill set, not a single skill

A world offers **three to five trainable skills**; two where the lore supports no more. The player selects one. The +2 attaches to the selection.

World records therefore supply a set with reasoning per entry, not one judgement. Per D-W23 this is Atlas's recommendation to make during batching, with the final call the integrator's.

Supersedes the same-skill/different-skill framing of the cheap-skill question — a world that offers a menu makes the distinction moot.

**Amendment (batch 02, Arkania) — the menu is keyed on `(world, species)`, not on `world`.**

A pureblood Arkanian raised in Adascopolis and an Arkanian Offshoot raised in a segregated mining camp outside it share a homeworld and share no upbringing. One grows up inside a bioengineering corporation; the other is a legal non-citizen mining diamonds in tundra. Candidate skills came out with no overlap.

**Rule:** a world carries **one default menu**. A world with a stated internal division — caste, segregation, habitat partition — carries **additional menus keyed by species or subspecies**, and the default does not apply to those groups.

Divisions confirmed so far: Arkania (pureblood / Offshoot, by segregation); Glee Anselm (Anselmi / Nautolan, by habitat). **Both surfaced within two batches, so this is not an edge case.**

### D-W31 — `era_boundary` retired

The three-value enum (pre-change / post-change / unchanged) cannot express a world that changed more than once, and Telos changed at least twice inside the window.

**Replaced by the dated `state_changes[]` list as the primary structure**; the boundary label is computed from it rather than declared. Same defect and same fix as `ledger_conditional`.

**Amendment (batches 01–02) — the computed label needs five values, not three.**

| Value | Meaning | Found on |
|---|---|---|
| `unchanged` | no state change in the window | — |
| `pre-change` | window precedes the change | — |
| `post-change` | window follows the change | Urkupp, Korriban, Cathar, Arkania |
| `between-changes` | window sits between two changes | **Malachor V** — shattered 3960, destroyed 3951 |
| `mid-change` | a change is occurring during the window | **Alpheridies** — falls to the Sith during the Jedi Civil War |
| `incomplete` | changes exist but are not yet recorded | **Lehon** — rank-1 campaign events, deferred to the ledger |

`incomplete` is not a finding of stability. A record carrying it is explicitly unfinished.

### D-W38 — `adopted_origin` flag on `origin_world`

Two of thirty-one origin worlds are **adoptions, not origins**, and both surfaced in batch 02.

- **Miraluka** — evolved on an unnamed world that lost its atmosphere to space; migrated to Alpheridies c. 6000 BBY. Alpheridies is the *adopted* homeworld.
- **Arkanian** — Arkania likewise described as the adopted homeworld.

`origin_world` currently cannot distinguish *evolved there* from *migrated there*. Add `adopted_origin: true|false`; where true, record the prior world if named and `unnamed` if not.

**Same shape as Urkupp in a different direction.** Urkupp is an origin world that no longer exists; Alpheridies is a homeworld that was never the origin. Both break the assumption that origin world and ancestral world are the same object.

### D-W39 — Cross-world organisation index

**Czerka Corporation now spans three world records** — Korriban (Dreshdae settlement by Sith permission), Kashyyyk (the occupation), Arkania (allied with Adascorp and the Draay Trust). Adascorp and the Draay Trust also cross records.

The register has no structure for an entity that appears on many worlds. Without one, the same organisation is described three times with three warrants and no way to detect contradiction.

**Minimal object:** organisation name, per-world presence, per-world role, date bound, locator. Not a faction system — an index, so that a claim about Czerka on one world can be checked against Czerka on another.

### D-W32 — Source hierarchy: cite `METHOD-RECORD-01 §2, D-AB`, do not restate

Six ranks for setting and timeline facts: (1) KOTOR 1 and 2, (2) KOTOR Campaign Guide, (3) KOTOR comics and *Tales of the Jedi*, (4) *The Essential Atlas*, (5) *Dark Empire*, (6) *The New Essential Chronology*. Higher rank governs; disagreement is recorded, never silently resolved downward.

**A separate, disjoint hierarchy governs rules:** RCR governs, UAA governs on conflict within the Revised boundary, Campaign Guide is conversion input. **The games rank nowhere in it.** A game supplies what happened in the galaxy; it never supplies what a mechanic does.

**Wookieepedia is not a rank in D-AB — it is a route to whichever ranked source underlies a claim.** For Atlas purposes only, it is treated as a local **rank 7**, below all six. This is a local extension, not a change to D-AB.

The Telos precedent resolves under this: the wiki's 3959 traced to the Atlas at rank 4; the Campaign Guide's 3958 at rank 2 governed.

### D-W33 — The Atlas is the geography source, not the primary world source

**Corrects the seed, which has this inverted.** The Campaign Guide Gazetteer is rank 2 and written for this era; it is primary for world records. The Atlas is rank 4 exactly and supplies what the Gazetteer does not: sectors, regions, coordinates, hyperlane routes, adjacency.

**Consequence the seed must also carry:** the omission-hazard warning moves with primacy. All three confirmed cases — Cathar, Telos, Peragus — are *Gazetteer* entries describing the wrong side of a state change. The primary source carries the known defect.

**Escalation ladder for a world the Atlas lacks:**

| | |
|---|---|
| 1 | The games — thirteen landable worlds settle before the Atlas is opened |
| 2 | Campaign Guide Gazetteer |
| 3 | KOTOR comics, *Tales of the Jedi* |
| 4 | Wookieepedia (route; name the underlying rank) |
| 5 | Author it, marked `hybrid_authored`, with sources searched named |

**Absence in a rank-4 source is not a finding.** It is the weakest possible negative. Atlas reports *"not in the Atlas, searched X and Y"* and routes upward. Routine escalation, not a gap.

### D-W34 — Three branches, not two: Atlas-has, Atlas-omits, Atlas-cannot-represent

The appendix indexes **systems**. A world that shares a system with another has no entry and never will — Trandosha shares the Kashyyyk system (Trandoshan name: **Hsskassi**); Dxun is a moon of Onderon. These are not research gaps and do not resolve.

Detected by the parent pointer (D-W35): absence of a child entity from a system index is expected and uninformative.

### D-W35 — One entity type, self-referential `parent` pointer

**Not a new schema.** D-W7 already gave sub-locations a parent pointer with inheritance. Systems, worlds, moons, and sub-locations are the same table at different depths; a shared-system model would be that object renamed.

System → world → moon → sub-location. Trandosha's parent is the Kashyyyk system; Dxun's is Onderon; the Undercity's is Taris. Children inherit from the parent unless they override — temporal envelope per D-W7, coordinates per below.

Two supporting fields:

- **`coordinate_source: attested | inherited`** — Kashyyyk P-9 is attested (Companion appendix, read directly). Trandosha's P-9 is inherited and says so. Prevents the appendix appearing to assert what it never stated.
- **`alternate_names[]`** — load-bearing, not cosmetic. A name-keyed sweep returned a false negative on Lehon, which the appendix carries as **Rakata Prime** (Unknown Regions, G-11).

### D-W36 — Field-level era classification, replacing per-entry judgment

Supersedes D-W21's per-entry rule. Classified once for all world records:

| Class | Fields | Rule |
|---|---|---|
| **Invariant** | terrain, gravity, atmosphere, diameter, day length, year length, star type, sector, region, coordinate | Admissible from any ranked source regardless of era |
| **Era-bound** | government, population, species mix, exports, imports, affiliation, occupation status, starport, tech level | Requires a date inside the window, or field is marked absent |
| **Slow** | hyperlane access, charted status, settled status, dominant species presence | Requires a bound, not an exact date |

The **slow** class exists because hyperlanes break the binary — too slow for a decade to matter, too fast for millennia to be safe. It is also where the register's own predicates live: *charted* and *settled* are slow fields, so the exclusion table queries this class specifically.

**Maps onto D-AB's out-of-window modifier:** out-of-window material may supply invariant fields freely, may inform slow fields, may never supply era-bound fields. Same principle as the method record's physiological/cultural split for species, extended to worlds.

Worked case (Thyferra, printed p.107): grid location, terrain, diameter, day, year — take freely. Population, species mix, government, exports — take nothing without a date.

### D-W37 — Five unstated origin worlds resolved

The species chapter left five origin worlds unstated. Resolved and approved:

| Species | Origin world | System / sector / region | Read at |
|---|---|---|---|
| Bith | **Clak'dor VII** (a.k.a. Bith) | Colu system, Mayagil, Outer Rim; Rimma Trade Route | Wookieepedia — rank 7 |
| Devaronian | **Devaron** | Devaron system, Duluur, Colonies, M-13 | Wookieepedia — underlying: Companion, rank 4 |
| Nautolan | **Glee Anselm** | Jalor system, Mid Rim | Wookieepedia — rank 7 |
| Rodian | **Rodia** | Tyrius system, Savareen, Outer Rim | Wookieepedia — underlying: Companion, rank 4 |
| Cathar | **Cathar** | Quelii, Outer Rim, N-6 | Companion appendix p.12 — rank 4, read directly |

Devaron and Rodia should be **re-read at rank 4 from the appendix in hand** rather than left as relays. Bith and Glee Anselm remain rank 7 until an underlying rank is named.

**Human remains correctly unstated** — no single world; RCR pp.22–23 gives Core Worlds dominance, not an origin.

**Three findings carried out of this resolution:**

- **Clak'dor VII is a fourth omission-hazard case.** The Nozho–Weogar biological war and the ecological collapse date to ~300 BBY. At 3956 the world is intact and the Bith homeworld is part of the civilized galaxy. Every modern description is post-collapse.
- **Glee Anselm has two native sentients partitioned by habitat** — Anselmi on land, Nautolans in water. The species-presence field has no structure for two origin species on one world.
- **The Bith / Bith system collision is confirmed on both sides.** The Core Worlds Bith system (L-13) is a distinct object from Clak'dor VII. Any species-name-to-system join resolves Bith to the wrong world silently.

### D-W40 — The Gazetteer is era-agnostic by editorial policy, and the Timeline is its dating instrument

**Chapter VII, p.112, Timeline header:** the Timeline exists so that it *"should give Gamemasters a good idea of when to set their campaigns."* **The book states no campaign date and delegates the choice to the table.** Chapter VII's opening describes Krath, Mandalorians and Sith as simultaneous threats — a span of roughly forty-seven years, not a moment.

**Consequence, and it is a reframing rather than a defect finding:**

The Gazetteer's undated stat blocks are not an oversight. The book describes a fifty-year era and declines to pick a year within it. **Peragus II shattered and Cathar intact may both be correct for campaigns the book anticipates.** The conflict is between the book's scope and ours, not between the book and the facts.

**So the operative question per world is not "is this field reliable" but "which of the book's fifty years does this stat block describe."**

**The Timeline pp.112–113 is the instrument that answers it.** Twenty-eight dated entries, 4000–3950 BBY, naming worlds. It covers **eight of the eighteen** Gazetteer entries: Korriban, Cathar, Taris, Malachor V, Telos IV, Onderon, Dantooine, Lehon. For those eight, the stat block can be dated by internal cross-reference. **For the other ten, no internal anchor exists and external verification is the only route.**

**The Timeline is not complete for the window.** It omits the destruction of Taris in 3956 — a rank-1 event central to KOTOR 1 — in a year for which it carries three other entries. Absence from the Timeline is not evidence of non-occurrence.

**Distribution note:** seven entries fall in 3997–3996, then nothing until 3985, then twenty compressed into 3976–3950. The thirty-year gap is the Restoration period.

**Scope of the negative:** pp.102, 103, 112–113 read in full; **pp.104–111 not read.** A statement narrowing the Gazetteer's era could sit in one of the five thematic sections. Routine escalation, not closure.

### D-W41 — Telos IV: two narrow textual findings, precedent unaffected

**WITHDRAWN in part.** An earlier version of this entry claimed the seed's Telos precedent "needs rewriting before it is cited again." **That was wrong and is retracted.**

**The precedent is intact.** It is a *cross-rank date* precedent — the Legends wiki dates Telos IV to 3959 tracing to the Essential Atlas at rank 4; the Campaign Guide says 3958 at rank 2; **3958 governs and both are recorded.** Nothing found this session touches it.

**Two narrower findings stand:**

1. **The Timeline's wording is "successful attacks at Foerost and Telos IV," not bombardment.** No dead surface, no devastation, in the rank-2 text.
2. **The devastation is rank 1 (KOTOR 2), not rank 2.** Rank 1 governs outright; no cross-rank dispute arises.

**Telos IV is not an omission-hazard case.** Per `CANON-FINDINGS-01 §6`, its catastrophe follows the campaign date, so the Gazetteer's silence about it is correct behaviour rather than a fault.

### D-W42 — Warrants upgraded from rank 7 to rank 2

| Claim | Was | Now |
|---|---|---|
| Urkupp destroyed 3996 BBY | rank 7, escalation flagged | **rank 2** — Timeline p.113: Aleema Keto killed near the Cron Cluster after activating a supernova-inducing weapon, 3996 BBY |
| Malachor V — Trayus Academy discovered 3961 | `[r7-provisional]` | **rank 2**, Timeline p.113 |
| Malachor V — Mass Shadow Generator 3960 | `[r7-provisional]` | **rank 2**, Timeline p.113 |
| Malachor V — destroyed 3951 | `[r7-provisional]` | **rank 2**, Timeline p.113 |
| Korriban — Sith seizure and academy 3959 | rank 2, corroborating | **rank 2**, confirmed verbatim |
| Cathar — massacre 3973 | rank 2 | **rank 2**, confirmed verbatim |

`WORLDS-BATCH-01` §1 and `WORLDS-BATCH-02` §5 to be amended accordingly.

### D-W43 — Omission hazard and temporal problem are two problems, not one

**Correcting `B-19`, which counts three, and this register, which propagated it.**

`CANON-FINDINGS-01 §6` counts **one** omission hazard — **Cathar only** — and rebuts both additions specifically:

- **Peragus II** is written entirely post-destruction. The entry *carries* its change rather than omitting it.
- **Telos IV**'s catastrophe follows the campaign date. Silence about a future event is correct behaviour.

**The two take different countermeasures and must not be merged:**

| Problem | Definition | Countermeasure | Count |
|---|---|---|---|
| **Omission hazard** | entry silent about a **completed** change | cross-reference the Timeline (D-W40) | **1** — Cathar |
| **Temporal problem** | entry true at one moment, **misleading at another** | validity bounds on assertions (**D-W36**) | **7** |

> **D-W36 is the temporal countermeasure.** The three-class field split — invariant, era-bound, slow — *is* validity bounds on assertions. This register built the right countermeasure under the wrong problem name. Collapsing the two attaches the countermeasure to the wrong problem and loses the seven-instance one.

**Two claims from batches 01–02 reclassified:**

- **Clak'dor VII** — called "fourth omission hazard." **Wrong.** The ecological collapse is ~300 BBY, *after* the window. The entry is not silent about a completed change; it describes a state that has not occurred. **Temporal problem.**
- **Alpheridies** — called "fifth omission hazard." **Wrong.** The fall to the Sith occurs *during* 3959–3956. Descriptions of a peaceful isolated world are true earlier and misleading at our date. **Temporal problem.**

**The omission-hazard count remains one.**

**Provenance, and it is an instance of D-W29.** `B-19` counts three and cites `CANON-FINDINGS-01`, which counts one. A later document citing an earlier one while contradicting it. The count acquired its warrant by being carried rather than read, and travelled from there into the atlas seed and into this register. **D-W29's pattern occurring in the corpus rather than between agents.**

### D-W44 — D-W36 checked against the seven; two gaps found

**The seven temporal instances** (`CANON-FINDINGS-01 §6`, transcribed by Library): Katarr · Malachor V · Cathar · Dantooine · Taris · Peragus II · Telos IV. **"And counting" — a floor, not a total.**

**All seven are in the appendix at rank 4:**

| World | Sector | Region | Grid |
|---|---|---|---|
| Katarr | Vensori | Mid Rim | O-8 |
| Malachor | Chorlian | Outer Rim | S-4 |
| Cathar | Quelii | Outer Rim | N-6 |
| Dantooine | Raioballo | Outer Rim | L-4 |
| Taris | Ojoster (Taris) | Outer Rim | N-7 |
| Peragus | Xappyh | Outer Rim | Q-4 |
| Telos | Kwymar | Outer Rim | Q-4 |

**Katarr shares grid square O-8 with Alpheridies** (Farstey, Expansion Region). The Miraluka's two worlds are grid-adjacent.

### Verdict: covers one axis, misses two

**What D-W36 does:** answers *"does this field need a date."* Correct, and sufficient for a project anchored to one year.

**Gap 1 — validity bounds means an interval, not a requirement.**
The source's frame is *a campaign spanning both games crosses all seven*. Telos IV is true at 3956 and false at 3951; Katarr the same. **A field needs `valid_from` and `valid_until`, because a value can expire during play.** The three classes say which fields require dating. Nothing says a dated field carries a range, or that the range can lapse mid-campaign.

**Gap 2 — direction is assumed.**
The out-of-window rule assumes staleness runs one way: later material describes a later state, so exclude it. **Telos IV and Katarr are inverted — the entry is correct now and becomes wrong.** Harmless at a fixed 3956; not harmless if play moves toward 3951.

**Gap 3 — the two flags are not alternatives.**
`D-W43`'s table reads as a fork: omission hazard *or* temporal problem, one countermeasure each. **Cathar is both, and the source says so explicitly.** A record must carry an omission flag and a validity interval on the same field. `D-W43` is amended: the classifications are **independent, not exclusive.**

### Consequence for homeworlds

**At 3956 the Miraluka have attested presence on both Alpheridies and Katarr**, so both are homeworld-eligible per D-W23. A Miraluka raised on Katarr is from a world annihilated after our window — **a character premise that exists only because the anchor is 3956 rather than 3951.**

**The inverted case is not only a hazard. At our date it is an asset**, and the register should not be built to suppress it.

---

## 8. Open items

Rulings are recorded in §9. Items below are genuinely unanswered.

| Item | Blocks |
|---|---|
| Homeworld cardinality undecided (curated list, open selection, restricted subset) — deferred; Atlas is being built partly to inform it | D-W10 |
| Skill grants unassigned for `Spacer` and `Unknown` — deferred to skill assignment | D-W26, D-W27 |
| Whether `Ithorian` is a multi-world case or a null-origin case. "Ithor or a herd ship" is the `Spacer` shape arriving through a species, meaning null origin may be a species property and not only a character choice | D-W27, D-W35 |
| Species-presence field has no structure for two origin species partitioned by habitat on one world (Glee Anselm: Anselmi/Nautolan) | D-W23 |
| Seven multi-world species flags returned unresolved: Arkanian Offshoot (Arkania + Telerath), Echani (Eshan + Six Sisters), Ithorian, Kissai and Massassi (Korriban→Ziost; Massassi also Yavin 4), Rakata (Lehon; Flesh Raider → Tython), Zabrak (Iridonia + colonies) | D-W23 |
| Collisions unresolved, returned as-is: Arkania ×2, Korriban ×2, Mon Calamari ×2. Note **Mon Calamari, not "Dac"** — RCR pp.29–30; "Dac" appears nowhere in the chapter or pages read | D-W23 |
| Rank backing the Mytaranor / Hsskassi claims unnamed — "Legends-attested" is the formulation D-AB dissolves | D-W32 |
| Devaron and Rodia to be re-read at rank 4 from the appendix rather than left as rank-7 relays | D-W37 |
| Ownership of D-W28 and D-W29 — Library confirms §3.3 corrected (both obligations now on the standing check) and the carriage rule **absent and never generalised**. Three instances: D-P, B28, `RULES-01 v2` cited across twenty documents by agents who never held it. Its check is *who actually read this?* — distinct from *where did it come from* | method-register integrity |
| Whether `read_at` (D-W6) and the method record's new carriage check are one object under two names | schema / method alignment |
| `DECISION-RECORD-04` — confirmed written; location not established | A-17 |
| **Register has no date field.** No decision can be ordered against any other. `CONSOLIDATION-MAP` L190 names it. Not this document's to fix; this document now adds 37 undated decisions to it | decision-register integrity |
| Czerka/Trandoshan collaboration detail belongs in `kashyyyk_czerka_occupation` — causal detail that record lacks, sitting between two workstreams | temporal ledger |

---

## 9. Rulings this session (previously open, now closed)

| Was open | Ruling |
|---|---|
| Rank 1 for world narrative unassigned | Resolved by D-AB: six ranks, games at rank 1. Seed cites, does not restate |
| Batch protocol / scope cap | Named world list per batch; full-book pass across ~10–12 sessions to a persisted file |
| May Atlas suggest skills? | Yes — recommend and describe |
| Temporal-Files interface | Atlas reports date + locator once, never re-cites. Dates go to main agent for check; corrections return; Library updated. Ledger owns the record; world record carries the ID |
| Hyperlane era verification | Superseded by D-W36 — hyperlanes are a **slow** field requiring a bound |
| June 11 2014 HD Expansion Region map | Admissible: re-release of pre-boundary content. Second instance of the same rule: the July 2014 Wayback capture of the Companion page |
| Companion homeworld assignments | Rank-5 conjecture; never a source for species origin. Sector data unaffected |
| Voss | Out. **Does not fall out of the predicates** — the appendix lists it (Allied Tion, Outer Rim, S-6) with no date. Hand ruling, recorded as an override |
| Cheap-skill marking (same or different skill) | Superseded by D-W30 — world offers a menu, player picks one |
| `improvisation` field | **Killed.** Invent freely in the gaps; never contradict a ranked source. That is D-AB applied to narration, not a per-world enum |
| Five unstated origin worlds | Resolved and approved — D-W37 |
| Companion appendix obtained and verified clean | 2012 state confirmed: zero hits on Moraband, Bardotta, Ringo Vinda, Zanbar, Denova, Carreras, Cog Hive Seven, Corbantis. Reads **Fortnay**, not Forntay. ~4,900 systems, four columns, **no temporal data whatsoever** |
| Kashyyyk grid square | **P-9 confirmed at rank 4**, read directly from the appendix — retires the post-2014 canon chain (Visual Encyclopedia → Ultimate Star Wars → Force Awakens Beginner Game) |
