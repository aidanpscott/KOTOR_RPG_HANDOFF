# BUILD 149 — the gate catches it now, and it caught it the same day

---

## 1 · ⚠⚠ THE SHELF-vs-EXTRACT GATE CHECK — `PT-1772`, owner ruling

`check_shelf.py`. It regenerates `base-rules` into a temp directory and
compares it with the installed shelf. **It never writes to the shelf** —
installing is a decision a person makes; this only says whether it is owed.

**⚠ IT NAMES THE ROWS, NOT THE FILE.** *"`equipment.toml` differs"* is true of
a whitespace change and of eight wrong damage dice, and a person deciding
whether to re-ship needs to know which.

**⚠⚠ EXTRACT-TO-SHELF, NOT DOCUMENT-TO-SHELF, DELIBERATELY.** A document ahead
of its extract is `check_extracts`' finding and it says so in its own words;
this one would report the same fault in a vocabulary that does not name the
cause. **One check, one question** — and `§3` below is that decision being
right on its first live case.

Watched failing **three ways** before it was kept — a stale value (the
`PT-1767` incident replayed, naming the row), a generated file the shelf does
not carry, a file in the shelf nobody generates — then watched taking the gate
from `SENDABLE` to `DO NOT SEND` and back. Blocking, as ruled: it passes by
doing your own job, and a checkout with no shelf installed passes on that
ground rather than blocking on somebody's local install state.

## 2 · ⚠⚠ AN AUTHORED DROID MAY NOT BE NAMED AFTER SOMEBODY — `PT-1772`

`DROID-MODELS-01 §0c` addresses the author in terms: *"⚠ NO PLAYER AND NO
DROID MASTER MAY USE THESE. They belong to somebody."* `PT-1729` built the
refusal for the **player**, and a blueprint never goes through chargen — so
the eight names were free to an author.

`designation.dart` said why it lives in the engine when it was written:

> *"Loom will need the same refusal the day it validates an authored droid
> blueprint — `PT-1713`'s shape exactly, where the validator and the runtime
> say the same sentence **because they call the same function.**"*

**This is that day, and the function is called rather than copied.**

**⚠⚠ THE RESERVED CHECK ONLY, AND THE SHAPE RULE DELIBERATELY NOT.**
`PT-1726`'s *"no spaces, alphanumeric plus a hyphen"* is the rule for a
**player typing their own designation**. An author who names an NPC
`Melee Droid` has not broken `PT-1722` — and **three fixtures on the live shelf
are named exactly that way** (`Droid Target`, `Melee Droid`, `OA Droid`).
Widening a chargen rule into an authoring one is *assuming a local rule is a
global gate*; a case records the decision and names all three.

**⚠ AND THE FIRST CUT COMPARED THE FILENAME.** `name` in that loop is the
file, not the character, so it tested `unit.toml` against the ban list and
matched nothing — **a value used as a key, inside a check written to catch
authoring mistakes.** Five cases went red at once and the comment stays where
it happened. Two mutations pin it: never raising the fault, and asking the
`handle` instead of the name.

`_isDroid` is now **one predicate** shared with the melee check. The second
reader is exactly when three copied lines become `PT-1468`.

## 3 · ⚠⚠ AND THE NEW CHECK EARNED ITS PLACE THE SAME DAY — `PT-1773`, `PT-1776`

`PT-1773` fixed five more Vibrosword-family weapons **after `BUILD 148` had
already re-shipped once.** The handoff, in order, unprompted:

    check_shelf     ✓ clean — CORRECTLY. The extracts had not been re-run,
                    so the shelf and the extracts genuinely agreed.
    check_extracts  ⚠ STALE equipment.json, items.json — the DOCUMENT moved.
    re-extract      →
    check_shelf     ⚠⚠ STALE items.toml — 16 lines, and it named them.
    re-ship         →
    both            ✓

**That is the three-state framing working, with one check per boundary, and
neither able to see the other's gap.** It is also why `check_shelf` reading the
extract rather than the document was right: had it read the document it would
have fired first and said *the shelf is stale*, which was **not yet true.**

## 4 · ⚠ WHAT PT-1773 ACTUALLY MOVED, AND IT IS NOT A GAMEPLAY FIX

Checked rather than assumed:

    equipment.json   rows IDENTICAL — the fingerprint changed and no
                     extracted value did. The Vibrosword BASE type has been
                     1d12 since BUILD 148.
    items.json       four names, eight rows, all 2d6 → 1d12 — Krath Dire
                     Sword, both Sith Tremor Sword rows, Echani Foil, and
                     Bacca's Ceremonial Blade's four variants.

**⚠⚠ ALL FIVE LAND IN `items.toml`, WHICH NOTHING READS.** Real document
corrections, correctly shipped, **no gameplay consequence** — said plainly
rather than letting a re-ship imply a live bug was fixed.

---

## What ran

    Lodestar   668 tests   exit 0   (+9)
    Loom       263 tests   exit 0   (+2)
    app        533 tests   exit 0
    flutter build linux     built
    gate.py                 SENDABLE — now 52 checks, the same 2 warnings
    check_extracts          1 stale, the standing event_kinds one
    check_shelf             ✓ 24 files identical

## Heads

    Lodestar        30954f0
    Loom            c48e909
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   7497018
    MAIN_WORK       d0f0369

⚠ The shelf's `items.toml` was replaced. The generated package was diffed
against the installed one first: that file was the only difference, and its
diff was eight rows.
