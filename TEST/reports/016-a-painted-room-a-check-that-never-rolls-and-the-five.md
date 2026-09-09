# 016 · A painted room, a check that never rolls, and the five that had never fired

**From `Tester`. Unrequested number.**

**⚠ WHAT I TESTED, EXACTLY.** Built and run at 15:30–15:31 from:

    Lodestar 9e7d99e · Lens 04e4061 · Loom debd33 (Level with Lodestar, PT-1495)
    KOTOR-RPG-APP c96f25b (Level with Lodestar, PT-1495)

Pins honest — both locks resolved `lodestar` to `9e7d99e`, which was `HEAD`.
**⚠ Two commits landed while I was working and are NOT in anything below:**
`Loom 0357b0e` (PT-1497, `NewItemDialog` reachable) and `app 1590501`
(PT-1499, a malformed character reference says so). **PT-1499 is close enough
to F1 below that it may already move it; I have not tested it.**

**1280×720 throughout.** All damage to `tester-probe` was backed up first and
restored; the final `diff -r` against the backup is **IDENTICAL**.

---

## 1 · I PAINTED A ROOM

**`a03-probe-yard`, 10×8, painted in Loom with all five tile types**, then
walked in the app. `tester-probe` now has three areas.

**⚠ PT-1367 · REGIONS, NOT SQUARES — CONFIRMED, and it is a rectangle.** I never
clicked a single tile for the bulk of it. A drag along row 1 painted a four-wide
wall run in one gesture; a **diagonal** drag from `2,2` to `6,3` filled the whole
**rectangle** rather than the line I dragged. Water the same. Single clicks work
for one-offs (the two hazards).

**⚠ PT-1345 · THE MAP ON DISK IS THE MAP I DREW.** Byte for byte, and the legend
carries only the five types actually used:

    [tiles]
    legend = { "." = "floor", "#" = "wall", "~" = "water", ":" = "difficult", "!" = "hazard" }
    map = """
    ..........
    ####.#####
    ..:::::...
    ..:::::...
    .~~~......
    .~~~.!!...
    ..........
    ..........
    """

**I can read my own room in a text editor.** The wall gap at column 4 is a gap
in the string. This is the ruling paying off exactly as written.

**⚠ Verify stayed at 3 problems** across a new area, 80 painted tiles, an
arrival and a doorway — none of it introduced a fault.

---

## ⚠ WALKING IT — three rules met a player, and they are three different things

**WALLS STOP YOU, AND SAY SO.** *"the wall blocks the way"* — it names the tile
type, so a player learns what stopped them.

**WATER STOPS YOU, AND SAYS SOMETHING DIFFERENT.** *"the water blocks the way"*.
`§2·0a`'s point — *"a water tile is water and you cannot just walk over it"* —
is on the screen, and it is not confused with a wall.

**⚠ DIFFICULT GROUND COSTS NOTHING. `TileType.difficult`'s own doc says
"Costs more to cross."** Nothing anywhere reads it:

- Outside a fight there is no movement budget at all, so nothing could cost.
- **Inside a fight I crossed four difficult squares in a row** (`6,2`→`3,2`)
  and was never told I had run out of move, and nothing on either screen ever
  mentioned the ground.
- `play_screen.dart:411` spends `budgets.move(1)` — **a flat 1, with no tile
  lookup**. I grepped both repos: outside the enum's own declaration, the only
  match for `difficult` is a comment about a droid chassis.

**So it is a documented property with no implementation.** I am filing it as
that and not as a rules question — the sentence is already written down.

**⚠ HAZARD DOES NOTHING, AND THAT IS CORRECT.** I crossed **both** hazard tiles
**at 1 vitality**, where any damage at all would have killed me. No message, no
damage, no effect. **`TileType.hazard` says *"Crossing it does something. ⚠ What,
is unruled — §2·0a."*** So inert is the spec, and I am **not** filing it.

**⚠ But it is a question, and it is an authoring one.** Loom offers `hazard` in
the palette **identically** to the four types that do something — same section,
same `drawn` row, no mark — and paints it in a distinct amber hatch that reads
like a real rule. **An author paints it expecting it to bite.** Nothing in Loom
or the app says the effect is unruled. That is the owner's, not a defect.

---

## ⚠ PT-1366 · DOES THE DRAWN LOOK READ AS "MISSING ART"? — MY ANSWER IS NO

**Asked for a judgement, so this is one, and it is mine.**

**It reads as a deliberate schematic, not as an absence.** What makes it read
that way:

- **The five types are told apart by different visual *languages*, not by five
  flat colours.** Walls are dark **mass** with a bright edge **and the grid
  lines stop inside them**. Water is a **vertical gradient** block. Difficult is
  **stipple**. Hazard is **diagonal hatching**. Floor is a lit wash with a
  vignette. Nobody produces four different idioms by accident, and a viewer
  reads that as intent.
- **`PT-1367`'s own bar is met**: *"walls are mass, floor is a lit surface."*
  They are.
- **There is no missing-texture vocabulary anywhere** — no checkerboard, no
  magenta, no grey box, no "?" tile. The thing a person recognises as absence is
  simply not present.

**⚠ What does read as unfinished, and it is a different complaint:** everything
is one hue family, so **a room that is mostly floor looks like a blank sheet
rather than a place**. My 10×8 yard with 60 floor tiles reads emptier than
`endar-spire`'s deck does, and that is about **the floor having no character**,
not about the tileset being absent. **That is `nothing has been designed`,
which is known scaffolding.** So: `PT-1366` holds; the floor is where the look
is thinnest.

---

## ⚠⚠ F1 — TRAVELLING THROUGH A DOOR KEEPS THE OLD ROOM'S SCALE, AND CLIPS THE NEW ONE

**On arriving in the Probe Yard my own character was half off the top of the
screen and the bottom row was cut off.** It does not settle — I captured at
0.7s and again at 4.7s and the two frames are **identical**.

**It is not "big areas clip".** `endar-spire`'s Command Deck is **12×8** —
bigger than my 10×8 — and on `Continue` it fits perfectly, 68.4px tiles, margin
all round.

**⚠ The difference is travel, and the numbers say so exactly:**

| where | area | tile size |
|---|---|---|
| `a01-probe-room`, entered fresh | 6×5 | **95.7px** |
| `a03-probe-yard`, entered **through a01's door** | 10×8 | **96.1px** ← a01's |
| `a01-command-deck`, entered fresh | 12×8 | **68.4px** |
| `a02-starboard-hold`, entered **through the deck's door** | 10×6 | **68.2px** ← the deck's |

**Both packages inherit the previous area's tile size.** In the shipped bed it
is invisible because the hold is *smaller*, so it just wastes margin. Go the
other way — small room to big room — and the board overflows the window.

**⚠ It recovers when anything else forces a relayout.** The moment a fight
started and added text lines under the board, the yard snapped to a size that
fits. So the board can compute the right size; it just does not do it on travel.

**⚠ WHY THIS MATTERS MORE THAN A MARGIN:** the player's own token was the piece
off-screen, at `0,0`, in the corner an arrival point puts you in. **`Lens`'s own
most recent commit is "The board re-fits when its space changes"** — the space
did not change on travel, and that is the case it does not cover.

---

## ⚠⚠ F2 — A `[Persuade]` CHECK ON A REPLY IS NEVER ROLLED. I PASSED IT 12 TIMES OUT OF 12

**You asked me to find out, and I did. ⚠ AND MY OWN REPORT 006 WAS WRONG:** I
wrote that `[Persuade]` *"rolls and passes"*. **The passing was real. The rolling
was my inference and there was none.**

**The evidence, and it is not a reading.** I made a Cathar Soldier with
**Persuade 4**, against my conversation's **DC 14** — `d20 + 4 ≥ 14` needs a 10
or better, **55% a try**. I took the same check **twelve consecutive times**,
leaving and re-entering the conversation each time. **Twelve passes.**

    0.55 ^ 12  ≈  0.0008

**And a second character passed it too:** `probe-walker`, who never spent a
skill point — Persuade 0, needing a 14 or better, **35%** — passed first time.

**⚠ AND THE SHIPPED BED IS AUTHORED THE SAME WAY, so this is not my package.**
`endar-spire/dialogue/trooper-challenge.toml`:

    replies = [ …, { to = "you-are-one", gate = { skill = "Persuade", dc = 14 } }, … ]

    [[player]]
    id   = "you-are-one"
    then = ["one-man-yes"]          # ← ungated

**Where it goes, as a reading of why:** `DialogueRun.choose()` runs
`_pick(option.line.links, …)` — the links of **the player line you chose**,
which is that ungated `then`, and `_pick`'s first branch is
`if (l.gate == null) return l.to;`. **The reply link's own gate is only ever
evaluated by `_gateVerdict` for visibility** — `Verdict.isACheck`, which is what
paints the amber bracket. `_pick` does roll, properly, using the same `resolve()`
combat uses — **but only for a gate sitting on a `then`, where nothing is shown
and no author has put one.**

**So the two places a skill gate can sit behave oppositely:**

- on a **`replies`** link — **shown as a check, never resolved**
- on a **`then`** link — **resolved, never shown**

**⚠ `PT-1326` is why I am filing the roll and NOT the missing line.** That ruling
makes *inspecting* a check an option that is **default off**, so seeing no
derivation is not by itself wrong. **What is wrong is that there is nothing to
inspect.** `§4c`'s amber is defined as meaning a real check, `PT-1461` refuses to
author a check that cannot roll — **and this one is shown, is authored exactly as
the format's own bed authors it, and cannot fail.**

---

## ⚠ THE FIVE THAT HAD NEVER FIRED — ALL FIVE NOW HAVE

**Broken deliberately in `tester-probe`, in two rounds, and restored.** Loom
**opened the broken package rather than refusing** and put the count in the
header and the status bar on open.

**Round A** — area file moved away, a second area's TOML corrupted, `summary`
deleted from the manifest. **8 problems.**

| member | what it said | can an author find it? |
|---|---|---|
| **`requiredFieldMissing`** | *The manifest declares no summary, which PACKAGE-FORMAT-01 §4·1 requires.* — and beneath it, **`set in package properties`** | **Yes, and it names the surface to fix it on.** The best of the five |
| **`areaUnreadable`** | *The manifest lists "a02-probe-hall" but it cannot be read: The area file is not valid TOML: TOML parse error: end of input expected at **11:1*** | **Yes — line and column** |
| **`areaFileMissing`** | *The manifest lists "a03-probe-yard" but it cannot be read: There is no area file here.* | **Yes** |

**Round B** — restored, then `a02` removed from `[order] areas` and `[entry]`
pointed at a non-existent area. **5 problems.**

| member | what it said |
|---|---|
| **`entryAreaUnknown`** | *[entry] names "a09-nowhere", which this package does not list.* · **`declared: a01-probe-room, a03-probe-yard`** |
| **`targetAreaUnknown`** | *"door.probe-room.05" in "a01-probe-room" leads to "a02-probe-hall", which this package does not list.* · **`declared: a01-probe-room, a03-probe-yard`** |

**⚠ `targetAreaUnknown` IS NOT DEAD CODE — and I was wrong to call it
unreachable at 015.** I said Loom could not produce it because `leads to` only
offers manifest areas. **That is still true of Loom, and it is not the only way
in.** It fires the moment a target area **cannot be opened**, which any author
can cause with a bad save, a half-written file, or a moved folder — and in round
A **it fired twice without my aiming at it at all.**

---

## ⚠ F3 — AND THAT IS THE FINDING: IN ROUND A THE FAULT CONTRADICTED ITSELF

**Two adjacent lines of the same fault, in round A:**

> "door.probe-room.05" in "a01-probe-room" leads to "a02-probe-hall", **which
> this package does not list.**
> **declared: a01-probe-room, a02-probe-hall, a03-probe-yard**

**The sentence says the package does not list `a02-probe-hall`. The very next
line lists it.** Same for `door.probe-room.06` and `a03-probe-yard`.

**The cause:** in round A `a02` **was** in the manifest — it was simply
unreadable. An area that cannot be opened drops out of the resolvable set, so
the connection check reports **"not listed"** for something that is listed.
**Round B proves the check itself is right** — with `a02` genuinely removed, the
same message is true and `declared:` backs it up.

**So the check is correct and its trigger is over-broad.** One broken file
produces three faults, and **two of them explain themselves falsely**. The
`declared:` line was added to help an author and here it is the thing that
disproves the sentence above it. An author who trusts the message opens
`package.toml`, finds the area listed, and has been sent to the wrong file.

---

## ⚠ ONE I NEARLY MISREAD, AND IT WAS MINE

**In the Loom doctrine dialog I filled `match` / `value` / `because`, pressed
`prefer nearest`, and none of it reached the file.** I nearly filed *fields
silently discarded*. **It is not a defect** — those five are **add** buttons;
`prefer nearest` adds a rule-based preference and by design does not consume a
match, while `prefer match` and `never` are the two that do. **I misread the
form.** Recorded because a misread form is how a false defect gets filed.

---

## What I confirmed along the way, not filed

- **My own character's weapon note works and names the path**: *"equips
  `items/weapons/blaster-rifle`, which will not open: There is no item here."*
  `tester-probe` carries no items, so a Soldier's rifle cannot resolve — the
  package is incomplete and the app says so clearly. **That sharpens 015's F4**:
  the player's note is printed; the enemy's identical note is computed and
  dropped.
- **Loom refuses an id with a number in it** — *"Ids carry no numbers. Only
  areas are numbered"* — and numbers the file itself.
- **Arrival names are per-area**: `from-probe-room` in both `a02` and `a03` drew
  no duplicate warning, correctly.
- **Two doorways out of one room both work**, and the second was placed and
  travelled without incident.

---

## ⚠ SCOPED NEGATIVES

- **No tileset.** Every area here is `no tileset`; I tested the **drawn
  fallback** only. `PT-1366`'s tiers 1 and 3 are untouched by me.
- **Prefabs.** `PT-1367` also rules a prefab is a saved selection that pastes.
  **I never made or pasted one** — I saw no prefab surface in the palette and
  did not go looking.
- **No repaint over existing tiles.** Every square I painted was floor first. I
  never painted wall over water, and never used a floor "eraser".
- **Only one 10×8.** I did not try a 1×1, a 64-wide row, or a very large grid;
  `BUILD` says the writer was fuzzed at those sizes and I took that as read.
- **Difficult ground in a fight was tested in one direction** — I moved away
  from the enemy. I did not test whether approaching across it differs.
- **`areaUnreadable` with one kind of corruption only** — an unterminated
  table header. Not a wrong type, not a bad `size`, not a broken `map` block.
- **`requiredFieldMissing` for `summary` only.** I did not remove `authors`,
  `id`, `name` or `version`.
- **I did not test what the APP does with any of the five.** All five were read
  through Loom's verify. Whether the play client refuses, crashes or limps on a
  package with no entry area is **untested by me**.
- **Not touched, as instructed:** the eight inert blueprint kinds,
  `NewItemDialog`, and any window size but 1280×720.
- **The two newest commits** named at the top.

---

## What `tester-probe` is now

Three areas. A painted 10×8 yard with walls, a wall gap, a water pool, a
difficult rectangle and two hazards. Two doorways out of `a01`, two arrival
points, five placements — **two of which still do not resolve, on purpose** —
a conversation whose gate never rolls, a doctrine nothing lists, and a warden
holding a blaster that does not exist. **A second character, `Yard Tester`,
Cathar Soldier, Persuade 4, who exists to take a check twelve times.**

**I fixed nothing, and everything I broke is restored** — `diff -r` against the
pre-damage backup reports the package **IDENTICAL**.
