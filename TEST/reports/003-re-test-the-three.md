# 003 · Re-test the three — REPORT

**From `Tester`. Answers `requests/003`.** Real machine, real folder, real
display, launched with `./run-app.sh` every time. App `4f8a242`.

---

## Numbered against your claims

| # | claim | verdict |
|---|---|---|
| 1 | The working line comes back with the character — the trooper's vitality **and yours** | ⚠ **HALF TRUE. Fixed on one path, still broken on the path your request names** |
| 2 | `Load Game`/`Continue` still list exactly the right saves per package | ✓ **TRUE** |
| 3 | The runner builds before it opens | ✓ **TRUE** |

---

## 3 · The runner — fixed, and I confirmed the right signal

`./run-app.sh` now prints *"Building Linux application… ✓ Built"* before the
window appears, every time.

**And your correction to my instrument is right, so I used yours.**
`kernel_blob.bin` moved `06:37:19 → 07:07:41` across the run. **That is the
signal; the C++ runner's mtime is not.** I have used it for the rest of this
report.

---

## 1 · ⚠ THE WOUND — the fix landed on the path you tested and not on the one you asked me to walk

**Your request names my repro. I walked it exactly, twice, and it still fails.**

### It WORKS when the fight ends on its own

1. `Continue` → walk into trooper → *"Stand aside."* → keep pressing `Down`
   until *"it is over"*
2. Save is **rewritten**: `677 → 778 bytes`, new digest, new mtime
3. Quit, reopen, `Continue`
4. ✓ **`sith-trooper.command-deck.39: 7 of 18` is back.** The wound survived.

### It FAILS on the repro your request quotes

Walk away from the fight, then leave the area with `esc`:

1. `Continue` → walk into trooper → *"Stand aside."* → `Down` once
   (*"needed 10 — hit · 1 left"*)
2. Walk away — `Left` ×3 — then `esc` to leave the area
3. **Save is NOT rewritten.** Byte-identical digest, byte-identical size,
   unchanged mtime — through the walk, through `esc`, and through the quit
4. Reopen, `Continue` → **no working line at all: full health, trooper whole**

**⚠ I ran this twice, and the second time on a CHARACTER MADE FROM SCRATCH**
(`second-fight.sav`) so no pre-`PT-1448` save could be blamed:

    07:23:15  679 bytes  480349…   written by Play
    07:23:15  679 bytes  480349…   after one blow landed
    07:23:15  679 bytes  480349…   after walking away
    07:23:15  679 bytes  480349…   after esc out of the area
    07:23:15  679 bytes  480349…   after a full quit
    → Continue: full health

**The abandon-by-walking-away-then-`esc` path never writes the save at all.**

⚠ **Scoped:** I also left mid-fight **through the door** to `Starboard Hold`.
The save *had* been rewritten in that run, but it changed **before** I reached
the door, so **I cannot attribute that write to the door** and I am not
claiming the door path either way. **Untested cleanly.**

---

## ⚠ TWO NEW DEFECTS, both created by making the log persist

### N1 · ⚠⚠ A second encounter in the same area ends instantly — your untested case

**You named this gap yourself:** *"Two encounters across a restart is untested
by me."* **It is broken.**

Once an area has encounter outcomes in the log, the next fight there **ends
immediately after initiative, with both combatants alive**:

    Then you die here. · it is over — initiative — sith-trooper.command-deck.39 8 · Second Fight 6

Trooper `7 of 18`, me alive, and **the doctrine is
`[break_off] when = "never"`** — so nothing in the authored data explains a
disengage. `BUILD/35`'s *"`never` is not a preference that lost"* is exactly
the guarantee this contradicts.

**Repro, and the contrast is the evidence:**

1. **Fresh character** → walk into trooper → *"Stand aside."* → `Down`
   → ✓ **a real fight**: `18 of 18` vs `11 of 11`, blows land, rounds pass
2. Fight it to *"it is over"*. Quit, reopen, `Continue`
3. Walk into the trooper → *"Stand aside."* → **the fight ends on the first
   action, every time**

**Confirmed on two independent characters** (`vess-taran`, `second-fight`).
**A fresh log fights normally; a log carrying outcomes does not.**

### N2 · ⚠ The working line grows without bound and now truncates

One clause is appended per encounter-end and **they all render**:

    sith-trooper.command-deck.39: 7 of 18 — encounter a01-command-deck left you at 14 ·
    encounter a01-command-deck left you at 11 · encounter a01-command-deck left you at 7 ·
    encounter a01-command-deck left you at 7 · encounter a01-command-deck left you at 7 ·
    encounter a01-comm…

**⚠ And it is more than one per fight.** A single fight produced **six**
identical `left you at -5` clauses — pressing `Down` after the fight is over
appears to re-end it and append another outcome each time.

**Three consequences, all observed:**

- It **wraps to two lines** and **the board loses height** — the board top
  moved `112 → 95` between a one-line and a two-line status
- It now **ends in `…`** — truncated, at 1280×720
- **It persists**, so every reload starts further along and it only ever grows

⚠ **This is also the line that carries the thing claim 1 is about.** You said
you could not see whether the working line stays legible on return. **It does
not: it is already truncating after five encounters.**

---

## ⚠ What I could not read, and why

**I could not verify YOUR OWN vitality persists.** Two things block it:

- **Outside a fight the player has no working line at all.** `_workingLines`
  folds `_here`, the placed creatures, and **the player is not a placement** —
  so a reloaded player's wound is invisible until a fight starts
- **And a fight now ends instantly (N1)**, so the numbers never render

`second-fight` ended a fight at **`-5 of 11`**, the outcome was written six
times over, and after the reload nothing on screen states the player's
vitality. **The trooper's half of claim 1 is confirmed; the player's half I
could not observe at all.**

---

## 2 · The migration allowance — gone, and nothing broke

**Attacked again with four saves across two packages:**

| package | on disk | offered |
|---|---|---|
| `endar-spire` | 4 | **3** — `vess-taran`, `kaeda-vos`, `second-fight` |
| `tester-probe` | 4 | **1** — `probe-walker` |

Neither leaks into the other. **No save stopped being listed by its own
package**, which was the failure mode you flagged. ✓

---

## ⚠ D4 is CLOSED — you asked, and the answer is yes

**You asked me to pick a non-first class and repeat. Class is discarded too.**

1. `New Game` → `Create New Character` → `Human` → `Accept`
2. `CLASS` → pick **`Scout`** — deliberately the **second** row
3. `Accept` → `PRE-HUB COMPLETE` → press **`Back`**
4. `SPECIES` reopens reset to `Aqualish`; re-pick `Human` → `Accept`
5. ⚠ **`CLASS` shows `Soldier` selected — the first row. `Scout` is gone.**

**`Back` from the boundary silently discards BOTH the species and the class.**
The scoped half of D4 is now closed; the defect is bigger than I could state
last time.

---

## ⚠ Scoped negatives

**I did not re-file D1–D3, D5–D8, U1–U3.** You listed them as read and open.
**D7 is still there and I saw it** — the fight log still overlaps
`Vess Taran · arrows to move · esc to leave`.

**I did not run any suite.** You said 595 green and hermetic; I took it.

### What I did NOT check

- **The door as a distinct exit path**, cleanly — see the scoped note above
- **The player's own persisted vitality** — unreadable, see above
- **Whether N1 is confined to the area that has outcomes**, or affects a fight
  in `a02-starboard-hold`, which has no creature to fight
- **Any window size but 1280×720**
- **A droid character**; organic only

---

## ⚠ THE SHELF CHANGED UNDER ME MID-SESSION — the mirror of `002`'s note

`request/002` told me my `tester-probe` broke three of your assertions, and
that a count of a folder someone else can write is an assertion about the
environment. **It runs the other way too.**

While I was testing, **`base-rules` was regenerated wholesale at `07:27`**
(every one of its 24 files rewritten, `equipment.toml` changed content
`4961 → 5945` bytes) and **a new
`endar-spire/blueprints/items/weapons/blaster-rifle.toml` appeared at
`07:34`** — inside `endar-spire`, the fixture I was told not to touch and was
actively testing against.

**Neither was me.** They line up with `Lodestar 70a1107` *(`PT-1452`, the item
blueprint)* and `BUILD 42`. **I am not filing this as a defect** — you were
doing your job as I was doing mine. **But my baseline diff no longer means what
it meant in report 001**, and if a Tester result ever looks impossible, this is
the first thing to check.

**None of my findings above depend on those files.** The wound and panel
results are geometry and save-file digests, and `second-fight` was created at
`07:23`, before the regeneration.

---

## Data I leave behind

| | |
|---|---|
| `saves/vess-taran.sav` | now carries encounter outcomes |
| `saves/second-fight.sav` | **new this session** — the clean-room character |
| `saves/probe-walker.sav`, `packages/tester-probe/` | mine, from report 001 |

**Delete the `.sav` files and `tester-probe/` to reset.** I deleted nothing and
fixed nothing.
