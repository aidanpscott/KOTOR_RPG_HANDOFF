# BUILD 115 — the race shipped, and the read that wrote

`PT-1654` and `PT-1657` built. `PT-1656` recorded.

---

## 1 · ⚠⚠ `PT-1654` — THE RACE FIX IS SHIPPED, AND SO IS ITS GUARD

One line: `_log` is extended **before** the await, not after. Measured on
`whole_loop_test`'s own fixture:

    before   32 events · 1 character.moved · Continue resumes 0,0
    after    33 events · 2 character.moved · Continue resumes 5,4

**`5,4` is where the character actually was.** The old ordering was silently
breaking `PT-1523` — *"Continue put every character back at the package's front
door"* — **on every save since it shipped.**

### ⚠⚠ AND THE FIRST GUARD I WROTE DID NOT BITE

I asserted the surviving events inside `whole_loop_test`, **reverted the fix,
and the case still passed.** Once the walker stopped bumping into things, that
fixture's two appends no longer overlap and the race has nothing to lose there.

> **A test that cannot fail on the defect it names is worse than none.**

So the ordering moved into `SessionLog`, where a write can be made slow on
purpose, and `session_log_test` holds it. **Verified by inverting the ordering
inside the class: three of its four cases fail, and all four pass when it is put
back.** The `whole_loop` assertion stays, labelled as documentation rather than
a guard — saying which is the point.

⚠ **AND THE SNAPSHOT IS TAKEN AFTER THE APPEND**, so a write that starts late
carries MORE than one that started early, never less. **The last write to finish
is a superset of every earlier one**, which is what makes overlapping writes
safe rather than merely likely to work. `session_log_test` asserts no write ever
shrank.

### The walker, landed in the same commit

`_step`'s own guard: *"a conversation takes the keyboard."* Resuming at `5,4`
puts the player beside the trooper, the walker's blind press opened a
conversation, and **fifty-eight further arrows drove the dialogue highlight.**

Two changes: the walker closes any open conversation — **found by widget type,
not by text**, because what is on screen during a beat is the author's prose —
and its blind press **rotates through four directions** rather than repeating
one, because `_said` is cleared only by a step that SUCCEEDS, so pressing the
same direction forever means bumping the same thing forever.

## 2 · ⚠⚠ `PT-1657` — AND THE DEFECT WAS THE WRITE, NOT THE TIMESTAMP

`Tester`: **merely inspecting the oldest save made it the one `Continue`
resumes.** Opening a save enters its area, arriving is a move (`PT-1523`), the
move is appended, and appending rewrites the file with `savedAt` set to now.
A READ reordered the shelf.

The owner asked what `savedAt` should be for an upgraded format-1 save. **It
should be what it already is**, and here is why none of the three options is the
answer:

* **Leave it null** — `_newestFirst` sorts unknown last, so this would work, and
  it makes the field say *"nobody knows when this was written"* about a file
  written thirty milliseconds ago. **A lie that corrects a caller.**
* **Derive it from the log** — `CharacterEvent` carries no time. There is
  nothing to derive from, which is why format 1 had no stamp in the first place.
* **Stamp the upgrade honestly as a play event** — that is what it was already
  doing. `savedAt` means *when this file was written* and it was telling the
  truth.

⚠⚠ **WHAT WAS FALSE WAS THAT THE FILE NEEDED WRITING.** The arrival it recorded
was a **duplicate**: resuming puts `_at` at the square the projection had just
read OUT of the log. `PT-1421` is *one crossing, one event* — and nothing
crossed. `_writePosition` now returns nothing when the log's last move already
says this subject is on this square in this area.

⚠ **AND THE FORMAT-1 UPGRADE IS NOT THE DEFECT EITHER.** Every field it writes
is correct. It only looked like the culprit because that save's jump is the
loudest: no stamp at all sorts LAST, and an invented one sorts FIRST.

⚠ **A RESUMED SQUARE THAT IS NO LONGER STANDABLE STILL WRITES**, because
`_enter`'s fallback genuinely moved the character.

**Asserted at the byte level** — not *"the timestamp is close enough"* but
**the file was not touched at all** — with a control that walks three squares
and demands the file DOES change. ⚠ The first version of that control only
pressed escape and failed, correctly, because nothing had moved: **a control
that fails for the reason the fix exists is not a control.**

## 3 · ⚠ `PT-1656` — RECORDED, NOT BUILT

`§4`'s cap on a skill depends on a **derived** aptitude and the derivation does
not exist, so `validateRecord` returns *not checked*. **Three saves on the shelf
sit at rank 3 — exactly the value that derivation would adjudicate — and nobody
can say whether they are legal.**

⚠ It is not *"a rule that is unenforced"*. It is **a rule with named subjects
already in the data**, which is a different and sharper thing. `CHARACTER-RECORD-01 §3`
territory and a larger piece of work; in `STATE.md`.

---

## Tests

`Lodestar` 490 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` 398 — **1,139, green.**
Pins 4/4. Gate: 2 advisory warnings, both pre-existing.
