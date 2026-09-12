# BUILD 141 — the companion comes with you

`PT-1741`. The most defect-shaped of the three gaps `BUILD 140` named, closed.

---

## 1 · ⚠⚠ THE FORMAT HAD ALREADY DECIDED THE SHAPE

`PT-1735` put somebody on the player's side and **they stayed in the room.**
`[[contents]]` is an author's statement about an AREA, so membership cannot
live there.

> `EVENT-KINDS-01`'s world-and-party section has carried **`party.joined` /
> `party.left` at `campaign` lifetime since it was written**, among the kinds
> it calls *"declared and unimplemented… a roadmap, not a defect."*

**Nothing here is a new idea.** The kind, the lifetime and the argument were
all settled before the feature existed — and the shelf's `event_kinds.toml`
already carries both rows, so persistence needed no change at all.

**⚠ ITS OWN PROJECTION, FOR `combatRoster`'s REASON.** `projectPlayState` takes
a `required String subject` and is **one character's state**; a party is about
several. `partyIn` is the third fold of that family after `remainsIn` and
`combatRoster`, and the document did not need a new section shape either.

### ⚠⚠ The payload is a decision, and it is said rather than implied

The document declares the kind and **not its contents**. A member has to be
**rebuildable in an area that never declared them**, so the event carries what a
`[[contents]]` row carries — the `tag` that is its identity (`PT-1331`) and the
`from` path its blueprint lives at (`PT-1452`, *a path, always*) — with the role
alongside so a `henchman` does not arrive an enemy.

**⚠ THE ROLE IS KEPT AS THE STRING.** A log written by a later build with a role
this one does not know **loads rather than throwing**, which is `PT-1699`'s
reading: the record comes back short rather than not at all.

## 2 · ⚠ Two halves, and neither is recruitment

**Meeting a companion RECORDS what the placement already said.** `PT-1735`
decided the side; what was missing was anywhere for that fact to live once the
room closed. **The day a ruling gives joining a trigger, it replaces one line**
and nothing downstream changes, because everything downstream reads the log.

**Arriving anywhere rebuilds any member the room does not declare**, beside the
player, through the **same reader** via a `placements` parameter.

> Blueprint resolution, equipment, species speed and ability line, the class
> ladder and the role are **every one of them a rule that would drift the day it
> existed twice** — and `attack.dart` already carries four comments about that
> having happened. One parameter is cheaper than any of them.

**⚠ SOMEBODY THE ROOM DECLARES IS LEFT TO THE ROOM.** An author who places the
same companion in the next area meant it to stand where they put it, and
arriving twice would be two of them.

**⚠ AND NOWHERE TO STAND IS NOT SILENCE.** A player arriving in a doorway with
the party behind them is told somebody did not fit — otherwise **the companion
vanishes and the save still says they are with you.**

## 3 · ⚠⚠ AND THE SHELF FLAKE GOT ITS FOURTH SIGHTING, IN A SECOND FILE

`acceptance_test` failed in the full run and passed alone, **with no change to
it at all** — and it is the same shape exactly: `sandboxed()` symlinks the real
shelf, and it taps a package **by name** in the **lazy horizontal row** whose
behaviour its own comment already documents (*"at seven `Taris Undercity` is not
built at all"*).

> **That is independent corroboration of a cause `BUILD 140` could only call
> evidence-fits.** A second file, a different test, the same mechanism — and it
> appeared the same day `Tester` was adding fixture packages.

Same fix, copying the **three** packages this one asserts, because its point is
that the shelf reaches the screen: the assertions stay and **the set stops
moving under them.**

## 4 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| nobody is brought along | the acceptance |
| the join is never recorded | 2 |
| a join is written on every entry | 1 |
| somebody the room declares is brought again | 1 |

**⚠ THE LAST ONE CAUGHT NOTHING AT FIRST.** The dedupe clause had no bed that
could exercise it, so I built one — the same companion declared in **both**
rooms, asserting the square a brought copy would stand on is **empty floor the
player can walk onto.** A clause with no case is a clause that is not there.

**⚠ AND THE ACCEPTANCE ASKS BY BUMPING.** Outside a fight nothing on the play
screen renders a creature's name — `Lens` paints the board and the roster only
exists during a round — so walking into the companion is the observable, and it
proves two things at once: **on the board, and on the player's side**, since an
enemy in that square would have started a fight.

## 5 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 625 | **633** |
| `Loom` | 261 | **261** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 504 | **507** |
| | 1,400 | **1,411** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
**caught Loom one behind** and it is level now. `flutter build linux --debug` ✓.

## 6 · ⚠ Companions — what is left

- **Nothing recruits** — a trigger is a design question, and the seam for it is
  one line wide now.
- **Nothing switches control.** The doctrine drives a companion, which is what
  makes every slice so far work.
- **They do not fight over a door.** A fight is abandoned on travel (`§4`, a
  round is transient) — correct, and worth knowing the party crosses mid-fight
  intact while the fight itself does not.
- **`§10`'s enemy-side trigger is reachable and still undriven.** An enemy
  walking past a companion to reach the player — a `TEST` pass, and now there
  are two party members on two boards to do it on.
