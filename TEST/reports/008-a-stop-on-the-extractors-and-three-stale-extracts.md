# 008 · A stop on the extractors, and the three stale extracts

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** Read-only throughout:
I ran one script, `check_extracts.py`, **after reading it to confirm it only
opens files for reading**. Given `PT-1469`, reading before running was the
whole lesson.

---

## ⚠⚠ 1 · STOP — "make the six agree" is not mine to do

**Two separate rules, and both are explicit.**

> `PT-1446`, and every request so far: *"**Write only `HANDOFF/TEST/reports/`.
> Not the product repos, not `MAIN_WORK`, not `HANDOFF/BUILD/`. Do not fix
> anything you find**"* — and *"a tester that fixes is a second builder."*

**All fourteen extractors, `_paths.py`, `check_extracts.py` and
`check_engine_pin` are in `MAIN_WORK/scripts/`.** Making them agree is (a) a
fix and (b) in `Coder`'s lane. **It fails both tests, not one.**

⚠ **And `PT-1469` already ruled on it deliberately:** *"THE ARGUMENT ORDERS ARE
STILL INCONSISTENT AND THAT IS RECORDED RATHER THAN FIXED."* I am not going to
quietly convert a recorded deferral into a Tester edit.

**What was NOT done about it:** nothing. I did not touch a script, did not stage
a change, and did not run any extractor. **I spent the turn measuring the thing
instead** — below — so that whoever does it has the real population.

---

## ⚠ And the measurement is why the stop was worth taking: it is not six

`_paths.dest()`'s own docstring records the shape as **four `(source, dest)` and
two `(dest)`**. **I counted fourteen extractors in four shapes**, and the
dangerous shape has **seven members, not two.**

### ⚠ Shape A — `argv[1]` is the DESTINATION, source hardcoded · **7 scripts**

    extract_chassis.py            SRC = design/CHARGEN-DATA-01.md
    extract_droid_skills.py       SRC = rules/DROID-SKILLS-01.md
    extract_event_kinds.py        SRC = design/EVENT-KINDS-01.md
    extract_first_level_feats.py  SRC = design/CHARGEN-DATA-01.md
    extract_starting_equipment.py SRC = rules/STARTING-EQUIPMENT-01.md
    extract_feats.py              argv[1] → _dest()
    extract_items.py              argv[1] → _dest()

**Hand any of these seven a source path and it writes the JSON over it.** That
is the `FEATS-LIBRARY-01.md` destruction, and it is available from five more
scripts than the ruling records.

### Shape B — `argv[1]` = source, `argv[2]` = dest · **5 scripts**

    extract_classes.py · extract_powers.py · extract_professions.py
    extract_programmings.py · extract_species.py

### ⚠ Shape C — `argv[1]` = source, and it writes NOTHING · **1 script**

    extract_skills.py    src = sys.argv[1]; prints counts, never dumps

### Shape D — takes no argument at all · **1 script**

    extract_equipment.py   dest comes from a variable

**⚠ So `argv[1]` means "the file I will overwrite" in seven scripts and "the
file I will read" in six.** Same single-argument invocation, opposite meaning,
and the two populations are near-equal — which is why no habit protects you.

⚠ **"Make the six agree" would leave eight of the fourteen disagreeing**, and
would leave five of the seven dangerous ones untouched. **That is the reason
this was worth stopping on rather than doing badly.**

**`_paths.dest()` refuses a `.md` destination**, which covers Shape A pointed at
markdown. ⚠ **It does not cover Shape A pointed at a `.json` source** — and
`worlds.json` is a resolver export that is a source to nothing but is still a
`.json` file sitting in the same tree.

---

## 2 · The three stale extracts — attributed by date, not by inference

    ⚠ STALE chassis.json            CHARGEN-DATA-01.md
    ⚠ STALE event_kinds.json        EVENT-KINDS-01.md
    ⚠ STALE first_level_feats.json  CHARGEN-DATA-01.md

**It is three extracts but only TWO stale sources** — `chassis` and
`first_level_feats` both derive from `CHARGEN-DATA-01.md` and carry the same
recorded md5.

| | source last edited | extract last regenerated | verdict |
|---|---|---|---|
| **chassis · first_level_feats** | `3c15c33` **09-09 14:19** — `PT-1467`, +30 lines to `CHARGEN-DATA-01.md` | `a46f6e9` **09-09 09:43** — `PT-1461` | ⚠ **stale by 4h36m — caused by `PT-1467`** |
| **event_kinds** | `7e22922` **09-08 15:50** — `PT-1435` | `5510cbf` **09-08 07:51** | **stale ~8h, and now a full day** |

### Whose they are

- **⚠ Neither is mine.** No `Tester` report caused a source edit that outran an
  extract. I checked every source edit against every regeneration by commit
  date rather than by `PT-` number.
- **`chassis` and `first_level_feats` are the current slice's own.** `PT-1467`
  added 30 lines to `CHARGEN-DATA-01.md` — **the annotation convention that
  `PT-1469` reports on left two of its own extracts behind.** That is the
  actionable pair.
- **`event_kinds` is the deliberate one**, and it matches `STATE`: *"14 emitted
  kinds are not in `EVENT-KINDS-01` … writing them into the document is the
  owner's."* The document moved at `PT-1435`; the extract is correctly waiting.

### ⚠ And one thing to know before regenerating the pair

**Re-running an extractor is the operation that erased eighteen `_notes`
paragraphs**, and `a46f6e9` — the last regeneration of exactly
`chassis · droid_skills · first_level_feats` — is the same three files.

✓ **I checked, and it looks safe now:** all three still carry a `_notes` key
today, and `extract_chassis.py` and `extract_first_level_feats.py` both
reference `_notes`, consistent with `PT-1469`'s *"they live in the scripts
now."*

⚠ **Scoped:** I verified the notes are **present in the files and referenced in
the scripts**. I did **not** verify the round-trip, because that means running
an extractor, and an extractor writes.

---

## ⚠ 3 · The carry-forward, and it lands on the check you cited as the good one

> *"`check_extracts` says 'current 32', which is a denominator."*

**⚠ It is not a denominator. There are 19 extracts.**

    data/extracted/*.json                    19 files
    declared source-comparisons              34
    + worlds.json, a resolver export          1
    = what the check tallies                 35   → printed as "current 32 · stale 3"

`classes.json` and `items.json` **declare nine sources each**, and the counters
increment **per source**, not per file. So `32` is a count of md5 comparisons in
one unit, printed beside `stale 3` in what looks like the same unit, over a
population of 19 in a third.

**⚠ Which means it carries the exact failure you described.** If
`data/extracted/` silently lost five single-source files, the line would read
`current 27` and **nothing would say the population had changed** — the same
shape as `check_engine_pin` printing `2 compared` where it had compared 4.
**The check that was offered as the counter-example is the check that has it.**

**What it never prints, and what would have caught it:**

- **19** — how many extracts it opened
- its four `SEARCH` roots (`rules`, `force`, `design`,
  `../HANDOFF/STUDY/_reference` — all four exist today; **I checked, because a
  silently missing root is a silently narrowed scope**)
- that two files carry nine sources apiece

**I am not changing it** — same lane, same rule. Recording it because you asked
that the next person to touch a check make its scope the loud part, and this is
the concrete version of that for this check.

---

## ⚠ One correction, small and factual

**The restore was not mine.** *"Your restore worked because the corpus was
tracked and clean"* — I have never run an extractor, restored
`FEATS-LIBRARY-01.md`, or written anything outside `HANDOFF/TEST/reports/`.
`PT-1469` records it as the slice's own note (*"ITS OWN NOTE IS THE IMPORTANT
HALF: RESTORED FROM GIT"*). **Flagging it only because an attribution that
drifts is how a wrong-place negative starts.**

---

## ⚠ Scoped negatives

**What I read:** all 14 `extract_*.py` argument handlers, `_paths.dest()`,
`check_extracts.py` in full, `PT-1468` and `PT-1469`, and the git history of
`CHARGEN-DATA-01.md`, `EVENT-KINDS-01.md` and the three extracts.

**What I ran:** `check_extracts.py`, once, after confirming it only reads.

**What I did NOT do:**

- **Change anything.** No script, no data, no staged edit — see the stop
- **Run any extractor**, in any shape, with any argument
- **Verify Shape A's overwrite by trying it.** ⚠ I read the seven `_dest(argv[1])`
  call sites; **I did not point one at a source to watch it destroy the file**,
  and I would not
- **Check `check_engine_pin`'s current scope.** You reported it; I did not
  re-derive it
- **Test anything in the app this turn.** This is a read, like `005`, and the
  distinction matters — **`006` and `007` were play sessions and this is not**

**No app was launched, and the live folder was not touched.** My saves —
`rell-vantt`, `t3-m4-probe`, `t3-k9` and the rest — are as `007` left them.
