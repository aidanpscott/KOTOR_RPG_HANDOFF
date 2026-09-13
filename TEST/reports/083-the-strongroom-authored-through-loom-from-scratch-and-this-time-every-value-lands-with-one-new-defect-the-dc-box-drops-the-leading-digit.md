# TEST 083 — the strongroom authored through Loom from scratch, a second
# time and a fresh package: EVERY VALUE IN CODER'S FIXTURE NOW LANDS,
# including the three TEST 081 could not reach. Seven of that report's
# findings are closed. One new defect, and it sits on the control that
# closed the biggest of them: the free-entry DC box intermittently drops
# the leading digit and silently writes a different, legal number.

## Build state — and no drift this time

    Loom            HEAD f69b278  the pick-list carries one name per damage kind
    KOTOR-RPG-APP   HEAD 69acddf  a set mine detonates, and what you do to one
                                  survives the reload
    lodestar        89ba2e15 — ⚠ RECORDED AND RESOLVED AGREE, in both repos
    lens            (unchanged)

Both working trees clean. **This is the first session in three where the
resolved engine matched the recorded pin**, so nothing below is qualified
by `ref: main` drift.

`check_shelf.py`: `✓ 25 rules files, all identical to what the extracts
generate`. Loom PID `134557` killed by PID, confirmed gone.

**I authored a brand-new package, `strongroom-rebuilt`** — not TEST 081's
`tester-strongroom`, and not Coder's `locked-and-trapped`. Nothing was
reused: new area, new blueprints, new conversation, new item, new
creature. I did not open Coder's file until the comparison at the end.

---

# THE DELIVERABLE — it succeeds completely this time

Every field and **every number** in Coder's hand-written fixture is now
reachable through the UI. The two files agree on all of it:

| | Coder's | mine |
|---|---|---|
| mine `over` / `disarm` / `notice` | `[[2,1],[2,2]]` / 20 / 12 | same |
| mine `does` / `amount` / `rounds` / `save` | dot / 6 / 3 / `{15, half}` | same |
| mine **`kinds`** | `["poison"]` | **`["poison"]`** ✓ |
| footlocker `kind` / **`locked`** | container / **18** | **container / 18** ✓ |
| console `kind` / `locked` / `conversation` | terminal / 15 / `dialogue/console` | same ✓ |
| crate | `kind = "fixture"` | *absent* — see below |
| vault door `locked` | **28** | **28** ✓ |
| keyed door `key` | `sith-keycard` | same ✓ |
| `[entry].at` | `"back"` | **`"back"`** ✓ |

The only real difference is the crate's `kind`: clicking `fixture` still
writes nothing, so mine omits the key. **Verified benign in TEST 081 and
still true** — `area_open.dart` is explicit that an absent `kind` means
read the path, and `placeables/crate` is a fixture by path. The rest are
whitespace alignment, block order, and my own guard blueprint being
`guard-droid` rather than Coder's `probe-droid`.

Loom's own **Verify reports nothing wrong with any of the six objects.**
The 19 problems it does report are `a02-vault` having no way out — which
is true of Coder's fixture too — and the eighteen per-class starting
weapons this package does not carry.

---

## Seven TEST 081 findings closed, checked one at a time

| | then | now |
|---|---|---|
| **D1** conversation invisible until restart | needed a restart | **`says console` appears immediately**, and the tree node fills in the same moment |
| **D2** ladder-only DCs | 18 and 28 unreachable | **free number box beside every ladder**, labelled *"the ladder recommends; it does not constrain — §3b"* |
| **D3** `notice = 12` written by an unselected row | invisible | **the box shows `12`** and is editable |
| **D4a** no `kinds` control | absent | **11-name pick-list**, and `poison` writes |
| **D4b** an item cannot be a key | forced to be a weapon or a `charge` | **`Object` base type** — the keycard is `base = "object"` |
| **D5** hazards never drawn | invisible | **drawn at both squares** in Loom |
| **D7** `[entry].at` unwritable | Loom emitted `area` only | **`starts at` in package properties**, and when unset it warns *"the game begins at the first square it can stand on — usually the top-left corner"* |

Two more, from the not-a-bug list rather than the defect list:

- **The lock/key exclusion now says which half won.** Setting a DC reads
  *"locked at 18 — Security only, and any key is cleared"*; setting a key
  reads *"it takes the sith-keycard — no Security check, and any DC is
  cleared"*. TEST 081's complaint was that the clear was silent and needed
  a pre-warning. It no longer is.
- **`noticed within` is kind-aware.** On a placeable it now says *"nothing
  reads this on a fixture — only a creature notices, and only a HIDDEN
  thing is noticed"*; on the guard it says *"how far off this one notices
  the player"*. That is half of D6 answered.

**The damage-kind list is 11 names, not the 13 raw values I measured in
TEST 082** — `electric`/`electrical` and `fire`/`heat` have been collapsed
to one name each, which is the near-duplicate question that function's own
docstring raised, decided rather than passed through. Worth knowing that
the count differing from my report is deliberate.

---

## ⚠⚠ THE NEW DEFECT — the DC box drops the leading digit

The free number box is the control that closes D2. It intermittently
**keeps only the last digit typed**, writing a different, entirely legal
DC with no error.

I hit it authoring the console: I typed `15` and the file said
**`locked = 5`**. Probed properly, clearing the box each time:

| typed | result |
|---|---|
| `1` `2` | **12** ✓ |
| `1` `8` | **8** ✗ — and 6 times out of 6, at both 60 ms and 900 ms between keys |
| `1` `5` | **15**, **5**, **15** — *flaky, 2 of 3* |
| `2` `5` | **25** ✓ |
| `3` `0` | **30** ✓ |
| `2` `8` | **8** first attempt, **28** on the second |

So it is neither purely timing nor purely value — `18` failed every time
while `15` mostly worked and `28` worked on a retry. **I could not pin the
rule down and am not asserting one**; the shape is a field rebuilt from the
committed value between keystrokes, with the caret reset so the next digit
overwrites, but I did not confirm that and Coder should not treat this
paragraph as a diagnosis.

**What makes it matter rather than merely annoy:**

- It is silent. There is no refusal, and `8` is a perfectly good DC.
- It writes a number the author did not choose — the *"working-but-wrong
  default"* shape the hazard dialog's own gating was built to stop.
- It lands on the one control that exists to reach the off-ladder numbers,
  and **18 — one of the two values `BUILD 180` measured as carrying almost
  the whole game — is the case that failed every single time.**

**Mitigations, checked rather than assumed:** the box and the file always
agreed, so nothing lies to you — the wrong number is on screen if you look.
And the ladder chips are reliable; I set the console's 15 with the
`moderate 15` chip after the box refused, and 28 went in on a retry. So
every value is reachable, just not dependably by typing.

---

## Still open from TEST 081 — unchanged, re-checked

- **The `NEW PLACEABLE` dialog is word-for-word as it was.** It still says
  *"a container, a terminal or **scenery**"* where the kind row, the file
  and the brief all say **`fixture`**, and it still gives the instruction
  (*"place it, then select it on the board"*) without the reason. As in
  TEST 081, the missing clause is one line and already exists in the
  ruling that approved the design — `PT-1941`: *"a blueprint is a
  template… when the values are the instance, they belong on the
  instance."*
- **`side  enemy · henchman · companion droid · companion beast` with
  *"fights the player"* is still on every placeable.** The crate is an
  enemy. This is the half of D6 that was not addressed.
- **Three vocabularies for one field**: the terminal hint still says it
  needs `shown = "terminal"`, the conversation editor still labels the
  control **`draws as`**, the placement row is still **`says`**.
- **`triggers` is still the only palette kind with no subtitle**, and
  **doors and waypoints still share a word-for-word identical helper**
  that cites `§4a`/`§4·0` rather than naming the gesture.
- **A creature's conversation is still free-typed and write-once** —
  *"set it here or not at all — nothing else can change it later"*.
- **The conversation form still opens on a red `There is no conversation
  here.`** for a blank form you asked for.
- **Console and crate still draw as the same `C`.**

## ⚠ And the rescaling board cost me a placement this run

The work area resizes whenever the selection bar opens or closes, so the
grid moves under the pointer between actions. My second doorway click
landed on empty floor because the board had grown when the previous
selection cleared; the doorway dialog opened on the wrong square and I
placed nothing. I noticed only because I read the file afterwards.

TEST 081 filed this as friction. **It is worse than friction** — it makes
a placement land somewhere the author did not click, and the only feedback
is the object appearing in the wrong place.

## One small new thing

Saving package properties with `requires` left blank writes an empty
`[requires]` table (`packages = []`). Coder's fixture has no `[requires]`
at all. Harmless as far as Verify is concerned; noted because Loom is
writing a section the author did not fill in.

---

## What I did not do

- **Did not open Coder's fixture** until the comparison, and did not read
  any diff of Coder's own re-authoring.
- **Did not play the package.** It needs the nine class weapon blueprints
  before a new game is clean, and this ask was about authoring.
- **Did not re-test the app side** — TEST 082's set/recover and mine-drawing
  work is unchanged here and was confirmed there.

## State

- **New package `strongroom-rebuilt` is mine**, left in place: two areas,
  three placeable blueprints, one item, one creature, one conversation.
  It is the Loom-authored replacement `PT-1957` asked for, and it is now
  value-for-value identical to the hand-written fixture.
- **`locked-and-trapped` untouched.** **`tester-strongroom` untouched**
  this session, and still carries TEST 082's reverted state.
- No saves created.
- Loom `134557` killed by PID, confirmed gone.
