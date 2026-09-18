# `sync_docs.py` is gone — `PT-2338`

**It copied every `docs/` file whose hash differed from the working tree, in
one pass, with no idea what it was overwriting.** That is safe for a file the
mirror is merely BEHIND on. It is destructive for one that has **forked** —
where each side holds lines the other lacks — and six of the published
documents are forked today. **A single accidental run would have destroyed 937
lines of real, deliberate local content.**

**⚠⚠ THE SCRIPT WAS ALREADY DOCUMENTED AS GONE WHILE IT SAT HERE WORKING.**
`check_docs_mirror.py`'s own docstring said *"`sync_docs.py` is gone"* — a
sentence written about a file that still existed, still resolved its paths, and
still ran. Believing it was the reason nobody looked.

## What replaced it

**`MAIN_WORK/scripts/check_docs_mirror.py`, and it deliberately does not copy.**
It reports two different facts and refuses to guess between them:

    STALE   the mirror is behind: every line it has, the source has
    ⚠ FORK  each side has lines the other lacks

**A stale file is a copy; a forked one is a decision.** `PT-2336` copied the
rulings ledger on exactly that basis — confirmed STALE first, then copied.

## What is still open

**Twelve documents are stale and six are forked, and that question is held.**
`EQUIPMENT-01` is 1,209 lines behind in the copy a designer actually reads.
**Reconciling them is real work that needs a decision per forked file**, which
is why removing the script did not wait for it: the hazard and the question had
different urgencies, and the smaller safe action was waiting on the larger hard
one.

**⚠ DO NOT REBUILD THIS AS A BLIND COPIER.** Anything that replaces it has to
read `check_docs_mirror`'s classification first and refuse the forked half.
