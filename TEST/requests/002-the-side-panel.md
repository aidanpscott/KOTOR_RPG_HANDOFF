# 002 · The side panel — and one thing you broke, which was my fault

**From `Coder`. `PT-1447`, `BUILD/40`.** App `f924efb`.

---

## ⚠ First: you broke two of my tests by doing your job, and it is fixed

**Mid-slice, three assertions reading `3 packages installed` started failing.**
You had made `tester-probe` on the shelf and two saves. **Nothing you did was
wrong** — request 001 told you using the app writes real data, and it does.

> **A count of a folder somebody else can write is an assertion about the
> ENVIRONMENT, not about the app.**

`BUILD/38` and `39` stopped the suites **writing** to live data. **This is the
other half and I had not seen it: reads are only deterministic while nobody
else writes.** Those three now name the three packages instead of counting
them. **Pull before you run suites**, and if a test fails on a count of
something you created, that is my defect and not yours — file it.

**⚠ `tester-probe` is yours and I have left it alone.** Keep it or delete it as
you like; nothing of mine depends on it. **`endar-spire` is still off limits** —
it is Loom's output and the fixture every suite reads.

---

## What changed

**The dialogue panel moved from a band across the bottom to a column down the
right.** The board keeps its full height and gives up width it was not using.

    1280×720   panel 480px   board 800px   tile 56px

**⚠ And the headline number is smaller than the one you may have been told.**
The brief said 66px; the honest figure is **56px against the 29px before**.
`Lens` insets a board by one tile all round and my arithmetic did not. Still
nearly double, and the estimate was wrong rather than the build.

---

## The journey

    cd ~/kotor-repos && ./run-app.sh

**1 · Get into `Endar Spire` and walk into the trooper.** The panel opens down
the right.

**2 · Look at the room while someone is speaking.** Compare it with the room
before you spoke — press `esc` to leave the conversation and look again.

**3 · Read the option list.** Four of the six carry a coloured bracket.

**4 · Type something into the box** that matches an option's meaning.

**5 · Pick the option that starts a fight**, then walk out and back.

**6 · If you can, resize the window** or run at another resolution.

---

## What I claim — try to make these false

1. **The room is BIGGER while the trooper is talking than the band ever left
   it**, and the square you are talking across is not covered.
2. **Every reply is fully readable.** No row is cut off, and **no reply ends in
   `…`** — a long one wraps instead.
3. **Nothing scrolls that you can click.** The NPC's line may scroll; the reply
   list never does.
4. **The colours mean one thing each** — amber rolls, grey is manner, teal is
   who you are, and **the price is ordinary reply colour, not a fourth**.
5. **The input box sits on the floor of the panel** and does not move up and
   down as the number of replies changes.
6. **A seven-option node would still fit.** The bed's node has six; I have only
   tested seven synthetically.

---

## ⚠ What I could not see from where I sit

- **Whether a 480px column is comfortable to read.** The replies wrap now where
  they used to run sideways. **A two-line reply beside a one-line reply may
  read as a list or as a mess, and a test cannot tell me which.**
- **Whether the room being off to the left feels right**, or whether a
  conversation should be nearer what it is about.
- **⚠ The one I already know is ugly and did NOT fix:** the replies start at
  **five different x positions**, because each bracket is a different width and
  two options have none. **`§4c` rules colour and says nothing about
  alignment**, so I reported it rather than deciding it. **Tell me whether it
  actually bothers you** — that decides whether it is worth a ruling.
- **Whether the slack in the middle of the panel reads as breathing room or as
  something missing.**

---

## What I already ran — do not repeat it

**595 tests, green**: Lodestar 270 · Lens 4 · Loom 111 · app 210. Nothing is
red. Seven long replies are asserted to fit at five viewports, every row's
rectangle is asserted inside the panel, and `§4c`'s four colours are asserted
for the first time.

---

## ⚠ Known scaffolding — NOT bugs

**The weapon is a fist. The portrait is a circle. The board is drawn, not
textured. Nothing has been designed** — sizes are right, but typography,
palette and framing have never been touched. The full list of nine is in
`HANDOFF/docs/RUNNING-ON-THIS-MACHINE.md`.

**⚠ And the panel is structure, not a look.** It is a plain column on a plain
ground. **Judge what it does, not what it looks like.**

---

## ⚠ Wrong versus undecided

Read `HANDOFF/BUILD/STATE.md` before filing. Known undecided and **not bugs**:

- **The ragged left edge of the replies** — above.
- **What a save is NAMED, and how many.**
- **"The same place" is the entry area** — walk to the second area, quit,
  `Continue`, and you arrive back at the first. **That is the spec.**
- **Click-to-move** — wanted, not built, and it needs a settings surface that
  does not exist. `PT-1443`.

---

## Data safety

**All four suites are hermetic and leave `~/.local/share/kotor-rpg/` alone** —
verified again this slice. **Using the app still writes real saves**, which is
the product working. Delete `.sav` files to start clean; **do not delete
anything under `packages/` except your own.**

**Report as `reports/002-the-side-panel.md`.** Write only `TEST/reports/`.
