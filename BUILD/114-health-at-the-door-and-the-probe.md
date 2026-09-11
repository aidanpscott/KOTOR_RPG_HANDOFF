# BUILD 114 — health at the door, and the probe answers the save race

`PT-1648` built. **And the `_said` probe has an answer, and it reverses the
question.**

---

## 1 · ⚠⚠ THE PROBE — AND THE HARNESS IS WHAT BREAKS, NOT THE PRODUCT

> **`PT-1632`: why does extending `main._log` before its own `await` break
> travel?**

It does not. **It fixes the save, and `whole_loop_test` cannot survive a
correct one.**

Measured, both configurations, same fixture, one line apart:

| | events saved | `character.moved` | `Continue` resumes at |
|---|---|---|---|
| **shipped** | 32 | **1** | **`0,0`** |
| **early `_log`** | 33 | **2** | **`5,4`** |

`5,4` is where the character actually was — beside the trooper, where the fight
happened. ⚠⚠ **THE SHIPPED BUILD LOSES ONE `character.moved` AND PUTS THEM BACK
AT THE FRONT DOOR**, which is the exact defect `PT-1523` ruled against:
*"`Continue` put every character back at the package's front door."*

### Why the test fails on the correct save

Resuming at `5,4` puts the player **adjacent to a creature with a
conversation.** The walker reads its position off the status line, and for the
first frames after a reload that line is showing `_said` — the wound line,
*"Kaeda Vos: 5 of 9 — in your campaign, a01-command-deck left you at 5"*. With
no position, `walkTo` falls into its blind-press branch and presses
`arrowRight`.

**That opens the conversation.** From `_step`'s own guard — *"a conversation
takes the keyboard"* — every further arrow drives the dialogue highlight
instead of the character, so the position never returns:

    STEP 0  pos=NONE  texts=3   first=a01-command-deck
    STEP 1  pos=NONE  texts=4   first=Kaeda Vos: 5 of 9 — …left you at 5
    STEP 2  pos=NONE  texts=17  first=SITH-TROOPER.COMMAND-DECK.39
    …
    STEP 59 pos=NONE  texts=17  first=SITH-TROOPER.COMMAND-DECK.39

Fifty-eight steps inside a conversation the walker does not know it is in.

⚠⚠ **SO `whole_loop_test` HAS BEEN PASSING BECAUSE OF THE BUG.** Its walker
survives only because the lost event drops the player at `0,0`, far from the
trooper. **A test that passes only because a rule is unenforced** — a shape
already in this file, met again from the other side.

### ⚠ WHAT I DID NOT DO, AND WHY

**Not shipped.** `PT-1632` is the owner's ruling and the reason it exists is
still live: shipping this is a save-path change **plus** a harness change — the
walker needs to dismiss a conversation before it walks, or read position from
somewhere `_said` cannot occupy. That is a slice, and the owner asked for the
probe rather than a third remedy.

⚠ **BUT IT IS NO LONGER HALF-UNDERSTOOD**, which is the condition `PT-1632`
names. The question it was blocked on is answered.

⚠ **AND THE LIVE DEFECT IS THE OTHER ONE.** While this waits, `Continue`
resumes characters at the wrong square and `PT-1523`'s ruling is not held. The
race is not a latent tidiness problem; it is losing the fact `PT-1523` exists
to preserve.

⚠ **THE PROBE WAS REVERTED BY INVERSE COPY, NOT BY `git checkout`** — files
restored from saved copies and `md5sum -c` checked both back to byte-identical.
`BUILD 110` recorded why: *a destructive restore chained onto a verification
step is a bad habit even when it is caught.*

## 2 · ⚠⚠ `PT-1648` — HEALTH AT THE SCREEN WHERE A PACKAGE IS CHOSEN

`Tester`: **Tester Probe and Endar Spire rendered as identical library cards.**
The only place a fault surfaced in the app was an in-area band a player sees
**after they have already entered.** The real shelf, as of this slice:

    Base Rules        0
    Endar Spire       0
    Taris Undercity   2     ← PT-1646's own fault, found this week
    Tester Probe     14

**The tile now carries `validatePackage`'s count, in the same words `Loom`
uses.**

⚠⚠ **AND IT IS VERIFY'S ANSWER, NOT A SECOND ONE.** `PT-1546` bars a category
that is mechanical, and a tile deciding health by its own reasoning would be a
second source of truth — the shape `PT-1636` spent a slice removing from
`outOfReach`. The end-to-end case drives the real screen against the real shelf
and **demands the tile's number equal `validatePackage`'s exactly**, so a
cheaper local heuristic cannot be substituted later without failing.

⚠ **A RAW COUNT RATHER THAN A CONDITION.** *"Playable"*, *"degraded"*,
*"broken"* would be bands **I invented from a number** — a mechanical category
wearing a judgement, which is what `PT-1546` bars. The count is the fact; the
report is the detail.

⚠ **NOTHING AT ZERO** — *"a clean package must not look anxious"*, which
`verify_test` asserts one program over. **AND NOTHING WHILE UNKNOWN**, because a
package still being verified must not be drawn as clean.

### And the affirmative lives on the row, once

That leaves absence carrying two meanings — *nothing is wrong* and *nothing was
looked at* render alike. **That is precisely what happened to the in-area
band**: it had been in nearly every screenshot this thread and was never
noticed, because absence reads as non-existence.

So the library's status line says it: *"4 packages installed · checked, 2 with
problems"*, or *"· checked, none with problems"*. **One sentence says checking
happened; the tiles stay quiet unless they have something to say.** The band's
behaviour is not the defect and is unchanged — what was missing was a surface
**before** the player walks in.

⚠ **VERIFY RUNS AFTER THE SCREEN IS UP, ONE PACKAGE AT A TIME.** It opens every
area and every blueprint a package declares, and this is the FIRST screen. **A
library that waits to be verified before it draws is a worse screen than one
with no counts.**

## 3 · ⚠ AND `2 RULES UNCHECKED` NAMES ITS SUBJECT

It read identically on a clean package and a broken one **because it is not
about the package at all** — it is `record_validate`'s coverage of THIS
CHARACTER. `Tester` half-took it for several reports to mean something about
the bed, reasonably: **the line beside it in the same strip is *"N drawn and
not present"*, which IS about the package.** Two facts about two different
subjects, sharing a row and a vocabulary.

    before   Kaeda Vos · 2 rules unchecked
    after    Kaeda Vos · 2 rules about this character not checked

⚠ **LABELLED RATHER THAN MOVED.** Moving it would hide a real limitation, and
`PT-1458`'s own entry says why it is surfaced at all: *"the difference between
a rule that is not enforced and a rule nobody remembers exists."*

---

## Tests

`Lodestar` 490 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` 392 — **1,133, green.**
Pins 4/4. Gate: 2 advisory warnings, both pre-existing.
