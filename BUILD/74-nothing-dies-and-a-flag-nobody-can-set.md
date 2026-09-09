# BUILD 74 — `PT-1515` and `PT-1516`: nothing died, and no flag could be set

**793 green** — Lodestar 366 · Lens 5 · Loom 131 · app 291.

---

## ⚠⚠ `PT-1515` — THREE CAUSES, AND EACH ONE ALONE WAS ENOUGH

### 1 · `Role` had four members and **every one was a party role**

    player · companionDroid · companionBeast · henchman

**There was no way to say *"this is not ours"***, and `combatantFrom` defaults
to `Role.player` — so **every creature an author placed was a party member as
far as the rules were concerned.** That is why the party's stand-at-1 rule
applied to the whole galaxy. `enemy` added; a placement is one, and **that line
is the seam** the day a placement can join the party.

⚠ The rule was also **written twice**, in `stateOf` and in `applyDamage`. A pool
that floored at 0 would have reported `down` by arithmetic even after the state
rule was fixed. One function now.

### 2 · ⚠⚠ TESTER'S SENTINEL WAS NEVER DEAD — and that is the sharp part

At **−2 with `Con 10`** it was **dying**, not past the threshold. **Making death
work would not have fixed this on its own.**

**The revive was the defect.** `_writeOutcome` asked `c.vitality.current <= 0` —
**a raw number** — and stood everything up at 1, enemies included, and wrote it.
`PT-559` stands up a downed **PARTY MEMBER**. It is party-only now, and an enemy
left dying stays dying at the vitality `encounter.ended` already records.

> **A rule restated as a number is a rule that has stopped being the rule.**

### 3 · `character.died` was declared, produced, and folded by nothing

`applyDamage` has returned it since combat was built, and **both call sites
discarded it** — an attack's kinds went into `_said`, and `f.advance()`'s return
value was dropped on the floor. **Computed twice over, written never.**

⚠ **And it had no constant**, only a raw string, so nothing could switch on it —
which is why `projectPlayState` folded `revived` and not this. **A death could
not have survived a quit even once something wrote one.** Third instance of a
declared kind with nothing on the other end.

⚠ **A RECORDED DEATH OUTRANKS THE ARITHMETIC.** A death floors the pool at 0 and
`stateOf` calls 0 `down`; re-deriving state from the pool would have downgraded
the death and handed the creature back at 1 the next time a fight ended. **The
event is the fact; the number is a consequence of it.** And a `revived` reaching
a dead subject is **refused**, not ordered around — a projection that depends on
its producer being careful has a rule it does not enforce.

## ⚠ WHAT A DEAD CREATURE LEAVES BEHIND: **NOTHING**

**And that is a consequence rather than a choice.** There is no corpse among
`AREA-FORMAT-01`'s five tile types, `[[contents]]` is **authored**, and `§4`'s
no-write rule bars the engine from editing a package. **Inventing loot would be
a format decision made from a play screen.**

⚠ **So it is removed from `_here` ONCE rather than skipped in four places.**
`_here` draws the marker, answers `_occupant`, feeds the fight and feeds the
panel — filtering there is the difference between a creature being **gone** and
a creature being **ignored by whichever list someone remembered.**

⚠⚠ **AND `PT-1511`'s VACATED SQUARE IS REACHABLE.** Tester could not construct
it because nothing died. The placement's square no longer answers `_occupant`,
so **it is walkable** — the wall-under-a-creature question stops being
hypothetical.

⚠ **The app has no difficulty setting.** `Encounter` defaults to `normal` and
nothing ever passed another, so **every fight so far has been Normal.** Named
once as `_mode` rather than left as a literal in two places.

---

## ⚠⚠ `PT-1516` — AND THE PAYLOAD GAP, NAMED RATHER THAN FILLED

Loom's effect button wrote `{ kind: <whatever you typed> }`. The best an author
could produce was:

```toml
effect = [ { kind = "quest.flag-set" } ]
```

**`flagsFrom` matches on a `flag` field.** So a flag effect authored in Loom was
**silently a no-op** — beside a `flag` **GATE** button that could read one. **A
readable half with no writable half, offered as if complete.**

### You asked for the shape before a form. Here it is, and it is three.

`EVENT-KINDS-01` declares ~40 kinds and `PLAY-STATE-01 §6` leaves every payload
**deliberately unspecified**. **Derived from the consumers, not from what a
field name suggests:**

| kind | carries | read by |
|---|---|---|
| `quest.flag-set` | **`flag`** | `DialogueView.flagsFrom` |
| `quest.concluded` | **`quest`, `conclusion`** | `DialogueView.questsFrom` |
| `encounter.began` | **nothing** — the kind is the whole effect | `PT-1437` |

**Everything else has no specified payload and no consumer.** Requiring fields
nobody reads would be **a validator inventing a format** — asserted, so a schema
cannot creep in unnoticed.

> **⚠⚠ `item.lost` IS THE SHARP CASE.** `§9`'s own worked example writes
> `{ kind = "item.lost", item = "credits", count = 50 }` — **and nothing in this
> project reads it.** The fields look load-bearing and are decoration. **An
> author following the format's own example writes an effect that does
> nothing**, and the only reason that is not `PT-1516` again is that no gate
> reads a purse.

### The fix is in the validator, so the Builder's refusal is automatic

`validateConversation` requires those fields; `PT-1379` does the rest. Loom's
effect vocabulary is **closed** — the same argument `§4` makes for gates,
*"a box you can type a gate into is an escape hatch by another name"* — and the
form **names the fields the chosen kind wants**, with the second box labelled by
the kind rather than staying `dc`. **A box labelled `dc` that silently means
`conclusion` is how a form teaches the wrong thing.**

⚠ `EVENT-KINDS-01 §3b` records the gap and what would close it: **a payload
column, written when a consumer exists, kind by kind — not all at once and not
from what the names imply.**

---

## ⚠ Citations

`PT-1515` and `PT-1516` match the index. **The header ruling now has a number —
`PT-1518` — so the code cites it** instead of `PT-1416`, the ruling it overturns.
That is the owner's number rather than one of mine.

## Still open

- ⚠ `PT-1509` — fog. Ruled, unstarted. `PT-1517` and `PT-1519` are new and
  unbuilt.
- ⚠ `tester-probe/sentinel-challenge` still needs a **failure node** — content,
  and Tester's package. It is the only shipped conversation that does not
  validate.
- ⚠ The conversation editor has **no button for `unlink`**.
- ⚠ A dying enemy is left dying and nothing ticks it out of combat. **Correct as
  far as any ruling goes, and worth knowing**: it is out of the fight, not dead,
  and stays that way.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 45 annotation cells.
- ⚠ `AGENDA-CURRENT.md` forked 814 / 1553 — **left, as ruled.**
