# TEST 132 — the 2×2 readout, free options, and the third texture

**Build — the full chain.**

```
local HEAD            e6c2e4a  "Clear TEST 131's three small leftovers — PT-2560"
working tree          clean
pubspec.lock resolves lodestar  4fe831be1054d3050a793ff2090ac4ef9f286956
                      lens      32b77e3bf2aa0ec6e624df25e06f8eed0910d2cd
package_config.json   ~/.pub-cache/git/Lodestar-4fe831be.../
                      ~/.pub-cache/git/Lens-32b77e3b.../
built from            git archive e6c2e4a
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints.

**Verdict.** **All four routed items confirmed.** Three of my own TEST 131
findings confirmed fixed alongside them, including the panel overflow — read
at **both** window sizes as promised at PT-2554. **One new defect, and it is
severe**: the Inventory and the dialogue both show the purse a character
*started* with, never the one they have.

---

## 1. The 2×2 readout grid — confirmed

Two separate bordered boxes, not a column. Solving the scale from the message
frame's own design rect gives **1.596** with design y=0 at y≈85, and the
boxes land where `computer_x.gui` declares them:

```
                design rect              rendered
left  column    x  66..314               x  696..1092     Slicing / Spikes
right column    x 326..574               x 1111..1507     Repair  / Parts
rows            y 387..413, 417..443     y  727..744, 776..794
```

A clear gap between 1092 and 1111 separates the two boxes.

**The mirrored value placement is there**, exactly as the comment describes:

```
●  Slicing              10          5   Repair  ●
●  Spikes                7          0   Parts   ●
```

Left reads label-then-value, right reads value-then-label, and each box carries
its circle at its own **outer** end.

### The caps are smooth, not overlapping or clipped

Measured rather than eyeballed — the leftmost lit column of the left box's
leading cap, row by row:

```
y=722  695      y=730  693      y=738  693      y=745  694
y=724  694      y=732  693      y=740  693      y=747  694
y=727  693      y=735  693      y=743  693      y=749  695
```

Monotonic in, flat across the middle, monotonic out, symmetric about the box's
vertical centre. That is a clean rounded cap. A corner drawn at its native
32px against a 26px box would have overlapped itself and shown a step or a
doubled edge; there is neither, on the left box's left cap or the right box's
right cap.

## 2. Free options — confirmed

⚠ **I had to author the mix.** `locked-and-trapped`'s console costs **both**
its replies, so it cannot show a free one beside a costed one. I added
`costs = 4` to exactly one reply of **my own** `tester-strongroom` console and
left the other two bare, and copied `items/supplies/spike` into that package
so the Slice verb could run at all (TEST 131's lesson).

```
1 I was told to come this way.
2 [Slicing] Stand aside. (2 spikes)
3 Then stop me.
```

Two bare sentences with no bracket, no skill tag and no parenthetical, beside
one costed option in the usual format — in one list. `costFor(4, 10)` = 4 − 2
= 2, so the cost is computed rather than echoed.

## 3. The third texture — confirmed, and only a mutation could confirm it

The rendered cap disc measures **23 × 23** at design 14 × 1.596, filled solid
`(13, 89, 69)` = `C.border`, widening 3 → 23 → 8 symmetrically.

```
rendered pill cap vs uibit_fill_circ alpha        0.939
  ...vs a solid square   (control)                0.751
  ...vs a hollow ring    (control)                0.160
```

### ⚠ But shape similarity CANNOT settle this clause, and it is worth saying why

```
rendered cap      vs a maths-perfect disc         0.936
the ASSET ITSELF  vs a maths-perfect disc         0.938
```

**The ported art is a circle, and so is a generic circle.** The corner and
edge tiles were decisive at TEST 131 precisely because their shapes are
irregular; a disc carries no information that could tell provenance. Matching
the asset at 0.939 proves only that the thing on screen is round.

### So I mutated it

I replaced `uibit_fill_circ.png` **in my own built bundle** — the repo asset
and the pub-cache untouched — with a plus sign, and re-opened the terminal:

```
before   ●  Slicing   10
after    ✚  Slicing   10
```

**The cap rendered as a plus sign.** The drawn shape provably comes from that
file and not from a Flutter primitive. Asset restored afterwards; sha256 of
the restored file matches the copy I took before the swap.

## 4. The three small closures

### ✓ `In Stock` tracks the filtered list

Same item selected throughout, tab by tab:

| tab | rows shown | In Stock |
|---|---|---|
| ALL | 2 | **2** |
| WEAPONS | 0 | **0** |
| ARMOR | 0 | **0** |
| MISC | 2 | **2** |

At TEST 131 it read `2` on every tab including the empty ones. The 0/2
contrast is what makes this a reading: with only ALL and MISC I would have had
two tabs that agree by coincidence.

### ✓ `In Inventory` is a real count, and it tracks the item

```
Vibroblade selected   Item Cost 100   In Inventory 2     ← I carry 2
Medpac     selected   Item Cost  40   In Inventory 3     ← I carry 3
```

At TEST 131 it read `—`. Two different items giving two different correct
counts is the discriminator.

⚠ **The replacement-name half is unexercised.** `PT-1152` asks for a count
*plus* what the item would replace; nothing is worn on this bed, so only the
count shows. Not a defect on this evidence — a bed with a worn item in the
same slot would settle it.

### ✓ The display name reads consistently

`store-bed`'s blueprint is named **Medpac** now, and the list, the detail pane
and the file agree. That was a fixture inconsistency rather than an app
defect, as the blueprint's own new comment says.

### ✓ Notes autofocus — confirmed

```
Journal -> NOTES, NO CLICK:
  caret at x 469-470, y 224-243, RGB (200,164,90)   ← C.amber, blinking
```

At TEST 130 and TEST 131 the box was caretless until clicked. It is focused on
open now.

⚠ Watch the footer: it moved down when the footer portrait landed —
`NOTES` is at y 850 now, not 832. My first attempt clicked past it and read
"no caret" on the Journal, which would have been a false negative if I had not
screenshotted what was actually on screen.

## 5. Three of my own TEST 131 findings, confirmed fixed

Not routed, but they are in the screens I was already in.

### ✓ The panel overflow — read at BOTH window sizes, as promised

```
1900 × 1008    scale 1.596   design y=0 -> 85    design y=480 -> 851
1280 × 1008    scale 1.135   design y=0 -> 191   design y=480 -> 736
```

The pane's inner area runs to ~860 in both. **Nothing is clipped on either
axis at either size**, and all four readout rows are on screen — where at
TEST 131 two of four were unreachable at any size. `scaleWithin` is handed
`constraints.biggest` now rather than the window.

⚠ This is the reading I said at `PT-2554` I would take, and it is why:
a fix that only changed the number would have passed at 1900 and still
clipped at 1280.

### ✓ `affordable` — an unaffordable option now dims and says so

One spike held, a two-spike option:

```
1 I was told to come this way.
2 [Slicing] Stand aside. (2 spikes) ⚠ you have none      ← dimmed
3 Then stop me.
```

### ⚠ But *"you have none"* is a fixed string, and it contradicts the screen

`terminal.dart:173` appends `' ⚠ you have none'` whenever `affordable` is
false, and `affordable` is now `held >= cost` — so it prints for **any**
shortfall, not only for zero. On this screen the readout two boxes below it
read **`Spikes  1`**. A player is told they have none and shown that they have
one, at the same moment. `TerminalOption` carries no held count to say the
real number.

### ✓ The phantom `credits` row is gone

After a completed sale the bag lists exactly `stim-pack` and `vibroblade` —
no `credits` row. At TEST 131 one appeared per sale.

## 6. ✗ NEW AND SEVERE — the Inventory and dialogue show the STARTING purse

Found while confirming the credits filter above.

```
sold one vibroblade for 100, starting from 500

  the Store's readout          Credits  600
  the Inventory's readout      CREDITS  500
```

The save carries the transaction:

```
{"kind":"character.equipment-set","payload":{"credits":500}}
{"kind":"item.lost","payload":{"subject":"Buyer","item":"items/weapons/vibroblade"}}
{"kind":"item.acquired","payload":{"subject":"Buyer","item":"credits","count":100}}
```

Three readers, one fold, and two of them bypass it:

```dart
play_screen.dart:1871   creditsAfter(_log, subject: handle, starting: …)   // Store  ✓
play_screen.dart:2280   widget.character?.equipment?['credits']            // Inventory ✗
play_screen.dart:5688   widget.character!.equipment?['credits']            // Dialogue  ✗
```

The Store's own comment names `creditsAfter` as *"a completely separate
fold"*, so it is the authority — and the Inventory shows the purse the
character was authored with, forever.

⚠ **The dialogue one is the more consequential of the two.** `payment` is a
real gate term in the closed grammar, and `DialogueView.credits` is what
prices it. A player who has earned or spent anything is gated against the
number they started the campaign with.

⚠ Scope: the Inventory half is **measured in play** — 600 against 500 on the
same save. The dialogue half is a **source reading**; I did not build a
`payment`-gated bed for it, and I am not claiming I did.

## Fixtures

`mk131.py` gains **`mix`** — `tester-strongroom`, Slicing 10, spike count from
`$SPIKES`, bag of spikes only. Its console now costs exactly one of three
replies, so a free option and a costed one appear in the same list. The
package also received a copy of `locked-and-trapped`'s `items/supplies/spike`
blueprint, without which Slice refuses.

⚠ **`store-bed`'s `stim-pack.item` was renamed to "Medpac" by Coder** between
runs, closing TEST 131's name mismatch as a fixture inconsistency. Noted so
the earlier report is read against the right file.
