# 30 · The dialogue screen

**256 Lodestar tests · 203 app · 101 Loom.** All three analyze clean.
**Four captures in `BUILD/screens/dlg_*.png`.**

---

## 1 · It sits over the board, and the board keeps its height

**A `Stack`, not a `Column`** — `PT-1264` keeps the play surface a major view,
so the board does not shrink when someone speaks. **KOTOR cut away entirely.**

**⚠ Coverage is a CAP, not a height, and the first number was wrong.** A fixed
third covered the room when the panel had one line and **clipped itself when it
had five** — the test found only **two of five options drawn.** The panel now
sizes to its content under a **half-height ceiling**, which holds four.
**`STUDY 18` found source nodes offering up to seven**; nothing rules the
number and this one is mine.

**⚠ And past the cap it scrolls, which is a defect rather than a feature.**
`§4c` records hiding-not-greying as the thing KOTOR got right *because "the
list is always plausible"* — **which assumes you can see the list.** A
scrolled-off option is hidden by furniture rather than by a gate. **Named, not
solved.**

---

## 2 · `§4c`'s colours, drawn for the first time

    AMBER  [Persuade]              a real check — IT ROLLS
    GREY   [Lie]                   manner — no roll, pure tone
    TEAL   [Human]                 who you are — no equivalent in either game
    BONE   [Bribe · 50 credits]    a price — PT-1315, the one number

**⚠ NO NUMBERS ON A CHECK.** `[Persuade]`, and you roll — `PT-1307`, asserted.

**⚠ A SHUT OPTION IS NOT DRAWN AT ALL.** The runtime drops it and the panel has
**no styling for one**, so `PT-1429`'s live alternative is not half-built by
accident.

**⚠ AND THE BRACKET IS DERIVED.** There is no `label` field in the format, so
nothing an author typed can disagree with what rolls.

---

## 3 · ⚠⚠ What the capture found that no test did

**Three things, and the second is the one that matters.**

- **The room read through the words.** At 95% opacity the grid lines and the
  trooper's own marker were visible **behind the reply text**. `PT-1264` wants
  the play surface visible; **it does not want it under the sentences.** Opaque
  now — the surface stays visible *above* the band.
- **⚠⚠ I drew the price in `accent` beside teal `[Human]`.** Two greens a shade
  apart, in the screen whose whole purpose is one-colour-one-meaning. **That is
  `TRACE-93`'s defect and it is the second time this design has reproduced it**
  — `PT-1307` caught the first, three exchanges after the finding was filed.
  **`§4c` assigns amber, grey and teal and says nothing about a price**, so a
  price is now drawn in ordinary reply bone and carries its meaning in its
  words.
- **`[human]` was lowercase and was an id.** It sat beside `[Persuade]` and
  read as a different kind of thing. `§4c`'s own example is `[Zabrak]`.

**⚠ And one it found that is not fixed:** the panel's top edge **cuts the row
the speaker is standing in.** You can see the room and not the square you are
talking across. That is the coverage question in its sharpest form and it wants
a real viewport.

---

## 4 · The typed box, with no AI in it

**`PT-1303`: typing something that MEANS an authored reply counts as picking
it.** The box exists now because **the AI lands in it later and building it
afterwards would reshape the screen.**

**⚠ WHAT "MEANS" IS IN THIS BUILD, STATED PLAINLY.** `PT-1303` requires
**recognition against a fixed set**, not free-form similarity — *"an AI
recognising which authored option you meant"* is a menu's job. **`§7` leaves
the topic taxonomy open — "shape settled, list not"** — so the fixed set here
is **the option list itself and the bracket words** (`persuade`, `lie`,
`human`), matched on normalised text.

**That is the degenerate case of the mechanism:** enough to test the screen,
**not enough to talk.** Nothing computes a similarity and nothing guesses.
**The AI replaces one function and touches nothing else.**

**⚠ And a fired branch is visible as it fires — `PT-1304`.** The first Enter
shows *"that is: …"* and highlights the option; the second commits. **A player
never learns from consequences that the plot moved on a misreading.**

**⚠ Text that reaches nothing says so** — `§4.3` answers and returns, and with
no AI it reports that rather than pretending.

---

## 5 · Where the conversation starts — and a thing I broke and fixed

**A blueprint may name its conversation** — `conversation = "dialogue/…"`, the
one line `DIALOGUE-FORMAT-01 §8` said it would need. **Walking into a creature
that has one talks to it; one that has none is attacked.** Hostility is a data
question rather than a special case.

**⚠ AND THAT MADE THE FIGHT UNREACHABLE.** Two existing tests failed, and they
were right to: walking into the trooper opened the tree forever and **combat
was gone.** The rule now is **talking happens first and a fight is what happens
once talking is over** — a per-visit set, as transient as the fight itself.

**⚠ It is a placeholder and the real answer is a conversation that ENDS IN A
FIGHT.** `§5` has no effect kind for that and none is invented here.

**⚠ AND THE TEST SUBJECT IS WRONG, AS FLAGGED.** A Sith trooper that talks
instead of shooting is the only creature in the bed. Nothing rules what makes a
creature hostile.

---

## 6 · ⚠ Two debts, named

- **⚠ THE CONVERSATION FILE IS HAND-WRITTEN, AND THAT BREAKS `PT-1346`.** The
  test bed is meant to be the Builder's output. **Loom has no dialogue editor
  and this slice was told not to build one**, so this is the first package
  content in the project the Builder did not make. **The Builder owes a
  conversation editor.** The file says so on its first line.
- **`credits` is a named placeholder constant** in the play screen. Nothing
  projects a purse, and without it `§4c`'s price could not be drawn at all.
  Same standing as `plainAggression`.

---

## 7 · Not built

No AI, no escalation, no character brain, no Loom editor. **And `§6`'s speaker
override is not exercised** — it needs a second creature in the area and the
bed has one, which the conversation file records where the field would be.
