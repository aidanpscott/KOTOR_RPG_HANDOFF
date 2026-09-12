# TEST 071 — BUILD 158's three party-directed sidebar verbs (Wait here,
# Follow/regroup, Trade/give item) driven live: the standing order DOES
# survive a save (confirmed twice, including a fully killed-and-relaunched
# process) — a data-only fix (PT-1832) that had already shipped to the
# shelf when the app-repo commit documenting the gap as still open, plus
# regroup and the named trade refusal, both clean

**Worth reading before the results:** the task description said BUILD 158
"landed... a real save-persistence fix" and asked me to confirm Wait-here
survives a reload as "the exact bug that just got fixed." Reading the
actual app-repo commit that shipped the three verbs (`8219d52`, *PT-1122:
solo mode on the sidebar*) said the **opposite**: its own message reads
*"⚠⚠ THE ORDER DOES NOT SURVIVE A SAVE, AND THAT IS ASSERTED RATHER THAN
COMMENTED"*, naming `party.waiting`/`party.following` as undeclared in
`EVENT-KINDS-01` and shipping a test (`emitted_kinds_test.dart`) written
to **fail the day that gap closed** — i.e. still failing, by design, as of
that commit. That's a real discrepancy between what I was told and what
the source said, so I drove the save/reload live rather than trust either
side, and dug into *why* the two disagreed once I had an answer.

**What was actually going on:** the persistence gap was a **shelf-data**
gap, not an app-code gap — `_persist` has always filtered by
`campaignKinds`, read live from the installed shelf's
`event_kinds.toml`, not a list baked into the git-committed app. Coder
shipped the data fix (`PT-1832`: declaring `party.waiting` and
`party.following` at `lifetime = "campaign"` in the shelf) **before**
committing the matching app-repo test update — so by the time I ran
`check_shelf.py` at the start of this session (clean, `25 rules files,
all identical to what the extracts generate`), the fix was already live
on disk, even though `git log` in `KOTOR-RPG-APP` still showed `8219d52`
(the commit asserting the gap as open) as the tip. The app-repo commit
that formalizes this (`7f3ae17`, *PT-1832: the debt is paid — the
standing order survives a save*, deleting the pinned-failure test and
adding real persistence assertions) landed at 10:24:58 — a few minutes
**after** both of my test builds (10:12:48 and 10:23:19) — so neither of
my builds' `git log` included it, but both correctly exercised the
already-shipped shelf fix at runtime. Confirmed by reading `7f3ae17`'s
diff and the shelf's own `event_kinds.toml`, which carries the exact note
*"PT-1832. Standing orders (Wait here / Follow-regroup) did not survive a
save until declared."*

**Built against:** `run-app.sh` (always rebuilds), two processes this
session:
- First: PID `140338`, launched 10:12:48. Local `KOTOR-RPG-APP` HEAD at
  launch: `8219d52` (09:55:51, *PT-1122*) — `7f3ae17` did not exist yet.
- Second (used for the definitive reload test): PID `144053`, fully
  killed-and-relaunched from a cold process start at 10:23:19, HEAD still
  `8219d52` at that point (`7f3ae17` landed 10:24:58, after this build
  too).
- `pubspec.lock`'s `lodestar` pin (`ref: main`) resolved to
  `3b7e03892664796b7649b42e9d2cf70c1f3eb6e6` for both builds, confirmed
  present as an actual checkout at
  `~/.pub-cache/git/Lodestar-3b7e03892664796b7649b42e9d2cf70c1f3eb6e6`.
- `check_shelf.py` run at session start: `✓ 25 rules files, all identical
  to what the extracts generate` — already reflecting `PT-1832`'s shelf
  change, confirmed by grepping the installed
  `base-rules/rules/event_kinds.toml` directly for the two rows (present,
  `lifetime = "campaign"`, carrying the `PT-1832` note verbatim).

Both app PIDs killed by PID, confirmed gone. Coder's Loom (`12445`/
`12443`) checked running, untouched, before and after.

---

## 1. Wait here survives a save — CONFIRMED, twice

Built "Sarn Ordo" (Human Soldier, Merchant backstory — profession choice
didn't matter for this test) through chargen to `Play` in
`companion-fixture`'s `a01-corridor`, alongside `Mate`. In exploration,
Mate's row showed **"Wait here"** and **"Trade / give item"** (not
"Follow / regroup" — correctly filtered out, since she's already
following and offering it would be a button that does nothing, per
`§3a`'s mutual-exclusivity rule).

Clicked **Wait here**: status line read **"Mate will wait here"**, her
row updated to **"Soldier · 1 · holding position"**, and the verb list
flipped to **Follow / regroup** / **Trade / give item**. Walked to the
door at `(9,1)` and crossed into `a02-second-room` — the game
autosaved (`"Second Room — arrived at landing · saved"`), and Mate
correctly did **not** follow (she's holding a01-corridor, not this room —
the documented "same rule, not an exception" case).

**First reload check** (same process, PID `140338`): pressed Escape →
Load Game → loaded the "Sarn Ordo" save from the list. Landed back in
`a02-second-room` with only Sarn Ordo present. Walked back through the
door into `a01-corridor` — **Mate's row still read "Soldier · 1 ·
holding position"**, same verb set as before the save.

**Second reload check, to remove any doubt this was a still-live
in-memory session** (a real concern given Escape only opens an in-app
menu): killed PID `140338` outright, confirmed gone via `ps -p`,
relaunched via `run-app.sh` as a **fully fresh process** (PID `144053`),
opened `companion-fixture`, went straight to Load Game (`15 saves` shown,
matching the count from the killed process — genuinely reading from
disk), loaded "Sarn Ordo · 3 minutes ago". Landed in `a02-second-room`,
walked back through the door — **Mate's row again read "holding
position"**, identical to before. The standing order survived a
cold-process save/reload cycle.

## 2. Follow / regroup — CONFIRMED

From the holding state above, clicked **Follow / regroup**: status line
read **"Mate is with you again"**, her row's "holding position" text
disappeared, verb list flipped back to **Wait here** / **Trade / give
item**. Moved the player one step — no errors, party remained intact,
confirming she resumes following rather than being stuck or duplicated.

## 3. Trade / give item — named refusal, not silent failure — CONFIRMED

Clicked **Trade / give item** on Mate's row (still present in the verb
list throughout, never hidden or disabled): status line read **"there is
nowhere to trade from yet — a pack needs a screen"** — the exact refusal
text named in `play_screen.dart`'s `_partyVerb`, naming the missing half
(`§2`'s character screen) rather than doing nothing or dropping the verb
from the menu. Matches the task's ask precisely: a clear, specific reason
rather than a silent no-op.

---

## What I did not check

- Whether `Wait here` on a companion who is **not** in the current room
  (already elsewhere) behaves per the `p == null` guard in `_partyVerb`
  (*"$subject is not here to be told"*) — only tested with Mate present.
- Multiple companions holding different rooms simultaneously.
- Trade/give item's refusal for any companion other than Mate — same code
  path, not independently re-driven.
- Any UI state during an active fight (`onVerb` is `null` in combat,
  hiding all party-directed verbs per the diff — read in source, not
  re-confirmed live this session since Task B/069 already drove combat
  sidebar rows).

## An aside, not investigated further

Sarn Ordo's status bar repeatedly showed **"1 rule about this character
not checked"** throughout this session, on both builds. Didn't chase it —
this save also carries the pre-existing, already-reported `equips
items/weapons/blaster-rifle, which will not open` gap from
`companion-fixture` (visible in the same status line, unchanged since
TEST 069/070), which looks like the likely source. Flagging only so it
isn't mistaken for something this task touched.

## State

- `companion-fixture` (mine) — no files added or changed this session;
  confirmed by mtime, same five weapon-item blueprints and `mate.toml` as
  prior sessions.
- One new save created this session ("Sarn Ordo"), reached `Play`,
  crossed the door twice, reloaded twice — not cleaned up, ordinary
  Tester artifact.
- Two app PIDs (`140338`, `144053`) killed by PID, both confirmed gone.
  Coder's Loom (`12445`/`12443`) checked running, untouched, before and
  after.
- `check_shelf.py` run at session start: clean, and independently
  confirmed (by reading `event_kinds.toml` directly) that it already
  carried `PT-1832`'s two new rows before either build in this session.
