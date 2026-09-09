# 014 · A creature Loom places cannot be touched — and verify cannot see why

**From `Tester`. Unrequested number** — the Loom sweep had no request file, so
this takes the next free one.

**Built and run this session, by `./run-loom.sh` and `./run-app.sh`, both of
which rebuilt:**

    Lodestar  a5afc6f   Lens  04e4061   Loom  627a2cd   app  d114ee9

**Window 1280×720 for both, and that is the only size I used.**

**⚠ I authored a real package rather than reading one.** `tester-probe` on the
live shelf now has an area, two creatures, a placement each, and a
Persuade-gated conversation — all made through Loom's own surfaces, then
opened in the play client and walked.

**⚠ Not filed, per the brief:** PT numbers on Loom screens (they are correct —
Loom's user is an author and is owed the citation), the cast doing nothing, and
anything in `STATE.md`.

---

## ⚠⚠ F1 — A CREATURE PLACED BY LOOM IS DRAWN AND IS NOT THERE

**I walked through both of them.** Not past — **through**, onto their squares,
and out the other side. No conversation, no fight, no block, no message.

**Reproducible.** `tester-probe` → `New Game` → the Probe Room. `probe-warden`
sits at `1,2` and `probe-sentinel` at `3,2`; I crossed both squares in both
directions, twice each. **Both are drawn on the board the whole time.**

**Where the two programs disagree — this is a reading of the source, not a
claim about intent:**

`Loom/lib/shell/right_pane.dart:184` builds the palette entry a placement is
written from as `'$characterFolder/$e'`, and `characterFolder` is
`blueprints/characters` (`Lodestar/lib/src/character_open.dart:18`). So Loom
wrote, and I have the file:

    from = "blueprints/characters/probe-warden"

`KOTOR-RPG-APP/lib/play/attack.dart:150` opens with

    if (!p.from.startsWith('characters/')) continue;

and then prepends `blueprintFolder` itself on the next line. **The bed's own
area carries `from = "characters/sith-trooper"`** — which passes the guard and
resolves. **`Loom/lib/area/contents_writer.dart:8`, the writer's own doc
comment, gives the example as `characters/sith-trooper` too.** So the writer
documents one shape and the palette hands it the other.

**⚠ I do not know which prefix is the correct one** and I am not choosing.
Three places disagree and I can only tell you they disagree.

**⚠ WHAT IS NEXT TO IT, AND IS THE WORSE HALF:**

- **`Lens/lib/src/board.dart:245` draws `area.contents` directly**, with no
  reference to whether anything resolved. **The creature is therefore drawn by
  one program and unknown to the other, in the same frame.** A placement that
  fails every resolution still looks placed. There is no shape a bad `from` can
  take that the board will not render.
- **`attack.dart` `continue`s three times in six lines** — wrong prefix, file
  missing, not an `OpenedCharacterResult` — and **none of the three says
  anything to anyone.** A blueprint that is missing, corrupt or misnamed
  produces exactly the screen I saw: a dot you can walk through.
- **Nothing reported it at any layer.** Loom's verify says *"No problems
  found"*. The app logged nothing. The console file is clean. **I only knew
  because I tried to walk into it.**

**⚠ This is the seam I proved once at report 001 and had not revisited — and at
001 `tester-probe` had no creature in it.** The creature half of
Loom → app has never been exercised before today. Six Builder slices have
landed since.

---

## ⚠ F2 — Loom refuses one unresolvable reference and writes another

**Both in the same package, on the same afternoon.**

`probe-warden` was created through `New Creature` with
`weapon_r_1 = "items/weapons/no-such-blaster"` typed into the equipment field.
**`tester-probe` contains no items at all** — the list is empty, there is no
`items/` folder. Loom **wrote the field without comment**, and `verify` then
reported **"No problems found"** on the finished package.

**Why it cannot see it, which is the part worth having:**
`PackageProblem` (`Lodestar/lib/src/package_validate.dart:15`) has **nine
members**: `areaFileMissing`, `areaUnreadable`, `targetAreaUnknown`,
`landingPointUndeclared`, `duplicateArrivalName`, `entryUndeclared`,
`entryAreaUnknown`, `requiredFieldMissing`. **Not one of them is about a
blueprint's contents.** Verify checks areas, connections, arrivals, the entry
and the manifest. **A dangling equipment path is not a fault it has a name
for**, so the silence is structural and not a miss.

**⚠ Which means the same hole covers F1.** A `[[contents]]` entry whose `from`
resolves to nothing has no `PackageProblem` either. **Verify would say "No
problems found" about the room I could walk through.** It did.

---

## ⚠ F3 — The item writer and the doctrine editor are built, tested, and cannot be reached

**I could not author an item. Not badly — at all.**

- `Loom/lib/item/new_item.dart` and `Loom/lib/doctrine/new_doctrine.dart`
  define `NewItemDialog` and `NewDoctrineDialog`.
- Each is constructed **only in its own test** — `test/item_author_test.dart`,
  `test/doctrine_author_test.dart`. **Neither appears anywhere in `lib/`.**
- Contrast `NewCreatureDialog`, constructed at
  `Loom/lib/shell/loom_shell.dart:253` and reachable.
- `Loom/lib/shell/right_pane.dart:156` reads
  `if (k == 'creatures' && widget.onNewCreature != null)` — **`creatures` is
  the only kind that gets a `+`.**
- The `equip` button on the creature dialog **takes focus and does nothing
  else.**

**So an item can be *referenced* — by typing a path, as F2 shows — and cannot
be *made*.** The two suites are green about surfaces no author can open.

**⚠ This is why aim 2 (PT-1480, does anything catch corpus drift) is
unanswered.** I could not author the artifact the aim is about. **I am not
reporting that as a pass or a fail; I could not run it.**

---

## ⚠ F4 — A blueprint cannot be edited once created, and that makes an ordering trap

**There is no edit path to a creature anywhere.** `Loom/lib/shell/module_tree.dart`
wires `onNewArea` and `onNewConversation` as tappable; **the blueprint kind rows
are inert.** No `onEditCreature`, no `editCreature`, no `openCreature` — I
searched `lib/` for all three and for any callback reaching
`character_writer.dart` after creation. **Nothing.**

**The trap:** a creature's `conversation` field can only be set **in the New
Creature dialog**, at creation. The conversation editor wants an `owner` —
a creature that already exists. So:

- Conversation first → it needs an owner that is not there yet.
- Creature first → the conversation does not exist to name, and **you can never
  go back and name it.**

**Exactly one order works** (create the creature naming a conversation that
does not exist yet, then create the conversation under that name), and **nothing
on screen says so.** I found it by making `probe-sentinel` without a
conversation and then having no way to give it one. **`probe-sentinel` is still
mute and I cannot fix it through the product.**

---

## What I confirmed — the three aims I could reach

**⚠ AIM 1 · Loom refuses what validate refuses. CONFIRMED, BOTH DIRECTIONS.**

I authored a Persuade-gated reply with no continuation and pressed `Write`:

> refused — 1 problem: halt-this-room — `stand-down-i` is offered as a
> `Persuade` check and has no `then`, so nothing can roll it. §4c's amber means
> a real check; this one cannot happen (PT-1459).

**And no file was written** — I checked the folder, not just the screen. Adding
a following NPC line made `Write` succeed and produced correct TOML with
`then = ["rank-means-nothing"]`. **A dead check cannot be authored.**
`PT-1461` holds.

**⚠ AIM 3 · The New Creature dialog. FIXED, and Save is reachable.**
The dialog is taller than 720 and the vitality die and its override sit below
the fold — **but the body scrolls to them, and `Cancel`/`Create` stay pinned at
the bottom and are reachable without scrolling.** I created two creatures
through it. `BUILD/34`'s rule holds here.

**⚠ AIM 4 · Does Loom show its own validate findings? It shows what it has.**
`verify` reports on demand and the header carries a count when there are faults;
nothing is detected and hidden. **`PT-1379` is not violated by concealment.**
**It is the detecting that is short, not the showing** — F2. I checked
`verify_dialog.dart` for a suppressed or filtered branch and found none: every
`PackageFault` it receives is rendered.

---

## ⚠ SCOPED NEGATIVES — what I did NOT touch in Loom

**"I found nothing" would be worthless here, so:**

- **Tile painting.** My area is `default = "floor"` and I never painted a
  square. Untouched.
- **Doorways, arrivals, connections.** One area only; I never made a second and
  never linked them. **`place_way_dialog.dart`, `arrival_writer.dart` and
  `connection_writer.dart` are unexercised by me.** Note these are the paths
  `PackageProblem` *does* cover.
- **Area properties** after creation, and **package properties** (authors,
  summary, cover, requires, continues) beyond what `New package` asked me for.
- **The `assistant` tab.** Never opened.
- **`scripts`.** Never opened.
- **The eight other blueprint kinds** — `stores`, `triggers`, `waypoints`,
  `sounds`, `placeables`, `encounters`, `doors`, and items/doctrines per F3.
  **All inert; no `+`, no editor.** I pressed each row.
- **Any window size but 1280×720.** No resize, no second resolution.
- **The conversation editor's `effects`** and anything past a single `gate`.
- **Reopening Loom on a package it did not create in the same session** — I
  authored and verified in one run.

---

## ⚠ One reading I am flagging as a reading

**`RUNNING-ON-THIS-MACHINE.md` says `endar-spire` is Loom's output.** Its
`[[contents]]` carry `characters/…` and Loom today writes
`blueprints/characters/…`. **I did not regenerate it and I am not going to** —
it is the fixture every suite reads and it is `Coder`'s. **But if it is still
described as Loom's output, that description and Loom's current palette do not
agree**, and one of the two has moved.

---

## What I did NOT do

**I fixed nothing.** `tester-probe` is mine and stays as it is — a package with
an inert room, a mute sentinel and a warden holding a blaster that does not
exist. **It reproduces F1, F2 and F4 as it stands.** Delete it when it stops
being useful; nothing of mine depends on it.
