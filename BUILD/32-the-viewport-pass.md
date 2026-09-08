# 32 · The viewport pass — `§7`, re-derived

**258 Lodestar · 206 app · 108 Loom · 4 Lens.** All analyze clean. **Captures
re-taken.**

---

## 1 · The click bug is gone by construction, not by a bigger number

**It was a cap — a third, then a half. Both clipped.** A clipped row is **still
laid out and still hit-testable**, so a tap at its coordinates landed on
**whatever is at that point**: in the test, `push` instead of `shove-past`,
silently.

> **`§4c`'s hiding-not-greying assumes the list you SEE is the list you HAVE.
> A row that can be tapped and cannot be read breaks that whatever the cap is.**

**So there is no cap.** The panel is exactly as tall as its content — no
scroll, no clip, **no row anywhere that cannot be seen.** `viewport_scale_test`
asserts every row's rectangle lies inside the panel's, at **seven option counts
across three viewports.**

## 2 · The board is above the panel, not under it

**The `Stack` was wrong.** It kept the board at full height and drew the panel
over it, so the room stayed *"visible"* while **the square you were talking
across sat under the words.** `PT-1264` kept the grid a major view **so you can
read it**, and half a room is not the room.

**⚠ AND THAT EXPOSED A BUG IN `Lens`, NOT IN THE APP.** With the board given
less height it **ran off the top edge** — `_tile` was cached so a player's zoom
survives a rebuild, **and it therefore never re-fitted when the VIEW changed.**
It re-fits now, and **a deliberate zoom is still the player's**: once they have
scrolled, a smaller view does not take it back. **Found by looking at a
capture.**

---

## 3 · ⚠ The measurement — five real viewports

```
                                        1 opt        3 opt        5 opt        7 opt
1280×720   s=2.82  entry 15.5px    175px 24%    260px 36%    346px 48%    431px 60%
                        tile left        68px         57px         47px         36px
1366×768   s=3.01  entry 16.6px    186px 24%    277px 36%    367px 48%    457px 60%
1600×900   s=3.53  entry 19.4px    217px 24%    324px 36%    430px 48%    536px 60%
1920×1080  s=4.20  entry 23.1px    258px 24%    384px 36%    511px 47%    638px 59%
2560×1440  s=4.20  entry 23.1px    258px 18%    384px 27%    511px 35%    638px 44%
```

**⚠ The ratios were not wrong. The cap was.** `scaleFor` is height-bound at
every 16:9 viewport and clamps at 4.20 from 1080p up, which is why the panel's
share *falls* at 1440p instead of rising.

### The constraints the eventual design does not get to choose freely

- **A seven-option conversation takes 60% of a 720p screen** and leaves the
  room a **36px tile** — about half what a quiet room gets. `STUDY 18` found
  source nodes offering up to seven, so this is not a corner case.
- **⚠ With the panel open, the room's size is governed by HEIGHT ALONE.** A
  12×8 room in a 1280×285 strip fits to height and leaves ~70% of the width
  black. **A full-width panel buys nothing that a shorter one does not.** A
  panel down one SIDE would leave the room a squarer space: at 1280×720 with a
  480px side panel the tile is **66px against 29px today.** *Reported, not
  built — that is a design decision.*

---

## 4 · The two from `BUILD/23`, and both measured wrong rather than looked wrong

- **`GENDER` shouted because the strip borrowed the SCREEN's header.** The
  screen's bar is uppercase by `§2`; the strip's rows are title case. **Two
  places, two cases, one string.** Split into `genderTitle` and `genderStep`.
  **⚠ And six tests had locked the shouting in**, which is why nobody caught it
  reading the code.
- **The Skills fade was 6 design-pixels — 17px at a real viewport, SHORTER THAN
  A ROW.** So whether it landed on text or on the gap between two rows was
  **luck**, and the capture shows it landing on a gap: **twelve of twenty-six
  skills, and a list that looks complete.** The fade is one row now, so it
  always cuts a row.

**⚠ AND THE SKILLS FADE IS STILL NOT ENOUGH, WHICH IS A DESIGN QUESTION.** A
one-row fade says *"a bit more"*; it does not say *"fourteen more"*. **Reported
and left** — nothing here restyles.

---

## 5 · ⚠ Which screens forgive a wrong scale, and which do not

**The list is worth more than the fixes, so here is the rule it comes from:**

> **A screen forgives a wrong scale when its content is one column that scrolls
> and nothing competes for the space. It stops forgiving the moment two things
> must both be readable in one fixed budget — or content can be silently
> clipped while staying interactive.**

| | screens | why |
|---|---|---|
| **Forgiving** | Species · Model · Class · Origin · Gender · Backstory · Abilities · Feats · Powers · Equipment · Identity · Console Home · Library · Load Game · Options | one column, it scrolls, nothing else wants the room |
| **⚠ Forgiving ONLY IF IT SAYS IT SCROLLS** | **Skills** — and it did not | a list that hides half itself and looks complete is not forgiving, it is silent |
| **Unforgiving** | **the dialogue panel over the play surface** | two things, one height, both must read |
| | **the play surface** | the room must FIT; a stale fit clips it — `Lens`, §2 |
| | **the hub summary** | fixed rows in a fixed height — it overflowed by 337px once |
| | **Loom's New Creature dialog** | still overflows 58px at 1280×720, reported at `PT-1425` and unfixed |
| | **Loom's area tab** | grid, palette and tree share one width |

**⚠ The pattern in the unforgiving column is that every one of them divides a
fixed budget between two things.** Chargen's screens never do — which is why
eleven of them survived a scale nobody had checked, and the first screen that
divided anything did not.

---

## 6 · Not done

**No restyling, no palette, no typography.** The Skills fade's sufficiency, the
side-panel question, and Loom's 58px overflow are all reported and left.
