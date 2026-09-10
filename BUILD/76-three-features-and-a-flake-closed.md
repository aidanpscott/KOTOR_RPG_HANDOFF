# BUILD 76 — `PT-1519`, `PT-1517`, `PT-1509`: three features, and the flake closed

**813 green** — Lodestar 372 · Lens 5 · Loom 131 · app 305.

---

## ⚠ `PT-1519` — a remainder that is not the square count

    ◆ 6 → 4   shown while standing BESIDE rough ground, before any step

**One number cannot show a cost that has not happened**, and the square count is
exactly what a player would guess wrong. `Value` and `ValueAfterUse`, with the
arrow as the sliver.

⚠ **THE DIRECTION IS NOT KNOWN AND DOES NOT MATTER.** `PT-1513` put the
multiplier on the **creature** and the source on the **ground kind**, so every
difficult neighbour costs the same: *"stepping onto rough ground would leave 4"*
is unambiguous however many there are. **The shape of `PT-1513` is what made
the keyboard case tractable.**

⚠ A remainder below zero is **not shown** — `canAfford` already refuses that
step, and `1 → -1` would describe a move that cannot happen.

## ⚠ `PT-1517` — five budgets, and shape carries identity

    ◆ move · ● action · ▲ bonus · ■ gear · ✶ reaction · per encounter

⚠ **A spent pip goes grey WITH ITS SHAPE INTACT**, which is the ruling in one
class: `spent` never changes the path.

⚠ **THE SQUARE IS MINE AND THE CODE SAYS SO.** The ruling assigns four shapes
and `gear` is the fifth budget with none.

⚠ **FOUR IS THE THRESHOLD**, measured — counted below, a numeral above.

⚠⚠ **THE REACTION POOL IS LABELLED, AND ONLY IT.** `PT-1422` made it the one a
naive implementation gets wrong: four of five reset per **turn** and reactions
are **per encounter**, so an unlabelled empty slot reads as *"spent this turn"*
and a player waits for it to come back.

⚠ **A bonus nobody granted is ABSENT, not grey.** Its own comment says it does
not exist; a grey pip is a promise.

⚠ **DRAWN, NOT JOINED INTO THE PANEL.** Shape cannot be a string — and the panel
is one `Text` with `maxLines: 2`, so a sixth clause there is `BUILD 69`'s
truncation. A pip row costs one line of height and cannot be ellipsed.

## ⚠ `PT-1509` — the map is memory, and the perception half is left alone

`m` toggles the areas this character has stood in, in the order they first did.
**An area never entered is ABSENT, not greyed** — you do not know a room exists
until you have been in it, and a greyed row promises one, which is `PT-1500`'s
defect in a different pane. **Nor is it the manifest's order:** `[order].areas`
is what the *package* has, and sorting by it leaks how many areas there are and
where the gaps in your knowledge fall.

⚠⚠ **AND THE RULING'S PREMISE HELD FOR A DIFFERENT REASON THAN IT GAVE.**
`PT-1509` calls the map *"nearly free"* **because `area.entered` is campaign
lifetime** — and **`area.entered` has no constant, no producer and no consumer
anywhere in this project.** Declared and entirely unimplemented. The map folds
`character.moved` instead, which carries `area` and has been written at every
arrival since `PT-1523`.

⚠ **A FOURTH STATE, AND ALL THREE CHECKS ARE BLIND TO IT** — recorded in
`EVENT-KINDS-01 §3d`. A kind with **neither end** is invisible to *emitted and
undeclared*, *declared and ignored by replay*, and *a fold with no producer*.
**It is not added to the check, deliberately:** "declared and unimplemented"
describes most of the vocabulary and that is a **roadmap**, not a defect — and a
check that flags a roadmap is a check somebody switches off.

⚠ **THE PERCEPTION HALF IS NOT BUILT, ON THE RULING'S OWN INSTRUCTION:** *every
creature needs a detection state per observer… **unruled, and it should be ruled
before it is built.***

---

## ⚠⚠ THE FLAKE WAS A PATTERN, AND IT IS CLOSED

**Four occurrences across two slices, and every one was the same thing:** a
**fixed millisecond budget around a real disk read**, ample alone and not ample
in a full run with four isolates competing.

> **The project's own rule was already written — in `Loom`:** *"⚠ WAIT FOR IT
> RATHER THAN SLEEPING AT IT. A fixed delay made this flaky against a real disk
> read."* **The app had never adopted it.**

⚠ **AND THE BRITTLE WAIT AND THE REPORTED SYMPTOM WERE IN DIFFERENT PLACES.**
`play_walk_test` reported *"Command Deck not found"* at the **round trip**, and
the wait that was too short was the **50ms for the entry area to open** — the
very first assertion. I fixed the two travel waits first and it flaked again.

⚠ **One wait was wrong in an instructive way:** `walkTo` is **still walking**
when the travel fires — its target is the door square and the arrival lands
elsewhere — so the arrival message is cleared by the next step. It waits for the
**area id**, which persists.

**Three consecutive clean full runs**, then two more since.

---

## ⚠ `PT-1527` — the producer refuses the pair now, and I could not reproduce it

`PT-1515`'s projection refused a revive after a death, and its comment said why:
*a projection that depends on a producer being careful is a projection with a
rule it does not enforce.* **`TEST 022` met the actual producer two slices
later.**

⚠⚠ **I COULD NOT REPRODUCE IT ON HEAD AND SAY SO** rather than claiming the role
guard was the whole story. A controlled test — **with the control being that the
creature must actually die, or the absence of a revive is vacuous** — kills a
creature and writes no revive.

**What is certain is that `role` is the wrong thing to lean on alone:** it is a
fact about **an object the fight is holding**, and the pair is a fact about the
**log**, which is what outlives the fight and is what `Tester` read. The guard
asks the log now.

⚠ **And `PT-1524` removed the mechanism that let a dead enemy return:** the
projection floors a dead subject to 0, and under `PT-1515` an enemy at 0 was
`down` — so it came back into `_here` and re-crossed the threshold. **That is
where six deaths for one creature came from.**

## Still open

- ⚠ `PT-1509`'s **board/perception** half — per-observer detection is unruled.
- ⚠ `PT-1528` — Strength buys no damage. Ruled this slice, unbuilt.
- ⚠ `tester-probe/sentinel-challenge` needs a **failure node**.
- ⚠ The conversation editor has **no button for `unlink`**.
- `PT-1484` unblocked; `PT-1485`; the effect columns; 45 annotation cells.
- ⚠ `AGENDA-CURRENT.md` forked — **left, as ruled.**
