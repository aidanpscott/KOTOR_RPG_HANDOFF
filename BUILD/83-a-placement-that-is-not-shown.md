# BUILD 83 — `PT-1550`: a placement that is not shown, and what a corpse is for

**859 green** — Lodestar 395 · Lens 7 · Loom 131 · app 326.

Lodestar `61e2849` · Lens `6b55219` · Loom `be9215c` · app `3f72057`.

---

## ⚠⚠ `PT-1550` — AN AUTHOR MAY PLACE A CREATURE THAT IS NOT SHOWN

The ruling: **not a perception system. A property of the placement.** One
field, no checks, nothing computed, no tile involved.

    [[contents]]
    tag    = "ambusher.command-deck.03"
    from   = "characters/sith-trooper"
    at     = [7, 1]
    hidden = true

## ⚠ WHERE THE FIELD LIVES, AND WHY THERE

**`AREA-FORMAT-01 §3`'s `[[contents]]`** — the block that already carries
`tag`, `from` and `at`. It is written up as **`§3a`**.

⚠ **It is a fact about ONE PLACEMENT, not about a creature.** The same
blueprint placed twice may be hidden once: `from` is a template and `hidden`
is this instance's. Putting it on the blueprint would make *every* Sith
Trooper in the package an ambusher.

⚠ **Absent means shown.** Every area written before the ruling is correct
without migration — and that is the field's default in `PlacedThing`, not a
sentence in a document.

## ⚠⚠ AND `LOOM MUST BE ABLE TO WRITE IT` — `PT-1440`. TODAY IT CANNOT.

*Anything the Builder cannot write, the Builder eventually destroys.*

**Checked rather than assumed:**

    ContentsWriter.render            emits tag, from, at — and nothing else
    ContentsWriter.append            appends; never rewrites an entry
    ContentsWriter.withTagRemoved    removes a WHOLE entry, fields and all
    callers                          area_tab.dart:105 and :183, those two

⚠ **So a hidden placement is a hand edit, and the hand edit SURVIVES today.**
Loom appends and deletes; it never edits an entry in place, so a later
placement does not drop a `hidden` line somebody added. **The moment that
changes is the moment Loom gains an edit-in-place path** — which is exactly
when the rebuild has to carry the field.

⚠ **THE BUILDER IS BEING REBUILT, so this is a NEED for the rebuild rather
than surface work now.** It is the same shape as `conversation`, which
`bed_creature_test:113` records as *read and written by nothing* until
`PT-1425` gave Loom the field — and `BUILD 31`/`33` found the creature dialog
**silently erasing** a hand-added `conversation` line before that.

> **`hidden` is one checkbox on the placement dialog. Naming it now so the
> rebuild has it in scope is the whole ask.**

## ⚠⚠ AND WHAT `hidden` DOES NOT MEAN: NOT PRESENT

**The thing worth getting right.** A hidden creature is **in the room.** It
stands on its square, it holds that square, and walking into it finds it. It
is only NOT DRAWN.

⚠ **The alternative — filtering it out of `_here` — was the tempting one**,
because `PT-1538` filters the dead out of `_here` exactly that way and that
filter is right. **It is right for a creature that is GONE and wrong for one
that is waiting.** A hidden creature you can walk through is a marker with no
consequence, which is the same defect `PT-1532` names below.

## ⚠ SO THE RENDERER IS TOLD, AND DOES NOT DECIDE

`Lens` draws `area.contents` for **both programs**, and the two disagree —
**and both are right**:

    the play client   a hidden creature is not drawn
    Loom              an author must see everything they placed

An author who cannot see it cannot select it, move it or delete it. So
`paintAreaBoard` and `AreaViewport` take **`concealed`, a set of tags**, and
the CALLER decides: **Loom passes nothing, always.**

⚠ **It is a set of tags rather than a flag the renderer reads off the
placement**, and that is deliberate: a renderer that consulted `hidden` itself
would be holding a policy in the one place that must not have one.

⚠ **And `shouldRepaint` compares the set.** A set that changes with a painter
that does not is a creature that stays invisible after the thing that found it.

## ⚠ THREE SURFACES SHOW A CREATURE, AND ONE PREDICATE ANSWERS ALL THREE

    Lens's token          concealed, passed to AreaViewport
    the marker overlay    _drawMarker, drawn OVER the token
    the panel's wound     _workingLines, outside a fight

`_concealedThing(PlacedThing)` is asked by each. **A rule applied to one path
and not the next is this corpus's most-repeated defect** — and here it would
have been a hidden creature with no token and a marker circle sitting exactly
where it stands.

⚠ **It is NOT asked by `_occupant`, by `_present` or by the fight**, and that
is the point. Those are *is it there*, not *is it shown*.

## ⚠⚠ CONTACT IS THE REVEAL

The ruling says *"until something reveals it"* and names no mechanism, because
**a mechanism is what it rules out.** Walking into a square already does
something, so the reveal rides on a gesture the player has: **no roll, no
radius, no score.**

Bumping a hidden creature reveals it **and stops there** — the ambusher is on
the board and the next press is yours. The second press does what contact
always did: talks, or fights.

⚠ **Nothing else reveals, because nothing else can.** An encounter today is
`[me, the one I touched]`. **The day an encounter takes more than two, that is
the second caller of `_reveal`.**

## ⚠ THE LIMITATION, NAMED RATHER THAN LEFT TO BE FOUND

**A reveal is the VISIT's, not the campaign's.** `_revealed` is cleared by
`_enter` with everything else the area owns, so **walking out and back in
re-hides an ambusher you already found.**

⚠ **A reveal that outlived the visit would have to be an event, and
`PLAY-STATE-01` has no kind for one.** Inventing a kind nothing rules is
precisely how `character.moved` came to be **declared, read, and written by
nothing** (`PT-1523`). This is a gap named, not a modifier invented.

## ⚠⚠ AND A `hidden` THAT IS PRESENT AND NOT A BOOLEAN IS AN ERROR

`hidden = "yes"` is **a placement the author believes is concealed and the
runtime shows.** Silently reading it as false is *absence treated as error, or
error treated as absence* — this corpus's other most-repeated defect, in the
one field where it is invisible by construction.

⚠ **And contents are read ONCE, before either `[tiles]` branch.** The mapped
form and the default form each called `_contents` themselves; a malformed
`hidden` refused in one and accepted in the other would have been the
rule-applied-to-one-path defect **written on the same day as the field.** The
suite asserts the refusal **from both forms**, each with its well-formed
control.

## ⚠ AND FOG STAYS RULED OUT — `PT-1509`'s HALF THAT IS NOT BUILT

`wall.blocksSight` **stays `true` and stays UNREAD.** `PT-1529` established
that a field that is right with nothing consuming it is **a roadmap rather
than a defect.**

> **The board shows what is in the area. What perception governs is WHO IS
> STANDING IN IT.**

⚠ **And the half that matters is built:** `PT-1509`'s map of areas this
character has stood in is a real fog of war — **of the world rather than the
room** — and it is per-character, so a droid and a Jedi genuinely know
different things.

---

# ⚠⚠ `PT-1532` — WHAT A CORPSE IS FOR, BEFORE BUILDING ONE

**Four things a corpse could be for. Three are already served and the fourth
is the one we cannot do.**

## 1 · LOOT — the real purpose, and the one thing we have none of

`STUDY 23`: a KOTOR corpse **is the creature itself**. `SetIsDestroyable`'s own
BioWare comment says *if false, the caller does not fade out on death but
sticks around as a corpse* — **same object, same inventory.** `RancorCorpse`
and `KraytCorpse` exist as placeables **with zero placed instances.**

⚠ **So a corpse's job in the source game is to be a container you take from.**

**Checked, not assumed:**

    an event kind for gaining an item      none. `item.lost` is declared,
                                           `§9` has a worked example, and
                                           NOTHING READS IT — `PT-1516`
    inventory transfer anywhere            none in KOTOR-RPG-APP/lib or
                                           Lodestar/lib. One `loot` in the
                                           tree and it is a comment
    the player's own [equipment]           not written by chargen at all —
                                           `PT-1452`'s open gap

**The one purpose a corpse actually has is the one we have no machinery for
at any layer.**

## 2 · OBSTRUCTION — buildable, and it would UNDO the thing that works

A body that blocks or slows its square is cheap now: `PT-1513` gave the tile a
cost and the creature the multiplier.

⚠⚠ **But `PT-1511`'s vacated square is the consequence that currently WORKS**,
and it was unreachable until `PT-1515` made anything die at all. **Replacing a
working consequence with a blocked square is a net loss** unless the block is
itself interesting, and nothing rules that it is.

## 3 · EVIDENCE — already answered, without a body

*Is this one dead?* `character.died` is a constant, `play_state.dart` folds it,
it survives a quit and it is campaign-scoped. A gate that wants to know **reads
the log.**

⚠ **A corpse would be a second and weaker source for a fact the log already
carries** — a value used as a key, one more time.

## 4 · DRESSING — honest, and exactly the thing the ruling warns about

*"If nothing loots it and nothing walks over it, it is a marker with no
consequence."*

## ⚠⚠ THE ANSWER: NOT YET, AND THE BLOCKER IS NAMED

**A corpse is for looting. Build looting and the corpse comes with the
container it is** — an event kind that says something changed hands, and a
screen that can take. Built first, it is a marker that blocks a square that
used to be walkable, delivered before the thing that would make it worth
walking to.

## ⚠ AND MY EARLIER REASON WAS THE WRONG REASON — `PT-1525` HAD ALREADY SAID SO

I argued three blockers — **no corpse tile type**, **`[[contents]]` is
authored**, **`§4` bars the engine from editing a package**. All three block
the **placeable** path, and **KOTOR abandoned that path.** Leaving the
combatant where it stood needs none of them: the body is where it fell, the
inventory is already on it (`PT-1452`), and it is runtime state
`PLAY-STATE-01` already projects.

> **It is CHEAP and it is still not worth doing.** That is a different answer
> from *the format forbids it*, and a better one — a wrong reason sends the
> next person to look in the wrong place.

## ⚠ AND `PT-1550` PROVED THE HALF THE CORPSE WOULD NEED

**On the board and not drawn** is now expressible, tested, and one field. A
corpse is the **inverse** — drawn and not on the board — and that half has no
mechanism at all. **The symmetry is worth noticing: one of the two directions
took a boolean, and the other still takes a system.**
