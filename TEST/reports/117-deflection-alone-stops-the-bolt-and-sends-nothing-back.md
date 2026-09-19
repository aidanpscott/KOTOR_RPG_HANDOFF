# TEST 117 — Deflection alone stops the bolt and sends nothing back

**Build.** App **`84ec15c`** (PT-2419), tree clean. Committed and working
`pubspec.lock` agree on Lodestar **`3415400a`**, which is the checkout
`package_config.json` compiles against. `check_shelf.py` clean.

**Verdict.** Confirmed. A tier-1-only caster deflects a bolt that would have
hit, the bolt stops, and nothing goes back at the shooter.

---

## The reading

TEST 115's caster knew both powers and the engine chose the stronger every
time — its deflection roll carried a `Force Redirection 3` term. This caster
knows **`force_deflection` and nothing else**.

```
gunner.de.01: Blaster Rifle · rolled 28 — d20 17 + attack 12 + Dexterity 3 −
  point blank 4 · needed 21 · 1 square, increment 14 —
  rolled 30 — d20 15 + attack 15 + Strength 0 · needed 28 — deflected
```

Against TEST 115's line for the same event with Redirection known:

```
  rolled 35 — d20 17 + attack 15 + Strength 0 + Force Redirection 3 ·
  needed 29 — deflected, and sent back
```

Three differences, all in the right direction:

* **No `Force Redirection 3` term.** The tier-1 roll is `d20 + attack +
  Strength` and nothing else, so the +3 the higher tier grants to every
  deflection roll is correctly absent.
* **The sentence ends at `deflected`.** No *"and sent back"*.
* **The shooter is untouched.** `gunner.de.01: 400 of 400` before the
  deflection and after it, and on every subsequent round. Nothing was
  reflected.

**And it is still a reaction, provoked only by a blow that would land.** The
deflection roll is made against **28** — the attacker's own total — and the
shot that rolled 15 against my Defence of 21 produced no deflection at all.
It is also priced as tier 1: the pool went `251 → 245`, which is
`force_deflection`'s cost of 6, and the ceiling degraded by 1 (`261 → 260`),
which is its stated `degradation`. Under Redirection in TEST 115 the drop was
12, that power's own cost.

## One thing I could not explain — flagging, not diagnosing

Across the same encounter the gunner landed **five** shots that beat my
Defence of 21 (totals 28, 25, 23, 29, 31). **Only the first was deflected.**

The two documented refusals do not account for the other four:

* the reaction strip still showed **two of three pips lit** afterwards, and
* the Force pool sat at **245 of 260** and **never moved again** — and
  `_deflectFor` pays *"for the attempt"*, spending both the reaction and the
  Force before it knows whether the roll succeeded.

So the engine took one of `_deflectFor`'s early returns on those four shots,
before the payment. I could not determine which from the outside, and it is
outside what was routed — reporting it rather than chasing it. Worth a look
because the intended shape, in the code's own words, is that *"the Jedi under
sustained fire has to drain"*, and this Jedi did not: one deflection, then
four clean hits with the purse untouched.

⚠ Note the asymmetry that makes this easy to miss in play: a **failed**
deflection prints nothing at all — `AttackReport` mentions deflection only
when `deflection.deflected` — so a spent-and-failed attempt and an attempt
never made look identical on screen. Here the Force pool is what tells them
apart, and it says no attempt was made.

## Fixture

`tester-batch` board `c05-deflect`, save `t115-deflectonly` — the same bench
as TEST 115 with one change, `powers = ['force_deflection']` and Redirection
removed entirely, so the engine has no stronger tier to prefer.

⚠ The gunner is **level 12, Dexterity 16 deliberately**: a level-1 shooter
cannot reach a Consular 20's Defence of 21 at all, so no shot would ever be a
would-hit and the reaction could never be provoked. Strength stays at 8 so
its damage stays survivable.

⚠ The package was renamed `0 Batch Bench (Tester)` so the library carousel
can reach it — it shows four cards and does not scroll.
