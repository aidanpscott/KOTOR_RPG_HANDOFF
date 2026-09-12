# TEST 077 — PT-1856 confirmed: the action keys now vanish the moment the
# Action is spent, closing TEST 076's finding. And PT-1857's exploration
# Scan confirmed on all three counts: one attempt per hidden creature per
# visit, reset by leaving and coming back, and it genuinely finds a lurker
# the passive look cannot

**Built against:** `run-app.sh` (always rebuilds). App process started
16:12:03; local `KOTOR-RPG-APP` HEAD `cb13d3c` (15:55:26, *Pin to the
engine carrying the effect model*), which is the tip and contains both
commits under test — `fcb864d` (*PT-1856: the action keys vanish once the
Action is spent*) and `3d8d331` (*PT-1857: Scan gets its exploration
half*). Working tree was clean apart from `M pubspec.lock`: the `lodestar`
dependency uses a floating `ref: main`, so my build's `pub get`
re-resolved it to `67e6775c0e56f6360698426d24b7cd4c270595e3` while HEAD's
recorded pin is `e66d44a4ba600525600723fc5471ac932696e5c9`. **I diffed the
three functions this report depends on — `noticed()`, `scanCheck()` and
`Budgets.dash()` — and they are byte-identical between the two**, so
nothing below is an artifact of that drift. `lens`
`e79bc066233fabc7776c8b94737029646d762e6e`. Both checkouts present.
`check_shelf.py` at session start: `✓ 25 rules files, all identical to
what the extracts generate`.

App PIDs `3335616` and `3541349` killed by PID, both confirmed gone.
*(No Loom to report on: the background Loom task belonging to this session
exited cleanly with code 0 earlier today, before this test began, and I
did not restart it.)*

---

## 1. The action keys vanish with the Action — CONFIRMED, and it is my
## TEST 076 case exactly

Driven in `companion-fixture`'s corridor with a Soldier (speed 5).

- **Action available:** the combat line reads
  `f powers · c scan · d disengage · s hide · h hurry · space to end your turn`.
- **Pressed `h`** — "hurrying — 10 squares this round", Action pip dark,
  **10 move and Gear still unspent**. The line now reads **only
  `space to end your turn`.** The five keys are gone.
- **Ended the turn** — Action refreshed, and all five keys returned.

That middle state is precisely the one TEST 076 filed: under the old
`anythingLeft` gate the keys stayed on screen there, naming five things
that could only answer "you have already acted". Gating on `canAct` fixes
it, and keeping `anythingLeft` for the end-turn sentence is the right
split — the sentence is about the whole budget, the keys are about the
Action.

## 2. Exploration Scan — all three checks CONFIRMED

**The fixture, and why it had to be built.** The passive look is
`take 10 + the better of Awareness/Alertness`, so "what a passive look
cannot catch" means a `stealth` above that total. My Soldier took
**Awareness 4**, making the passive total exactly **14**; I added one
placement to my own `tester-probe` package's `a01-probe-room` —
`probe-sentinel.probe-room.21` at `(0, 3)`, `hidden = true`,
**`stealth = 15`** — one point beyond it. Every other hidden placement in
that room omits `stealth`, which is 0, so they are found by walking in;
this was the only one that needed looking for. **Reverted afterwards**
and the file verified back to its previous ending.

The arrival line confirmed the baseline on every entry:
**`you notice probe-warden — 14 against 0`** — the passive half finding
the stealth-0 placement and showing my total as 14. The stealth-15 lurker
was **not drawn** on the board, so it was genuinely concealed.

**`c` works outside a fight** and asks which sense:
`scan with — 1 Awareness · 2 Alertness`. Chose Awareness.

### One attempt per hidden creature per visit — CONFIRMED
First scan: **`you find nothing — 9 against 15`** — it rolled (d20 5 +
Awareness 4) against the placement's own stealth total, and said so.
Pressing `c` again immediately: **`you have searched this room — come back
and look again`** — refused outright, no second roll.

### Leaving and coming back resets it — CONFIRMED
Walked out the `(5,2)` door into Probe Hall and straight back. The scan
was allowed again and produced a **new** number:
**`you find nothing — 12 against 15`**.

### It genuinely finds the lurker — CONFIRMED
Repeated the out-and-back cycle. On a later visit:
**`you find Probe Sentinel — 20 against 15`** — and a token appeared on
the board at `(0, 3)`, the square the hidden placement occupied. Note it
names the creature by its **display name**, not its tag.

So across four visits the rolls were 9, 12, … , 20 against a fixed 15:
the hider's number is settled and the finder's is rolled, which is the
contest the rule describes, and one visit buys exactly one roll.

---

## What I did not check

- **`Vigil`** — the feat that makes a combat Scan free once a round. My
  character did not take it, so the `· free, Vigil` branch is unexercised.
- **The combat half of Scan**, which spends the Action rather than a
  visit. This session's Scan work was entirely in exploration.
- **A multi-target scan.** One press scans every *unsearched* hidden thing
  in the room, one roll each, but the status line reports only the first
  roll's numbers (`line ??=` in the source). My room had exactly one
  unsearched lurker by then, so I never saw how a two-target scan reads —
  worth a look if a fixture ever has two.
- **`nothing here is hidden from you`** — the refusal when a room holds no
  hidden thing at all. The probe room always had at least one.

## State

- `tester-probe` (mine) — one `[[contents]]` block added for this test and
  **removed again**; file verified byte-identical in its ending afterwards.
  Nothing else in the package touched. (The room's pre-existing package
  problems — `not a creature path, expected "characters/…"` and friends —
  are long-documented faults of that deliberately-faulted fixture, not
  mine and not new.)
- `companion-fixture` untouched.
- Two saves created (one per package), neither cleaned up.
- Both app PIDs killed by PID, confirmed gone.
