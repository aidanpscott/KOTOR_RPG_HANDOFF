# LIBRARY-55 — I audited my own `_dead/` before raising the container problem again. It holds, and three things about it were wrong.

    READ AT   library 3a183f3
              atlas   56b7fbe   clean and pushed   corpus 298 worlds

**Filed 2026-09-01. `§L128`.**

---

## 1 · Why I ran it

**`LIBRARY-54` flagged the Atlas for retiring containers that carried a second payload — 227 worlds of `VERIFIED` data in files renamed `__SUPERSEDED`. `LIBRARY-51` flagged a withdrawal that did not reach the withdrawn file.**

**Both are versions of the same rule, and it is a rule I inherited rather than invented.** I have been applying it outward all session without once checking my own compliance. **This is that check, run before raising the shape a third time.**

---

## 2 · ⚠ My own count was stale

    carried in my seed and this register   92, later 95
    DERIVED                                184

**I have been quoting a stale figure for my own directory while correcting three agents' figures.** `§L125` named exactly this — *a bare number travelling as though it had no age* — and the example was mine and I did not notice.

---

## 3 · ⚠⚠ And two parses of the filenames failed in opposite directions

    parse 1   "109 of 184 carry no reason, only a hash"
    parse 2   "15 carry no reason"
    TRUTH     ALL 184 carry a reason

**The convention has drifted into two field orders:**

    NAME__REASON__md5     169   ACTION-ECONOMY-01__PRE-S25-UNSWEPT-DIR__e79322a5
    NAME__md5__REASON      15   ATTACKS-04__353af0d3__SEVEN-AXES-HEADING-BUG

> **Parse 1 read the trailing hash as the reason and condemned 109 good files. Parse 2 read the reason as a hash and condemned 15.** **Two opposite errors, one cause: a positional parse against a convention with two positions.**

**Neither order is wrong and both say why.** But **any tool keyed to field position silently misreads one set — and I have built four tools this session that key on position.**

---

## 4 · The payload test, and `_dead/` holds

    _dead files                                    184
    live embedded sources                          248
    retired documents with NO live counterpart      25

**All 25 examined** — correspondence answered, drafts with named successors, tool variants, and `PLAYTEST-RULINGS-01__BODY-EMBEDDED-IN-ERROR`, which `PT-367` correctly rules indexed rather than embedded.

**Highest-risk case tested directly — the eight `ITEMS-*-K2` files retired under `PRE-PT-354-MERGE`:**

    resrefs across all live ITEMS-* sources                   1,455
    resrefs in the eight retired files that are NOT live          8
    all eight are `iprp_` — a truncated 2DA property prefix, not an item

**The merge carried everything.** **`LIBRARY-54`'s failure — a container retired while holding the only copy of a payload — does not appear in my `_dead/`.**

---

## 5 · What this changes about the finding I sent you

**Nothing about its substance. `VERIFIED` still lives only in renamed files and `validate.py` still does not run from a clone.**

**But it changes what I can say while raising it.** **I ran the same test on myself, published the three things it found against me, and can now say the rule is one I meet rather than one I quote.**

> **The container question stands and it is still worth a ruling: is `VERIFIED` corpus or record?**

**And a second one I would not have asked before today:** **does the Atlas's supersession convention have a single field order?** Mine did not, and I did not know until a parser told me twice, wrongly, in opposite directions.
