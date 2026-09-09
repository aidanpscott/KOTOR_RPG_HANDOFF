# BUILD 70 — `PT-1501`/`PT-1505`: every authored check in this project was free

**728 green** — Lodestar 326 · Lens 5 · Loom 123 · app 274.

---

## ⚠⚠ The owner's finding, and the runtime was not the thing that was wrong

Twelve passes out of twelve at a nominal **55%**. The reply was drawn in amber,
the player picked it, and **nothing rolled.**

### How you tell a visibility gate from a skill gate — **BY POSITION**

The distinction `PT-1432` drew is **already in the runtime** and did not need
inventing:

    a gate on a `replies` link    COLOURS   — §4c's amber; the reply is shown
    a gate on a `then` link       ROLLS     — `Verdict.isACheck`, `_pick`

`Verdict.isACheck` exists for exactly this and its own doc says a check
*"resolves when the player commits to it"*. **Committing is the outbound link.**
A `replies` list SHOWS ALL and brackets each entry; a `then` list PICKS ONE and
is where dice are touched. So there was nothing to add to the engine.

### ⚠⚠ THE AUTHORING WAS WRONG — AND SO WAS MY OWN RULE

`PT-1459` asked only whether a gated reply **had a `then` at all**. It does not
help. `_pick` returns on the **first ungated link** —

    if (l.gate == null) return l.to;

— so a `then` carrying one bare link never rolls either. **That is the common
case, and it is the shape of every conversation anyone has authored**, the
shipped bed included. My rule was one condition short and the missing condition
was every real instance.

⚠ **A rule that fires on nothing real is a rule nobody has tested.** It passed
for four slices because the only thing it could catch was a shape no author
produces.

### The fix is the roll, not a line

`§9` is a worked example of **the bed's own file, by name**, and it settles it:

```toml
then = [
  { to = "stands-down", gate = { skill = "persuade", dc = 14 } },
  "not-on-my-board",
]
```

⚠ **THE GATE IS WRITTEN TWICE AND THAT IS NOT DUPLICATION.** On the reply it
colours; on the way out it rolls. Flattening them into one is exactly what
`PT-1432` warned against.

⚠ **AND THE ORDER OF THE OUTBOUND LINKS IS MEANING.** The gated link first, the
failure second — reversed, `_pick` falls through and the check never happens.

---

## What the extended rule found

Both shipped conversations, refused **by name**:

    endar-spire/trooper-challenge   you-are-one    — fixed, §9's form
    ⚠ tester-probe/sentinel-challenge  stand-down-i — NOT MINE. See the NEED.

## ⚠⚠ AND THE BUILDER COULD NOT REPAIR WHAT IT WROTE — the other half of `PT-1379`

`PT-1379` stopped Loom **creating** a fault the validator detects. Fixing the
bed found the sibling: `ConversationDraft.link` **only ever appended**. There
was no `unlink`. The bare `then` that `author_bed_answers` wrote — correct
under `PT-1459`, wrong under `§9` — **could be added to and never corrected.**

> **A tool that can only add is a tool whose early mistakes are permanent.**

`unlink` is `unlink`, not `setGate`, **because order is meaning**: removing and
re-adding puts the author in charge of which link `_pick` reaches first.

The bed was then re-authored **through Loom's own draft and writer**
(`tool/author_bed_persuade.dart`), which refuses to write what `validate`
refuses. **Content from `§9`, not invented here.** The diff is four lines.

## ⚠ `PT-1502` — travel keeps the previous area's tile size (Lens)

`_fitFor` cached the **view** `Size`; `_fitted` divides that view by
`area.width + 2`. **Travel changes the room and not the window**, so the cache
key could not see the only thing that had changed. A 10×8 area was drawn at a
6×5 tile. The key is `(view, room)`; a room change also clears `_zoomed`,
because a zoom is a choice about the board you were looking at.

⚠ **The test read from disk inside `testWidgets` and reported "did not
complete" rather than failing** — which is the shape that made it look like a
hang. Wrapped in `tester.runAsync`. Control: with `_fitForArea` out of the key
the case fails.

---

## ⚠⚠ `PT-1506` — AND THEN THE ROLL HAPPENED IN SILENCE

Making it roll surfaced the reason it was ever findable only by counting.
`_pick` called `resolve`, read `succeeded`, and **threw the derivation away.**

> **A check that rolls and records nothing is indistinguishable from a check
> that does not roll.**

⚠ **`check.resolved` has been declared `transient` in `EVENT-KINDS-01` since
`PT-1418` — carrying the sentence *"carries its whole derivation"* — and
NOTHING IN THIS PROJECT EMITTED IT.** `PT-1418` found fourteen emitted kinds
undeclared; this is the mirror of that, and it sat for six slices.

The event names every modifier, keeps the raw die beside the total, and records
the link it was rolling **for** — and it is written **whether it passed or
failed**, because a failed check is the one a player is most owed.

⚠ **All three `_pick` sites record, not the one the bug was found in.** In
`_beat` the pick had to be lifted out of the `Beat` constructor: evaluated
inline it runs after the event list is copied and the event is dropped
**silently**.

The play screen says it — **verdict first**, `BUILD 69`'s rule, because that
row can wrap or be cut. And it now survives the end of the conversation: a
failed check that closes the panel used to be overwritten by *"the
conversation is over"*.

### ⚠ And the app test was asserting a die

`dialogue_screen_test` asserted *the trooper stands aside*, **full stop** — and
it was green twelve times out of twelve for the same reason the owner's play
was. It now asserts what must hold either way: the approach is **answered**,
and the roll is **said**, with its derivation. **The verdict is not pinned.**

---

## ⚠⚠ A FINDING AGAINST `§9` ITSELF — I DID NOT COPY IT WHOLE

`§9`'s failure node is not terminal:

```toml
[[npc]]
id      = "not-on-my-board"
say     = "My board says otherwise. Last warning."
replies = ["back-off", "push"]
```

**It re-offers `push`.** A failed Persuade returns the player to the same check
with nothing spent, so **the check is passed eventually, always** — which is
`PT-1501`'s defect reached by a longer road. The example is demonstrating `§7`
re-entrancy and the retry is, I think, incidental to that.

⚠ **So the bed's failure node is TERMINAL, and that is a deliberate divergence
from the document, reported rather than taken.** Whether a failed check may be
retried is a rule, and it is the owner's.

---

## ⚠ THE NEED — `tester-probe/sentinel-challenge`

    halt-this-room → stand-down-i   Persuade DC 14, and `then = ["rank-means-nothing"]`

**It cannot be wired to §9's form without a failure node, and that is CONTENT.**
Where a failed Persuade against the sentinel lands is the owner's choice, and
**`tester-probe` is Tester's package** — not mine to author. Until it has one,
that conversation is refused by `validate` and Loom will not write it.

## ⚠ A CITATION COLLISION, CORRECTED — and two records outside my reach

I filed this slice's two findings as `PT-1503` and `PT-1504`. **The index had
already spent both on the previous slice** — `PT-1503` is *"`PT-1499` was built
and Tester was still right"* and `PT-1504` is *"the fourth instance was beside
the third"*. Renumbered to **`PT-1505`** (the dead check `PT-1459` could not
see; `unlink`) and **`PT-1506`** (the roll that recorded nothing; `§9`'s retry)
everywhere I write.

⚠ **Two records cannot be corrected and are recorded instead:**

    Lodestar 0913ce0   its commit message says PT-1503
    ⚠ TEST 017         cites `0913ce0 (PT-1503)` — Tester's file, not mine

**A wrong PT number points a reader at the wrong ruling, which is worse than
none.** The lesson is that I was minting numbers ahead of the index rather than
reading it.

## Still open

- ⚠ **`PT-1500` — the palette.** Ruled and unstarted.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 48 annotation cells.
- ⚠ The editor has **no button for `unlink`** — the verb exists on the draft
  and only a tool calls it. A conversation authored by clicking still cannot be
  corrected by clicking.
