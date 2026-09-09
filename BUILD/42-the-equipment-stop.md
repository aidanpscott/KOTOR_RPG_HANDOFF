# 42 · ⚠⚠ STOP — the equipped weapon cannot be read

**Nothing was built. No code changed.** All six repositories are clean at the
heads `BUILD 41` left them.

**What was being built:** read the weapon a creature has equipped at the seam
and use it in `strike()`, so the bed's trooper stops fighting with a weapon
nobody authored.

**What stopped it: the equipped value names something that does not exist, and
nothing defines what it would contain if it did.**

---

## 1 · What the author actually wrote

    [equipment]
    weapon_r_1 = "items/weapons/blaster-rifle"

**The seam already has this.** `openCharacter` reads `[equipment]` into
`AuthoredCharacter.equipment` — a `Map<String, String>` — and `combatantsIn`
has it in hand. **Nothing is missing on the reading side of the blueprint.**
The wall is one step further in: *what does that string point at?*

---

## 2 · ⚠ It points at a file that does not exist, and there is no format for it

**`PACKAGE-NAMING-01` is unambiguous about what a `path` is:**

> **`path`** — *identity of a **definition** — and where it lives.*
> *"it **is** a path, so the word needs no explaining — and it makes **identity
> and location the same thing**, which is where findability comes from."*

Its own worked example is `items/weapons/echani-vibroblade`. And
`PACKAGE-FORMAT-01 §3`'s layout has `blueprints/items/` among the nine
categories.

**So `items/weapons/blaster-rifle` names `blueprints/items/weapons/blaster-rifle.toml`.**

    ⚠ The bed has no blueprints/items/ folder at all. Six files, none an item.

**And there is no format for one if it were there.** Checked:

| | |
|---|---|
| Readers in `Lodestar` | `openCharacter` · `openArea` · `openDoctrine` · `openConversation` · `open` — **no `openItem`** |
| Documents defining an item blueprint's fields | ⚠ **none.** No file in `HANDOFF/docs/` mentions `blueprints/items` or an `[item]` table |

> **⚠ THIS IS `BUILD/34`'s STOP AGAIN, AND IT IS THE THIRD INSTANCE.** A folder
> in `PACKAGE-FORMAT-01`'s layout with no format behind it. `doctrines/` was
> the first and `DOCTRINE-FORMAT-01` closed it at `BUILD 35`; `blueprints/doors/`
> is still open; **`blueprints/items/` is this one.**

---

## 3 · ⚠ And the thing that looks like an answer is the wrong shape

**There IS a record with that id** — in the generated rules, not in the package:

    base-rules/rules/equipment.toml
    id = "blaster-rifle"   name = "Blaster Rifle"
    section = "Ranged"     values = ["1d12", "energy", "28 m", "19–20"]

**The damage is right there, and I did not use it. Three reasons, and the first
is the one that matters:**

**⚠ It would make `path` mean two different things.** `PACKAGE-NAMING-01` makes
identity and location **the same thing**; resolving a path by throwing away
`items/weapons/` and looking the last segment up in a flat catalogue makes the
first two segments decorative. **A path that is sometimes a location and
sometimes a lookup key is not a path.**

**The shapes do not match either.** The path is two-level by ruling — `TRACE-90`
measured two levels as collision-free across 9,178 items. `equipment.toml` is
flat, keyed by a bare id and grouped by a `section` that is not `weapons`.

**And `values` is an untyped positional array whose shape changes by section.**
`Ranged` carries four entries; `Lightsabers` carries five in a different order.
**Nothing in the data says which index is damage** — `EQUIPMENT-01 §4`'s table
header does, in prose, and **nothing in the app parses that file today.** A
reader would be inferring a schema from a document's column order.

**⚠ Any of those three could be answered by a ruling. None of them can be
answered by me**, and picking one is exactly the step-4 error `PT-1349` names.

---

## 4 · ⚠ WHAT IS MISSING — as a need

> **A way for the engine to answer *"what dice does this weapon roll"* from
> what an author wrote.**

**Three unknowns sit under that, and they are separable:**

1. **What an `[equipment]` value REFERS TO.** A blueprint file in the package,
   or a record in the rules catalogue. `PACKAGE-NAMING-01` says the first; the
   only thing that exists is the second.
2. **If a blueprint: what an item blueprint contains.** There is no document
   and no reader. Same shape as `DOCTRINE-FORMAT-01` before `BUILD 35`.
3. **If a catalogue record: how a positional `values` array is read**, given
   its shape depends on `section` and only `EQUIPMENT-01`'s prose says which
   column is which.

**And one that is not mine either:** whether a creature may equip something the
package does not ship — the trooper's rifle is a base-rules record, and
`tester-probe` already showed a package getting `base-rules` without declaring
it (`Tester`'s U3).

---

## 5 · ⚠ What was NOT done about it

**Nothing.** No file in any repository changed.

- **The two hardcoded weapons are untouched.** I did not swap the dice, and I
  did not use the item's name while leaving the dice hardcoded — **that would
  make the log say `blaster-rifle` while rolling `1d3`, which is the same
  contradiction one layer deeper and harder to see.**
- **No `openItem` was written**, no `[item]` shape proposed, and no resolution
  from a path to `equipment.toml` added.
- **No test was written**, because there is nothing to assert.

---

## 6 · ⚠ What was learned about a spec

**`PACKAGE-NAMING-01`'s *"identity and location are the same thing"* is
load-bearing in a way nothing had needed before.** It reads as a convenience
argument about findability. **It is the line that makes the catalogue reading
illegitimate**, and without it the shortcut would have looked reasonable.

**And the brief's description was half right, which is worth correcting because
it changes the size of the fix.** The trooper does not swing a fist:

    play_screen.dart:694   the PLAYER   Weapon('unarmed',    1d3)
    fight.dart:107         the TROOPER  Weapon('vibroblade', 1d6)

**Two hardcoded weapons, not one — and the enemy's is the stranger of the two:
a creature holding a blaster rifle attacks with a melee weapon at range.** Any
ruling has to cover both, and the player's has no `[equipment]` to read at all
— the chargen Equipment step resolves an item's **name and price**, never dice.

---

## 7 · The rest of the prompt

**`PT-1451` acknowledged** — `check_derived`, `check_absence_claims` and
`check_stale_claims` exit 2 on zero scope. ⚠ **And the trap in verifying it is
the same family as the bug**: piping through `tail` and echoing `$?` reports
**`tail`'s** status, not the script's. `set -o pipefail`, or check
`${PIPESTATUS[0]}`. **This slice's own audit ran them bare for that reason** —
by luck rather than by knowing, and it is worth writing down.

**The viewport re-verification is sized in the reply**, and the short version
is that **the side panel is not among the suspect claims.**
