# 015 · `BUILD/67` confirmed against the package that found it — and a list that cannot list

**From `Tester`. Unrequested number.** Confirms `PT-1493` / `BUILD/67`.

**Pins are honest.** `Loom` and the app both resolve `lodestar` to
`ce425423` — `Lodestar` `HEAD`. Both rebuilt this session (`kernel_blob.bin`
14:53); neither runner was trusted to do it.

    Lodestar ce42542 · Lens 04e4061 · Loom 51b49db · app 0a40e4b

**⚠ Confirmed against `tester-probe`, not a fresh package** — as asked. Its two
original `[[contents]]` rows still carry the **old** string Loom wrote, so the
area file now holds **both forms side by side** and every claim below is a
comparison inside one room:

    from = "blueprints/characters/probe-sentinel"   ← Loom, before 67
    from = "blueprints/characters/probe-warden"     ← Loom, before 67
    from = "characters/probe-warden"                ← Loom, today
    from = "characters/probe-sentinel"              ← Loom, today

---

## ⚠ CONFIRMED — and the seam is closed

**§1 · The path. A creature Loom places is there now.** I placed both blueprints
again with today's Loom; it wrote `characters/…`. In the app:

- **It stopped me.** I walked into `probe-warden.probe-room.03` at `4,1` and did
  not pass through it — the status line still read `4, 2`.
- **It talked.** My conversation, authored in Loom at 014, ran **end to end**:
  *"Halt. This room is sealed."* → the `[Persuade]` reply → *"Rank means nothing
  in here."* → `[Leave]`, which is `DIALOGUE-FORMAT-01`'s absent-`then`.
- **It fought, and it won.** `probe-sentinel.probe-room.04` at `4,3` has no
  conversation, so walking in started a fight: initiative, rolls, damage, and
  **YOU FALL**. A creature I authored beat me.

**⚠ The four rows are now visually different on the board.** The two that
resolve draw as filled combatants; the two that do not draw as hollow `P`. That
is new and it is the right half of the fix — `Lens` still draws every row, but
the player can now see which ones are real.

**§2 · The runtime silence. The sentence prints.** I staged the fault by moving
`probe-sentinel.toml` aside (my package; restored immediately after) and the
play screen said, verbatim:

> ⚠ `"probe-sentinel.probe-room.04"` is placed from `"characters/probe-sentinel"`
> and there is no blueprint there — it is drawn and is not present

**§3 · The structural silence. Verify reports without being asked.** Opening
`tester-probe` **cold** puts `2 problems` in the header *and* the status bar
before I click anything. The faults name the tag **and** the area, and quote the
exact string:

> `"probe-warden.probe-room.02"` in `"a01-probe-room"` is placed from
> `"blueprints/characters/probe-warden"`, and there is no blueprint there. It
> will be drawn and will not be present.

**`equipmentMissing` fires and names the slot** — more than the format asked
for:

> `"probe-warden.probe-room.03"` in `"a01-probe-room"` equips
> `"items/weapons/no-such-blaster"` in slot `"weapon_r_1"`, and there is no item
> there.

**§4 · `NewDoctrineDialog` is reachable, and I authored a doctrine.** `doctrines`
has a `+`, the form fits 1280×720 with `Create` reachable, and it wrote correct
`DOCTRINE-FORMAT-01` TOML. **That is the first artifact of that kind I have ever
been able to make.**

**F4 · The ordering trap says itself.** In amber under the conversation field:

> ⚠ set it here or not at all — nothing else can change it later. The path need
> not exist yet: name it now and author the conversation against this creature
> afterwards.

**It does turn a dead end into an order.** And as `BUILD/67` says, it does not
rescue `probe-sentinel`, which is still mute.

**⚠ Cold reopen — the negative you named. It is the same package.** Closed Loom
completely and reopened it three separate times. Each time: both areas, the
conversation, both creatures, the entry marker, and the **problem count**, all
intact. **Loom does not remember which package was last open** — it starts at
*"no package open"* and the chooser opens on `packages/`. I am reporting that as
behaviour, not a fault; the app has a `console/` for this and Loom has none, and
I do not know whether that is intended.

---

## ⚠ THE CONNECTION FAMILY — `PT-1379` holds, and I could not break it

**`tester-probe` had never had two areas. It has now: `a02-probe-hall`, an
arrival point, and a doorway. I walked it** — *"Probe Hall — arrived at
from-probe-room"*.

**Every fault `PackageProblem` already covered on this path is refused at
authoring, so the checker can never see Loom's own output:**

- **`landingPointUndeclared`** — pointing a doorway at an area with no arrival
  points: *"a02-probe-hall" declares no arrival points — place one there first*,
  and `Place` stays disabled.
- **`duplicateArrivalName`** — a second arrival with a name already in use:
  *This area already declares an arrival called "from-probe-room", and a
  connection landing there could not say which*, `Place` disabled.
- **`targetAreaUnknown`** — unreachable by construction; `leads to` lists only
  areas the manifest carries.
- **`Place` is gated twice** — it stays disabled until **both** an area and a
  landing point are chosen, not just the area.

**⚠ Which is the contrast worth having.** On the connection paths the Builder has
never been able to write the fault. On the blueprint path it wrote one for six
slices and nothing looked. **Same rule, two outcomes, and `67` is what made them
match.**

---

## ⚠⚠ F1 — ONE SHAPE OF BROKEN `from` STILL CANNOT BE REPORTED, AND IT IS THE ONE LOOM WROTE

**Photographed in a single frame:** three hollow markers on the board, **one**
`⚠` sentence.

`combatantsIn` opens with `if (!p.from.startsWith('$charactersIn/')) continue;`
— the deliberate silent one, correctly justified as *"a door is not a fault."*
**`blueprints/characters/probe-warden` trips that guard.** It is a creature by
any reading, it is the exact string `Loom` shipped, and to the runtime it is
indistinguishable from a door.

- **Verify catches it.** `package_validate` loops `area.contents` with **no**
  `charactersIn/` filter and reports `blueprintMissing`.
- **The play screen cannot.** The filter that decides "not a creature" is the
  same filter the old string trips, so the row never reaches `missed`.
- **I walked through both of them again today**, at `1,2` and `3,2`, standing on
  their squares, with the new build, and **nothing was said.**

**⚠ Every package Loom wrote before today carries that string.** The fix reaches
the writer and the checker; it does not reach the rows already on disk, and an
author who opens one in the app gets exactly the screen `PT-1493` was filed
about. **I am not proposing which side should move** — three places once
disagreed and Coder settled it at the reader; whether the runtime should also
name a `from` under `blueprints/` is the same judgement call again.

---

## ⚠⚠ F2 — THE NEW `+` WRITES A DOCTRINE THE PALETTE CAN NEVER SHOW

**`hold-the-room.toml` is on disk under `blueprints/doctrines/`. Loom says
`doctrines · none in this package`.**

**Not staleness.** I closed Loom completely and cold-opened the package again.
Still *"none in this package"*.

`right_pane.dart:280`:

    static const folderFor = <String, String>{'creatures': characterFolder};

**One entry.** For the other nine kinds `folder == null`, so `of()` sets
`out[kind] = const []` **without looking at the disk at all**. So *"none in this
package"* under `doctrines`, `items`, `doors`, `encounters`, `placeables`,
`sounds`, `stores`, `triggers` and `waypoints` **is a constant, not a fact about
the package.**

**⚠ That was harmless while nothing could write those folders. `67` made it
false**: `newableKinds` now gives `doctrines` a `+`, and the same pane that
offers to create one reports it absent for ever. **A creature's `doctrine` field
is a typed path with no list to pick from, so the doctrine I authored cannot be
attached to anything and nothing on screen admits it exists.**

**⚠ It is `F3`'s shape one step along** — *built, tested, constructed nowhere*
became *constructible, listable nowhere*. The reachability test guards the
first; nothing guards the second.

---

## ⚠ F3 — `equipmentMissing` only fires through a placement that resolves

**Proven inside one package, before and after, no reading required:**

- With `probe-warden` placed **only** by the broken row, verify said **2
  problems** and the dead blaster was **not** among them — although the
  blueprint was on disk, in the creatures list, and named an item that is not.
- After re-placing the same blueprint with a `from` that resolves: **3 problems**,
  the third being the equipment fault.

`package_validate` nests the `[equipment]` loop **inside** the `area.contents`
loop and `continue`s past any row whose blueprint does not open. So a blueprint
that is authored and not yet placed — the normal state of a creature between
being made and being used — **has its equipment unchecked**, and a blueprint
placed only by a broken row is checked for the placement and never for its
contents. The fault is also re-reported once per placement rather than once per
blueprint.

**⚠ This is `BUILD/67`'s own sentence about itself:** *"`PT-1452` made every link
fail out loud at the SEAM, and nothing checked it at REST."* The new check is
still at a seam. It is a placement's seam instead of a play session's.

---

## ⚠ F4 — an enemy's weapon note is computed and never read

`combatantsIn` sets `weaponNote: held.note` (`attack.dart:206`) and `speedNote`
(`:197`). **Neither is read anywhere.** The only `weaponNote` on a screen is
`play_screen.dart:122`, which passes `_myWeaponNote` — the **player's**, a
different value.

So when the warden fights, `equippedFrom` will have built
*"equips `items/weapons/no-such-blaster`, which will not open: …"* and thrown it
away, and the enemy's line will read `unarmed`, **identical to a creature that
genuinely carries nothing**.

**⚠ The asymmetry is visible on one screen I captured:** my own line says
*"your record names no weapon"*, and `probe-sentinel.probe-room.04: unarmed`
says nothing at all. For the sentinel that is correct — it carries nothing. For
the warden it would be wrong and silent.

**⚠ SCOPE — I did not photograph the warden fighting.** My conversation has no
branch that starts a fight and a creature with a conversation talks instead of
fighting, so I could not stage it, and I stopped rather than working around it.
**This finding is a source reading plus the on-screen asymmetry, and I am
labelling it as one.**

---

## Two small ones

**F5 · The ordering warning is field-specific; the constraint is dialog-wide.**
The amber sits under `conversation` and says *nothing else can change it later*.
**`doctrine`, class, level, faction, abilities and equipment are equally
unchangeable** — there is still no creature editor. An author who reads that
sentence under one field can reasonably conclude the others are editable. They
are not.

**F6 · The header's problem count goes stale after an edit.** I added two
placements; the status bar said *"edited a01-probe-room"* and the header still
read `2 problems` when the truth was 3, until I pressed **Verify again**. The
count is right on open and right after an explicit verify, and wrong in between.

---

## ⚠ ONE THING I GOT WRONG, AND IT WAS MINE

**I filled the doctrine dialog's `match` / `value` / `because` and pressed
`prefer nearest`, and the written file carried none of them.** I nearly filed
that as fields silently discarded.

**It is not.** Those five buttons are **add** buttons: `prefer nearest` adds a
rule-based preference and by design does not consume a match; `prefer match` and
`never` are the two that do. The dialog showed me exactly what it added. **I
misread the form and the file was right.** Recording it because a wrong reading
of a form is how a false defect gets filed.

---

## ⚠ SCOPED NEGATIVES — still not swept

- **Tile painting.** Both areas are `default = "floor"`. **I have still never
  painted a square**, so no tileset, no per-tile write, no `[tiles]` beyond the
  default.
- **`targetAreaUnknown`, `entryAreaUnknown`, `areaFileMissing`, `areaUnreadable`,
  `requiredFieldMissing`** — five of the eleven `PackageProblem` members are
  **unexercised by me**. I never removed a manifest field, deleted an area file,
  or corrupted one.
- **Area properties after creation**, and **package properties** beyond what
  `New package` asked at 014 (no cover, no `requires`, no `continues`).
- **The `assistant` tab.** Still never opened.
- **`scripts`.** Still never opened.
- **The contents of the eight other blueprint kinds** — `doors`, `encounters`,
  `items`, `placeables`, `sounds`, `stores`, `triggers`, `waypoints`. Only
  `doctrines` gained a way in, and per F2 the listing is a constant for all nine.
- **Conversation `effects`**, and anything past a single `gate`.
- **`NewItemDialog`** — not attempted. `BUILD/67` says why and `PT-1480`'s aim
  stays unanswered; **I did not try to force it.**
- **Any window size but 1280×720.** No resize, no second resolution, either
  program.
- **A roll result for the `[Persuade]` check.** The gate resolved and advanced,
  but I saw no pass/fail line for it in this package. **I did not investigate
  and I am not calling it anything** — at 006 I saw one in `endar-spire` and the
  difference may be mine.

---

## What `tester-probe` is now

Two areas joined by a working doorway, four placements — **two that resolve and
two that do not, on purpose** — a conversation with a gate, a doctrine nothing
can see, and a warden holding a blaster that does not exist. **It reproduces F1,
F2, F3 and F5 as it stands, and it is the fixture the seam was proved and
re-proved on.** Mine to keep; nothing of Coder's depends on it.

**I fixed nothing.** The one file I moved — `probe-sentinel.toml`, to stage the
`⚠` sentence — was restored in the same minute and the package is byte-identical
to before that step apart from what Loom itself wrote.
