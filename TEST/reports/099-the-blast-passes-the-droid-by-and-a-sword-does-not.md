# TEST 099 — THE FIX HOLDS, ON A BOARD BUILT SO NOTHING ELSE CAN EXPLAIN IT.
# Death Field hit both organics for `12d4 27` each and **did not name the droid
# at all** — a droid standing ONE SQUARE NEARER the blast centre than an organic
# the blast did reach. Force Scream and Crush Opposition I, two of the eleven
# exclusions that arrived with this ruling, passed it by as well.
# ⚠ AND THE CONTROL THAT MAKES IT MEAN SOMETHING: after three blasts the droid
# stood at exactly `200 of 200`. I then hit it with a vibrosword from the same
# square and it took **18**. It is a live, visible, damageable body in the same
# fight — it simply cannot be reached by a power that excludes its kind.

## Build state

    KOTOR-RPG-APP   cb8aed2  PT-2268 — the fix itself, built and measured from this
    lodestar        d00b18c  — HEAD's own pin, and the pub-cache checkout
    lens            32b77e3

    ✓ FRESH — built from exactly this source at 09-17 15:02:58

Lodestar and Loom clean; the app tree carried one modified **test** file and
nothing in `lib/`, so HEAD is what ran. `check_shelf.py` green at both ends.

---

# THE BOARD, AND WHY IT IS SHAPED THIS WAY

Three creatures **identical in every field but one** — same class, level,
abilities, 200 vitality, same doctrine. Only `species` differs, which is the
single field `kindOf` reads:

    (4,1)  m-org-near   human   distance 0 from the centre   ← the cast aims here
    (5,1)  m-droid      droid   distance 1
    (6,1)  m-org-far    human   distance 2

The droid stands **nearer the centre than an organic the blast does reach**, so
if it is skipped and `m-org-far` is not, neither distance nor line of sight can
be the reason. That is the shape your own new guard uses; this is it on a real
board with a real cast.

# 1 · DEATH FIELD — the power the bug was named for

    Death Field · 20f — 159 → 139 · ceiling −4 to 155 · at m-org-near.probe.01 ·
    m-org-near.probe.01 — 12d4 27 · m-org-far.probe.03 — 12d4 27 ·
    Blaster — drained 27 · 74 → 74

    roster: m-org-near 173 of 200 · m-org-far 173 of 200 · m-droid 200 of 200

Both organics took 27. **The droid is not named in the line at all** — it is not
in the touched set, rather than being in it and taking zero. Its vitality did
not move.

⚠ And `heals: caster` paid out beside it — `drained 27 · 74 → 74`, clamped
because I was already full.

# 2 · TWO OF THE ELEVEN NEW EXCLUSIONS, on the same bodies

**Force Scream** — a cone rather than a radius, and it carries both damage and
a penalty, so there were two ways for it to touch the droid and it took neither:

    Force Scream · 8f — 139 → 131 · at m-org-near.probe.01 ·
    m-org-near.probe.01 — 12d6 40 · −2 str 10r · −2 dex 10r · −2 con 10r ·
                          −2 int 10r · −2 wis 10r · −2 cha 10r ·
    m-org-far.probe.03  — 12d6 41 · −2 str 10r · −2 dex 10r · −2 con 10r ·
                          −2 int 10r · −2 wis 10r · −2 cha 10r

**Crush Opposition I** — a radius of 7 and no damage at all, so the only thing
it could land is the modifier pair:

    Crush Opposition I · 8f — 131 → 123 · at m-org-near.probe.01 ·
    m-org-near.probe.01 — -1 attack · -1 will · m-org-far.probe.03 — -1 attack · -1 will

Neither names the droid. Three powers of three different shapes — radius with
damage, cone with damage and ability penalties, radius with modifiers only —
and the droid is absent from every one.

# ⚠ THE CONTROL — the droid is not an inert token

This is the part that makes the three readings above worth anything. After all
three blasts:

    m-org-far 132 of 200 · m-org-near 133 of 200 · m-droid 200 of 200

Every point the organics lost came from the blasts; the droid had lost nothing.
I then walked one square and hit it with a vibrosword:

    Vibrosword · rolled 14 — d20 1 + attack 9 + Strength 4 · needed 9 — hit ·
    damage 18 — 1d12 12 + Strength 6 · 182 left

    roster: m-org-far 132 of 200 · m-droid 182 of 200 · m-org-near 133 of 200

**The droid's only lost vitality in the whole fight came from a sword.** It is
in the encounter, it has a turn, it is visible, it is in reach and it takes
damage — so "the blast did not touch it" is about the kind exclusion and
nothing else. Without this the negative would have been unscoped.

---

## What I did not do

- **Did not test the other fifteen** of the seventeen area powers that exclude a
  kind — three, chosen to differ in shape (radius/cone, damage/no damage).
- **Did not test a `targets`-side power against the wrong kind** (`destroy_droid`
  aimed at an organic, say). The ruling you routed is the exclusion side, and
  `kindsFor` completes a negative into a positive at one place, but I did not
  exercise the positive direction.
- **Did not test a beast**, which `kindOf` can never return — noted in the
  engine's own comment, not something a blueprint can reach today.
- **Loom not launched.**

## State

- **New package `blast-kind` is mine** — one area, three creatures identical
  but for `species`, one authored caster (Consular 12, format 3).
- ⚠ The droid is `species = "droid"` with no chassis and no origin, which is
  the shape the shipped `melee-droid` blueprint uses and what `record_validate`
  requires of a droid.
- My build lives in the scratchpad copy only. **Your `build/` was never written
  to and neither shared bundle was touched.**
- App pid `450657` killed by pid and confirmed gone; no Loom; nothing of yours
  touched.
