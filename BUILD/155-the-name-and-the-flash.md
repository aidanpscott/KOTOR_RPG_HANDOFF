# BUILD 155 — the name, the flash, and a deferral whose reason has expired

---

## 1 · ⚠⚠ THE DEFERRAL STANDS. ITS STATED REASON DOES NOT.

> *"PT-1631 already established a henchman can't even be authored yet — no
> role field on a blueprint would let one be placed to check a visual
> distinction against."*

**A henchman is authorable today**, and has been since `PT-1735`:

    [[contents]]
    tag  = "mate.a01.01"
    from = "characters/mate"
    at   = [1, 1]
    role = "henchman"          ⚠ accepted by area_open's _placeableRoles

`companion_test` and `fight_test` both place one. **The field is on the
PLACEMENT, not the blueprint** — which is exactly what `PT-1735` decided and
why `PT-1631`'s reading was true when it was written and is not now.

**⚠ THE RULING IS UNAFFECTED AND I AM NOT ARGUING WITH IT.** Deferring a
visual distinction until henchmen are real content is right either way. What is
worth correcting is the **reason**, because *"we can't check it"* is the kind of
reason that keeps something deferred after the blocker is gone — which is
`PT-1718`'s shape exactly: ruled, blocked, and never re-checked once the block
lifted.

## 2 · ⚠⚠ AN ENTRY IS NAMED, NOT TAGGED — `PT-1795`

`BUILD 154` shipped the locked sidebar showing

    mate.a01.01 · Soldier · 1 · 10 of 10

where a person reads a name, **and said so in its own comment**: the seam
carried the class, the level, the species, the faction and the speed — and not
the name. The blueprint has had one since the reader was written.

`PlacedCombatant` carries it now. **The tag stays the identity** (`PT-1331`)
**and stays the fallback**, because a placement whose blueprint will not open
has no name and is still on the board — `PT-1493` keeps it drawn rather than
dropping it, and a row with no label would be worse than one labelled by its
tag.

## 3 · ⚠⚠ THE LOW-HEALTH FLASH — `PT-1109`, AND THE CLOCK PREDICTED IT

> *"Low health, for anyone, is carried by the health bar itself flashing
> between red and white — deliberately not a static color, since a static red
> would be indistinguishable from an enemy's already-red baseline identity.
> This corrects a real gap `TRACE-22` found in the source: neither game gave a
> shrinking bar any additional signal for urgency, leaving a sliver of health
> looking identical to a large loss at a glance."*

**⚠ `low` IS A RULED THRESHOLD AND NOT ONE I PICKED.** *Below half vitality* is
already a mechanical condition in four rules documents — `Deep Cover` leaves an
encounter under it, `Blood Frenzy` and `Life Debt` key off it. **The same
standing `defaultPerceptionSquares` has as the detection radius**: the number is
reused, not invented, and no new ruling was needed to draw it.

**⚠⚠ AND `PulseClock` WROTE ITS OWN FUTURE IN A COMMENT:**

> *"Only Continue pulses today, so a per-widget controller would look identical
> and be wrong the moment a second thing pulses. **The clock is shared now so
> that never becomes a bug nobody can see.**"*

This is that moment. The flash takes the clock rather than starting its own,
and **the file moved out of `package_menu/` when it did** — a shared style
primitive named for one screen is a name that lies the first time a second
screen uses it.

`maybeOf` returns `null` where no clock is installed rather than throwing: a
dozen widget tests pump this panel directly with no screen around it, and **a
pulse is a decoration on a fact the bar already shows by colour and length**, so
its absence degrades to a static bar. Only a low portrait listens, so a party at
full health animates nothing — and a control case holds that.

## 4 · ⚠ THE AUDIT THAT FOUND THE SIDEBAR, RUN AGAIN

Fifteen widget files cite no UI design document at all. **That is not itself a
fault** — the chargen screens cite `CHARGEN-DATA-01` and their own rulings,
which is the right source for them.

**⚠⚠ BUT `play_screen.dart` IS STILL ONE OF THEM, AND `§2` AND `§3` ARE ITS
OWN.** `BUILD 154` closed the sidebar half; the rest of that section is locked
and unbuilt, and worth the owner's sequencing rather than my choosing:

| | |
|---|---|
| **`§2`** the player card opens the full character screen — Inventory, Equipment, Sheet, Skills/Feats/Powers, Journal, Message Log | unbuilt, **and behind the same first-click question `PT-1443` already holds** |
| **`PT-1137`** grid tokens are the sidebar's own portraits, *"rather than a plain marker, so a token on the board and its entry in the sidebar are visibly the same character"* | `Lens` draws marks; **now that the portrait exists, this is buildable** |
| **`PT-1108`** two real combat interaction systems, the second faithful to `TRACE-14`/`TRACE-21` spinner-cycling, off by default | unbuilt, and explicitly *"accepted deliberately as worthwhile rather than scope creep"* |
| **`§3a`/`§3b`** the exploration action catalogue and party following | unbuilt |

---

## What ran

    Lodestar   682 tests   exit 0
    Loom       263 tests   exit 0
    app        559 tests   exit 0   (+3)
    flutter build linux     built

Mutation-checked: nulling the name at the seam kills the naming case; the
flash has a control case at full health.

## Heads

    Lodestar        f1c2cc0   (unchanged)
    Loom            7a0ca16   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   a27edce
    MAIN_WORK       592f313   (unchanged)
