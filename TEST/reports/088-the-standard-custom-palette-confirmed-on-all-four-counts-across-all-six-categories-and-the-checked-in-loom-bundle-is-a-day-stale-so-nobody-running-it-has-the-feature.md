# TEST 088 — THE STANDARD/CUSTOM PALETTE IS RIGHT ON ALL FOUR COUNTS, and on
# every category rather than one: fifty on the Standard side, one tap copies a
# byte-identical `.item` into the open package, the second tap refuses, and the
# refusal is spelling-blind — my pre-existing EDITED `.toml` at a standard
# path survived untouched. Custom shows only my own and updates with no restart.
# ⚠⚠ BUT THE CHECKED-IN LOOM BUNDLE IS A DAY STALE — it predates both palette
# commits, so anyone launching Loom from the tree today has none of this. I had
# to rebuild the Dart side before I could test anything.
# ⚠ And the problem count does not refresh after a copy: copying in the very
# blueprint a problem names leaves the count unchanged until you re-verify.

## Build state

    Loom            HEAD 61718e0  Re-pin lodestar after PT-2059's catalogue field
    KOTOR-RPG-APP   HEAD 12e5309  PT-2059: the catalogue join
    lodestar        4901ab97 — ⚠ LOCK, PUBSPEC AND THE PUB-CACHE CHECKOUT ALL
                    AGREE, in both repos. `ref: main` floats but has not drifted.

Both trees clean. `check_shelf.py` green at the start **and** at the end:

    ✓ 25 rules files and 50 standard blueprints, all identical to what the
      extracts generate

**The gate already covers the new artefact** — it now counts the fifty
blueprints beside the twenty-five rules files, so a standard blueprint drifting
from its base type is caught the same way everything else on the shelf is. That
is the check I would otherwise have had to invent, and it was already there.

---

## ⚠⚠ FIRST, THE THING THAT NEARLY MADE THIS REPORT WORTHLESS

`Loom/build/linux/x64/debug/bundle/.../kernel_blob.bin` is stamped
**`2026-09-13 16:15:48`**. The two palette commits are
`0e5141f` (**2026-09-14 09:22**) and `5ebe0a1` (**09:27**).

**The bundle in the tree is roughly a day older than the feature.** Launching
Loom the obvious way today gets a build with no Standard side at all. I checked
the timestamp before testing only because `TEST 087` was burned by the same
thing from the other direction, and it is the difference between this report
and a report that says "the palette does not exist".

I could not rebuild it properly: **there is no `cmake` anywhere on this
machine**, so `flutter build linux --debug` refuses at the first step, and
`~/spike/env.sh` — which my notes said to source — no longer exists; the
toolchain is just `~/spike/flutter/bin`. Only the Dart half changed, so I ran
`flutter build bundle --debug`, copied the whole runnable bundle into my own
scratchpad, dropped the fresh `kernel_blob.bin` into the copy, and ran **that**.

**The shared tree's bundle was left exactly as I found it** — same bytes, same
timestamp, verified after. Everything below was measured on a blob built from
`61718e0` at `11:21`.

---

# 1 · THE STANDARD SIDE — fifty, and the fifty that should be there

> `standard | custom`
> **`50 shipped with the rules — tap one to copy it into this package and
> edit the copy`**

**The number is computed, not written down** — `right_pane.dart` interpolates
`${widget.standard.length}`, so `50` is the count of what was actually read off
the shelf rather than a claim about it.

Listed alphabetically by display name, `Adrenal` through `Wookiee Warblade`,
each with a `+`. All six categories Coder named are present and I read every
screen of the list rather than the first:

| | on the shelf | in the palette |
|---|---|---|
| weapons | 29 | Blaster Carbine … Wookiee Warblade |
| armour | 6 + droid plating 3 + `clothing` | Armour Class 4–9 · Light · Medium · Heavy · Clothing |
| robes | 4 | Jedi Robe · Knight Robe · Master Robe · Revan Robes |
| consumables | 4 | Adrenal · Charge · Medpac · Shield generator |
| supplies | 2 | Repair part · Security spike |
| objects | 1 | Object |

**And the set is complete rather than merely plausible.** I parsed
`equipment.toml`'s 56 base-type rows against the blueprint folder: **every base
type has a blueprint except the six `Wield classes` rows**, which are `1`–`6`
and are not carriable things. So "one per carriable base type" is exactly true,
and the exclusion is the right one — `Heavy` is droid plating and a wield class
is not an item.

---

# 2 · EDIT COPY — one tap, and the bytes are the bytes

**I copied one of each kind rather than one**, and checked the disk each time:

| tapped | wrote | status line |
|---|---|---|
| Long Sword | `items/weapons/long-sword.item` | `copied Long Sword — items/weapons/long-sword` |
| Armour Class 6 | `items/armour/armour-class-6.item` | `copied Armour Class 6 — items/armour/armour-class-6` |
| Jedi Robe | `items/armour/robe-1.item` | `copied Jedi Robe — items/armour/robe-1` |
| Medpac | `items/consumables/medpac.item` | `copied Medpac — items/consumables/medpac` |
| Object | `items/objects/object.item` | `copied Object — items/objects/object` |
| Repair part | `items/supplies/part.item` | `copied Repair part — items/supplies/part` |

**All six are byte-identical to the shelf original** (`cmp`, re-checked at the
end of the session). That is the promise the byte-copy decision was made for,
and it holds.

**The status line names both halves**, which matters more than it looks: two of
the six have a display name that is not their path — *Jedi Robe* is `robe-1`
and *Repair part* is `part`. An author who only saw the name would not know
what to write in `[equipment]`; the line tells them.

**It lands as `.item` beside a `.toml`** — my package was all legacy and the
copies came in under the current extension, mixed, as ruled.

### ✓ And the copy is a real blueprint, not just a file

This is the half I would not have taken on trust. `palette-probe` opens with
**18 problems**, all of the shape *"a player who picks X starts holding an item
at `items/weapons/…`, and this package carries nothing there."* One of them
names `items/weapons/long-sword`.

| | Verify |
|---|---|
| `long-sword.item` removed | **18 problems** |
| `long-sword.item` restored by **Edit Copy** | **17 problems** |

Run twice, one file changing. **The blueprint Edit Copy wrote satisfied a real
package fault** — the validator reads it, joins it and stops complaining. That
is end-to-end through the actual UI verb, which is what the owner's own ruling
asked for.

---

# 3 · THE SECOND TAP REFUSES — and the dangerous case is the one that works

> `this package already has `items/weapons/long-sword` — `Edit Copy` never
> replaces what is already here`

File unchanged by md5, nothing added. The whole sentence fits the status bar.

### ✓⚠ AND IT IS SPELLING-BLIND, which is the case that would have hurt

I set this up deliberately before touching the palette. `palette-probe`
contained:

```toml
# blueprints/items/weapons/short-sword.toml   ← LEGACY extension, EDITED
[item]
name = "Short Sword — MY EDITED COPY"
description = "If Edit Copy overwrites this line, the refusal did not hold."
```

A refusal keyed to `.item` would not have seen it, and `Edit Copy` would have
written `short-sword.item` beside it — leaving two files for one path, the
author's edits orphaned and invisible. Tapping **Short Sword**:

> `this package already has `items/weapons/short-sword` — `Edit Copy` never
> replaces what is already here`

**md5 unchanged, no `.item` written beside it, still three files in the
folder.** The refusal names the path without an extension, which is the right
vocabulary for a check that does not care which one is on disk.

*(Read, not run: `copyStandard` resolves its destination as
`into.path/blueprints/<path>`, so opening `base-rules` itself as a package and
tapping a row would compare the source file against itself and always refuse.
The shelf cannot be forked through this verb by construction. I did not test
it, because I had no safe way to open the shared shelf as a package — and I
came close to doing it by accident, see **what was mine** below.)*

---

# 4 · THE CUSTOM SIDE — only mine, and it does not need a restart

Before any copying, with two hand-authored files on disk, Custom showed
**exactly those two** under a `weapons` group and nothing from the Standard
side. After the six copies it showed all eight, grouped by folder —
`armour · consumables · objects · supplies · weapons` — **immediately, with no
restart**. That is `TEST 081`'s D1 not recurring on a new surface.

### ✓ And it is really reading the files, not listing filenames

**Mutation test, because a clean listing proves nothing on its own.** I made
`long-sword.item` invalid TOML and reopened:

> ⚠ **long-sword**
> `Not valid TOML: TOML parse error:`

Marked, in red, with the reason underneath, and the file still shown rather
than hidden — `PT-1575`'s *"an author who cannot see their file cannot fix
it"*, working. Restored afterwards and verified byte-identical again.

⚠ **One thing the marker does not cover, correctly:** an item whose `base`
names a base type that does not exist opens fine and is listed clean. That is
`ENGINE-INTERFACE-01 §4` doing its job — `openItem` is barred from reading the
rules, so it cannot know — and Verify is the layer that would catch it. I am
naming it so the green listing is not read as a stronger guarantee than it is.

### ✓ Both guarded branches, including the one with no package open

With no package open the list still shows all fifty and **the sentence
changes**:

> `50 shipped with the rules — **open a package to copy one into it**`

Tapping a row then does nothing, which the line above has already explained.
Neither branch fails silently.

---

## ⚠ THE ONE REAL FINDING — the problem count does not move when you copy

`palette-probe` reads **18 problems**, one of which is *"a player who picks …
starts holding an item at `items/weapons/long-sword`, and this package carries
nothing there."*

I used **Edit Copy** to put exactly that blueprint into the package:

| | header | Verify dialog |
|---|---|---|
| before the copy | `18 problems` | 18 problems |
| **after the copy** | **`18 problems`** | **18 problems** |
| after pressing **Verify again** | `17 problems` | **17 problems** |

**The fault was fixed and nothing said so.** `_verify` fires on package open
(`loom_shell.dart:246`), and `Edit Copy` is not one of the events that re-runs
it — so the count, and the report behind it, both stand stale.

**Why it is worth raising rather than shrugging at.** This is the one verb
whose whole purpose is to add a blueprint the package was missing, and the
commonest reason to reach for it is a Verify line telling you something is
missing. An author follows the instruction, the number does not move, and
nothing on screen says the number is old. The remedy is one click and it is in
the dialog already — `Verify again` — so this is a refresh that is not wired
rather than anything deeper. `PT-1730` already re-verifies after *"setting the
entry area, creating an area"*; this is the same list with one new member.

## ⚠ And the verb is named for an edit that has no surface in Loom

*"Edit Copy"* — the copy lands correctly and is genuinely yours. **There is no
way to edit it in Loom.** `NewItemDialog` creates and never loads; nothing in
`lib/` opens an existing item into a form; tapping a Custom item row sets paint
mode and shows nothing at all.

**I am naming this rather than filing it**, for two reasons. The commit message
says so itself — *"`PT-2037` slice c"*, and `standard_blueprints.dart` calls
Edit Copy *"the FIRST of the four verbs a palette blueprint has"*. And the
owner's ruling (`PLAYTEST-RULINGS-01:64265`) is explicitly about why you may
**never** edit the shipped one, which this respects exactly. The gap is only
that the copy you now own is edited in a text editor rather than in Loom.

---

## What was mine, not the product's

- **I read Verify as an inert control and was wrong.** Tapping `18 problems`
  did nothing through several attempts, and I was close to filing it.
  `xdotool`'s window-relative clicks were not landing on the module tree
  (they land fine on the palette); **absolute screen coordinates opened it
  first try.** My automation, and the control is correct — the count is its own
  `GestureDetector` inside the row, exactly as the source says.
- ⚠ **I nearly copied into `base-rules` itself.** Typing a path into the GTK
  directory chooser's `ctrl+L` bar got mangled and left the location reading
  `base-rules` with that row selected; one more click would have opened the
  shelf as a package. I caught it by screenshotting the dialog before pressing
  Open. Nothing was written. Flagging it because *"open the shelf as a package
  by accident"* is a real user path, even though the refusal above means the
  verb itself would have held.

## What I did not do

- **Did not exercise the legacy-source branch of `Edit Copy`.** All fifty shelf
  blueprints are `.item`, and the shelf is generated, so a `.toml` source is
  unreachable without editing `base-rules` — which is shared with Coder and
  guarded by `check_shelf`. The walk uses `isKind` and the write always uses
  the current extension, so the branch is written; it is untested.
- **Did not test a copied blueprint in play.** Byte-identity with a shelf file
  the generator produced, plus Verify joining it and dropping a problem, is the
  evidence I have.
- **Did not test the other three palette verbs** — only Edit Copy exists.
- **Did not touch the poison work**, as instructed.
- **Did not re-test** `PT-2029`, `TARGETING-01` or anything from TESTs 084–087.

## State

- **New package `palette-probe` is mine and left on disk** — one area, two
  hand-authored items (`tester-blade`, and the deliberately-edited legacy
  `short-sword.toml` that the spelling-blind refusal was built to meet) and the
  six blueprints `Edit Copy` wrote. It is a working palette fixture.
- **All mutations restored and verified**: `long-sword.item` is byte-identical
  to the shelf again; `check_shelf.py` is green; `base-rules` untouched.
- ⚠ **`Loom/build/flutter_assets/` in the shared tree now holds output from my
  `flutter build bundle`** — gitignored, regenerable, and it does not shadow
  the desktop bundle. The desktop bundle itself is byte-for-byte as I found it.
- My Loom PIDs `97354`, `99477`, `100424`, `101763` all killed by PID, all
  confirmed gone. No Loom or app of Coder's was touched.
