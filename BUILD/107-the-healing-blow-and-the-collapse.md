# BUILD 107 — the healing blow, and the collapse

Lodestar `9aa7382` · Loom `802dec5` · app `660134a`.
Lodestar 463 · Lens 7 · Loom 236 · app 367 — **1,073 green.** Pins level.
Gate SENDABLE.

---

# ⚠⚠ `PT-1622` — A CREATURE WITH STRENGTH 1 HEALED WHAT IT HIT

`Tester` built `probe-feeble` **so a fight could be survived.** Probe Walker
went **1 → 3 → 4 by being struck.**

    str 1  →  −4 modifier          the attack roll was right; `− Strength 4`
    unarmed   1d3                  belongs there
    rolled 1  1 − 4 = −3           and that went to applyDamage as an amount

**⚠⚠ AND `applyDamage`'s OWN COMMENT NAMED THE CONTRACT** — *"a negative
`amount` reaching `applyDamage` is a caller's own business rather than a hidden
feature."* **The caller is `strike`, and it was not minding that business.**

## Clamped where the total is computed

`resolveAttack`, the one place the number exists. **Not in every caller** — a
clamp per caller is the rule-applied-to-one-path family waiting to happen, and
that family stands at twelve.

**⚠ AND IT DOES NOT TOUCH `heal`.** That path hands `applyDamage` a negative
`amount` deliberately and **never comes through a damage expression** — so the
deliberate negative still works and the accidental one cannot. A clamp inside
`applyDamage` would have broken healing; that is why the site matters.

**⚠ AND IT IS NOT AN EXOTIC VALUE.** Loom's New Creature takes the six abilities
as free numbers, and **any Strength below 8 gives a negative modifier.** A case
walks 1, 3, 6 and 7.

## ⚠⚠ AND A HIT THAT DOES NOTHING IS STILL A HIT — a third sentence

    out of reach     PT-1593 — a swing that could not be taken
    miss             a swing that failed
    grazed           a swing that LANDED and did nothing

`damage 0 — 1d3 1 − Strength 4 — not enough to hurt`. **The derivation survives
the floor** (`PT-1326`): a player who sees the negative term and a total of 0 can
tell a rule from a bug; one who sees only `0` cannot.

---

# ⚠⚠ `PT-1623` — EVERYTHING STARTS COLLAPSED

    left    areas and conversations, and nothing under them
    right   its kinds and no contents

## ⚠ AND *"UNDER THEM"* IS THE AREA'S CONTENTS, WHICH IS THE RULING'S OWN PARALLEL

The right pane shows its **kinds** and no **contents**; the left shows its
**areas** and no **placements**. **Collapsing the area LIST as well would leave
an author who just opened a package unable to see what is in it** — a wall
rather than a focus, and the reason given is attention.

## ⚠⚠ AND MY REASON FOR THE OLD DEFAULT WAS WRONG

`BUILD 105` defaulted the palette to `terrain` and I wrote *"an empty right pane
on open is a pane that has to be learned."* **The ruling is about attention
rather than tidiness** — everything dropped at once is distracting and there is a
lot to scroll through — and **a selector whose rows are all you see is not
unlearnable; it is the only thing on the pane.** `PT-1620` measured the same
thing from the other side.

## Two decisions inside it

**⚠ THE TWIST IS ITS OWN TARGET.** Tapping the NAME opens the area on the board,
which it has always done. **Expanding is a different verb and must not steal that
tap** — one row, two gestures, and the glyph says which is which.

**⚠⚠ AND A SELECTION FROM THE BOARD REVEALS ITS AREA.** `PT-1553` makes these
**two views of one selection**; a selected row hidden inside a collapsed area
would be one view quietly not showing it, which is the disagreement between two
surfaces this project keeps finding.

---

# ⚠ AND THE TWO ONE-LINERS, BOTH FIXED WHERE THEY ARE READ

**`didYouMean` is deduplicated on the fault**, not at the site that builds it —
`PT-1622`'s own principle, one file over. An area declaring two arrivals with the
same name offered *"did you mean: north, north"* **two rows above the fault that
explains why.** Order is kept: the list is the area's declaration order, which is
what the author is looking at.

**`a arrival point` → `an arrival point`.** The note is BUILT from the way's
name, which is right; **the article was hand-written beside it, which is the half
that cannot follow the data.** A vowel test, not a grammar engine — the two ways
are `arrival point` and `doorway` and anything cleverer would be a rule nobody
asked for.

**⚠ AND ONE OF MY OWN CASES WAS ASSERTING THE DEFECT.** `palette_test` read
`expect(find.text('an arrival point, painted'), findsNothing)` with the reason
*"the note is built from the way name, not hand-written"* — **it was pinning the
wrong article as correct.** Fourth time a test has held a defect in place; the
count is worth keeping.

---

# ⚠ WHAT ASSUMED THE OLD SHAPE — NINE

    two_trees × 3      the tag, the leaf selection, and the new collapsed group
    faults_on_rows × 3 every marked row is inside a collapsed area now
    palette × 2        terrain was the default page; and the article case
    mode_selector      "one mode at a time" opened on terrain
    new_package        the tiles were visible from the first frame

**⚠ And one is not an assumption but a consequence worth stating:** the disarm
count went from two to three, because **entering `terrain` is now a mode change
too.** The case says so rather than being adjusted to fit.

---

# ⚠ AND ONE THING I COULD NOT DO

**Loom will not build on this machine: `cmake` is not installed.** `flutter build
linux` stops at *"CMake is required for Linux development"*, and `which cmake`
finds nothing. The existing `build/linux/x64/debug/bundle/loom` is from
**8 September** and predates everything from slice one onward, so running it
would show a Builder several slices old rather than this one.

**`apt install cmake ninja-build` and `STATE.md`'s `env.sh` clang shim are what
it needs** — and the shim is already recorded there as *"not optional"*, because
a cold build without it dies with `CMAKE_CXX_COMPILER not set`.

---

# STILL OPEN

`character.downed`'s `campaign` lifetime, now that `dying` sits beside it at a
different one · the icons, which `PT-1366` makes separate work · `§5` has no
second interaction the product can reach · the two deferrals in `STATE.md`.
