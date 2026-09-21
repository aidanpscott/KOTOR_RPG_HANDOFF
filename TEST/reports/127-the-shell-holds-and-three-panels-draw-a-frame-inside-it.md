# TEST 127 — the shell holds, and three panels draw a frame inside it

**Build.** App **`2f83cfe`** ("The shell, wired into play — PT-2498"), tree
clean, built from `git archive` of that sha. The committed lock resolves
Lodestar **`46f0fcea`**, and that is the pub-cache checkout
`package_config.json` compiles against. `check_shelf.py` clean: 29 rules
files and 65 standard blueprints.

**Verdict.** The shell itself is right — containment, divider and board
width all measured and confirmed. **Three of the four panels draw their own
sculpted frame inside it**, which is the one clause you asked me to check
and it fails. One further real finding: the empty-bag state is unreachable
for any character the app creates.

⚠ **CORRECTED AFTER FILING.** This report originally claimed the Powers
readout was blank for every power. That was wrong — see the retraction in
§3. The blanks were correct behaviour for unlearned powers, and my
"control" shared the same property as the cases under test.

---

## 1. The shell

### Containment, and the divider — confirmed

The board and party rail sit inside the sculpted border with a bronze
vertical divider between them: the rail occupies x 126–445, the divider
sits at x ≈ 447–460, the board pane runs x 447–1773.

**Nothing renders outside the frame or overlaps its edges.** Measured
rather than eyeballed — the frame's inner box, found by scanning inward
from all four sides:

```
frame inner box   x 126 – 1773    y 79 – 929
all content       x 151 – 1400    y 119 – 917
margins           left 25 · top 40 · right 373 · bottom 12
content pixels outside the box: 0
```

### The board fills its available width — confirmed, with a wide board

A 6-wide board looks small, so I re-ran on the 14-wide `m01-guard`:

```
board pane   x 447 – 1773   (1326 wide)
board grid   x 528 – 1692   (1165 wide)
gaps         left 81 · right 81
```

Equal margins and 88% of the pane — not letterboxed, not undersized. The
small board is small because it has six columns, not because the pane is
constrained.

### ✗ A frame inside a frame — three panels of four

Opening a panel over the board gives **two complete sculpted frames**, each
with its own row of studs, its own side bosses and its own rounded corners.
It is unmistakable at any zoom: the outer shell's stud row, its inner edge,
and then the panel's own frame beginning below it.

Measured, and the split is clean:

| panel | box | framed? |
|---|---|---|
| Inventory | x 684–1773, y 141–929 (1089 × 788) | **yes** |
| Equip | x 684–1773, y 141–929 (1089 × 788) | **yes** |
| Abilities | x 685–1773, y 142–929 (1088 × 787) | **yes** |
| **Character Sheet** | x 620–1773, y 79–929 (1153 × 850) | **no** |

The three framed panels are pixel-identical to one another, so they are
consistent among themselves — but they are inset inside a second border,
and the Character Sheet is not: it runs flush to the shell's own inner edge
at y 79 and carries one border only.

So the Character Sheet is the one that matches the clause, and it is the
odd one out.

## 2. Inventory

**The seven-category strip is there and it filters.**
`FILTER │ ALL DATAPADS WEAPONS ARMOR USEABLE QUESTS MISC`, and choosing
WEAPONS reduces eighteen rows to exactly the three weapons —
`blaster-pistol (Equipped)`, `blaster-rifle`, `vibroblade`.

**`(Equipped)` marks worn gear**, on exactly the four slots the fixture
dresses: belt, blaster-pistol, clothing, mask.

**CREDITS is a real number** — `1375`, the value I authored, and it holds
across tab changes. A fixture authored at 0 reads 0, so it is the record's
number rather than a constant.

⚠ **The icon is a slot, not an icon.** Every row draws a rounded square to
the left of the name and every one of them is empty. The screen's own
comment says so — *"the box is empty and visibly a placeholder"*. So the
clause is name + an icon *slot*; there is no artwork yet.

**Both empty states exist and read differently:**

```
nothing here under DATAPADS — the filter is hiding 16 other things
carrying nothing — nothing picked up yet
```

The first even counts what it is hiding.

### ✗ But the empty-bag state cannot be reached by any character the app makes

I could only produce `carrying nothing` by hand-writing a record. Every
character the app creates shows one row: **`standard (Equipped)`**.

`ledger_writer.dart` writes `'route': 'standard'` into the equipment
payload at three separate sites, and both the Inventory list
(`play_screen.dart:1546`) and the Equip screen's `worn` map take **every
String value** in the equipment map:

```dart
for (final e in eq.entries) if (e.value is String) …
```

`route` is a String, so the character's equipment *route* is rendered as a
worn item called "standard". Dropping the key and changing nothing else
gives `carrying nothing — nothing picked up yet` immediately, which is how
I know the message works and what is blocking it.

## 3. Abilities

**Three genuinely different layouts — not one list in three hats:**

| tab | list | readout |
|---|---|---|
| SKILLS | named rows with checkboxes | SKILL RANK · BONUS · TOTAL RANK |
| POWERS | a nine-column icon grid of `?` tiles | BASE COST · ADJUSTMENT · COST PER USE |
| FEATS | chains of boxes joined by `→` | none |

**Feats' description pane grows into the readout space** — measured:

```
SKILLS  description pane  y 346 – 608   (262 tall)  + readout below
FEATS   description pane  y 371 – 696   (325 tall)  no readout
```

The Feats pane extends into the band where the other tabs put their
numbers, which is the clause exactly.

**Two feats show their own distinct names.** Selecting two different boxes
gives **`Cautious`** and **`Gear Head`**, each with its own description
("Careful, deliberate handling of dangerous…" / "An instinct for
machinery — what it does, how it…"). Not a truncated letter, not the same
name twice.

**An unpriced power shows a dash** — `BASE COST --`, `ADJUSTMENT --`,
`COST PER USE --`. No `null`, no `0`.

### ⚠⚠ RETRACTED — the clause passes, and properly

**As first filed this section claimed every power reads `--` and every
power is titled `UNKNOWN FORCE POWER`. That is wrong, and Coder was right
not to be able to reproduce it.**

`UNKNOWN FORCE POWER` is the **deliberate label for a power the character
has not learned** — `abilities_screen.dart:534` documents it and `:542`
implements it as `p.known ? p.name : 'UNKNOWN FORCE POWER'`, with `:604`
dashing the costs on the same condition. The grid shows the **whole
106-power roster in shelf order** (`PT-1250`: *"an unlearned power is
present and anonymous"*), and the character in my fixture knew four. All
three tiles I sampled were unlearned, so all three were correct.

Re-run on the same build with the tiles located by pixel rather than by my
own arithmetic, which is what went wrong:

| power | known? | priced? | title | costs |
|---|---|---|---|---|
| Force Scream (#46) | yes | yes | **Force Scream** | **8 · 0 · 8** |
| Crush Opposition II (#8) | yes | no | **Crush Opposition II** | `--` · `--` · `--` |
| any unlearned | no | either | `UNKNOWN FORCE POWER` | `--` · `--` · `--` |

So the routed clause — *an unpriced power shows a dash, not `null` or
`0`* — **passes, and not vacuously**: a known priced power shows real
numbers, a known unpriced one shows dashes, and the two are distinguishable
on screen.

⚠ **Why I got it wrong, since it is the same shape twice.** I did pair the
negative with a positive, as the standing practice says — I deliberately
sampled two *priced* powers as the control. But both controls were
**unlearned**, so they shared the property that actually caused the blank.
A control that shares the defect's cause is not a control. The property I
needed to vary was `known`, and I never checked which powers the fixture
had learned.

⚠ **And the feat chain tiles carry no label and no icon** — they are empty
red-bordered boxes joined by arrows, so a chain cannot be read until each
box is clicked one at a time.

## Also noticed

* `Escape` closes an open panel and returns to the board rather than
  leaving it — `PT-2465` holding, incidentally confirmed several times.
* Abilities opens on **`v`**, not `b`; `b` is the short meditation.

## Fixture

`tester-mind`. `mk124.py` now takes a board argument and authors **1375
credits** and a bag chosen to land in four of the seven tabs and miss two,
so DATAPADS and QUESTS have a real negative behind them. `mk123.py` gains
**`bare`** — no body item *and* no `route` key — which is the only way I
found to reach the empty-bag message.
