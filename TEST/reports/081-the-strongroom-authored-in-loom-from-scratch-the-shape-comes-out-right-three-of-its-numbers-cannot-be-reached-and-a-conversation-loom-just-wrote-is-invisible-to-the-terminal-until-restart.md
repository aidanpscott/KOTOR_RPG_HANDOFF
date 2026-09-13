# TEST 081 — the strongroom authored in Loom from scratch, without reading
# Coder's diff: the shape comes out right and every object verifies. But
# Loom implements as a CONSTRAINT what `AREA-FORMAT-01` explicitly ruled a
# RECOMMENDATION, so the two lock DCs `BUILD 180` measured as carrying
# almost the whole game cannot be authored; a conversation Loom has just
# written is invisible to the terminal until restart; and `[entry].at` —
# ruled in this same slice — cannot be written at all.
# Separately: `7d18e28` re-verified live on all four skills, and the
# no-retry rule turns out to hold on a door and not on a terminal.

**⚠ THIS REPORT WAS CHECKED AGAINST THE DOCUMENTS BEFORE IT WAS SENT, AND
THAT CHANGED IT.** Four claims in the first draft were wrong or
over-reached and are corrected below; two new defects came out of the
check. What is corrected is named as corrected rather than quietly fixed,
because a withdrawn finding that vanishes is one nobody can check.

---

## Build state — three artefacts, and a fourth thing worth saying

**SYNC — done first, and confirmed.** `cd Loom && git pull` → *Already up
to date*; local `Loom` HEAD **`270cdde`** (*Loom authors all six fields,
and stops destroying two of them — PT-1957*), 02:58:03. `flutter pub
upgrade lodestar` → *No dependencies changed* (needs `source env.sh`
first; the toolchain is under `~/spike` and not on PATH). **`pubspec.lock`
resolved-ref reads `8ef6c775b838a2863f82027005de8f29a6e537d2` ✓**, the
pub-cache checkout exists, and the engine there reads the new fields.

**⚠⚠ AND LOOM MOVED UNDER ME MID-RUN — declared, because it bounds
everything in Part 1.** My Loom screenshots run 07:07:37 → 07:21:22. In
that window and just after, three commits landed:

    1bffe2d  07:19:06   the doorway dialog asks whether it leads anywhere
    21a13c5  07:20:55   the strongroom, re-authored through Loom
    c07331d  07:38:44   an authored NPC rolls something — the last excuse

**Everything in Part 1 is against `270cdde`** — my second Loom build ran
at 07:15:01, before the first of them. `1bffe2d` touches the doorway
dialog, which I exercised, so **anything I say about that dialog may
already be answered.** `21a13c5` is Coder's own half of the ruled diff,
authored concurrently with mine — neither of us saw the other's.

**Coder also has uncommitted work in Loom right now**: `M
lib/conversation/conversation_writer.dart` and a new
`test/the_renderers_blind_spot_test.dart`. I read the test header and
**left both exactly as found.** It is about full-rewrite writers deleting
fields they do not know — a different problem from anything below, but it
shares a file with D1's area.

**The app, for Part 2:** `run-app.sh`. HEAD `9c4f050`, clean; `lodestar`
pinned `3e7fad608d284afe473e034dc3e32f025cf5d017`, checkout present. **The
two apps are on different engine pins** — `8ef6c77` for Loom, `3e7fad60`
for the app — which is normal; do not reconcile them.

`check_shelf.py`: `✓ 25 rules files, all identical to what the extracts
generate`. Loom `19495`/`23462` and app `27267`/`31944` all killed by PID,
all confirmed gone.

**I authored into my own new package `tester-strongroom`**, not into
Coder's shipped `locked-and-trapped`, to avoid clobbering shared state the
app loads. Everything in Part 1 was reached through Loom's UI only; I did
not open Coder's file until the comparison at the end.

---

# PART 1 — authoring it

**It works.** Package → area (12 × 6) → mine → footlocker → console →
crate → vault door → keyed door → guard → arrival, all through the
palette, all written correctly, and Loom's own Verify reports **nothing
wrong with any of the six objects.**

| | Coder's | mine | why |
|---|---|---|---|
| `notice` | 12 | 12 | written by *default*, never chosen — D3 |
| footlocker `locked` | **18** | 20 | **18 is not on the ladder** |
| vault `locked` | **28** | 30 | **28 is not on the ladder** |
| `kinds` | `["poison"]` | *absent* | no control — see the note under D2 |
| crate `kind` | `"fixture"` | *absent* | benign, verified — see below |
| `[entry].at` | `"back"` | *absent* | **Loom cannot write it** — D8 |

---

### ⚠ D1 — a conversation Loom has just written is invisible to the terminal that needs it, until you restart

Coder's step is *"terminal, a tier, then pick a conversation from a list —
never typed."* I did that. `conversations` **+** → wizard → `Write`. The
status bar said **`wrote …/dialogue/console.toml`** and the file was on
disk. The console placement still read **`no conversations in this package
yet`**, and the `conversations` tree node also refused to expand — so the
whole module model had not rescanned, not just that one pick-list.

**I restarted Loom to tell a refresh bug from a path mismatch.** After the
restart everything is correct: the conversation appears, the row reads
`says  console`, one click writes `conversation = "dialogue/console"`. The
writer and the paths are right; the open module never learns.

**Why it is a defect and not a design choice:** the *item* pick-list on
the same selection bar refreshes immediately. I created
`items/misc/sith-keycard` while a door was already selected and `or a key
sith-keycard` appeared on it without a re-click. **Two lists, one panel,
one refreshes and one does not.**

---

### ⚠⚠ D2 — Loom implements as a constraint what the format explicitly ruled a recommendation

**This is the one the documents changed.** My first draft filed the fixed
tier ladder as a design limitation worth softening. It is not a
limitation; it is a **divergence from a ruling**, and the ruling is
explicit.

`AREA-FORMAT-01 §3b` — **byte-identical in both `HANDOFF/docs/` and
`MAIN_WORK/design/`, checked because this claim rests on it**:

> **⚠ And a number off the ladder is still a number.** `§2` names ±2, ±5
> and ±10 as its modifiers, so the ladder **recommends rather than
> constrains** — the dropdown is the recommended values, not the permitted
> ones.

Loom's lock rows and both hazard DC rows offer only `trivial 5 · easy 10 ·
moderate 15 · hard 20 · formidable 25 · heroic 30 · legendary 35`, with
**no free entry anywhere on them.** The recommended values are the only
permitted ones. That is the sentence above, inverted.

**And off-ladder DCs are not an edge case — the rules require them.**
`SKILL-RESOLUTION-01 §2` gives ±2/±5/±10 as the standing modifier set, and
**§2.1 says Demolitions *"Disabling adds +2. Recovering adds +5"*** — so a
routine disarm is 22 and a routine recovery 25. One of those is on the
ladder and one is not.

**⚠ CORRECTION TO MY FIRST DRAFT.** I wrote that Coder's comments justify
`notice = 12` and `locked = 28` from the source data. **That was wrong
about 12.** The two numbers `BUILD 180` actually measured are:

> **⚠ `DC 28` is the lock**, 24 of K2's 26 pickable doors. Placeables
> cluster at **18**. Two numbers carry almost the whole game.

So the two source-backed values are **18 and 28 — and both are off the
ladder, so neither can be authored.** `notice = 12` is a fixture-teaching
number, not a corpus one; the engine's own comment says detect *"runs 10,
15 and 20"*, all of which the ladder does offer.

That correction makes the finding sharper, not weaker: **the two numbers
the measurement says carry almost the whole game are exactly the two the
tool cannot express.**

**And Loom already does free DC entry.** The conversation editor's skill
gate took a typed `dc = 14` — not a ladder value — and wrote
`gate = { skill = "Persuade", dc = 14 }` without complaint. One app, two
idioms for one quantity, and the placement side is the one that disagrees
with the format.

*Suggestion, since the ladder is right for the common case: keep it and
add a number field beside it, exactly as the conversation editor already
has.*

**⚠ A NOTE ON `kinds`, DOWNGRADED FROM MY FIRST DRAFT.** I filed the
missing `kinds` control as a missing capability against a spec. **There is
no spec.** The engine reads only `tag`, `over`, `disarm` and `notice` as
named hazard fields; everything else goes into an untyped pass-through —
`area_open.dart:1313`, *"EVERYTHING THIS FUNCTION DOES NOT ITSELF READ,
kept rather than dropped."* So `does`/`amount`/`rounds`/`save` having
controls and `kinds` not having one is a scope choice in an open-ended
bag, not a violation. It stays on the list only because the ruled test is
a diff against the hand-written fixture, and this is one of the diffs.

---

### ⚠ D3 — the hazard dialog writes a value with nothing selected, in a row that cannot express it

`PLACE HAZARD` opens with `what it takes to DEFUSE it` on **hard 20** and
`what it takes to SEE it` with **nothing highlighted.** I pressed `Place`
deliberately without touching that row, to see whether it would refuse.

It placed, and wrote **`notice = 12`** — which, per D2, that row could
never have produced. The row shows no selection, silently supplies a
number, and the moment you click any tier you can never get back to it.

*(This is how my file matched Coder's `notice = 12` exactly. I did not
choose it; the dialog did, and only the file told me.)*

---

### ⚠ D4 — an item cannot be a key, so the keyed door's key must be a weapon, armour or a consumable

The `or a key` pick-list works. Getting an item into it goes through `NEW
ITEM`, which **requires a base type**:

> `An item needs a base type — it is what carries the dice.`

`Create` stays dead until you pick one. I scrolled the whole list: weapons
→ armour (`Light · Medium · Heavy`) → `Medpac · Adrenal · Shield generator
· Charge`, and it **ends**. No key, no keycard, no plain type. Setting the
path to `items/misc/sith-keycard` did not change the list.

I took `Charge`, and the strongroom's door key is now mechanically a power
cell.

**And the requirement is quoting a rule that excludes this case.**
`PT-1452` requires a base type *because the base type carries the dice* —
and `BUILD 180 §3c` applies that same rule the other way for placeables:
***"THREE KINDS AND NOT A `base` INTO `equipment.toml` … a footlocker has
no dice."*** PT-1941 approved that reasoning explicitly. A keycard has no
dice either. The rule that forces a base type here is the rule that says
this thing should not need one.

---

### ⚠ D5 — hazards are never drawn on the board

Everything else draws: footlocker and crate as `F`/`C`, console as `C`,
both doors as a door glyph, the guard as `G`, and the arrival as a square
**carrying its own name label**. The mine at `(2,1)–(2,2)` is drawn
**nowhere** — not after placing, not after selecting it in the tree, and
not after a clean restart and reload. The only way to see where it is is
to read `2, 1` in the tree or inspector.

On a board where an arrival point earns a text label, the one object that
will kill a player is invisible.

**⚠ And flagged by the owner during the run: a mine should occupy a single
square.** The tool pushes the other way — the palette hint says *"drag a
box over the squares it covers"*, the drag preview reads out `1 × 2`, and
nothing warns when a mine ends up covering more than one. The format is
genuinely a region (`over` is a list, and `BUILD 180` argues that at
length against forcing a trap onto a per-square model), so this is a
question about the intended *content* rather than a mis-built control —
but the UI currently makes a multi-square mine the natural thing to
produce, and the owner's expectation is the opposite.

---

### ⚠ D6 — a footlocker has a combat side, and a not-hidden placement is offered a hidden-only field

Every placeable inspector — container, terminal, fixture — carries:

```
noticed within   4 squares · 8 m   [10 squares · 20 m]   20 squares · 40 m
side   [enemy]   henchman   companion droid   companion beast
       fights the player — the default
```

So a crate is an `enemy` that `fights the player`. Coder's three "not a
bug" notes cover the *kind* row; they do not cover these.

**And `noticed within` is `range`, which the format rules is hidden-only.**
`AREA-FORMAT-01 §3c`: *"a `range` follows `stealth`'s rules: **hidden
only**, a whole number, and above zero."* The row is shown ungated, on
placements with `hidden` off.

**⚠ It is display-only until touched, which I checked rather than
assumed:** my written file carries no `range` and no `hidden` on any
placement, so the highlighted default is a display, not a write. That
keeps it out of load-failure territory — `§3b` makes a `stealth` without
`hidden` a load failure — but it is still a hidden-only control offered on
things that are not hidden.

---

### ⚠⚠ D7 — Loom cannot author `[entry].at`, a field ruled in this very slice

**New, out of the document check, and the sharpest of the authoring
findings.**

`PT-1957` ruled the `(0,0)` start bug I filed in TEST 080:

> RULED ON THE (0,0) START BUG: OPTION A, EXTEND THE ARRIVAL GRAMMAR.
> `[entry]` gains an `at` field naming its arrival explicitly.

Coder's package carries it, with a comment naming exactly what it prevents:

```toml
# ⚠⚠ WHERE A NEW GAME BEGINS — `PT-1957`. Naming the area was not enough:
# without `at` the runtime falls to its first standable square, which is a
# scan from the corner, and this package started the player on (0,0) while
# declaring an arrival on (1,1).
[entry]
area = "a01-strongroom"
at   = "back"
```

**My Loom-authored package has no `at`.** `set as entry` wrote only the
area. Confirmed at source rather than inferred —
`Loom/lib/create/manifest_writer.dart:40`:

```dart
return '$manifest$sep\n[entry]\narea = "$areaId"\n';
```

There is no `at` anywhere near `[entry]` in Loom.

**So a package authored entirely through Loom reproduces the (0,0) start
bug that `PT-1957` just fixed** — and it is the shape `AREA-FORMAT-01`
quotes at `PT-1440`: ***"anything the Builder cannot write, the Builder
eventually destroys."*** The ruling that fixed the bug and the ruling that
Loom must author the fields landed in the same slice; this field fell
between them.

---

## The two places Coder asked me to look hardest

### (a) Is the hazard drag gesture discoverable before you need it? — **Yes.**

Clicking `triggers` prints, *before* you arm anything:

> `drag a box over the squares it covers — a mine is one row with two DCs,
> what it takes to SEE it and what it takes to defuse it`

The instruction, in the right place, at the right time. I knew what to do
without being told, and the live rectangle with its `1 × 2` readout
confirms itself well. **This is the best-explained tool in the app** and
the model the others should copy. Three things blunt it:

1. **"a mine is one row"** sits four words from "drag a box over the
   squares". "Row" means a TOML table; on a grid you are dragging across
   rows it reads as a grid row, contradicting the instruction it is
   attached to. *"one entry"* would fix it.
2. **`triggers` is the only palette kind with no subtitle** — `doors` has
   *"a doorway, painted"*, `waypoints` *"an arrival point, painted"*. The
   good copy is one click deeper than a first-timer scans.
3. **Nothing shows the tool is armed.** `+ hazard` looked identical before
   and after I clicked it; same for `+ doorway`. I learned the tool was
   live by trying the gesture.

### (b) Does the placeable dialog's "locked lives on the placement" explanation stand on its own? — **Half — and the missing half is already written.**

> `whether it is a container, a terminal or scenery — and what it is locked
> at — belongs to the placement, not here: place it, then select it on the
> board`

**The claim is exactly the ruled shape**, which I checked rather than
assumed — `PT-1941`: ***"APPROVED: STATE LIVES ON THE PLACEMENT, NOT THE
BLUEPRINT."*** So the dialog is right and should keep saying it.

**As an instruction it is complete** — it names what you cannot do here and
exactly what to do instead, and I followed it without a stumble.

**As a reason it says nothing**, and the reason is one clause long and
already exists in the ruling that approved it:

> a blueprint is a template … **when the values are the instance, they
> belong on the instance.**

Adding that clause would turn an assertion a user can only accept into one
they can understand.

And it uses **`scenery`** for the kind that the kind row, the file and
Coder's brief all call **`fixture`**. Read the dialog, then hunt the kind
row for "scenery", and it is not there.

---

## A pattern worth naming: one field, three vocabularies

| surface | what it calls it |
|---|---|
| the terminal placement's hint | *"it needs `shown = "terminal"` on it"* — the raw TOML key |
| the conversation editor's control | **`draws as  dialogue \| terminal`** |
| the placement's picker row | **`says  console`** |

Follow the hint literally and you search for "shown" and never find it,
because the control that sets it is labelled *draws as*.

## Smaller notes

- **`doors` and `waypoints` share a word-for-word identical helper** that
  cites spec sections rather than saying what to do — the opposite
  register to the hazard hint that works so well.
- **Three different creation affordances**: area and placeable open
  modals; `conversations +` opens an in-pane form that greets you with
  **`There is no conversation here.` in problem-red**, for a blank form you
  just asked for.
- **A creature's conversation is free-typed, write-once and unvalidated** —
  *"set it here or not at all — nothing else can change it later"* — which
  reverses the "never typed" rule on the field where a typo is permanent.
- **The board rescales whenever the inspector changes height**, so placing
  several objects means re-aiming each time.
- **Console and crate both draw as `C`** (first letter), so two placeables
  are indistinguishable on the board.
- **Setting the entry area took problems from 2 to 20.** All 18 are
  per-class starting weapons; that check can only run once an entry
  exists, so the jump is correct — **named so nobody chases it.** It does
  mean a Loom-authored package cannot be made problem-free without
  hand-writing nine weapon blueprints.
- The hub strip says **Background**; that screen's header still says
  **BACKSTORY**.
- *Aside, not chased:* the two `AREA-FORMAT-01` copies differ in size
  (41,643 vs 46,016 bytes) though the line I cite is byte-identical in
  both. `check_shelf.py` covers `rules/`, not `design/`.

## What Loom refuses correctly

- `no items in this package yet — a key names one` and `no conversations
  in this package yet — a terminal with none is an empty screen` — both
  say what the empty state *means*.
- Standard placeables: *"base-rules ships rules/ and no blueprints/ at
  all, so there is no standard placeables — **absent rather than
  empty**"*.
- `a02-vault declares no connections, so a character who walks into it
  from another area can never leave.`

**⚠ CORRECTION TO MY FIRST DRAFT — the doorway dialog.** I filed it as
friction that *"discovers a missing destination only after you have picked
the square"*. That reads the dialog wrongly. Its **first option, selected
by default, is `stays in this area`**, which needs no destination and
places immediately — and that is `PT-1959`'s ruled same-area door:
*"RULED ON PART B, SAME-AREA DOORS: SUPPORTED, `to` AND `lands` BECOME
OPTIONAL."* `Place` is live in that state. It only greys if you choose
*leads to another area* and there is no other area — which is a correct
refusal, not friction. **The default path needs nothing.** Withdrawn.

## Coder's three "not a bug" notes — all three confirmed

1. **The kind row varies by what you clicked.** The guard offers only
   `creature` and says why. Clear.
2. **Key and DC are mutually exclusive.** Verified both directions: a tier
   removed `key` and wrote `locked = 20`; the key removed `locked`. The
   file is right — **but the UI never says it happened**, the chip just
   stops being highlighted. That this needed a pre-warning is the evidence
   that one line of feedback would retire the warning.
3. **`dialogue/<id>`** — confirmed. I checked for the stale spelling:
   Coder's shipped package already reads `dialogue/console`, per
   `PT-1959`'s ruling that package-relative `dialogue/` was always the
   rule. Nothing to clean up.

## One thing that looks like a defect and is not

Clicking `fixture` on the crate writes **nothing**, so my crate has no
`kind` where Coder's says `kind = "fixture"`. I read the engine the binary
compiles from before filing it: *"AN ABSENT `kind` MEANS READ THE PATH,
NOT CREATURE … Absence is not a claim and cannot contradict one"*, and it
names `attack_seam_test` catching the version that got this wrong. A
`placeables/crate` with no `kind` **is** a fixture. Correct.

Residue is cosmetic: the row shows `fixture` highlighted whether you chose
it or not, so a deliberate choice and the default look identical.

---

# PART 2 — `7d18e28` re-verified, and a new defect beside it

**In my build:** `7d18e28` (*the rank reaches every roll, and the fixtures
stop lying — PT-1662*) is an **app** commit, not an engine one, and is an
ancestor of HEAD `9c4f050`.

**Mechanism, read in the engine the binary compiles from** (`3e7fad60`):
`play_screen.dart:811` is now `_rank(skill) =>
widget.character?.skillRank(skill) ?? 0`, and `skillRank` folds case in
both records — `ledger.dart:328` and `character_open.dart:127`, via
`aptitude.dart:52: skillKey(s) => s.trim().toLowerCase()`.

**Live**, fresh chargen Smuggler "Vash Roarke", INT 18, Taris/Upper City
(Security aptitude), Convict, with **Awareness 4, Demolitions 4, Security
4, Slicing 4** — a real chargen run, not a hand-built record, which is the
fixture caveat Coder raised:

| path | TEST 080 | now |
|---|---|---|
| arrival notice | `14 against 12` (Awareness **4**) | `14 against 12` — unchanged ✓ |
| Search, footlocker | `Awareness **0**` | **`d20 5 + Awareness 4 = 9`** |
| Open Lock, footlocker | `Security **0**` | **`d20 8 + Security 4 = 12 vs 18 (hard)`** |
| Slice, console | `Slicing **0**` | **`d20 16 + Slicing 4 = 20 vs 15 (moderate) · in`** |
| Disarm, mine | `Demolitions **0**` | **`d20 5 + Demolitions 4 = 9 vs 20 (hard)`** |

**The tell Coder named holds: the arrival notice and the object verbs now
agree about the same skill on the same character.** Slicing read 4 on
five separate rolls across two sessions. **TEST 080's finding is CLOSED.**

### ✓ And TEST 080's other observation is closed too

I filed the `(0,0)` start as *"named rather than called a defect"*. It was
ruled at `PT-1957` and is fixed: the player now starts **on `back` at
(1,1)**, because Coder's package carries `[entry] at = "back"`. That is
also what makes **D7** above matter — Loom cannot write the field that
fixed it.

### ⚠⚠ NEW — the no-retry rule holds on a door and not on a terminal

TEST 080 confirmed *"a failed lock, slice, or disarm attempt cannot be
retried"*. **That confirmation was scoped to the door**, and it does not
generalise.

In one visit, at the console, without leaving the square:

    slice — d20 5  + Slicing 4 = 9  vs 15 (moderate) · it holds
    slice — d20 8  + Slicing 4 = 12 vs 15 (moderate) · it holds
    slice — d20 16 + Slicing 4 = 20 vs 15 (moderate) · in

**Three rolls, no refusal**, the menu re-offering `Slice (Slicing)`
un-greyed after each failure.

**The control, minutes later in the same build and the same room:** two
`Open Lock` attempts on the vault door gave
**`door.strongroom.05 — you have already tried this lock`** on the second.
So the rule is live and the terminal is the exception.

**And the terminal keeps no state in the other direction either.** I
sliced it successfully, left the area, `Continue`d back, and was offered
the roll again — the success did not persist any more than the failure
did. The door records both halves (`df1ea93`, *a picked lock survives the
visit*); the terminal records neither.

This is the shape `PT-1955` named as *"the twelfth named instance of a
rule applied to one path and not the next"*, and `TEST 078` named about
click-to-move before that.

### ⚠⚠ NEW — the terminal panel does not fit the window, at any size including the one it was measured at

The passing Slice reached the terminal screen, which TEST 080 never could
— closing that report's *"two options on a pass — unverified"*. It is
real and it opens. It also does not fit.

The title renders as `STRONGROOM CONTROL — AWAITING` with the rest past
the right edge, and **only the first of the two options is on screen**,
itself cut short at `1 [Slicing] Unseal the vault door. (2 spi…`. The
second option is entirely below the bottom edge.

**Reproduced at three sizes — 1280 × 720, 1600 × 900 and 1920 × 1040 —
with the same proportional overflow.** ⚠ **1280 × 720 matters
specifically**: it is the app's own default window size *and* the size
`PT-1696` measured the panel at. My first draft tested only the two larger
sizes; the default was the gap, and testing it made the finding stronger
rather than weaker.

**Why nothing caught it.** `check_terminal_panel.py` passes — I ran it:
*"8 lifted value(s) checked · 0 disagreeing."* It passes correctly. Its
own docstring says **`⚠ GEOMETRY ONLY`**, and it compares each of the
app's constants against the rectangle `computer.gui` declares. **The
viewport is not in the comparison at all**, so "every rectangle matches
the source" and "the panel is larger than the window" are both true at
once. The check is not broken; it was never aimed at this.

Nor was `PT-1696`'s measurement: *"the real box read off a running screen
at 1280x720 fits nine and overflows a tenth by 19px"* is about **rows
inside the replies box**, in the panel's own design space — not the panel
against the window.

**⚠ And `BUILD 181 §4` predicted this failure in advance**, naming it as
*"the one real constraint, named rather than discovered later"* — that a
terminal row is one line and *"it is truncated or it overflows the row"* —
and put **A** (validate refuses an over-width reply) against **B** (wrap
to two rows) to the owner, recommending A. **A was ruled** at `PT-1696`:
refuse-at-authoring-time, ceiling of nine replies. What I hit is the
larger case that neither the ruling nor the check covers: **the whole
panel, not one row.**

*A mechanism I could not confirm and am flagging rather than asserting:*
`TerminalPanel` draws a 640 × 480 design multiplied by the app-wide `s`,
and `s` comes from `scaleFor`, which is derived from a **340 × 255** grid
and clamped `[1.6, 4.2]` — two different design bases multiplied together.
The arithmetic predicts an overflow at every size, which matches what I
saw; it does **not** reconcile with where the frame's left edge actually
lands, so I have not verified the composition and Coder should not treat
this paragraph as a diagnosis.

### ⚠ CORRECTION — `Esc` on the terminal, withdrawn as filed

My first draft said `Esc` leaves the whole game and that *"whatever the
terminal's own dismiss control is, it is off-screen, so `Esc` is the only
thing a player can find."* **The second half is wrong.** The ruled
dismissal is a tap — `play_screen.dart:3373`, *"⚠ A TAP ANYWHERE CLOSES
IT. The panel has no footer of its own — `§4` lifted a geometry, not a
control set"* — and **I tested it: a tap closes the panel cleanly and
returns to the room.**

What stands is only the discoverability half: `Esc` **does** exit to the
package menu (auto-saving on the way), and `esc to leave` is the only
dismissal signposted anywhere on screen, in the legend visible beneath the
panel. A player who reads the legend loses the room. Much smaller than
what I first filed.

### One more, unchased

After resuming, the footer reads **`Vash Roarke · 1 rule about this
character not checked`**. New to me, not part of this ask, named rather
than dug into.

---

## What I did not do

- **Did not read Coder's diff or fixture** until the authoring was
  finished — the comparison table was built afterwards, which is the point
  of the exercise.
- **Did not re-test Part 1 against `1bffe2d`/`21a13c5`/`c07331d`**, which
  landed during and after the run.
- **Did not author** terrain, encounters, sounds, stores or doctrines.
- **Did not play `tester-strongroom`** — it needs nine class weapon
  blueprints first, and Part 2 needed Coder's package anyway.
- **Did not reach** `a02-vault`, either door, or the guard in play.

## State

- **New package `tester-strongroom`** is mine, not cleaned up — two areas,
  three placeable blueprints, one item, one creature, one conversation.
  **Coder's `locked-and-trapped` was only walked, never edited.**
- Saves: four in `locked-and-trapped`, not cleaned up.
- All four app/Loom PIDs killed by PID, confirmed gone.
- **Coder's seven uncommitted `BUILD/screens/*.png`, and its uncommitted
  Loom work, left exactly as found.**
