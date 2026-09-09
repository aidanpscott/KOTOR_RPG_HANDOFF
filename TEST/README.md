# TEST — what `Coder` asks `Tester` to do, and what comes back

**`PT-1446` split the work.** `Coder` builds and still tests its own slice;
`Tester` is a second pair of eyes and **never fixes**.

---

## ⚠ One writer per path, one level down

**`PT-1446` says `Tester` writes `HANDOFF/TEST/` and nothing else — and it also
says `Coder` writes its requests here.** Those collide as written, so this
directory is split:

| path | writer | reader |
|---|---|---|
| `TEST/requests/` | ⚠ **`Coder` only** | `Tester` |
| `TEST/reports/` | ⚠ **`Tester` only** | `Coder`, the owner |
| `TEST/README.md` | `Coder` | everyone |

**Neither agent edits the other's directory, ever** — not to tick something
off, not to correct a typo. **A reply to a report is a new request**, and a
reply to a request is a new report. `PT-1446`'s reason is push collisions, and
they happened all session with one agent working.

**⚠ This is a proposal until the owner folds it into `PT-1446`.** It is written
here because a convention nobody wrote down is the thing `BUILD-ORDER-01`
exists to prevent.

---

## ⚠ What a request is FOR — and what it is not

> **`PT-1446`: *"`Tester`'s value is USING the thing, not verifying it. A
> tester that only runs suites is a harness with more overhead."***

**So a request is a JOURNEY TO WALK, not a suite to run.** `Coder` can run
suites — it does, before every push, and it says so in the request. **What
`Coder` cannot do is be surprised by its own work.**

**⚠ The six defects of `PT-1443` were found by using it while 197 tests
passed.** *"These two saves look identical"* had no assertion behind it and
never could have: nobody writes an assertion for a thing they have not thought
of.

**A request that says "run the app suite" is a defect in the request.**

---

## What a request must carry

Every one of these earns its place. The last three exist because leaving them
out has cost real time.

**1 · The journey.** Concrete steps a person takes — click this, type that,
quit and reopen. Not test names, not file names.

**2 · What `Coder` claims is true.** ⚠ **Falsifiable statements, numbered, so
a reply can name one.** *"Walk out mid-fight, come back, the trooper is still
hurt"* — not *"combat persistence works."*

**3 · ⚠ What `Coder` could NOT see from where it sits.** The honest gap, and
the reason the request exists at all. A widget test renders at a fixed size
with a loaded font: it cannot tell you that two greens are a shade apart, that
a panel felt cramped, or that an option list read as an error. **This is where
`Tester` earns its keep, so it is stated rather than implied.**

**4 · What `Coder` already ran, with numbers.** So `Tester` does not spend 75
seconds reproducing a green suite. If a suite is red, **say which tests and
why**, because a `Tester` that hits a known failure and stops has lost a turn.

**5 · ⚠ KNOWN SCAFFOLDING — things that are NOT bugs.** The weapon is a fist.
The portrait is a placeholder circle. The board is drawn, not textured. Nothing
has been designed. **Nine of these exist, each with the ruling that made it
one.** Leaving this out means nine non-defects come back.

**6 · ⚠ WRONG versus UNDECIDED.** This project distinguishes a **defect** from
a **had-to-behave-somehow** — the code had to do something and no document says
which. **A request names where the rulings live** so `Tester` can file the
second kind as a question for the owner rather than as a bug for `Coder`.

**7 · Data safety, and what is real.** ⚠ **All four suites are now hermetic**
and touch nothing in `~/.local/share/kotor-rpg/` — verified by mtime snapshot.
**But USING the app is not a test: it writes real saves to the real folder**,
because that is the product working. `Tester` should know which of its actions
are real, and how to reset.

**8 · What not to touch.** Paths, per the table above.

---

## What a report must carry

**1 · ⚠ SCOPED NEGATIVES.** *"I did not find X"* is worthless without **where
you looked.** This project has produced **five** wrong-place negatives — a
correctly scoped search against the wrong location, twice inside checks built
to prevent exactly that. **Say what you checked AND what you did not.**

**2 · Three buckets, not one list.**

| | |
|---|---|
| **DEFECT** | it is wrong, and `Coder` can fix it |
| **UNDECIDED** | nothing rules it. **For the owner, not for `Coder`** |
| **AS DESIGNED** | it looked wrong and is not. ⚠ **Worth filing anyway** — if it fooled `Tester` it will fool a player |

**3 · A repro for anything in bucket one.** ⚠ **`Tester` never fixes**, so a
finding that cannot be reproduced is a finding `Coder` cannot act on. Exact
steps, and what you expected instead.

**4 · What you tried that found nothing.** ⚠ **The most under-valued half.** It
stops `Coder` re-asking, and a path that survives being attacked is worth
knowing about.

**5 · Numbered against the request's claims**, so *"claim 3 is false"* is a
sentence that can be written.

---

## Naming

    requests/NNN-short-name.md      NNN ascending, never reused
    reports/NNN-short-name.md       ⚠ THE SAME NNN as the request it answers

**A report with no request gets the next free number and says so** — `Tester`
finding something nobody asked about is the point of `Tester`, not an
irregularity.
