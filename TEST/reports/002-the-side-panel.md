# 002 · The side panel — REPORT

**From `Tester`. Answers `requests/002`.** Walked in the real binary at a real
1280×720, launched with `./run-app.sh`. Measured off the actual frames, not
from a test.

---

## Numbered against your claims

| # | claim | verdict |
|---|---|---|
| 1 | The room is bigger while the trooper is talking | ✓ **TRUE — measured 56.9px** |
| 2 | Every reply fully readable, none ends in `…` | ✓ **TRUE** |
| 3 | Nothing scrolls that you can click | ✓ **TRUE at six options** (scoped) |
| 4 | The colours mean one thing each; the price is ordinary reply colour | ✓ **TRUE — sampled** |
| 5 | The input box sits on the floor of the panel | ✓ **TRUE** (variation untested) |
| 6 | A seven-option node would still fit | ✓ **CREDIBLE — computed, not observed** (scoped) |

---

## ⚠ THE ALIGNMENT QUESTION — mine to answer, so here is the answer

**Measured first.** Five reply-text left edges in the 480px column:

    x = 837   Stand aside. / My mistake.   (no bracket)
    x = 881   [Lie]
    x = 914   [Human]
    x = 929   [Persuade]
    x = 992   [Bribe · 50 credits]

**Ragged span 155px — 32% of the panel's width.** Your five, confirmed.

### ⚠ No. The ragged edge is not what bothers a reader.

I read the list at size and then at 2×. **The raggedness is close to invisible,
and there is a reason it is invisible: the brackets are not ragged.** They form
a clean column at `x=837`, and **that column is what the eye actually scans**.
You pick a line by *what kind of option it is* — a check, a species, a price —
and the bracket is that. The reply text is what you read **after** you have
chosen the line, and by then alignment is doing no work.

**Two more things protect it:** the wrap is a correct hanging indent — the
second line of `[Human]` lands at `914`, under its own first line, not at the
margin — so a two-line reply reads as one block. And with six rows at 39–60px
pitch there is no wall of text where a ragged edge causes line-tracking errors.

**⚠ So I would not spend a ruling on aligning the reply text.**

### ⚠ But two real things are hiding behind that question

**A · The ungated options sit in the bracket column, and read as the wrong kind
of thing.** `Stand aside.` and `My mistake.` start at `x=837` — **the same x as
`[Lie]` and `[Persuade]`**. Scanning the left edge you get four brackets and
then two bare sentences occupying the bracket slot. For a beat they read as
labels rather than as things you say. **This is the actual scanning cost, and
it is not raggedness — it is two items in the wrong column.**

**B · The widest bracket squeezes its own reply and produces an orphan.**
`[Bribe · 50 credits]` is 155px wider than no bracket at all, so its reply
starts at `992` with **~270px left** — and wraps to:

    [Bribe · 50 credits]  Fifty credits says you saw
                          nobody.

**A one-word second line.** The widest label is the one whose text has least
room, which is backwards.

**⚠ My reading, flagged as a reading:** the cheap fix for both is to let a
bracket that is wide — or a reply that has none — sit on its **own line**, with
the reply text at one left edge underneath. That costs vertical room, which
§6 below says there is plenty of. **I am not proposing it as a ruling; you
asked whether it bothers a reader, and this is the part that does.**

---

## 1 · The room is bigger — measured three ways

**Board, tile pitch, at 1280×720, measured off the frame:**

| state | board | tile |
|---|---|---|
| **panel open** | `x 58..741`, `y 96..552` | **56.9px** × 57.0px |
| no panel | `x 251..1028`, `y 66..583` | 64.8px |
| the old bottom band | — | 29px *(your figure, not re-measured — the band no longer exists to measure)* |

**Independently: the two markers sit one row apart and their centres are
57.25px apart** — a pitch measurement that does not depend on where I think the
border is.

⚠ **So `BUILD/40`'s `56px` is honest to within a pixel, in the real binary, at
the real size.** And the square being talked across is not covered — the
trooper at `6,4` and the player at `6,3` are both fully drawn, clear of the
panel edge at `x=800`.

---

## 4 · The colours — sampled, not eyeballed

| bracket | RGB | reading |
|---|---|---|
| `[Persuade]` | `(187,153,84)` | amber — the roll |
| `[Human]` | `(135,205,186)` | teal — who you are |
| `[Lie]` | `(110,97,74)` | dim/warm — manner |
| `[Bribe · 50 credits]` | `(193,193,169)` | **ordinary reply colour** |
| reply text | `(193,193,169)` | — |

✓ **The price is not a fourth colour** — it samples identical to the reply text.
Claim 4 holds. ⚠ One note: `[Lie]` is a dim *warm* tone rather than a neutral
grey; it reads correctly as "quieter than the rest", but "grey" is not quite
what is on screen.

---

## 6 · Seven options — credible, and I did NOT see seven

**I could not observe it: the bed's node has six, and authoring a seventh reply
is Loom work I did not do.** So this is arithmetic on measured rows, and I am
labelling it as such.

**Measured in the running app:** row pitch **39px** for a one-line reply,
**60px** for a two-line one. First row top `y=89`. Input box top `y≈610`.
**Slack below the last option today: ~269px.**

**Worst case, seven two-line replies:** `7 × 60 = 420px` from `y=89` ends at
`509`, against a box at `610`. **~100px clear.**

⚠ **And I checked the provenance of your 76px before doubting it.** The
seven-option assertion is in `test/viewport_scale_test.dart`, which **does**
set `t.view.physicalSize` and `addTearDown(t.view.reset)` — **it is not one of
the 23.** Different datum from mine (panel bottom vs input box), same order,
both comfortably positive. **I was ready to file this as untrustworthy and it
is trustworthy.**

⚠ **`test/dialogue_screen_test.dart` IS one of the 23** — four `MediaQuery`
blocks at `Size(1280,720)`, `setSurfaceSize`/`physicalSize` count **zero**. It
does not carry the seven-option claim, but it is a dialogue-panel test whose
surface is 800×600 while it believes otherwise.

---

## 2, 3, 5 — what I saw

**2 · Nothing truncated.** All six replies fully readable; two wrap to a second
line; **none ends in `…`**. ✓

**3 · Nothing scrolled.** The reply list did not scroll and nothing clickable
was out of view at six options. ⚠ **Scoped: six is not seven** — the case your
claim is really about is the one I could not produce.

**5 · The box is on the floor.** `say something…` at `y≈610–637`, hard against
the panel bottom, in every capture. ⚠ **Scoped: I only ever had six-option
nodes, so I never saw the count change and cannot say the box holds still when
it does.**

---

## ⚠ AND THE PANEL IS WHERE `003`'s WORST FINDING SHOWS

**The status line under the board now wraps to two lines and truncates with
`…`** — it accumulates one clause per encounter-end and never stops. **When it
took a second line the board top moved `112 → 95`: the growing text ate board
height.** Full detail is `reports/003` **N2**; it belongs here too, because it
is the line that sits directly beneath this panel and it is already unreadable
after five encounters.

**And `D7` — the fight log overlapping
`Vess Taran · arrows to move · esc to leave` — is still present**, as you said.

---

## ⚠ Scoped negatives

**Checked:** the panel at 1280×720 only, with the bed's six-option node, on
`endar-spire`, in the real binary at `4f8a242`.

**NOT checked:**

- **Seven real options** — the whole of claim 6 as an observation
- **Any other window size.** ⚠ Your journey step 6 said *"if you can, resize"* —
  **I did not.** The window is fixed at 1280×720 by the runner and I did not
  attempt to resize it, so **five of your six viewports are untested by me**
- **The typed `say something…` box.** Journey step 4 — I never typed into it
- **`[Bribe · 50 credits]` and four of the six replies.** I only ever took
  *"Stand aside."*, because that is the one that starts the fight `003` needed
- **Whether the slack in the middle reads as breathing room.** Honestly: with
  six options there is ~269px of empty column between the last reply and the
  box, and it reads as **empty**, not as calm. With seven long replies it would
  be nearly full and would read better. I would not act on that until the
  panel holds a real worst-case node

**Nothing red, no exception, no overflow** in any run log this session.
