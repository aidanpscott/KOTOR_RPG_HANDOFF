# 46 · Three slices — the droid loads, the wire is connected, `PT-1459`

**632 green** — Lodestar 293 · Lens 4 · Loom 114 · app 221.
`Lodestar 3a24455` · `Loom 3249dde` · `app 4eb7d28`.

---

## 1 · ⚠⚠ The droid was already fixed and the app was not running the fix

**`PT-1458` shipped in `Lodestar 4b3a482` last slice. The app's `pubspec.lock`
stayed pinned to `78782b6`, the commit before it** — so `t3-k9.sav` went on
being refused by a build that contained the fix nowhere.

> **`BUILD/37` wrote this down and it still caught me:** *"the front-ends
> consume `Lodestar` and `Lens` FROM GITHUB, not from the sibling folder."*
> **I pushed the engine and the app in the same act without re-resolving in
> between**, and nothing in the app's suite touched `validateRecord`, so
> nothing could fail. `Loom` was two commits behind as well.

**The guard is the fix.** `droid_loads_test` asserts **the resolved engine**
accepts a Remote — not that the source does.

**⚠ And my first control was invalid.** Editing `pubspec.lock` alone left the
test passing, because `package_config.json` had not been regenerated. **With a
real `pub get` it fails with exactly `STR is 6, outside 8 to 18`** and passes
again when restored. **A control that does not change what runs is not a
control.**

**Verified on the artifact through the app's OWN assembled facts**, not a
hand-made set: `T3-K9` validates **legal**.

---

## 2 · ⚠⚠ The answer was authored and then orphaned

**`droid_arrays.toml` has shipped in `base-rules` since the extraction** — nine
rows of `weapon · consumable · repair`, exactly the droid kit per class — and
**no reader in the app, the engine or Loom ever opened it.** Its only
references anywhere are the generation scripts that write it.

**And the screen could not have branched if it had wanted to.**
`EquipmentScreen` received `className` and **no species and no chassis at
all.** Some steps were wired; the rest were never told what they were building.

**⚠ THE BOOTS WERE A HARDCODED ROW, NOT DATA** — which is why *Dockworker's
Treads* reached a chassis that *"hovers, ignores difficult terrain, and makes
no footfalls."* They belong to the organic assortment and are not in the droid
table. **Nothing here rules on hovering: the droid kit simply does not contain
them.**

A droid renders `weapon · consumable · repair`. **The two tables have different
SLOTS, not different values in the same slots** — rendering the organic four
with two blank would say the slots exist and are empty, which is a different
claim.

**⚠ And null is the honest answer for the other ten classes.** Nine droid
arrays against nineteen class arrays; a droid in a class with no droid row has
no array, and the screen already says so. **Falling back to the organic row is
what put boots on a hoverer**, and the test asserts it does not.

### ⚠ The Feats half is a STOP, and it is one row further down

`FeatsScreen` has the same missing wire — **and wiring it changes nothing.**
`feats.toml` says *"Granted at 1st level to every droid"* in `description` and
carries `availability = "selectable"`; the fields are
`id · name · chain · is_chain_head · section · description · effect ·
availability` and **none of them says who may take a feat.**

> **Filtering on prose is `TRACE-83` again. The screen has nothing to ask.**

**Not wired, because a parameter nothing can use is building ahead.** The need
is a **feat eligibility field**, and that is a format ruling.

---

## 3 · `PT-1459` — two format fixes

### ⚠ A dead check is refused

The bracket's colour comes from the **reply's** gate; the roll happens over the
chosen player line's **own `then`**. With none, `_pick` returns null **before
any dice are touched** — `resolve()` is never called. **`§4c`'s amber means a
real check, so the colour lies**, and `PT-1307` derives the bracket precisely
*"so nothing an author typed can disagree with what rolls."*

**Refused, not reported** — `PT-1379`'s precedent. Run against the bed it names
the Persuade option **and only that one**: teal and the price are not checks,
so **only the colour that promises a roll is flagged.**

**⚠ An ungated dead end is NOT a problem.** Absent `then` means the
conversation ends, and `Stand aside.` and `My mistake.` are correct content.

### ⚠ The end of a conversation is not an empty line

The runtime manufactured `NpcLine(id: '', say: '')` — **exactly the shape
`PT-1433` refuses from an author.** A reader that rejects a value must not
fabricate it. `Beat.line` is now null and `Beat.ended` says so explicitly.

**And it cost something:** the app tested `line.id.isEmpty` to notice, **so it
knew and said nothing.** It says *"the conversation is over"* now.

### ⚠⚠ And the rule makes the bed's own conversation invalid

**Loom authors a dead check.** `conversation_author_test` asserted
`problems is empty`; it now asserts **the one known problem by name**, so it
cannot grow quietly.

> **The fix is authoring, not code, and not mine to invent.** What a successful
> Persuade *leads to* is content. **Loosening the assertion or inventing a
> continuation would both have hidden it.**

**This is the one thing in the slice that is owed a decision.**
