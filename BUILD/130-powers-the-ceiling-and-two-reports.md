# BUILD 130 — powers at level 1, the reply ceiling, and two things already done

`PT-1697`, `PT-1696 §5`, plus the two report items.

---

## 1 · `PT-1697` — THE NUMBER IS THE RULE, NOT A LITERAL

`picks: 2` sat in `hub.dart` as a bare literal, with a comment saying the
`+1 per level after` half was **deliberately unapplied** because
`POWER-COSTS-01 §6` called acquisition open.

**`PT-1697` closes that status for this question**, so the progression is
written whole, once:

```
powersKnownAt(level: 1) → 2 · level 2 → 3 · level 20 → 21 · level 0 → 0
```

**⚠ ONE FUNCTION, NOT A PER-CLASS TABLE**, because the ruling is explicit about
what it does **not** settle: *"whether individual classes WITHIN each track
differ from each other."* A table would be that answer, invented.

**⚠ The `+1` half has a home and no caller.** Nothing levels a character up, so
creation asks for level 1 and that is all — **and the level is 1 because
creation is**, not because a `1` was convenient: `PreHubResult` carries a
species, a variant, a model and a class, and no level.

`POWER-COSTS-01 §6`'s Acquisition row is **narrowed, not struck.**

## 2 · `PT-1696 §5` — NINE, AND TWO CONSTRAINTS ARRIVE AT IT

**Seven is the floor.** What happens past it was mine to choose, and this
project's own rules rule out two of the three:

    scroll    BUILD/34: "anything you can click must be laid out where it can
              be seen, and a scroll view is only safe for things you READ."
              The NPC's line is read; the options are clicked.
    truncate  §4c hides a failed option rather than greying it, which assumes
              THE LIST YOU SEE IS THE LIST. An option that exists and is not
              drawn is absence-versus-error on the one surface where absence
              already means *gated*.
    refuse    what is left — and PT-1379's shape: the Builder must not be able
              to author the fault its own validator detects.

**⚠ AND THE NUMBER WAS MEASURED, NOT ARGUED.** My first probe guessed the
panel's geometry and reported an overflow at **five**, which was the harness
rather than the panel. Reading the real box off a running screen — **480 ×
683.2** at 1280×720 — gives:

| options | |
|---|---|
| 5 · 7 · 8 · 9 | fit |
| **10** | **overflows by 19 pixels** |

And `PT-1303` picks a reply by **digit**: the digits are 1–9, so **a tenth could
be drawn and never chosen.** Layout and input arrive at the same number
independently — the shape `§3c`'s ten squares has, where KOTOR's blueprints and
RCR's darkvision agree.

**⚠ It counts what is AUTHORED, not what will show** — `§4c` hides a failed
gate, so the drawn list is never longer, and **the worst case is every gate
passing**, which is the case a validator has to hold.

**⚠ `then` IS NOT CAPPED.** `PT-1432` makes it *pick one* — a fallback chain,
walked until a gate passes — so **nothing about it reaches the panel.** A
mutation that caps it fails.

## 3 · ⚠⚠ THE FOURTEEN KINDS ARE ALREADY DONE — `PT-1418` PAID IT

Checked before building. **All fourteen are first-class entries in
`EVENT-KINDS-01`**, each with a lifetime; the check has **no exception list at
all**, and its own note says why:

> *"The exception list is GONE, not emptied… with an exception list this passed
> while fourteen kinds were undeclared; without one it cannot."*

`emitted_kinds_test` passes, all fourteen grep in the document, and the only
allowance anywhere near this is `check_event_producers`' `ONLY_FROM_CONTENT` —
**three entries, each with a reason, and pointing the other way** (declared and
not written). **`STATE.md`'s entry is stale**, not queued work.

## 4 · ⚠⚠ THE DISCARD LIST — THE PRECEDENT IS ITS OWN, AND IT IS ALREADY SHIPPED

The ask was to find precedent before semantics get invented. **There is
precedent, and the strongest is `step-reopened` itself: the semantics exist, in
one document and in three pieces of code, while the other document says they do
not.**

### What is already true, precisely

| | |
|---|---|
| payload | `discards` — **a list of STEP NAMES**, not fields, not indices |
| written by | `ledger_writer.dart`: the reopened step **itself**, then every step after it |
| read by | `replay`'s `case stepReopened` → `clear(name)` for each |
| `clear` | maps a step name to the record fields that step owns — **nine cases** |

### ⚠⚠ And the two documents disagree about whether this is settled

- **`EVENT-KINDS-01`** describes it as done: *"It carries **the list of steps it
  discarded**, so replay can clear exactly those slices."*
- **`CHARACTER-RECORD-01`**, under the heading *WHAT THE RE-LOCK WRITES IS
  UNRULED*: *"six fields today, by assignment… **Nothing has ruled what it
  writes.**"*

**Both are `PT-1411`/`PT-1415`-era.** The second is also **stale on its own
count** — `clear` handles **nine** steps, not six fields.

### Other discard-shaped things in the format

- **`SAVE-LOAD-01 §198`** — the sibling one layer up: *"playing forward from an
  earlier point writes a REWIND EVENT. `PT-1415`'s `step-reopened` is exactly
  this shape one layer up: the rewind names what it discards, replay honours it,
  and nothing leaves the log."* **It is unbuilt**, and it cites `step-reopened`
  as ITS precedent — so it inherits rather than sets.
- **`CHARGEN-DATA-01 §90`** — a different sense, and the one transferable
  warning: `recommend_order` discards the source's rank numbers because
  *"a consumer keying on rank silently drops feats."* **Name a thing by its
  stable identity, not its position** — which argues for step NAMES over
  *"everything after index N"*, and is what the code already does.

### ⚠ The one thing I would put in front of a ruling

**`clear` ignores a step name it does not recognise, silently** — the `switch`
has no default. So **an old log naming a step this build no longer has replays
as though nothing was discarded**, which is the exact failure the discard list
exists to prevent: the code comment says it carries the list *"rather than
leaving replay to derive it… and would then replay an old log differently the
day the order changes."*

**Not fixed here** — what an unknown step name should mean is a ruling, not a
repair, and it is the thing the payload's semantics turn on.

## 5 · ⚠ A FLAKE SEEN ONCE, NOT REPRODUCED

`whole_loop_test`'s two cases failed in one full run and passed alone and in a
second full run (455 green). **Recorded rather than ignored**: that file reads
the real shelf, which `Tester` is actively publishing to, and it is the fourth
time a shared-folder test has moved under this suite.

## 6 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| no reply ceiling | the tenth-is-refused case |
| the cap drops below the floor | all three ceiling cases |
| `then` is capped too | the `then` case |

## 7 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 566 | **573** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 455 | **455** |
| | 1,285 | **1,292** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level.

## 8 · Not done, named rather than skipped

- **Nothing levels a character up**, so `powersKnownAt`'s second half has no
  caller — stated in the function rather than left for somebody to discover.
- **The nine-reply ceiling is measured at one viewport.** A much smaller window
  would fit fewer, and nothing re-measures at runtime; the digit ceiling is the
  half that holds everywhere.
- **`recommend_order`** stays parked, as instructed.
