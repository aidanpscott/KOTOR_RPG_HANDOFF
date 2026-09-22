# TEST 130 — TEST 129's five severe fixes, re-confirmed

**Build — the full chain, re-declared as promised.** The lock moved twice
during the last exchange, so none of TEST 129's numbers hold.

```
local HEAD            93fdcf0  "TEST 129's five severe defects — PT-2538, PT-2540"
working tree          clean
pubspec.lock resolves lodestar  df9dda46e68025fe2659ca8b3a1125070f38199b
                      lens      32b77e3bf2aa0ec6e624df25e06f8eed0910d2cd
package_config.json   ~/.pub-cache/git/Lodestar-df9dda46e68025fe2659ca8b3a1125070f38199b/
                      ~/.pub-cache/git/Lens-32b77e3bf2aa0ec6e624df25e06f8eed0910d2cd/
```

All three agree. Built from `git archive 93fdcf0`. `check_shelf.py` clean:
29 rules files and 65 standard blueprints.

⚠ For the record of what moved: TEST 129 declared Lodestar `29c636b7`; a
mid-conversation note showed `1b69d5c9`; the build under test is `df9dda46`.

**Verdict.** **Four of the five are confirmed outright.** The fifth — Notes —
is **half confirmed and half unreachable by my harness**, and I will not
claim the half I could not read. Two further findings, one of them a
surviving instance of the same defect in chargen.

---

## 1 · The classifier — reading one: the pair

Both halves, run on the same benches as TEST 129, same hazard shape, same
character:

| board | landed | TEST 129 | **now** |
|---|---|---|---|
| `a0334` | `shaken for 30 rounds` | GOOD EFFECTS ✗ | **BAD EFFECTS** ✓ |
| `a0330` | `slowed for 30 rounds` | BAD EFFECTS | **BAD EFFECTS** ✓ |

```
GOOD EFFECTS                    BAD EFFECTS
none                            shaken — 30 round(s) left
```

The specific defect is fixed and the control did not regress. **And as
`PT-2541` predicted, the pair no longer discriminates** — both sides read the
same now, so this reading alone could not tell the shipped fix from a hundred
wrong ones. That is what reading two is for.

## 2 · The classifier — reading two: the census, with a live control

Run against the engine the app actually compiles against, through its own
`conditionPolarity` rather than a reimplementation:

```
beneficialConditions      = {} (0 entries)
conditionNames            = 21 names
probed                    = 31 (31 bad, 0 good)
names reaching GOOD       = []
```

The 31 are the engine's own 21 — `conditionNames.toList()`, not a list I
typed — plus ten I invented to stand for what a future ruling or a package
could mint: `blessed`, `hasted`, `inspired`, `shielded`, `regenerating`, and
the degenerate `''`, `' '`, `'SHAKEN'`, `'Shaken'`, `'slowed '`. **Not one
reaches the good column.** The five invented plausible-benefit names are the
exact case the old default got wrong and the case a list-patch would have
reopened; they are bad now.

### The control — the good branch is live, and the census is not vacuous

A census returning "everything is bad" would read identically against
`EffectPolarity conditionPolarity(_) => bad`. So I mutated it.

⚠ **On a COPY.** The pub-cache is shared with Coder and I did not touch it —
`cp -r` to scratch, one edit, a throwaway package with a path dependency.

```
beneficialConditions = {'blessed'}      ← the single mutation
  blessed      good
  shaken       bad
  slowed       bad
  paralysed    bad
  hasted       bad
```

So the good branch is reachable, one name flips it, and everything else stays
bad. **The census result is caused by the set being empty, not by a dead
branch** — which is the reading that would still catch a regression to a
hand-maintained list.

### And it is the shape `PT-2540` ruled

`conditions.dart:603`:

```dart
EffectPolarity conditionPolarity(String name) =>
    beneficialConditions.contains(name) ? EffectPolarity.good
                                        : EffectPolarity.bad;
```

`play_screen.dart` now switches exhaustively on the result and no longer maps
an unknown onto either column itself. The decision left the screen.

### ⚠ One new path I could not reach, and why

The fix adds `(not a condition the rules name)` for an unruled name. **No
shipped or authorable content can produce one.** `effect.dart:383` refuses a
condition outside `conditionNames` at load — *"the vocabulary is closed; a word
outside it is refused rather than mapped to the nearest member"* — and
`Condition` has exactly one construction site in the engine
(`conditions.dart:256`), fed by that validated path.

So the provenance tag is a defence with no current route to it. Correct as
belt-and-braces, and I am reporting it as unexercised rather than confirmed.

## 3 · A dismissed companion shows a real name — confirmed

Ten on the roster, three fielded, seven dismissed and never placed this
session. All seven:

```
Frail Guard      Assassin Droid    Astromech    Bare Droid
Battle Droid     Remote            Subject
```

Not one tag. **And not the path-derived form either**, which is the
discriminator worth having: `rosterRowName`'s last resort is
`_readableFrom(from)`, which would turn `characters/dr-assas` into
`Dr Assas` and `characters/frail` into `Frail`. Every row shows the
blueprint's own `name` field instead — `Assassin Droid`, `Frail Guard` — so
`_rosterNames` is reading the blueprint, not decorating the path.

## 4 · The phantom re-add — confirmed

Removed a fielded companion, then re-added the same one without a reload,
which is the exact path that produced the phantom:

| | TEST 129 | **now** |
|---|---|---|
| sidebar vitality | `0 of 0` | **`400 of 400`** |
| sidebar subtitle | `in the fight, and the round does not hold it` | **absent** |
| sidebar verbs | none | **Wait here · Dismiss from party · Trade / give item** |
| Party row | `REMOVE` dimmed, *"down — not until this fight is over"* | **`REMOVE` live, no refusal line** |
| count | `PARTY IS FULL — 3 of 3` | `PARTY IS FULL — 3 of 3` |

All three symptoms gone, and the slot is releasable again.

## 5 · Escape — confirmed across nine surfaces

Pre and post screenshot on each, measured as lit pixels in the panel band:

| open | Escape goes to | TEST 129 |
|---|---|---|
| Equip | the board ✓ | the board |
| Inventory | the board ✓ | the board |
| Character | the board ✓ | — |
| Abilities | the board ✓ | — |
| **Party Selection** | **the board** ✓ | **nothing** ✗ |
| **Journal** | **the board** ✓ | **nothing** ✗ |
| Options | the board ✓ | — |
| **Messages** | **the Journal** ✓ | **nothing** ✗ |
| **Notes** | **the Journal** ✓ | **nothing** ✗ |

```
equ: panel-band lit px  pre    715 -> post      0
inv: panel-band lit px  pre   1344 -> post      0
chr: panel-band lit px  pre    612 -> post      0
abl: panel-band lit px  pre      0 -> post      0   (its title sits lower;
                                                     verified by eye — panel
                                                     gone, board clear)
pty: panel-band lit px  pre   1997 -> post      0
jrn: panel-band lit px  pre   2459 -> post      0
opt: panel-band lit px  pre   1017 -> post      0
```

Messages and Notes go **back one level to the Journal**, not to the board —
matching their own `◂ JOURNAL` button, and a second Escape then reaches the
board. That reads right rather than wrong, and it is worth writing down
because "closes all seven screens" would have predicted the board.

## 6 · Notes — the focus half is fixed; the typing half I cannot read

### ✓ The field can now be focused, which is the defect I filed

TEST 129's finding was *"nothing can ever give the field focus"*. It can now.
Measured rather than inferred — a burst of frames 0.2s apart:

```
lit px in the notes box:  146  184  146  184  146  184  146  184
the alternating element:  x 469-470, y 221-239, RGB (200,164,90)
```

A 2 × 19 pixel bar in `C.amber` at the box origin, blinking at about 0.5 Hz.
That is `cursorColor` — the caret. **Before the fix there was none by any
route.** Reproduced in two separate sessions.

### ✗ But `autofocus: true` does not take — a click is still required

The fix's comment says the field *"takes focus on open… one more click before
you can begin is a step with no decision in it."* It does not:

```
Journal -> NOTES, no click        lit px 146 146 146 146 146 146   no caret
then one click inside the box     lit px 146 184 146 184 146 184   caret
```

Two sessions, same result. The `GestureDetector` half works — a tap anywhere
in the box, including empty space well below any text, takes focus. The
autofocus half does not, so opening the screen still leaves a player facing a
box with no caret.

### ⚠ Whether a focused field accepts characters, I could not determine

With the caret confirmed present immediately beforehand, **nothing I send
produces a glyph**:

```
xdotool type --delay 45/120       nothing
xdotool key a / b / c / d         nothing, and the caret never moves
xdotool type --window (XSendEvent) nothing
Ctrl+V against a real X clipboard  nothing
```

⚠ **And I do not think this is a product defect, but I cannot prove it is
not.** The evidence cuts both ways:

* **Key events DO reach the app** from my harness — arrows move the player,
  `Escape` walks the panel chain, `Down` sprang the hazard, and `i` opened the
  Inventory from the board during this run.
* **But characters are a different channel on Linux Flutter.** `EditableText`
  takes text from the platform text-input plugin via the GTK input-method
  context, not from the raw key stream, and my synthetic keys have never put a
  character into **either** `EditableText` in this app — before the fix or
  after it. The one exception is the two characters that landed once in
  TEST 129 and never reproduced.
* I looked for a second text field to use as a control and the only other one
  in the app is chargen's, which is behind a ten-step flow I could not drive
  to the end — see below, and it has its own problem anyway.

**What would settle it in one second: a human pressing a key on the Notes
screen.** If a character appears, this item is fully closed and the remaining
defect is only the autofocus. If none appears, the field is still unusable and
it is severe.

⚠ Note the clipboard attempt needed a helper — `xclip` and `xsel` are not
installed on this machine, and my first paste test in TEST 130 was void
because of it. The retry used a GTK clipboard owner.

## 7 · ⚠ THE SAME DEFECT IS STILL LIVE IN CHARACTER GENERATION

Source only — I could not reach the step in play, and I am not claiming I
did.

`chargen/identity_screen.dart` uses the same raw `EditableText`, and its
`_Field` wrapper reads:

```dart
focusNode: focus ?? FocusNode(),        // :679
```

with **no autofocus and no gesture detector** — the exact shape TEST 129
found. Its two call sites differ:

* **`:459` — the NAME field — passes no `focus`.** So `focus ?? FocusNode()`
  mints a **fresh node on every build**, which is worse than the Notes bug
  was: even something that did request focus would lose it on the next
  rebuild. Nothing requests it. This is the field a player types their
  character's name into.
* **`:577` — the story field — passes a persistent `_storyFocus`**, and one
  thing in the file calls `requestFocus()` on it: the **CLEAR button**
  (`:600`). So that field is focusable by pressing an unrelated button and
  not by clicking it.

`grep` for `requestFocus|autofocus` across `lib/` finds them in
`notes_screen.dart` and nowhere else outside this file's one CLEAR handler.

⚠ **Stated as a source reading, not a play confirmation.** Chargen is ten
steps deep and Origin alone wants a homeworld, an aptitude and an upbringing
before it advances; I stopped rather than spend the slice there. If it
reproduces, it is the same fix in two more places, and the name field is the
worse of the two.

## Fixtures and method

`mk112.py shaken` / `slowed` — Coder's condition benches, unchanged. One
unavoidable hazard a square from the spawn, so the two runs differ only in the
condition's name.

`mk129.py party` — ten companions off ten distinctly-named blueprints, three
fielded.

`tool/census.dart` — the 31-name census through `conditionPolarity`.
`mut/` — a **copy** of the pub-cache Lodestar with one name added to
`beneficialConditions`, plus a throwaway package with a path dependency on it.
The pub-cache itself was not touched.
