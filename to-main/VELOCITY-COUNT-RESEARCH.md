# The Velocity swing count: history and numbers

CODER → MAIN, 2026-11-02 (`PT-2752`). Research only. Nothing in the rules has changed. The app carries the count as one constant per tier (`velocitySwingsTier1/2/3` in `lib/play/declared_attack.dart`), all three set to **three, provisional** until the owner rules (TEST 222 hash, app 238f68e onward).

**The question:** do the Velocity chains (Flurry, Rapid Fire, Saber Swarm) swing 3 / 4 / 5 times by tier, or three times at every tier?

## 1. When 3 / 4 / 5 was written

- Both shapes are in the very first commit of MAIN_WORK, `46aa5ce3` (2026-08-22, "Initial: rules, playtest, agent seeds…"). git cannot order them, so the order comes from what the documents say about each other.
- 3 / 4 / 5 lives in two places in ATTACKS-01 §2:
  - the table: "A Velocity chain — Flurry, Rapid Fire, Saber Swarm | 3 / 4 / 5 by tier";
  - line 46: "all grant three at tier 1, four at tier 2, five at tier 3".
- Neither carries a PT number or a reason.
- **No owner ruling for it was found.** I searched PLAYTEST-RULINGS-01, REGISTER, decisions/, comms/ and HANDOFF for "3/4/5", "four at tier", "four/five strikes/attacks/swings", and "Velocity" with tier or count. Nothing quotes the owner on the count.

## 2. When "three at every tier" was written, and which is later

The documents call 3 / 4 / 5 the **earlier draft**, in three places.

- **ACTION-ECONOMY-01 §7.1, "Velocity does not scale with tier".** It was first committed to comms/ in `a24dfc98` (2026-08-23, the PT-97 sweep):
  > "Flurry, Rapid Fire, and Saber Swarm grant the same number of attacks at every tier. The tiers reduce the penalty."
  > "This is KOTOR's shape. Flurry there gives +1 attack at tier 1, tier 2, and tier 3 alike — −4/−2, then −2/−1, then nothing at all."
  > "An earlier draft had the tiers grant three, four, and five attacks. That made Power and Precision unplayable: both apply their bonus to every attack, and one enhanced swing cannot compete with five ordinary ones. The imbalance was ours, not inherited."
- **ATTACKS-01 §2.3b (`PT-180`)** quotes that same passage as standing law.
- **PREGENS-01 §6, "Every correction, and who found it".** Three independent pre-scenario playtest audits:
  - A = PLAYTEST-PREFLIGHT-01;
  - B = Pre-Scenario Fix Recommendations;
  - C = PLAYTEST-FIXES-01.

  Under "Found by all three": "Velocity frozen at a fixed count per tier … Korr's 'five strikes' struck".

Later documents agree with "three":

- the tier rows (ATTACKS-04 and -05, `attack_tiers`) read "Three strikes" / "Three shots" at tiers 2 and 3;
- FORMS-01, on Ferocity: "ACTION-ECONOMY-01 §421 cut Velocity from five strikes to three to prevent exactly that shape";
- the ruling ledger at line 5246 says the same;
- ATTACKS-01 §3: "Improved Flurry changes the penalty and nothing else … A player who knows what Flurry does knows what Master Flurry does."

**So "three at every tier" is the later rule, a correction found by three audits.** ATTACKS-01 §2's table and line 46 look like the earlier draft, left standing when the rest was corrected.

Two limits on this evidence:

- **The audit documents themselves are missing.** PREGENS-01 and ORCHESTRATOR-HOLDINGS name them, but they are not in the repos.
- **Nothing shows the owner chose 3 / 4 / 5.** If he did choose it deliberately, it was the earlier draft's choice. I found no record of him re-ruling it after the audits.

One ledger line reads the other way: PLAYTEST-RULINGS-01:1196, "The only chain outside Velocity that scales its attack count". It is about Echani Strike (an unarmed chain, 2 / 3 / 4 strikes). It is loose wording beside ATTACKS-07, not a statement on Velocity's count.

## 3. The balance reasoning on record

**For three:**

- ACTION-ECONOMY-01 §7.1, quoted above. Power and Precision put their bonus on one swing, while Velocity multiplies every swing, so scaling the count crowds out both.
- PREGENS-01 §5.2, "Velocity against Power, single weapon" (Korr, level 8, against Defense 19):

  | Declaration | Attacks | Damage | Per round |
  |---|---|---|---|
  | Barrage | 3 | 13 | 27.3 |
  | Crushing Blow | 1 | 23 | 16.1 |

  > "Velocity leads by 70% with a single weapon. Dueling and dual-wielding are the two answers."

  So Velocity already leads at three swings.
- ATTACKS-01 §2.3b: flat riders multiply by the strikes ("A +6 damage rider is +18 on a Barrage"). More swings make every per-hit rider worth more.

**For 3 / 4 / 5:** nothing on record. I found no turn-economy or real-time-speed argument anywhere I searched.

## 4. The numbers: expected damage per round

**Assumptions:**

- **Soldier 8:** PREGENS-01 §5.2's Korr (attack +12 against Defense 19, so a 7 hits before penalties), 13 damage per hit.
- **Soldier 16:** the same gap to the target's Defense, 17 per hit.
- **Weapon:** one vibrosword, threatening 19–20 at ×2.
- **Not counted:** riders (stun, knockback, Defense costs).

| Declaration | Soldier 8 | Soldier 16 |
|---|---|---|
| Strike (no declaration) | 10.4 | 13.6 |
| Flurry t1, 3 swings at −4 | 23.4 | 30.6 |
| Whirlwind t2, 3 swings at −2 | 27.3 | 35.7 |
| Whirlwind t2, 4 swings at −2 | 36.4 | 47.6 |
| Barrage t3, 3 swings at −1 | 29.3 | 38.2 |
| Barrage t3, 5 swings at −1 | 48.8 | 63.8 |
| Power Attack t1 | 12.4 | 15.4 |
| Forceful Slash t2 | 15.0 | 18.0 |
| Crushing Blow t3 | 17.6 | 20.6 |
| Critical Strike t1 | 11.0 | 14.4 |
| Wounding Strike t2 | 14.8 | 18.4 |
| Deathstroke t3 | 24.0 | 28.8 |

My 29.3 and 17.6 at level 8 sit close to PREGENS' 27.3 and 16.1, which left out criticals.

- **Three at every tier:** Barrage is 1.7× Crushing Blow and 1.2× Deathstroke. That is the gap PREGENS already called large, and left to Dueling and two weapons to answer.
- **3 / 4 / 5:** Barrage is 2.8× Crushing Blow and 2.0× Deathstroke, at both levels. Whirlwind at tier 2 (36.4) beats every tier-3 Power or Precision pick. This is the shape §7.1 calls "unplayable".

## Recommendation

**Three at every tier**, as the rows, ACTION-ECONOMY-01 §7.1, ATTACKS-01 §3 and K2 all say.

1. It is the later, corrected rule, found by three independent audits.
2. 3 / 4 / 5 roughly doubles Velocity's lead over the other axes at tier 3.
3. It matches K2.

**If the owner agrees:** correct ATTACKS-01 §2's table and line 46. The code is already at three.

**If he rules 3 / 4 / 5:** change two constants (`velocitySwingsTier2 = 4`, `velocitySwingsTier3 = 5`) and update the TEST 222 bed's expectation. ATTACKS-01 §7.1, §2.3b and §3 would then need rewording to match.
