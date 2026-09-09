# BUILD 61 — `PT-1484` and `PT-1485` queued, and two things measured while they wait

**684 green.** No behaviour changed this slice.

---

## `PT-1484` — recorded, not built

Written into `grant_reaches_class_test.dart` beside the code that will
implement it: **the item half is not offered at all** where it cannot reach
this character; `PT-695` gives a profession one grant with the player choosing
the form, and **where the item form cannot reach them there is no choice to
make.** The rejected option and its reason are recorded too, so a later fix
does not re-derive them.

**The last assertion in that file turning red is the fix working.**

## `PT-1485` — queued, and it is the opposite operation

`PT-1484` **withholds** an item a class cannot use. `PT-1485` **adds** one a
class can. Confirmed against the data: `Acolyte` teaches **Mysticism** and its
grant is `Padawan Robe → Jedi Robe` — so the item half is a Jedi's and the
aptitude half is a knowledge skill. Withholding would empty the item half for
most of the roster.

---

## ⚠⚠ "Populate `targets` from the prose" is NOT mechanical

I checked before planning it as a slice, and it does not survive contact.

**The prose states a NEGATIVE and `targets` is a POSITIVE list.**

    prose:    "This power does not affect droids."
    column:   targets = ["sentient", "beast"]

Of the 21 silent powers, **the cells name no positive kind at all** — seven of
the eight sampled contain none. Converting one to the other needs **the closed
set of kinds**, and ⚠ **nothing states it**: `sentient`, `beast`, `droid` and
`self` are simply the four that appear across 17 authored rows, and they occur
together only inside individual power cells, never as a declared set.

**So it would be inference, not transcription** — precisely what the 23-vs-2
measurement warned against.

⚠ **A cheaper shape that invents nothing:** record the negative the prose
actually states.

    excludes = ["droid"]

That is transcription. It composes with `targets` rather than replacing it, and
a gate can then answer **three** ways — *permitted*, *excluded*, *silent* —
instead of guessing on 21 powers. **Needs a ruling on the field, not on the
kinds.**

## ⚠ And `professions.teaches` is `equipment.section` again

`Acolyte`'s note sent me to look, and the field next to it has the same shape.

**11 of 28 `teaches` values are not a skill name.** Ten are a skill name with
flavour fused on:

    Conscript   Athletics — they marched it into you before they trusted you with a rifle
    Veteran     Intimidate — you have seen things and it shows
    Dancer      Acrobatics — you were paid to make it look easy
    …ten in all, and ⚠ ALL TEN RESOLVE TO A REAL SKILL WHEN TRIMMED

The eleventh is `Mysterious Stranger`'s **`ANY SKILL`**, which is a value.

⚠ **This field is rendered to the player as their aptitude**, and it is a value
used as a key — the same defect `PT-1480` fixed in `equipment.section`, and the
same proportion as `PT-1482`'s `kit` column: over a third.

**Unlike the seven, the split here IS mechanically decidable** — *"the head
resolves to a skill name"* is a test, and it passes 10 of 10. **But whether the
flavour is kept and where is a data-shape decision**, and it is good flavour: a
player probably should read *"you were paid to make it look easy."* Reported
rather than changed.

## Still open

- ⚠ `professions.teaches` — 11 of 28, needs a ruling on where the flavour goes.
- ⚠ `targets` — the negative is transcribable, the positive is not.
- `PT-1484` and `PT-1485`, both waiting on the Guardian run.
- 45 annotation cells; conditional damage; a citation assembled at runtime.
