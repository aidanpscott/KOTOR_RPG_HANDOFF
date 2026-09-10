# STUDY 29 — the diagonal cost was ruled, and a document says it wasn't

**Answering `Coder`'s cross-session question: does RCR give a diagonal movement
cost?** Short note, not a batch — one corrected negative and one misrouted
question.

---

## 1 · ⚠ I DO NOT HOLD RCR. THE PREMISE OF THE REQUEST IS WRONG.

`Coder` wrote *"you hold RCR and have read Chapter 12."* **I do not, and I have
not.** `STUDY 25 §6` and `STUDY 26 §6` both record it in terms:

> *"RCR was not read — it is not on this machine in any form searched. Every RCR
> claim here is quoted from our own corpus quoting it."*

**Re-verified now, wider than before:** searched the whole filesystem for
`*rcr*`, `*revised*core*`, `*d20*star*wars*`, and every `.pdf`/`.epub`/`.djvu`
under `/mnt/ga` and `/home/aidan`. **The Revised Core Rulebook is not on this
machine in any form.**

**The Extractor holds RCR** — it read ff.287, 330, 331, Chapter 15 and the skill
list for perception, and Chapter 3 for the Defence ladders. **Chapter 12 is its
read, not mine.**

---

## 2 · ⚠⚠ BUT THE COST HALF IS ALREADY RULED — AND NOT BY RCR

`MAIN_WORK/playtest/PLAYTEST-RULINGS-01.md:238`, in the table headed
**"What is still genuinely open"**:

> | **Grid diagonals** | **Ruled here: diagonal costs 1 square, diagonally
> touching is adjacent, and diagonal adjacency satisfies both melee reach and
> flanking.** |

**It is one sentence carrying three rulings:**

1. **diagonal costs 1 square** ← the half `Coder` believes is open
2. diagonally touching is adjacent ← **this is `PT-1581`**
3. diagonal adjacency satisfies melee reach *and* flanking

**`PT-1581` took clauses 2 and 3 out of a sentence whose first clause is the cost.**

**⚠ And "Ruled here" means the project decided it — it is not an RCR fact.** So
the honest answer to *"what does RCR say"* remains unknown, and **the answer to
*"what is our cost"* is settled and has been.

*(`PT-4` at line 117 rules the flanking geometry separately — *"opposite sides or
opposite corners"* — and is consistent with it.)*

---

## 3 · ⚠⚠ AND A DOCUMENT ASSERTS A SILENCE THAT IS NOT THERE

`MAIN_WORK/design/AREA-FORMAT-01.md:464` (mirrored at `HANDOFF/docs/…:464`):

> *"`§9` gives a square 2 metres and **nothing in the corpus says whether a
> diagonal counts as one square or more.** Our movement has no diagonals at all,
> so the runtime counts **the greater of the two axes** — the reading that cannot
> disagree with a move that does not exist. **A ruling replaces it in one line.**"*

**The corpus does say. It says it at `PLAYTEST-RULINGS-01:238`.**

⚠ **This is the project's own recurring shape** — a scoped negative that is wrong
because it searched the wrong document. `STUDY 19` searched `Stats/` and missed
the GUI tree; `STUDY 20` searched filenames and missed contents; `STUDY 25` found
two class tables in a file whose name said `DROID`. **This one asserts corpus
silence from `design/` without reading `playtest/`.**

### ⚠ The good news for `Coder`: the runtime already agrees

**"The greater of the two axes" is Chebyshev distance.** For a diagonal step,
`max(|dx|, |dy|) = max(1,1) = 1`.

> **The implementation already charges 1 square for a diagonal — which is exactly
> what the ruling says.** The 3.5 alternating rule would give `1, 2, 1, 2`;
> Chebyshev never does.

**So no cost code needs to change.** What needs correcting is the *comment* —
the number is **not** "mine", it is the owner's ruling, and `AREA-FORMAT-01:464`
should cite `PLAYTEST-RULINGS-01:238` rather than claim the corpus is silent.
**`MAIN_WORK` is not my path; reported, not edited.**

---

## 4 · The metres-vs-squares sharpening, checked

`Coder` suggested that if RCR gives speeds in metres, an alternating diagonal may
be **unexpressible in its own terms**. **The corpus supports the premise and not
the conclusion.**

**Premise, attested** — `ACTION-ECONOMY-01 §9`, quoted identically in four places:

> *"Square size: 2 metres. RCR's own unit — d20's 5-foot square converted to
> metric, which is why every species record reads Speed 10 metres."*

**So a speed of 10 m is exactly 5 squares.**

**⚠ But an alternating diagonal is still expressible in metres** — it would read
*2 m, 4 m, 2 m, 4 m*, which is no harder to state than *1, 2, 1, 2*. **Metric
does not forbid it.** What metric does do is make it *ugly*: a 10 m speed spends
unevenly and a player tracking metres must remember which diagonal they are on.
**That is an argument about ergonomics, not expressibility, and it is not
evidence about what RCR says.**

---

## 5 · ⚠ A DATED HYPOTHESIS FOR THE EXTRACTOR — MARKED, NOT A FINDING

**Not from any file on this machine. Offered only because it is cheap for the
Extractor to confirm or kill in Chapter 12.**

**The 1–2–1 alternating diagonal is a D&D 3.5 rule (2003). RCR is 2002 and is
built on 3.0**, where a diagonal cost one square flat. **If that holds, the
alternating rule is chronologically unavailable to RCR** — and the owner's
warning *"do not assume 3.5 carries over"* cuts in the same direction here rather
than against it.

**⚠ This is recollection, not a read, and it is exactly the kind of claim this
project has been burned by.** It should be confirmed against Chapter 12 or
discarded. **It does not change `§2`: our cost is ruled regardless of what RCR
says.**

---

## 6 · What was NOT checked

* **RCR itself — not on this machine.** `§1`.
* **`PLAYTEST-RULINGS-01` is 54,233 lines and was searched by keyword**
  (`diagonal`, `RCR`+movement terms), **not read.** A second, later ruling that
  supersedes line 238 would not necessarily have surfaced.
* **The `PT-` number attached to the line-238 ruling was not identified** — the
  row sits in a summary table rather than under a numbered heading, so it is
  quotable by file and line but not yet by ruling id.
* **No code was read or written.** The Chebyshev claim in `§3` is from
  `AREA-FORMAT-01:464`'s own description of the runtime, **not from the
  implementation.** `Coder` should confirm against the code.
