# BUILD 154 — the sidebar, built to the design that was already locked

---

## 1 · ⚠⚠ WHAT WAS WRONG, AND IT WAS THE POSITION AND THE PRESENTATION

`RosterPanel` and `APP-UI-VISION-01`'s sidebar were built independently, and
**neither play-screen file cited the document once** while five other files in
the app quote it by section. `PartySidebar` is built to it:

| | was | now |
|---|---|---|
| **`PT-1111`** | docked **right** | **docked left**, correcting the drift the ruling itself names |
| **`PT-1124`** | combat only | **runs during exploration** — the party is why it exists, so it no longer asks the fight whether to be drawn |
| **`PT-1132`** | text rows and bars | **a portrait** — vitality the left wing, Force the right, both full-height and flanking, name · class · level beside them |
| **`PT-1132`** | player a **card**, everyone else a **line** | **one treatment**; `self` is a selection border and nothing else |
| **`PT-1133`** | one shape for everybody | **an enemy is the inversion** — bar above the portrait, name only, fixed red |
| **`PT-1133`** | join order | **self first out of combat, initiative order in it** |

The ordering is applied by the screen, not the panel: **which order applies is
a question about the fight**, and the screen is what holds the fight.

## 2 · ⚠⚠ WHAT IS DELIBERATELY NOT BUILT, AND WHY EACH ONE IS NOT "LATER"

**A signal with no mechanic behind it cannot be drawn without inventing the
state it reports.**

    the four condition markers   disabled · debilitated · level-up pending ·
    (`PT-1132`, `TRACE-30`)      buff/debuff with a count badge
                                 ⚠ NO MECHANIC EXISTS for any of them. There
                                 is no effects system, no debilitated state,
                                 and no level-up.

    the XP wing and readout      `progress` carries `xp` and it is always 0,
    (`PT-1132`)                  and NO XP-to-next-level total exists anywhere
                                 in the rules. A bar with no denominator, or
                                 one I chose, is worse than its absence.
                                 `level` is real and IS shown.

    click-to-target              this screen has ZERO pointer handling, and
    (`PT-1110`)                  `PT-1443`'s click-to-move is the ruling
                                 already waiting on that question. The first
                                 click into this screen is its own slice.

    the main-menu party rail     a different screen, and `PT-1102`'s rail is
    (`PT-1102`)                  about multiplayer seats and invite slots,
                                 which do not exist.

The portrait is the placeholder `UI-ASSETS-01 §2` already records — *"currently:
a filled circle"* — because no portrait art exists and `IdentityScreen` says so
to the player's face.

## 3 · ⚠⚠ AND I FOUND A DEFECT I HAD JUST WRITTEN

Out of combat the player is in **neither** list the entries are built from:
`_here` holds *placements* and the player is not one, and
`f.encounter.combatants` is empty between fights. So the player's own entry
read

    Vess Taran · in the fight, and the round does not hold it · 0 of 10

**for the entire walk** — which is the first thing `PT-1124`'s whole point, an
exploration sidebar, would have shown. `me` is the fallback now.

> Found by reading the failure text of a case that was failing for a different
> reason, which is the third time this month that has paid.

## 4 · ⚠ EVERY INCUMBENT STRING IS KEPT

`hidden`, `noticing`, `N of M`, the Force readout and `exhausted from` all
moved across unchanged. **Renaming a state while moving it is how a guard stops
matching something that is still true** — and each of those words has a case
watching for it.

`PT-1422`'s turn-order strip moved across too. `PT-1133` makes the sidebar's
ORDER the turn order, which is delivered by the entries arriving sorted — **it
does not make the initiative numbers or the whose-turn-now mark redundant**, and
dropping them with the panel that held them would have been a deletion nobody
asked for.

**⚠ THREE EXISTING CASES CHANGED THEIR EVIDENCE AND NOT THEIR CLAIM.** Two used
the panel's **absence** as *the fight ended* — true while it was drawn from the
fold, and a constant once `PT-1124` makes it permanent. They read `inCombat`
now, which is the same fold one step closer to the fact.

---

## What ran

    Lodestar   682 tests   exit 0
    Loom       263 tests   exit 0
    app        556 tests   exit 0   (+6)
    flutter build linux     built

Mutation-checked: removing the sidebar kills five cases; docking it right kills
the left-dock case.

## Heads

    Lodestar        f1c2cc0   (unchanged)
    Loom            7a0ca16   (unchanged)
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   01cc030
    MAIN_WORK       9f2b2ed   (unchanged)

---

## ⚠⚠ ONE THING THE DESIGN DOES NOT ANSWER — flagged, not solved

**Nothing distinguishes a companion from a henchman**, on the board or in the
sidebar, and `APP-UI-VISION-01` does not distinguish them either. `roleNames`
carries four values and `isParty` collapses every one of them to *not an
enemy*. Excluded from this slice at the owner's instruction and raised here as
a **design** question rather than an unbuilt one.
