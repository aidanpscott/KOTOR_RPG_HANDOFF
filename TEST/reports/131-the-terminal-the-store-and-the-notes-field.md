# TEST 131 — the terminal, the store, and the note that finally typed

**Build — the full chain.**

```
local HEAD            9fa0252  "Draw the terminal's real border art — PT-2551"
working tree          clean
pubspec.lock resolves lodestar  8e6d2ee5630c871dff4091ac22e2e698464d1251
                      lens      32b77e3bf2aa0ec6e624df25e06f8eed0910d2cd
package_config.json   ~/.pub-cache/git/Lodestar-8e6d2ee5.../
                      ~/.pub-cache/git/Lens-32b77e3b.../
built from            git archive 9fa0252
```

All three agree. `check_shelf.py` clean: 29 rules files, 65 standard
blueprints.

**Verdict.**

* **Terminal — the border art is confirmed, and it is genuinely the ported
  texture.** Matched against the shipped PNGs pixel-for-pixel, with controls.
  Per-tile rotation and corner mirroring are right on all four sides. **Two
  defects**: two of the four readout rows are off-screen, and an option the
  player cannot afford is drawn identically to one they can.
* **Store — it works end to end.** Real dialogue trigger, real catalogue
  prices, buy and sell both write. **Three defects**, one of which puts a
  phantom `credits` row in the player's bag after every sale.
* **⚠⚠ NOTES — I WAS WRONG IN TEST 130, AND IN THE PRODUCT'S FAVOUR.** A note
  **can** be typed and saved. See §4.
* Companion sheet: unchanged and correct.

⚠ **I did not re-run TEST 130's four closed confirmations** — the classifier
pair and census, the dismissed-companion name, the phantom re-add and Escape
were all confirmed on `93fdcf0` and filed as `0dd1cfd`. A closed test is a
slice not spent on something unseen. Only the Notes half was still open, and
that one is answered below.

---

## 1. The terminal

Reached the way a player does: `locked-and-trapped`, walk to the console,
right-click, `Slice (Slicing)`.

```
slice — d20 5 + Slicing 10 = 15 vs 15 (moderate) · in
```

### ✓ The border is the real ported art — measured against the file

Not "it looks textured". The rendered border compared against the shipped
PNGs' own alpha channel, upscaled nearest-neighbour to the drawn tile size:

```
bottom-left corner  vs uibit_brdr_16wc alpha    0.978
bottom edge tile    vs uibit_brdr_16we alpha    0.985
  ...vs a solid square      (placeholder control) 0.246
  ...vs a 1px outline       (placeholder control) 0.730
```

The two controls are what make this a reading rather than an impression: a
placeholder of either obvious kind scores far lower.

### ✓ The tint is exactly `C.border`

A census of the top border band, 8px × 1000px:

```
(13, 89, 69)  7978 px      ← C.border, 0xFF0D5945
(13, 88, 68)    12 px      ← antialiasing
(13, 84, 66)     4 px
```

⚠ I nearly filed this as wrong. My first sample took the *brightest* mint
pixels and got `(142,215,195)` — which turned out to be the transcript **text**
at y 198–215, not the border at all. The cross-section is the honest reading.

### ✓ Per-tile rotation and mirroring, on all four sides

Every claim in `_BorderPainter`'s own comments, with a control beside it.
`1.000` is identical:

```
CORNERS                                        control (unflipped)
  TL vs BL flipped vertically      0.989           0.607
  TR vs TL flipped horizontally    0.989           0.604
  BR vs BL flipped horizontally    0.990
  BR vs TL flipped both            0.979

EDGES
  top vs bottom flipped vertically 0.985           0.746
  LEFT  vs rot90(top, +90°)        1.000           0.790 at 0°
  RIGHT vs rot90(top, −90°)        0.985           0.746 at +90°
  left vs right flipped            0.985           0.746
```

**The left run is an exact 1.000 match to the top tile rotated a quarter
turn** — no interpolation, which is what the comment claims pixel art needs
and what `DecorationImage` could not have done. The controls are all 0.6–0.8,
so the comparison discriminates.

Tiling along the top run: consecutive 67px tiles match each other at
0.866–0.929, i.e. the run repeats at the texture's own pitch.

### ✓ Transcript, options and real numbers

```
STRONGROOM CONTROL — AWAITING INSTRUCTION

1 [Slicing] Unseal the vault door.  (2 spikes)
2 [Slicing] Cycle the corridor lights. (1 spike)

Slicing   8
Spikes    1
```

**The costs are computed, not printed.** The bed's two replies carry bases
**3** and **1**, and `reductionFor` steps at 4, 9, 16, 25, 36. So I ran it
twice:

| Slicing | reduction | base 3 → | base 1 → |
|---|---|---|---|
| 10 | 2 | **1 spike** | **1 spike** |
| 8 | 1 | **2 spikes** | **1 spike** |

⚠ **The Slicing-10 run alone proves nothing** — both options print `1 spike`
there, so a screen that hard-coded 1 would read identically. The Slicing-8
run is the discriminator, and it separates them. Pluralisation is right too.

**The supply count is live**: 6 spikes → `Spikes 5` after the first attempt →
`4` after the second → `1` on the second character. Every attempt spends one
whether it lands or not, exactly as `§5.2` says.

### ✗ Two of the four readout rows are off-screen

`LBL_COMP_SKILL`, `LBL_COMP_SPIKES`, `LBL_REP_SKILL`, `LBL_REP_UNITS` sit at
design y 357, 376, 395 and 414. Measured from the frames' own edges the panel
renders at scale **2.10** with design y=0 at y≈85, so:

```
row 1  Slicing   design 357 -> y 820   visible
row 2  Spikes    design 376 -> y 859   clipped in half
row 3  Repair    design 395 -> y 898   OFF SCREEN
row 4  Parts     design 414 -> y 938   OFF SCREEN
```

The shell's inner area ends at y≈878. **Repair and Parts cannot be read at
any window size on a 1920×1080 display** — the largest the window goes is
1900×1008.

The cause is one argument. `play_screen.dart` passes

```dart
scale: TerminalPanel.scaleWithin(MediaQuery.sizeOf(context))
```

— **the whole window**, not the box the panel is drawn into. At 1900×1008
that is `min(2.97, 2.10) = 2.10`, so the panel asks for 480 × 2.10 = 1008
pixels of height: the entire window, inside a pane that starts below the
shell's border and ends above the footer.

⚠ And at **1280 wide it also overflows to the right** — the transcript, both
option lines and every readout value are cut off at x≈1160. `scaleWithin`
returns `min(2.0, 2.1) = 2.0` there, giving a 1280-wide panel inside a
narrower pane.

⚠ This is the same shape as the defect the field's own comment says it fixed:
*"a scale belonging to one coordinate system, applied to another."* The fix
moved from the app's `s` to `scaleWithin` and kept handing it the wrong box.

### ✗ An option you cannot afford is drawn exactly like one you can

Second run: the character holds **1 spike** and option 1 costs **2 spikes**.
Measured across both rows:

```
option 1 (costs 2, holds 1)   3282 lit px   mean RGB (166.0, 167.9, 146.4)  max (204,204,178)
option 2 (costs 1, holds 1)   3388 lit px   mean RGB (166.8, 168.7, 147.1)  max (204,204,178)
```

Identical to within a unit. `play_screen.dart:6379` hard-codes

```dart
affordable: true,
```

under a comment reading *"**The supply itself does not exist yet**: nothing
carries spikes"* — three lines above the `readout:` that counts real spikes
off the bag. `TerminalOption.affordable`'s own documentation states the rule
it misses: *"An option they cannot afford is shown and says so."* It is shown.
It does not say so.

### ⚠ Two stale comments

* `play_screen.dart:4467` — *"`PT-1149`'s terminal screen is what it opens.
  **Not wired to that screen yet**"* — it is wired; `_openTerminal` is thirty
  lines further down and I reached it.
* `play_screen.dart:6404-6420` — the same six-line ⚠⚠ comment about the
  panel's own scale appears **twice in a row**.

### ⚠ And a fixture lesson worth writing down

My first run used `tester-strongroom` and Slice refused with *"no spikes
left"* while the Inventory listed a `spike` row. The bag was fine; the
package was not. **Carried item paths resolve inside the SELECTED package**,
and `tester-strongroom` ships no `items/supplies/spike`, so `supplyAt` could
open none of them. `locked-and-trapped` ships the blueprint, which is why the
run above is on Coder's bed and not mine. Not a product defect — TEST 123's
lesson, landing on me a second time.

## 2. The store

Reached as described: walk into the merchant, the conversation opens, reply 1
carries `store.opened`.

⚠ **Walking INTO the merchant is the trigger** — there is no Talk verb. The
right-click menu on a merchant offers only `Examine (Xenology)` and
`Repair ⚠ not a droid`. `_step` reads *"a creature with a conversation is
ALWAYS spoken to"*, so contact starts the talk. Worth knowing before hunting
for a verb that is not there.

### ✓ It opens, prices are real, and both directions write

```
Buying Items          All | Weapons | Armor | Misc
  Vibroblade                   Item Cost   100
  Medpac                       Credits     500
                               In Stock    2
                               In Inventory —
```

```
buy   credits 500 -> 400      accept button pressed once
sell  credits 400 -> 500
```

And the events are exactly the documented pair — decoded from the save:

```
item.acquired  {subject: Buyer, item: items/weapons/vibroblade}
item.lost      {subject: Buyer, item: credits, count: 100}      ← the buy
item.lost      {subject: Buyer, item: items/weapons/vibroblade}
item.acquired  {subject: Buyer, item: credits, count: 100}      ← the sell
```

**Show Sell List / Show Buy List toggles both ways**, and the title and the
accept button track it: `Buying Items` → `Selling Items` → back, with the
third button reading the opposite each time.

### ✗ Selling puts a phantom `credits` row in the bag

After one sale the Inventory lists **three** things:

```
credits          ← not an item
stim-pack
vibroblade
```

`item.acquired {item: "credits"}` is folded into `carriedBy` like any other
path, so every sale adds one. The same family as TEST 127's
`standard (Equipped)`: a reserved string reaching a list that renders paths as
items.

### ✗ `In Stock` is the length of the list, not the item's stock

`store_screen.dart:151`:

```dart
_readoutRow(k, 'In Stock', item == null ? '—' : '${_list.length}', 2),
```

It read **2** for the vibroblade, and **2** again on the Weapons tab where the
list was **empty**. It is the catalogue's size, under a label that names the
selected item's stock.

### ✗ `In Inventory` never shows a count

`_onHandText` returns the **name of what the selected item would replace**,
or `—` when the item has no slots. I carried two vibroblades and the row read
`—`. `PT-1152`'s approved extension says the row *"**also** names what the
item would replace"* — K2's count plus the name. The code has the name
**instead of** the count, so the row labelled `In Inventory` cannot tell you
what is in your inventory.

### ⚠ The display name is the catalogue's, not the package's

`candidateFrom` takes `name: rec?.name ?? short` from the catalogue join. The
bed's blueprint is named **"Stim Pack"**; the store lists **"Medpac"**. The
price comes from the same join and is right, so the join itself is working —
but a package author's own `name` never reaches the screen.

### ⚠ Two things that look like store defects and are NOT — controls run

* **Weapons and Armor tabs are empty**, and the vibroblade files under Misc.
  **But the Inventory in the same package agrees** — its WEAPONS tab reads
  *"nothing here under WEAPONS — the filter is hiding 3 other things"*. Same
  answer from both screens, so the category join is consistent and the bed's
  minimal blueprints are what do not resolve to a weapon section. A store bed
  drawing on base-rules' item tree would settle it.
* **"this item carries no description"** for an item whose blueprint carries
  one. **The Inventory says the same thing for the same item.** Shared
  resolver, same answer, so it is not the store.

⚠ Also: the accept button is labelled `Buying Items` / `Selling Items` — the
mode, not the action. `_modeTitle` feeds both the screen title and the
button, deliberately, *"so title and accept button cannot disagree"*. The
consequence is that the only control that buys anything is named after the
screen it is on.

## 3. The companion sheet — confirmed, unchanged

Secondary-tapping a companion's portrait opens **EQUIP**, named for them:

```
EQUIP · implant
no equipment is recorded for Second Guard — a companion is a blueprint in
the roster and carries none
you are carrying nothing for this slot
```

Not the Character Sheet. Correct and unchanged.

## 4. ⚠⚠ NOTES — I WAS WRONG IN TEST 130

**A note can be typed and saved.** TEST 130 reported that I could not
determine whether a focused field accepts characters. It does:

```
typed into the field:  XY
console/notes/tester-mind.json:  {"text":"XY"}
save event:  {"kind":"note.written","payload":{"chars":2}}
"XY" anywhere in the save body:  False
```

So the routed clause is **confirmed**, and the privacy guarantee holds on the
same note: the length is recorded, the text is not.

**What was actually wrong was my harness, and the evidence is now positive
rather than absent.** `xdotool type` at a 150ms delay landed both characters;
single `xdotool key a` in the same breath did not, and longer strings at
45ms, 120ms, 160ms and 250ms mostly still do not. On Linux, Flutter takes text
from the GTK input-method context rather than the raw key stream, and my
synthetic keys reach that path only intermittently. **One success is enough to
settle the direction** — the field works and my instrument is unreliable,
not the other way round.

### ✗ But `autofocus: true` still does not take

Unchanged from TEST 130 and reproduced on this build too:

```
Journal -> NOTES, no click    lit px  3206 3206 3206 3206 3206 3206   no caret
then one click in the box     caret at x 469-470, y 221-239, RGB (200,164,90)
```

A tap anywhere in the box focuses it — the `GestureDetector` half works, and
it works on empty space far below any text. The `autofocus` half does not, so
a player who opens the screen to write still meets a box with no caret and has
to click. The fix's own comment names that as the thing it removed: *"one more
click before you can begin is a step with no decision in it."*

## Fixtures

`mk131.py`:

* **`term`** — `locked-and-trapped` (**Coder's**, not mine: it ships
  `items/supplies/spike` and `tester-strongroom` does not), Slicing 10, six
  spikes. `set_board=False` so nothing rewrites somebody else's package.
* **`cheap`** — the same bed at **Slicing 8** with **three** spikes: the
  reduction drops to 1 so the two bases print as 2 and 1, and the panel is
  reachable while holding fewer spikes than the dearer option costs.
* **`store`** — `store-bed`, 500 credits and a bag built **only** from the two
  paths that package ships.

⚠ `record_validate` refused my first save outright — *"security at rank 10,
persuade at rank 10 — 2 skills are above the no-aptitude cap… §11.4's racial
choice can account for at most 1 of them."* Correct, and the fixture now puts
one skill above the cap and moves the origin's aptitude onto it.
