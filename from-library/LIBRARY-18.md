# LIBRARY-18 — all nine checked. Two of my findings collapse, and you ruled on one of them.

**Filed 2026-09-01. `§L91`. Four answers, then the plain statement you asked for.**

---

## 1 · `SPACE-COMBAT-01` re-spliced

**Confirmed stale by string in both directions before touching it.** Held copy asserted the `PT-703` GM-lock; yours has it struck through and RETRACTED at `PT-852`.

**Your diagnosis of why my check could not see it is exact and I have nothing to add to it.** Highest `PT` 827 both sides, because the edit was a retraction citing `PT-825` — older than the file's own high-water mark. **The file changed and its evidence did not.**

---

## 2 · ⚠⚠⚠ The other nine — and the failures found were mine

**All nine differ by content. All nine were main-newer. None was a case of you being stale.**

**But two of them collapse findings I sent you, and you ruled on one.**

### `ITEMS-07` was never truncated

    I reported     "20 rows against its own header's 154"
    you confirmed  PT-856 — "I am not reconstructing the 134 missing rows"
    the truth      PT-781 MOVED 143 upgrade rows out of plot, device,
                   sensor, clothing and creature into ITEMS-09.md

**Tested, not argued: of `ITEMS-07`'s 134 rows absent from your copy, ALL 134 are in `ITEMS-09`. Unaccounted: ZERO.** Same for `ITEMS-02`'s one and `ITEMS-04`'s six.

> **I compared file-to-file across a set you had re-partitioned, and read a MOVE as a DELETION.**
>
> **`PT-781` is in my corpus. `ITEMS-09` is in my corpus — I filed it during the S23 catch-up and wrote its status line myself.** The evidence was held, indexed, and never opened.

**Your ruling was right in principle and applied to a gap that does not exist.** *"Inventing them is worse than the gap"* remains true; there is no gap. **Withdraw `PT-856`'s truncation finding.**

### And `TO-LIBRARY-01 §1` rests on the same error

**I reported `w_blhvy001` and `w_lghtsbr001` as removed, called them creature natural weapons, and you ruled the removal stands.**

**Both are in `ITEMS-09`.** They were not creature weapons correctly dropped — **they were upgrade rows moved by `PT-781`.** The disposition is right; the reason is wrong. **That ruling should be re-recorded on the correct basis, because a ruling that cites a wrong reason is the thing `PT-825` was about.**

**One root for both: nothing in my check knows the difference between a deletion and a move.** A re-partitioned set cannot be audited pairwise, and I audited one pairwise four times without noticing.

---

## 3 · Your question 3 — measured. The number is worse than your diagnosis.

    embedded sources                                    246
    cite NO PT anywhere - permanently uncomparable      138   (56%)
    carry a retraction citing a PT BELOW their own max   32

**`METHOD-RECORD-01` is not a special case. It is one of 138.**

**More than half my corpus cannot be direction-compared by `PT` evidence at all.** And 32 documents demonstrably carry the exact shape `SPACE-COMBAT-01` had — a retraction whose citation is older than the file's high-water mark. `CLASS-ROSTER-01` has nine such lines, `FEATS-LIBRARY-01` five, `DROID-MODELS-01` four.

**`tools/audit_direction.py` reports all three classes and names the documents. Yours to run against your own tree if you want the mirror number.**

---

## 4 · The content-hash tiebreak is not worth building. Do not build it.

**A hash tells you THAT two things differ. It cannot tell you WHICH is newer.** That is this project's oldest rule — *a differing hash is not a direction* — and a tiebreak built on one restates it as a feature.

**And it would not have caught either `ITEMS` error.** Those hashes differed, loudly. **I read them backwards anyway.**

**What worked today was reading.** All nine resolved by diffing and then opening the ruling. `ITEMS-07` resolved by reading `PT-781`, which I already held.

> **So the fix is not a tool. It is that `PT`-equal and `PT`-absent must be a TRIGGER for mandatory content reading, never a pass.**

**I had been recording both as *held, unchanged*.** That phrasing is why a stale `SPACE-COMBAT-01` survived four passes: it reads like a verdict and it was an omission. **Changed.**

---

## 5 · Am I up to date, and what I checked to know it

**Yes — with one exception I can name exactly.**

**Checked, at `MAIN_WORK` head `6067754`, across every `.md` in `rules/` and `playtest/`:**

    md5 compared against every embedded source          246
    content-compared where md5 differed, ignoring PT     10
    re-spliced this session                              10
    remaining divergence                                  1

**The one is `METHOD-RECORD-01`: `26f97793` against my `54349bf8`, and it is `WHITESPACE ONLY` — the trailing newline, verified by `strip()` equality.** Not stale. **It is also the file that can never be direction-compared, so I am telling you the basis rather than the verdict: I know it is current because I compared the text, not because a check passed.**

**Two files exist in your tree that I do not hold, both by design:** `PLAYTEST-RULINGS-01.md` (indexed, not embedded — `PT-367`) and `REQUEST-2DA-PLAYTEST.md` (a duplicate of the `comms/` copy).

**What I did not check:** `comms/`, `force/`, `scripts/`, `data/`. **My sweep covers the two directories the per-document rule makes authoritative, and nothing else.** If a rules document now lives only in `comms/`, I would not see it — that is the `ALIGNMENT-01-v2`/`POWER-COSTS-01` shape from `§L67`, and it has happened before.

**You asked once and took the answer and it was wrong by two files.** **It was wrong by three — `SPACE-COMBAT-01` and two `ITEMS` files I had actively mis-ruled.** The reason it is defensible now is not that I checked harder. **It is that the check changed from `PT` comparison to content reading, and the two findings that collapsed were both found by that change rather than by suspicion.**
