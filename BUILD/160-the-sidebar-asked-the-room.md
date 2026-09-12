# BUILD 160 — the sidebar asked the room, and membership is the roster's

---

## 1 · ⚠ THE NARROWED QUESTION, ANSWERED

**The widget carries no location filter at all.** `PartySidebar` renders
whatever entries it is handed; its only `present` field is `PT-1468`'s
fight-roster disagreement.

**The narrower gate was in `play_screen`'s `_sidebar` getter, and it was one
line:**

    : <String>[
        if (me != null) me.handle,
        for (final p in _here)                       ← the CURRENT AREA
          if (isParty(p.combatant.role) && …)        ← isParty as a FILTER
            p.placement.tag,
      ];

`isParty` was applied **inside** `_here` rather than being the source. `_here`
is reset on every area entry (`_here = placed`), so it is exactly *who is
standing in the room that is loaded*.

## 2 · ⚠⚠ AND THE TWO SOURCES COULD NOT DISAGREE UNTIL `PT-1122`

`_bringTheParty` brought every member the room did not already declare. So
`_here` always contained the whole party, and the room-based answer and the
roster-based answer **matched in every reachable case**.

`PT-1468`'s shape exactly: *two answers to one question*, invisible while they
happen to agree. Solo Mode made them diverge for the first time —

    a companion holding position in the room behind you was still in the
    party and GONE FROM THE ONE SURFACE THAT COULD EVER OFFER THEM
    Follow / regroup

## 3 · ⚠ WHY THE FIX IS NOT THE ONE LINE

Sourcing from `partyIn` alone produces **three wrong readings** for a member
the room does not hold:

    no name    →  the tag on screen — `PT-1795`'s defect, one source over
    0 of 10    →  no combatant to read
    present:false  →  a sentence about a FIGHT, printed outside one

So the absent half of the roster is resolved through `combatantsIn` — **the
same reader**, for the reason `_bringTheParty` already gives: blueprint
resolution, equipment, species speed and the class ladder are rules that would
drift the day they existed twice. `_restore` runs on them too, because a row
reading full health for somebody you left bleeding would be worse than no row.

**⚠ THEY ARE NOT PLACED.** Nothing is added to `_here`, so no board draws them,
no range check measures to them, and nothing can be walked into.

**⚠ THE SQUARE IS THE ONE THE ORDER RECORDED.** `PT-1122`'s `WaitingOrder`
carries a real position in a real room; a placement needs one, and inventing
`0,0` would put a false fact in a record that already has the true one.
`combatantsIn` never reads the area when it is given `placements` — checked in
the function body, where `area.contents` is that parameter's fallback and its
only use.

**⚠ `elsewhere` IS ITS OWN FIELD**, not `present` and not `holding`. And it is
asked of `_here` rather than of the standing order: today the only way to be
elsewhere **is** to be holding position, and writing `held` there would bake
that coincidence in — which is the whole shape this change is about.

## 4 · ⚠⚠ AND ONE OF MY OWN ASSERTIONS WAS PINNING THE DEFECT IN PLACE

`BUILD 158`'s solo-mode test asserted the companion was **absent** from the
sidebar in the second room. Its stated reason:

> *"a02 declares nobody and the log said hold position, so nothing put them on
> this board"*

**The sidebar is not the board.** The assertion was correct about the board and
was reading the panel, and in doing so it locked in the defect — a green test
saying the party member should not be listed.

**Third time this file has used the sidebar as a proxy for the board** —
`BUILD 159` caught two of them in the same session. Named in the test now, so
the fourth is caught by reading it.

---

## Tests

    App  576 pass   (party_sidebar +3 · companion +1)

Mutation-checked: restoring the `_here` source fails the new case **and**
`BUILD 158`'s solo-mode case; dropping the name resolution fails the new case
alone.

⚠ `Lodestar` untouched — this was entirely a question about which source the
screen asked.
