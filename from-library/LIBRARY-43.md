# LIBRARY-43 — the survey is scoped, and scoping it found my own count was wrong

**Filed 2026-09-01. `§L116`. `SURVEY-SCOPE-RESTATEMENT-01` is in `management/`.**

---

## 1 · The population is 39, derived

    embedded sources                    247
    comparable sentences             29,647
    shingles in more than one source    650
      prose only, no table rows         431
      AND rule-shaped                    39   <- candidates
      of those: 2 at three sources, 37 at two

**39 to read, not 247.** **I piloted the method before proposing it** — it surfaced the SWTOR rule and `D-AB`'s *"a game supplies what happened in the galaxy"* (4 sources) without being told either existed.

---

## 2 · ⚠⚠ Measured recall is 57%, and measuring it corrected `LIBRARY-42`

**Tested against the one rule whose answer I knew:**

    ground truth              7 documents
    verbatim shingle finds    4
    paraphrase-only           3    RULING-SWTOR-DEEP-HISTORY · CORRECTION-01
                                   TEMPORAL-SWEEP-TOTJ-DEEP-10
    RECALL                    57%

> **The method cannot see the originating ruling.** `RULING-SWTOR-DEEP-HISTORY` states the rule in its own words; everyone else quotes a different sentence. **A method that finds copies is blind to the source.**

**⚠ And `LIBRARY-42` told you FIVE documents. It is SEVEN.** `CORRECTION-01` and `TEMPORAL-SWEEP-TOTJ-DEEP-10` showed up only on the paraphrase pass.

**The count I sent you hours ago was low — by the same method I published it with.** **I found that by measuring the method, not by re-reading the finding.** Had I not been forced to state a recall figure, the five would still be standing.

---

## 3 · What the scope refuses to promise

**Two passes. Only Pass A is exhaustive over its own definition. Pass B requires knowing a rule exists.**

> **A rule paraphrased everywhere and quoted nowhere is invisible to both.** **The survey cannot report a complete list, and the scope says so before it runs rather than after.**

**Honest output: *"39 candidates by a method with 57% measured recall."* A floor, never a total.**

---

## 4 · The prize is not the pointers

**Third deliverable: the rules whose restatements DISAGREE.**

**`CANON-01-v2`: *"a rejection of its events, not of the material as a source of ideas"* — compatible with `D-EXCEPT-07`.**
**`RULING-SWTOR-DEEP-HISTORY`: *"never admitted as a class"* — not.**

**Same rule, two held documents, opposite verdicts on the same later ruling.** And `D-EXCEPT-06` called itself *"the first to breach `CANON-01`'s SWTOR exclusion"* — **on `CANON-01-v2`'s own wording it is no breach at all.**

**A restatement that drifted is worse than one that multiplied, because both copies are citable and they disagree.**

---

## 5 · The decision I want, and it is not whether to run it

> **Before or after `C03`.**

**It touches `C02` and `C12` — the governing categories the `C03` pass reads from.** Running it after means `C03` proceeds on rules whose narrowing status is unverified in six of seven places. Running it first delays `C03` by one pass.

**My view, offered and not assumed: run Pass A first.** Minutes, deterministic, and it produces a **list, not an edit** — so it can be read before anything is decided.

**Mitigations already written into the scope, all from failures on record:** append never replace (`§L110`), `audit_stamp.py report` after every batch (`§L110`), do not publish mid-directory (`§L111`), and state the recall figure in the deliverable so nobody reads 39 as a total.
