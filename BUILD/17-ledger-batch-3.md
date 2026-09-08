# 17 · Ledger batch 3 — Continue and Load Game light up

**`KOTOR-RPG-APP` `d1a2c05` · `Lodestar` `fc4fb3`.** 176 app tests, 109
Lodestar tests, analyze clean.

---

## ⚠⚠ THE WHOLE LOOP RUNS

> Make a character · **Play** · quit · **reopen the app** · **Continue** · and
> be the same character in the same place.

**The first time anything in this project has survived a restart.** The test
pumps a fresh `App` against the same root — what a restart does — and the
character comes back off the disk.

**And the two buttons have said "no saves" under them since the first screen
this project ever built.** They do not any more.

---

## What each piece does

| | |
|---|---|
| **Play writes the save** | One file per character per campaign, named for the character's **id** — `§5·0`, `PT-1416`. `deriveId` does the naming, which is `PACKAGE-NAMING-01`'s shape transferred |
| **Continue opens the most recent** | **and the disk decides which.** *"Which save is most recent is not a fact about the save."* The header gains nothing; `mostRecentHandle` asks the filesystem, exactly as `PT-1358` settled it one object over |
| **Load Game lists them** | over the menu, not as a new screen — the shape the re-lock warning already uses. Each row shows the save's **rules version**, the only fact worth showing that is about the save rather than about the disk |

---

## ⚠ `§5`'s five steps — three built, two not, and why

    1  resolve packages         ⚠ NOT BUILT, AND NOT NEEDED HERE
    2  latest valid snapshot    ⚠ NOT BUILT, AND NOT NEEDED AT ALL YET
    3  replay events            ✓
    4  validate the projection  ✓
    5  open                     ✓

**Step 1 is already done by the time this runs.** The menu a save is opened
from *belongs to a package* — it was opened to reach the menu. A save carried
between packages would need it, and `PT-1415` says a character is not portable
between packages, so nothing produces that case.

**Step 2 has nothing to take.** `PT-1327` makes a snapshot **a cache** —
delete every one and lose nothing — and none is written. Replay of a 26-event
log is not a problem worth caching.

---

## ⚠ Validation runs, refuses loudly, and says what it could not check

A save naming a species this package does not have **will not open**, and the
panel says which. Tested with exactly the character `PT-1412` will produce for
real when a package closes a species.

**⚠ And three of `§4`'s twelve rules cannot be checked at all**, so they are
**returned rather than skipped** — a validator that quietly checks nine of
twelve reports *legal* for a character it never examined. **The play HUD
carries `N rules unchecked` beside the character's name.**

| Rule | Why not |
|---|---|
| skill ranks ≤ cap **for their derived aptitude** | only the with-aptitude ceiling is enforced. The aptitude set comes from **five sources** (`§3`) and that derivation is not built, so rank 3 on a skill with no aptitude passes |
| granted feats appear in the class schedule | **no class-to-granted-feat map is extracted.** `FEATS-LIBRARY-01 §5a`'s `Class \| Ladder \| Caps at` table was skipped by shape at batch 3c, and the granted records carry no class |
| chosen feats' prerequisites are met | **`feats.json` carries no prerequisite field.** Chain order is implied by `is_chain_head` and nothing states a prerequisite |

---

## ⚠ "The same place" means the entry area, and the vocabulary is why

**Position is not in the log, and `EVENT-KINDS-01` says it should not be.**
`character.moved` and `area.entered` are both **`session`** lifetime — and
`SAVE-LOAD-01 §4` gives lifetimes their job: *"they decide what is written in
the first place."*

**So a save cannot know where you were standing, by the vocabulary's own
rules.** Continue lands in the package's entry area. That is correct today and
it is a decision someone should make deliberately before it is not: **a player
who walks to the second area, quits, and continues arrives back at the first.**

Reported rather than changed — the fix is a lifetime ruling, not code.

---

## Two things the loop found, both mine, both from this batch

- **The play HUD overflowed by 0.311 pixels** the first time a real character
  name reached it. No capture had shown it because no capture had a character.
- **The test hung** until each body was wrapped in **one** `runAsync`. The app
  reads the disk in `initState` on nearly every screen, so a pumped frame
  outside the real-async zone waits on a future that never completes.

---

## What was NOT built

**No snapshots** — a cache, and deleting every one must lose nothing. **No
multiplayer.** **No play beyond what exists**; walking between two areas is
where this lands, and it is where it landed before.

**No save slots.** `§5·0` describes one as **a point in the log**, with a
**rewind event** in `step-reopened`'s shape. Nothing takes a slot, so nothing
rewinds — **specified, not built.**

**No `Save Game`.** `PT-1255` keeps it on the menu; Play writes the save and
nothing else does. **A character who walks to the second area and quits loses
nothing, because nothing about that walk was ever in the log.**
