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

---

# ⚠⚠ AND THEN `STUDY 30` CAME BACK WITH THE CAUSE AND THE BILL

**Both verified here before folding in.**

## ⚠⚠ FOUR OF THE SIX ARE ONE EVENT

    :462  # Added after S6   →  PT-29 · PT-30 · PT-31 · PT-32
    :512  # Added after S6   →  PT-29 · PT-30 · PT-31 · PT-32

**The S6 batch was written up twice and both were kept** — and it is a
**re-drafting, not a copy**: `PT-31` goes from *"`Ready` is the ranged answer to
an approaching enemy"* to *"No change to reactions. Use `Ready`."*

> **A duplicated SECTION is a duplicated decision. One line to see, four to
> chase.**

**It is the only duplicated top-level heading in the file** — checked. The check
reports it as the cause, with its own ratchet, so **the owner is making THREE
decisions and not six.**

## ⚠⚠ AND THE BILL IS `PT-484`, NOT `PT-1085`

I called `PT-1085` the sharpest. **The exposure is somewhere else.**

`BEASTS-ATTACKS-01` cites `PT-484` **four times** — 148, 355, 880, 900 — and the
citations rely on the **second** heading, *"NATURAL WEAPONS ARE PER-BEAST, NOT
PER-TYPE."* **The first, unmarked heading is narrower**: *"HERD ANIMAL weapons
are per-beast."*

**Lines 880 and 900 cite it about a biting, clawing beast and about a PACK
predator** — neither of which the herd-animal version licenses.

> **Nothing is wrong today. And the earlier heading is at 15447 against the
> later at 15503, so THE WRONG VERSION IS THE ONE YOU REACH FIRST.**

**`PT-1085` has no substantive citation at all.** *The sharpest-looking case and
the one that could cost something were not the same case*, which is worth more
than either finding.

## ⚠⚠ AND A FLOOR ON THE ID COUNT, BECAUSE TWO OF THREE INSTRUMENTS GOT IT WRONG

`LIBRARY-12:15` — **same file, same ids**:

> *"The pattern dropped every one- and two-digit ruling id — PT-21, PT-29,
> PT-30, PT-31, PT-32, and the rest. It did not error. **IT RETURNED A SMALLER
> NUMBER THAT LOOKED LIKE AN ANSWER.**"*

**`STUDY 30`'s regex invented a duplicate; that one dropped forty. Both returned
a number that looked like an answer.** So the check pins `ID_FLOOR = 1538`.

**⚠ A FLOOR RATHER THAN A PIN**, because rulings are added and never removed: a
pinned count would fail on the owner's next ruling and teach everyone to bump
it. **A floor cannot be satisfied by a pattern that silently matches less**,
which is the only failure it is for. **Controlled**: narrowing the regex to
three-digit ids reports *1448 against a floor of 1538* and fails.

---

## ⚠ WHAT NEITHER OF US CHECKED, AND IT IS THE QUESTION THAT MATTERS

    ✓  has it already cost something?   ANSWERED by `STUDY 30`, above. Not
                                        yet, and `PT-484` is the near miss
    ⚠  a differently-shaped heading     the check is structural, over ##/###
                                        only — invisible to the study and to
                                        the check alike
    ⚠  decisions/ and PT-INDEX-01       unswept. Six is a PLAYTEST-RULINGS-01
                                        figure and nothing else
    ⚠  PLAYTEST-RULINGS-01:238          still has no number. Quotable by file
                                        and line, not by id
