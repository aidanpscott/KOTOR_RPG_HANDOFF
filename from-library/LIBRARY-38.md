# LIBRARY-38 — `LIBRARY-35` is largely retracted. The homeworld set answers it, and I published before reading it.

**Filed 2026-09-01. `§L111`.**

---

## 1 · Three quarters of `LIBRARY-35` dissolves on reading `D-CARD-01`, `D-AGE-01` and `D-NOMENU-01`

### `Malachor V` and `Peragus II` absent from the corpus — not a third state

**`D-NOMENU-01` rules them among the seven added worlds that take no menu.** *"They remain in `selection.json`… expanded, if at all, as places described inside other entries."*

**And `D-AGE-01` says it outright: *"`Sapient Species: None`. Not homeworld-eligible at all. A minimum age on a world nobody is from is a rule doing no work."***

**`D-MAL-01`'s *"it keeps its world record"* is satisfied** — the `selection.json` row plus description inside other entries is the record.

### `Urkupp` carrying a menu — the design working, not a contradiction

    cardinality.py   "Urkupp" claimed by ['Dashade']
    D-AGE-01         min_age 40 — born before the 3996 supernova

**Urkupp's menu is reachable and correctly so.** A Dashade of forty or more can claim it, and `D-AGE-01` exists for that one case. **I reported a live, ruled, working mechanism as a defect.**

---

## 2 · Why I misread the whole thing

**`D-CARD-01`: *"Cardinality is a property of the SPECIES, not the world."***

**Eligibility is enforced species-side by `tools/cardinality.py` — 47 records, all bands assigned.** The `ineligible` bucket in the retired JSON was a **world-side convenience**, not the governing mechanism.

**I found a missing flag and assumed it was the gate.**

    Naboo · Bespin · Cerea    claimed by NOBODY across all 47 records
    Urkupp                    claimed by Dashade
    Malachor · Peragus        claimed by NOBODY, and no menu by ruling

---

## 3 · ⚠ What survives, and it is one band wide

**Three of four bands are lookups.** `Locked` (15), `Paired` (3), `Regional` (14) name their worlds — a claim on Naboo simply is not in the list.

**`Diaspora` (15) is not a lookup.** *"Origin world plus any of the 290 with attested presence of the species."* `cardinality.py` names only the enumerated worlds; Human's basis reads *"any world with an attested Human population — the largest legal set."*

> **So for 15 of 47 species the gate is a judgement about a world's prose, made per claim — and that judgement is exactly what the `ineligible` bucket pre-computed.**

**The three worlds hold the right answer in their own prose** — Bespin *"NOT YET COLONISED… UNTIL 1,989 BBY"*, Cerea *"HAS NOT YET ESTABLISHED FORMAL CONNECTION"*, Naboo *"only Gungans live here in 3956"*.

**Losing the flag does not make a wrong answer available. It makes a correct answer require reading the entry at claim time rather than consulting a list.** **A real cost, and much smaller than I reported.**

**Whether that wants restoring is yours.** If it does, the population is the Diaspora band only, and the three worlds already carry their own basis.

---

## 4 · How I got it wrong, which is the part worth keeping

**`LIBRARY-35` went out after I read `D-MAL-01` and `D-CURRENCY-01`, and before I read `D-CARD-01`, `D-AGE-01` and `D-NOMENU-01`.**

**All five are in the same directory. I named the unread three in that same letter as my next block.**

> **I reported a governance defect in your tree while explicitly holding an unread stack of your rulings on the same subject.**

**That is `PT-407`'s receiving obligation inverted — the scope of the negative was known to be incomplete by the agent stating it.** I chose `decisions/`-first *for governance*, which was the right order, and then did not wait for my own read to finish before publishing.

**The rule I would take from it: a finding derived from a ruling set is not ready while any ruling in that set is unread.** Not "check more" — **"do not publish mid-directory."**

---

## 5 · Position

**`decisions/`: 24 of 32 read closely.** The homeworld set is done — `D-CARD-01`, `D-AGE-01`, `D-NOMENU-01`, `D-MENU4`, `D-BLOCK-01`, `D-DUDS-01`.

**`C03` remains unblocked and I have still not written into it.** **The reason I gave in `LIBRARY-37` — that the ineligible question touches the homeworld mechanic — has now dissolved.** **The remaining reason is that I would rather finish `decisions/` first, which is the lesson above applied to myself.**

**Eight rulings left: `D-BLOCK-01` residue, `D-CLOSE-01`, `D-CRYSTAL-01`, `D-EXCEPT-06`/`-07`, `D-MANDO-01`, `D-NAMES-01`, `D-OPEN-01`, `D-ROLE-01`, `D-TIEBREAK-01` and Rule 3.**
