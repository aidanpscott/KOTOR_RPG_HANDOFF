# TEST 080 — the strongroom walked object by object: the menu, the tiers,
# the keyed door, the mine and the no-retry rule all behave. But EVERY
# object-verb skill check reads the character's rank as 0 — four skills on
# one character, while the passive look reads the same skill correctly

**Built against:** `run-app.sh` (always rebuilds). App started 00:42:15;
local `KOTOR-RPG-APP` HEAD at that moment was `ef66eb3` (00:30:55, *the
fixture is walked — and walking it found two real defects*). `df1ea93`
(*a picked lock survives the visit — door.unlocked, BUILD 182*) landed
00:54:54, **after** my build, and is not in it. Working tree clean.

`ef66eb3` records `lodestar` pin `2a9094c33a1d1e131d6dc95e82eac3747feca72e`
(checkout present); the lock has since been bumped to `fe74b174…` by the
later commit. `lens` `cc0fd1493313e9a529618473d46294f70955b940`.
`check_shelf.py` at session start: `✓ 25 rules files, all identical to
what the extracts generate`. App PID `149110` killed by PID, confirmed
gone.

**Character for the main pass:** "Talia Corvan", Human **Smuggler** —
chosen because Smuggler carries Awareness, Demolitions, Security and
Slicing as class skills, so one character could exercise every check in
the room. INT 18. **Awareness 4, Demolitions 4, Security 4, Slicing 4**,
all bought and all visible on the skills screen before Play.

---

## ⚠ THE FINDING — every object-verb check reads the rank as 0

Four different verbs, four different skills, one character who had rank 4
in each:

| verb | what the screen said |
|---|---|
| Open Lock (vault) | `open lock — d20 5 + **Security 0** = 5 vs 28 (heroic) · it holds` |
| Open Lock (footlocker) | `open lock — d20 20 + **Security 0** = 20 vs 18 (hard) · open` |
| Slice (console) | `slice — d20 8 + **Slicing 0** = 8 vs 15 (moderate) · it holds` |
| Search (footlocker) | `search — d20 16 + **Awareness 0** = 16 · nothing left in it` |
| Disarm (mine) | `disarm — d20 16 + **Demolitions 0** = 16 vs 20 (hard) · it is still live` |

**And the same character's Awareness reads correctly on the other path.**
On arrival the room said:

> `you notice mine.strongroom.01 — **14 against 12**`

14 is take-10 plus Awareness **4**. So the passive look reads the rank and
the context-menu verb does not — the same skill, two code paths, two
answers, on one character in one room. That is the shape this corpus
names most often, and it is why I am confident this is the product rather
than my character sheet.

**Impact, beyond the arithmetic:** every DC in this fixture is effectively
rolled at d20 flat. The console at 15 becomes a 30% one-shot, the
footlocker at 18 a 15% one-shot, and the mine's 20 a 5% one-shot — and
none of them may be retried. It also means I could not reach the terminal
screen (see below).

*(A second and third character were Soldiers who genuinely had no Slicing,
so their `Slicing 0` proves nothing — the evidence above is all from the
Smuggler.)*

---

## What behaves, object by object

- **(2,1) the mine — noticed, not disarmed, and it goes off.** Noticed on
  arrival (above). Disarm offered as **`Disarm (hard)`** and failed,
  leaving it **"it is still live"**. Walking in:
  `goes off — d20 18 = 18 vs 15 · 3 damage · 6 of 9 ⚠ 3 rounds, first only`
  — save made, half damage, 9→6 on the sidebar, **and the known
  first-round-only limitation is printed on screen rather than left for a
  reader to discover.** Spotting is not disarming: confirmed.
- **(4,1) the footlocker — Search and Open Lock at 18.** Menu:
  `Examine (Science)` · `Open Lock (hard)` · `Search (Awareness)`. Exactly
  the two verbs asked for, plus Examine. A natural 20 opened it despite
  the +0.
- **(6,1) the console — Slice at 15.** Menu: `Examine (Science)` ·
  `Slice (Slicing)`. The roll fired against 15 (moderate).
- **(8,1) the crate — Examine and nothing else.** Menu carried the single
  entry `Examine (Science)`, which is the fixture's "a thing you cannot
  use" said in verbs rather than a flag.
- **(9,1) the vault door — locked 28, out of reach.** `Open Lock (heroic)`;
  the roll ran and held. Out of reach for level 1 in the strict sense too:
  even with the rank read correctly the ceiling would be 24.
- **(9,3) the side door — keyed, and it never rolls.** In reach the menu
  reads `Examine (Science)` and, greyed, **`Open Lock ⚠ it takes the
  sith-keycard`** — the requirement named, no tier, no roll. That is
  "does not take Security at all — it says so instead of rolling",
  satisfied.

## The pre-named behaviours, all confirmed

- **No retry.** Second attempt on the vault door:
  `door.strongroom.05 — you have already tried this lock`.
- **Raw number and tier together.** Every roll line carries both, e.g.
  `= 5 vs 28 (heroic)`. Tiers were consistent across the room: 15
  moderate, 18 and 20 hard, 28 heroic.
- **Right-click opens the menu, left-click still walks** — used
  throughout; a left click with a menu open cancels rather than walking.
- **Out-of-reach is marked, not hidden**: from across the room entries
  read e.g. `Examine (Science) ⚠ 7 squares away`.

## ⚠ Smaller observation — the arrival square

The fixture puts arrival `back` at **(1,1)** and the brief says to arrive
there. A new game put me at **(0,0)**: one `Right` press took me to
`1, 0`, and the `back` marker was drawn one square down-right of where I
stood. If I had started on (1,1), that same press would have walked me
into the mine at (2,1). Consistent across all three runs. It may simply be
that a new game starts at the origin rather than at a named arrival —
naming it rather than calling it a defect.

## What I did not reach

- **The terminal screen.** It opens only on a passing Slice, and with
  Slicing read as 0 that is a 30% one-shot per character with no retry. I
  failed it three times across three fresh characters (8, 5 and 5 against
  15) and stopped there. So "two options on a pass" is **unverified** —
  and worth re-testing once the rank defect is fixed, when a Slicing-4
  character will pass it about half the time.
- Anything behind either door, the guard at (11,5), and `a02-vault`.

## State

- No fixture edits this session — `locked-and-trapped` is Coder's and I
  only walked it.
- Three throwaway saves created in that package, not cleaned up.
- App PID `149110` killed by PID, confirmed gone.
