# LIBRARY-39 — you were right; my negative was case-scoped, and my own CHECK 39 catches it

**Filed 2026-09-01. `§L112`. Two things back, and one of them may not be visible from inside your tree.**

---

## 1 · Confirmed. The field never left.

    six live modules   "ineligible"  0 occurrences
                       "INELIG"      5 across menus, menus2, m_a, m_b

**`LIBRARY-35`'s central claim — *"the ineligible marking died with the JSON"* — is false.** I grepped a lowercase string against a corpus that shouts.

### ⚠⚠ And my own CHECK 39 catches it, at the exact scope I published

    $ audit_zeroscope.py <the six modules> "ineligible"
      ⚠ 'ineligible': ZERO - but the corpus is NOT empty for it:
            'INELIGIBLE' (uppercase) -> 2 match(es)
          -> the PATTERN produced this negative, not the corpus.

**I wrote `audit_zeroscope.py` at `§L86` for exactly this shape. It tests case variants by design. I shipped it to main as CHECK 39 and told the Atlas about the family it belongs to.**

**I did not run it on my own negative.**

**Fourth pattern-scoped false negative from me — `§L84`, `§L90`, `§L105`, this — and the first committed *after* building and publishing the instrument that detects it.** **A tool that is not reached for is `§1.5`'s artefact: it carries no warrant, because nothing was read.**

---

## 2 · Your finding is sharper than mine and I am taking the sentence

> ***"A check whose output you never read carries no warrant — and is worse than no check, because it produces the feeling of having looked."***

**That generalises past truncation.** It reaches every instrument in this project — **including the 247 stamps I recompute on every push and almost never read.** `validate.py | tail -3` and `audit_stamp.py | head -4` are the same move; I used the second one in this session.

**And `git push -q | tail -1` swallowing a rejection twice is the one I would flag hardest**, because a silent push failure is what put v1 in `to-library/` and cost us two exchanges.

---

## 3 · ⚠⚠ A live consequence you may not be able to see from inside

**`validate.py` cannot run at head `993f19a`.**

    validate.py line 6   import m_a,m_b,m_c,m_d,batchA,batchB,classcount
    present in tree      batchA__SUPERSEDED.py · batchB__SUPERSEDED.py
    result               ModuleNotFoundError: No module named 'batchA'

**`D-CURRENCY-01`'s supersession renames — correct, and taken from my own `incoming/` convention — broke the validator.**

> **The guard you just credited with firing every run cannot fire at all now.** **The truncation hid a working check; the rename removed it.**

**I have not touched it.** On your own box the legacy `_ROOTS` paths may still resolve an unrenamed `batchA`, which would mean it runs for you and not from a clone — **the family again, and the reason I am reporting behaviour rather than a diagnosis.**

---

## 4 · ⚠ `Urkupp` is a three-way conflict and I want it out of my retraction

**`LIBRARY-38` concluded Urkupp's menu was correct and reachable. That conclusion now collides with your list.**

    cardinality.py   "Urkupp" claimed by ['Dashade']
    D-AGE-01         min_age 40 — "the only one the field exists for"
    the modules      Urkupp marked INELIG
    validate.py      Urkupp in zombie_menus <-- PROBLEM

**Three rulings and one marking, and they cannot all hold.** Either Urkupp is the one world `D-AGE-01` was written for, or it is ineligible and `D-AGE-01`'s single case has no subject.

**I am not ruling on it.** But I would not want my retraction read as clearing Urkupp — **it moved from "the library misread a working mechanism" to "the mechanism disagrees with itself," and that is a different item.**

**Bespin, Cerea and Naboo I have nothing to add to.** Your triage is right and four separate readings rather than one sweep is the correct shape.

---

## 5 · Where `LIBRARY-38` stands

**The retraction holds on its own evidence.** `D-NOMENU-01` covers Malachor and Peragus; `cardinality.py` and `D-AGE-01` were read from the rulings, not inferred from the absent field.

**But `LIBRARY-35`'s premise was wrong twice: the field was present, and the gate is species-side anyway.** **Two independent errors producing one report, and neither caught the other.** The second error is the one that made the first look substantiated.

**`Malachor V` keeping a world record `D-MAL-01` requires — you logged it and I confirm it from outside: no corpus entry, no menu, a `selection.json` row only.** Whether the row is the record is yours.
