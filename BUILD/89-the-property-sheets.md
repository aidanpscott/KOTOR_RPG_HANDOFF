# BUILD 89 — slice three: the property sheets, and two corrections

**949 green** — Lodestar 397 · Lens 7 · Loom 196 · app 331 · `+22`.

Lodestar `da13d65` · Lens `6b55219` · Loom `cf4f5ad` · app `7b0f6c9`.

⚠ **No two-row tab bar.** `STUDY 29` found clicking a back-row tab **swaps the
rows** — `Tester` aimed at Statistics and hit Feats, `PT-1439`'s hazard live in
their most-used editor. **A placement has few enough properties to show at
once, so it shows them at once.**

---

## ⚠ CORRECTION 1 · `PT-1567` — DEPTH IS UNBOUNDED

`NewItemDialog` refused anything that was not exactly `items/x/y`:

    if (p.split('/').length != 3) 'Two levels under `items/`…'

**And `items/weapons/echani-vibroblade` sits in a table column headed EXAMPLE.**

> **An example read as a rule is `PT-1495` in a second document** — the same
> defect as a rule hidden in an example, one direction along.

⚠ **AND IT MATTERED NOW RATHER THAN LATER.** `BUILD 88` made the palette nest at
whatever depth an author made, so **a dialog that writes one level cannot author
the structure its own pane displays.** The two would have drifted from the day
they shipped.

**The suite gained the positive half**: `items/hold-out` is written, read back by
`openItem`, and comes home as `Created('items', 'hold-out')`.

## ⚠ CORRECTION 2 · FINDING 6 — THE SIGNATURE STOPPED LYING

`AreaTab` took `painting`, `placing` and `placingWay` — three parameters from
the days when the palette held three selections. `BUILD 88` made them **derived
from one mode in one place**, so the defect was gone and the signature still
described the old shape: **three fields a caller could set inconsistently, on a
widget that could no longer be given an inconsistent set.**

> **A signature that lies about the model is a defect waiting for its second
> caller.**

---

# ⚠⚠ THE PLACEMENT PROPERTY SHEET — AND `PT-1551`'s EXCUSE IS SPENT

`hidden` has been in `AREA-FORMAT-01 §3a` and in the reader since `PT-1550`, and
`loom_can_write_test` excused it on **one** argument:

> *"Loom appends and removes whole entries and never rewrites one, so the hand
> edit survives — **until it gains an edit-in-place path.**"*

**This is that path.** `hidden` and `dc` are in the **writable** list now, not
the excuse list — and the excuse was **retired by the thing it predicted**,
which is the only way an exception list stays honest.

## ⚠⚠ AND THE WRITER EDITS ONLY THE NAMED KEYS

**This is the whole contract, and it is what the excuse protected.**
`ContentsWriter.setFields` copies **every line it does not name** straight
through — whitespace, trailing comment and all. A rewrite that re-serialised the
entry from a parsed model would destroy exactly the hand-added field the excuse
existed to defend.

    mood      = "sullen"        # not a field this build knows

**survives a `hidden = true`, asserted.** The unknown lines are the test.

⚠ **And `null` REMOVES a key**, because *absent* is a state the format has and
an empty string is not: `§3a` says absent means shown, so `hidden = false` and
no `hidden` are the same fact and writing the longer one would make every area
diff on a default.

---

# ⚠ `PT-1564` — THE TIER IS A LABEL ON A NUMBER

`AREA-FORMAT-01 §3b`. The seven tiers of **`SKILL-RESOLUTION-01 §2`** — *trivial
5 · easy 10 · moderate 15 · hard 20 · formidable 25 · heroic 30 · legendary 35*,
**the middle five being `traps.2da`'s own values** — offered as the dropdown.

> **The FILE carries the number. Nothing stores the word.**

So *easy* cannot disagree with 10 — **Aurora's Encounter filed under Hard with
Difficulty Easy, made impossible.** `tierOf(15)` computes *moderate*; `tierOf(14)`
is null, because `§2` names ±2, ±5 and ±10 as its modifiers and **the ladder
recommends rather than constrains.**

⚠⚠ **AND A `dc` WITHOUT `hidden` IS A LOAD FAILURE.** It is a difficulty for
finding something already in plain sight — two statements that cannot both be
true. **So turning `hidden` off takes the `dc` with it**, because the reader
refuses the pair and `PT-1379` says the Builder must not be able to create the
fault its own validator detects.

## ⚠⚠ AND ONE CONTRADICTION, RECORDED RATHER THAN SETTLED

**`SKILL-RESOLUTION-01` is SETTLED (`D-AO`):**

> *"Three of KOTOR's eight skills do not roll against anything… **Stealth and
> Awareness are a contested pair.** A system that assumed every skill has a DC
> would have got three of eight wrong."*

and `§4`: ***"The defender rolls the better of Awareness or Alertness"*** — an
**OPPOSED** roll, not a fixed DC.

**⚠ So a DC for Awareness is a resolution mode our own settled document says
that skill does not use.** Written as ruled, recorded in `§3b` and in the
reader's own doc comment.

**⚠ What both readings share is that the number is what a finder must beat** —
under a fixed-DC reading it is a DC; under the opposed reading it is the hider's
**Stealth total**. **The number is the same; only its name is in question.**

---

# ⚠ `PT-1565` — EVERY NUMBER OF A DERIVED FIELD, VISIBLE

## Vitality, in Challenge Rating's shape

    derived 12 · override 0 = vitality 12
    derived 12 replaced by 40 = vitality 40

**`AUTHORED-CHARACTER-01`'s `override = 0` hid what the derived value would have
been** — the one number an author needs in order to decide whether to override
at all. An author setting 40 could not see that the rules said 12.

⚠⚠ **AND OURS REPLACES WHERE THEIRS ADDS, SO THE OPERATOR IS ON THE ROW.**
Aurora's *calculated plus adjustment* **is** the rating; ours is `capacity()` —
`override == 0 ? derived : override`. **Three numbers with an unstated operator
is a row that reads as arithmetic and is not**, and that would have been the
more convincing lie.

## ⚠ And a correction to the premise on abilities

> *"No screen of ours shows bought + racial = total together, and that is why
> `PT-1533` survived as long as it did."*

**The chargen abilities screen already showed all three on one row.** What it did
not show was **what any of them was** — three numbers in a line with no headings
**read as a coincidence rather than a derivation**, which is a fair reason nobody
registered it. They are named now: `bought · species · total · bonus`.

⚠⚠ **AND THE BONUS WAS GENUINELY ABSENT, WHICH IS THE HALF THAT MATTERS.**
`§12.5` puts an ability **MODIFIER** on every attack, and `PT-1533` was the fight
reading a bought score with no species applied. **The screen showed the score and
never the modifier**, so *the one number a blow actually uses appeared on no
screen at all.*

⚠ **A zero bonus is `+0`; an absent adjustment is `-`.** They mean different
things — *this score is average* against *this species does not touch this
ability* — and `PT-1534` settled that distinction one program over.

---

# ⚠⚠ WHAT I FOUND ASSUMING THE OLD SHAPE

## ✓ FIXED HERE

    1  `NewItemDialog`'s depth rule — an EXAMPLE enforced as a rule, and the
       palette had already outgrown it
    2  `AreaTab`'s three parameters — a signature describing a model that had
       been removed one slice earlier
    3  `loom_can_write_test`'s `hidden` excuse — retired by the thing it
       predicted, rather than by someone remembering

## ⚠ FOUND, NOT FIXED — REPORTED

    4  ⚠⚠ `PlaceWayDialog` IS THE ONLY DIALOG THAT ASKS BEFORE WRITING.
       Placing a creature writes immediately and a way asks first — because a
       doorway needs a target and a creature does not. Defensible, and it
       means "place" means two different gestures depending on the mode.
       Worth a ruling before a third mode arrives
    5  ⚠ THE `assistant` TAB STILL SAYS "not built yet" — third slice running
    6  ⚠ `new_creature.dart` HAS NO `species` FIELD, and `CharacterWriter`
       takes one. `PT-1490` added species and chassis to the WRITER and the
       dialog never gained the input — so a Loom-authored creature is always
       species-less, which is the `PT-1533` shape in the Builder: the value
       that reaches a blow has no author-facing control

---

## ⚠⚠ THREE THINGS ARE NOT RULED, AND I HAVE NOT CHOSEN

**`PT-1550`'s CONTACT IS THE REVEAL stays as the floor regardless** — bumping a
hidden creature always finds it, and that is built and tested.

    when the roll happens      on entering the area · each turn · on
                               approach · never (contact only)
    passive or active          the finder's number taken at 10, or a roll
    a failed find              retried, or settled once

⚠ **AND THE FOURTH IS THE ONE ABOVE**: `dc` names a resolution mode
`SKILL-RESOLUTION-01` says Awareness does not have. Asked, not assumed.
