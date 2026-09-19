# TEST 112 — six conditions enforced in play, a way up that works, and two clauses that cannot bite

**Build.** App `fb52718` (tree clean), `pubspec.lock` resolved-ref `6f12c37c`,
and the pub-cache checkout `package_config.json` compiles against is
`Lodestar-6f12c37c`. Built from `git archive fb52718`. `check_shelf.py`: 29
rules files and 65 standard blueprints identical to what the extracts
generate.

**Verdict.** All five items confirmed. The stand-up works in both halves —
that was the one that could have made prone a permanent disable, and it does
not. Every enforced condition changes exactly what its ruling says and
nothing else, and the unenforced control says so in its own line.

**One real gap, and it is not in this thread:** slowed's *"Bonus lost"* and
cowering's *"keeps the Bonus"* cannot be confirmed in play, and cannot
currently matter. `bonusGranted` is assigned `false` in exactly two places in
production code — the `Budgets` constructor and `startTurn` — and **nothing
anywhere sets it true**; the only `= true` in either repo is a fixture in
`budget_strip_test`. So no creature is ever granted a Bonus, the pip is never
drawn, and `legality.bonus` is computed into a field nothing can spend. Both
clauses would pass a play-test identically if they were deleted.

---

## The instrument, and why it is the player

Conditions were put on the **player** wherever possible. An enemy's budget is
invisible — the only thing readable about it is how far it walks — while the
player's budget strip states `move`, `action`, `gear` and `reaction`
directly, and the verb line beneath the board collapses to `g gear · space to
end your turn` the moment the Action is forbidden.

Two things govern every reading below:

* **Legality is applied at `Budgets.startTurn`** (`moveLeft = immobile ? 0 :
  speed ~/ moveDivisor`), so a condition landing mid-turn shows nothing until
  the next turn begins. Every budget reading here is taken a turn after the
  landing.
* **A hazard is the only way to put a condition on the player without staging
  a fight** — but the hazard path substitutes `1` for a missing `rounds`,
  where the on-hit path passes `onHit.rounds` straight through. So **prone
  was read from a real item and never from a hazard**: a hazard could not
  show *"never expires"* if it tried.

The bench uses `dc = 99, on_save = "none"` so the condition always lands. My
first build used `dc = 1`, which is the opposite mistake and read *"you shake
it off"* every time.

## 1. Prone — both halves, and the way up

**The player, hit by a real `w_brifle_23` Charric** (the survivable one;
`w_sls_x02` is 2d6+1d8 and killed a 9-vitality Scout outright before anything
could be read):

```
prone — d20 2 + reflex 5 = 7 vs 14 · takes hold
```

| | normal | prone |
|---|---|---|
| move | `5` | **`0`** |
| action | available | pip dark |
| verbs offered | `f powers · c scan · d disengage · s hide · h hurry · t treat · r repair · o throw · g gear` | `g gear` |

* **Zero, not halved.** 5 → 0, not 5 → 2. Prone reaches `immobile`, the
  sentinel, and leaves `moveDivisor` alone — which is the distinction
  `PT-2365` spelled out, and the held board below reads the same way while
  slowed reads 2.
* **Movement refused, and it says why:** `you are prone`.
* **It does not expire.** It landed and was still on three rounds later,
  through three further enemy turns.
* **`u` works:** `you are up — that was the Action`.
* **And the line is not the proof — the next turn is.** After standing, the
  turn began at `5 move` with the Action available and the full verb list
  back, and I moved: `a01-prone-me · 0, 1`. A printed sentence with the
  condition still attached would have read identically.

**The enemy, hit by the same weapon, three consecutive times:**

```
prone — d20 12 = 12 vs 14 · takes hold   →   dummy.pf.01 gets up — that was the Action
prone — d20  9 =  9 vs 14 · takes hold   →   dummy.pf.01 gets up — that was the Action
prone — d20  2 =  2 vs 14 · takes hold   →   dummy.pf.01 gets up — that was the Action
```

It spends its whole turn standing and never swings — and my vitality stayed
at `51 of 51` across all three, which is the independent confirmation that
the turn really went on standing rather than attacking.

## 2. Slowed — the halving, the three numbers, and the Slow/Mire split

On the player, from a hazard: `slowed for 30 rounds`, and then

| quantity | reading |
|---|---|
| move | `2` — halved from 5 |
| attack | `unarmed · rolled 13 — d20 10 + attack 4 + Strength 0 − power 1 · needed 13` |
| Defence | `defence base 10 + power -1 = 9` |
| Reflex | `goes off — d20 2 + reflex 5 − power 1 = 6 vs 15` |

All three −1s, each as its own named term. (The Reflex reading needed a
second, plain-damage mine as a probe: a hazard springs once, so the condition
mine cannot show the penalty it just applied.)

**Force Slow does not halve movement and Force Mire does — measured as a
matched pair.** Same dummy, same starting gap of 6, same retreat:

```
Force Slow · 6f  — 48 → 42 · ceiling −1 to 47 · dummy — d20 10 = 6 vs 14 · slowed
                   dummy.ct.01 — -2 defence · -2 reflex · -2 attack
                   dummy.ct.01 closes 5 squares — 6 to 1

Force Mire · 12f — 48 → 36 · ceiling −3 to 45 · dummy — d20 10 = 6 vs 14 · slowed
                   dummy.ct.01 — -4 defence · -4 reflex · -4 attack
                   dummy.ct.01 closes 2 squares — 6 to 4 · out of movement 4 squares short
```

5 squares against 2, from the same 5-square budget. `condition_spares =
['movement']` on Force Slow's row is doing exactly what it was added for, and
the powers' own −2/−4 bundles are distinct from the `slowed` condition's −1.

## 3. Shaken — all three numbers, and it restricts nothing

`shaken for 30 rounds`, and the budget strip reads `5 move`, action
available, full verb list, `defence base 10 = 10`. It forbids nothing, and
Defence is **not** among its quantities — which the derivation line confirms
by showing no penalty where slowed showed `power -1`.

| quantity | reading |
|---|---|
| attack | `d20 10 + attack 4 + Strength 0 − power 2 · needed 13` |
| saves | `goes off — d20 15 + reflex 5 − power 2 = 18 vs 15` |
| skills | see below |

**The skill −2, with its control**, on the same board, same fight, same mine:

```
not shaken:  disarm — d20 16 + Demolitions 0 = 16 vs 20 (hard)
shaken:      disarm — d20 10 − Demolitions 2 =  8 vs 20 (hard)
```

The term flips from `+ Demolitions 0` to `− Demolitions 2`, and it is not
clamped at zero. The control matters: this Scout's base Demolitions rank *is*
0, so a single reading of `Demolitions 0` would have been consistent both
with the penalty applying and with it never arriving.

**The fear residual lands, and Fear is exempt — one cast each, same target.**
Horror caught both dummies at once:

```
Horror · 12f — dummy.ct.01 — d20 17 = 13 vs 14 · cowering
               stoic.ct.02 — d20 20 = 30 vs 14 · shaken
```

The Wisdom-30 dummy **made** its save by 16 and still ended up shaken; the
low-Will one failed and got cowering, in the same line, as its own control.
Then Fear at the same target:

```
Fear · 6f — stoic.ct.02 — d20 20 = 28 vs 14 · resists
```

Made save, **nothing applied**. Same caster, same target, same made save,
different power — residual against none.

And those two lines are also the saves penalty, measured by accident of the
same die face: both rolled a natural 20, `= 30` before shaken and `= 28`
after.

## 4. Held and cowering

| | held | cowering |
|---|---|---|
| landing | `held for 30 rounds` | `cowering for 30 rounds` |
| move | **`0`** — zero, not halved | `5` — untouched |
| action | available, full verb list | pip dark, verbs collapse to `g gear` |
| Defence | `defence base 10 = 10` | `defence base 10 = 10` |

Held is zero rather than the divisor's 2, and it leaves the Action alone —
the opposite of prone, which takes both. Cowering takes the Action and leaves
movement, which is the opposite of held. Neither carries a number.

Cowering was also seen on an enemy from a real power, via Horror: on its turn
the board said **`dummy.ct.01 is cowering`** and it did not act.

## 5. The control — an unenforced condition

```
goes off — d20 16 + reflex 5 = 21 vs 99 · entangled for 30 rounds · ⚠ nothing enforces it yet
```

`5 move`, action available, full verb list, `defence base 10 = 10`. It lands,
it is named, it restricts nothing — and the product **says** it is not
enforced rather than leaving it to look like a working condition that
happened to change no number. That warning is absent from all five enforced
conditions above, so the same mine mechanism distinguishes the two cases by
itself.

## What could not be confirmed, and why

* **The Bonus clauses.** Covered at the top: nothing in the product grants a
  Bonus, so slowed losing it and cowering keeping it are both inert. This is
  a gap in what exists to be restricted, not in the restriction.
* **Shaken on an enemy's attack roll.** `_enemyTurns` overwrites `_said` per
  actor and the shaken creature acted first, so its line was gone before it
  could be photographed. Read on the player instead, where all three numbers
  appear at once.

## Noticed in passing, not a defect in this thread

`Force Mire` prints `⚠ Force Mire does not say what it may be aimed at` on
every cast. Its shelf row carries no `targets`, where `force_slow`,
`force_plague` and the rest of the family do. The product announces the gap
rather than guessing, which is right — but the row is one field short of its
siblings.

## Fixtures

`tester-conditions` on the shelf: seven boards, a dummy, a sabre-armed dummy,
a Wisdom-30 dummy for made saves, and blueprints for the two real prone
weapons. Saves `t112-*` written one at a time so `Continue` cannot pick the
wrong one. The four "problems" the library reports against this package are
unreachable-area warnings from switching boards through `[entry]`, not
hazard refusals — checked with `validateConnections`.
