# BUILD 86 — `PT-1553` findings 1 and 2: one mapping, one create shape

**884 green** — Lodestar 395 · Lens 7 · Loom 151 · app 331.

Lodestar `61e2849` · Lens `6b55219` · Loom `45a2df8` · app `f453601`.

⚠ **Loom only.** No reader, no writer, no other program.

---

## ⚠⚠ FINDING 1 — THE COPY THAT WROTE

`BlueprintIndex.folderFor` is the one declaration of **category → folder**, and
it carries the reason three kinds have a home and seven do not (`PT-1500`).

`right_pane.dart` built a placement's `from` with its own copy:

    final path = k == 'creatures' ? '$charactersIn/$e' : '$k/$e';

> **That was the copy that WROTE.** Everything downstream — the tag, the file,
> the token, the fight — trusts the string this line produces.

⚠ **AND IT WAS CORRECT BY COINCIDENCE.** `doctrines` and `items` happen to name
their own folders. `creatures` lives in `blueprints/characters` — `PT-1325`
ruled beasts and people share one document — **which is why that one kind needed
a special case at all.** A fourth kind whose folder differs from its category
would have gone through the general branch and written a path nothing resolves.

⚠⚠ **AND THAT IS EXACTLY HOW `PT-1493` HAPPENED THE FIRST TIME.** Three places
disagreed on a prefix, each correct in isolation, **and the one that wrote was
the outlier.** A creature was *drawn and was not there*: `combatantsIn` skipped
it, `Lens` drew it anyway, and you could walk through it.

### The fix: one conversion, in one place

    BlueprintIndex.folderLeafFor(kind)   'creatures' → 'characters'
    BlueprintIndex.pathFor(kind, id)     → 'characters/probe-warden'
    placed.dart · kindOfFrom(from)       the inverse, through the same helper

**⚠ The two path bases are the whole hazard.** `folderFor` is package-relative
(`blueprints/characters`); a `from` and an `[equipment]` path are relative to
`blueprints/` (`characters/x`). **One side prepending the prefix and the other
not IS `PT-1493`**, so the conversion happens in exactly one function.

### ⚠ AND `new_item.dart` WAS A THIRD COPY

    if (!p.startsWith('items/')) …

It asks `kindOfFrom(p) != 'items'` now, **and interpolates the folder's real
name into its own refusal sentence** — so the message cannot outlive the fact it
states. A build where items have no folder says that instead, rather than
printing `null/`.

### ⚠ The control

**Every kind `folderFor` declares round-trips, both directions**, and the seven
with no folder return **null rather than a guessed path**.

⚠⚠ **And the assertion that actually matters is a widget test on the palette**:
tap `probe-warden` and what comes back is `characters/probe-warden` — **not
`creatures/…` and not `blueprints/characters/…`**, which are the two wrong
answers `PT-1493` was made of. *The copy that wrote is the copy that is tested.*

---

## ⚠⚠ FINDING 2 — ONE SHAPE FROM EVERY CREATE DIALOG

    NewCreatureDialog    handle    'probe-warden'
    NewDoctrineDialog    handle    'plain-aggression'
    NewItemDialog        path      'items/weapons/blaster-rifle'

**and all three call sites in the shell named the parameter `path`.**

Nothing had broken, because only a status line read it.

### ⚠⚠ AND THE OWNER'S REASON THIS IS MORE THAN TIDYING

**Our dialogue system is not NWN's or KOTOR's, and the conversation dialog is
the one that differs most:**

    PT-1430   a CLOSED gate vocabulary, against their free script references
    PT-1432   TWO kinds of link list — `replies` shows all, `then` picks one
    PT-1434   NPC-to-NPC continuation
    PT-1433   an empty `say` REFUSED, where 59% of theirs are blank
    PT-1552   our editor asks for the SCHEMA; Aurora's Store Wizard asks in
              the domain's language

> **So a conversation is the kind whose create path will change most in the
> rebuild — and a shared return shape is what lets it change WITHOUT BREAKING
> ITS CALLERS.**

### The shape

    class Created { final String kind; final String id; }
        blueprintPath   derived through folderFor — NULL for a kind with no
                        blueprint folder
        describe        where it lives IS what it is — PACKAGE-NAMING-01

**⚠ `id` is relative to the kind's OWN folder** — `probe-warden`, or
`weapons/blaster-rifle` for a kind that nests. **Exactly the shape
`Listed.names` returns**, so a thing that was just made and a thing already
listed are the same string.

**⚠ It is the pair the tree already uses.** `Placed` carries a `kind` and a
`handle`; so does this. **One vocabulary for a thing that exists and a thing
that was just made**, rather than a second one invented at the create seam.

**⚠⚠ AND THE NULL IS THE POINT.** A conversation lives under `dialogue/`, not
under `blueprints/`. It can carry this shape **today** without pretending to be
a blueprint — which is what a null buys that an empty string does not.

**⚠ And a path nothing declares is REFUSED, not classified.**
`Created.fromBlueprintPath` returns null for `placeables/crate`, for `characters`
with nothing after it, and — the sharp one — **for `blueprints/characters/x`,
the `PT-1493` mistake itself**, rather than accepting a kind called `blueprints`.

---

## ⚠⚠ AND ONE FOUND WHILE WRITING THE TEST

The palette read `(bp[k] as Listed)` — **a cast on a map lookup.** A kind the
index did not answer for **crashed the pane** instead of reading as *not read
yet*.

> **Absence treated as an error, in the shape this corpus repeats most.**

`BlueprintIndex.of` fills every kind, so it was unreachable. **Unreachable is
not the same as safe**, and a cast is what turns a missing key into a blank pane
with a red exception behind it. It reads `…` now, which is what the pane already
shows while the index is loading.

---

## ⚠ FINDINGS 3 AND 4 STAND, AND THE OWNER GAVE THE REASONS

**3 · Three routes to the `+` verb — NOT A DEFECT.** The kinds genuinely differ
because **seven of ten have no file format yet.** Three routes are three real
situations, and it resolves when the palette is rebuilt rather than by being
tidied first.

**4 · `new_package_test`'s count assertion — KNOWN, AND LEFT.** It passes only
because its package is empty. **It will break loudly the first time somebody
tests a package with things in it, which is the right way round.** Not
pre-emptively loosened: **a test that stops counting is a test that stops
noticing.**

---

## ⚠ SLICE TWO IS THE PALETTE, AND IT WAITS FOR THE WORD

`Tester` is still closing the quest, script and import/export holes — **and
quests especially may want a home in it.**
