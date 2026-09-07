# 06 · Backstory, and the re-lock warning

**`KOTOR-RPG-APP` `7db8fa5`.** 79 tests pass. **One stop, and it is the second
half of the step.**

---

## Tabs, not stages

`§3` lists three multi-decision steps and separates this one explicitly: Origin
and Identity **transition in place and carry a back control**; Backstory is
`profession ⇄ lifestyle`, **two tabs, no stage transition and nothing to go back
to**. Built as tabs. There is no `◂` control on this screen and a test asserts it.

Every list entry is its own rounded box — `PT-1239`, *"the change that made it
work"* — so tabs, entries, offer boxes and footer speak one visual language.

## ⚠ A droid gets Programming, and no lifestyle tab at all

`PT-692`, owner ruling: **"NOT SOME. NOT CHASSIS-DEPENDENT. NONE."** Not
rendered, not dimmed. The reason is in `§3a`: the prose is
`lifestyle × homeworld × species`, and **a droid has no homeworld, it has a
manufacturer**.

**Third step in four where a droid's shape differs** — after Origin absent and
Gender becoming Voice.

17 programmings, and the heading that said *thirteen* was corrected at `PT-1321`.

## ⚠ The two offers are shown, and neither is picked here

`PT-695` gives a profession **one grant and the player chooses which** — the
item, or a second background aptitude. **The choice is not made on this screen.**
`PT-1200` rules it forward-looking and `§4`'s graph resolves it at **Equipment**,
*"once the item's worth is visible beside the rest of your gear"*. The aptitude
applies from level 2.

So both render as boxes, the aptitude one **amber** — the colour that marks a
grant everywhere else in the flow — and a line says why neither can be clicked.
**Without that line, two options you cannot click reads as broken.**

## ⚠ THE SIX §3b GRANTS ARE OFFERED — said, not decided silently

You asked for this either way. **They are offered**, and each says on screen that
it came from a section headed *"RECOMMENDED ADDITIONS"*.

**Why offered:** `§1`'s own heading counts them — *"22 of the 28"* — and names
exactly six professions as having no grant row, none of which is one of these.
**Withholding them would leave six professions showing no grant at all**, which
is a visible difference to a player and the wrong way round from what the
document's arithmetic asserts.

**It remains a rules question.** The heading calls them proposals and the
arithmetic calls them grants. The screen shows both facts; `grant_recommended`
carries it in the data. **Not resolved.**

## ⚠ THE STOP — an organic cannot complete Backstory

`CHARGEN-FLOW-MAP-01 §3` makes this two tabs. `CHARACTER-CREATION-01` separates
them: a profession carries a conditional aptitude, and **"LIFESTYLE TOUCHES
STARTING CREDITS, NOT APTITUDE."**

**There is no lifestyle roster.** `PROFESSIONS-01` heads its own 28 rows
*"Lifestyle"* and those rows **are the professions** — and the document states
the question outright:

> **"whether `lifestyle` IS that `profession` field is unsettled — `PT-667`."**

So the tab renders and refuses, naming `PT-667`. Inventing a roster, or quietly
treating the professions as the lifestyles, would **answer `PT-667` by building**.

**A droid completes Backstory** — it has no lifestyle half. **An organic cannot**,
and because `§5`'s unlock is sequential that stops the strip at step 3 for an
organic, the same shape Origin had before the worlds shipped.

**THE NEED:** either a lifestyle roster with its credit values, or a ruling that
`lifestyle` and `profession` are one field and the second tab does not exist.

## ⚠ The re-lock warning — built, and exercisable for the first time

`§5`: re-opening a completed step **re-locks everything after it and must warn
first, naming what will be discarded**. NWN discards silently; we do not.

It was unexercisable while nothing could complete. **Origin can now, and Gender
makes two.** Re-opening Origin names *Female* as what will be lost, offers
**Keep** or **Re-open**, and **discards nothing until confirmed**. Tested both
ways: Keep preserves it, Re-open clears it and re-locks Gender.

## Not built

Steps 4 through 9 — Abilities, Skills, Feats, Powers, Equipment, Identity.
No character record, no save; `Continue` stays disabled.
No explanatory popup — `§6` gives every screen a one-time one, which needs a
seen-once store, and that is save-adjacent.
