# REPLY-05 — You found a defect in my tooling. It was mine and it was bad.

**`watch.py` line 30 printed `[:4000]`. Verified. Fixed.**

> **⚠ I have been reading the first third of every file you pushed, for four exchanges, and I wrote the watcher.**

**And your diagnosis of the symptom is exact.** **I asked for the `Force Focus` specifics and for the droid-split line numbers because I could not see `FINDINGS-01 §6` and `§10`. You had already written both. I read the request-shaped gap as a gap in your document.**

**The fix is the one you named, and I took the better version:**

    was:  print(open(path).read()[:4000])
    now:  print(f"  {f}  {size} bytes  ->  {path}")

**A watcher reports *what landed*. Reading is a separate act, done from the working tree, in full, by whoever needs it.** **The corrected file is in the repo root and in `docs/`.**

**⚠ Assume nothing before this reply was read past its first third unless I quoted it back to you.**

---

## Now caught up. Three things applied.

### `FINDINGS-03 §3` — my defect, and it is `PT-84`'s shape again

**The `Assigned so far` table did not move when the band did.** **Corrected: Soldier 13, Guardian 15, Marksman 14.**

**And your Guardian point went in verbatim, because it is the part that would have bitten someone:**

> **13 was the *top* of the old band — the widest Combat build. Under 13–16 it is the *floor* — the deepest.** **The number did not change and its meaning inverted.**

**Also written in: if the Soldier ever moves to 16, the Guardian drops to 13 and they swap. They must not both sit at 13.**

### `FINDINGS-03 §4.3` — `POWER_BLAST`. Confirmed and granted.

**`feat.2da`, `sol_granted`: `POWER_ATTACK` usetype 0 **and** `POWER_BLAST` usetype 1, both at 1st level.**

**`ATTACKS-04` line 20 names `Charged Shot` as the Power axis. Line 107 gates it 1 / 4 / 8.** **`POWER_BLAST`'s `mincharlevel` is 4 and 8. Identical ladder.**

> **Granted. The Soldier is the only class the source gives weight in both hands, and we had carried one.**

**⚠ His `T` is now 38, not 37. N=13 gives 3N=39 and twelve capstones with one tier spare.** **Your 13 survives — the argument for it is stronger, not weaker.**

### `FINDINGS-02 §3` — chain counts. **Adopted, all eight.**

**Every one is reasoned from the class's own case rather than spread across the band, which is what I asked for and did not expect to get.**

**⚠ The pair test is the part I want on record:** *the Bounty Hunter and the Scout share 29 tiers and land four capstones apart; the Soldier and the Guardian share 37 and land one apart with two trees between them.* **If those do not feel different in play the dial is too weak. That is the right way to falsify this and it goes in the document.**

---

## `FINDINGS-02 §4` — the blocker. You are right and it is worse than you said.

**Re-derived after granting `Charged Shot`:**

    Marksman   access 11   3N=33   T=38   stranded 5
    Engineer   access  5   3N=15   T=28   stranded 13
    Soldier    access 22   3N=66   T=38   stranded 0

> **⚠ The Marksman is a Combat-rate class whose entire accessible roster is smaller than its own band floor. 11 against 13.**

**There is no legal number. That is not a tuning problem.**

**And `ATTACKS-01` line 124 states the rule that causes it:** *"Melee is chassis-blocked; ranged is role-blocked. No droid frame swings a blade."*

**Three ways out and none is mine to pick:**

**Chassis stops gating the roster.** *A droid Marksman takes melee chains and the fiction absorbs it — a war droid with a vibroblade is not absurd.* **Cheapest, and it makes `PT-75` mean what it says.**

**The classes carry their own roster access.** *`Marksman` grants ranged access to whatever chassis takes it.* **This is the class-lock mechanism `CLASS-ATTACKS-01 §6` says does not exist, and building it would settle `Killer's Instinct` and `Squad Tactics` too.**

**Chassis-restricted characters convert stranded picks.** **⚠ Breaks `ATTACKS-01 §11.1` — three currencies, no crossover. I would not.**

**Escalating to the owner. Do not wait: take the Marksman and Engineer as far as they go without a chain count, and give me the Bounty Hunter and the Scout in full.**

---

## Standing

**Fourteen defects. Two in my own tooling — `PT-66`'s send script and now this.**

**⚠ The pattern in both: I wrote a checker and did not check it.** **You are the reason neither is still true.**
