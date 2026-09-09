# 40 · `PT-1447` — the side panel, and the room doubles

**595 tests green** — Lodestar 270 · Lens 4 · Loom 111 · app 210. Captures
re-taken. **App `f924efb`.**

---

## 1 · ⚠⚠ The headline number is NOT the one I promised

| | |
|---|---|
| **Promised** | 66px tile against 29px |
| **Measured** | **56px against 29px** |

**I reported 66–67px from arithmetic, and the screen never drew it.** `Lens`'s
`AreaViewport._fitted` divides by `width + 2` and `height + 2` — **a one-tile
margin all round** — and my figure divided by 12 and 8. **The capture showed
57px and the code said why.**

**It is still nearly double, and the move is still right.** But the number in
`BUILD/32` and in the brief was optimistic by a fifth, and the test now uses
`Lens`'s own formula so it cannot drift again.

    1280×720    panel 480px   board 800px    tile 56px
    1366×768    panel 512px   board 854px    tile 60px
    1600×900    panel 600px   board 1000px   tile 70px
    1920×1080   panel 714px   board 1206px   tile 85px
    2560×1440   panel 714px   board 1846px   tile 121px

**⚠ The panel is `170` design units, not a fixed 480px.** `170 × scaleFor(1280,
720) = 480`. A fixed column would hold ~48 characters at 1280 and ~32 at 2560,
because the type grows with `s` and the column would not. **Constant measure,
not constant pixels.**

---

## 2 · Why the axis matters, which is the whole argument

**With the panel open the room was governed by HEIGHT alone.** A 12×8 room in a
1280×285 strip fits to height and leaves **~70% of the width black**, so the
band was taking the only axis that mattered while the spare width bought
nothing.

**⚠ And it serves `PT-1264` better than either predecessor.** The `Stack` drew
the panel over the board; the `Column` cut its height. **The play surface is
now LARGER while someone is speaking than the band left it**, and the row the
speaker stands in is never cut.

---

## 3 · What survived the move, deliberately

**⚠ THE LIST YOU SEE IS THE LIST YOU HAVE.** Every row's rectangle is asserted
inside the panel's, **at seven option counts across five viewports, in the new
shape** — because a taller narrower panel changes the arithmetic that produced
the click bug.

**Seven of the bed's LONGEST reply fit at every viewport**, with 76px to spare
at 1280×720 and 487px at 2560×1440. `STUDY 18` found source nodes offering up
to seven, so that is the case that had to hold.

### ⚠⚠ And the same bug turned up in a second costume

`maxLines: 2` with an ellipsis was **ample in a 1280px strip and truncates in a
480px column.**

> **An ellipsised option is a TRUNCATED option** — the row is drawn, it is
> tappable, and what it says is not what it does.

**`§4c`'s hiding-not-greying has to mean the WORDS too**, or a player choosing
between two replies that both end in `…` is choosing blind. Removed, and there
is a test that fails if a line cap ever comes back.

### ⚠ A column is bounded where a band could grow

At seven options something has to give, and **`BUILD/34` had already ruled
what**: *anything you can click must be laid out where it can be seen, and a
scroll view is only safe for things you READ.* **The NPC's line is read. The
options are clicked.** The line yields; the options never do.

---

## 4 · `§4c`'s colours are asserted now, and nothing guarded them before

`TRACE-93`'s one-channel-two-meanings defect **has been reproduced by this
design twice** — `PT-1307` caught the first, `BUILD/30`'s capture caught the
price drawn in `accent` beside teal `[Human]`. **Both were caught by a person
looking. Nothing in the suite could have failed.**

**A relayout is exactly when a colour convention gets re-derived by accident**,
so amber-rolls, grey-manner, teal-identity and **the price in ordinary bone**
are a test now — including three assertions that a price is *not* either green,
and one that a check wins the bracket when an option carries several terms.

---

## 5 · ⚠⚠ I invented an overflow by modelling geometry instead of measuring it

**Twice, and it cost the most time in this slice.**

The test guessed the panel's height as a flat **`0.755` of the viewport**, then
as **one status row**. The real screen leaves it **`55.6 · s` less** than the
viewport — measured by probing the running screen, which is what I should have
done first.

**On the wrong geometry I blamed `FlexFit.tight` for a 6px overflow and swapped
it out.** With the measured geometry tight was fine all along. **The comment
recording the false cause was corrected rather than left**, because a wrong
reason in a comment is worse than no comment.

**⚠ AND THE CAPTURE IS WHAT SENT ME BACK.** `loose` dropped the slack under the
input and left a **300px void** beneath it; `tight` put the hole **between the
NPC's words and the replies.** Neither was visible in a measurement and both
were obvious in a picture. The input sits outside the flexing region now, so it
holds the floor and the slack falls between the last reply and the box.

**One real overflow did exist**: at 1280×720 the six-option bed node takes
**403.9px of 543.5**, the NPC line is already squeezed to one line, and a
recognition line then overflowed by 15px. The row's bottom margin went from a
full `gap` to `0.6 · gap` — matching the row's own vertical padding factor —
which bought back ~20px. **That is a reading; nothing specifies row spacing.**

---

## 6 · ⚠⚠ `Tester` broke two of my tests by doing its job

**Mid-slice, `3 packages installed` started failing.** Not a regression: a
second agent had made a fourth package, `tester-probe`, and two saves.

> **A count of a folder somebody else can write is an assertion about the
> ENVIRONMENT, not about the app.**

**`BUILD/38` and `39` stopped the suites WRITING to live data. This is the
other half and I did not see it: reads are only deterministic while nobody else
writes.** Three assertions now name the three packages instead of counting
them; the count's own rendering is covered by `library_tile_test` against a
shelf it controls.

**Filed to `TEST/requests/002` so `Tester` knows its own work caused it and
that it is fixed.**

---

## 7 · The two counts

**HAD TO BEHAVE SOMEHOW — 3.** The code had to do something and no document
says which: **where the slack falls** inside the panel; **the spacing between
option rows**; and **which edge carries the panel's border**.

**READINGS — 3.** Decisions made with a reason, written down: **`170` design
units** so the column scales with its text rather than staying 480px; **the
`0.6` row margin**, chosen against a measured 15px overflow; and **removing
`maxLines`**, which follows the click-bug principle rather than any ruling.

**⚠ Not counted as either:** the NPC line yielding is `BUILD/34`'s rule
applied, not a new decision.

---

## 8 · Not built

**Not click-to-move** — it needs key bindings and a settings surface that do not
exist, and it is its own slice.

**⚠ And one thing the capture found that is NOT fixed:** the replies start at
**five different x positions**, because each bracket is a different width and
two options carry none. It is ragged in a narrow column in a way it never was
in a wide band. **`§4c` rules colour and says nothing about alignment**, so it
is reported rather than decided.
