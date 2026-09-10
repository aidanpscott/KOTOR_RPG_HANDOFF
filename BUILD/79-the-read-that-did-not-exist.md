# BUILD 79 — `PT-1533`/`PT-1534`: the read that did not exist

**835 green** — Lodestar 382 · Lens 5 · Loom 131 · app 317.

---

## ⚠⚠ `PT-1533` — THE RECORD WAS RIGHT AND THE READ DID NOT EXIST

    sheet   STR 18 · DEX 8      ← chargen applied the species modifier
    log     str 14 · dex 10     ← the bought scores, correctly stored
    fight   str 14 · dex 10     ← nothing applied it here

`CHARACTER-RECORD-01`: **`abilities` holds the BOUGHT scores; the modifier
applies ON READ.** `PT-1260` and `PT-1402` ruled it and **only half landed.**

⚠ **THE PARSER ALREADY EXISTED.** `Adjustments.parse` has been in
`abilities_screen.dart` since chargen was built, handling the prose and the
unicode minus, reporting anything it cannot read rather than dropping it.
**What was missing was a caller.** That is the third time this slice-family a
derivation turned out to be further along than the play screen suggested —
`PT-1424`'s speed, `PT-1531`'s BAB, and now this.

⚠ **THE SUBRACE RESOLUTION WAS ALSO ALREADY WRITTEN** — in `hub.dart`, inline.
`PT-1402`: *the subrace wins where it has a line and the parent fills silence.*
It is a named function now, and **the hub's copy is the one to fold in next**.

⚠⚠ **EVERY MECHANICAL READ GOES THROUGH ONE PLACE.** `_ability` covers the
attack, the damage, the Force pool **and vitality** — a species that adjusts
Constitution changes how much you can take, which is the reading a player
notices first, and it was the one most likely to be missed by a per-consumer
fix.

---

## ⚠⚠ `PT-1534` — ZERO IS EXACTLY WHEN A PLAYER NEEDS TELLING

    was:  16 + 1 = 17, and no ability term at all
    now:  the ability the WEAPON USES is named, at zero

**Both silent readings were wrong.** Omitting reads as
*counted-and-irrelevant*; a bare zero reads as *counted-and-nil*. **Naming the
ability at zero reads as: this is the one that counts, and yours is average.**

⚠ **A FEAT IS DIFFERENT AND STAYS OMITTED.** Nothing consults Weapon Focus, so
`+ Weapon Focus 0` would claim it was checked. **The ability is shown because it
WAS consulted.** The distinction is the point.

⚠ **A weapon that uses no ability SAYS SO — on the line, not as a Term.**
`damage terms are never rendered`; a `Term('no ability', 0)` would be invisible
to the player it is for. And it is said **only when the wielder's Strength would
otherwise have mattered** — a clause on every shot is a clause nobody reads.

### ⚠ And the tautology

    was:  rolled 16 — d20 16
    now:  rolled 16 on a d20 · needed 10

**The dash introduces a derivation. With none there is nothing to introduce.**

---

## ⚠⚠ THE REACTION PIP FAILED MY OWN RULE, ONE FIELD OVER

`_playerCombatant` built `Budgets(reactionsLeft: 0)` **unconditionally**, so the
star was grey **from the first frame of every fight**.

> I wrote *"a bonus nobody granted is ABSENT, not grey — a grey pip is a
> promise"* — and applied it to `bonus` and not to `reaction`, **one field
> over.**

It is computed from `reactionPool` now — Dexterity and the base attack bonus,
banded, which `ACTION-ECONOMY-01` already defines. **Zero is still possible and
is now a fact rather than a placeholder.**

## ⚠⚠ AND CREATURES HAD NO BASE ATTACK BONUS AT ALL

`fight.dart` passed `baseAttackBonus: null` for **every** creature while the
player gained a real one. **That is why one side one-shot the other and a second
round never happened** — and why a bright pip had never been seen going grey:
the killing blow ends the encounter in the same frame.

A blueprint names a **class** and a **level**, which is exactly what a BAB table
is read by. `PlacedCombatant` carries both now and **one map serves both
sides** — `play_screen` and `fight.dart` being the pair a rule gets applied to
one of.

## Still open

- ⚠⚠ The class defence bonus — **an RCR Chapter 3 read, and the owner's.**
- ⚠ `hub.dart` still has its own copy of the subrace resolution.
- ⚠ Three classes have no BAB table: `engineer`, `marksman`, `saboteur`.
- ⚠ `PT-1509`'s perception half; `PT-1532`; `tester-probe`'s failure node; no
  `unlink` button; `PT-1484`, `PT-1485`, effect columns, 45 annotation cells.
