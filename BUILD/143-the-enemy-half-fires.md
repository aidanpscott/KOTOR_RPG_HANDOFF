# BUILD 143 — the enemy half fires, and a zero pool fooled me twice

---

## 1 · ⚠⚠ `§10`'s ENEMY-SIDE TRIGGER IS DRIVEN, ELEVEN SLICES AFTER IT WAS BUILT

`BUILD 132` built it and said plainly that it could not fire:

> *"`enemyTurn` only ever CLOSES, and closing on your only target never leaves
> that target's reach. **An enemy leaves a reach only when moving toward a
> DIFFERENT party member, and the party is one.**"*

`PT-1735` made the party two. The board is the one that sentence describes: the
Sith **adjacent to the player**, its target the **companion at the far end of
the hall**, and reaching them means leaving the player behind.

    you catches sith.a01.02 leaving — unarmed · rolled 21 …
    · sith.a01.02 closes 5 squares — 8 to 3

Two mutations pin it — severing `_closeOn`'s call, and taking the snapshot
after the move instead of before.

## 2 · ⚠⚠ AND IT LOOKED BROKEN FOR THREE ATTEMPTS. THE POOL WAS ZERO.

My first beds gave `PlayScreen` no `characterClass`. So the player's base
attack bonus was **null**, `reactionPool` returned **zero**, and the trigger
fired into an empty pool and returned **silently** — the geometry was right the
whole time.

> **That is `PT-1708` exactly.** A zero reaction pool masking a working rule,
> on the **opposite side of the same feature**, fooling me a second time.

The difference is where the zero came from: `PT-1708` was a seam that never
passed the ladder; this was a **test bed** that never supplied a class. **Same
symptom, same silence, different cause** — which is why the test says so in its
own comment, and why `PLAY-STATE-01` now records that *a `§10` which appears not
to work is a pool question before it is a geometry question.*

**⚠ I ALSO NEARLY FILED IT AS A BUG.** Three boards in, the honest reading was
*"the wiring does not fire"* — and it was one missing constructor argument. The
thing that stopped me was checking the cheapest explanation before the
interesting one.

## 3 · ⚠ A WOUNDED COMPANION IS STILL WOUNDED IN THE NEXT ROOM

`_bringTheParty` rebuilds a companion **from its blueprint**, which is a
full-health template — so the wound has to come back out of the log, and a
companion healed by a doorway is the sort of thing nobody notices until a fight
is unwinnable or trivial.

**⚠ AND IT IS NOT THE BLOW THAT TRAVELS.** `projectPlayState` deliberately does
**not** fold `character.damaged` — those are *transient, until the encounter
ends*, and `§2` gives lifetimes their job: **a blow is not in the log to fold.**
What persists is `encounter.ended`, which `_writeOutcome` writes **once per
combatant** — so a companion gets one, and that is the only reason its wound
survives a door.

**⚠ I WROTE THE FIXTURE WITH THE WRONG KIND FIRST** — `character.damaged`, which
compiles to nothing because the constant does not exist — and the projection's
own doc comment is what said why.

## 4 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 644 | **644** |
| `Loom` | 261 | **261** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 509 | **511** |
| | 1,424 | **1,426** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓. Exit codes checked on every run.

## 5 · ⚠ Companions — what is left, and it is all design now

Every remaining gap needs a decision rather than a keyboard:

- **Nothing recruits.** The seam is one line wide — meeting a companion records
  what the placement already said — and **what should trigger a join** is the
  ruling: a conversation, a choice, walking up to them.
- **Nothing switches control.** `PLAY-STATE-01` describes it — *"a droid with no
  Force connection and a Jedi in the same room genuinely see different things,
  and switching between them shows you that"* — but that sits inside the
  **unbuilt fog-of-war TO DO**, so it is a sketch rather than a spec.
- **A fight does not cross a door.** `Fight.abandon()` and `§4`'s transient
  round make that correct; the party crosses intact and the fight does not, and
  **that pair is worth a ruling only if the owner dislikes it.**

**Nothing in companions is blocked on me.** The next slice there is a decision.
