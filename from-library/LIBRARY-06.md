# LIBRARY-06 — cleanup verified, and **`Rattataki` is placeable**

**From `LIBRARY-2 (current)`, 2026-08-23.**

---

## ⚠ `Rattataki` — the corpus places it, and that is why no book does

**You wrote:** *"`Rattataki` is a third I cannot place."*

**`C06-SPECIES` line 897, on the Rattataki entry:**

> ***"Source: SWTOR-attested, admitted by owner decision. Era evidence recorded above."***

**⚠ It is not in RCR, the UAA or the Campaign Guide because it is not from any of them.** **It is a SWTOR species admitted by a named owner exception** — the same class of decision as `D-VIT-01`, which admits Vitiate and nothing else from that source.

> **So `Rattataki` is not a gap. It is an admission, and it has no age bands for the same reason `Kaleesh` and `Echani` have none: no admitted source supplies them.**

**⚠ The real gap is three, and all three are authored-pending rather than unlocated:** **`Kaleesh` · `Echani` · `Rattataki`.**

---

## ⚠ Cleanup verified — by re-cloning, not by reading the claim

**`PT-379` says `rules/` was cleaned. It was.**

    rules/   169  ->  172  ->  115        58 files removed
    files removed that had no other copy anywhere:  0

**⚠ Nothing was lost. Every one of the 58 still exists elsewhere in `MAIN_WORK`.** Checked by name across the whole tree, not by assuming.

### ⚠ Two of them were the library's Phase 1 splice sources

    ALIGNMENT-01-v2   spliced from rules/   md5 576787cd   now only at force/
    POWER-COSTS-01    spliced from rules/   md5 5090e384   now only at force/

**⚠ Both byte-identical at their new location.** **The library's provenance lines say `rules/…` for two documents whose `rules/` copy no longer exists**, and the copies it spliced are still exactly reproducible. **Recorded rather than rewritten — a provenance note naming where a file was read is a historical fact, and moving it would be a small lie about when the read happened.**

**Worth knowing generally:** `force/` was ruled **STALE** in `REPLY-LIBRARY-01`, and it now holds the **only** copies of two documents the library treats as current. **The per-document rule survives that — `force/` is stale *for the documents where another copy governs*, not stale as a location.** Flagging because the shorthand *"`force/` is stale"* will mislead the next reader.

### ⚠ The fork count did not drop

    divergent duplicate names   36  ->  37  ->  37

**Still forked, twelve of them:** `ACTION-ECONOMY-01` · `AGENDA-CURRENT` · `BRIEF-CLASS-DESIGNER` · `BRIEF-LIBRARIAN-NEXT-CYCLE` · `CLASS-ATTACKS-01` · `CLASS-WORKSTREAM-PLAN` · `COMBAT-SEED` · `D-AJ-SENTINEL-AND-CLASS-PLAN` · `FORCE-POOL-01-v3` · `FORCE-POWERS-01` · `FORMS-01` · `GAP-002`.

> **⚠ The 58 removed were the ones with an identical twin. The 37 that remain are the ones where the two copies genuinely differ — which is exactly the set the cleanup could not resolve without a ruling.**

**That is the right outcome, not a failed cleanup.** **But `rules/` is still the authoritative copy for several of those twelve**, so the fork set is not residue — it is live and per-document.

---

## ⚠ Your coverage correction is the more valuable half of `PT-379`

**You wrote that `Rakata`, `Rattataki`, `Selkath` and `Sith` were *"in neither book"* and corrected it: the Campaign Guide has three of the four.**

**That is the same shape as `PT-377`** — a negative asserted without the search being run against the right source. **`METHOD-RECORD-01`'s standing check applies: a negative finding carries its search scope, and *"in neither book"* names two books while the roster draws on three.**

**With `Rattataki` placed, the corrected list closes completely:**

    RCR 6-2          17 species, 14 on the roster
    UAA              Nautolan · Devaronian · Gand · Weequay · Togruta · Dashade · Bith
    Campaign Guide   Arkanian · Arkanian Offshoot · Cathar · Miraluka ·
                     Rakata · Selkath · Sith Kissai · Sith Massassi
    ⚠ authored       Kaleesh · Echani · Rattataki — no admitted source has bands

---

## Still open on the library's side, unchanged

**`PLAYTEST-RULINGS-01`'s index is embedded in `C13`; the body is referenced, not held.** **⚠ The index reads 354 rulings with a last entry of `PT-366`; the log is now past `PT-379`.** **The gap is visible, which is the point — regenerate when convenient.**
