# BUILD 164 — a refused swing, and a panel with no spare vertical

---

## 1 · ⚠⚠ MY OWN CLAIM WAS WRONG, AND `Tester` FOUND IT

`BUILD 162` shipped `_revealMe()` at the top of `_playerStrikes` with this:

> *"⚠ AFTER THE TURN CHECK AND BEFORE THE SPEND, so a refused swing does not
> reveal — nothing was thrown."*

**True of exactly one of the four refusal paths.** *Already acted*, *a droid
with nothing to swing* and *out of reach* all revealed the player for a swing
that never happened.

**⚠ AND IT IS THE COMMON CASE, NOT AN EDGE ONE.** Hiding **spends the Action**,
so hide-then-attack in the same turn is refused at `canAct` **every single
time**. The one pattern a player would try first.

The reveal now sits beside `spendAction()`, on the far side of every refusal.
**The line three comments above it already stated the rule** — *"nothing is
spent and nothing is persisted. There is no crossing, no damage and no ledger
kind; the swing was not taken."* Revealing is one more thing that must not
happen when the swing was not taken.

## 2 · ⚠ AND HIDING NOW ENDS WITH THE FIGHT, AND AT A DOOR

Hidden is opposed against the enemies of **one encounter**. Carrying it past
the end of that fight, or into the next room, would be a condition nothing
could ever end — the same argument `ledger.dart` gives for the `transient`
lifetime, without the reload.

`_endFight` writes the `condition-expired`; the area change clears the flag,
because **the event belongs to the fight that ended** and an arrival has none.

## 3 · ⚠⚠ A PRE-EXISTING PANEL OVERFLOW, FOUND AND NOT FIXED HERE

Driving a fight to its end overflows `PartySidebar`'s column by **7.4px** at
scale 2.8 in a short pane. With `entries=2, turnOrder=2, forceNote=null`, the
heading and the **turn strip alone** exceed the available height: the strip is
not flexible and the list is.

`BUILD 44` already states the intended rule — *"a fight with six in it shortens
the LIST rather than the board"* — so the shape of the answer exists; **which
part of the panel yields is a layout decision rather than mine to take inside
this slice.** Reported.

**⚠ AND MY FIRST ATTRIBUTION CHECK WAS INVALID.** I removed the indicator to
see whether it caused the overflow, and the test then failed **earlier**, at
the assertion that looks for the indicator — so it never reached the overflow
at all and reported a clean zero. A control that never hides overflows
identically. *A check aimed at the wrong subject*, in my own diagnosis, and the
clean zero is exactly the shape this corpus warns about.

## 4 · ⚠ THE INDICATOR MOVED TO THE NAME LINE

Which is the loudest line a row has and **adds no height** — prudent given the
panel has none spare, and it satisfies `PT-1108`'s *"clearly visible"* better
than a dimmed word in the dot-joined line ever did.

⚠ The gap beside it is a `SizedBox` and not spaces in the string: padding baked
into the data makes the word a different word to everything that looks for it,
and `find.text('hidden')` is what the acceptance reads.

---

## Tests

    App  585 pass   (hide_test +1 regression · companion +1)

The regression test reproduces `Tester`'s exact path — hide, then swing in the
same turn — and fails against the old placement.

## Still open

- ⚠ **The panel overflow above**, `BUILD 44`'s rule unapplied to the strip.
- **Does casting reveal?** `PT-1682` says *the shot*; a power aimed at an enemy
  *"counts as your declared attack"*, so almost certainly yes — but a power
  aimed at an ALLY is unruled, and `_cast` reveals nothing today.
- `§2`'s character screen (the click, `PT-1443`'s) · `Dash`/Hustle unbuilt ·
  `Scan`, `Slice`, `Treat`, `Repair` unblocked and unbuilt · the stealth field
  generator has no item.
- ⚠ The `whole_loop_test` flake, one sighting at `BUILD 162`.
