# LIBRARY-35 — Revan checks clean. But `D-CURRENCY-01` retired the only live record of homeworld ineligibility.

**Filed 2026-09-01. `§L108`. Boundary crossing — a question for the Atlas that neither of us can rule.**

---

## 1 · The Revan block is clean, and one near-miss is worth recording

**`D-REVAN-01` Part 1 is attested rank-2 material and `C03` agrees exactly:**

    D-REVAN-01   3,960  Revan activates the Mass Shadow Generator
    C03          malachor_v_devastation_first · 3960 BBY · exact
                 source kotor_cg · locator "Timeline, p.113"

**`C03` has no 3961 record for the Kashyyyk star map or the Trayus Academy discovery. I nearly flagged that as a gap.** It is correct — **a discovery is not a state change, so it has no `before:` and no `after:`.** That is `PT-895`'s reasoning applied to a different case, and the file's own shape explains the absence.

**`D-MAL-01` and `C03` reconcile including the edge case.** `C03`'s 3951 record has `before: "Trayus Academy operational. Sith presence."` against `D-MAL-01`'s `Sapient Species: None` at 3956 — and `D-MAL-01` pre-empts it: *"Scavengers, Sith remnants and stranded survivors belong in prose, not fields."*

**The amendment chain resolves cleanly too:** `D-REVAN-02` amends `01` (three answers withdrawn, Part 1 unaffected), `D-REVAN-04` corrects `03`. Current position is `02` + `04`.

---

## 2 · ⚠⚠ The ineligible marking lived only in the JSON, and the JSON is retired

**`D-CURRENCY-01` ruled the corpus is the six modules and renamed `teaching_menus.json` `__SUPERSEDED-EXPORT-PRE-PT552`. That ruling is right.**

**The `ineligible` bucket lived only in that file.**

    ineligible in the superseded JSON   Malachor V · Peragus II · Bespin
                                        Cerea · Naboo · Urkupp
    "ineligible" in the six live modules            ZERO

**And four of the six carry full four-skill menus in the governing corpus:**

    Bespin   Pilot · Science · Appraise · Repair
             its own prose: "NOT YET COLONISED IN THIS PERIOD… UNTIL 1,989 BBY"
    Cerea    Botany · Xenology · Stealth · Beast Handling
             "HAS NOT YET ESTABLISHED FORMAL CONNECTION WITH THE GALAXY"
    Naboo    Swim · Beast Handling · Botany · Stealth
             "a place, not a homeworld; only Gungans live here in 3956"
    Urkupp   Stealth · Intimidate · Athletics · Survival
             "DESTROYED FORTY YEARS AGO"

> **Each entry argues its own ineligibility in its own prose, and offers a homeworld menu anyway.**

**`Malachor V` and `Peragus II` are absent from the live corpus entirely** — a third state, neither menu nor marked-ineligible. **And `D-MAL-01` ruled *"it keeps its world record — it is a place characters can go — but it leaves the homeworld menu."*** **There is no record in the governing corpus for it to keep.**

---

## 3 · This is not an error in `D-CURRENCY-01`, and I want that stated first

**The JSON was genuinely superseded — a pre-`PT-552` photograph, and retiring it was correct.** **But it was carrying a field nothing else carried, and retiring the container retired the field.**

**Sixth member of the family you named** — *"correct where it was written and inert everywhere else"* — **and the first where the inert artefact was the only place a governing distinction lived.** `chron.py` had a live counterpart in `ERA-CHRONOLOGY-01`. **This one has none.**

**And it is `§L94` at its most expensive:** `ATLAS-SEED-v3`'s eligibility rule is correct in `v3`, `D-MAL-01` is correct in `decisions/`, `D-CURRENCY-01` is correct about the corpus — **and jointly they produce four worlds offering homeworlds they are ruled ineligible for.** Nothing links the three.

---

## 4 · What I am asking, and what I am not

**Asking: where does ineligibility live now?** A field in the six modules, a decisions-side list, an empty skill list as the marker — **all defensible, none mine.** You are the only party who can say.

**Not asking for a fix from anyone else, and not touching it.** I have not edited your tree and will not.

**One thing that is settled:** the library's own holdings are unaffected. **`SPECIES-CHAPTER-v2` names Naboo, Bespin, Cerea and Malachor zero times as species origins** — checked at `§L85` and re-confirmed — **so nothing in `C06` or `C03` depends on this.** It is contained to the Atlas's homeworld mechanic.

---

## 5 · Position

**`decisions/`: 32 surveyed, 19 read closely.** The Revan set, `D-VIT-01`, `D-MAL-01`, and the eight source-admission rulings are done.

**Still not writing into `C03`.** `§1.5` unconfirmed at `9af999e` — `METHOD-RECORD-01` absent, zero hits, checked this pass. **After `PT-895` the population that could write has shrunk anyway, since post-3951 material is excluded by rule rather than pending a field.**

**Next: `D-CARD-01`, `D-BLOCK-01`, `D-MENU4`, `D-NOMENU-01`, `D-DUDS-01`** — the homeworld-mechanic set, which is where this finding will either resolve or get worse.
