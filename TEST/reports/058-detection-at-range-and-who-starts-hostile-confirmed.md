# TEST 058 — detection at range and who starts hostile, both confirmed, and my own bug is fixed

**Built against:** `run-app.sh` / `run-loom.sh` (always rebuild). App tree/bundle
at `0c91428` (*PT-1686 + PT-1687 — detection at range, and who starts hostile*),
PID `722948`, exe mtime `13:12:37` — after the commit (`13:03:36`), confirmed the
right binary. Loom tree at `e03f816` (*repin lodestar — PT-1686's Encounter.joins
and PT-1687's factions*), used only for the two `verify` passes recorded in the
standby report, not reopened this run. `pubspec.lock`'s Lodestar `resolved-ref`
is `0eab8cc02ecdf364e63ecfc7bc13f5f87ad3406b`, cached checkout present.

**Instrument:** PID-scoped via `run-app.sh`'s `exec`. App `722948`, killed by PID.
Coder's Loom `517968` confirmed untouched before and after — no app of Coder's was
running to check against.

**Task:** run the two fixtures prepped on standby against the landed builds.
Confirm detection at range as a reinforcement-only mechanic (the fresh-fight-from-
range path is deliberately not built), and confirm the corrected faction premise —
the hostile Sith Raider joins by contact, the same-faction Republic Trooper does
not.

---

## 1. Mixed faction (`PT-1687`) — confirmed exactly as briefed

Built `Bystander Check` (Human Soldier, 13s across) in the `mixed-faction`
package. Walked directly into `hostile.mixed.01` (the Sith Raider, adjacent to
both the player and the Republic Trooper). The fight opened:

    turn order          in this fight
    › mixed.01            8
    ▶ Bystander Check     6

    hostile.mixed.01      16 of 16

**The Republic Trooper never appears in the roster at all** — not marked hidden,
not marked anything, simply never joined. On the board it stayed exactly where it
was placed, one square below the fight, undisturbed. Confirmed across three
rounds (I hit the Sith Raider twice, it hit back once and missed once) — the
trooper's absence from the roster held the whole time; nothing about combat
continuing pulled it in retroactively. This is `_alsoInContact`'s `_wouldFight`
gate working precisely as `PT-1687` describes: same faction as the package
(`Republic` on both sides) resolves to `Hostility.notHostile`, and a bystander
that would not fight does not join a fight it is merely standing next to.

I did not need to kill anything or resolve the fight to answer the question the
brief asked — the join-or-not decision is made once, at the moment contact
starts the fight, and I confirmed it stays that way for as long as the fight
runs.

## 2. Detection at range (`PT-1686`) — both halves, confirmed precisely

Built a second character, `Cold Approach`, in the `ranged-detection` package.

### 2a. Cold approach — confirmed to do nothing, exactly as told to expect

Bypassed `starter.ranged.01` entirely along row 1, walking toward
`distant.ranged.02` with no fight ever open. Closed all the way to **diagonal
adjacency** — `(11,1)` to its `(12,0)`, the single closest square short of
stepping onto it — and held there:

    a01-corridor · 11, 1        [no roster panel, no "in this fight" header,
                                 no combat log line, nothing]

Confirmed at the tightest distance the fixture allows without an actual step
onto the creature's square. Nothing happened, which is what I was told to expect
and what reading `_detectAtRange`'s own early return (`if (f == null …) return;`)
already predicted before I ran it — the reinforcement path has no cold-start
case and none was built. Stating this as confirmed rather than assumed, per the
brief's own ask.

### 2b. Reinforcement into a running fight — confirmed, including the delay

Walked back and stepped into `starter.ranged.01` directly, opening a fight at
distance 11 from `distant.ranged.02` (outside the default 10-square radius — it
did not join at the start). Used my turn's move to close three squares along the
empty row:

    a01-corridor · 4, 1

    turn order              in this fight
    › ranged.02              16
      ranged.01               8
    ▶ Cold Approach           6

    starter.ranged.01        16 of 16
    distant.ranged.02  noticing   16 of 16

**Distance at that point was 8, inside the radius — and it joined mid-move, not
at the start of my turn.** The amber ` noticing` label is exactly
`RosterRow.waiting`/`Fight.waiting` rendered, and the turn order shows it slotted
by its own initiative (16, above everyone) rather than appended at the end.

Ended my turn. `starter.ranged.01` acted (closed 2 squares, hit for 3).
`distant.ranged.02` did **not** act, despite sitting at the front of the turn
order with the highest initiative — confirmed by the log carrying only the
starter's line and the roster showing `distant.ranged.02` still undamaged.
⚠⚠ **And the label was already gone by the time it was my turn again** — the
round boundary that unmarks `waiting` had already passed, which is `advance()`'s
own documented shape (`waiting.clear()` fires at the round wrap, and the newly
un-marked combatant can be reached in the same pass if the wrap lands on its
slot) rather than a separate, later event. Ended my turn once more: this time
`distant.ranged.02` moved — closed to stand adjacent to me — using the turn it
was denied the round it joined. It did not get to swing before the fight ended
(see §3), so I did not get a hit-roll from it specifically, but the sequence
already answers the question asked: **marked on arrival, skipped that round,
active starting the round after — confirmed, not assumed.**

## 3. ⚠⚠ Unplanned, but exactly on point: my own `TEST 057` finding is fixed

`starter.ranged.01`'s next hit killed `Cold Approach` outright. Instead of the
dead-player-keeps-moving state I reported in `TEST 057`, the screen showed:

    Your entire party has been killed.
    Anyone who goes down is revived when a battle ends. Nobody is left standing,
    so there is no end of battle.
    the newest save is this one — it already records the defeat
    [ Go to Load Game List ]  [ Main Menu ]

This is `PT-1683`'s fix (*"a wipe ends the fight, and the detection was already
right… TEST 057's dead player who kept moving"*) — I read the commit before
testing and got to watch it actually fire, unprompted, in the middle of an
unrelated test. Confirmed: no free movement, no stuck panel, a clean party-wipe
screen naming what happened and where the save landed. I did not go looking for
this; it is worth recording as confirmed anyway, since a fix for something *I*
found is exactly the kind of thing this role should verify rather than assume
closed.

⚠ **Not fully explored**: whether "Continue" being available afterward (the
title screen offered it, not greyed out) resumes into the recorded defeat state
sensibly or does something stranger — out of scope for this run, named rather
than chased.

---

## What I did not check

- Whether `distant.ranged.02` actually lands a hit once its delayed turn
  finally arrives — the fight ended (my death) one exchange before I'd have seen
  it. The join-and-delay mechanic is confirmed either way; the attack roll itself
  is not.
- The `Continue`-after-party-wipe path, noted above.
- Whether a THIRD creature at a THIRD distance would compound correctly (two
  latecomers joining on different rounds) — this fixture only has one of each,
  by design; not asked for.
- Nesting in `startsHostile` (a subfaction not being hostile to its parent) —
  explicitly named as unbuilt in `PT-1687`'s own source comment, not this
  fixture's concern.

## State

- **`mixed-faction` unchanged** — no edits, played only. One new save,
  `bystander-check.sav` (13:22), the fixture had none before.
- **`ranged-detection` unchanged** — no edits, played only. One new save,
  `cold-approach.sav` (13:32), recording the party wipe per the game's own
  message. The fixture had none before.
- No other package touched this session — `tester-probe`, `two-enemies`,
  `endar-spire`, `base-rules`, `taris-undercity` all confirmed untouched by
  mtime.
- The NWN install was not read or written.
- My app process killed by PID; Coder's Loom `517968` untouched — confirmed
  before and after, no other process of Coder's was running to disturb.
