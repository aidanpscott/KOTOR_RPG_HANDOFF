# BUILD 85 — `PT-1553`: two trees, slice one. An authored thing gets a home.

**876 green** — Lodestar 395 · Lens 7 · Loom 143 · app 331.

Lodestar `61e2849` · Lens `6b55219` · Loom `67b7cf5` · app `f453601`.

⚠ **Loom only. No reader, no writer and no other program changed.**

---

## ⚠⚠ WHAT WAS ACTUALLY MISSING

**A placement had no home in any surface at all.**

`ContentsWriter.proposeTag` has numbered tags from the area counter since
`PT-1377`. `ContentsWriter.append` has written them. `Lens` has drawn a token
for each. `PT-1331` makes a tag **permanent and never reassigned**, and the log
records it.

> **And the author who caused a tag had never seen it.**

It existed as a `[[contents]]` row in a file. You could click the token on the
board and the selection bar would name it — **while that one tab was open, and
only then.**

## ⚠ IN PLACE, NOT BESIDE — AND THE REASON IS OURS, NOT AURORA'S

**Our format already separates the two.** `blueprints/characters/x.toml` is a
TEMPLATE; a `[[contents]]` row is a PLACEMENT pointing at one.

> `PT-1542` found **a SURFACE that collapsed them, not a MODEL that did.**

So `placed.dart` is a **view over what the openers already return** —
`OpenedArea.contents`, `.connections`, `.arrivals`. Nothing was added to
Lodestar, no file changed shape, and the tree cannot disagree with the board
because it is reading the same three lists.

## ⚠ THE TREE NESTS AREA → KIND → INSTANCE

    a01-command-deck
      creatures
        sith-trooper.command-deck.39      6, 4
      doorways
        door.command-deck.01              7, 2
      arrival points
        aft                               1, 3

**⚠ Only the groups the area actually has.** Ten empty category rows under
every area would be `PT-1500`'s defect again — **the palette enumerates the KIND
SPACE** (ten categories, three that can be listed and seven that say they
cannot), **the tree enumerates WHAT EXISTS.**

**⚠ In FILE ORDER.** `§3` gives contents no ordering meaning, so sorting would
invent a rank an author did not write — **and a tag they just made would move
away from where they are looking.**

**⚠ And the coordinate is on the row**, because two placements of one blueprint
differ by their square before they differ by anything else.

## ⚠⚠ AN ARRIVAL HAS NO TAG, AND THE TREE KEEPS THAT DIFFERENCE

`§4·0` makes an arrival *"a name and a coordinate"*, and Lodestar's own comment
says why: **a tag identifies a thing the LOG records**, and the log records that
a character moved — not that a doorway exists.

So the handle is `arrival:<name>` — **the convention `AreaTab` and
`AreaGridView` have already shared since arrivals existed.** A second convention
would have been a second bug. **A doorway does carry a tag**, and it was equally
invisible; it has a row now too.

## ⚠⚠ AND THE UNCLASSIFIABLE ROW IS KEPT, NAMED, AND REACHABLE

A `from` whose first segment matches no declared folder gets its own group,
drawn in alert: **`⚠ unknown kind`**.

**Not dropped and not guessed into the nearest category.** `PT-1493` is exactly
this row — a creature was *drawn and was not there* because Loom wrote a path
the reader could not resolve, and **nothing on any surface said so.**

> **A thing you cannot classify must still be selectable, or you cannot delete
> it.**

## ⚠ ONE SELECTION, TWO SURFACES

It was `AreaTab`'s own `_selected`. It is the shell's now, as `(area, handle)`.

**⚠ The embedder holds it, and that includes a test.** `arrival_delete_test`
grew a six-line `_Holder` that does what `LoomShell` does. **That is the point
rather than a cost:** a tab that kept a private copy as a fallback would be the
second source of truth this ruling exists to remove.

**⚠ And placing SELECTS what you just made** — a creature, a doorway, an
arrival. The tag is on the selection bar and on its own row in the tree before
the next click. **That is the slice, in one line.**

---

# ⚠⚠ WHAT I FOUND ASSUMING THE OLD SHAPE

## ✓ FIXED HERE

### 1 · TWO `blueprintKinds` LISTS, AND A COMMENT SAYING SO

`module_tree.dart:74` declared its own ten-kind list beside
`right_pane.dart:70`'s, with the comment *"the same nine the palette shows."*

⚠ **`PT-1441`'s tenth kind had already been added to both by hand**, and the
comment still said nine above ten entries. **Two lists that must never diverge
and nothing anywhere that could notice if they did.** `§6·0` establishes they
are **one list rendered twice for two jobs**, so there is one.

### 2 · THE TREE'S OWN DOC COMMENT WAS A STALE CLAIM

> *"⚠ CATEGORIES ONLY. The tree nests area → its contents, and that needs
> contents to exist. **Nothing is placed yet.**"*

**True for exactly one slice** — `4d` gave the palette a place verb. A comment
that describes an absence is a comment with an expiry date, and nothing expires
it.

### 3 · THE SELECTION LIVED IN THE TAB

Reachable only by clicking the board, only while that tab was open, **and
destroyed when the tab was replaced.** A second view of it was not possible; it
was not a model, it was a widget's field.

## ⚠ FOUND, NOT FIXED — REPORTED

### 4 · ⚠⚠ THE CATEGORY→FOLDER MAPPING IS WRITTEN TWICE

`BlueprintIndex.folderFor` is the declaration, and it carries the reasons
(`PT-1325`, `PT-1441`, `PT-1452`, `PT-1500`).

**`right_pane.dart:220` writes it again**, as the line that builds the path a
placement will be written with:

    final path = k == 'creatures' ? '$charactersIn/$e' : '$k/$e';

⚠ **It is correct today only because `doctrines` and `items` happen to name
their own folders.** The day a fourth kind gets a folder whose name differs from
its category — which is what `characters`/`creatures` already is — **that line
writes a path nothing can resolve, and `PT-1493` happens again.**

⚠ `placed.dart` deliberately derives the inverse from `folderFor` rather than
becoming a third copy, and the suite asserts every entry round-trips. **The
second copy is still there and it is the one that WRITES.**

### 5 · ⚠ TWO OF THE THREE CREATE DIALOGS RETURN A HANDLE AND ONE RETURNS A PATH

    NewCreatureDialog.onCreated    handle    'probe-warden'
    NewDoctrineDialog.onCreated    handle    'plain-aggression'
    NewItemDialog.onCreated        path      'items/weapons/blaster-rifle'

**And all three call sites in the shell name the parameter `path`.** The status
line prints whichever it got, so nothing has broken.

⚠ **It matters for the NEXT slice.** `selectedBlueprint` is a **path** — so
*"select the blueprint you just created"*, the palette's exact analogue of what
this slice did for placements, **cannot be done for two kinds of three** without
reconstructing the path from the handle. **Which is finding 4, one caller
along.**

### 6 · ⚠ THREE ROUTES TO ONE IDEA: `+`

`creatures` goes through `onNewCreature`; `items` and `doctrines` go through
`onNewOfKind` + `_creatingKind`; the other seven have no `+` at all
(`newableKinds = {'doctrines','items'}`). **Not a defect — the kinds genuinely
differ in whether they have a format — but three shapes for one verb, and the
palette is next.**

### 7 · ⚠ A COUNT-BASED ASSERTION THAT NOW DEPENDS ON WHAT IS PLACED

`new_package_test` asserts `findsNWidgets(2)` for `creatures`, `doctrines` and
`doors` — once in the tree, once in the palette. **With instances in the tree a
kind name can now appear a third time.** It still passes because that test makes
an empty package, **and it is a coupling that was invisible before today.**

---

## ⚠ THE FIVE SETTLED THINGS — NONE REOPENED

    PT-1340  SINGLE WINDOW          no new window; the same left pane
    PT-1375  FOUR TABS BY KIND      no tab added; a leaf OPENS an area tab
    PT-1376  editor owns C/S/C      the tree creates nothing and saves
                                    nothing — it selects, and opens the
                                    editor that does own those
    PACKAGE-NAMING-01  PATH AS
             IDENTITY               `kindOfFrom` matches the FIRST segment
                                    against declared folders — never
                                    resolving a path by its last segment,
                                    which `BUILD 42` refused for this exact
                                    reason. And the selection is CLEARED when
                                    the package changes: a bare tag means
                                    nothing without a package
    PT-1331  NEVER-REASSIGNED TAGS  the tree displays a tag and never edits
                                    one. Making it visible STRENGTHENS the
                                    ruling — a permanent identifier nobody
                                    can see is a rule nobody can check

## ⚠ AND WHAT SLICE ONE IS NOT

**Not the palette, not the Standard/Custom split, not the editors, not the
wizards.** Nothing cosmetic was touched.

**No rename, no drag, no reorder, no context menu.** The tree **selects** and
**opens**. Delete is still the selection bar's, where `STUDY 17` put it.
