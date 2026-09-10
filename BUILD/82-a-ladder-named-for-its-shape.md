# BUILD 82 — `PT-1547`: a ladder named for its shape

**849 green** — Lodestar 389 · Lens 5 · Loom 131 · app 321.

---

## ⚠⚠ `noble` WAS NOT AN AVAILABLE NAME, AND IT IS THE WORST ONE I COULD HAVE PICKED

It is one of our **nine upbringings** — beside Bastard, Orphan, Outcast,
Peasant, Slave, Street Urchin, Soldier's Child and Unknown — and `PT-705` rules
that **an upbringing grants nothing.** Its `grants` field is null **by design**,
and `PT-1385` already had to warn an agent not to read that null as missing
data.

> **The one identifier that must never appear beside a bonus is the name of the
> thing ruled to grant none.**

**A value used as a key, ninth in this corpus.**

## ⚠ AND `PT-1544`'s OWN WORDS SAID THE ANSWER

*"a defence track is a **NAMED LADDER** classes point at."* **A ladder named for
a class is not a named ladder** — it is a class's copy that a second class
borrows, which is precisely what the ruling was written to prevent. **I read
that structure out of the games and then named the result after a class
anyway.**

    hold-three-then-two   the irregular one — endpoints only, interior unread
    step-every-two        the linear one — computed from the stated rule

⚠⚠ **AND THE OFFSET MOVED TO THE BINDING.** There is now **one** irregular
ladder and a class that points at it `+1`, rather than two ladders that must be
kept in step. **The column is the object and the class is a pointer**, which is
what `classes.2da.armorclasscolumn` does.

## ⚠⚠ IT IS **TWO** OF OUR CLASSES, NOT THREE — correcting `PT-1544`'s count

**We do not ship a Noble class.** Our nineteen base classes are Soldier, Scout,
Smuggler, Bounty Hunter, Engineer, Marksman, Machinist, Agent, Treasure Hunter,
Medic, Brawler, Duelist, Saboteur and the six Force ones — **and `noble` in our
data is an upbringing.**

**RCR's Noble table is EVIDENCE for the ladder's values; it is not a binding.**
So `soldier` and `jedi_consular` point at ladders and **seventeen point at
nothing**, not sixteen.

⚠ **The RCR read is still owed, and `f.42` fills THE LADDER, not a class.**

---

## ⚠ AND THE SWEEP YOU ASKED FOR — 2,433 identifiers, two hits, both correct

`scripts/check_coined_names.py` compares **the names this project coins**
against every `id` our extracts already own.

⚠ **IT IS NARROW ON PURPOSE.** A class id used as a **key into** the class data
is correct and common — `defenceTrackOf` **must** be keyed by `soldier` and
`jedi_consular`. **What it checks is the left-hand side of a definition**, where
we are naming a new thing rather than pointing at an existing one.

⚠ **Its coining sites are listed by hand, and that list is its own scope line.**
A site nobody adds is a site nobody checks — printed rather than implied.

⚠ **Controlled:** with `noble` restored it reports
*"'noble' names a defence ladder in combat.dart:542 — AND IT IS ALREADY AN id IN
upbringings.json"* and exits 1.

**Result on the current tree: nothing we coin is already ours.**

---

## ⚠ EVERYTHING ELSE IS UNDISTURBED, as asked

- an offset from nothing is nothing
- the Soldier's ladder clamps rather than extrapolating
- `bonusAt` does not interpolate — a level-7 Consular gets no class term
- zero is a value, with an explicit-zero track tested
- the rest of the roster is left alone
- the Saboteur points at the Smuggler's rows rather than copying them

## Still open

- ⚠⚠ **The irregular ladder's interior** — an RCR Chapter 3 read; `f.42` fills
  the ladder.
- ⚠ `PT-1540`, `PT-1542`, `PT-1509`'s perception half, `PT-1532`, `PT-1537`.
- ⚠ `tester-probe`'s failure node; no `unlink` button; `PT-1484`, `PT-1485`,
  effect columns, 45 annotation cells.
