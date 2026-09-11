# BUILD 123 — the roster is a fold, and the panel reads two sources on purpose

`PT-1672`, `PT-1059`. Where the fold lives was answered before a shape was
assumed, and the answer turned up a missing producer.

---

## 1 · ⚠⚠ WHERE IT LIVES — A NEW PROJECTION, NOT AN EXTENSION

**`combatRoster(log, encounter:)` in `Lodestar`, beside `projectPlayState`
rather than inside it.** Three reasons, and the third is the one that decides
it:

1. **`projectPlayState`'s signature settles it.** `required String subject`,
   with `if (who != subject) continue` at the top of its fold. That projection
   is **one character's state**; a roster is about **a fight.** Putting other
   people's membership inside one character's state would make `PlayState`
   answer a question it is not about.
2. **The precedent is `remainsIn`** — `PT-1525`, three days old: a fold over
   the same log, about a *place* rather than a person, own file, **own section
   of `PLAY-STATE-01` rather than a field in `§3`'s set.** Two folds became
   three and the document did not need a new one.
3. **⚠⚠ AND THE HARD ONE: `projectPlayState` TAKES `vitalityCapacity` AND
   `constitution` FOR ITS SUBJECT.** A roster would need those *for everybody*,
   which means opening blueprints — and `ENGINE-INTERFACE-01 §4` bars the
   engine from browsing a disk. **Membership has to be separable from the
   numbers**, and the separation is the design.

## 2 · ⚠⚠ THE KIND THE RULING FOLDS HAD NO ENGINE PRODUCER

`PT-1672`: *"`encounter.began`/`encounter.ended` already exist as event
kinds."* True — **and nothing in the engine ever wrote a `began`.**
`check_event_producers` carried the excuse verbatim:

> *"no engine producer, by design: `PT-1437` makes it the one engine kind an
> AUTHOR may name."*

`_begin` started a fight and emitted nothing. **A fold over those two kinds
would have been empty for the whole fight and fully populated at the instant it
ended** — the roster arriving exactly when the fight stopped needing one.

**⚠ TWO PRODUCERS, ONE KIND, AND THE PAYLOAD SEPARATES THEM.** An author's
`encounter.began` carries nothing — `PT-1437`, *the kind alone is the effect* —
and is a **request to start a fight.** The engine's carries `subject` and
`encounter`, **the same payload `encounter.ended` already carries**, because
began and ended are the two halves of one membership and **a matched pair is
the only shape a fold can close.** `combatRoster` requires a subject, so a bare
one joins nobody.

**⚠ And it is `transient` (`PT-1612`), so no roster reaches a save.** Not a
gap: `ENGINE-SPEC-04 §4` writes no round, `_enter` abandons the fight, and **a
roster restored from a save would describe a fight that no longer exists.** The
membership is as transient as the round it belongs to.

## 3 · ⚠⚠ TWO SOURCES, JOINED ONCE, AND THE SEAM IS NAMED

|  |  |
|---|---|
| **membership** | the fold over the log — `PT-1672` |
| **the numbers on each row** | the **live combatants** |

**`character.damaged` is transient and is deliberately never logged** —
`projectPlayState`'s own note: *"lifetimes decide what is written in the first
place. So a blow is not in the log to fold."* **A live bar cannot come from the
fold**, and a fold that supplied one would be inventing a number.

**⚠ So they are joined in ONE place** — `_rowsFor` — because `PT-1468`'s rule is
that two lists which can disagree eventually do. **And the disagreement is a
state a row can be in:** a member the round does not hold draws *"in the fight,
and the round does not hold it"* rather than vanishing or reading zero. **A bar
at zero would read as *nearly dead*, which is a different fact and a worse one
to get wrong.**

**⚠ `hidden` is TOLD, not asked** — the same seam `PT-1551` gives `Lens`, and
from the same `_concealed` set the board uses. There is no event for visibility
and `PT-1550` refuses to mint one: *"inventing a kind nothing rules is how
`character.moved` came to be declared, read, and written by nothing."*

## 4 · ⚠ THE PANEL TAKES WIDTH, AND THAT WAS ALREADY SETTLED

`PT-1447` decided this axis one arrangement over: a column under the board
*"pays in height instead — a room in a 1280×285 strip fits to HEIGHT and leaves
~70% of the width black"*, and `BUILD 44` is that **this screen has no spare
vertical and a row is not free.** So the roster sits beside the board, where
the dialogue panel does — and the two never share the row, because
`_maybeFight` calls `_endTalk` before `_begin`.

## 5 · ⚠⚠ THE FORCE BAR — THE FRAME STAYS AT THE TRUE MAXIMUM

    [████····························▒▒▒▒▒▒▒▒]
     current      headroom to the ceiling   what exhaustion took

**If the frame shrank to the working ceiling, a degraded pool would look
FULL** — which is precisely the state `PT-1059` says two values cannot express:
*"a Force user who sleeps normally wakes healed, pool full, ceiling still
degraded. You cannot rest off exhaustion."* **What was lost has to keep
occupying space or it has not been shown at all.**

**⚠ The degraded band is a THIRD colour, not a dimmed first one** — a bar
drawing exhaustion as a paler version of what you have left would be saying the
same thing twice. And the three are **new tokens, declared as mine**:
`UI-STYLE-VALUES-01 §1` gives every accent exactly one meaning and a Force pool
is none of them, the same argument `Lens` makes for `hazardMark`.

**⚠ The third number appears only when it differs.** An undegraded pool saying
*"max 20 · 20"* is arithmetic with nothing to say.

## 6 · ⚠⚠ TWO DEFECTS FOUND BY CASES THAT ASKED FOR SOMETHING

**The dead colour was unreachable.** `_vitalityColour` maps `down`, `dying` and
`dead` to their own colours — and **all three are at or below zero, so the FILL
band has width zero in exactly the three states the colour exists to
distinguish.** A dead row drew an empty frame identical to a full one's:
*length* said *nothing left* and nothing said why. **The track carries the state
now** when there is nothing left to fill. Found by the case that asked for it.

**The panel's first arrangement overflowed by 47px.** A card above a `Flexible`
list reads as bounded and is not — the card's height is whatever its Force note
runs to. **`force_cast_test` caught it**, a suite with nothing to do with the
roster, because its window is smaller. It is one scrollable now, with the card
as its first row.

## 7 · `PT-1675` — INTERRUPT IS BUILT AND NOBODY HAS EVER SEEN ONE

**⚠⚠ THE ZERO IS A FACT, NOT A STUB, AND THAT IS THE WHOLE FINDING.**

`ATTACKS-01 §10`: *"uses per encounter = the lower of your highest reaction tier
and your ability allowance."*

| half | state |
|---|---|
| **the allowance** | **wired.** Dexterity and the base attack bonus both reach `Budgets` |
| **the tier** | **has no source anywhere in the project** |

- `§10`'s three reaction chains are **Snap Shot, Overwatch and Parry**, and
  **none is in `base-rules`**: there is no `attacks.toml`, and `Overwatch` does
  not appear anywhere in the extract.
- **`CharacterRecord` has no `attacks` field.** `§11` makes attacks a **third
  currency** with its own pick schedule, and chargen has no step that spends
  one.
- `§11.1` gives every character `Strike` and `Shoot` free, and a reaction chain
  is neither.

> **So `0` is arithmetically right for every character that can currently
> exist, and permanently right until attack rosters are extracted and a pick
> step exists.** Making it *"reach `Budgets`"* is that thread, not that line.

**⚠⚠ WHAT THIS SLICE DOES CLOSE IS THE SILENCE.** `DialogueRun` withholds every
interrupt at zero reactions — correct, `PT-1500`: nothing shown can be refused.
**But `Beat.interrupts` was then empty for two different reasons** — *this line
offers none* and *you cannot pay for the one it offers* — **and a screen cannot
tell them apart from an empty list.** An author who writes an interrupt sees
nothing, forever, with nothing saying why.

`Beat.interruptsWithheld` says which, and the panel prints *"there is an
interruption here and you have no reaction to spend."* `PT-1487`'s rule, one
surface late: *"the pick already refused with the numbers; the MENU said
nothing, so the only way to learn a power was out of reach was to try it."*
**Here you could not even try.**

**⚠ And the field fell into the trap its own neighbour warns about.** `begin`
and `choose` each rebuild a `Beat` field by field, with a comment saying a new
field will be silently dropped — **and both dropped it on the first run.** A
comment warning about a trap is not a guard against it.

## 8 · ⚠⚠ `save_on_use` — THE CHECKBOX IS REAL, AND I MUST CORRECT MY OWN CAUSE

**The control exists and is not TOML-only.** `save on use` is a `_Toggle` on
Loom's door selection bar; `door_saves_on_use_test` **selects the door on the
board, taps the words, and reads the file back through `openArea`.** Clicking a
door's square selects it — `a.connections` is in `grid_view`'s hit list.

> **⚠⚠ AND MY EXPLANATION FOR WHY TESTER DID NOT FIND IT IS WITHDRAWN.
> `PT-1676` records it and it is not supported.**
>
> I read `bundle/loom` — **the launcher stub, which does not change when Dart
> code changes.** The Dart payload is `data/flutter_assets/kernel_blob.bin`,
> **and I rebuilt Loom's before reading its date, destroying the evidence.**
> The app's payload was from the same morning, which suggests these are rebuilt
> routinely. **"Three days stale" is unestablished, and the real cause is
> unknown.**
>
> This is my own memory note — *read the copy the binary was built from; three
> artifacts* — walked into at the first opportunity.

**What would hide the control, and is worth Tester checking:** the grid's tap
handler **paints instead of selecting whenever a palette tool is armed**. Clear
the palette, click the door's square, and the toggle is on the selection bar
under the tag line. Loom's bundle is rebuilt either way.

## 9 · ⚠⚠ TWO CHECKS REPAIRED, AND ONE OF THEM HAD GONE BLIND

**`audit_rulings.py` could not see five rulings.** Its heading regex accepted
**only an em dash**, and `PT-1670` onward are written `## PT-1670 -- TITLE`. So
citing `PT-1672` reported **CITED BUT NEVER WRITTEN and blocked the gate**,
while the ruling sat in the file being cited correctly. `1663 → 1668` headings.

> **The instrument was measuring typography.** `PLAYTEST-RULINGS-01.md` is the
> owner's file — `PT-1446` — so the repair is in the check and never in the
> document, and **a check that demands one dash character from a human writing
> prose will go blind again.** All three dashes count now.

**`check_event_producers.py` caught its own stale allowance**, the hour the
producer landed: *"`encounter.began` is in the content-only list AND is
constructed — the allowance is out of date."* **An exception that outlives its
exception is permission nobody is using any more.**

## 10 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| leaving does not remove | the roster closing, and the second-fight case |
| a nameless `began` joins a row | the subject guard's own case |
| no `encounter` scoping | another room's fight |
| the caller may mutate the result | the unmodifiable case |
| the join is not recorded in the log | both play cases |
| no degraded band | the force frame |
| a hidden row is not marked | the hidden row |
| an absent member draws a zero bar | the absent row |
| the track never carries the state | the dead row |
| the withheld line is not drawn | `PT-1675`'s panel case |

**⚠ And one of my own cases was vacuous.** *"An author's `encounter.began` joins
nobody"* is refused by the **scope** line, not the subject guard — an author's
event carries no `encounter` either, so the guard was never reached. **Split in
two**; the guard's own case is the one that fails when it goes.

## 11 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 527 | **542** |
| `Loom` | 252 | **252** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 409 | **420** |
| | 1,198 | **1,224** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.
`check_event_producers.py`: *every kind a projection folds, something writes.*

## 12 · Not done, named rather than skipped

- **A hidden row cannot occur in play.** A fight starts by contact and contact
  reveals (`PT-1550`), so no fight member is ever concealed. The row property is
  built, wired to the board's own set, and **tested at the panel** — the same
  standing `ACTION-ECONOMY-01 §5`'s second interaction had before looting gave
  it a caller.
- **Companions do not exist**, so every non-player row is an enemy. The fold and
  the panel do not care which.
- **No click-through to a character screen** — deferred, as asked, and no row
  looks pressable.
- **Turn order is not shown.** The roster is join order, not initiative order;
  `STUDY 32` says turn order is *why* a roster exists, and nothing draws it yet.
- **The reaction tier still has no source** — §7. That is a thread.
