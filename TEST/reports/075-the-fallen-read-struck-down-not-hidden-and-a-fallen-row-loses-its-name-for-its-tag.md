# TEST 075 — PT-1846 confirmed live: a fallen combatant's row reads
# "struck down" rather than "hidden", with the fight still running —
# and one thing found beside it: on falling, the row's label changes from
# the creature's NAME to its raw TAG

**Built against:** `run-app.sh` (always rebuilds). App process started
12:59:44; local `KOTOR-RPG-APP` HEAD `d2d28d0` (12:50:55, *PT-1846: the
fallen say so in their own words*) — the commit under test, and still the
tip when I finished, so no drift this session. `pubspec.lock` pins
(`ref: main`, floating): `lodestar`
`17bba42abe4f40940e78c06d848d7e4f1700544d`, `lens`
`e79bc066233fabc7776c8b94737029646d762e6e`, both confirmed present as
checkouts. `check_shelf.py` at session start: `✓ 25 rules files, all
identical to what the extracts generate`.

App PID `1250879` killed by PID, confirmed gone. Coder's Loom (`12445`/
`12443`) checked running, untouched, before and after.

**Character:** "Jorel Sarn", Human Soldier, **STR 18**, Hunter profession
taking the melee upgrade (**Long Sword**, auto-selected as the single
alternative) — chosen specifically so a 16-vitality enemy could be
dropped in a blow or two while a second enemy kept the fight alive. That
last part matters: the commit notes that killing the *only* enemy ends the
fight and the corpse loses its row entirely, so the window under test only
exists with another enemy still standing. `companion-fixture`'s corridor
gives exactly that — `starter` (16 vitality) plus `chaser` (60).

---

## The fallen row reads "struck down" — CONFIRMED

Started the corridor fight and struck `starter.corridor.01` down while
`chaser.corridor.03` was still up at 52 of 60, so the fight continued and
the row survived to be read. The row:

**`starter.corridor.01` / `struck down` / `0 of 16`**

- The status line reads **`struck down`** — the product's own phrase, the
  one `_condition` already uses when the player reaches zero.
- The word **`hidden` does not appear** on the row, which is the defect
  PT-1846 set out to fix: the sidebar was asking the board's not-drawn set
  (`_concealed`, which carries the fallen) a question about a creature.
- The vitality bar is drained and the row stays in the list for as long as
  the fight runs.
- The corpse is **not drawn on the board** — correct and unchanged; the
  board's answer is still *do not paint this*.

So the display language is now separated from the not-drawn mechanism,
which is what the ruling asked for, and the membership stays shared.

## ⚠ Found beside it: a fallen row loses its name and shows its tag

Same row, same combatant, same fight, two screenshots minutes apart:

| when | what the row says |
|---|---|
| alive, at 2 of 16 | **`Starter`** · `2 of 16` |
| struck down | **`starter.corridor.01`** · `struck down` · `0 of 16` |

While it was alive the row carried the creature's display name; the moment
it fell, the label became the raw placement tag. `PT-1795` ruled on
exactly this shape — *"`PT-1331` makes the tag the identity and a tag is
not what a person reads"* — and `PT-1833` re-stated it when the roster
became a second source of rows. It holds for the living and does not hold
for the fallen.

**I am not asserting the mechanism.** The obvious guess — that the fallen
drop out of `_here`, so `placed[h]?.name` falls through to the tag — does
not survive a look at the source: `_rememberWhereEverythingStood` iterates
`_here` and *explicitly skips* fallen tags, which only makes sense if they
are still in it. So something else is producing the fallback and I did not
chase it further. The observation is solid; the cause is Coder's to find.

Worth noting it is the same class of thing PT-1846 just fixed one row
over: a row about a creature answering with a value that belongs to the
board's bookkeeping rather than to the person.

---

## What I did not check

- **The party-member case.** The ask allowed either ("kill a party member
  *or* watch an enemy fall") and I took the enemy. I did try for the
  companion: backed off and ran ~20 rounds letting `chaser` work on
  `Mate`, and she went 60 → 35 while taking `chaser` from 60 → 31 — she
  was winning, and grinding her to zero was going to cost many more
  rounds than the finding was worth. So whether a fallen **companion's**
  row also reads `struck down`, and whether it also loses its name, is
  untested. Given the name fallback chain differs for party members
  (`_away` sits between `placed` and the tag), the second half of that is
  a genuinely open question rather than an assumed duplicate.
- The **player's own** row on being struck down — would have ended the
  session's fight, and was not asked for.
- Whether `struck down` and the enemy-inversion treatment interact
  correctly on the same row (the fallen row kept the red, bar-above
  enemy layout, which looked right, but I did not check it against the
  PT-1133 lock line by line).

## State

- No package touched this session — confirmed by mtime; `companion-fixture`
  carries the same files as prior sessions, including the `a01-corridor`
  contents order restored at the end of TEST 074.
- One save created ("Jorel Sarn"), left mid-fight, not cleaned up —
  ordinary Tester artifact.
- App PID `1250879` killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) checked running, untouched, before and after.
