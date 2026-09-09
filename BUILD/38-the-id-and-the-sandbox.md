# 38 · `PT-1445`, and the suite stops writing to real data

**206 of 206 app tests pass** — and the app repository is **clean for the first
time in three sessions.** Lodestar 270 · Lens 4 · Loom 111 untouched.

---

## 1 · ⚠⚠ The four tests were right. One line of `hub.dart` was wrong

**The ruling is followed exactly. The fix was not where the ruling said it
would be**, and that is worth writing down rather than quietly correcting.

`hub.dart` has **two independent paths to one record**, which is what makes the
acceptance a test rather than a tautology:

| | path | was |
|---|---|---|
| the log | `LedgerWriter.preHub(…, package: widget.packageId)` | ✓ **already the id** |
| the record | `recordFromChoices` → `package: widget.packageName` | ⚠ **still the name** |

`mustMatch` compares `replay(log).asMap` against `recordFromChoices.asMap`
field by field. **It reported that the two paths disagreed on `package`, and
they did.** The previous session moved one path to the id and left the other.

### ⚠ And the asymmetry decides which one moves

**`replay()` reads `package` straight out of the payload.** It has no package
list and cannot map an id back to a name. **So a projection carrying the
display string could never be reproduced from the log** — the record had to
move, and the log could not have.

**`record.package` is an identity, not something a player reads.** Its only
consumer in the whole app is `SaveStore.listFor`. Checked before changing it:
nothing renders it.

> **One line changed. Zero test edits. All four pass.**

**⚠ The tests were the thing that caught it**, and they caught it precisely
because the acceptance was built as two independent paths. **A test that had
asserted on the log alone would have passed.**

---

## 2 · The migration allowance, and when it can go

`PT-1445` keeps `SaveStore.listFor`'s both-ways read and asks when it retires.
**It is now written in the file, and it is checkable rather than a feeling:**

> **When no save remains whose `package` is not an id in the library.**

**Nothing new can create one.** The single writer is `LedgerWriter.preHub` and
it is given `packageId`. The allowance **reads both and writes one**.

**⚠ And deleting it fails loudly**, which is why it is safe to leave: an old
save stops being listed by its own package. Keep it until someone has looked in
the folder, not until it merely feels old.

---

## 3 · ⚠⚠ The suite no longer writes into the owner's data

**`flutter test` was rewriting `~/.local/share/kotor-rpg/saves/kaeda-vos.sav`
and `console/first-run.json` on every run.** Same bytes — `PT-1265`'s guarantee
held and nothing was ever corrupted — **but it is the owner's save directory,
and a second agent running suites repeatedly makes it a live hazard.**

### ⚠ The split is READ versus WRITE, not real versus temp

**Pointing all 19 files at a temp directory is the shape that let three defects
through.** `PT-1382`'s vendor-scoping, `PT-1425`'s throwaway package and
`PT-1417`'s save acceptance **all passed against a temp fixture and failed on
the real folder.** Reading the real shelf is the property that catches those.

| | | |
|---|---|---|
| **READS of the real shelf** | **all kept** | 2,533 generated records no fixture reproduces. These tests **genuinely need the real path** |
| **WRITES** | **redirected** | These only ever needed **a** path and took the nearest one |

`sandboxed()` returns a `Locations` whose **`packages` is a symlink to the real
shelf** and whose **`saves` and `console` are a fresh temp root.** `Locations`
already splits a root into exactly those, **so no engine change was needed** —
it is the same `Locations(dir)` constructor `save_round_trip_test` has used
since batch 2, with the read half pointed back at the shelf.

### ⚠ My own count was wrong, and a scoped negative is why

**I reported "19 test files write to the real folder." The true statement is 19
READ and 6 WRITE.**

The first measurement snapshotted **content hashes** and reported everything
clean — because the rewrite is byte-identical. Re-run on **mtimes** it found
two writers. **But that pass covered only five files**, so it missed four more
calling `FirstRun.markSeen()`. A grep for the writing call found those.

> **⚠ Two mis-scoped negatives in one slice — the wrong signal, then the wrong
> file set.** Both were mine, both were caught by widening rather than by
> luck, and the second is exactly the failure the standing rule names.

**`import_test` and `save_round_trip_test` already used a temp root** and were
left alone. `save_round_trip_test` is where the pattern came from.

### ⚠ And the control against passing by accident

**A sandbox that silently pointed at an empty directory would let these tests
pass while testing nothing.** So the shelf link was deliberately pointed at a
nonexistent path:

    broken link   → acceptance_test and base_rules_test FAIL
    restored      → both pass

**The real-shelf coupling is still there and still load-bearing.** The sandbox
does not hide it.

**Result: 206/206, and the live data folder is untouched by the entire suite**,
verified by an mtime snapshot taken around the whole run.

---

## 4 · The ten uncommitted files — committed, and why

**They should be, and they are.** The tree is clean.

- **The thing blocking them was a ruling, and `PT-1445` made it.** They were
  not unfinished; they were undecided.
- **206/206 pass.** They were red only because of the one line in §1.
- **They were the only thing in the tree not on GitHub**, in a tree that now
  lives under a Steam folder that a verify can wipe.
- **⚠ A second agent is coming.** Ten uncommitted files in a tree someone else
  is about to work in is a trap — they cannot tell adopted work from their own.

Split into **two commits**, because they are two concerns and one of them may
want reverting alone: `7625f3d` the test isolation, `3d97d52` the ruling and
`PT-1443`'s save work. `base_rules_test` carried a hunk of each and was split
between them.

---

## 5 · What `PT-1443` closes with this

Saves are **filtered by package**; `Continue` and `New Game` are **gated on a
package having an `[entry]` area**, with the reason said on screen — `base-rules`
is legitimately area-less per `PT-1380`; **`Back` after the hub no longer walks
into a game that saves nothing**; and Select Premade reads **Select Premade
Character**.

**⚠ Still open from `PT-1443`, and untouched here:** the side panel, click-to-move
with the key bindings and settings surface it needs, and Baldur's Gate 3 as a
fourth source. **All three are design, not correctness.**
