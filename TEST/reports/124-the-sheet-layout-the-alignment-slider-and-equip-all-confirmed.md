# TEST 124 — the sheet layout, the alignment slider and Equip, all confirmed

**Build.** App **`159364f`** ("the marker is a window, not a lid — PT-2478"),
tree clean, built from `git archive` of that sha. The committed lock resolves
Lodestar **`d1fcab69`**, and that is the pub-cache checkout
`package_config.json` compiles against. `check_shelf.py` clean: 29 rules
files and 65 standard blueprints.

**Verdict.** **All three items confirmed**, and the two colour claims are
measured in pixels rather than eyeballed. No defects. One thing I was about
to flag turned out to be wrong on measurement, and that is recorded rather
than dropped.

---

## 1. The sheet — viewport, row layout, and the slider

### Portrait sits properly sized in the viewport

Measured on the rendered screen, at `y = 400`:

```
viewport left stroke   x 393
circular placeholder   x 580 – 760      (181 px wide)
viewport right stroke  x 947
```

The viewport is **555 px** wide around a **181 px** child — **3.1× its
child's width**, so it is not collapsed to it. Vertically it runs `y 217 –
596`.

⚠ **What is confirmed is the box, not a photograph.** My saves carry
`portrait: null` and this bench ships no portrait asset, so the viewport
holds the circular placeholder. The sizing claim is settled; "a portrait
renders correctly inside it" still needs a package that has one.

### The arc sits beside the viewport, in a row

```
viewport   x 393 – 947    y 217 – 596
ribbon     x 977 – 1049   y 149 – 664
```

The ribbon begins 30 px clear of the viewport's right edge and their
vertical spans overlap. **Side by side, not stacked** — stacked would put
the ribbon's y-range below 596 with the x-ranges overlapping, and neither is
true.

### The slider colour — the ramp, and the waist in particular

Sampled down the ribbon, one reading every 12 px:

```
y=168  #F5080D        the top stop, #FF0408
y=288  #BF2A3F
y=384  #8B4F73   ┐
        (marker)  ├─ the waist, bracketing the authored #7D5980
y=420  #755E88   ┘
y=504  #477EB7
y=648  #08A9F6        the bottom stop, #00AEFF
```

The authored waist is `#7D5980` — a desaturated **grey-mauve** — and the two
samples either side of the marker are `#8B4F73` (139,79,115) and `#755E88`
(117,94,136). The waist falls exactly between them. It is emphatically
**not** the saturated indigo `#3626A3` the code's own comment records as the
wrong reading from a fixed texture column.

### The marker is translucent — and the control proves it

At the waist, rows through the marker:

```
y=391, 412   (24,178,139)   = #18B28B, the two teal rules
y=389-390, 413-414          near-black hairlines, one each side
y=395-408    (69,44,64) → (66,47,68)     the fill
```

The fill is a dark **mauve**, and the arithmetic matches a wash rather than a
cover: ribbon `#7D5980` (125,89,128) × (1 − 120/255) = **(66,47,68)**.
Measured (66–69, 44–47, 64–68).

⚠ **The control is the part that makes this a reading.** A solid dark blob
would also look dark at the waist. So I moved the marker: a fixture with
thirty dark encounters folds to **`Deep Dark 0`**, putting the marker at the
ribbon's top. The same fill there reads:

```
(134, 3, 5)
```

Ribbon `#FF0408` (255,4,8) × (1 − 120/255) = **135**. Measured **134**.

Same marker, two positions, two completely different fills, each exactly the
ribbon beneath it at alpha 120. **A window, not a lid** — a lid could not
have changed colour.

## 2. Equip — both states, and the worn item in its own list

Opened on `q`.

**The slot view shows the worn item as a real selection.** Title `EQUIP`,
subtitle naming the current slot, and the list:

```
head                          body
mask (Equipped)               clothing (Equipped)
                              light
                              medium
                              robe-1
```

Not "pick one". The lattice draws all twelve cells with the worn ones named
in bright text — `mask`, `clothing`, `belt`, `blaster-pistol` — and the
eight empty ones dim.

**Clicking a slot drops into the item-selected view.** Clicking the body
cell:

* the worn `clothing (Equipped)` is highlighted gold as the current choice,
  with its three bag alternatives beneath it;
* its **own description** sits on the right — *"section: EQUIPMENT-01 §5.2 —
  a robe caps no Dexterity at all, and Clothing is +0 by ruling rather than
  by source."*;
* a **CANCEL / OK footer** replaces the lattice, which is gone entirely —
  the two panes are never drawn together.

Selecting `light` moves the gold highlight and **swaps the description** to
that item's own (*"section: PT-1734 — read from baseitems.2da rows 66–68…"*),
so the description tracks the selection rather than the slot.

`CANCEL` returns to the slot view, and the subtitle now reads **`body`** —
the clicked slot became current, which is `PT-1252`'s defect (a slot view
with no current slot, saying "pick one") staying fixed.

`OK` refuses and says why, naming both ends:

```
equipping is not built yet — what it costs is unruled (implant-1 → implant)
```

**A worn item is always among its own slot's choices — in its strongest
form.** The bag holds **no head item at all**: its eight entries are three
body armours, gauntlets, an implant, a forearm band and two weapons. The
head slot's list is still `mask (Equipped)`. The item comes from what is
worn, not from what is carried.

⚠ And the contrast that stops that being vacuous: clicking the **empty**
`implant` slot opens the item view showing only the bag's `implant-1`, with
**no `(Equipped)` marker** on it. The marker tracks the record, not the list
position.

## 3. Auto Level Up — sized to its own label

Measured on the gold pixels:

| button | border box | label glyphs | padding |
|---|---|---|---|
| **Auto Level Up** | x 608 – 732 (124 px) | x 612 – 728 (117 px) | 4 / 4 |
| Level Up (dim) | x 631 – 709 (79 px) | x 634 – 706 (73 px) | 3 / 3 |

The label is **inside** the border with symmetric padding, and the narrower
dim button follows the same rule at the same scale. The previous fault — a
border narrower than its text — is gone.

⚠ **I was going to flag this as still cramped.** At a 6× crop the `A` and
the final `p` look as though they touch the stroke, and my first note said
the wide button had lost padding the dim one kept. The measurement says
otherwise: both have the same 3–4 px, and neither overflows. Recording it
because the eyeball reading and the pixel reading disagreed, and the pixels
are right.

## Also noticed

* **`SWITCH WEAPONS` states its own absence** — *"the second weapon
  configuration is not built yet"* — rather than sitting there inert.
* **`DEF 10 · ATTACK — · DAMAGE —`** on the Equip footer: the two bars it
  cannot derive print a dash instead of a number, consistent with the
  sheet's Defence row.

## Fixture

`tester-mind`, and one change that matters beyond this test: **the standard
item tree is now copied into the bench** (`blueprints/items`, 65 items from
`base-rules`). Item paths resolve inside the *selected package*, which is
why every earlier fixture naming `items/armour/clothing` produced the read
failure I chased in TEST 123 — the bench had no items at all.

`mk124.py` dresses the character in four slots — `body` clothing, `head`
mask, `belt` belt, `weapon_r_1` blaster-pistol — and puts eight deliberately
chosen alternatives in the bag as `item.acquired` events, with **nothing
that fits the head slot**, so the "worn item is always offered" clause has a
real negative behind it. Its second argument is the number of dark
encounters: `1` gives `Neutral 49` and the marker at the waist, `30` gives
`Deep Dark 0` and the marker at the top — the pair the translucency control
needs.
