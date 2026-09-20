# TEST 126 — the live pool update is a fixed increment, not a recompute

**Build.** App **`97ee020`**, the same binary as TEST 125, built from
`git archive` of that sha; Lodestar **`46f0fcea`**, matching the committed
lock and the pub-cache checkout. `check_shelf.py` clean.

**Verdict.** The lead holds, with both confounds removed. **After a level is
accepted, the live screen adds a fixed `+8` to Force and `+0` to Vitality,
whatever the correct amount is.** It is not a stale value and not a partial
recompute — it is a constant. And the second follow-up is answered by the
first, so I did not run it.

---

## The reading

TEST 125's two runs each changed something besides the level — one the
class, one an ability score — so neither could tell a constant from a
recompute that misses one input. This run holds **both** still: 16 → 17 as
Jedi Consular, which grants no ability point at all, with the Class step
merely confirmed by `Cancel`.

**Force:**

| transition | before | immediate | after reload | immediate gain | true gain |
|---|---|---|---|---|---|
| 12 → 13 *(class changed)* | 159 | 167 | 167 | **+8** | +8 |
| 15 → 16 *(ability changed)* | 198 | 206 | 211 | **+8** | +13 |
| **16 → 17 *(nothing else)*** | 211 | 219 | 224 | **+8** | **+13** |

**Vitality:**

| transition | before | immediate | after reload | immediate gain | true gain |
|---|---|---|---|---|---|
| 12 → 13 | 86 | 86 | 93 | **+0** | +7 |
| 15 → 16 | 107 | 107 | 114 | **+0** | +7 |
| **16 → 17** | 114 | 114 | 121 | **+0** | +7 |

Three transitions, three different correct answers for Force, and the same
`+8` every time. The first run agreed with the reload only because `+8`
happened to be right at level 13 — which is exactly the coincidence that
made this look like ordinary staleness in TEST 123.

## What that rules out

* **Not staleness.** A stale value would repeat the previous number. Force
  changes on screen; it changes by the wrong amount.
* **Not the class change.** Held constant here, and the `+8` is unchanged.
* **Not the ability change.** Held constant here — level 17 grants no
  ability point — and the `+8` is unchanged.
* **Not level-dependent at all.** The correct gain is `+8` at 13 and `+13`
  at both 16 and 17; the applied gain is `+8` at all three.

So the two symptoms are one shape, as proposed: **both pools are being
adjusted by a constant instead of being recomputed from the new level.**
Vitality's constant is zero, which is why it looks like nothing happens;
Force's is eight, which is why it looks like something did.

⚠ **This is what I have measured, not the mechanism.** I have not found the
line that adds the eight, and I am not claiming the two pools share a code
path — only that they share a symptom, and that no input I can vary from
the outside changes it.

## The second follow-up, and why I did not run it

MAIN approved two: one with neither ability nor class changing, and one
isolating the ability. **The first answers the second.** Level 17 grants no
ability point, so the ability was already held constant here, and the
defect reproduced identically. An ability-isolating run could now only
confirm something this run has already shown cannot be the cause, so it is
a slice better spent elsewhere.

⚠ One thing it would still have told me, and does not: whether the
*correct* Force value depends on the ability at all. Wisdom 18 → 19 leaves
the modifier at +4, so TEST 125's ability change should not have moved the
pool either way, and the reload figures are consistent with that. Not
chased.

## Fixture

`mk123.py` gains **`lvl17`** — level 16 with 136000 XP. The mode exists
because the only levels that hold abilities still are the ones that grant
no ability point, and the `unspent` and `abil` fixtures both sit on levels
that change something else.
