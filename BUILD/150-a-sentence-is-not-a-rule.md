# BUILD 150 — §4a was extracted all along, into the wrong shape

---

## 1 · ⚠⚠ THE FINDING: IT WAS NOT UNEXTRACTED

`AUTHORED-CHARACTER-01` has carried this since it was written:

> *"The log has recorded `item_unresolved: nothing applies it yet` since it
> was written… a player reading *'an upgrade on the gear you already have'*
> takes it and finds their weapon unchanged. **What it needs is `§4a`
> EXTRACTED** and a second offer on that screen."*

**`§4a` has been extracted since the extraction batch.** `two_weapon.toml`
ships **both** of its columns — as the document's own prose:

    later_with_the_melee_grant = "Hunter: Vibroblade ·  BOTH: a Double-Bladed Sword"

**That is a sentence.** Nothing can act on it, and nothing has. The gap was
never *unextracted*; it was **extracted into a shape no consumer could use**,
and the note naming the gap could not see the difference from outside.

`weapon_upgrades.toml` is the same table as **21 rows** — one per *(class,
condition, alternative)*, each carrying the weapons the grant hands over. Ten
of nineteen classes grant one.

    soldier-any-0     Soldier   any      Long Sword + Short Sword
    soldier-any-1     Soldier   any      Double-Bladed Sword
    duelist-hunter-0  Duelist   hunter   Vibrosword
    duelist-both-0    Duelist   both     Vibrosword + Vibroblade

**⚠ `two_weapon.toml` IS KEPT.** The prose is what a person checks the parse
against, and deleting the thing the structure was derived from is how a parse
becomes unfalsifiable.

## 2 · ⚠⚠ WHAT `BOTH` MEANS, SETTLED BY EVIDENCE RATHER THAN PREFERENCE

Two readings were available: **both professions**, or **the feat and the
grant**. It decides what ten classes hand a player, so it is not a detail.

**It is the feat and the grant.** Three independent reasons:

* **A character holds ONE profession.** The app's `profession` is a single
  value, not a list — *"Hunter and Veteran"* is not a state anybody can reach.
* **`Machinist`, `Duelist` and `Medic` each carry a `BOTH` clause with no
  `Veteran` clause at all.** Under the two-professions reading their `BOTH` is
  unreachable. **That settles it without needing the first reason.**
* The section's own title is *"IF THE PLAYER SPENDS THEIR LEVEL-1 FEAT ON
  `Two-Weapon Fighting`"*, and the second column is *"Later, with the melee
  profession grant."*

**It is written into `§4a` now**, because a table that gets extracted should
not need a reader to reconstruct the argument.

## 3 · ⚠ THREE ELLIPTICAL CELLS WRITTEN OUT — AND NO RULE CHANGED

    Veteran: one Blaster Pistol · BOTH: two          → two Blaster Pistols
    Veteran: one Heavy Blaster  · BOTH: two          → two Heavy Blasters
    … two Heavy Blasters or Long + Short             → Long Sword + Short Sword

Each is the **only** reading its own clause admits. **A table that is
extracted cannot be read by inference** — and a parser that resolved the
ellipsis would be guessing in the one place the document can simply say it.
The re-extract moved **those three strings and nothing else**, checked.

## 4 · ⚠⚠ TWO GUARDS, BOTH WATCHED FAILING

* **Nineteen class rows, or nothing is written.** `PT-1772`'s lesson one file
  over: a section that silently returns fewer rows than the document has is
  indistinguishable from a clean read.
* **Every weapon must resolve** — against `EQUIPMENT-01`'s base types, or
  against `§2c`'s disambiguation rows. Renaming one weapon in the document to
  `Heavy Blasterr` made it exit non-zero naming both the class and the term.

**⚠ AND THE SECOND GUARD FOUND SOMETHING BEFORE IT WAS FINISHED.**
`Heavy Blaster` — granted to four classes — is **not a base type**. `§4c`
lists it among the Pistol wield class, `EQUIPMENT-01`'s table has no such row,
and `§2c` resolves it to `g_w_hvyblstr01` at 200cr. **It is a catalogue item,
not a base type**, which is exactly what `item_disambiguation` exists for — so
the check resolves against both, the way the Equipment step already does.

## 5 · ⚠⚠ AND THE ANCHOR BIT AGAIN — THIRD SIGHTING

`§4a`'s heading is `## 4a · ⚠⚠ IF THE PLAYER…` — a **middle dot**, not a
period. My anchor read `^## 4a\. ` and matched nothing, **while the error
message said the HEADER had moved.** A check that reports the wrong cause is
one slice of chasing the wrong thing.

    BUILD 147   a number-word map that stopped at ten
    BUILD 148   a heading anchor that required one ⚠ where there were two
    BUILD 150   a heading anchor that required a period where there is a dot

**Same family every time: a check keyed to a SPELLING of its subject.** The
anchor is `^## 4a\b` now, and the message names both possible causes rather
than asserting one.

## 6 · ⚠ WHAT IS NOT BUILT, NAMED RATHER THAN IMPLIED

**The second offer on the Equipment screen.** `weapon_upgrades.toml` is the
data half — the half `AUTHORED-CHARACTER-01` named as the blocker — and
**nothing in the app reads it yet.** A player taking the Hunter grant today
still gets `item_unresolved`. The screen work is its own slice and is not
pretended to be done here.

---

## What ran

    Lodestar   668 tests   exit 0
    Loom       263 tests   exit 0
    app        533 tests   exit 0
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings
    check_shelf             ✓ 25 rules files identical
    check_extracts          1 stale — the standing event_kinds one

The base-rules inventory moved with it: **24 files / 2,592 records → 25 /
2,613.**

## Heads

    Lodestar        30954f0   (unchanged)
    Loom            c48e909   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   db5b647
    MAIN_WORK       1407db2

⚠ The shelf gained `weapon_upgrades.toml` and `two_weapon.toml` was replaced
with the three expanded cells. Diffed against the installed package first —
and `check_shelf` named the new file as **NOT INSTALLED** before it was
copied, which is the check doing its job on a file that had never existed.
