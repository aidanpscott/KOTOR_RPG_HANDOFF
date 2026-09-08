# 14 · Identity — the last step, and what Play owes

**`KOTOR-RPG-APP` `fd48d5c`.** 150 tests pass, analyze clean. **All nine steps
are built. Play can unlock for the first time, and it still does nothing.**

---

## ⚠ 1 · The portrait question, answered before the screen

**There is no portrait set. Not ours, not a placeholder set, not one to
import.**

| Where I looked | What is there |
|---|---|
| `UI-ASSETS-01 §2` | *"Presets per species, filtered by the species chosen (`PT-1214`). With 47 species and multiple portraits each **this is the largest art commitment in the flow**."* And: **"Currently: a filled circle."** |
| `ASSET-REPLACEMENT-01` | `Portraits · PT-1214 presets, ours · ⬜` — **an unticked box, marked ours** |
| `data/extracted/` | No portrait data in any of the 16 extracts |
| the shelf | No image file of any kind in any of the three packages |
| the app | Nothing. `species_screen.dart` defers them to this step and that is all |

> **⚠ So the placeholder IS the authored state, not a shortcut I took.**
> `§2` names it — a filled circle — and `PT-1157` requires a placeholder to be
> visibly a placeholder, so it is labelled rather than dressed up as art.

**⚠ And this is the first screen where `PT-1350` is visible to a player** —
exactly as the brief anticipated. The stage renders the circle and says there
is nothing to pick.

### ⚠ Importing would not fill it either, and that is the sharper finding

**K1 ships 181 `po_*` portrait textures** — `po_pbastila`, `po_pcanderous`,
`po_pbastila3e`. **They are named for the games' own characters, not for a
species.** `PT-1214` asks for *presets per species*; an import supplies Bastila's
face, which is a different thing. **The art import answered at `PT-1409` cannot
satisfy this row**, and the screen says so rather than implying importing would.

### Two needs, neither invented here

- **The presets themselves.** 47 species × several each, ours to draw. Sizes are
  already specified: **66–84px on Identity, 46px in the rundown, 14–19px in
  lists** — one source image, several sizes.
- **⚠ The custom-upload spec.** `PT-1180` found NWN ships genuine
  custom-portrait support via a player-side folder *"and ours does too."*
  `§2`: **"A custom portrait needs no art, but it needs a spec: accepted
  formats, dimensions, and what happens to an image of the wrong aspect."**
  That spec is unwritten — **and it is the one half of this that needs no
  drawing at all.**

**`identity.portrait` is `null` in the choice, not a fabricated ref.**
`CHARACTER-RECORD-01`'s shape is `{"kind": "preset", "ref": "bith_04"}` and no
preset exists to reference.

---

## 2 · Step 9 — Identity

**Three stages that transition in place.** `§3` groups Identity with Origin, and
the back control is **inside the step**: `BACK` returns to the earlier stage
without leaving Identity and **without losing state**. Backstory went the other
way at `PT-1401` — two tabs collapsing into one — and this is that distinction
in reverse.

    IDENTITY  →  IDENTITY — NAME  →  IDENTITY — YOUR STORY
              [Name ▸]          [Story ▸]        [Accept]
    Cancel        BACK              BACK

### YOUR STORY

**The full rundown above**, exactly as `PT-1243` names it: name, species, class,
all six abilities, then the flavour choices as rounded chips — origin,
upbringing, profession. **⚠ Not aptitudes**: that chip was removed at owner
ruling because aptitude is a mechanical consequence and the rundown is about who
the character *is*.

**Below it, a generated story assembled from exactly those choices**, with the
assembly visible in the prose rather than generic — the world supplies the
place, the upbringing supplies how it went, the profession supplies the work,
the class explains the hands. **Three variations, all true to the same inputs.**

**⚠ A real text field, not a display.** `Try another` regenerates from the same
inputs; `CLEAR` empties it and focuses the cursor — both were asked for
specifically. The status line tracks **three states**: *assembled from your
choices · edited by you · empty*, so a blank field reads as deliberate rather
than broken.

**⚠ A droid has no world and no upbringing.** The generator drops those clauses
rather than printing an empty one.

---

## ⚠ 3 · Play can unlock, and what it owes

`_unbuilt` is now **empty**. `_describe` is **exhaustive** — the wildcard
existed because four steps were unbuilt, and it would now hide the next step
added rather than failing to compile.

**Play still does nothing, and the hub says what it owes.**

> **⚠ WHAT PLAY MUST WRITE IS A LOG, NOT A RECORD.**
> `CHARACTER-RECORD-01` opens by ruling that out: *"This record is a
> **PROJECTION** of the event log, not the store. Creation writes **events** —
> a species chosen, a point spent, a feat taken. The record is what you get by
> replaying them… **the log is what persists.**"* And `SAVE-LOAD-01` is titled
> **"the save is the log."**

**So the next stretch is not "serialise the hub".** The hub holds nine choice
objects in memory, in whatever order the player clicked. The ledger wants the
choices **as ordered events**, and three consequences fall out that the document
calls **not optional**:

- *"Validate on load"* means **validate the projection**, after replay — not a
  file on disk.
- **A correction is a new event, not an edit.** Nothing rewrites history.
- **Multiplayer falls out of the log's visibility sets**, not out of the record.

**⚠ And the re-lock is already an event problem.** Re-opening a completed step
discards everything after it — six fields, today, by assignment. Under an
append-only log that discard is itself an event, and *"a correction is a new
event, not an edit"* says it cannot be a deletion. **Nothing has ruled what the
re-lock writes.**

Two smaller things the record's own shape asks for and no screen produces:

| Field | State |
|---|---|
| `backstory.lifestyle` | In the record. `PT-1401` collapsed lifestyle into the profession row, so no screen sets it |
| `identity.story_origin` | `CHARACTER-RECORD-01 §` calls it **"proposed here, not ruled"** |

---

## What was NOT done

**No character record. No save.** `CHARACTER-RECORD-01` and `SAVE-LOAD-01` have
still never been written to, and Play still leads nowhere. Nothing was extracted
from either game. No portrait art was made or imported.

**Not captured:** Identity was verified by test at 1280×720, not by screenshot,
and **the step strip with zero padlocks and Play unlocked has never been seen** —
that state has not existed before today.
