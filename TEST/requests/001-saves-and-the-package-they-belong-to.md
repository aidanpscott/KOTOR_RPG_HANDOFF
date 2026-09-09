# 001 · Saves, and the package they belong to

**From `Coder`. Answers `PT-1443`'s save defects and `PT-1445`'s ruling.**

`Lodestar` `f7fe50d` · `Lens` `04e4061` · `Loom` `b2308e1` · app `3d97d52`

---

## Why you are being asked

**`PT-1443` found six defects in ten minutes of using it, while 197 tests
passed.** Five of those defects are now fixed and **the fixes are the kind that
tests are bad at judging** — they are about what a menu offers, what a button
does, and whether two saves are distinguishable. **The suite cannot tell me a
disabled row looks broken.**

---

## The journey

**Do this on the real machine, with the real folder open beside you.**

    cd ~/kotor-repos && ./run-app.sh

**1 · Make a character in `Endar Spire`.** All nine steps. Play. Then quit the
app completely.

**2 · Reopen. Press `Continue`.** You should get the same character.

**3 · Now go back to Console Home and open `Taris Undercity`.** Look at
`Continue` and `Load Game`.

**4 · Go back and open `base-rules`.** Look at the whole menu.

**5 · Make a second character in `Taris Undercity`.** Play, quit, reopen,
`Continue` — then check `Load Game` in **both** packages.

**6 · In the hub, press `Back`.** Then find your way forward again.

**7 · At the character entry screen, read the two options.**

---

## What I claim — try to make these false

1. **`Continue` and `Load Game` in `Taris Undercity` do not offer the
   `Endar Spire` character**, and vice versa. Each package offers only its own.
2. **`base-rules` offers no `New Game`, no `Continue`, no `Load Game`**, and
   **says why on screen** rather than just greying out.
3. **`Continue` on `base-rules` does not red-screen.** It previously did.
4. **`Back` from the hub returns you to where you came from** and does **not**
   drop you into a game.
5. **The entry screen reads `Select Premade Character`**, not `Select Premade`.
6. **A save survives a full quit** — the character, and the wound if you were
   hurt.

⚠ **Claim 1 is the one I most want attacked.** It is the ruling that never
reached the code, and the fix reads every save's log to answer a question the
header cannot — see *undecided*, below.

---

## ⚠ What I could not see from where I sit

- **Whether a disabled `Continue` reads as "not yet" or as "broken."**
  `APP-UI-VISION-01` says disable means *not yet* and hide means *not
  applicable*. I added a line of text to `base-rules` saying it supplies rules
  and not a place to play. **I cannot tell you whether that line lands or
  whether the screen still looks faulty.**
- **Whether two saves are distinguishable to a person.** The header carries
  **no name, no time, no character and no package** — so `Load Game` shows what
  little it has. **`PT-1443` said two saves looked identical. I do not know if
  they still do.**
- **Whether `Back` now goes somewhere that feels like back.** It goes to the
  pre-hub boundary. That is correct and may still be surprising.

---

## What I already ran — do not repeat it

**591 tests, all green**, immediately before pushing:

    Lodestar 270 · Lens 4 · Loom 111 · KOTOR-RPG-APP 206

**Nothing is red.** If you see a failure, it is new and it matters.

---

## ⚠ Known scaffolding — NOT bugs, do not file these

| | why |
|---|---|
| The weapon is **a fist** | Nothing resolves equipment in play yet. The trooper does carry a rifle in its blueprint |
| The portrait is **a filled circle** | `PT-1319` — no portrait art exists, and none is ours |
| The board is **drawn, not textured** | `AREA-FORMAT-01 §2b`'s untextured default. No tileset has been imported |
| The purse is **hardcoded** | Route 2 needs a credit value that is not written |
| **Nothing has been designed** | Sizes are right — `BUILD/32` re-derived them against real viewports. **Typography, palette and framing have never been touched.** What you will see is structure at a correct scale |

**The full list of nine is in `HANDOFF/docs/RUNNING-ON-THIS-MACHINE.md`.**

---

## ⚠ Wrong versus undecided

**Rulings live in `MAIN_WORK/playtest/PLAYTEST-RULINGS-01.md`, and the current
state of every open question is `HANDOFF/BUILD/STATE.md`.** Read `STATE.md`
before filing — several things that look like defects are **open questions with
nobody's answer yet.**

**Known undecided, already on the owner's plate — file as questions, not bugs:**

- **What a save is NAMED, and how many.** The header has no name, time,
  character or package. **`Continue` cannot order saves without a field the
  format does not have**, and `listFor` reads every log to find the package.
- **"The same place" is the entry area.** `character.moved` is `session`
  lifetime, so **by the vocabulary's own rules a save cannot know where you
  were standing.** Walk to the second area, quit, `Continue` — you arrive back
  at the first. **That is the spec, not a bug.**
- **The side panel**, click-to-move, and key bindings. Wanted, not built.

---

## ⚠ Data safety, and what is real

**All four suites are hermetic as of `3d97d52` and `b2308e1`** — I snapshotted
`~/.local/share/kotor-rpg/` by mtime around a full run of all four and it is
untouched. **Run them as often as you like.**

**⚠ But USING the app is not a test.** It writes **real saves to the real
folder**, because that is the product working correctly. So:

    ~/.local/share/kotor-rpg/saves/       your saves land here, for real
    ~/.local/share/kotor-rpg/packages/    the shelf — endar-spire is the test bed

**To start clean:** delete the `.sav` files in `saves/`. **⚠ Do not delete
anything under `packages/`** — `endar-spire` is Loom's output and the fixture
every suite reads. If you damage it, say so rather than rebuilding it; it is
`Coder`'s to regenerate.

---

## What not to touch

**Write only `HANDOFF/TEST/reports/`.** Not the product repos, not `MAIN_WORK`,
not `HANDOFF/BUILD/`. **Do not fix anything you find** — `PT-1446`, and a
tester that fixes is a second builder.

**Report as `reports/001-saves-and-the-package-they-belong-to.md`.**
