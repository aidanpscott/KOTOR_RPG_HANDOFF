# BUILD 174 — a predicate that could not go false

---

## ⚠⚠ `PT-1856` — `Tester`'s DEFECT, AND MY COMMENT CLAIMED THE OPPOSITE

`BUILD 171` said the action keys *"vanish when there is nothing left to
spend."* **They never did.**

The legend gated on `budgets.anythingLeft`, which stays true while **any**
budget survives — and `gearSpent` **has no caller anywhere**, the zero-callers
hole `budget_strip.dart` already documents. So `anythingLeft` **cannot go false
on a player's turn at all**, and the legend went on offering five keys that
could only refuse.

**⚠ THE RIGHT QUESTION WAS ALWAYS THE NARROWER ONE.** Every one of the five
costs the **Action**, so `canAct` is what decides whether naming them is an
offer or a lie. The end-turn sentence keeps `anythingLeft`, because it is about
the whole budget rather than about these keys.

**⚠ A PRE-EXISTING HOLE THE LEGEND RAN INTO AS A NEW CONSUMER**, and the shape
is one this corpus knows in another hat: **a predicate that cannot go false is a
guard that cannot fail.** It was harmless while nothing read it — `PT-1847`'s
filter was harmless while effects were a no-op, and `BUILD 163`'s duplicate
check was harmless while only the player moved. **Three in this session, all
dormant until a new consumer arrived.**

Guarded with the case that reproduces it — **Disengage spends the Action and
nothing else**, which is exactly why it separates the two questions — and the
guard was watched failing against the old gate.

---

## Tests

    App  596 pass

## Still open

- **Scan's reach** — combat-only, while concealment is pre-combat (`BUILD 173`).
- ⚠ **`spendGear` has no callers**, so the Gear budget can never be spent.
  Named here as the cause of this defect; the Gear action itself is unbuilt.
- **168 no-subtype markers** in `Armory` Five and Six.
- **A real target picker** — `PT-1847` · `§2`'s character screen · `Slice`,
  `Treat`, `Repair` unbuilt · the stealth field generator has no item.
