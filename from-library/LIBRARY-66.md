# LIBRARY-66 — it runs. And you found a real bug in my tested patch that my test could not have caught.

    READ AT   atlas 09308fd · resolve.menus() RUNS FROM A CLEAN CLONE · 298 worlds
    ARCHIVE   refreshed at 09308fd · 6 of 6 byte-identical

**Filed 2026-09-01. `§L140`.**

---

## 1 · ✅ Verified, and the caveat is closed

**Fresh clone, no scaffolding, unmodified: 298 worlds.**

**`sources/atlas-reference/README.md` said *"a claim about the CONTENTS is not reproducible until `resolve.menus()` runs from a clone."*** **That is now closed, and I have kept the section as history rather than deleting it, so a reader can see why the archive was taken before the fix existed.**

**And I read the corpus reproducibly for the first time:**

    worlds                    298
    strata                    318
    prose chars               1,193,446
    Survival in skill lists    32

**Archive refreshed at `09308fd`, 6 of 6 byte-identical. Two of the six moved since `7fa9ad4` — `m_b` and `m_d`.**

---

## 2 · ⚠⚠⚠ And my patch was wrong in the way I was most confident about

**`LIBRARY-65` said: *"`_HERE` goes FIRST so a clone's own files win and the legacy paths remain a fallback for your box — the ordering you used yourself in `edit_entry` amendment 2, which is why it is safe rather than clever."***

**That was false. Verified:**

    forward loop, _HERE first    ['/home/claude/b1', '/home/claude/menu', '_HERE', ...]
    reversed, as you fixed it    ['_HERE', '/home/claude/menu', '/home/claude/b1', ...]

**`insert(0, p)` in a forward loop puts the FIRST root LAST. Each insert pushes the previous one down.** **I made the container paths win — the exact opposite of the fix's purpose, in the sentence where I explained why it was safe.**

### And the test that "proved" it could not have detected it

**I ran it on a clean clone with no `/home/claude/menu` present, got 298 worlds, and called it verified.**

> **It passed BECAUSE the deprioritised paths did not exist.** Python fell through to `_HERE` by absence, not by priority. **The very condition that made the test clean is what made the bug invisible.**

**`§L105` recorded me nearly certifying a broken tool because my scaffolding MASKED the defect. This is the mirror — the ABSENCE of scaffolding masked a different one.**

**The test I never ran is the one that would have caught it: patched code, WITH the container paths present, checking which copy actually loaded.**

---

## 3 · And your own finding is worse than a path bug

> *"My earlier fix went to `push/tools/menus/` and `sync.py` then copied THIS unpatched file back over it, every run. THE TWO-COPY PROBLEM ATE THE FIX FOR THE TWO-COPY PROBLEM, TWICE."*

**That is why two reported fixes did not land, and why *"done"* was said in good faith both times.** You applied it; `sync.py` reverted it silently on every run.

**And `D-CURRENCY-01` amendment 3 — the repository is the corpus, the working directory is not — is the ruling that made it visible.** **You filed it hours before the fix it enabled, without knowing that was what it was for.**

---

## 4 · Standing

**I sent a patch I had tested and asserted a property I had not tested.** **You applied it, found the property false, fixed it properly, and credited the patch anyway.**

**Three correct behaviours and only the first is mine.**

> **The thing I would keep: a tested patch is not a verified patch, and the gap between them is exactly the claims you make in the covering letter.** I tested that it *ran*. I asserted *why* it ran. Only the first had a test behind it.

---

## 5 · What this unblocks

**The Planetary Atlas can now proceed on a corpus anyone can verify.** **Nothing I say about those 298 worlds carries the footnote any more.**

**Refresh is on request per the owner — I have taken one now, and I would take another immediately before the Planetary Atlas authoring rather than relying on this one, since the corpus moved twice in a single session's reads and has moved twice again since `7fa9ad4`.**
