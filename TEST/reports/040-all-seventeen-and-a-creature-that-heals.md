# 040 · All seventeen fired, and a creature that heals what it hits

**From `Tester`. Unrequested number.** `PT-1512` and **`PT-1617`** followed:
`BK16/`, `SV-T039/`, and **`base-rules` was left alone** — see the header.

**⚠⚠ BUILT AND MEASURED AGAINST — two different things, and they are not the
same build:**

    §1–§3  Loom 2e78da7  →  Lodestar 5031aed        built 15:00
    §4–§5  app  fb666f0  →  Lodestar 661405c        the 14:10 bundle, RE-RUN, NOT REBUILT

**⚠ I did not rebuild the app.** `KOTOR-RPG-APP` was **2, then 3, then 5 dirty**
throughout — Coder is mid-`PT-1618`. **So `§4`–`§5` are a re-run of the bundle I
made at 14:10 from `fb666f0`, and the app HEAD has moved twice since (`d11b724`
now).** Loom's three new fault strings were verified in the pub cache **and** in
its binary before I used it.

**⚠⚠ AND `base-rules` MOVED AGAIN, MID-SESSION, AND I LEFT IT.** At **15:01**
`event_kinds.toml` gained:

    kind = "character.dying"
    lifetime = "transient"
    note = "transient — until the encounter ends  PT-1618 — newly declared"

**That is `039 §3` landing while I worked. `PT-1617` says report it, not reverse
it, and the diff is the only reason I noticed.** ⚠ **And `transient` means it
will correctly never reach a save** — so a future count must expect
`character.dying` = 0 and judge `character.downed` alone.

**As I write: `Loom 323c3b5` · `MAIN_WORK 88de5ef` · `HANDOFF 11540e5` —
`BUILD 106`. Nothing here is against those.**

---

# ✅ 1 · ALL SEVEN FIRED — AND SO DID THE OTHER TWO NOBODY HAD SEEN

**You named seven. ⚠ The enum is SEVENTEEN now, not nineteen** — `PT-1607`
removed `conversationOwnerUnknown` and `conversationOwnerNotTheSpeaker` with
`owner` itself — **and two MORE had never been seen, which you did not list:
`areaFileMissing` and `landingPointUndeclared`. I fired all nine.**

> **⚠⚠ EVERY ONE OF THE SEVENTEEN `PackageProblem` MEMBERS HAS NOW BEEN SEEN TO
> FIRE ON A REAL PACKAGE.**

**And the wording mattered every time, exactly as you said:**

| member | what it says that a bare name would not |
|---|---|
| `duplicateArrivalName` | *"…declares more than one arrival called `from-probe-room`, **so a connection landing there cannot say which**."* — the consequence, in the right terms |
| `targetAreaUnknown` | *"leads to `a99-nowhere`, which this package does not list."* ⚠ **`declared: a01…, a02…, a03…, a04…`** — it lists the four that ARE |
| `targetAreaUnreadable` | *"which this package **lists but could not read**, so **this connection could not be checked**."* ⚠ **That is `TEST 016 F3` closed** — the two cases were conflated and are now distinguished, and it declines rather than asserting |
| `referenceMissing` | *"`probe-feeble.toml` names the conversation `dialogue/no-such-talk`, and there is nothing there."* ⚠ **No `areaId`** — a blueprint fault, correctly area-less |
| `entryAreaUnknown` | headed **`manifest · entry`** — a synthetic row for package faults, sorted FIRST |
| `entryUndeclared` | *"This package declares **4 areas** and no `[entry]`, so **a new game has nowhere to begin**."* — it counts them |
| `requiredFieldMissing` | *"…which `PACKAGE-FORMAT-01 §4·1` requires."* ⚠⚠ then **`set in package properties`** — **it names WHERE TO FIX IT**, the only one of the seventeen that does |
| `areaFileMissing` | *"…but it cannot be read: **There is no area file here**."* — same opening as `areaUnreadable`, distinct tail |
| `landingPointUndeclared` | *"lands on `no-such-landing` in `a02-probe-hall`, and `a02-probe-hall` declares no arrival by that name."* |

## ⚠ And the last one exposed a small thing in its own suggestion list

    declared: from-probe-room, from-probe-room

**My duplicate-arrival fixture, listed TWICE.** **The `didYouMean` is not
deduplicated** — so an author with a duplicate-name fault is offered the same
suggestion twice, two rows above the fault that explains why.

---

# ✅ 2 · THE SUPPRESSION, READ RATHER THAN INFERRED

**You were right to push: `11-not-13` was arithmetic. ⚠ I read the rows.**

**`a02` fully walled, its arrival unstandable and its one connection isolated —
all four conditions true at once:**

    a01-probe-room   zoo-empty.probe-room.15   …
    a02-probe-hall                             ⚠ EXACTLY ONE ROW
      No square in "a02-probe-hall" can be stood on, …
    a03-probe-yard                             …

**No `landingNotStandable`, no `connectionUnreachable`, no `areaHasNoWayOut` for
`a02`.** And **each of those three was fired independently on this same area in
`039`**, so *"they never fired at all"* is excluded. **Pre-emption, confirmed by
reading, and the `return` in the source says why.**

---

# ✅ 3 · THE PALETTE REBUILD LANDED, AND THE SEVENTH SIGHTING WAS THE LAST

**`Loom 2e78da7` — *"Slice four — the left pane empties, and the palette becomes
a mode selector"*.**

    palette
      terrain            ⚠ selected, and the varieties below it
      creatures
      doctrines
      doors        a doorway, painted
      encounters
      items
      …
      waypoints    a arrival point, painted

> **✅ THE DOUBLE LINE IS DEAD.** *"⚠ cannot list — no folder is specified for
> this kind **yet**"* is gone from `doors` and `waypoints`. **Six reports, seven
> sightings, closed by a rebuild rather than a patch.**

**✅ And the left pane HAS emptied** — the module tree now runs `areas` →
`conversations` and **carries no `blueprints` section at all.**

**⚠ One new slip in the fresh text: `waypoints` reads *"**a** arrival point,
painted"*.** One character.

---

# ⚠⚠ 4 · AND A CREATURE WITH LOW STRENGTH HEALS WHAT IT HITS

**I built `probe-feeble` in `037` with `str = 1` so a fight could be survived.
⚠ It does not damage. It HEALS.**

    probe-feeble.probe-hall.02: unarmed · rolled 14 — d20 17 + attack 1
      − Strength 4 · needed 14 — hit · ⚠⚠ -1 damage · 3 left
    probe-feeble.probe-hall.02: unarmed · rolled 16 — d20 19 + attack 1
      − Strength 4 · needed 14 — hit · ⚠⚠ -1 damage · 4 left

**Probe Walker went 1 → 3 → 4 BY BEING HIT**, across several landed blows.

**⚠ The attack roll is right** — `− Strength 4` belongs there. **The DAMAGE is
where it goes wrong:** `str 1` gives a `−4` modifier, unarmed's base is small,
and the total goes negative. `strike` passes `a.damage!.total` straight to
`applyDamage`, whose own comment says *"a negative `amount` reaching
`applyDamage` is a caller's own business rather than a hidden feature."*

> **⚠⚠ THE CALLER IS `strike`, AND IT IS NOT MINDING THAT BUSINESS.**

**⚠ And this is not an exotic value.** Loom's `New creature` takes the six
abilities as free numbers — **I typed `14` into one this morning** — and **any
Strength below 8 gives a negative modifier.** A `Strength 6` weakling on a small
weapon is an ordinary authoring choice.

**⚠ Shape it wants:** a floor at the boundary. `ATTACKS-01 §12.5` puts Strength
on melee damage; **nothing says it may take it below zero**, and the clamp
belongs where the total is computed rather than in every caller.

---

# ⚠⚠ 5 · `down` IS A KNIFE-EDGE, AND I WATCHED DAMAGE STEP OVER IT

**You asked me to land a player on exactly 0. ⚠ I tried, and failing is the
finding.**

**`Blade Tester` against `probe-sentinel.probe-slit.03`, damage 1 or 3 per blow:**

    hit · 1 damage · 5 left
    …
    hit · 3 damage · 1 left        ⚠ one point from the state
    hit · 3 damage · -2 left       ⚠⚠ STEPPED STRAIGHT OVER ZERO

**The fight ended at `−2` — `dying`, not `down`.**

> **⚠⚠ `down` REQUIRES THE DAMAGE TO LAND EXACTLY ON THE REMAINING VITALITY. It
> is a coincidence, not a transition, and 1–3 damage against 1 vitality misses
> it two times in three.**

## ⚠ And the log's own figures, PLAYER ONLY, which is the number the ruling needs

**`039` said "at most ~40". ⚠ That was three times too generous.**

    THE PLAYER ONLY, across all twenty saves:
      character.revived                    48
      encounter.ended at or below zero:    66
         exactly 0   -> DOWN               10
         negative    -> DYING or dead      56

> **⚠ SO A WRITER BESIDE `revived`'s WOULD EMIT 48 EVENTS FOR AT MOST 10 GENUINE
> DOWNS.** `PT-1618`'s move to the crossing is right, and the crossing will fire
> **rarely**.

**⚠ And 10 is a FLOOR, not a count.** `encounter.ended` records where a fight
FINISHED; a player can cross zero and be struck again into the negative inside
one fight. **The log cannot count its own missing event — which is the whole
reason the event is needed.**

## ⚠⚠ AND THE HENCHMAN QUESTION HAS A DIFFERENT ANSWER THAN EITHER OF US EXPECTED

**You asked me to separate player from henchman in the 91. ⚠ The split is not
player/henchman at all:**

    character.revived, all saves:   91
       THE PLAYER                   48
       ⚠⚠ probe-sentinel.probe-room.04 — A PLACED CREATURE   43

**`revived`'s guard is `c.role != Role.enemy`, and a creature is being revived
43 times — nearly half the count.** Confined to two saves, `grave-digger.sav`
(37) and `yard-tester.sav` (6), **both predating this session.**

**✅ And it is already known and already recorded** — the source comment beside
the guard says *"`TEST 022` then met the actual producer within two slices —
`grave-digger.sav` carries revives for an enemy at −2, −3, −4 and 0"* and **"I
COULD NOT REPRODUCE IT ON HEAD."**

> **⚠ So the finding is not the defect — it is that MY OWN COUNTS WERE
> CONTAMINATED BY IT. `038`'s "92 revivals" and `039`'s "91" both included 43
> events for a creature. The player figure is 48, and it is the only one that
> bears on `PT-1618`.**

---

# 6 · Scoped negatives

- **⚠ `§4` and `§5` ran on the 14:10 bundle of `fb666f0`.** The app HEAD is
  `d11b724` and 5 dirty. **Neither the healing nor the knife-edge was checked on
  a current build**, and both are Lodestar-side arithmetic that I read in
  `5031aed` but exercised through `661405c`.
- **⚠ I did not read unarmed's base damage.** *"`str 1` gives −4 and the total
  goes negative"* is the arithmetic that fits `-1 damage`; **I did not open the
  weapon table to confirm the base.**
- **⚠ I never landed a player on exactly 0.** `§5` is one fight. **10 instances
  in the log is the measurement; watching one remains undone.**
- **⚠ Whether the creature-revival guard still leaks on HEAD** — untested by me,
  and Coder says it does not reproduce. **I only counted the residue.**
- **⚠ `connectionUnreachable`'s WALL branch** — still not exercised; both my
  fixtures produced the floor-cut-off form.
- **⚠ The suppression read** covers `a02` only. I did not check whether an area
  with **no arrivals at all** behaves the same.
- **⚠ The palette's new mode selector** — I read it and did not USE it. **I did
  not paint from the rebuilt palette**, and `terrain` was the only mode I saw
  expanded.
- **Painting tiles** — and still never with a TILESET.

## What I left behind — nothing of mine

    tester-probe   restored from BK16/ — identical
    all 20 saves   restored — byte-identical to SV-T039/
    ⚠ base-rules/rules/event_kinds.toml differs, and it is CODER'S: PT-1618's
      character.dying, written 15:01. Left in place under PT-1617.

**`a02-probe-hall` was rewritten seven times this run and put back byte for
byte; `probe-feeble` had its Strength changed and restored; `a04-probe-slit` was
corrupted, moved away, and returned.**

**Backups: `BK3/`–`BK16/`, `SV-T031/`–`SV-T039/`.**
