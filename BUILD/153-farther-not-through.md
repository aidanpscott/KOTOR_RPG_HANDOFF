# BUILD 153 — farther, not through; and the sidebar question answered

---

## 1 · ⚠⚠ THE SIDEBAR QUESTION — NO, IT DOES NOT IMPLEMENT THE LOCKED DESIGN

Asked directly, answered directly. `APP-UI-VISION-01` has a real, locked party
sidebar design, and **`RosterPanel` is not it.** They were built independently
and the play screen never read the document:

    grep APP-UI-VISION lib/play/roster_panel.dart   → 0
    grep APP-UI-VISION lib/play/play_screen.dart    → 0

Elsewhere the app cites it constantly — `package_main_menu`, `console_home`,
`step_strip`, `menu_button`, `pulse_clock` all quote it by section. **The play
screen is the part that was built without reference to it.**

| locked | built |
|---|---|
| **`PT-1111`** docked **LEFT**, explicitly *"correcting the right-edge placement the party rail also mistakenly drifted into"* | docked **RIGHT** — second child of the board's `Row`, with its rule on its left edge |
| **`PT-1124`** the sidebar **runs during exploration**, party always visible | **combat only** — `if (_roster.isNotEmpty)`, and the roster closes on `encounter.ended` |
| **`PT-1132`** a **portrait**, seven signals, *condition never statistics* | **text rows and bars** — no portrait anywhere in the file |
| **`PT-1132`** *identical treatment for the player and every party member* | **two treatments** — *"the player's own row, drawn as a card rather than a line"* |
| **`PT-1110`** *no separate target plate — the sidebar IS the target display* | **not clickable at all** — no `GestureDetector`, no `onTap` |
| **`PT-1102`** collapsible, a thin tab visible in both states | **not built**; and no party rail on the package main menu either |
| **`PT-1133`** ordering: personalised out of combat, shared initiative in it | turn order exists **in combat**; there is no out-of-combat panel to personalise |

**⚠ WHAT `PT-1735` ONWARD ACTUALLY BUILT WAS THE RULES HALF, NOT THE UI.**
Those slices touched `attack.dart` and `play_screen.dart` only — sides, the
wipe rule, the roster fold, `partyIn`, recruitment. **A companion shows up in
the existing panel because membership is a fold, not because anything
implemented `PT-1102`.** So the companion work is not *wrong* against the
design; it is **orthogonal to it**, and the sidebar remains unbuilt.

> **⚠ AND `RosterPanel` IS NOT WASTED EITHER.** Every fact the locked portrait
> needs — who is in the fight, vitality, standing, hidden, waiting, present —
> is already computed and already folded. What is unbuilt is the presentation
> and the position, not the data behind it.

**⚠ THE COMPANION-vs-HENCHMAN GAP IS REAL AND IS THE OWNER'S.** Confirmed from
this side: `roleNames` has four values, `isParty` collapses every one of them to
*not an enemy*, and **nothing in the panel or the board distinguishes a
companion from a henchman.** The design document does not distinguish them
either. **That is a gap in the design, not an omission in the build.**

## 2 · ⚠⚠ `PT-1782` BUILT — A LONG WEAPON RAISES THE FLOOR

> *"Marksman Rifle and Sniper Rifle both extend their wielder's perception
> range to match their own weapon range, passively, respecting line of sight."*

**The column first.** The property was ruled and stated in the **prose beneath**
the ranged table, so `equipment.toml` shipped both rifles without it for two
slices — *ruled and unbuilt*, exactly how `PT-1718` sat for months. `Extends
perception` is a yes/no column now, with the three-state treatment `balanced`
already has, and **it carries no number of its own**: the ruling extends
perception *to match the weapon's own range*, which the `Range` column holds
beside it, and a second number could disagree with it.

**Then the rule.** `perceptionSquares(base:, extendedTo:)` — **the larger of the
two**. `PT-1686`'s rule is untouched: `§3c`'s field is the *creature's* range
and an author who narrows it narrows both. This is a **floor the wielder
brings**, so a pistol reaching 24 m takes nothing away from somebody who sees
20.

**Then the detection.** `_detectAtRange` asks it. Three cases on `PT-1686`'s own
board, where **the only difference is what the player is holding**:

    eleven squares, vibroblade   not noticed   (the existing control)
    eleven squares, sniper rifle NOTICED       25 squares from 50 m
    behind a wall, sniper rifle  not noticed   farther, not through

The wall case carries the rifle **specifically** to prove the extension buys no
way through — the ruling says so outright so it is not built as x-ray vision.
The vibroblade case is the instrument check: if the others passed because of
the board rather than the weapon, it would find the same creature.

## 3 · ⚠⚠ I STARTED TO WRITE THIS CONVERSION TWICE IN ONE SLICE

`metres ÷ 2 = squares` already existed **twice over**, and I reached for a
third:

    round.dart       squaresFromMetres(int)      since PT-1589 — the ruling
                                                 ABOUT this unit crossing a
                                                 seam twice
    item_open.dart   rangeSquaresFrom(String?)   parses this exact column, and
                                                 guards a zero range

I wrote `metresCellToSquares` in `sight.dart` **under a doc comment warning
against exactly that**, and the compiler caught it on a duplicate export. Then I
rewrote it to delegate — and found the second incumbent, which already did the
whole job. **Both copies deleted; a case now asserts the two survivors agree**,
so the next person reaching for a fourth finds it named.

## 4 · ⚠ AND `check_shelf` CAUGHT ME, TWO SLICES AFTER I BUILT IT

The acceptance failed on its first run. Not the rule, not the wiring: **I had
added the column to the document and the extract and not re-shipped
`base-rules`.** The check named `equipment.toml` and the two lines.

> **That is the gap it was built for, catching its own author rather than
> `Tester`.**

---

## What ran

    Lodestar   682 tests   exit 0   (+14)
    Loom       263 tests   exit 0
    app        550 tests   exit 0   (+3)
    flutter build linux     built
    gate.py                 SENDABLE, the same 2 advisory warnings
    check_extracts          38 comparisons · stale 0
    check_shelf             ✓ 25 rules files identical
    check_engine_pin        4 compared · all level

Mutation-checked: the weapon never extending, and the creature's own range
dropped — each kills at least one case, in opposite directions.

⚠ Also re-extracted and re-shipped `PT-1792`'s four rows mid-slice — the sixth
Vibrosword miss and the three Training Lightsaber threats.

## Heads

    Lodestar        f1c2cc0
    Loom            7a0ca16
    Lens            e59ff95   (unchanged)
    KOTOR-RPG-APP   8626028
    MAIN_WORK       9f2b2ed
