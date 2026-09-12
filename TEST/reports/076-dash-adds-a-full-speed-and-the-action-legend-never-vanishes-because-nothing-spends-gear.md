# TEST 076 — Dash (`h`) confirmed live: it adds a whole speed rather than
# doubling what is left, and it costs the Action. The legend is on screen
# in combat and absent outside it — but it does NOT vanish once you have
# acted, and the "nothing left" line it falls back to is unreachable

**Built against — and this one needs care.** `run-app.sh` (always
rebuilds); app process started **14:32:01**. Local `KOTOR-RPG-APP` HEAD
was `e4682f7` (14:11:39, *PT-1852: the four Action keys are on the
screen*) and stayed there for the whole session — **but the working tree
was not clean.** `git status` at build time:

```
 M lib/play/play_screen.dart
 M pubspec.lock
 M test/two_enemies_test.dart
```

So my build is **HEAD plus Coder's uncommitted work**, which is
`PT-1855`'s **Scan** action (`c`, with a `Vigil` feat) — in progress, not
committed, and not reported to me. I read it only far enough to know what
it was and left it alone. Two consequences, both handled below: the legend
I saw has a fifth entry that no commit contains, and the engine pin I
compiled against is not HEAD's.

- Engine pin **on disk / in my build**: `lodestar`
  `d25bbb00583723872cc534b22cdf708d48e5ef83`. **HEAD's** pin is
  `c7a8aacba18b88d1b8ab8566363b54494dd3b39a`. Both are present as real
  checkouts, and **`Budgets.dash()` is byte-identical between them**
  (diffed), so §1 below is not an artifact of the uncommitted bump.
- `lens` `e79bc066233fabc7776c8b94737029646d762e6e`, checkout present.
- `check_shelf.py` at session start: `✓ 25 rules files, all identical to
  what the extracts generate`.

App PID `4022299` killed by PID, confirmed gone. Coder's Loom (`12445`/
`12443`) checked running, untouched, before and after. Coder's uncommitted
changes were left exactly as found — read, never staged, reverted or
committed.

**Character:** "Sarn Veld", Human Soldier, speed **5**.

---

## 1. Dash adds a whole speed, not double the remainder — CONFIRMED

Driven the way the distinction actually shows, which is *after* moving:

- Moved **2** of 5 → the strip read **`3 move`**.
- Pressed `h` → **"hurrying — 8 squares this round"**, strip **`8 move`**.

3 remaining **+ 5 speed = 8**. Doubling what was left would have given 6.
So the implementation matches the document's *"double your movement this
round"* read as two speeds, and a creature that has already walked gets
the bigger jump.

Also driven on a fresh turn for contrast: `h` → **"hurrying — 10 squares
this round"** (5 + 5). That is the case where both readings agree, which
is exactly why the partway case above is the one that decides it.

**It costs the Action — CONFIRMED.** The Action pip went dark the moment
the dash landed, and afterwards `s` answered **"you have already acted"**
and `h` answered **"you have already acted"**.

*(Incidental: the 8-square dash carried me the length of the corridor and
through the door in a single turn, which is the feature doing visibly what
it says.)*

## 2. The legend: present in combat, absent in exploration — CONFIRMED

- **Outside a fight** the line reads `arrows to move · m map · i carrying ·
  esc to leave` — no Action keys, which is right and is what the commit
  says it had to settle for (adding one there overflowed by 57px).
- **Once a round is running** the combat line carries them, alongside the
  existing end-turn affordance.

All four asked-for keys are present: **`f powers`**, **`d disengage`**,
**`s hide`**, **`h hurry`**, then **`space to end your turn`**.

⚠ **It actually shows five.** The live line is:

> `f powers · c scan · d disengage · s hide · h hurry · space to end your turn`

`c scan` is **not in `e4682f7`** — it comes from the uncommitted `PT-1855`
work described above. Flagging it so the extra entry is not mistaken for
something PT-1852 did, and so nobody reads my confirmation as covering it.
I did not exercise `c scan`.

## 3. ⚠ They do NOT vanish once you have acted — and the fallback line is unreachable

The ask was to confirm the keys "disappear once you've already acted
(since all four would just refuse at that point)", which is also the
commit's own stated rule:

> *"THEY VANISH WHEN THERE IS NOTHING LEFT TO SPEND… every one of them
> costs the Action, so offering them to somebody who has already acted
> would name three keys that can only refuse."*

**That is not what happens.** Demonstrated in one turn:

1. Dashed — Action spent, `8 move` remaining. The line **still named all
   five keys**.
2. Pressed `s` → **"you have already acted"**. Pressed `h` → **"you have
   already acted"**. So the named keys could, at that point, only refuse —
   precisely the situation the rule is meant to prevent.
3. Spent every remaining square (`0 move`, Action spent, Gear still lit).
   The line **still named all five keys**. The
   `⟩ nothing left — space to end your turn` variant never appeared.

**Why, read from the source and then confirmed:** the gate is
`budgets.anythingLeft`, not `canAct`. The engine defines

```dart
bool get anythingLeft => !turnOver &&
    (moveLeft > 0 || !actionSpent || (bonusGranted && !bonusSpent) || !gearSpent);
```

and **nothing anywhere spends Gear** — `grep` for `spendGear`/`spendBonus`
returns no callers in `lib/`, and the engine's own `spendGear()` has none
either. So `!gearSpent` is permanently true, `anythingLeft` collapses to
`!turnOver`, the keys never vanish during your turn, and the "nothing
left" branch is dead code in the product as it stands.

Worth noting this is a **known fact meeting a new consumer** rather than a
fresh discovery: `budget_strip.dart` already carries the comment
*"`Tester` checked THE PIP: … `spendGear` has zero callers."* The pip
survived that because it is only ever lit; the legend does not, because it
uses the same predicate to decide when to go away.

The fix is presumably one word — gate on the Action rather than on any
budget — but which predicate is correct is a UI decision, so I am naming
it rather than proposing it.

---

## What I did not check

- **`c scan`** — uncommitted, unreported, not mine to test.
- **Hidden disables Dash** (`'not while you are hidden — hurrying is
  loud'`) and the assertion that a refused Hustle neither costs nor
  breaks cover. Read in the diff, not driven; my dash runs were never made
  from hiding.
- Whether Dash and Disengage interact (both spend the Action, so the
  second should simply refuse).
- Whether the legend wraps or overflows at other window sizes — I drove
  one geometry, 1600×900.

## State

- No package touched this session — confirmed by mtime.
- One save created ("Sarn Veld"), left mid-fight, not cleaned up.
- App PID `4022299` killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) untouched. **Coder's uncommitted working-tree changes
  left exactly as found.**
