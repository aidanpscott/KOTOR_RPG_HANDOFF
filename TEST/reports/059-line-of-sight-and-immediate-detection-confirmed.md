# TEST 059 — line of sight, immediate detection, and correcting myself mid-session

**Built against:** `run-app.sh` (always rebuilds). Three separate relaunches, one
per area under test, because `[entry]` is a package-level field and this build
only re-reads it on a fresh process — exiting to the library and reopening the
same running app was **not** enough (same shape as `TEST 054`'s "package arealist
needs a full re-open," one level stricter). Declaring each build precisely:

| Test | PID | exe mtime | KOTOR-RPG-APP HEAD at that mtime |
|---|---|---|---|
| a02-obstructed | `734625` | `13:56:57` | `acde619` (*PT-1686 — detection needs a line*) |
| a03-immediate | `740269`\* | `14:15:38` | `acde619`, same |
| a04-hidden-wall | `740269`\* | `14:23:04` | `cebb08e` (*PT-1694 + PT-1692 — a shot needs a line, and so does the find*), landed **while I was mid-session** |

\*Same PID, relaunched between a03 and a04 — the second launch rebuilt against a
newer HEAD than the first, which matters for §3 below.

Loom `e03f816` used only to `verify` the new areas (0 problems, both new areas),
not reopened for actual play. `pubspec.lock`'s Lodestar `resolved-ref`
`0eab8cc02ecdf364e63ecfc7bc13f5f87ad3406b`, unchanged, cached checkout present.

**Instrument:** PID-scoped via `run-app.sh`'s `exec`, three launches, all killed
by PID. Coder's Loom `517968` confirmed untouched throughout — checked before,
between, and after.

**Task:** build the fixture that actually exercises line-of-sight-gated
detection (nothing in the existing `ranged-detection` bed had a wall in it), and
confirm the fight-start immediate-detection fix with a player who wins
initiative against an in-range, undetected creature.

---

## Fixtures built

Extended `ranged-detection` (not a new package — same fixture family, same
shared `characters/corridor-guard` blueprint) with three new areas, switching
`[order].areas`/`[entry]` per test:

- **`a02-obstructed`** (12×3): a starter adjacent to the entry, a full-height
  wall at column 5 across rows 0–1, and a second guard at (9,0) — in range (9 ≤
  10) the entire time, on the far side of the wall. Row 2 carries no wall, so
  stepping down and across clears the line without a doorway.
- **`a03-immediate`** (10×3, no walls): a starter at (1,0), a second guard
  already at (6,0) — in range and in the clear from the moment the fight opens.
  Needs a player who can win initiative against a DEX-10 creature, so I built
  `Initiative Winner` at DEX 18.
- **`a04-hidden-wall`** (10×3): the same wall shape as a02, but one **hidden**
  creature at (7,0), stealth 10 — comfortably beaten by a 4-rank
  Alertness/Awareness build (total 14), so a find is the uncorrected case, not
  a lucky roll. Tests `_lookAround`, not `_detectAtRange`.

Loom's `verify` on both new areas: **No problems found.**

## 1. Line of sight blocks `_detectAtRange`, and resumes exactly where sight opens

Walked into `starter.obstructed.01` (adjacent, direct contact — always starts a
fight regardless of the faction/range gates). At fight open, the roster held
only the starter — `blocked.obstructed.02`, 9 squares away and still within the
default radius, did **not** join, even though the fight-start immediate-check
(§3 in `TEST 058`) now runs unconditionally on every `_begin`. Confirmed this is
sight, not range: I stayed on row 0 (the wall's row) for two full rounds, taking
hits, and it never joined.

Moved down to row 2 (no wall) and right, still short of column 5 — **still not
joined**, at distance 8 with an open-looking row under me. Continued right, past
column 5, to (7,2):

    inrange.immediate.02 →  [not applicable here — a02's own guard:]
    blocked.obstructed.02          noticing
    16 of 16

Joined the instant the line cleared, marked ` noticing`, same amber label and
same skip-a-round/act-next-round behaviour already confirmed in `TEST 058` —
this test adds the sight gate on top of a mechanic already known to work, rather
than re-proving the delay itself.

## 2. Fight-start immediate detection, with the player actually winning initiative

Built `Initiative Winner`, DEX 18, and walked into `starter.immediate.01`. The
log named both rolls on the very first frame:

    initiative — Initiative Winner 9 · starter.immediate.01 8

**The player won, 9 to 8** — the exact case `PT-1683`'s /`acde619`'s own
comment names as the one the old bug needed (*"the droids win initiative... the
gap was invisible for exactly the fights the tests could start"*). And in that
same first frame, before I had taken any action:

    turn order              in this fight
      inrange.immediate.02   16
    ▶ Initiative Winner       9
    › starter.immediate.01    8

    starter.immediate.01     16 of 16
    inrange.immediate.02  noticing   16 of 16

`inrange.immediate.02` — 6 squares away, in the clear, never touched — was
already in the roster, marked `noticing`, despite topping the initiative order.
Ending my turn ran the starter's attack and then, at the round boundary,
`inrange.immediate.02`'s first real turn (it closed 5 squares and swung, and
missed) — confirming both halves in one sequence: detected on arrival, not a
round late; and still correctly held to its own first-turn skip once detected.

## 3. ⚠⚠ Correcting myself: `PT-1692` was NOT built when I planned this, and IS now

I want to be precise about the timeline rather than just report the final
state. When I read `_lookAround` (`play_screen.dart:416`) to plan this fixture,
it had **no** `canSee` call anywhere in it — only `_detectAtRange` had gained
one, in `acde619`. I built `a04-hidden-wall` fully expecting to confirm a real
gap: a hidden, low-stealth creature found through a wall, matching the letter of
`_lookAround`'s source at the time.

By the time I actually played it, `cebb08e — PT-1694 + PT-1692 — a shot needs a
line, and so does the find` had landed (`14:03:38`, mid-session) and closed
exactly that gap — its own message says so directly: *"PT-1692 closes the
find-on-approach gap I named and declined to fix without authorisation."* I
relaunched between a03 and a04, so the a04 binary already carried the fix.

**What I actually observed matches the fix, not the gap I'd planned to find**:
approaching `silent.hiddenwall.01` (stealth 10, distance 7 from spawn — well
within range, total 14 beats it outright) along the walled row produced **no**
notice message and **no** reveal on the board, across three separate steps
getting closer (distance 7 → 6 → 3) while the wall stood between us. Only once
I went around via row 2 and cleared the wall's column did it fire, staying
revealed from then on. ⚠ **And it does not settle behind the wall** — the
commit's own words, and I confirmed it structurally: `_settled` would have
permanently frozen a wrong answer at distance 7 if the check had run and failed
there; instead it kept re-asking every step until sight actually opened, which
is what let a single approach path demonstrate both halves (blocked, then
found) without needing a second character.

I'm reporting this as a **build-timing correction**, not a defect: the brief
that sent me to build this bed was accurate about *what the fixture should
test*, momentarily inaccurate about *whether the code existed yet*, and correct
again by the time I pressed a key. Worth having on record precisely because the
next person reading this shouldn't have to re-derive which commit closed it.

---

## What I did not check

- `PT-1694`'s own half (*"a shot needs a line"* — ranged attacks, not
  detection, respecting sight) — out of scope for a detection-fixture brief,
  not touched.
- Whether `_settled`'s not-settling-behind-a-wall behavior also holds for
  `_detectAtRange`'s reinforcement path, or whether that one settles once
  admitted and simply never re-asks a creature already in the encounter —
  didn't have a case in this session where a joined-but-still-blocked
  distinction mattered (once `blocked.obstructed.02` had clear sight, it joined
  immediately and stayed joined).
- The diagonal-corner permissiveness `canSee`'s own doc comment describes
  ("two walls meeting at a diagonal do not seal the diagonal") — my wall is a
  single straight segment; I didn't build an L-shaped corner to test that
  specific claim.

## State

- **`ranged-detection` gained three areas** (`a02-obstructed`,
  `a03-immediate`, `a04-hidden-wall`), all listed in `[order].areas`, `[entry]`
  reset to `a01-corridor` afterward — the fixture's original default, not left
  pointed at whichever area I tested last. Three new saves: `line-tester.sav`,
  `initiative-winner.sav`, `wall-ear.sav` — the package had one save
  (`cold-approach.sav`, from `TEST 058`) before this session.
- No other package touched — `tester-probe`, `two-enemies`, `mixed-faction`,
  `endar-spire`, `base-rules`, `taris-undercity` all confirmed untouched by
  mtime.
- The NWN install was not read or written.
- All three app processes killed by PID; Coder's Loom `517968` untouched —
  checked before, between, and after each relaunch.
