# BUILD 127 — detection at range, and who starts hostile

`PT-1686`, `PT-1687`. Combat's queue finished.

---

## 1 · ⚠ DETECTION REUSES THE NUMBER THAT WAS ALREADY RULED

`PT-1571` settled **one** default perception range with no per-species or
per-chassis table — **ten squares, 20 m, what 97.8% of 4,397 KOTOR blueprints
carried** — and that same number is the detection radius. No new field.

**⚠⚠ AND THE DELAY PORTS AS A ROUND, NOT A FRACTION OF ONE.** KOTOR scales its
reaction by distance (`distance/10` seconds, 2.0 s at the 20 m default) against
a 3-second round, so **every distance inside the range reacts within one round
in the source.** Finer granularity than *under one round* does not exist on our
clock. `PT-1496`: the trigger transfers, the real-time arithmetic does not.

**⚠ Contact is exempt**, because *contact is not detection at range, it is
already touching.* A creature pulled in by adjacency acts at once; one pulled in
by distance is marked `noticing` and acts the round after.

**⚠ And the mark is the point.** A row that simply appeared with no mark would
make a combatant who cannot act look like one who is about to — the same defect
as a hidden row that vanished.

### ⚠ `waiting` is cleared at the round boundary, and nothing counts rounds

`Fight.waiting` empties in `advance` right after `beginRound`. **A creature
marked on the round it arrives is unmarked by the next boundary, which IS *"does
not act until the round after"*** — no arithmetic, no round number stored, no
comparison to get wrong.

### ⚠ And a latecomer lands where `PT-1422` puts them

`Encounter.joins` rolls their initiative and re-sorts with **the same
comparator** `rollInitiative` uses — now named `byInitiative`, so there can only
be one. A second copy would put a latecomer in a different place **on a tie**
than the opening roll put anybody. `§9` forbids re-rolls, so this is their one
roll and not a second for anybody, and **`Fight.admit` re-finds `turn` rather
than adjusting it**: whose turn it is must not change because a stranger walked
in.

## 2 · ⚠⚠ `PT-1687`'s PREMISE DOES NOT HOLD ON THE DATA

> *"A static campaign-level fact already on every shipped package."*

**Checked before building:**

| | |
|---|---|
| packages declaring a faction | **none** — of seven on the shelf |
| creature blueprints declaring one | **none** |
| `PACKAGE-FORMAT-01` | **had no field at all** |

**The reader for `[character] faction` has existed since
`AUTHORED-CHARACTER-01 §2a` was written, with nothing anywhere filling it in.**

**⚠⚠ SO `undeclared` IS ITS OWN ANSWER, AND IT JOINS.** `startsHostile` returns
three things, not two, and the third is the whole reason it is not a `bool`:
**reading absence as *not hostile* would mean nothing could ever attack a player
again.** Absence-versus-error, in the one place where getting it wrong empties
the game.

`[package] faction` is added to the format, and the campaign's declaration is
the player's side — `PT-680`, `PT-685` — with `character.faction-changed`
already folded by `projectPlayState` for a defection. Nothing new was needed for
the override.

### ⚠ Same faction is peace, different is war — and that is a READING

`FACTIONS-01` gives the factions, the nesting and `§4b`'s sentence, **and no
hostility matrix.** This is the simplest rule consistent with both halves:
`§2ab` makes *"a Jedi campaign a Republic campaign"*, and its contrast has the
Sith warlords as *"peers fighting each other, with no parent above them."*

**⚠⚠ NESTING IS NOT IMPLEMENTED, AND THAT IS THE READING'S KNOWN HOLE.** `§2ab`
makes the Jedi Order a subfaction of the Republic, so a Jedi should not be
hostile to a Republic soldier — and this compares names, so it says they are.
**The tree is prose in `FACTIONS-01` and is in no extract**, so implementing it
would mean inventing the data as well as the rule. **Pinned by a test** so the
day the tree is extracted, that case fails and says why.

## 3 · ⚠⚠ DETECTION WALKED STRAIGHT PAST `PT-1437`

`PT-1437` has been the rule since `PT-1436` was superseded: **a creature with a
conversation is ALWAYS spoken to, and the fight starts when the conversation
says so.**

Detection at range did not ask. **The test bed's own trooper — six squares away
with a challenge to deliver — joined a fight it had not been given a line in.**
Caught by `roster_panel_test`, whose roster grew by one.

> **Thirteenth instance of a rule applied to one path and not the next, and this
> time it was a NEW path walking past an OLD rule.**

The check lives in `_wouldFight`, so **contact and range both read it** — and
`_hostile` still outranks everything, because a conversation that turned hostile
said so explicitly.

## 4 · ⚠ THE `range` OVERRIDE IS NOT AVAILABLE TO DETECTION

`§3c` makes `range` legal **only on a hidden placement** — `area_open` refuses
*"a range and is not hidden"* — because it was built for `PT-1573`'s
find-on-approach. My first control case set `range = 2` on an unhidden creature
and **the area would not open.**

**So `PT-1686` gets the default and only the default:** an author cannot
currently give one unhidden creature sharper or duller eyes than another. The
reader is right and the ruling did not ask for the field to change — **named
rather than worked around**, and the control moves the creature instead.

## 5 · ⚠⚠ THREE SHELF-DEPENDENT TESTS WERE ALREADY RED — ATTRIBUTED, THEN FIXED

They failed **with my changes stashed**, so they are the environment and not
this slice. The shelf has grown from four packages to seven — `Tester` has
published `mixed-faction` and `ranged-detection` for these very rulings — and
`tester-probe`'s fault count moved from 13 to 17.

> **⚠⚠ THE LIBRARY IS A HORIZONTALLY SCROLLING ROW, SO A `ListView` BUILDS ONLY
> WHAT FITS.** At four packages every tile was on screen; at seven
> `Taris Undercity` **is not built at all**. `find.text('Taris Undercity')` read
> as *is this package in the library* and measured *does this tile fit at 1280
> pixels.*

`acceptance_test`'s own comment had already learned this once, for the COUNT:
*"a count of a folder somebody else can write is an assertion about the
environment, not about the app."* **It came back for the names.** All three now
ask the row's `contents`, and the tile's own fields are compared against what
the package DECLARES rather than against a literal — `endar-spire`'s `authors`
had been edited from two names to one.

**⚠ And the health ratchet compares the screen's numbers to the validator's**
rather than the painted badges, which is what `PT-1546` was actually about: *"a
tile that computed health itself would be a second source of truth."* What is
painted is the row's business and `library_tile_test` holds it against a shelf
it controls.

## 6 · ⚠ And the gate caught me writing prose into a TOML example

`check_fenced_examples.py` blocked on `PACKAGE-FORMAT-01:115` — I had inserted
the `faction` section **inside** the manifest's fenced block, between `cover`
and `[requires]`. *A worked example is what an author copies.*

## 7 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| a range joiner acts immediately | the `noticing` case |
| nothing detects at range | three cases |
| the faction gate is open | the not-hostile case |
| `undeclared` read as peace | seven cases |
| the **panel** sorts its input | the strip case |

## 8 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 545 | **555** |
| `Loom` | 253 | **253** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 441 | **447** |
| | 1,249 | **1,265** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.

## 9 · Not done, named rather than skipped

- **Nothing declares a faction**, so the gate is inert on today's data and every
  pair is `undeclared`. `Tester`'s `mixed-faction` package may be the first to
  declare one — it is theirs and I have not read it.
- **Faction nesting** — §2.
- **The `range` override** — §4.
- **Detection does not see through walls, and does not not-see through them
  either.** `squaresBetween` is a distance; nothing consults line of sight, and
  `wall.blocksSight` is still read by nothing.
- **A creature that a conversation made hostile still joins by range**, which is
  right, but nothing re-checks the faction gate afterwards.
