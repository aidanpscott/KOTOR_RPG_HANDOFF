# TEST 073 — Hide (key `s`, PT-1108/PT-1843) driven live: the roll, the
# dedicated indicator, zero-stat watchers who still catch you, and reveal
# on a miss all CONFIRMED — but a REFUSED swing reveals you too, which is
# the one thing the commit says it must not do

**Built against:** `run-app.sh` (always rebuilds). App process started
11:55:02; local `KOTOR-RPG-APP` HEAD at that moment was `7c3d00a`
(11:39:25, *PT-1108/PT-1843: Hide is an Action a player can press*) — the
commit under test. `b7e16cf` (12:00:57, *PT-1841: a room is as you left
it*) landed **after** my build and is not in it, which is right: that's
the next slice, not this one. `pubspec.lock` pins (`ref: main`, floating —
same caveat as TEST 071): `lodestar` `17bba42abe4f40940e78c06d848d7e4f1700544d`
and `lens` `e79bc066233fabc7776c8b94737029646d762e6e`, both confirmed
present as checkouts; the lodestar checkout was fetched 11:47:09, eight
minutes before my build, so that is the copy that compiled.
`check_shelf.py` at session start: `✓ 25 rules files, all identical to
what the extracts generate`.

App PID `177282` killed by PID, confirmed gone. Coder's Loom (`12445`/
`12443`) checked running, untouched, before and after.

**Character:** "Oreth Lhent", Human Soldier, **Stealth rank 2** — Stealth
is not a Soldier class skill, so it costs 2/rank and caps at 2, which is
the most a level-1 Soldier can carry. Watchers: `companion-fixture`'s
`starter`, `chaser` and `mate.corridor.02` — and **no installed blueprint
in any package declares `[skills]`**, checked by grep, so every watcher
in this fight is rank 0 on both Awareness and Alertness. That makes this
fixture the "poor Awareness" case by default, which turned out to matter
a lot (§2).

---

## 1. `s` rolls, hides, and says so on its own line — CONFIRMED

Outside a fight, `s` refuses out loud: **"there is nobody here to hide
from"**. Inside one, on my turn, it rolls and reports the derivation both
ways — **"hidden — 4 beat 2"**, **"hidden — 19 beat 13"** on successes,
**"seen — your 18 against their 18"** on failures. Pressing it while
already hidden refuses with **"you are already hidden"** and — worth
noting — does *not* spend the Action, since the pip stayed lit.

On success the sidebar row gained a **dedicated `hidden` line of its
own**, in accent colour, bold, letter-spaced, sitting directly under the
name and above `Soldier · 1` — not a dimmed word folded into the
dot-joined status line below. That is PT-1108's *"real, clearly visible
indicator"* rather than the easy-to-miss checkbox the ruling rejects by
name. The state also survived movement and the enemy's turns: I walked
five squares and sat through a full enemy round still reading `hidden`.

## 2. A zero-stat watcher really does catch you — CONFIRMED, repeatedly

This is the case the commit's own fixture note is about (*"a thug written
with awareness = -20 and no alertness LOOKS blind and is not… ZERO IS
STILL A ROLL"*), and with every watcher here at rank 0 it fired constantly.
Failures observed, all against creatures with no declared skills at all:

- **"seen — your 18 against their 18"** — a tie, and **the tie goes to the
  watcher**. My 18 was a good roll and it still lost.
- **"seen — your 14 against their 19"**, **"your 5 against their 16"**,
  **"your 3 against their 19"**, **"your 11 against their 20"**,
  **"your 6 against their 6"** (another tie), **"your 4 against their 5"**.

So a rank-0 creature is emphatically not blind: it rolls a full d20, wins
ties, and with three of them opposing at once a Stealth-2 player fails far
more often than not. Nothing here reads as broken — it reads as the rule
working exactly as the commit describes.

## 3. Swinging breaks cover on a MISS — CONFIRMED

Hidden, adjacent, with an Action in hand, I attacked and rolled:

**`unarmed · rolled 11 — d20 11 + attack 1 − Strength 1 · needed 13 — miss`**

— and the `hidden` line was **gone** from the row immediately. The swing
gave me away even though it did nothing. Confirmed again on the other
side of the coin a few turns later with a critical (**"rolled 20 … hit ·
damage 2 … × 2 critical"**), which also revealed. Hit and miss reveal
identically, which is PT-1682's *"what gives you away is the shot rather
than the hit."*

## 4. ⚠ A REFUSED SWING REVEALS YOU TOO — the one case that should not

**This is the finding.** The commit states the rule plainly:

> *"AFTER THE TURN CHECK AND BEFORE THE SPEND, so a refused swing does
> not reveal — nothing was thrown."*

Live, a refused swing **does** reveal. Reproduced deliberately:

1. On my turn, adjacent to an enemy, pressed `s` — **"hidden — 19 beat
   13"**, row showed `hidden`, and the Action pip went dark, because
   **hiding itself spends the Action**.
2. Still the same turn, bumped the adjacent enemy to attack.
3. The screen said **"you have already acted"** — the swing was refused,
   no attack roll was made, nothing was thrown — **and the `hidden` line
   was gone from the row.**

The cause is visible in `play_screen.dart`'s `_playerStrikes`, and it is
a straight-line synchronous ordering rather than anything racy:
`_revealMe()` sits after the `!f.playersTurn` check but **before** the
`if (!f.player.budgets.canAct)` peek (and before the droid-melee gate
below it). So exactly one refusal path — *not your turn* — is protected
by the placement, and the other two fire after cover is already broken.

**Why this is easy to hit rather than a corner case:** hiding spends the
Action, so *hide, then try to attack in the same turn* — a very natural
thing for a player to try, and arguably the first thing anyone tries
after hiding — always costs the hiding for nothing. The player pays an
Action for the hide, gets a refusal that makes no attack, and loses the
hide anyway.

*(The protected path, "not your turn", I confirmed only by reading the
source — `_step` doesn't gate on turn ownership before reaching
`_playerStrikes`, so the branch is reachable in principle, but the enemy
turns resolve synchronously after `space` and I could not land a keypress
inside that window from outside the app. Flagging as read, not driven.)*

---

## What I did not check

- The "not your turn" refusal path live (see above) — source only.
- A droid player hitting the `melee is closed to every droid chassis`
  refusal while hidden, which by the same ordering would also reveal —
  inferred from the code, not driven.
- Hiding against a watcher with a *high* Awareness or Alertness: no
  installed blueprint declares `[skills]` at all, so this would have meant
  authoring one into my own fixture. Given §2 already produced plentiful
  detections from rank-0 watchers, I left the shipped data alone rather
  than editing it for a case the failures already covered.
- Whether the hidden state affects anything mechanically beyond the
  indicator (enemy targeting, attack bonuses from hiding) — the ask was
  about the Action, the indicator and the reveal, and I stayed there.
- `§4`'s stealth-field generator, which the commit explicitly names as
  not wired (no item declares itself one), so there was nothing to drive.

## On the `whole_loop_test` flake

Nothing to add: I did not run the Dart test suite this session — my pass
is entirely through the built app — so I have no independent sighting of
it either way. Noted and kept in mind. The commit itself also records it
(*"FLAKE SIGHTING, FIRST ONE"*), so there are now two written records of
the same one event rather than two events.

## State

- No package touched this session — confirmed by mtime; `companion-fixture`
  carries the same files as prior sessions and I added nothing.
- One save created ("Oreth Lhent"), reached `Play`, fought a long corridor
  fight — not cleaned up, ordinary Tester artifact. `Mate` was downed
  during it by enemy fire; nothing I need from her survived past the test.
- App PID `177282` killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) checked running, untouched, before and after.
