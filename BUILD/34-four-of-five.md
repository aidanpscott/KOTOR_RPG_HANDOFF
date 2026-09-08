# 34 · Four of the five closed, one stop, and a sixth found

**258 Lodestar · 206 app · 110 Loom · 4 Lens.** All analyze clean.

---

## 1 · ⚠⚠ Doctrine and reaction are a STOP, and it is a format question

**The brief anticipated this and it is what happened.**

`AUTHORED-CHARACTER-01` writes `doctrine = "doctrines/sith-line"` — **a path
into a `doctrines/` folder.** `PACKAGE-FORMAT-01 §3`'s layout has **no
`doctrines/` folder**, and **no document says what a doctrine file contains.**

**⚠ And the two documents disagree on the shape.** `ATTACHMENT-01 §2` writes
`doctrine czerka_security` — **a bare handle.** Path or handle is undecided.

**Reaction is the same.** `ATTACHMENT-01 §3` specifies a reaction as
`on: <event kind> then: <response>` — a declared thing with two parts — and
**nothing says where one is declared.** The creature field is a list of names
pointing at nothing.

> **WHAT IS MISSING: a home in the package layout and a file format for a
> doctrine and for a reaction, and a ruling on whether a creature names a PATH
> or a HANDLE.**

**⚠ Why I did not build the field anyway.** A field would let an author type a
name that **cannot ever resolve** — the extension point `§4` refuses, one
document up. **The line is clean and it is why equipment WAS built:
`items/` exists and `doctrines/` does not.**

**⚠ AND THE COST IS REAL AND IS `PT-1423`'s.** The doctrine layer has no
authoring path, so **every creature the Builder makes carries none** and the
play screen still fights with the `plainAggression` fixture. **Nothing built
before this is wrong; nothing built after it can be right either.**

**⚠ And `[[connections]] from` is the same stop one level down.** `§4a` makes
the door template optional and `ConnectionWriter` can write it — but it names a
file in `blueprints/doors/`, **a folder in the layout with no format behind
it.** *Reported, not built. It was not cheap.*

---

## 2 · Equipment — built

**Read since the blueprint reader existed; written by nothing.** `PT-1425`'s
fist is a fist because of it, and **a creature with a blaster had never
existed.** It does now: the bed's trooper carries
`weapon_r_1 = "items/weapons/blaster-rifle"`, **made by clicking.**

**⚠ THE SLOT NAME IS THE AUTHOR'S, NOT LOOM'S.** `PT-1252` locks **eleven
slots** as a 3×5 lattice and names them in prose; **the only KEY names any
document writes are `body` and `weapon_r_1`.** Loom writes what it is given
rather than inventing the other nine.

**⚠ Two things to report rather than decide:**

- **`PT-1252` says eleven slots and its own lattice has twelve positions** —
  implant · head · hands / right arm · body · left arm / weapon R · belt ·
  weapon L / boots / weapon R · weapon L. **The key vocabulary wants a ruling.**
- **`EMBODIMENT-01` and `AUTHORED-CHARACTER-01` disagree on the value.** The
  record is `weapon_r_1: { item: …, fixed: false }`; the blueprint is a bare
  path. **So `integral` and `fixed-slot` — two of `ITEMS-08`'s three item kinds
  — cannot be expressed on a blueprint at all**, and a droid's built-in weapon
  is exactly that.
- **And nothing READS it in play yet.** The field is authorable; `strike()`
  still uses a hardcoded fist. **A separate slice.**

## 3 · `[requires]` and `[continues]` — built

**`new_package.dart` already said `[requires]` *"belongs in package
properties"*.** The gap was known, written down in a comment, and left open.
Both are in Package Properties now.

**⚠ `[requires].packages` is ordered and the order IS the precedence** — `§4`.
Written as given, **never sorted**.

**`[continues]` needed no ruling after all** — `§4` specifies it as one field,
`chain`, and `package_open` already reads it into `continuesChain`.

## 4 · ⚠ A sixth, found by looking again

**`cover`** — read by `package_open`, and `§4·1` puts it on the library tile.
**Written by nothing.** The first audit missed it because it looked at the
creature and at the manifest's *required* fields. **Closed.**

**And one that is neither:** **`format = 1`** — `§4` shows it and `PT-1366`
ruled it, and **`package_open` does not read it either.** Not the same defect;
a ruled field **nobody implements on either side**. *Reported.*

---

## 5 · ⚠⚠ The fix for one overflow found another, twice

**Adding two fields overflowed Package Properties by 136px.** So `DialogFrame`
scrolls its body — **which also closes `New Creature`'s 58px overflow, reported
at `PT-1425` and unfixed since.** One fix, every dialog.

**⚠ And making it scroll put `Save` below the fold**, where a tap lands on
whatever is at that point. **The actions are pinned now**, outside the scroll,
for the same reason the title is.

> **⚠ Third time this session: making a container scroll converts *content you
> cannot see* into *content you can click by accident*.** The dialogue panel,
> the option list, and now a dialog. **The rule that falls out: anything you can
> click must be laid out where it can be seen, and a scroll view is only safe
> for things you read.**

---

## 6 · Not done

**Doctrine, reaction and the door template**, all blocked on the same missing
thing. **Not the side panel.** And **equipment is authorable but not yet read
in play.**
