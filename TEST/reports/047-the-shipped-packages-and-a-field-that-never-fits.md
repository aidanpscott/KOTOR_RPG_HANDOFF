# TEST 047 — the shipped packages, a field that never fits, and one problem that is real

**Built against:** the **same two binaries as TEST 043–046.** App bundle
`kernel_blob.bin` built **16:11**, from `660134a` → Lodestar `9aa7382`
(`grep -c "PT-1626"` → **0**). Loom bundle built **16:39**, from `908a412`.
**Neither rebuilt.** `47789fa` / `776e42e` / Lodestar `e1a837c` remain untested by me.

**Instrument:** PID-scoped, and ⚠ **it caught something this run.** My first Loom
launch failed on a `cd` and `pgrep -n -f "bundle/loom"` handed me **Coder's** newest
process instead of mine. I noticed because the PID had no parent I owned, relaunched
with `$!` and `pgrep -P`, and drove `549811`/`550452`/`551223`/`552452` — all mine, all
killed by PID. Coder's `517968` survived every one. **`pgrep -n` is not PID-scoping;
it is the same class of mistake as `pkill -f` and I nearly repeated it.**

⚠ **I wrote nothing to any package this run.** `endar-spire` and `base-rules` were
md5-summed before and after (40 files, `diff` empty); `taris-undercity` was read only
and its files still date from Sep 7; my own bed is byte-identical to `PKG-T046`; the
save shelf is unchanged because nothing was played.

---

## 1. The shipped packages, on all seventeen members

### `endar-spire` — **No problems found.**

⚠ **It has never been re-verified since the position family, the two blueprint
members and `referenceMissing` landed**, and `TEST 026` found a fault in it once —
the orphaned conversation owner, `.07` against an area holding only `.39`. `PT-1607`
closed that by removing the field. **Verified now against the full seventeen: clean.**

Two areas (`a01-command-deck` entry, `a02-starboard-hold`), one conversation
(`trooper-challenge`), and **not one area drawn in the fault colour**.

### `base-rules` — **No problems found.**

`PT-1380` makes a rules-only package with no `[entry]` legitimate, and `validateEntry`
returns early when `areaOrder` is empty — *"a rules-only or asset-only package is
legitimate and has nowhere to begin BY DESIGN."* **It has now met the position family
and the position family had nothing to say**, which is the correct outcome rather than
a silent one: with no areas there is nothing for `_position` to be called on.

⚠ **A difference worth naming, because it is the affordance and not a defect.** A
package with faults shows a **count** in the header — *"Tester Probe · 11 problems"*.
A clean one shows a **`verify` control** instead, and pressing it gives a dialog:
*"VERIFY / Endar Spire / No problems found."* with **Verify again** and **Close**. A
tester who only ever opens faulted packages never sees that half of the UI. I had not.

### ⚠⚠ `taris-undercity` — **1 problem, and it is real**

Beyond the brief, and it is the one that found something. Not a fixture: authors
`aidanpscott, a second author`, version 0.2.0.

    a01-sewer-junction   entry
    "a01-sewer-junction" declares no connections, so a character who walks into
    it from another area can never leave.

**The fault is correct.** Both area files are three-line stubs — name, size,
`default = "floor"` — with **no arrivals, no connections and no contents at all**:

    [area]
    name    = "Sewer Junction"
    size    = [14, 10]
    [tiles]
    default = "floor"

So a new game begins in a 14×10 empty room with no exit, and **`a02-rakghoul-warren`
can never be reached at all.** The package's own summary says *"two rooms… to give the
library a second tile"*, so this may be a deliberate stub — **but it is what a player
gets, and the validator is right to say so.** ⚠ It is the same family as the a03/a04
one-way rooms I filed in my own bed, in a package that is not mine.

⚠ **Two observations on the fault, not defects I am filing:**

1. **`areaHasNoWayOut` has one sentence for two situations, and this is the wrong one.**
   *"a character who walks into it from another area"* — nothing connects to
   `a01-sewer-junction`; you **start** there. The conclusion is right and the premise
   named is impossible for an entry area.
2. **There is an `areaHasNoWayOut` and no `areaHasNoWayIn`.** `a02` is not flagged, and
   the source says exactly why (`package_validate.dart:260`): `enterable` is the entry
   plus every connection target, and *"an area nothing leads to cannot be walked into,
   so saying it has no way out would be a sentence that is false about it."* **That
   reasoning is sound and it leaves a gap**: a declared area that nothing leads to is
   reported by nothing. `taris-undercity` has one and its count is 1, not 2.

---

## 2. The truncated ages: **the field is fixed and the value never fits**

Measured at **four** window sizes, same shelf, same rows:

| window | panel | `Blade Tester` age |
|---|---|---|
| 900 × 600 | scaled down | `19 ho…` |
| **1280 × 720** (our target) | design size | `19 ho…` |
| 1918 × 800 | **did not grow** | `19 ho…` |
| 1900 × 1000 | **did not grow** | `19 ho…` |

⚠ **Identical clip, character for character, at every size.** Widening does not help
because the panel does not grow with the window; narrowing scales the whole design
down so the same characters are lost. **This is not a layout that fails at our target
size — the field is fixed and the value never fits at any size.** That is the answer to
which fix it needs.

The row is `package_main_menu.dart:452–472`:

    Row(children: [
      Expanded(  child: Text(e.character ?? e.handle, … ellipsis …)),
      SizedBox(width: M.gap * s),
      Flexible(  child: Text(_saveDetail(e),          … ellipsis …)),
    ])

⚠ **The name is `Expanded` and the detail is `Flexible`, both at the default flex.**
`Expanded` is a *tight* fit and `Flexible` a *loose* one, so a short name like
*"Yard Tester"* still claims its full share and **the long string is always the one
that yields.** The comment above it says the name *"is the half that must survive a
narrow column"* — that intent is met, and the cost is that the other half never
survives at all.

**What is lost is the unit, which is the part that carries the meaning.** `19 ho…` is
readable; `14…` — Barrier Tester, measured in TEST 046 — could be minutes, hours or
days. ⚠ **The value is correct** (TEST 046 proved `savedAt` right to the minute against
five saves) **and unreadable**, and it is the field a player uses to answer *"which one
was I just in."*

---

## 3. `SaveEntry.area` has exactly one reader, and it is the display

My own negative, followed. Every consumer of the header's `area`, whole codebase:

    package_main_menu.dart:507   if (e.area != null) e.area!,      ← the Load Game row
    save_file.dart:171           recomputing the header's byte length
    save_listing.dart:110        the constructor

**That is all.** `main.dart:298`'s `resume?.area` is a different `.area` — the
`Position` that `projectPlayState` folds out of **the ledger** — and it is what
Continue and Load actually use.

⚠ **Every other header field earns its place and `area` does not.**

| field | consumer | earns it? |
|---|---|---|
| `package` | `listFor` filters on it, falling back to `replay(readSave(…))` per save | ⚠ **yes** — this is `PT-1518`'s stated reason: not replaying every save |
| `savedAt` | `_newestFirst`, which orders **both** Load Game and Continue | **yes** |
| `character`, `className`, `level` | the row's "who" — and all three are `replay(log)` projections, so they cannot drift | display-only, but **cannot be wrong** |
| **`area`** | **the row's "where", and nothing else** | ⚠ **no** |

⚠⚠ **`area` is the only header field that is BOTH display-only AND not ledger-derived
at write time** — `main.dart:191` takes level, character and class from `replay(log)`,
while `area` is a caller-supplied parameter that TEST 046 showed is frozen at the
session's starting area. **It exists to be displayed, and it is the one that can be
displayed wrongly.** Deleting it would cost the row its third field and nothing else.

---

## What I did not check

- `47789fa` / `776e42e` / Lodestar `e1a837c`. Not in either bundle. Untested.
- **Whether `Verify again` differs from the first run.** I pressed `verify` once per
  package.
- Whether `taris-undercity` is *meant* to be a stub. I report what the validator says
  and what the files contain; the intent is the owner's to state.
- Whether the row would fit at a **smaller font** or with a shorter area id — I changed
  only the window.
- I did not re-verify `tester-probe` this run beyond TEST 046's 11; nothing in it moved.

## State

- **Nothing was written this run.** `endar-spire` + `base-rules`: 40 files md5-summed
  before and after, `diff` empty. `taris-undercity`: read only, files still Sep 7 13:02.
  `tester-probe`: byte-identical to `PKG-T046`. Save shelf: `diff -rq` clean against
  `SV-T042` — nothing was played.
- ⚠ `tester-probe` still reports **11 problems and most of them are mine on purpose**;
  `a07-probe-pinch` and `package.toml` say so in the package itself.
- The NWN install was not read or written.
- My four processes killed by PID; Coder's `517968` survived all of them.
