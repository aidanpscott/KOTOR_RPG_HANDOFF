# BUILD 75 — `PT-1523`: declared, read, and written by nothing

**804 green** — Lodestar 368 · Lens 5 · Loom 131 · app 295.

---

## ⚠⚠ `PT-1523` HAD TWO MISSING HALVES, NOT ONE

You named the writing half. **The reading half was missing too**, and the fix
would have been invisible without it.

    character.moved   declared `campaign` WITH THE REASON IN ITS COMMENT
                      folded by projectPlayState into a Position
                      ⚠ emitted by NOTHING          — TEST 021, 0 of 17 saves
                      ⚠⚠ and `.position` had ZERO USES in the whole app

`_open` set `_entry = _package?.entryArea` **unconditionally**. So the kind was
**declared, folded, unread AND unwritten — three ends missing.** Writing it
alone would have fixed nothing a player could see.

### ⚠ TWO MOMENTS, NOT EVERY KEYPRESS

`onAppend` **rewrites the whole save file** — `SAVE-LOAD-01` has no append — so
a `moved` per arrow key is **a file write per arrow key.**

> **The volume question is settled and the write-frequency one is not.**
> `PT-1328`'s 120,000 events at 0.34 MB is about the **log**. This is about the
> **disk**.

**Arrival in an area** and **leaving the screen** are the two moments that
decide where a resumed game begins. ⚠ And `_leaveScreen` appended **only when a
fight was in progress**, so leaving a room you had walked across wrote nothing
at all.

⚠ **A resumed square that is no longer standable falls back rather than
refusing** — an author may repaint a room between sessions and `PT-1367` makes
that one gesture; **a save must not become unopenable because a wall moved.**
The resume point is consumed **once**, and a New Game clears it.

⚠ **The saved area is used as-is**, and `openAreaIn` still checks it against the
manifest (`PT-1505`): a package edited so the area is unlisted gives the refusal
screen rather than **quietly relocating a character.**

### ⚠ And `whole_loop_test` had been asserting half its own headline

Its comment read *"⚠ THE SAME CHARACTER, IN THE SAME PLACE"* and **it only ever
checked the character.** It asserts the place now, walks back through the door
to reach the trooper, and the `Load Game` row says **the hold** rather than the
entry — **the screen that describes a save and the button that resumes it now
agree about where it is.**

---

## ⚠⚠ THE THIRD DIRECTION IS CHECKABLE, AND IT IS CHEAP — so I took it

    A  ⚠ EMITTED and UNDECLARED           check A, PT-1418 — 14 of 15
    B  ⚠ DECLARED and replay IGNORES IT   check B, PT-1418
    ⚠⚠ DECLARED, FOLDED, and NOBODY WRITES  — unseen until PT-1523

**Why neither could see it, and it is structural:** both compare the **document**
against a set of kinds **the code declares it handles.** Neither asks *is there
a construction site* — and that is a plain source-level fact nothing was
reading.

`scripts/check_event_producers.py` asks it — a `CharacterEvent(...)` whose first
argument names the kind. **95 files, 50 declared kinds.**

⚠ **ITS HONEST LIMIT IS DATA-DRIVEN EMISSION**, which `PT-1435` already named: a
package's `effect` may name any declared kind, written through a site that names
**no kind at all**. Four such sites exist. So it carries an **explicit allowance
list with a reason per entry** — *a check that excuses whatever it finds checks
nothing* — and the list is verified **both ways**: an entry for a kind that IS
constructed is reported as a **stale excuse**.

⚠ **Controlled:** producer removed → exit 1, naming the kind. Restored → 0.

### ⚠⚠ And it found one more while passing

**`character.faction-changed` is folded and no engine code ever writes one.**
`PlayState.faction` is only ever what a package's effect set. `FACTIONS-01 §4b`
gives a character **one handle and explicitly not a standing track**, so there is
nothing for the engine to move — **allowed with that as the reason**, so the day
something should change a faction, that line is the argument to overturn.

---

## ⚠ `PT-1524` and `PT-1525` landed mid-slice and both touched what I had built

**`PT-1524` — an enemy dies at 0.** `PT-1515` left a dying enemy nothing ticks
out of combat; the band is now the party's **entire**. An enemy is outside it:
above zero it stands, at zero or below it is dead.

⚠ **And `attack_seam_test` pre-set a target to −12** — `dying` under the old
band, **dead** the moment an enemy has none. Striking an already-dead creature
crosses no boundary, so `PT-1421`'s one-crossing-one-event **correctly wrote
nothing**. It kills a **living** creature now, which asserts the crossing rather
than a pre-dead state.

### ⚠⚠ `PT-1525` — MY REASON WAS THE WRONG REASON

I argued *a dead creature leaves nothing* as a **consequence**, on three
blockers. **All three block the placeable path, and KOTOR abandoned that path.**
A KOTOR corpse is **the creature itself** — `SetIsDestroyable`'s own comment
says it *sticks around as a corpse*, same object, same inventory — and
`RancorCorpse`/`KraytCorpse` ship with **zero placed instances.**

**Leaving the combatant needs none of my blockers**: the body is where it stood,
the inventory is already on it (`PT-1452`), and it is runtime state
`PLAY-STATE-01` already projects. **The filter stands and the comment now says
it stands as a thing not yet built, rather than a thing the format forbids.**

---

## ⚠ `listFor` READS THE HEADER — asserted, not asserted-about

`TEST 020`'s filing **retires.** `var owner = s.package;` first; the replay runs
only for a `format = 1` save.

⚠ **And the discriminating test is a save whose header and log DISAGREE**: the
header says `from-the-header`, the log says `from-the-log`, and `listFor` finds
it under the header and not under the log. **That proves no log was consulted**,
which a test that merely finds the save does not.

## Still open

- ⚠ `PT-1509` fog · `PT-1517` · `PT-1519` — ruled, unbuilt.
- ⚠ `tester-probe/sentinel-challenge` still needs a **failure node**.
- ⚠ The conversation editor has **no button for `unlink`**.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 45 annotation cells.
- ⚠ `AGENDA-CURRENT.md` forked 814 / 1553 — **left, as ruled.**
