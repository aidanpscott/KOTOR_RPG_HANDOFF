# BUILD 55 — `PT-1475`: the producer

**Chargen writes a path to an item blueprint. 23 of 28 arrays arm a character.**

---

## What it writes

    equipment = {
      route = "standard", credits = 100,
      items = ["items/weapons/blaster-rifle"],
      weapon_r_1 = "items/weapons/blaster-rifle",
    }

The same shape a trooper's blueprint uses — `PT-1452`, always, no second form.
Verified end to end: the producer's output goes through `equippedFrom`'s three
hops and comes back **Blaster Rifle, 1d12**.

## ⚠ It matches exactly and refuses rather than normalising

Ten of the eleven weapons the arrays name are the **exact** name of a base
type. A matcher that stripped hyphens and case would resolve the eleventh —
**and would also quietly resolve the next name that only looks close**, which
is how a Remote ended up in Dockworker's Treads.

| | |
|---|---|
| **23** arrays arm a character | |
| **1** is the Brawler's `NONE` | a value, not a failure to resolve one |
| **4** refuse | ⚠ one hyphen |

`EQUIPMENT-01` spells the base type **`Hold-Out Blaster`**; the arrays **and the
item catalogue** both spell it **`Hold Out Blaster`**. Two documents against
one. Agent and Medic, organic and droid, are the four. The test asserts the
**current** state, so correcting it turns red rather than passing silently.

⚠ **NEED, and it is one character.** Which spelling is right is yours — the
catalogue row is `g_w_hldoblstr01`, unambiguous, 100cr.

## ⚠⚠ And the log is the durable thing

The first version wrote the reference into `recordFromChoices` and **not into
the event** — and `ledger_test`'s replay caught it inside the same run. The
projection rebuilds `equipment` from the event verbatim, so **a record written
past the log does not survive a save.**

There is one `equipmentPayload()` now, and the record and the event both call
it. They cannot drift.

## `TEST 008` — a taken grant names which item

`taken: "item"` named nothing at all. It now records the item, its `resref`
where `§2c` disambiguates, its cost and its kind.

⚠ **And D3 from the log side:** an item taken where **no grant row resolves**
now writes `item_unresolved` — *"an item was taken and no grant row resolved
for this profession — nothing was added"* — rather than implying an item
arrived. `Tester` took the grant, nothing changed, and the log said
`taken: "item"` with no item. It cannot say that any more.

⚠ **The offer itself is still wrong and is NOT fixed here.** `§4a`'s label
names Soldier, Scout and Duelist and a Jedi Guardian is none of them, so the
screen offers a grant that does not apply. That is a selection defect in which
grant reaches which class — a separate slice, and the log now makes it visible
in any save it happens in.

## `item_disambiguation` has its first reader

`PT-1463` found it shipped and read by nothing. `§2c` answers *"which row each
array means"*, which is exactly what the Equipment step must answer to price
what it hands you — Blaster Carbine is 35cr and 500cr and `§2c` says which.
Cost is **null** where the catalogue is unambiguous: absent rather than
invented.

## Tests

**666 green** — Lodestar 297 · Lens 4 · Loom 119 · app 246.

Nine new, including the whole chain end to end. Verified red with the producer
reverted.

---

## ⚠ What a conditional-damage model would need — asked, not built

The Ion Blaster stays unarmed and should. `1d4 + 1d10 vs droid` is refused
rather than truncated, and that is asserted.

Four things, and the first is the only one that is cheap:

1. **A damage expression that is a LIST of terms, each with a condition** —
   `1d4` unconditional plus `1d10 when target.isDroid`. `Weapon` today is
   `damageDice`/`damageSides`/`critOn`: three scalars, so there is nowhere to
   put a second term at all.
2. **A target predicate the engine can evaluate.** `vs droid` needs the defender's
   KIND at the moment of the roll. `Combatant` carries handle, dexModifier,
   constitution, vitality, budgets and role — **it does not know whether it is
   a droid.** `PT-1474`'s `targets` column is the same fact from the other
   side, and neither is wired to a combatant.
3. **A grammar, and a refusal that survives it.** `EQUIPMENT-01` writes this in
   prose — `1d4 + 1d10 vs droid` — and there is exactly one such row today, so
   a parser would be inferring a language from one example. `PT-1452`'s rule
   must hold: anything the grammar does not cover is refused, not guessed.
4. **A damage line that can say why.** `PT-1326` renders one derivation;
   a conditional roll produces two, and *"1d10 because it is a droid"* is the
   part a player needs.

⚠ **The scoped negative that decides the cost:** `1d4 + 1d10 vs droid` is the
**only** conditional damage in 36 base types. One row, four structural changes
— and `targets` is already the same idea unmodelled, so whoever builds it
should build both.

## Still open

- ⚠ One hyphen: `Hold-Out Blaster` vs `Hold Out Blaster`. Four classes.
- ⚠ `§4a`'s grant offer reaching classes it does not name.
- `equipment.section` — a value used as a key.
- 48 cells where a citation is load-bearing in a sentence — a person reads
  those, and you said you will.
