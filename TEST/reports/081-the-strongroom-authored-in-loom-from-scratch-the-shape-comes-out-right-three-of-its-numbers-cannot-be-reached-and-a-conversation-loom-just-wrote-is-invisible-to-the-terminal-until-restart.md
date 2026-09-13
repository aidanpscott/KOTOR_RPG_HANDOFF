# TEST 081 — the strongroom authored in Loom from scratch, without reading
# Coder's diff: the shape comes out right and every object verifies. But
# three of the fixture's six numbers cannot be reached through the UI at
# all, a conversation Loom has just written is invisible to the terminal
# that needs it until you restart, and an item cannot be a key.
# Separately: `7d18e28` re-verified live on all four skills.

**SYNC — done first, and confirmed.** `cd Loom && git pull` → *Already up
to date*; local `Loom` HEAD `270cdde` (*Loom authors all six fields, and
stops destroying two of them — PT-1957*). `flutter pub upgrade lodestar`
→ *No dependencies changed* (needed `source env.sh` first; the toolchain
lives under `~/spike` and is not on PATH). **`pubspec.lock` resolved-ref
reads `8ef6c775b838a2863f82027005de8f29a6e537d2` ✓**, the pub-cache
checkout `Lodestar-8ef6c775…` exists, and I confirmed the engine there
actually reads the new fields (`disarm` in `area_open.dart` and
`exploration.dart`; `area_open.dart:272: final ky = e['key'];`).

**The app, for Part 2:** `run-app.sh` (always rebuilds). Local
`KOTOR-RPG-APP` HEAD `9c4f050` (*a shut door blocks before anything is
spent — PT-1957*), clean; its `pubspec.lock` pins `lodestar`
`3e7fad608d284afe473e034dc3e32f025cf5d017`, checkout present. **Note the
two apps are on different engine pins** — `8ef6c77` for Loom, `3e7fad60`
for the app — which is normal and worth saying so nobody reconciles them.

`check_shelf.py` at session start: `✓ 25 rules files, all identical to
what the extracts generate`. Loom PIDs `19495` and `23462`, app PID
`27267` — all killed by PID, all confirmed gone.

**I authored into my own new package `tester-strongroom`, not into
Coder's shipped `locked-and-trapped`.** Overwriting Coder's would have
clobbered shared state that the app loads and that is tracked in git.
Everything below was reached through Loom's UI only; I did not open
Coder's file until the very end, to compare.

---

## PART 1 — authoring it

**It works.** Package → area (12 × 6) → mine → footlocker → console →
crate → vault door → keyed door → guard → arrival, all through the
palette, all written correctly, and Loom's own Verify reports **nothing
wrong with any of them**. Every problem it raises is about the package
manifest and the nine per-class starting weapons, not about the six new
fields.

Structurally my file and Coder's are the same file. What differs is:

| | Coder's | mine | why |
|---|---|---|---|
| `notice` | 12 | 12 | written by *default*, not chosen — see D3 |
| footlocker `locked` | **18** | 20 | 18 is not on the ladder |
| vault `locked` | **28** | 30 | 28 is not on the ladder |
| `kinds` | `["poison"]` | *absent* | no control exists |
| crate `kind` | `"fixture"` | *absent* | benign — see below |

---

### ⚠ D1 — a conversation Loom has just written is invisible to the terminal that needs it, until you restart

This is the one that stops the walkthrough as written.

Coder's step is *"terminal, a tier, then pick a conversation from a list
— never typed."* I did exactly that. `conversations` **+** → the wizard →
`Write`. The status bar said
**`wrote /home/aidan/.local/share/kotor-rpg/packages/tester-strongroom/dialogue/console.toml`**
and the file was on disk.

The console placement still read **`no conversations in this package yet
— a terminal with none is an empty screen`**. The `conversations` node in
the module tree also still refused to expand — so it is the whole module
model that has not rescanned, not just that one pick-list.

**I restarted Loom to tell a refresh bug from a path mismatch.** After
the restart the conversation appears in the tree, the row appears on the
placement as `says  console`, one click writes
`conversation = "dialogue/console"`, and everything is correct. So the
paths are right and the writer is right — the open module simply never
learns about it.

**Why this is a defect and not a design choice:** the *item* pick-list on
the very same selection bar refreshes immediately. I created
`items/misc/sith-keycard` while a door was already selected, and the `or
a key  sith-keycard` line appeared on that door without so much as a
re-click. Two lists on one panel, one refreshes and one does not.

---

### ⚠ D2 — every DC on a placement is a fixed seven-step ladder, and three of this fixture's numbers are not on it

The lock rows and both hazard DC rows offer only
`trivial 5 · easy 10 · moderate 15 · hard 20 · formidable 25 · heroic 30
· legendary 35`. There is no free entry anywhere on them.

So `notice = 12`, `locked = 18` and `locked = 28` **cannot be authored**.
Coder's walkthrough already concedes one of them — *"a difficulty tier
(hard = 20 writes locked = 20)"* — against a fixture that says 18.

It matters more than a rounding difference because **Coder's own comments
justify two of those numbers from the source data**: `notice = 12` is
*"low enough that an ordinary Awareness finds it on approach"*, and
`locked = 28` is *"the number 107 of K2's own doors carry"*. The two
values the fixture argues for from evidence are the two the tool cannot
express. Anyone authoring K2-faithful content hits this immediately.

**And Loom already does free DC entry elsewhere.** The conversation
editor's skill gate takes a typed number — I set `dc = 14`, which is not
a ladder value, and it wrote `gate = { skill = "Persuade", dc = 14 }`
without complaint. One app, two idioms for the same quantity.

*Suggestion, since the ladder is genuinely good for the common case:
leave the ladder and add a number field beside it, the way the
conversation editor already has one.*

---

### ⚠ D3 — the hazard dialog writes a value the row it belongs to cannot express, with nothing selected

In `PLACE HAZARD`, `what it takes to DEFUSE it` comes up with **hard 20**
highlighted. `what it takes to SEE it` comes up with **nothing
highlighted at all**.

I pressed `Place` deliberately without touching that row, to see whether
it would refuse. It placed, and wrote **`notice = 12`**.

12 is not on the ladder. So the row shows no selection, silently supplies
a number, and that number is one the row could never have produced. The
moment you click any tier you can never get back to it. A user who wants
the default has to know not to touch the control — and a user who touches
it and wants to undo has no way back.

*(This is how my file ended up matching Coder's `notice = 12` exactly. I
did not choose it; the dialog did, and only the file told me.)*

---

### ⚠ D4 — `kinds` has no control, so a mine cannot be given a damage type

Coder's mine carries `kinds = ["poison"]`. The `PLACE HAZARD` dialog
offers `over`, the two DCs, `damage over time | condition`, `amount`,
`rounds`, `save dc`, and `on save: half | none`. There is no damage-kind
control anywhere, and nothing in the dialog mentions the field.

Five of the hazard block's eight keys are authorable. `kinds` is the one
that is not, and it is the one that decides whether a resistance applies.

---

### ⚠ D5 — an item cannot be a key, so the keyed door's key must be a weapon, armour or a consumable

Coder's `or a key` line is *"a pick-list of the package's items, not
typed"* — correct, and it works. But to get an item into that list you go
through `NEW ITEM`, which **requires a base type**:

> `An item needs a base type — it is what carries the dice.`

`Create` stays dead until you pick one. I scrolled the whole list. It
runs weapons → armour (`Light · Medium · Heavy`) → `Medpac · Adrenal ·
Shield generator · Charge`, and **ends there**. There is no `key`, no
`keycard`, no plain or miscellaneous type.

The dialog's own principle is `where it lives IS what it is —
'items/weapons/blaster-rifle'`. I set the path to
`items/misc/sith-keycard` and the base-type list did not change: still
weapons-first, still required. So the path says one thing and the
mandatory field says another.

I took `Charge` as least-wrong and it wrote:

```toml
[item]
name = "Sith Keycard"
base = "charge"
```

A door key is now, mechanically, a power cell. This is the clearest case
in the session of the UI *requiring* something that does not make sense.

---

### ⚠ D6 — hazards are never drawn on the board

Everything else is: the footlocker and crate as `F`/`C`, the console as
`C`, both doors as a distinct door glyph, the guard as `G`, and the
arrival as a square **carrying its own name label**. The mine at
`(2,1)–(2,2)` is drawn **nowhere** — not after placing, not after
selecting it in the tree, and not after a clean restart and reload.

The only way to see where it is is to read `2, 1` beside it in the tree
or `at 2, 1` in the inspector. On a board where an arrival point earns a
text label, the one object that will kill a player is invisible.

**Related, and flagged by the owner during the run: a mine should occupy
a single square.** The tool pushes the other way — the palette hint is
*"drag a box over the squares it covers"*, the drag preview reads out
`1 × 2` as you size it, and nothing warns you when a mine ends up
covering more than one. Coder's own fixture is `over = [[2,1],[2,2]]`, so
this is a question about the intended model rather than a mis-built
control, but the UI currently makes a multi-square mine the natural
thing to produce.

---

### ⚠ D7 — a footlocker has a combat side and notices the player

Selecting any placeable — container, terminal or fixture — shows these
rows underneath the ones that belong to it:

```
noticed within   4 squares · 8 m   [10 squares · 20 m]   20 squares · 40 m
how far off this one notices the player — PT-1686

side   [enemy]   henchman   companion droid   companion beast
fights the player — the default, and what every placement was before PT-1735
```

So a crate is an `enemy` that `fights the player` and has an opinion
about how far off it notices you. Coder's three "not a bug" notes cover
the *kind* row; they do not cover these two, and they are creature
concepts on a non-creature placement.

---

## The two places Coder asked me to look hardest

### (a) Is the hazard drag gesture discoverable before you need it? — **Yes.**

Clicking `triggers` in the palette prints, *before* you arm anything:

> `drag a box over the squares it covers — a mine is one row with two
> DCs, what it takes to SEE it and what it takes to defuse it`

That is the instruction, in the right place, at the right time, and I
knew what to do without being told. The drag then confirms itself well —
a live rectangle with a `1 × 2` size readout. **This is the best-explained
tool in the app**, and it is the model the others should copy.

Three things blunt it:

1. **"a mine is one row"** sits four words from "drag a box over the
   squares". "Row" means a TOML table here, but on a grid where you are
   dragging across rows it reads as a grid row, and it contradicts the
   instruction it is attached to. *"one entry"* would fix it.
2. **`triggers` is the only palette kind with no subtitle.** `doors` has
   *"a doorway, painted"* and `waypoints` has *"an arrival point,
   painted"*; `triggers` has nothing. The good copy is one click deeper
   than the place a first-timer scans.
3. **Nothing shows the tool is armed.** `+ hazard` was already rendered
   teal before I clicked it and looked identical after. Same for
   `+ doorway`. I only learned the tool was live by trying the gesture.
   (`+ arrival point` and the placeables at least say *"— loaded to
   place"* in the status bar.)

### (b) Does the placeable dialog's "locked lives on the placement" explanation stand on its own? — **Half.**

`NEW PLACEABLE` says:

> `whether it is a container, a terminal or scenery — and what it is
> locked at — belongs to the placement, not here: place it, then select
> it on the board`

**As an instruction it is complete** — it tells you what you cannot do
here and exactly what to do instead, and I followed it without a stumble.

**As a reason it says nothing.** It asserts the state "belongs to the
placement" and never says why: that one blueprint can be dropped many
times and each copy needs its own lock. That one clause is the whole
justification and it is missing. A user who disagrees has nothing to
disagree with.

And it uses **`scenery`** for the kind that every other surface — the
kind row, the file, Coder's brief — calls **`fixture`**. Read the dialog,
then hunt the kind row for "scenery", and it isn't there.

---

## A pattern worth naming: one field, three vocabularies

Setting a terminal's conversation crosses three surfaces, and each names
the same thing differently:

| surface | what it calls it |
|---|---|
| the terminal placement's hint | *"it needs `shown = "terminal"` on it"* — the raw TOML key |
| the conversation editor's control | **`draws as  dialogue | terminal`** |
| the placement's own picker row | **`says  console`** |

A user who follows the hint literally searches for the word "shown" and
never finds it, because the control that sets it is labelled *draws as*.
The hint names the file; the UI names the control; neither mentions the
other.

---

## Smaller UI notes

- **`doors` and `waypoints` share a word-for-word identical helper**:
  *"painted onto a square and names no blueprint — §4a makes a
  connection's `from` optional and §4·0 makes an arrival a name and a
  coordinate."* One blurb, two tools, and it cites spec sections rather
  than saying what to do — the opposite register to the hazard hint that
  works so well.
- **Three different creation affordances.** Area and placeable open
  modals; `conversations +` opens an in-pane form — which greets you with
  **`There is no conversation here.` in the same red as a real package
  problem**, for a blank form you just asked for.
- **A creature's conversation is free-typed, write-once and
  unvalidated.** `NEW CREATURE` warns *"set it here or not at all —
  nothing else can change it later. The path need not exist yet."* So the
  "never typed by hand" rule holds for placements and is exactly reversed
  for blueprints, on the field where a typo is permanent.
- **The board rescales every time the inspector changes height**, so
  placing several objects in a row means re-aiming at a different grid
  each time.
- **Console and crate both draw as `C`** — the glyph is the first letter,
  so two placeables at `(6,1)` and `(8,1)` are indistinguishable.
- **The doorway dialog discovers a missing destination only after you
  have picked the square**, and offers no way to create the area from
  there: cancel, leave, make the area, come back, re-place.
- **Setting the entry area took the problem count from 2 to 20.** All 18
  new ones are *"a player who picks <class> starts holding an item at
  items/weapons/…, and this package carries nothing there"*, one per
  class. That check can only run once an entry exists, so the jump is
  correct — **naming it so nobody chases it.** It does mean a
  Loom-authored package cannot be made problem-free without hand-writing
  nine weapon blueprints.
- The hub strip says **Background**; that screen's own header still says
  **BACKSTORY** (PT-1848 renamed it). One surface was missed.

## What Loom refuses correctly, and should keep refusing

- A doorway to nowhere: with no second area, `leads to` reads *"no other
  area in this package"*, `landing on` reads *"pick an area first"*, and
  `Place` stays dead. It also will not place until an arrival is picked.
- `no items in this package yet — a key names one` and `no conversations
  in this package yet — a terminal with none is an empty screen` — both
  say what the empty state means, not just that it is empty.
- Standard placeables: *"base-rules ships rules/ and no blueprints/ at
  all, so there is no standard placeables — **absent rather than
  empty**"*.
- `a02-vault declares no connections, so a character who walks into it
  from another area can never leave.`

## Coder's three "not a bug" notes — all three confirmed as described

1. **The kind row varies by what you clicked.** The guard offers only
   `creature`, and says why: *"fights, talks and can be attacked — and a
   blueprint under characters/ can be nothing else."* Placeables offer
   the other three and never `creature`. Clear.
2. **Key and DC are mutually exclusive.** Verified both directions on
   `door.strongroom.06`: picking `hard 20` removed `key` and wrote
   `locked = 20`; picking the key removed `locked` and wrote `key =
   "sith-keycard"`. The file is right — **but the UI never says it
   happened.** The chip just stops being highlighted. The fact that this
   needed a pre-warning is the evidence that one line of feedback would
   retire the warning.
3. **`dialogue/<id>`** — confirmed; Loom wrote `conversation =
   "dialogue/console"`. I checked for the stale spelling and found none:
   **Coder's shipped `locked-and-trapped` already reads
   `dialogue/console`.** Nothing to clean up there.

## One thing that looks like a defect and is not

Clicking `fixture` on the crate writes **nothing** — the key stays
absent, so my crate has no `kind` where Coder's says `kind = "fixture"`.

I read the engine the binary compiles from before filing it, and it is
correct. `area_open.dart` says so explicitly: *"AN ABSENT `kind` MEANS
READ THE PATH, NOT CREATURE… Absence is not a claim and cannot contradict
one"*, and names `attack_seam_test` catching the version that got this
wrong. A `placeables/crate` with no `kind` is exactly a fixture.

The only residue is cosmetic: the row shows `fixture` highlighted whether
you chose it or not, so there is no way to tell a deliberate choice from
the default. Harmless here; worth knowing it is display-only.

---

## PART 2 — `7d18e28` re-verified live

**In my build:** `7d18e28` (*the rank reaches every roll, and the fixtures
stop lying — PT-1662*) is an ancestor of app HEAD `9c4f050`. It is an app
commit, not an engine one — worth saying, because I looked in Lodestar
first and it is not there.

**Mechanism, read in the engine the binary compiles from** (`3e7fad60`):
`play_screen.dart:811` is now
`int _rank(String skill) => widget.character?.skillRank(skill) ?? 0;`,
and `skillRank` folds case in both records —
`ledger.dart:328: skills[skillKey(skill)] ?? 0` and
`character_open.dart:127`, with
`aptitude.dart:52: String skillKey(String s) => s.trim().toLowerCase();`.
That is exactly the shape TEST 080 inferred from the symptom.

**Live, on one character, in Coder's `locked-and-trapped`.** Fresh
chargen — "Vash Roarke", Human **Smuggler**, INT 18, Taris/Upper City
(Security aptitude), Convict — with **Awareness 4, Demolitions 4,
Security 4, Slicing 4**, all bought on the skills screen. A real chargen
run, not a hand-built record, which is the fixture caveat Coder raised.

| path | TEST 080 | now |
|---|---|---|
| arrival notice | `14 against 12` (Awareness **4**) | `14 against 12` — unchanged ✓ |
| Search, footlocker | `Awareness **0**` | **`search — d20 5 + Awareness 4 = 9 · nothing left in it`** |
| Open Lock, footlocker | `Security **0**` | **`open lock — d20 8 + Security 4 = 12 vs 18 (hard) · it holds`** |
| Slice, console | `Slicing **0**` | **`slice — d20 16 + Slicing 4 = 20 vs 15 (moderate) · in`** |
| Disarm, mine | `Demolitions **0**` | **`disarm — d20 5 + Demolitions 4 = 9 vs 20 (hard) · it is still live`** |

**The tell Coder named holds: the arrival notice and the object verbs now
agree about the same skill on the same character.** All four skills, one
character, one visit. **TEST 080's finding is CLOSED.**

### And the passing Slice reached the terminal screen — which TEST 080 never could

That closes TEST 080's *"two options on a pass — unverified"*. The screen
is real and it opened. It also surfaced something nobody has seen before:

### ⚠ D8 — the terminal screen does not fit the window

It is drawn larger than the viewport and clipped on two sides. The title
renders as `STRONGROOM CONTROL — AWAITING` with the rest cut off past the
right edge, and **only the first of the two options is on screen**, itself
cut short: `1 [Slicing] Unseal the vault door. (2 spi…`. The second
option is entirely below the bottom edge.

It scales with the window and overflows the same way at both sizes I
tried — **1600 × 900 and 1920 × 1040** — so it is not a small-window
problem. Coder's brief says the screen *"should open with two options"*;
one of them cannot be seen at all.

*(Pressing `2` did nothing, which is the known "picking an option doesn't
do anything yet" — not a finding.)*

### ⚠ D9 — `Esc` with the terminal open leaves the whole game

Pressing `Esc` on the terminal screen did not close the terminal; it
exited to the package's main menu (and auto-saved — `4 saves`). The
legend `esc to leave` belongs to the area beneath. Whatever the terminal's
own dismiss control is, it is off-screen with everything else, so `Esc`
is the only thing a player can find — and it costs them the room.

### One more, unchased

After resuming, the footer reads **`Vash Roarke · 1 rule about this
character not checked`**. New to me and not part of this ask; naming it
rather than digging.

---

## What I did not do

- **Did not read Coder's diff or Coder's fixture** until the authoring
  was finished — the comparison table above was built afterwards, which
  is the point of the exercise.
- **Did not author terrain, encounters, sounds, stores or doctrines** —
  outside the strongroom's six objects.
- **Did not play `tester-strongroom`.** It needs nine class weapon
  blueprints before a new game is clean, and Part 2 needed Coder's
  package anyway.
- **Did not reach the vault (`a02-vault`)**, either door, or the guard in
  play.

## State

- **New package `tester-strongroom`** created by me at
  `~/.local/share/kotor-rpg/packages/tester-strongroom` — two areas, three
  placeable blueprints, one item, one creature, one conversation. Mine,
  not cleaned up. **Coder's `locked-and-trapped` was only walked, never
  edited.**
- Saves: four in `locked-and-trapped` from this run (one auto-save on
  leaving), not cleaned up.
- Loom `19495`, Loom `23462`, app `27267` — all killed by PID, all
  confirmed gone.
- **Coder's seven uncommitted `BUILD/screens/*.png` were present at
  session start and left exactly as found.**
