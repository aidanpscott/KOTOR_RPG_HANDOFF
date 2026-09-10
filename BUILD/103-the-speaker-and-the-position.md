# BUILD 103 — the speaker is derived, and a position must be usable

**1,047 green** — Lodestar 456 · Lens 7 · Loom 217 · app 367 · `+30`.
Lodestar `bef95c7` · Loom `813d58d` · app `fb666f0` · MAIN_WORK `2cf773e`.
Pins level. Gate SENDABLE — 50 checks now.

---

# ⚠⚠ `PT-1607` — `owner` IS NOT CONSULTED, AND IT NOW HAS NO READER AT ALL

`DialogueRun` takes `speaking`, and it is **required** — the same reason
`strike`'s `distanceSquares` is (`PT-1593`): *so a caller cannot forget it.* A
default would have put the old answer back through the door marked
*convenience*. `by` defaults to it too, because `§6`'s *"defaults to
`conversation.owner`"* was the same second answer one line down.

## ⚠ WHAT `owner` IS STILL FOR — ASKED, AND THE ANSWER IS NOTHING

    the default speaker       PT-1607 — the placement you walked into
    `by`'s default            the same, one line down
    "who you are talking to"  the blueprint already says it, the other way

> **⚠⚠ SO ITS ONLY READERS ARE THE TWO CHECKS THAT IT IS WRONG.** A required
> field whose sole consumer is a validator asserting it is not broken. Stated on
> the field rather than left to be discovered.

**⚠ And those two change in WORTH rather than going away.** Before `PT-1607`
they caught a creature being renamed on screen; after it they catch a stale
field in a file. Still a wrong file, still only catchable at rest — **but the
consequence they used to name is gone.** They stay while `§1` requires the
field; dropping it is a format change and yours.

**⚠ And the turned-over test is the ratchet.** `dialogue_run_test` asserted
`b.speaker == 'guard.01'` — **the file's `owner`** — so it went red the moment
the rule landed, and it now asserts the opposite plus a case proving the same
file gives a different speaker to a different placement.

---

# ⚠⚠ `PT-1605` — THE FALLBACK, ON EVERY PATH THAT PLACES A CHARACTER

The `landing != null` branch put you on the arrival's square whatever was
painted over it, while the resume branch **two branches up** had been defended
since `PT-1526`.

**⚠⚠ AND A FALLBACK SAYS SO, which is the half not in the ruling's letter but
in its reason.** *Silently depositing a character in a wall was the defect;
silently rescuing them is only half better* — the author cannot fix what nobody
reports, and `PT-1604`'s validator runs at REST while this is the one surface in
PLAY that knows.

    Starboard Hold — arrived at north · the arrival "north" is not
    standable, so you are at 0,0

**⚠ AND THE CRASH CASE IS CLOSED.** A room with **no passable square at all**
arrives, says *"you are at nowhere in it"*, keeps drawing the board, and takes a
keypress without throwing. Verified by breaking the fallback and watching the
case go red.

---

# ⚠⚠ THE POSITION CATEGORY — FOUR MEMBERS, AND THE FOURTH PRE-EMPTS

    areaHasNoStandableSquare   nobody can stand anywhere — REPORTED ALONE
    landingNotStandable        declared, and not a floor
    connectionUnreachable      you can get in and cannot reach the door
    areaHasNoWayOut            no reachable door AT ALL, including none declared

**The fourth is reported alone and the other three are skipped**, because with
no passable square every one of them is true — **three faults saying the same
thing in three vocabularies is how a person comes to think there are three
problems.** Same argument `targetAreaUnreadable` makes about a connection that
*could not be checked*.

**⚠ AND `areaHasNoWayOut` IS NOT `connectionUnreachable` REPEATED.** That one
fires per door; this fires when there is no reachable door at all — **including
when the area declares none**, which no per-door check can see, because there is
no door to report it against.

**⚠ AND TWO CLAUSES KEEP IT FROM BEING A NUISANCE:** a one-area package has
nowhere to go by design, and **an area nothing leads to is not reported** —
*"a character who walks into it and can never leave"* is a false sentence about
a room nobody can walk into.

## ⚠⚠ REACHABILITY USES THE FOUR KEYS, NOT `PT-1588`'s EIGHT

`PT-1588` rules a diagonal costs one and a creature may walk it — **`approach`
does** — but `_step` binds four arrows and nothing else moves the player.

> **The narrower set is the safe one: this may report a way out that exists,
> and must never miss one that does not.** The day `PT-1443` or four more
> bindings land it widens to `stepOffsets` and **only ever loosens** — the
> direction a check may move without re-auditing what it passed.

**Third place eight-versus-four has become load-bearing**, after the cleave and
the enemy's approach.

## ⚠ AND IT FIRES ON A REAL PACKAGE

`tester-probe` `a03-probe-yard` and `a04-probe-slit` are **one-way rooms**: a01
leads to both and neither leads anywhere. Two soft-locks, shipped, found by a
check that did not exist this morning.

**⚠ And three fixtures went red — correctly.** Two-room test beds where the
second room has an arrival and no door ARE soft-locks. **The fixtures were not
wrong and neither was the check**: what was wrong was asserting over
`faults.single` and `report.ok` — *a check aimed at the whole report when its
subject is one clause of it.* Narrowed, not weakened.

---

# ⚠⚠ `PT-1603` — A CONVERSATION LEAVES A RECORD NOW

The three `_log.addAll` in the dialogue path persist. **And the filter is the
DECLARED LIFETIME, not a list in the screen:**

> `SAVE-LOAD-01 §4`: *"lifetimes decide what is written in the first place"* —
> **a sentence the corpus has carried since `PT-1420` and which every persist
> site in this app ignored in favour of hand-picking its own kinds.** A path
> that forgot simply did not write, which is exactly what happened.

`ChargenSource.campaignKinds` reads `event_kinds.toml` off the shelf. **⚠ So if
`encounter.began` should not be `campaign` — `PT-1606` calls that lifetime the
wrong part — the repair is one cell in `EVENT-KINDS-01` and nothing in the code
changes.** That is the whole reason the vocabulary is read rather than restated.

**Controlled**: the case asserts nothing is written BEFORE the choice, asserts
both kinds after, and asserts `check.resolved` — declared `transient` — is
**not** written, or the filter would be a pass-through wearing a lifetime's
name. Removing one `_persist` turns it red.

---

# ⚠⚠ `PT-1608` — THE DEFERRAL LIST HAS A TRIGGER NOW

`STATE.md` gains a **DEFERRED** table: what, what it costs, and **the condition
that was supposed to fire** — because the condition is the part that failed, not
the estimate. `BUILD 93`'s palette gesture and `BUILD 43`'s viewport sweep are
in it.

**⚠⚠ AND `STATE.md` WAS ITSELF THE DEFECT.** It says *"rewritten in full each
time, never appended"*, went eleven slices stale, was repaired at `BUILD 37`
with that warning added at the top — **and then went sixty-four slices stale**
carrying `BUILD 39`'s heads and *"846 tests"* against 1,047. **The warning did
not help, because a promise is not a trigger.**

So `scripts/check_state_fresh.py` compares the head table to the real heads and
checks the deferral section exists. **⚠ REPORTING, NOT BLOCKING, AND THAT IS
`PT-1600` APPLIED TO MY OWN NEW CHECK**: one that went red whenever any
repository moved would be red on most pushes including a peer's, and **a check a
person cannot get green by doing their own job is a check that gets turned
off.** Its job is to be read, which is the thing `STATE.md`'s own italics could
not manage. Gate: 49 → 50, still SENDABLE.

---

# ⚠ AND ONE THING I DID TO MYSELF, WORTH RECORDING

Verifying `PT-1603`'s instrument I broke the code, watched the test go red —
and then **restored it with `git checkout --` on the whole file**, which
reverted every `play_screen` change in the slice. Caught immediately by grepping
for the symbols; nine edits reapplied and the three suites re-run green,
including `PT-1596`'s, which is how I know nothing older was lost.

> **A destructive restore chained onto a verification step is a bad habit even
> when it is caught.** The verification is worth keeping; the `checkout` should
> have been the inverse patch.

---

# STILL OPEN

`owner` is a required field with no reader — dropping it is a format change ·
one conversation, one owner, N placements · `encounter.began`'s `campaign`
lifetime · `§5` has no second interaction the product can reach · the two
deferrals, now in `STATE.md` · and everything carried from `BUILD 102`.
