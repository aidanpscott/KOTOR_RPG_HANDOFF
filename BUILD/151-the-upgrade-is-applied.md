# BUILD 151 — the upgrade is applied, and the sentence every save carried is gone

---

## 1 · ⚠⚠ THE DEFECT `AUTHORED-CHARACTER-01` HAS CARRIED SINCE IT WAS WRITTEN

> *"The log has recorded `item_unresolved: nothing applies it yet` since it was
> written; **the Equipment screen said nothing**, and a player reading *'an
> upgrade on the gear you already have'* takes it and finds their weapon
> unchanged."*

**It is applied now.** The screen offers the alternatives, the player picks,
and the save records **which**.

    the profession grants one of these, and now you choose
      ▸ TAKES THE CLASS'S OWN melee UPGRADE
        it replaces the weapons in your array
      and now you choose which
        ▸ Long Sword + Short Sword      2 objects
        ▸ Double-Bladed Sword           one weapon — wield 3, and it IS the pair

**⚠ ONE ALTERNATIVE IS NOT MADE INTO A CHOICE.** A class with a single option
is handed it; making a player confirm a menu with one item is a step that only
ever has one answer.

**⚠⚠ AND OK WAITS FOR THE PICK.** Taking the upgrade without saying which is
**the state the old screen was permanently in** — the offer resolved to
nothing and the save said so afterwards.

## 2 · ⚠⚠ IT REPLACES THE ARRAY, WHICH `§4a` STATES ONCE AND PLAINLY

> *"The `Two-Weapon Fighting` table is an **ALTERNATIVE** to the array, not an
> addition to it. That is true of every row and worth stating once."*

So the payload carries the upgrade's weapons **instead of** the array's, and
the main hand is the **first weapon named** — `§4a`'s own balance note:
*"both upgrade rows put the UNBALANCED weapon in the MAIN hand — `Long Sword`
main with `Short Sword` off."* The table's order is the rule, so it is kept.

    items          [items/weapons/long-sword, items/weapons/short-sword]
    weapon_r_1     items/weapons/long-sword
    weapon_l_1     items/weapons/short-sword
    weapons_from   upgrade
    upgrade        soldier-both-0

## 3 · ⚠⚠ READ FROM `WEAPON-MATRIX-01`, AND THE DIFFERENCE IS THE FINDING

`PT-1780` ruled the matrix authoritative. **35 rows against `§4a`'s 21**, and
the fourteen new ones are exactly what `§4a` got wrong:

| | `§4a` | the matrix |
|---|---|---|
| **Soldier · Scout · Bounty Hunter** | one row, called `any` | **a profession-only row `§4a` never carried**, and `§4a`'s cell was the `BOTH` value |
| **Agent · Treasure Hunter** | `—` | **a full grant, both columns** |
| **Saboteur · Smuggler · Duelist** | — | **a third alternative each** |

**⚠⚠ AND `both` REPLACES THE PROFESSION ROWS RATHER THAN ADDING TO THEM.** The
`Scout` takes a `Long Sword` from `Hunter` and a `Double-Bladed Sword` **only
with the feat as well** — so with the feat the Long Sword is not also on offer.
A row is not *the profession row plus a feat*.

**⚠ `and` JOINS AND `or` SEPARATES**, which one cell needed: the `Agent` and
the `Treasure Hunter` get two pistols **and** a sword pair — **four weapons,
not a choice between two.** Reading `and` as an alternative would have halved
what two classes are handed.

`§4a`'s grant column is rewritten from the matrix cell for cell and carries a
banner saying it is **derived** and that the matrix wins if they disagree
again. The six Force classes are untouched: `§2` gives them no `Hunter` or
`Veteran` column at all, because `PT-702` makes a real lightsaber a **campaign
event** rather than a profession grant.

## 4 · ⚠ WHAT THE SCREEN KNOWS, AND WHY IT ALREADY KNOWS IT

Both facts the lookup needs are **settled by the time the screen opens**: the
profession came from Backstory, and **Feats precedes Equipment in the hub**, so
whether `Two-Weapon Fighting` was taken is a decided question rather than a
guess. No re-ordering was needed and none was done.

**⚠ A DROID IS OFFERED NOTHING.** `WEAPON-MATRIX-01 §3` carries the two droid
arrays and gives them no `Hunter` or `Veteran` column, and `PT-1713` closes
melee to every chassis besides. Offering one would be the screen inventing over
two rules.

**⚠ AND `Conscript` AND `Acolyte` STILL SAY NOTHING APPLIES YET**, correctly.
One is *"the best armour your Armour Proficiency allows"* and one is a robe
swap; **the matrix answers neither**, and claiming they resolved would be worse
than saying they did not.

## 5 · ⚠⚠ I REWROTE THE WRONG THIRTEEN ROWS, AND CAUGHT IT BY READING THE OUTPUT

The first attempt at the `§4a` edit used a regex over the whole document. It
matched **`§4`'s per-class array table** — same shape, first column a class
name — and rewrote those rows instead.

**Caught by reading what it printed**, reverted with `git checkout`, and redone
**bounded to `§4a`'s own line range**. A regex over a whole document is not a
line-range edit, and this document has several tables whose first column is a
class name.

## 6 · ⚠ TWO COUNTS MOVED WITH THE RULES

    base types   36 → 37    PT-1780 gave `Heavy Blaster` a row: §4c lists six
                            pistols in the Pistol wield class and the table
                            carried five, so four classes were granted a
                            weapon nothing could resolve
    records    2,613 → 2,628

A case now asserts that **every weapon every upgrade names resolves to a base
type** — the guard that would have caught the `Heavy Blaster` gap before a
player met it.

---

## What ran

    Lodestar   668 tests   exit 0
    Loom       263 tests   exit 0
    app        546 tests   exit 0   (+13)
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings
    check_shelf             ✓ 25 rules files identical

Mutation-checked three ways: the upgrade never replacing the array, `both`
ignored, and OK not waiting for a pick — each kills at least one case.

## Heads

    Lodestar        30954f0   (unchanged)
    Loom            c48e909   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   f26d62f
    MAIN_WORK       79eaae8

⚠ The shelf's `equipment.toml`, `two_weapon.toml` and `weapon_upgrades.toml`
were replaced. Diffed against the installed package first; those three were
the only differences.
