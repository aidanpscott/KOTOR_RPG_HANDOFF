# BUILD 94 — a `PT-` id must resolve to one ruling

**No product code.** `MAIN_WORK/scripts/check_ruling_ids.py`, and two corrections
to `STUDY 30`'s figures found by building it.

⚠ **Scope**: `PT-1446` gives the ruling record to the owner. **This check names
what is there and decides nothing** — which of each pair is current, and
numbering `PLAYTEST-RULINGS-01:238`, are both theirs. Nothing in
`playtest/` was edited.

---

## ⚠⚠ THE DEFECT, AND IT IS WORSE THAN AN UNNUMBERED RULING

    PT-30 :490   "Surprise: no action in round 1"
    PT-30 :534   "Surprise removes the round"

**Two headings, one id, both live, and nothing on the earlier one says so.**

> **A ruling with no number is one nobody can cite. A ruling with a SHARED
> number is one everybody cites wrongly** — and there are more of the second
> kind.

**⚠ `PT-1085` is the sharpest**: its two headings carry **opposite status
markers** — `✓ UPDATED WITH EVIDENCE` against `⚠⚠ UPDATED, NOT CLOSED` — under
one id, both live. **`STATE.md`'s own confessed shape** (*"a row struck through
as answered and the same row live below it"*) **except neither is struck
through.**

## ⚠ AND IT NEEDED NOTHING RECORDED — FOURTH TIME

The file already contained both halves of the comparison and **nobody had
compared them.** The stale STUDY index, the unparseable worked example, the
extract digest, now this: **`check_extracts`' own opening complaint, four times
over.**

---

# ⚠⚠ TWO CORRECTIONS TO `STUDY 30`, BOTH FOUND BY BUILDING IT

## 1 · IT IS NINE, NOT TEN. `PT-368` IS A FALSE POSITIVE.

    :11069  ## PT-368a — ⚠ SUPERSEDED by `PT-368` and `PT-369`
    :11075  ## PT-368  — ⚠ The maalraas is NOT lightsaber-resistant

**`PT-(\d+)` with no guard on a trailing letter matches `PT-368` inside
`PT-368a`.** Two different ids with one heading each, **and one of them is
explicitly superseded.**

> **THE SUFFIX IS PART OF THE ID**, and a check that drops it merges two rulings
> — **which is the defect it exists to find, one level up.**

`STUDY 30` flagged its own regex as the risk. It was right to.

## 2 · AND THREE OF THE NINE ARE ALREADY MARKED, SO THE LIVE CLASS IS SIX

    PT-21   second heading: "is withdrawn"
    PT-394  first heading:  "⚠ SUPERSEDED by PT-401"
    PT-426  second heading: "CLOSED. Verkaal is cut"

**A heading that says it is not current is not ambiguity — it is the record
working.** The six genuinely live pairs are **`PT-29`, `PT-30`, `PT-31`,
`PT-32`, `PT-484`, `PT-1085`.**

---

# ⚠⚠ AND MY OWN CHECK ALMOST DISMISSED THE SHARPEST CASE

**First run:** `PT-1085 is no longer ambiguous — take it off the list`.

Its second heading reads **`UPDATED, NOT CLOSED`**, and a bare `closed` keyword
match **read that as closed.**

> **A keyword search that cannot see a `not` in front of its keyword reports the
> opposite of what the document says** — and it did it to the one case the study
> called the sharpest.

A negative lookbehind now, and the comment says why, **because that trap is
waiting for any future keyword check in this corpus.**

---

## ⚠ HOW IT SHIPS: A RATCHET, NOT AN ALLOWANCE LIST

`BUILD 92` argued that **a check added while a corpus is dirty ships as
permission.** So:

    the six are NAMED, with their line numbers and what each pair says
    an id NOT on the list                    → fails
    an id ON the list that stops being       → ALSO fails
    ambiguous

**The `loom_can_write_test` rule: the list can only shrink.**

**⚠ THREE CONTROLS**: a new pair fails; the same pair with one heading marked
passes; **a suffixed id beside its base passes** — `STUDY 30`'s own false
positive, asserted absent.

**⚠ AND IT DECIDES NOTHING.** It says in terms that **file order is not
authority.** It flags ambiguity; a person picks the winner.

---

## ⚠ WHAT NEITHER OF US CHECKED, AND IT IS THE QUESTION THAT MATTERS

    ⚠⚠ has it already cost something?   `audit_superseded.py` / CHECK 38 asks
                                        whether a document CITES an overturned
                                        ruling. NOBODY HAS RUN IT AGAINST THE
                                        SIX. That is the question that says
                                        whether this is a hazard or a bill
                                        already paid
    ⚠  a differently-shaped heading     the check is structural, over ##/###
                                        only — invisible to the study and to
                                        the check alike
    ⚠  decisions/ and PT-INDEX-01       unswept. Six is a PLAYTEST-RULINGS-01
                                        figure and nothing else
    ⚠  PLAYTEST-RULINGS-01:238          still has no number. Quotable by file
                                        and line, not by id
