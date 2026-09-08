# The nine chargen screens, seen

**23 captures at 1280×720, `KOTOR-RPG-APP` `fd48d5c`+.** Produced by
`test/capture_test.dart` — the app's own pixels through `RepaintBoundary`, at
device ratio 1.0. Not a window grab.

> **⚠ A WIDGET TEST DRAWS EVERY GLYPH AS A BOX unless a real font is loaded.**
> The first capture proved the layout and hid every word. A real face
> (`Arimo`) is loaded and pushed down as the ambient default. **That is why the
> tofu boxes below are a finding rather than an artefact — see §A.**

---

## The organic Jedi — nine steps

| | |
|---|---|
| [`01-entry`](01-entry.png) | The entry screen. `Select Premade` correctly dead at `none` |
| [`02-species-subrace-open`](02-species-subrace-open.png) | Species with a subrace picker open |
| [`04-class`](04-class.png) | Class |
| [`05a-origin-world`](05a-origin-world.png) · [`05b`](05b-origin-upbringing.png) | Origin, before and after a world is picked |
| [`06-gender`](06-gender.png) | Gender |
| [`07-backstory`](07-backstory.png) | Backstory, one tab — `PT-1401` |
| [`08-abilities-organic`](08-abilities-organic.png) | Abilities, the point buy |
| [`09-skills`](09-skills.png) | Skills, aptitude marked with its sources named |
| [`10-feats`](10-feats.png) | Feats, 52 chain heads |
| [`11-powers`](11-powers.png) | Powers, 21 open at 1st level |
| [`12a-equipment`](12a-equipment.png) · [`12b`](12b-equipment-the-two-boxes.png) | Equipment, and **the two `PT-1200` boxes** |
| [`13a`](13a-identity-portrait.png) · [`13b`](13b-identity-name.png) · [`13c`](13c-identity-your-story.png) | Identity, all three stages |

## The droid — six steps, renumbered

| | |
|---|---|
| [`03-model`](03-model.png) | Model, which only a droid sees |
| [`20-droid-abilities-protocol-inferred`](20-droid-abilities-protocol-inferred.png) | ⚠ **The chassis spread, no spend controls, and the inferred line — 16 Charisma with its source named** |
| [`21-droid-skills-gated`](21-droid-skills-gated.png) | 13 of 25, and the three kinds of closure kept apart |

## The strip

| | |
|---|---|
| [`30b-strip-locked-padlocks`](30b-strip-locked-padlocks.png) | Nothing done. Only Origin is open |
| [`30-strip-organic-nine-play-unlocked`](30-strip-organic-nine-play-unlocked.png) | ⚠ **Zero padlocks, Play unlocked.** Never seen before today |
| [`30-strip-droid-six-play-unlocked`](30-strip-droid-six-play-unlocked.png) | Six steps, Play as 7 |
| [`31-relock-warning`](31-relock-warning.png) | The re-lock warning, naming what will be discarded |

---

# ⚠ WHAT LOOKS WRONG

Ten findings. **Nothing here was fixed** — three are divergences from a ruling
and belong to the owner.

## ⚠ A · The UI needs nine glyphs the app ships no font for

**This is the biggest one and it is not a capture artefact.**

The interface uses `✓ › ▸ ⚠ → • ⇄ …` **and a colour emoji `🔒`**, and
**`pubspec.yaml` bundles no font and no `fontFamily` is set anywhere.** Glyph
coverage is therefore whatever the user's system happens to have.

**Where it shows, in these captures:**

- **Every completed step's tick is a box** — `30-strip-organic-nine`. Nine of
  ten rows.
- **Every locked step's padlock is a box** — `30b`. `🔒` is an *emoji*: where it
  does resolve it will render in colour, against a monochrome terminal palette.
- **`Name ▸`** — `13a`. The step's own forward control.
- **The inferred-spread warning's `⚠`** — `20`, the line the owner asked to see.
- **Three `⚠` in a world description** — `05b`.
- **The summary chips' leading glyph** — `31`.

> **A different machine draws a different interface, and the two places it
> matters most are the strip's completed tick and its padlock — the only
> indicators the strip has.**

## ⚠ B · Origin is one screen, and `§3` says it is two stages

`CHARGEN-FLOW-MAP-01 §3`: *"`ORIGIN world → [Upbringing ▸] → upbringing`… **The
panel transitions in place**"*, and *"Origin and Identity carry a **back control
inside the step** — `◂ change world`"*.

**The built screen shows all three columns at once and has no back control.**
`05a` and `05b` are one screen in two states, not two stages. **Identity was
built to `§3`; Origin was not.** Reported, not changed.

## ⚠ C · The world description is a database dump

`05b` — screaming caps mid-sentence, `GAZETTEER f.122`, `Bureaucracy DC 15:`,
`DC 30:`, three tofu marks. It is the Atlas's own research prose shown to a
player verbatim. **The one screen where a player reads about their homeworld
reads like a spreadsheet cell.**

## ⚠ D · Three lines are simply wrong

| Where | Reads | Should read |
|---|---|---|
| `31` | **`· Male`** — a leading separator and a value with no label | the step's name, then its value |
| `31` | **`Human · Human`** | `Human`. The species and its variant are the same, so the chip doubles |
| `31` | **`9 of nine`** | a numeral and a word in one phrase, for a count where nothing is complete |

## ⚠ E · The story generator lowercases proper nouns

`13c` — *"you get **acolyte**, immediately"*, *"A **jedi sentinel** reads
people"*. `toLowerCase()` is applied to the class and profession names to make
them read mid-sentence, and they are proper nouns.

## ⚠ F · The rundown has no portrait, and `PT-1243` names one

*"A FULL RUNDOWN above: **portrait**, name, species, class, all six abilities…"*
`13c` shows name, species, class, abilities and chips. **The portrait is
absent** — the one element of the rundown that is also the step's first stage.

## ⚠ G · Developer prose on player screens

`13a` and `12a` open with a paragraph citing `UI-ASSETS-01 §2`,
`ASSET-REPLACEMENT-01`, `PT-1350`, `STARTING-EQUIPMENT-01 §1`. **Written for the
owner and left where a player reads it.** The *facts* belong on screen — that
nothing needs importing, that route 2 is not offered — the *citations* do not.

## ⚠ H · Nothing shows which species is selected

`02` — the panel on the right is the only feedback, and **the selected row
carries no mark in the list.** With the list scrolled, the selection can be off
screen entirely and nothing on the screen says what is chosen.

## ⚠ I · Rows are sliced, not scrolled

`09`, `21` — the last visible row is cut through the middle of its `+` control
rather than clipped at a row boundary. It reads as broken rather than as more
below.

## ⚠ J · Half the width is empty on four screens

`09` skills, `10` feats, `11` powers, `20` abilities all lay out in roughly
420px of 1280 and leave the rest black. `05` origin and `02` species use the
width properly, so the two halves of the flow do not look like one product.

---

## What was NOT captured

The **Play screen** — Play unlocks and leads nowhere, so there is nothing
behind it. The **premade path**, which no package supplies. **Any screen at
another size**: every capture here is 1280×720.
