# 43 · `PT-1452` — the item blueprint, and the trooper fires its rifle

**614 tests green** — Lodestar 282 · Lens 4 · Loom 114 · app 214.
`Lodestar 70a1107` · `Loom a66960c` · `app 1407b4e` · `MAIN_WORK 9d3ca99`.

**`BUILD/42`'s stop is answered and closed.** Four repositories, because the
chain runs through all of them.

---

## 1 · The extraction — and the array was worse than untyped

**`PT-1452` called the positional array a defect in the extraction rather than
an interface, and it was.** The old extract's own notes admitted the gap:
*"naming them would require a per-section schema this pass did not establish."*

**⚠⚠ AND IT DID NOT ONLY LACK NAMES — IT SILENTLY SHIFTED.**

    Stun Baton   ['1', 'bludgeoning', '20 / ×2', '1']     ← four
    Short Sword  ['1d6', 'piercing', '20 / ×2', 'yes', '1'] ← five

`§2`'s header is `Damage | Type | Threat | Balanced | Attacks`. **The Stun
Baton's `Balanced` is an em-dash and the extractor DROPPED it**, so the
trailing `1` is **`Attacks` sitting in `Balanced`'s place.** A reader indexing
by position would have read `balanced = "1"` and `attacks = missing`.

> **`TRACE-83`'s position-as-identity, in our own data.**

**Every cell is kept now and an em-dash becomes null.** `balanced` and
`may_be_paired` are **three-state** — true, false, or null — because *"nobody
said"* is not *"no"*.

**Lightsabers carry two damage columns and `§4b` picks one** — *"Use K1's. Our
campaign is 3956 BBY and K1 is the era."* So `damage` is K1, under the same
name every other section uses, and K2's survives as `damage_k2` rather than
being discarded.

34 rows, five sections, count unchanged. `base-rules` regenerated.

---

## 2 · The format — one field that matters

    [item]
    name = "Blaster Rifle"
    base = "blaster-rifle"

**An item names a base type; the base type carries the dice.** That is
`baseitems.2da` and `.uti` — a `.utc` references a `.uti`, and a `.uti` names a
base item row. **Both halves were already in the corpus** and the join had
never been stated.

**⚠ AN ITEM CARRIES NO DICE, DELIBERATELY.** One that restated them could
disagree with `EQUIPMENT-01`, and **a second copy of a number is a second
answer** — the argument `PT-1437` made for deriving `startsFight` from events.

**⚠ AND `base` IS REQUIRED.** An item without one carries no dice and no
threat, so nothing could resolve an attack with it. `§4`'s loud failure; the
alternative is a weapon that silently does nothing.

`blueprints/items/` was **the third folder `BUILD/34` named with no format
behind it.** `doctrines/` closed at `BUILD 35`; **`doors/` is still open.**

---

## 3 · ⚠ The join refuses rather than guesses

`EQUIPMENT-01`'s Ion Blaster is **`"1d4 + 1d10 vs droid"`** — a conditional
second die the resolver has no shape for.

> **Taking the leading `1d4` would arm a weapon that is QUIETLY WRONG against
> droids.** That is the silent-wrong-answer family this project keeps paying
> for, so it comes back as a refusal carrying the string.

**And what can be read but not modelled comes back NAMED.** A threat of
`"19–20 · on-hit stun"` yields `critOn: 19` and reports the stun as not
modelled. **An unstated threat takes `Weapon`'s own defaults — nothing is
invented**, and the Ion Rifle states none.

---

## 4 · Loom writes one, and the bed's rifle was authored by the Builder

**⚠ THE BASE TYPE IS CHOSEN, NOT TYPED** — the roster is closed, so a value the
reader would refuse is not typeable. Same argument as `DOCTRINE-FORMAT-01
§3`'s closed match vocabulary.

**⚠ THE PATH IS TYPED WHOLE**, because `PACKAGE-NAMING-01` makes the path the
identity. A dialog taking a name and inventing a folder would be choosing an
identity on the author's behalf. **Two levels are enforced** — `TRACE-90`
measured that as collision-free across 9,178 items.

**⚠ AND THE BED'S RIFLE WAS NOT HAND-WRITTEN.** `Loom/tool/author_bed_rifle.dart`
runs `ItemWriter` against the real shelf, so **the artifact and the tool are
tested by the same act** — `PT-1346`: a coder writing an artifact produces the
artifact and tests nothing.

---

## 5 · ⚠⚠ Two hardcoded weapons went, not one

    play_screen.dart  the PLAYER   unarmed    1d3   ← still unarmed, §6
    fight.dart        the TROOPER  vibroblade 1d6   ← GONE

**The enemy's was the stranger and it is the one that is fixed**: a creature
holding a blaster rifle attacked with a **melee weapon at range**, invented by
nobody's ruling. It is now whatever the blueprint says — **1d12, energy,
threatening on 19–20.**

**⚠ `unarmed` SURVIVES AS A NAMED FIXTURE.** `EQUIPMENT-01` has 25 base weapons
and **no unarmed row**, so those dice are ours. `PT-1425` named it a
placeholder and this did not change that — **it is defined once**, so the next
person searching for invented numbers finds one hit.

**⚠ AND `fight_test`'s DICE WERE TUNED TO THE INVENTION.** Removing the
vibroblade made a damage face of `4` unrollable on unarmed's d3 — **the test
telling the truth.** It supplies the weapon a trooper actually has now.

---

## 6 · ⚠ The player: it is TWO fixes, and the second is not small

**One of them is done.** The lookup is shared — `f.weapons[f.playerTag] ??
unarmed` — so the day the player has an equipment reference, **the seam needs
no second path.**

**The second is in chargen, and it is blocked on something already open.**
`[equipment]` names a **path to an item blueprint**, and chargen's Equipment
step produces **an item's name and price** from the class arrays. To arm the
player, those prose names must resolve to blueprint paths — and `STATE.md`
already records that **only 18 of 41 array names resolve to exactly one
catalogue row**, with `§2c` disambiguating 14.

> **So: two, and the second is the same unresolved-names problem that keeps
> Route 2's purse unoffered. Arming the player is not a seam change.**

---

## 7 · ⚠ What I am NOT doing here

**`PT-1453` is read and not acted on.** It says `BUILD 41` fixed the path it
tested and not the one the request quoted, and that persisting the log created
two defects. **My reading of the third path:** `_endFight` and `_enter` both
persist now, but **leaving the SCREEN with `esc` goes through neither** — it
returns to the package menu without ending the encounter, so nothing is
written. That is a third exit I did not find.

**It is a different slice and I have not started it**, because widening this
one is exactly what `PT-1453` says went wrong last time.

**And the viewport hygiene is deferred, deliberately.** It is 23 one-line
additions and it is cheap — **but it is a sweep across two repositories, and
folding it into a four-repository feature slice makes both harder to review.**
`PT-1453`'s lesson is that breadth outran testing; this is the same shape.
**Its own small slice.**
