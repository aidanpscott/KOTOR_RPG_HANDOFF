# BUILD 173 — the sweep, a strref I shipped, and a Scan that cannot be tested

---

## 1 · ⚠⚠ `PT-1854` — 455 MARKERS RESOLVED, AND A CORRECTION FIRST

**`PT-1853` shipped eight rows reading `ImprovedSavingThrowsSpecific (951)`.**
951 is a `dialog.tlk` **strref**, not a name. My column rule was *"label if
present, else column 0"* — and `k2_iprp_savingthrow.2da` has **no `label`
column at all**: its columns are `name` (the strref) and `namestring`.

    I put an index in the book, in the exact place the index was
    supposed to be removed from — and pushed it.

Two fixes, and the second is the one that matters:

- the column is `label`, else `namestring`, else the first
- **a number is not a name** — a digits-only value is refused outright, so a
  column chosen wrongly cannot reach a page again **whatever the table**

Chapter Seven was reverted to its pre-`PT-1853` state and re-run clean.

**⚠ AND THE CHECK ITSELF WAS WRONG TWICE BEFORE IT WAS RIGHT.** It normalised a
marker and a resolved label to **different tokens**, and applied the marker
normaliser to **only one side** — so it reported differences that were its own.
Corrected to normalise both sides identically: **204 changed rows, 0 differing
in anything but a label.**

⚠ The margin's English is a table hint too — *"which save"*, *"which Defence
type"* — used the same way: a filter the blueprint must satisfy. That closed
the 27 rows a colliding subtype had refused.

**Remaining: 168 rows whose marker carries no subtype at all** — 163
Species-restricted, 3 appearance, 2 Alignment-locked, plus one Gender row whose
only readable column is a strref. They have **no index for a margin to check**,
so resolving them means reading the blueprint alone with nothing to verify
against. A different confidence level, named rather than swept in.

## 2 · ⚠ `PT-1855` — SCAN COMMITS TO ONE SENSE

Ruled: unfeated it commits to one sense, the player's choice; **`Vigil` removes
the constraint entirely.** *"The forced choice is what gives the feat real,
unambiguous value rather than a flat bonus."*

Both of Vigil's clauses are built — the better of both **and** free once per
round. A feat half-built is a feat whose price nobody can judge.

**⚠⚠ AND IT BEATS A SETTLED TOTAL RATHER THAN ROLLING AGAINST ONE.** My first
version made it an **opposed** check with a Stealth roll for the hider.
`AREA-FORMAT-01 §3b` carries *"the hider's total, which a finder must beat"*,
and `noticed()` already reads it that way. A rolled defence re-rolls a settled
number every time somebody looks — *"a second evaluation with the same numbers
is not a second chance."*

⚠ Found by going to wire the app against the existing hidden-creature fixture
and seeing it writes `stealth` on the **placement** — an area-format field, not
the blueprint's `[skills]` my check was reading. **The wrong source led to the
wrong shape, and the fixture said so before a single test ran.**

## 3 · ⚠⚠ AND THE APP HALF SHIPS UNEXERCISED, SAID PLAINLY

**A passive look takes 10.** So an active Scan only beats one on a roll above
ten — and **there is no configuration in which a Scan deterministically finds
what a passive look missed.** Any such test asserts a particular die.

⚠ And the existing hidden-creature bed cannot host one either: `two_enemies_test`
says so in **its own comment** — *"the concealed window is real but not
observable in this fixture"* — which I read only after building against it
twice.

The engine half has six cases, including the mutation that would hollow out
Vigil. The app half is reviewed and unexercised, and that is the honest state.

⚠ **A design consequence worth a ruling:** Scan is a combat Action because the
action economy is a turn — but **concealment mostly matters before a fight
starts.** As built, the thing Scan is for is largely out of its reach.

## 4 · ⚠ AND `_mySkill` IS GONE

`_rank` already did it, and had since `PT-1573`. I added the second at
`BUILD 162` without looking for the first. **Two answers to one question in one
file**, and the only reason it never disagreed is that both were right.

---

## Tests

    Lodestar   740 pass   (stealth_test +6)
    App        595 pass   (unchanged — see §3)

## Still open

- **Scan's reach** — combat-only, while concealment is pre-combat.
- **168 no-subtype markers** in `Armory` Five and Six.
- **A real target picker** — `PT-1847` · `§2`'s character screen · `Slice`,
  `Treat`, `Repair` unbuilt · the stealth field generator has no item.
