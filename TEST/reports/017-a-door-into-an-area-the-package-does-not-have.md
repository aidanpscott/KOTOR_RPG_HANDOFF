# 017 · A door into an area the package does not have

**From `Tester`. Unrequested number.** The app side of the five, plus repaint,
prefabs and an extreme.

**⚠ WHAT I TESTED, EXACTLY.** Built 16:23 from:

    Lodestar (via lock) aac8505 · Lens 04e4061 · Loom 0cc9bcf · app d4dc2ea

**⚠ AND THE PINS ARE ONE COMMIT BEHIND, WHICH I DID NOT FIX.** `Lodestar HEAD`
is `0913ce0` (`PT-1503`); **both `pubspec.lock`s resolve to `aac8505`**
(`PT-1501`), its parent. `pubspec.lock` is yours, so I did not run
`pub upgrade` — **nothing below carries `PT-1503`.** `aac8505` is a clean
ancestor of `HEAD`, so this is a not-yet-levelled tree rather than a divergence.

**1280×720.** Every breakage was backed up and reversed; the only differences
left in `tester-probe` are the four edits I meant to make.

---

## ⚠ FIRST — `PT-1501` IS FIXED, AND MY ROOM WAS THE TEST CASE

Standing in `a01-probe-room`, both malformed rows now speak, on one line, with
nothing cut:

> ⚠ 2 drawn and not present — probe-sentinel.probe-room.01 — not a creature
> path, expected "characters/…" · probe-warden.probe-room.02 — not a creature
> path, expected "characters/…"

**Count first, both tags named, both reasons given, and the expected form
quoted.** The `⚠ WHEN A LIST CAN BE ELLIPSED, LEAD WITH THE COUNT` rule works:
even had it truncated, I would have known **that** two were wrong.

**⚠ `016`'s F1 is closed.** `blueprints/characters/…` — the one shape of broken
`from` the runtime could not report — is now reported, by name.

**⚠ And `PT-1502` is closed too.** `a03-probe-yard` (10×8) entered through
`a01`'s door (6×5) now **fits**: 66.8px tiles, the whole board on screen, my own
token fully visible at `0,0`. Last report it rendered at `a01`'s 96px and clipped.

---

## ⚠⚠ F1 — A DOOR INTO AN AREA THE MANIFEST DOES NOT LIST WORKS, SILENTLY

**This is the limp, and it is the one that matters.**

I removed `a02-probe-hall` from `[order] areas` and **left the file on disk** —
`targetAreaUnknown`, the fault Loom refuses to author and verify reports by
name. Then I walked into `a01`'s door.

**The app took me there.** *"Probe Hall — arrived at from-probe-room."* Full
board, arrival point, everything. **Nothing was said, at any point** — not on
the library card, not in the hub, not on the door, not on arrival.

**Where it goes:** `play_screen.dart:271` is

    final r = await openArea(_pathOf(id));

**The id is turned into a path and the file is opened. The manifest is never
consulted.** `[order] areas` gates nothing at play time.

**⚠ WHAT IS NEXT TO IT, AND IS THE POINT:** `Lodestar` treats the manifest as
**the** authority — three of the five faults are phrased *"The manifest lists
…"* — and `Loom` will not let you author a connection to an area the manifest
does not carry. **Two of the three programs agree the manifest defines the
package. The one the player uses does not read it.**

**So the failure is not "a broken package limps".** It is that **a player can
be taken into content the package declares is not part of it**, and the
subtractive edit — removing an area from the manifest — has no effect
whatsoever on what a player can reach.

**⚠ I do not know whether `[order]` is meant to gate travel** — the name says
ordering. But `targetAreaUnknown` exists as a fault, so something believes it
does, and the play client is the thing that disagrees.

---

## ⚠ F2 — THE HUB ASKS WHETHER AN ENTRY IS NAMED, NOT WHETHER IT EXISTS

**Two packages, the same underlying problem, opposite screens.**

**`base-rules`** — `Continue`, `New Game` and `Load Game` **all greyed**, and
the screen says:

> this package names no starting area — it supplies rules, not a place to play

**`tester-probe` with `[entry] area = "a09-nowhere"`** — **all three enabled,
nothing said.** You press `Continue`, and only then:

> There is no area file here.

**The guard is `package_main_menu.dart:129`:**

    bool get _canEnterPlay => widget.package?.entryArea != null;

**A null test.** It asks whether `[entry]` names something, never whether the
something is there. `a09-nowhere` is not null, so the package is offered as
playable.

**⚠ The app already owns the exact sentence** — *"names no starting area"* — and
applies it only to an entry that is **absent**, never to one that is
**unresolvable**. **That is `PT-1443`'s own shape one turn on:** that ruling was
about a disabled row reading as broken; this is a row that should be disabled
and is not. **`PT-1380`'s comment two lines below the guard says it outright —
*"A DISABLED ROW WITH NO REASON IS A BUG A PLAYER CANNOT DISTINGUISH FROM ONE."*
The inverse is here and unguarded.**

**⚠ I did not run the nine chargen steps to see whether `New Game` fails the
same way.** `Continue` commits and then fails; `New Game` would presumably do so
after nine steps, and I am not asserting it.

---

## ⚠ F3 — THE AT-REST EQUIPMENT FAULT CLAIMS THE BLUEPRINT WAS NEVER PLACED, AND IT WAS

**`PT-1501` added the at-rest check I asked for at `015`, and it works** —
verify went 3 → 4 and the new fault is the one that was missing. **Its
explanation is false in my package, and the disproof is the line above it:**

> `probe-warden.probe-room.03` in "a01-probe-room" equips
> "items/weapons/no-such-blaster" … and there is no item there.
>
> `probe-warden` — "probe-warden.toml" equips "items/weapons/no-such-blaster"
> in slot "weapon_r_1", and there is no item there. **It is authored and has
> never been placed, so nothing else would have looked.**

**`probe-warden` is placed twice**, and one of those placements produced the
fault immediately above.

**It is unconditional.** `package_validate.dart:352` bakes the clause into the
`reason` string of **every** at-rest `equipmentMissing`, with no test of whether
the blueprint is placed:

    reason: '"$name" equips "${e.value}" in slot "${e.key}", and there '
        'is no item there. It is authored and has never been placed, so '
        …

**⚠ This is `016`'s F3 again, in a different file** — a helpful clause asserted
rather than checked, sitting next to the evidence that contradicts it. And the
same dead reference is now reported **twice**, once per path.

---

## ⚠ THE APP SIDE OF THE FIVE — refuse, crash, or limp

**Nothing crashed. Nothing red-screened. `esc` always got me out.**

| broken | what a PLAYER gets | verdict |
|---|---|---|
| **`requiredFieldMissing`** (no `summary`) | The library card with **no description line**. Plays normally | **Graceful.** Not a defect — `summary` is an authoring rule, and a card with no blurb reads as an author who wrote none |
| **`entryAreaUnknown`** | Hub fully enabled → `Continue` → *"There is no area file here."*, `a09-nowhere` in the status bar | **Limp — F2.** Honest once you get there, offered as playable before |
| **`areaFileMissing`** (entry area) | Identical, naming `a01-probe-room` | **Limp — same as above** |
| **`areaUnreadable`** (entry area) | *"The area file is not valid TOML: TOML parse error: end of input expected at 40:1"* | **Honest, and the one written for a developer** — below |
| **`targetAreaUnknown`** | **Travels there. Says nothing.** | **⚠ LIMP, AND THE WORST — F1** |

**⚠ F4 · THE FAILURE SCREEN IS A PLAY SESSION, NOT A REFUSAL.** All three
entry failures land you **inside the play screen**: no board, the message in
alert colour, your vitality along the bottom, and *"arrows to move · esc to
leave"* offered. **I pressed the arrows. They do nothing and say nothing.** The
message is honest, but the app has already committed to playing a game that
cannot start, and then offers controls that are inert.

**⚠ F5 · A TOML PARSE ERROR REACHES A PLAYER, VERBATIM.** *"end of input
expected at 40:1"* is **exactly right for an author** — I would want the line
and column. It is the only string in this family written for a developer;
everything else in this app talks like a game (*"the wall blocks the way"*,
*"it supplies rules, not a place to play"*). **A judgement, and mine:** the
information should stay, the sentence around it should not be a parser's.

---

## ⚠ REPAINT AND ERASE — FLOOR IS THE ERASER, AND UNPAINTING IS A REGION TOO

**There is no eraser tool, and there does not need to be.** `erase` appears
nowhere in `Loom/lib`; painting **floor** over a tile removes it, and floor is a
paint like any other, so **everything `PT-1367` gives painting, it gives
unpainting.**

**Three repaints, all read back from the file:**

- **Floor over wall, by a drag** — row 1 went `####.#####` → `#..#.#####`.
  **A region erase from one gesture.**
- **Floor over difficult, by a diagonal drag** — rows 2–3 went `..:::::...` →
  `..:::.....`, **a 2×2 rectangle erased**, not the line I dragged.
- **Wall over water, non-floor onto non-floor** — row 4 `.~~~......` →
  `.~#~......`.

**And it reads correctly in the play client**: the new gaps in the wall are
gaps, and the wall standing inside the water pool draws as mass surrounded by
blue. **The legend did not shrink** — `~` is still in it because water is still
used elsewhere, which is the rule working.

---

## ⚠ PREFABS — THERE IS NO SURFACE, AND NO CODE

**Asked whether it exists at all: it does not, anywhere.**

**One occurrence of the word in all four repos**, and it is a note saying there
are none:

    Loom/lib/area/new_area.dart:18
    /// ⚠ NOTHING BELOW THIS. No grid, no tile map, no prefabs — 4b and 4c.

**No `Prefab` type in `Lodestar`. No prefab widget, dialog or writer in `Loom`.
No test.** The palette carries `floor · wall · water · difficult · hazard`, then
`ways`, then the ten blueprint kinds — **no selection tool, no copy, no paste,
no saved-selection surface of any kind.**

**⚠ So `PT-1367`'s third size is unbuilt, and it is not in `STATE.md`** — I
grepped it. That is the difference from `NewItemDialog`, which is unbuilt **and
written down**. **A ruled feature that is neither built nor tracked is the one
that gets forgotten.**

---

## ⚠ ONE EXTREME — AND LOOM REFUSES THE DEGENERATE CASE

**A 1×1 and a 64×1 cannot be authored.** Both are refused in `New Area` with
`Create` disabled:

> The smallest area is 2 × 2 tiles.

**⚠ That is consistent rather than contradictory:** `BUILD` says the tiles
writer was fuzzed against the 1×1 degenerate case, because a **reader** must
round-trip anything a hand-written file contains. The **dialog** declining to
create one is a separate decision and a defensible one. **Worth knowing that the
two differ.**

**So I took the extreme as 64×2 — a 32:1 strip — and it holds at both ends:**

- **In Loom**: 11px tiles, all 64 columns inside the pane, centred, no overflow.
- **In the app, entered through a door from a 6×5 room**: 19px tiles, the whole
  strip on screen, the arrival label placed, my token visible, movement working.

**⚠ And that is a real datum for `PT-1502`, not just a pass.** Four measured
tile sizes across two packages:

| entered | area | tile |
|---|---|---|
| fresh | `a01-probe-room` 6×5 | 95.7px |
| **through a door**, before `PT-1502` | `a03-probe-yard` 10×8 | **96.1px — a01's**, clipped |
| **through a door**, before `PT-1502` | `a02-starboard-hold` 10×6 | **68.2px — the deck's**, undersized |
| **through a door**, after `PT-1502` | `a03-probe-yard` 10×8 | 66.8px, **fits** |
| **through a door**, after `PT-1502` | `a04-probe-slit` 64×2 | 19.4px, **fits** |

**The extreme did not break it.** A 32:1 strip is the case a width-fitting rule
would get wrong, and it does not.

---

## ⚠ SCOPED NEGATIVES

- **`PT-1503` is not in anything above** — the locks are behind `Lodestar HEAD`
  and I did not touch them.
- **`New Game` on a broken-entry package** — untested; I ran `Continue` only.
- **`areaUnreadable` on a NON-entry area** — untested. I corrupted the entry
  area; I did not corrupt `a02` and walk into it.
- **One kind of corruption only** — an unterminated table header. Not a wrong
  type, not a bad `size`, not a broken `map` block, not a truncated file.
- **`requiredFieldMissing` for `summary` only** — I did not remove `authors`,
  `id`, `name` or `version` and see what the app does.
- **I did not combine faults in the app.** Each round was one breakage.
- **No `Load Game` against a broken package** — `Continue` only.
- **No tileset.** Still the drawn fallback everywhere.
- **Repaint tested with four combinations** — floor over wall, floor over
  difficult, wall over water. I did not repaint over an arrival, a doorway or a
  placement, and **I do not know what painting a wall under a creature does.**
- **Not touched, as instructed:** the eight inert blueprint kinds, and any
  window size but 1280×720.
- **`items` has gained a `+`** (`PT-1497`) and **I did not open it** — not this
  brief.

---

## What `tester-probe` is now

**Four areas.** A 6×5 entry room with three doorways, a 10×8 painted yard now
carrying deliberate repaints, a 4×4 hall, and a 64×2 strip. Five placements,
two of which still do not resolve **on purpose** and now say so out loud. A
conversation whose gate never rolls. A doctrine nothing lists. A warden with a
blaster that does not exist, now reported twice.

**I fixed nothing. Every breakage was reversed** — the manifest is whole, all
four areas are listed, `[entry]` is correct, and the only differences from the
backup are the third doorway, the repaints, the new area, and its line in
`[order]`.
