# BUILD 180 — the placeable format, and it is three things rather than one

**A proposal. Nothing in it is ruled and nothing is built against it.** Same
process as `BUILD 179`: measured rather than estimated, and every count below
came out of the games this afternoon.

---

## 1 · ⚠⚠ WHAT IS ACTUALLY BLOCKED

Five of `APP-UI-VISION-01 §3a`'s eight object verbs have nothing in the world
to aim at. `area_open` reads `[area]`, `[tiles]`, `[[contents]]`,
`[[connections]]` and `[[arrivals]]` — **and `[[contents]]` is characters
only.**

    Search        a container         ⚠ nothing can be one
    Open Lock     a lock              ⚠ nothing has one
    Disarm        a trap              ⚠ nothing has one
    Slice         a terminal          ⚠ nothing can be one
    Pick Pocket   a purse             ⚠ nothing has one

**And `TerminalPanel` is built, tested, and reachable from nothing** —
`PT-1149`'s one screen for slicing and repair exists, and no door into it does.

⚠ **`blueprints/placeables/` and `blueprints/doors/` are the fourth and fifth
folders to exist with no format behind them.** `PACKAGE-FORMAT-01` named this
shape itself at `BUILD 42`, about `items/`: *"third time a folder has existed
with no format behind it."*

---

## 2 · ⚠⚠ THE MEASUREMENT, AND IT SPLITS THE PROBLEM IN THREE

I expected one format. The games have three, and **they do not overlap at
all** — every template of both games, shared and module-local:

| | K1 | K2 | carries |
|---|---|---|---|
| **Doors** `.utd` | 503 | 360 | ⚠ **locks**, keys, conversations |
| **Placeables** `.utp` | 1,254 | 842 | ⚠ **inventory**, usable, a few locks |
| **Triggers** `.utt` | 850 | 345 | ⚠ **traps**, and nothing else |

### ⚠⚠ TRAPS ARE NOT ON PLACEABLES. ZERO, IN BOTH GAMES.

    K1   0 of 1,254 placeables trapped        23 of 850 triggers trapped
    K2   0 of   842 placeables trapped        34 of 345 triggers trapped

**So `§3a`'s *Disarm (Demolitions)* aims at a TRIGGER**, which is a region
rather than an object — and that is a different format from the thing you
click on. `DisarmDC` clusters hard at **20**; `TrapDetectDC` at **20**, with a
few at 15 and 10.

### ⚠ AND MOST LOCKS ARE ON DOORS, WHICH WE ALREADY HAVE

| | locked | key-required | sealed `DC ≥ 100` | ⚠ **pickable** |
|---|---|---|---|---|
| K1 doors | 175 | 82 | 59 | **43** |
| K2 doors | 140 | 102 | 29 | **26** |
| K1 placeables | 56 | 4 | 1 | **48** |
| K2 placeables | 24 | 4 | 0 | **20** |

**A locked thing is usually not a Security check.** Of K2's 140 locked doors,
**102 want a key and 29 are sealed at `DC 100` or more** — a sentinel meaning
*the plot opens this, you do not*. The genuinely pickable population of the
whole of K2 is **46 things**, and of K1, **91**.

⚠ **`DC 28` is the lock**, 24 of K2's 26 pickable doors. Placeables cluster at
**18**. Two numbers carry almost the whole game.

> **⚠ SO `Open Lock` IS A SMALLER VERB THAN IT SOUNDS, AND `§5.2` ALREADY SAID
> SO.** *"Security spikes — **optional.** Spikes grant a bonus, not access —
> the one skill where the consumable is insurance rather than a cost."* A
> corpus where most locks want a key agrees with that ruling exactly.

---

## 3 · ⚠⚠ THE PROPOSAL

### 3a · Three kinds, and two of them already have a home

> **`[[contents]]` gains a `kind`, defaulting to `creature`.** One list, one
> placement grammar, `PT-1331`'s tag rule unchanged.
>
>     [[contents]]
>     tag  = "footlocker.command-deck.01"
>     kind = "placeable"
>     from = "placeables/footlocker"
>     at   = [4, 2]
>
> **A trap is a REGION and goes in its own list**, because it is not a thing on
> a square:
>
>     [[hazards]]
>     tag    = "mine.command-deck.01"
>     over   = [[4, 2], [5, 2]]
>     disarm = 20
>     notice = 20
>
> **And a door is a `[[connections]]` entry**, which already exists — it gains
> the lock fields and nothing else.

⚠ **`kind` RATHER THAN A SECOND LIST FOR PLACEABLES**, because everything
`[[contents]]` already does applies unchanged: a tag, a `from`, a square,
`hidden`, `stealth`. A `[[placeables]]` list would be the same grammar twice
and would drift.

⚠ **AND A TRAP IS NOT GIVEN ONE**, because it genuinely is not the same shape.
It has no square, no blueprint, and no tag a player can click — `over` is a
list of squares. Forcing it into `[[contents]]` would be `position-as-identity`
in a new place.

### 3b · The state is on the PLACEMENT, not the blueprint

This is the one real design question and our own format has already answered
it twice.

> **`hidden`, `stealth` and `range` are PLACEMENT fields today**, not blueprint
> fields — `PT-1550`, `PT-1564`, `PT-1573`. *This* footlocker is locked at 18;
> the blueprint says what a footlocker **is**.

    [[contents]]
    tag    = "footlocker.command-deck.01"
    kind   = "placeable"
    from   = "placeables/footlocker"
    at     = [4, 2]
    locked = 18            # ⚠ the Security DC. Absent = not locked.
    key    = "sith-keycard"  # ⚠ present = no check opens it, PT-1487 says so

⚠ **AND THE SOURCE AGREES, THE HARD WAY.** KOTOR puts these on the template
and then needs **937 module-local placeable templates in K1** to place ~6,000
things — a template per lock, effectively per instance. **That is the same
1.17-items-per-shape number `BUILD 179` measured for consumables**, and the
same answer: when the values are the instance, they belong on the instance.

### 3c · The blueprint, then, is very small

    [placeable]
    name  = "Footlocker"
    kind  = "container"      # container · terminal · fixture
    
⚠ **THREE KINDS AND NOT A `base` INTO `equipment.toml`.** `PT-1452`'s rule is
that an item blueprint names a base type *because the base type carries the
dice*. A footlocker has no dice. What `kind` decides is **which verbs the
context menu offers**, which is `§3a`'s filter and nothing more:

    container   Search · Open Lock  (+ Examine)
    terminal    Slice               (+ Examine)
    fixture     ⚠ Examine only — a thing that is scenery

---

## 4 · ⚠ WHAT THIS DELIBERATELY DOES NOT DO

**No `Useable` flag.** Half of KOTOR's placeables carry `Useable = 0` and are
pure scenery. **`fixture` is that**, by having no verbs rather than by a
boolean — an object that answers *Examine* and nothing else is already the
thing the flag was for, and `§3a`'s filter does the work.

**No scripts.** `OnOpen`, `OnUsed`, `OnTrapTriggered` and thirteen more hooks
are on every KOTOR placeable. We have no scripting and `PT-1437` already
settled the one case that mattered — *"the fight starts when the CONVERSATION
says so"*. A `conversation` field on a placeable is the cheap half and is not
proposed here either, because **228 of K1's placeables have one** and that is
a real feature deserving its own look rather than a line in this note.

**No `Pick Pocket`.** It needs a purse on a creature, which is a character
question and not this one.

---

## 5 · ⚠ THE ORDER I WOULD BUILD IT IN, IF RULED

1. **`[[connections]]` gains `locked` and `key`.** Doors exist, the lock is
   two fields, and it lights `Open Lock` on the population that actually has
   locks. **Smallest real win in the tree.**
2. **`kind = "placeable"` and the `container` blueprint.** Lights `Search`,
   and gives the remains/pile code a second producer.
3. **`terminal`**, which finally opens `TerminalPanel`.
4. **`[[hazards]]`**, which is `Disarm` and is the largest of the four.

---

## Tests

Nothing built. App **631** green, Lodestar **794**, gate **SENDABLE**.

## Still open

- ⚠ **Everything in this note.** Three kinds, state-on-the-placement, the
  three blueprint kinds, and the build order all need your word.
- **A placeable's `conversation`** — 228 of K1's have one; named and not
  proposed.
- From `BUILD 179`: **`charge` refuses all sixteen of its own items**, and
  `Examine`'s *what a total tells you* is unruled.
