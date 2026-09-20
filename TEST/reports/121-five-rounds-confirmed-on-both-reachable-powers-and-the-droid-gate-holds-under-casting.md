# TEST 121 — five rounds confirmed on both reachable powers, and the droid gate holds under casting

**Build.** App **`bf2a9b2`** ("Beast Control and Beast Confusion: five rounds
too — PT-2462"), tree clean, built from `git archive` of that sha. The
committed lock resolves Lodestar **`d1fcab69`**, and that is the pub-cache
checkout `package_config.json` compiles against. `check_shelf.py` clean: 29
rules files and 65 standard blueprints.

⚠ The routing named `b602712`; that is the **HANDOFF** commit (`S35h: sync
agenda mirror (PT-2458)`), not an app one. `bf2a9b2` is what carries the
duration change and is what I tested.

**Verdict.** **Both items confirmed.** Force Distraction and Force Confusion
now run five rounds, not ten, and the refusal states the remaining count
correctly. All five droid species refuse **both** powers under real casting,
with a sentient control proving the gate is not simply refusing everything.
The two Beast powers remain unreachable for the same standing reason and are
reported as such rather than as passes.

---

## 1. Duration — five rounds on both reachable powers

### Force Distraction — held four enemy turns, resumed on the fifth

Cast, then withdraw four squares (cast **before** moving, so `lastSeenAt` is
not refreshed — the trap from TEST 119), then end turns and watch:

```
cast     Force Distraction · 8f — 159 → 151 · at guard.gd.01 · guard.gd.01 is distracted
round+1  guard.gd.01: unarmed · out of reach — unarmed reaches 1 square and Whisper is 4 away
round+2  … out of reach …
round+3  … out of reach …
round+4  … out of reach …
round+5  guard.gd.01 closes 3 squares — 4 to 1 · rolled 2 … miss
round+6  guard.gd.01 … hit · 82 left
```

Four consecutive enemy turns ignoring me, then normal pursuit on the fifth.
That is the cast round plus four — **five rounds inclusive**. Under the old
ten it would have stood still for four more.

### Force Confusion — the refusal's countdown, and it is arithmetically five

Force Confusion has the only "already" refusal in the pair; Distraction has
no equivalent message, so the clock above is the only way to read it.

Casting at `guard.cf.01` and then attempting a second sentient every two
rounds:

```
you already have guard.cf.01 turned · 3 rounds left
you already have guard.cf.01 turned · 1 rounds left
Force Confusion · 20f — 139 → 119 · at ally.cf.02 · ally.cf.02 turns on its own side
you already have ally.cf.02 turned · 3 rounds left
you already have ally.cf.02 turned · 1 rounds left
Force Confusion · 20f — 119 → 99 · at guard.cf.01 · guard.cf.01 turns on its own side
```

Two rounds pass between each reading, so with the cast at round *N* the
counts are `3` at *N+2* and `1` at *N+4*, and the effect is gone by *N+6*.
That solves to `untilRound = N + 4` — **five rounds inclusive**, and the
message's number is right at every step. Ten would have read `8` on the
first line.

⚠ **It repeats cleanly.** Both sequences end with a *new* cast succeeding
the moment the previous one lapsed, on the same caster — the per-kind limit
tracks the live instance, not a latched flag. That is `PT-2439` ruling 2
still holding at the shorter duration.

### Beast Control and Beast Confusion — still unreachable, not confirmed

Both rows now state five (`beast_control` via `distraction_rounds`,
`beast_confusion` via `confusion_rounds`), and they go through the same two
readers I measured above. **But neither can be cast at anything.** `kindOf`
returns `droid`, `sentient` or null and has no third answer, and says so
itself:

> ⚠ A NAMED SPECIES THAT IS NOT A DROID IS A SENTIENT. `species.toml`'s
> `is_droid` is the only division the corpus draws … **`beast` exists in the
> `targets` vocabulary and nothing in a package is one yet.**

So their five rounds are inherited from a shared reader rather than
observed. Reporting that as unreachable rather than as a pass — the routing
asked for four powers and I can only stand behind two.

⚠ One good change worth naming: the `?? 10` fallbacks are gone, replaced by
`p.confusionRounds!` / `p.distractionRounds!` with a comment saying a row
that lost its field *"would have kept handing out ten, silently and only
sometimes."* That is the right call — it turns a silent wrong duration into
a loud data fault.

## 2. The droid gate, re-verified by casting

Per your instruction the picker's ⚠ is not treated as evidence. Every one of
these is a **cast**, and the pool is the witness that a refusal costs
nothing.

**Force Distraction**, five droids in one encounter:

```
Bare Droid     — Force Distraction does not affect a droid
Astromech      — Force Distraction does not affect a droid
Assassin Droid — Force Distraction does not affect a droid
Battle Droid   — Force Distraction does not affect a droid
Remote         — Force Distraction does not affect a droid
```

**Sentient control, same encounter, immediately after:**

```
Force Distraction · 8f — 159 → 151 · ceiling −1 to 158 · at guard.dr.01 · guard.dr.01 is distracted
```

**Force Confusion**, the same five:

```
Bare Droid     — Force Confusion does not affect a droid
Astromech      — Force Confusion does not affect a droid
Assassin Droid — Force Confusion does not affect a droid
Battle Droid   — Force Confusion does not affect a droid
Remote         — Force Confusion does not affect a droid
```

**Sentient control:**

```
Force Confusion · 20f — 151 → 131 · ceiling −4 to 154 · at guard.dr.01 · guard.dr.01 turns on its own side
```

**The pool is the proof that nothing was spent on the refusals:** it sits at
159 through all five Distraction refusals, drops to 151 on the control, sits
at 151 through all five Confusion refusals, and drops to 131 on the second
control. Ten refusals, zero Force, two controls that both land.

And the cause is properly closed rather than patched: the inline copy in
`Present.placed` is **deleted**, and the placement now calls the same
`kindOf` the player does, with a comment recording why —

> ⚠⚠⚠ ONE CLASSIFIER, NOT TWO — `TEST 120` … **The copy is deleted rather
> than repaired**: a second answer to *what kind is this* is the thing that
> made `PT-2450`'s fix look complete while the half that matters stayed
> broken.

## Also noticed

* **A refusal leaves the target picker open**, with the same power still
  selected, so the next target can be chosen straight away. Sensible for a
  player. ⚠ Worth knowing for anyone scripting the UI: it means a following
  keystroke lands as another *target* choice rather than opening the powers
  menu, which silently re-runs the previous power at a different creature.
  Two of my early readings were wrong for exactly that reason before I
  caught it.
* ⚠ **An area whose content `tag` does not match its blueprint's `handle`
  makes the whole package's saves unreadable, with no message.** I authored
  `tag = "drx.on.02"` for a blueprint with `handle = "dr-x"`; the package
  loaded, the card showed a problem count, and **Continue and Load Game were
  simply greyed out for ever** with no save-count line and nothing naming
  the cause. Renaming the tag to `dr-x.on.02` fixed it immediately. The
  refusal is probably correct; the silence is what cost the time.

## Fixture

`tester-mind`, `0 Mind Bench (Tester)`. One board added:

* **`m05-one`** — exactly one sentient and one droid, so the picker is
  always `1 Guard · 2 Subject`. ⚠ Built because on the five-droid board the
  target numbers shift as creatures change state, and a mis-keyed digit
  casts at the wrong creature. `dr-x.toml`'s `species` is rewritten between
  runs.

In the end the five-droid board `m03-droids` did the sweep in one pass, by
leaving the picker open and chaining target digits against a single selected
power — which is the same behaviour noted above, used deliberately.
