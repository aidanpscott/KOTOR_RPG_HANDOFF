# 16 · Ledger batch 2 — to disk and back

**`Lodestar` `d3a46f` · `KOTOR-RPG-APP` `244fce8`.** 173 app tests, 109
Lodestar tests, analyze clean.

---

## ⚠ `PT-1265`'s guarantee, run for the first time

> *"Replay of a log is bit-identical, always."*

Four assertions, on a synthetic log and on a real one:

| | |
|---|---|
| **event for event** | kind, step and payload, every event |
| **SHA-256 on the bytes** | re-writing the loaded log gives **byte-for-byte the same file** |
| **replay of both** | the two records compared **field by field**, every key |
| **twice is the same** | writing one log twice gives identical bytes — Dart's `gzip` writes no timestamp, so a save is reproducible and a diff of two saves means something |

**A real chargen log: 26 events, 759 bytes on disk.**

---

## ⚠ The header was already half-built, and I did not notice until I looked

**`save_listing.dart` already READ `§2`'s four fields and had no writer.**

    "KRSV"            magic, 4 bytes
    u16               format version
    u16 len + utf8    compressor
    u16 len + utf8    rules version

So the format was not invented here — it was **completed**. And `readSave` goes
**through `listSaves`**, so one reader decides what a header means and there is
no second opinion to drift from. Its `SaveProblem` reasons are the ones a
damaged save produces.

**The magic is first**, so `head -c 4` and `file` both identify it — which is
`PT-1329`'s whole point: *"`SAVEGAME.sav` opens with the `MOD` signature… the
name was never the format."*

---

## ⚠ The compressor is `gzip`, and that is the fallback — said, not assumed

`PT-1328` recommended **zstd-10** with gzip as fallback, and measured the gap
at **0.09 MB on a 16.3 MB log**.

**Dart ships `gzip` in `dart:io`. It ships no `zstd`** — every `zstd` on pub is
an FFI binding to a native library, which is a build dependency on three
desktop targets and two mobile ones. **For 0.09 MB, that is the wrong trade,
and the brief said to take gzip and say so.**

> **⚠ AND THE CHOICE STAYS REVERSIBLE BECAUSE IT IS IN THE FILE.** `§2`:
> *"recording which one was used means switching later does not orphan
> existing saves. Without it, the choice is permanent by accident."*
> **A save packed with a method this build does not know refuses and says so** —
> tested, by rewriting the compressor field in place. That is the field doing
> its job rather than decorating the header.

`none` is also implemented, so **the field is exercised by more than one
value**. A field with one possible value is a field nobody has tested.

### Measured, not quoted

**120,000 events: 11.3 MB raw → 0.34 MB gzip, 32.8×.**

`PT-1328` measured 11.6× for gzip-6 on its own 120,000-event log. **This is a
different log** — more repetitive, being synthetic chargen events — so the test
asserts the **order** and not the number.

---

## The payload is one JSON object per line

The shape of an **append-only** log, rather than a container that has to be
rewritten to grow. It also compresses the way `§2` predicts: the same handful
of kinds and keys, thousands of times over.

**⚠ Absent, not zeroed, on the wire too:** an event that belongs to no step —
`character.created` and the pre-hub's three — carries **no `step` key at all**.

---

## Where it goes, and what it is called

`Locations(root).saves`, from `PT-1382`. The extension is **`.sav`**,
`PT-1329`. **The caller does the disk** — `ENGINE-INTERFACE-01 §4` — so
`writeSave` returns bytes and `readSave` takes them, exactly as
`save_listing.dart` already said.

**⚠ Mobile returns null by design**, and a save path is the second thing
through that door: Android and iOS have no shared location, so the app supplies
its own root. The first thing through was packages.

---

## ⚠ THE THING TO REPORT RATHER THAN SOLVE — what a save is named, and how many

**`SAVE-LOAD-01 §5a` settles WHERE. Nothing settles HOW MANY, or what one is
called.** And `save_listing.dart` already carries the sharp end of it, in a
comment written before this batch:

> *"⚠ Deliberately absent: a 'latest' or 'most recent' save. `Continue` wants
> one, and this cannot honestly supply it. `SAVE-LOAD-01` gives a save header
> four fields and **none of them is a time, a name, a character or a
> package**. Ordering by file mtime would be the caller's filesystem guessing
> at a fact the format does not record."*

**So the header is the constraint, and it is a small one.** Three questions,
none of them mine:

| | |
|---|---|
| **One save per character, or many?** | A log is append-only, so *"save"* may mean *flush the log I already have* — one file per character, rewritten. Or it may mean a **slot**, in which case a character has many files and they share a log prefix |
| **What names the file?** | The character's name is a player's free text and is not unique. A uuid is unique and unreadable. `PACKAGE-NAMING-01` answers this shape for packages and nothing answers it here |
| **What does `Continue` order by?** | With no time in the header, either the header gains a field or `Continue` orders by something the format does not record |

**⚠ `§6` already leans one way without deciding:** *"a save that is **a log**
may want showing differently from a save that is a slot."* **That is the same
question, and answering it decides all three.**

---

## What was NOT built

**No `Continue`, no `Load Game`, no snapshots.** Batch 3 lights the two
buttons; snapshot granularity is open in `§6` and a snapshot is **a cache**
(`PT-1327`) — delete every one and lose nothing.

**No validation.** `CHARACTER-RECORD-01 §4` gives thirteen legality rules and
loading checks none of them. `§5`'s load sequence is five steps and this
implements **step 3 only** — replay. Steps 1 (resolve packages), 2 (snapshots),
4 (validate) and 5 (open) are not built.

**The rules version is carried and not yet acted on.** `§5` discards snapshots
when it moves; there are no snapshots. **A log knows what it was played under
and nothing asks it yet.**
