# TEST 048 — a room nobody can enter, three sentences that can be false, and what only a clean package shows

**Built against:** Loom bundle `kernel_blob.bin` built **16:39**, from `908a412` —
the **same Loom binary as TEST 043–047**. **Not rebuilt.** Loom HEAD is now `776e42e`
and is untested by me. The app was not run this run; the app bundle is still the 16:11
one from `660134a` → Lodestar `9aa7382`.

**Instrument:** PID-scoped via `$!` + `pgrep -P` — **not `pgrep -n`**, which handed me
Coder's process in TEST 047. Four Looms (`561250`, `563677`, `564722`, and one earlier),
all killed by PID; Coder's `517968` survived every one.

⚠ **And a second instrument correction.** My hardcoded window coordinates broke: Loom
opened at **320,171** this run, not 360,192, and my first open silently did nothing.
I now read the geometry with `xdotool getwindowgeometry --shell` and compute every
click from it. **A coordinate that worked yesterday is not an instrument.**

⚠ **Nothing outside my own bed was written.** `endar-spire` + `base-rules`: 40 files
md5-summed before and after, `diff` empty. `taris-undercity`: read only, still Sep 7.
Save shelf: `diff -rq` clean — nothing was played.

---

## 1. How much fits in a room nobody can enter: everything, and it costs one fault — the wrong one

`a08-probe-orphan` — 8×6, declared in `[order].areas`, and **no connection in the
package targets it.** It holds an arrival (`from-nowhere`), two creatures, one of them
carrying `conversation = "dialogue/sentinel-challenge"`, and **a door out at 7,5.**
A room with an exit and no entrance.

**11 problems → 12.** ⚠ **And I predicted zero, and I was wrong, and the way I was
wrong is the finding.**

The one new fault is **not** about the room. Expanded, a08 itemises as:

    creatures      probe-warden.probe-orphan.02   3,3   ← RED
                   "probe-warden.probe-orphan.02" in "a08-probe-orphan" equips
                   "items/weapons/no-such-blaster" in slot "weapon_r_1", and
                   there is no item there.
                   probe-anvil.probe-orphan.03    5,2
    doorways       door.probe-orphan.01           7,5
    arrival points from-nowhere                   0,0

⚠⚠ **`equipmentMissing` — a fact about a NAME — fires inside a room no player can
reach. Every fact about POSITION stays silent.** I chose probe-warden without thinking
(it carries my long-standing dead-blaster fixture), and the accident drew the line
exactly:

| about a **name** | about a **position** |
|---|---|
| the creature's blaster does not exist → **reported** | the room cannot be entered → **silent** |
| | the arrival is landed on by nothing → **silent** |
| | the door leads out of a room with no way in → **silent** |

**So the weight of the gap is: an author can furnish a room completely, wire an exit
from it, and the only thing `verify` will say is that one creature's rifle is
missing.** Swap that creature and the count returns to 11 for a room that can never be
played.

⚠ **And the reasoning that leaves it silent is still sound** — `package_validate.dart:260`,
*"an area nothing leads to cannot be walked into, so saying it has no way out would be
a sentence that is false about it."* The habit that keeps every sentence true is the
habit that has no sentence for this. **There is an `areaHasNoWayOut` and no
`areaHasNoWayIn`**, and `PT-1505` made the manifest the roster, so an area in the
roster that nothing leads to is a declared thing nothing asks about.

⚠ **`taris-undercity` has one of these by accident and it is not a fixture**
(TEST 047): `a02-rakghoul-warren` is reachable by nothing, and that package's count is
**1, not 2**.

⚠ **One thing `_position` DOES do in an unreachable area** — it still runs. Only the
last clause is gated. `a09` below proves it: `landingNotStandable` fired in an area
nothing leads to.

---

## 2. Three sentences that name a premise that can be false — two of them made to fire

The brief asked whether `areaHasNoWayOut` is the only member whose sentence can be
false about its own case. **I read all seventeen and it is not.** Three, and I made
the two new ones fire rather than argue them.

### `landingNotStandable` — *"A door landing there puts a character inside it."*

    "a09-probe-wording" declares the arrival "walled-landing" at 5,0, and that
    square is wall — nobody can stand on it. A door landing there puts a
    character inside it.

⚠ **No door lands there. Nothing in the package lands on it at all.** The fault is
right — the arrival *is* in a wall — and the consequence it names cannot happen on this
board. It is the same shape as `areaHasNoWayOut`'s: a true finding explained by a
scenario that requires a thing the package does not have.

### `blueprintMissing` — *"It will be drawn and will not be present."*

    "ghost.probe-wording.01" in "a09-probe-wording" is placed from
    "characters/no-such-creature", and there is no blueprint there. It will be
    drawn and will not be present.

⚠ **`ghost.probe-wording.01` is `hidden = true`. It will NOT be drawn.** The sentence
is the member's whole justification — *"a creature was drawn and was not there"* — and
it describes the visible half of a placement that is not visible. Both are right about
the missing file and wrong about what the player sees.

**Both fired on demand: 12 problems → 14, exactly the two predicted, in
`a09-probe-wording`.**

### `areaHasNoWayOut` — *"a character who walks into it from another area"*

Already filed from `taris-undercity` in TEST 047, where the area is the **entry**:
nothing connects to it and you start there. Its second branch (*"a character who
arrives is stuck"*) is looser and survives.

### And one that is not false but breaks the file's own standard

⚠ **`areaFileMissing` and `areaUnreadable` share ONE sentence** —
*"The manifest lists "$id" but it cannot be read: ${e.reason}"* — chosen between by
`File(path).existsSync()`. Two members, one wording, and the wording does not say
which. `connectionUnreachable`'s own comment three hundred lines later sets the
opposite standard: *"the sentence says which of the two it is rather than one word for
both."* **`approach`'s two stalls are two sentences on purpose (TEST 044/045); these
two members are one.**

### The other thirteen

I checked every one. `duplicateArrivalName`, `blueprintUnreadable`, `equipmentMissing`
(both branches), `targetAreaUnknown`, `targetAreaUnreadable`, `landingPointUndeclared`,
`areaHasNoStandableSquare`, `connectionUnreachable`, `entryUndeclared`,
`entryAreaUnknown`, `requiredFieldMissing`, `referenceMissing` — **all state only what
they measured.** Two worth naming as *checked and clean* rather than skipped:

- **`equipmentMissing`'s roster branch** says *"It is authored and nothing places it"*,
  which would be false for a placed blueprint — and it is guarded three lines above:
  `if (placed.contains(rel)) continue;`, with the comment *"silence here is not a gap:
  it is the clause being true."* **The premise is enforced.**
- **`connectionUnreachable`'s** *"Every arrival this area declares is unstandable"*
  branch fires only when `seeds.isEmpty` at that point, which after the
  `arrivals.isEmpty` fallback means exactly that. **This is the one that was hiding
  itself when I found it in TEST 039, and `PT-1619` left it tight.**

---

## 3. What only a clean package shows

I have spent this whole thread inside a bed that has never had fewer than ten problems.
Opening `endar-spire` and `base-rules` showed four things I had never seen.

1. **The `verify` control.** A faulted package puts a **count** in the header —
   *"Tester Probe · 14 problems"*. A clean one puts **`verify`** there instead. They
   occupy the same slot, so **the control and the count are mutually exclusive**: you
   cannot re-run verify from the header of a package that has faults.
2. **The VERIFY dialog** — *"VERIFY / Endar Spire / No problems found."* with
   **Verify again** and **Close**. Three surfaces at once, none reachable from my bed.
3. ⚠⚠ **The package's PATH.** This is the one worth filing.

       loom_shell.dart:166   _status = 'opened ${p.name} ${p.version} — ${p.path}';
       loom_shell.dart:216   if (!r.ok) _status = '${_status.split(" — ").first} — '
                                 '${r.faults.length} problem…';

   The open writes the path and `_verify` **overwrites it with the count.** Observed:

       opened Endar Spire 0.1.0 — /home/aidan/.local/share/kotor-rpg/packages/endar-spire
       opened Base Rules 1.0.0 — /home/aidan/.local/share/kotor-rpg/packages/base-rules
       opened Tester Probe 0.1.0 — 14 problems

   ⚠ **An author whose package has faults cannot see which copy of it they opened** —
   and thirteen lines above, the same file says *"`PACKAGE-NAMING-01` makes the PATH the
   identity."* **The identity is dropped exactly when something is wrong**, which is
   when "am I editing the right copy?" is the question most worth answering. I have hit
   the underlying version of this all thread: three artifacts, and reading the wrong
   copy is this project's most expensive mistake.

4. **A tree with no paragraphs in it.** Every child in `endar-spire` is a one-line row —
   `sith-trooper.comm… 6,4`, `door.command-de… 7,2`, `aft 1,3`. In my bed each fault
   adds a wrapped four-to-six-line explanation *inside* the tree, so a03 and a04's notes
   alone cost about 180px and I had to scroll to reach a09 at all. ⚠ **The tree's
   vertical cost grows with the number of faults, so the more wrong a package is, the
   less of it you can see at once.**

---

## What I did not check

- Loom `776e42e`, app `47789fa`, Lodestar `e1a837c`. Not in either bundle. Untested.
- **Whether `verify` can be re-run on a faulted package by any other route** — a menu,
  a key. I only observed that the header slot holds the count instead.
- Whether `a08`'s count returns to exactly 11 with a clean-equipment creature. I read it
  off the tree's itemisation (one red row) rather than by re-running with a swap.
- The `hidden` placement in `a09` was never revealed in play — I did not run the app
  this run, so I did not confirm by eye that it is undrawn, only that the file says
  `hidden = true` and a04's hidden four have always been invisible on arrival.
- `taris-undercity` was not re-opened this run.

## State

- **`tester-probe` gained two fixture areas and now reports 14 problems, four of them
  mine on purpose.** New `areas/a08-probe-orphan.toml` (unreachable, furnished — adds 1,
  and that 1 is `equipmentMissing`, not a position fault) and
  `areas/a09-probe-wording.toml` (adds 2, both wording evidence). `package.toml`
  `[order].areas` gains both. Every file parses. Both areas carry loud
  **DO NOT "FIX" IT** comments naming what they prove, as `a07` does. Snapshots
  `PKG-T043/` … `PKG-T048/`.
- `endar-spire`, `base-rules`, `taris-undercity`: **untouched**, verified by md5 and mtime.
- Save shelf **unchanged** — nothing was played.
- The NWN install was not read or written.
- All my Looms killed by PID; Coder's `517968` survived.
