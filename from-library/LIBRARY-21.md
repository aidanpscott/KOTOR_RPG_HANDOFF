# LIBRARY-21 — the scheme does not carry derivation chains, and it should not. Four of my headers were defective.

**Filed 2026-09-01. `§L94`.**

---

## 1 · Answered by measuring the scheme, not by recalling how I built it

**It carries exactly one kind of cross-category statement: a BOUNDARY.** *"Why a category and not an addition to `C17`."* `C21` is the model — it names `C17`, states that `C17` holds the rules for how equipment behaves while this category holds the items themselves, and cites the rule it applied.

**It carries no derivation pointers.**

## 2 · Because the documents carry them, at the clause, with section granularity

    SPACE-COMBAT-01   "MOUNTED-COMBAT-01 §7, PORTED WITHOUT CHANGE"
                      "MOUNTED-COMBAT-01 §9's THREE ALTITUDE BANDS BECOME
                       RANGE BANDS INSTEAD — SPACE HAS NO GROUND"
    PARTY-01          "LOOT-01 §4c fell back to 'party level' — a heading
                       with no rule under it"
    FEATS-LIBRARY-01  "Stacks with the SKILL-RESOLUTION-01 §5.1 curve"

**I checked three of your 38 rather than assuming the pattern held.** All three cite at the point of use, with a section number.

> **A header pointer would be a RESTATEMENT of what the document already says — and coarser.** `C17` instead of `MOUNTED-COMBAT-01 §7`.

**This project has a measured price for restatement.** `§L75`: three restatements of one source hierarchy, three different defects, one session. `ATLAS-SEED-v3`'s own rule is *"cite it; do not restate it. Restating is how v1 and v2 drifted apart."*

**A per-clause citation cannot drift from the clause it sits in. A header summary can, silently, while looking authoritative.**

**So: the answer you said would be a real one.** The scheme does not carry derivation chains and does not need to. **You look in two places** — and what makes that cheap is that the second file is named at the exact clause, at section level, not at the top of a category.

---

## 3 · ⚠ But four of my category headers were defective

**`C23`, `C24`, `C25`, `C26` — the four I created in the S23 catch-up — carried a range, not a boundary:**

> *"Nothing in `C01`–`C22` held this material."*

**That says why a NEW category. It does not say what the category is NOT**, which is what the other twenty-two do and what a reader needs at the shelf.

**Found by your question, not created by it.** It was an inconsistency in my own scheme and would have been true if you had never asked. **All four rewritten on `C21`'s model:** `C23` against `C17`, `C24` against `C21`, `C25` against `C10`, `C26` against `C05`.

### One carries a sentence more, and hold me to the reason

**`C23`'s boundary now ends:** *"`SPACE-COMBAT-01` derives from `MOUNTED-COMBAT-01` and invents no mechanic. Read the parent before ruling on the child."*

**That is the pointer you told me not to add because you asked. Why I think it is not that:**

- **The derivation is total, not partial** — every number ported, none invented. Your claim; I verified it in the document.
- **`LIBRARY-11` recorded me holding the child with the parent absent.** The sentence records a failure that happened, not a convenience.
- **It names the document, never a section.** Deliberately coarse, so it cannot fall out of step with the clause-level citations doing the real work. **If it said `§7` it would be a second copy of a fact and could go stale. Naming the document cannot.**

**If that reasoning is thin, say so and I will cut it.** The other three carry boundaries only.

---

## 4 · Your `C12` flag — exactly right, and derivable

**`IMMEDIATE-ITEMS-BATCH` cites `CANON-01` 13 times and `METHOD-RECORD-01` 11 times.** **Its Item 1 is literally *"Verify `CANON-01 §10` against `METHOD-RECORD-01`."***

A decision record whose task is comparing two governing documents will cite both heavily. **That is the document working, and its own heading says so.**

---

## 5 · The gap I am naming rather than closing

**Nothing links two documents such that editing one flags the other.** `MOUNTED-COMBAT-01` can change and no instrument of mine will mark `SPACE-COMBAT-01` as needing a re-read.

**The md5 discipline detects that a document changed. It cannot detect that a *different* document should now be suspected.**

**I have not built a dependency graph and I do not think I should.** 38 chains would need maintaining, and **an unmaintained graph is worse than none** — `§L88`'s finding about 245 stamps with zero recomputation, in a new shape. A graph nobody re-derives would report a dependency fine when the last person to touch it was six rulings ago.

**Recorded as a known limit.** If it bites, it will bite as a stale child under a changed parent, and the thing that catches it will be what has caught everything else this month: someone reading for an unrelated reason.

---

## 6 · Currency, since you pushed mid-check

**`PT-INDEX-01` moved while I was working — re-spliced at 864 rulings to `PT-877`.**

    MAIN_WORK paths walked   234    distinct filenames  228
    embedded sources         246    overlap             160

    held & byte-current      159
    held & whitespace-only     1    METHOD-RECORD-01
    held & CONTENT DIFFERS     0
    not embedded              68

**Your 67-not-embedded against my 68 differs by one because you pushed between the two derivations.**

**And your 247 banner names against my 246 sources is the same thing from the other side.** One of my banners reads `TEMPORAL-SWEEP-LEGENDS-01.md (fork-merged by the librarian; sources in _dead/)` — a parenthetical inside the name. **`§L90`: that parenthetical made the source invisible to my own stamp tool for one commit, because my pattern stopped at the space.** Your sweep counts it as a name; mine counts it as a source. **Both right, and worth knowing before either of us reconciles those two numbers again.**

---

## 7 · One against myself

**I deleted my working clone of `HANDOFF` with this letter in it and had to write it twice.** Nothing was lost — the file had not been committed, so there was nothing to recover and nothing to be wrong about. **Recording it because the same command against a repo with uncommitted filing in it would have lost real work, and the register's rule is `git rm`, per file, visible in the diff.** I ran `rm -rf` on a clone directory, which is not that rule but sits one keystroke from breaking it.
