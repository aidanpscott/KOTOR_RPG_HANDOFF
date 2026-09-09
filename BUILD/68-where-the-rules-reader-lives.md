# BUILD 68 — Where the rules reader lives, argued

**It is a `Lodestar` opener that Loom calls — and it must return ROWS, NOT
RECORDS.** The repo is the easy half; the return type is the half that decides
whether `PT-1430` holds.

---

## 1 · The anomaly is Lodestar's, not Loom's

Lodestar opens every kind of package file:

    open              package.toml
    openArea          areas/*.toml
    openCharacter     blueprints/characters/*.toml
    openItem          blueprints/items/**.toml
    openDoctrine      blueprints/doctrines/*.toml
    openConversation  dialogue/*.toml
    ⚠ —               rules/*.toml

**`base-rules` is a package** — `PT-1380` rules it *"a legitimate package with
no entry"*. A rules table is a package artifact exactly as an area is. **A
rules table is the one package artifact Lodestar cannot open**, and Loom
needing one merely walked into that.

Scoped negative: **no path under `Lodestar/lib/src` contains `rules/`** —
checked. This adds a capability rather than duplicating one.

## 2 · `ENGINE-INTERFACE-01 §4` bars browsing, not reading

Every opener takes **a path the caller found**. `openItem` knows nothing about
`endar-spire`; `openRules` would know nothing about `base-rules`. The app finds
the file, as it does now. **Nothing about §4 changes.**

## 3 · The monopoly argument runs the other way

⚠ **It is already broken, and Loom is not where.** The app parses rules TOML in
two places today — `chargen_source.parseKind` and `records.dart`'s `read` — and
Lodestar parses none.

- Loom grows its own → **three** parsers of the same bytes.
- One opener in Lodestar, called by both front-ends → **one**, and the app's
  two retire into it.

**A reader in Lodestar removes a second parser. A reader in Loom adds a third.**

## 4 · ⚠⚠ But the MEANING must not move, and this is the real decision

`openRules` returns `List<Map<String, Object?>>` and a typed error. **Nothing
else.**

The moment it returns a `SpeciesRecord`, Lodestar acquires opinions about
species, classes and professions **that it has deliberately never had** — and
`records.dart`'s typed layer becomes a second opinion on the same bytes. **That
is exactly `PT-1430`'s failure**, and it happens if the reader is too smart,
not if it is in the wrong repo.

    the ROWS are the format          → Lodestar, one reader
    the RECORDS are the vocabulary   → the app, and only the app

⚠ Loom needs rows. It wants `id` and `name` off `equipment.toml`, filtered on
`section` — which is a **key** since `PT-1480`, and this would be its third
reader. It does not need `PowerRecord` and must not be given one.

## 5 · And it makes an absence typed

`ChargenSource.baseTypes` returns `const {}` when the file is missing — which
reads as *"there are no base types"*. An opener returns `OpenedRules` or
`RulesError`, which is **absence against error**, the distinction this corpus
has paid for more times than any other.

---

## What falls out

- `NewItemDialog` becomes reachable — Loom calls the opener and filters on
  `section`. The dialog was never the finding.
- The app's two parsers become one call.
- `dialogs_reachable_test`'s second assertion turns red, **which is the fix
  working**, and it says so in its own body.

## ⚠ What I would NOT do

- **Not a Loom reader.** Third parser, second opinion.
- **Not typed records in Lodestar.** That is the failure this is meant to
  avoid, wearing the right repo's name.
- **Not a `RulesIndex` that knows `base-rules` by name.** The caller finds the
  file. That is what keeps §4 true.

**Say the word and I will build it.** It is one opener, one result type, and
two call sites retired.
