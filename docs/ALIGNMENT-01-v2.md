# ALIGNMENT-01 v2 — The Alignment and Force Drift System

**Status: SETTLED.** Two numerical test rounds and one book check. Four defects found and fixed; one authorship claim withdrawn.
**Decision ID: D-AF.**
**Supersedes:** `ALIGNMENT-01` v1.
**Depends on:** `GAP-002` (Branch C), `FORCE-POOL-01 v2` (D-AG), `CANON-01 v2 §9`.
**Sources:** KOTOR 1 `forceadjust.2da`, `globalcat.2da`; RCR pp.180–182.

---

## 0. What changed in v2, and why it matters

**The extractor's read of RCR pp.180–182 corrected four things.** Three are recorded below in place; one is large enough to name here:

> **The drift mechanic is not authored. RCR already has it.**
>
> v1 described "an authored drift mechanic where using dark-side powers pushes the character toward the dark side." **RCR p.181 states that a character gains a Dark Side Point for using a dark side Force-based skill or feat** — automatically, cumulative with the other two sources, listed as a *Major Transgression* and called a clear-cut situation.
>
> **The design was carrying an authorship claim it did not need, and two mechanics were describing one event.** Resolved in §2.1.

**And a fourth defect was found by the extractor rather than by testing** — the absence of hysteresis, §1.2. It is the same failure class as the three the numerical tests caught: invisible in prose, visible the moment a sequence is run.

---

## 1. The scale

**0 (Deep Dark) to 100 (Deep Light), starting at 50 (Neutral).**

KOTOR uses the same range — confirmed by `G_PC_Align_Val` in `globalcat.2da` — so players familiar with the games read the number without translation. The 100-point scale replaced a 55-point proposal that testing found too compressed: characters hit the floor by session 7 and the last several sessions of any fall were mechanically identical.

### 1.1 Seven bands

| Band | Range | Dark Power Cost | Light Power Cost |
|---|---|---|---|
| **Deep Light** | 86–100 | 1.75x | 0.50x |
| **Committed Light** | 72–85 | 1.50x | 0.75x |
| **Leaning Light** | 58–71 | 1.25x | 0.85x |
| **Neutral** | 43–57 | 1.00x | 1.00x |
| **Leaning Dark** | 29–42 | 0.85x | 1.25x |
| **Committed Dark** | 15–28 | 0.75x | 1.50x |
| **Deep Dark** | 0–14 | 0.50x | 1.75x |

**Universal powers always cost 1.0x.**

Multipliers are KOTOR's own, compressed from `forceadjust.2da`'s eleven bands to seven. The extremes (0.50x, 1.75x) match exactly.

### 1.2 Hysteresis — stated directionally, because the symmetric reading breaks it

> **Movement away from Neutral changes band immediately at the threshold. Movement toward Neutral requires three points past it.**

Falling into Committed Dark happens at 28. Climbing back out requires reaching 31. Rising into Deep Light happens at 86. Falling back out requires dropping to 83.

**This must not be implemented as a symmetric deadband around the current band's range.** Under that reading a character rising to 86 stays Committed Light, because 86 falls inside a range extended two points in both directions — and **band entry is blocked along with band exit.** A companion drifting upward toward mastery never arrives; with the player parked at 87, they are stuck below the threshold permanently.

**The symmetric reading silently disables mastery gain by drift**, and it produces zero band flips in testing, which looks like success. A system that never enters a band never leaves one either.

*Found by the mechanics agent while modelling companion alignment drift, after the wording in v1 of this section proved ambiguous enough to implement wrongly.*

> **Without this, band membership strobes.** A character parked at 29 who alternates one Tier-1 dark power (−2) with a minor light choice (+2) crosses the boundary on every single action. Tested at all six boundaries: **72 band flips across 72 actions becomes 6 with hysteresis** — one per boundary, then stability.
>
> Each flip changes both cost multipliers. A power costing 17 becomes 15 becomes 17 again, on consecutive turns, forever.

**RCR does this and we took it from there.** p.182: a character becomes tainted *at* one-half Wisdom but stops being tainted only by reducing Dark Side Points **to one less than one-half Wisdom.** The fall threshold and the recovery threshold are deliberately different numbers.

**You have seen the failure this prevents.** Players reporting they hit Light Side Mastery in KOTOR, took one dark side point, and lost it — that is a single threshold checked in both directions.

**Implementation note.** Band becomes a small piece of stored state rather than a pure function of the score, because it depends on the path taken. This is a mild exception to `RULES-01 §1.2`'s rule that derived values are computed and never stored, and it is the same shape as `CLOCK-01`'s narrative clock: a position history determines, not a value computed fresh.

---

## 2. What moves the needle

### 2.1 Dark power use — and its relationship to RCR's Dark Side Points

**RCR p.181 gives three sources of a Dark Side Point**, cumulative: spending a Force Point to call upon the dark side; using a dark side Force-based skill or feat; performing an evil act. A character doing all three at once gains 3.

> **Our alignment score replaces Dark Side Points entirely.** Same triggers, finer granularity. A character does not hold both a Dark Side Point count and an alignment score — the score *is* the count, expressed on a 100-point scale instead of against Wisdom.
>
> **Stated explicitly because leaving it implicit means two mechanics describing one event.**

**Tiered drift, once per encounter:**

| Power Tier | Drift | In Neutral band | Examples |
|---|---|---|---|
| **Tier 1** | 2 | **1** | Fear, Slow, Wound, Affliction |
| **Tier 2** | 3 | **2** | Choke, Plague, Kill, Lightning |
| **Tier 3** | 4 | **3** | Force Storm, Insanity, Death Field, Drain Life |

> **Drift is assessed once per encounter, at the highest tier used in that encounter.** A character who casts Force Lightning six times in one fight drifts exactly as far as one who cast it once. A character who uses Force Grip and then Force Storm in the same fight drifts by Force Storm's tier alone.

**The moral event is reaching for the dark side, not the number of times the trigger is pulled after.** Deciding to use it is the decision; repetition within that decision is not a second one.

**Two consequences, both intended:**

**Spam within a fight is free, and the Force pool is what limits it.** Six castings of Force Storm cost 120 Force points — `FORCE-POOL-01` caps that long before alignment would. **The pool limits how much you can cast; alignment limits how often you decide to.** Neither needs to do the other's job.

**Concentration is rewarded over dabbling.** Using the dark side decisively in one fight costs less than scattering single powers across three. That is a coherent playstyle and a defensible statement: the Sith who commits in the moment is not more corrupt than the one who reaches for it constantly.

**Verified against the settled profiles.** Spreading dark powers across encounters is unchanged from per-use scoring. Concentrating them reduces drift — six spammed powers in one fight fall from 18 to 3.

**Light power use does not drift alignment.** Staying light is restraint, not grinding — there is no way to farm alignment by spamming Heal. **Universal power use does not drift.**

### 2.2 The partition is open, and less absent than recorded

**The corpus recorded that RCR never defines "dark side Force skill," with the referent absent across five searched locations.** p.181 sits outside that range and carries a partial list: **Drain Energy, Fear, Force Grip, Force Lightning, and Rage.**

**It is an *includes* list, not a closed definition** — so the undefined-category hazard stands and the partition must still be authored. **But "absent" was wrong.** The negative's scope did not reach the page where the partial referent sits, and `GAP-002`'s finding that prior counts were reconstructions rested on absence rather than on open-endedness. **Different problems, different remedies.**

*Note also that `Rage` appears in that list in its feat sense, which is a fifth referent for an identifier already carrying four.*

### 2.3 The Neutral band reduction — what makes grey possible

**Within the Neutral band (43–57), dark power drift is reduced by 1 per use, minimum 1.**

Without it, dark power use generates constant downward pressure that light story choices cannot offset, and any character who touches a dark power at all is on a slow fall. Testing confirmed the grey profile declined monotonically with no equilibrium.

**With it, grey is sustainable but conditional:**

> **And "sustainable" means a tightrope, not a valley.** The equilibrium holds only where session gain exactly equals session drift. **One point of mismatch in either direction walks the character to a pole within 20 sessions.** There is no restoring force pulling a drifting character back toward balance — the position is held by continuous correction, not by the shape of the system.

| Playstyle | 15-session outcome |
|---|---|
| 2× Tier-1 per session + light story engagement | **Stable at 50–51** |
| 1× Tier-1 + 1× Tier-2 per session + light engagement | **Stable at 50** |
| 2× Tier-2 per session + light engagement | **Falls to 21** |
| 2× Tier-1 per session, **no story engagement** | **Falls to 21** |

**Grey is a discipline, not a default.** Available to a character who both restrains the intensity and stays engaged with the moral content. Not available to someone reaching for heavy powers, and not available to someone who uses dark powers and disengages from the story.

**And the protection is lost on exit.** Drift out of Neutral and full drift applies — stay moderate and balance is maintainable, commit and the system stops helping.

### 2.4 Story alignment shifts

**Five tiers each direction.** Packages declare a *tier*, not a number.

| Tier | Light | Dark | Shift |
|---|---|---|---|
| **1** | Meditation, small courtesy | Dark meditation, petty cruelty | ±1 |
| **2** | Kindness costing nothing | Selfishness with a victim | ±2 |
| **3** | Help at real cost | Betrayal, extortion, coercion | ±4 |
| **4** | Heroic act forgoing its reward | Murder, torture | ±8 |
| **5** | Dramatic heroism | Atrocity against many | ±15 |

> **Tier, not value, is the interface.** A package author writes "tier-3 dark act"; the rules pack owns what tier 3 is worth. This gives authors a five-word vocabulary instead of a number line, keeps every package consistent with every other, lets difficulty scaling multiply one table, and means an improvising AI GM makes the identical decision an author makes. A package may override with a raw number for a genuinely special moment, but the tier is the default.

**Tier 5 moves a full band in one act** — the Vader moment in either direction. Rare, GM-judged.

**Magnitudes are scaled from KOTOR's dialogue practice.** The specific values are not extractable (they live in compiled dialogue scripts, not tables), so these are authored against the observed shape.

### 2.5 Meditation

**Long rest with meditation** restores the Force pool and true maximum as any long rest does, and additionally moves the character **1 point toward their chosen side.**

**Short rest with meditation** restores Force points only. No alignment movement.

**The Sith equivalent needs its term sourced.** "Sith meditation" is attested in Legends, but the KOTOR-era term should be confirmed by the wiki researcher rather than authored — it will appear in player-facing text constantly.

**Meditation cannot cross a band boundary away from Neutral.** It moves freely within the current band and stops at the edge; deepening a commitment requires an *act*. **Reflection deepens what you already are; it does not transform you.**

**Movement toward Neutral is exempt** — you can always meditate your way back, you just cannot meditate your way deeper. The asymmetry says something true: falling requires action, recovery permits reflection.

**The opportunity cost is unsettled and is what stops the grind.** A 20-session campaign holds enough long rests that +1 each would dominate every other input. The intended shape: meditating instead of resting normally costs some or all of the rest's physical recovery, so a wounded party cannot afford it. **Blocked on RCR's rest and natural-healing rules — extractor.**

### 2.6 Passive recovery — below 50 only

**No dark powers used for an entire session and score below 50 → +3, capped at 50. Characters at or above 50 receive nothing.**

> **This restriction fixed the system's one blocking defect.** v1 had passive recovery trend toward 50 from both directions, reasoning that a character should not reach Deep Light by doing nothing. The effect was inverted: a disciplined Jedi who never touched a dark power was dragged backward every session, while a curious Jedi who used one dark power per session **disqualified from passive recovery** and kept all their story gains.
>
> **Test result: Profile A (never uses dark powers) ended at 54. Profile B (one dark power per session) ended at 72.** A rational player optimizing for light alignment should have used exactly one dark power per session to dodge the pulldown.
>
> **Fixed and verified: A reaches 82, B reaches 75.**

**Alignment above neutral is maintained by not using dark powers, not by grinding.** A Deep Light character who stops acting holds position — they neither climb nor decay.

### 2.7 Wisdom resistance

**Half the Wisdom modifier, rounded down, subtracted from total session drift — minimum 1 if the modifier is +1 or better.**

**And a floor on the result: if any dark power was used at all, net drift is never less than 1.**

> **The floor closes a hole that per-encounter scoring opened.** A single Tier-1 power inside the Neutral band drifts 1 after the band reduction. Wisdom resistance of 1 cancels it exactly — so a Wisdom 12 or better character using one mild dark power per fight, in Neutral, took **zero** drift.
>
> **That is the v1 test's blocking failure returning by a different route.** The original defect was that dabbling had no consequence; it was fixed by raising drift to 2, and the band reduction plus resistance had quietly restored it.
>
> **Tested: the grey profile concentrating two Tier-1 powers in one fight drifted to 59 — into Leaning *Light* — while using the dark side every session.** With the floor, it holds at 51. **Nothing else moves.**

**Reaching for the dark side always costs something.**

| Wisdom | Modifier | Resistance |
|---|---|---|
| 10–11 | +0 | 0 |
| **12–13** | **+1** | **1** |
| 14–17 | +2 to +3 | 1 |
| 18–19 | +4 | 2 |

**The minimum-1 floor smooths a cliff.** Under plain `floor(mod/2)` a Wisdom 13 character got zero — identical to Wisdom 10 — while 14 got 1. Wisdom 12–13 is common on non-Consular builds.

**Resistance buffers temptation without licensing sustained use.** Against one Tier-1 power it halves the drift; against a heavy session it is barely noticeable. A wise character resists the occasional lapse, not a committed descent.

---

## 3. Atonement — four routes, gated by depth

**RCR's structure, adopted with one deliberate departure.**

| Route | Effect | Cost | Available |
|---|---|---|---|
| **Meditation** | +2 per Force Point sacrificed | A character resource, spent in downtime. No scene needed. | **Not in Deep Dark** |
| **Heroic act forgoing its reward** | +8 (tier 4) | A scene, *and* you forgo the Force Point the act would have earned | Any depth |
| **Dramatic heroism** | +15 (tier 5) | Extreme personal cost, selfless, significant to the galactic balance. GM-judged. | Any depth |
| **Accepting a companion's pull** | +1 per session accepted | Requires influence 75+ with a companion on the other side, and the player's active choice each session. **See `INFLUENCE-01 §5`.** | Any depth |

**These are three different kinds of thing, not three sizes of one thing.** RCR p.182 makes meditation a downtime resource cost — *a period of meditation, reflection, and absolution*, explicitly able to occur between adventures without being played out. The heroic act is a scene that trades a mechanical reward for moral recovery. Dramatic heroism is a story beat with stated qualitative criteria.

**Meditation closes at Deep Dark**, matching RCR's rule that a dark character cannot rid himself of Dark Side Points by atoning. **You cannot think your way out of being a Sith Lord.**

### 3.0 The fourth route is different in kind

**Meditation, the heroic act, and dramatic heroism are all things the redeemed character does.** The companion pull is not.

> **A dark-side character who keeps accepting the pull from a light-side companion, and swings far enough, has been redeemed by a relationship rather than by deeds.**

It is slow — 1 point per session, roughly 38 sessions from the floor to Neutral if it were the only route, so in practice it accelerates an arc rather than carrying one. It requires sustained closeness to someone on the other side. **And it is the only route back that depends on another character rather than on the redeemed character's own actions.**

**It is also the most Star Wars version of redemption there is.** Vader does not atone through good works; he is pulled back by his son.

**Full mechanism in `INFLUENCE-01 §5`.** Recorded here as well because an atonement route documented only in the influence system would not be found by anyone reading about redemption.

### 3.1 The departure: any route accumulates

**RCR says that at Dark, *only* dramatic heroism works** — lesser heroic acts do nothing at all.

**We permit accumulation.** A dark-sider performing multiple heroic acts climbs out. From Deep Dark to Neutral is roughly 38 points — about five tier-4 acts or ten tier-3 ones. A real arc, and it sits in the player's hands rather than waiting on the GM to supply one specific kind of scene.

**This is a departure toward the games rather than away from them.** KOTOR lets you accumulate back from anywhere; the only-dramatic-heroism gate is RCR's addition. Consistent with the rest of the system's lean.

### 3.2 The consequence worth stating plainly

**Mastery bonuses are losable** (§4). So **the first step of redemption costs you the bonus.** A Deep Dark Sith Lord with +3 Strength begins atoning, crosses out of Deep Dark, and loses it immediately.

**That is a good dramatic beat and the player-facing text should say so plainly** rather than letting it arrive as a surprise. Turning from the dark side costs you power, visibly, before it gives you anything back.

### 3.3 The Wisdom check — RCR has a fall trigger we do not

**RCR p.182:** after becoming tainted, each new Dark Side Point forces a **Wisdom check at DC 10 + Dark Side Points possessed.** Fail it, or reach Wisdom in points, and you are *dark*.

**This is a fall trigger, not merely feedback.** A tainted character does not have to accumulate to the threshold — they can fall at any moment, on any new point, with the odds worsening as they hold more.

**It does not port by substitution.** On a 100-point scale, "points possessed" produces DCs no d20 can meet.

**Not adopted, recorded as a deliberate omission.** An equivalent — a check on each dark power use below Neutral, DC scaled to depth, failure dropping a full band — is thematically excellent and is the one piece of RCR's dark-side machinery we drop entirely. **Owner decision, deferred.**

---

## 4. Mastery at the poles

**Reaching Deep Light or Deep Dark grants a class-appropriate attribute bonus. Dropping below the threshold loses it.**

**This is KOTOR's design and we take it whole.** Community sources agree on the shape — +3 to an attribute, varying by class, with base and prestige class bonuses stacking, and companions receiving it too at high influence. **They disagree on which attribute for Consular and Watchman**; two accounts conflict and neither is data. Marked as needing the actual table.

> **Two feats named `DARK_SIDE_CORRUPTION` and `LIGHT_SIDE_ENLIGHTENMENT` exist in `feat.2da`, but they are *not* the mastery bonuses.** Both are prestige class grants — Sith Lord at level 1 and Jedi Master at level 1 respectively, unavailable to everyone else. Their effects are string references into `dialog.tlk` and unreadable from the data.
>
> **Recorded because the integrator initially asserted these were the mastery mechanism from memory, and the file said otherwise.**

**Losable is the important property.** It makes the poles an achievement to hold rather than a state to reach, and it is what gives §3.2 its bite.

---

## 5. The feedback loop, stated

**As a character drifts dark, dark powers get cheaper, tempting more use, driving faster drift.** Intentional. The fall accelerates once it starts.

**The counterweights are deliberate and limited:** the Neutral band reduction slows the start; Wisdom resistance buffers small lapses; passive recovery only helps below 50 and only when dark use stops entirely; atonement requires GM-awarded moments.

**Verified fall behaviour:**

| Profile | 10-session outcome |
|---|---|
| Pragmatist — Tier-1 + Tier-2 per session, Wis 12 | **14 — Deep Dark, not floored** |
| Falling Jedi — escalating to Tier-1+2+3, Wis 10 | **0 — floored at session 8** |

Two bands and 14 points apart. In the pre-fix test they converged at the floor.

---

## 6. Redemption, verified

From a floored character (score 0):

| Session | Action | Score | Band |
|---|---|---|---|
| 11–13 | Restraint, passive recovery | 3 → 9 | Deep Dark |
| 14 | **Atonement** + passive | 20 | Committed Dark |
| 15–16 | Minor light choices + passive | 25 → 30 | Committed → Leaning Dark |
| 17 | **Relapse** — one Tier-2 power | 27 | back to Committed Dark |
| 18 | Restraint, passive | 30 | Leaning Dark |
| 19 | **Atonement** + passive | 41 | Leaning Dark |
| 20 | Restraint, passive | 44 | **Neutral** |

**Ten sessions from floor to Neutral**, against ten sessions to fall. The symmetry is coincidental rather than designed but lands defensibly. **The relapse costs three points and one band**, taking a session and a half to undo — a failure that matters without resetting the arc.

**If it proves too forgiving in play, the lever is atonement frequency, not any drift number.**

---

## 7. Difficulty scaling and the exception flag

**Multiply dark drift rates by a campaign factor. Change nothing else.** Standard 1.0, Strict 1.5.

Under strict, a curious Jedi drops from Committed Light to Leaning Light — ten points and one band. **Dark powers become expensive, not forbidden.**

**Do not tune parameters independently.** Testing found separate "forgiving" and "strict" sets both broke: forgiving made dabbling completely free while still crushing heavy users; strict made a single dark power per session catastrophic. The ratios between drift, recovery, and atonement are load-bearing. **One knob.**

**Revan, the Exile, and Kreia are exempt from per-use drift** — `alignment_drift_immune: true`. Alignment moves only through story choices and GM awards. Revan's alignment is defined by player choice rather than mechanism; the Exile is a wound in the Force; Kreia rejects the binary explicitly. **Also the right shape for campaign configuration** — a grey-Jedi campaign sets it for the whole party.

---

## 8. Corrections carried from the extractor's book check

**Three, beyond the drift-authorship correction in §0:**

**The `+4/−8` figures are the *dark* tier, not the rule.** RCR has two: **Tainted at +2/−4** (Dark Side Points equal to half Wisdom) and **Dark at +4/−8** (equal or exceeding Wisdom, *or* failing the Wisdom check). **Multiple project documents cite `+4/−8` unqualified**, including `CANON-01 v2 §9`, `METHOD-RECORD-01 §1.3`, and `GAP-002 §3.1`. The full rule was captured once in `DECISION-GAP-001b §1` and the half that travelled was the dark tier. **Neither figure is live in this system** — we replaced check modifiers with cost multipliers — **but the corpus should be corrected**, because `GAP-002` still uses `+4/−8` as its example of the rule with no defined referent, and that framing now gets both the tier and the absence wrong.

**A fourth undefined-category instance.** RCR's `blinded` entry carries *any other skill check for which the GM deems sight to be important* — named example, open-ended, nothing closed. Joins the register alongside *skills requiring patience and concentration*, *dark-side and light-side Force skills*, and *mind-influencing Force skills*.

**A Wookiee interaction.** RCR p.182 sidebar: Wookiee Force-users do **not** gain Dark Side Points for using rage naturally, but **do** if they incorporate rage with any Force skill. While raging a Wookiee Force-user **cannot call upon the Force except to call upon the dark side.** This is a third referent for `Rage` in the dark-side rules, and the sidebar treats the species trait and the feat as separable — the collision register should note it.

---

## 8B. Two proposals tested and declined

**Recorded rather than dropped, per the rule that two corrections in this project were only recoverable because a rejection had been written down.**

### 8B.1 — Position-scaled story shifts. Declined.

**The proposal:** shift magnitude scales with current position, as KOTOR does — the same deed awarding fewer points the further a character already is toward that pole, on a 1/2/4/6/8/10 ladder, with odd values exempt from scaling.

**The appeal:** it makes arriving at a pole an achievement rather than an accumulation, and the final stretch a genuine grind.

> **It does not do that. Sessions to Deep Light: 6 flat, 7 scaled.**

**Why it fails.** Scaling only reduces awards *near* the pole. The journey from 50 to 86 spends most of its length where the multiplier is still 1.00 or 0.75. Every shape tested crosses the first two band edges on the same session; scaling adds one session at the very end.

**Only a falloff measured from the origin moves it meaningfully — 10 sessions — and that abandons the premise**, since a Neutral character would receive 5 for a major deed instead of 8.

**Nothing settled would have moved either, and structurally so.** The redemption arc runs 0→43, the grey equilibrium sits at Neutral, and passive recovery is 3, which is odd and therefore exempt. **All three live at or below Neutral; scaling only acts above it.**

**If mastery should take longer, the lever is tier values or deed frequency — not scaling.**

*(A linear shape was the better of the two tested. Stepped is discontinuous at 58, 72, and 86 — one point of movement would cost 25% of every later award, and at 86 a major deed would halve from 4 to 2. Playable against, and it reads badly.)*

### 8B.2 — Position-scaled power drift. Declined, and it would have inverted the tiers.

**The odd-value exemption breaks on consecutive values.**

Story shifts survive the exemption because their ladder is 1/2/4/6/8/10 — **the odd values sit between the even ones**, so exempting them disturbs nothing.

**Drift tiers are consecutive: 2, 3, 4.** Exempt the 3 and it stops shrinking while the 2 and the 4 continue shrinking around it.

> **A Tier-2 power would drift a character further than a Tier-3 across the entire dark half of the scale — at 7 of 15 sampled positions.**

**Force Lightning corrupting faster than Force Storm is nonsense, and a player would notice within two sessions.**

**Drift stays flat.**

### 8B.3 — One finding that outlived both proposals

**The grey equilibrium is a knife edge, not a basin.**

It holds only where session gain exactly equals session drift. **One point of mismatch in either direction walks the character to a pole within 20 sessions.**

**This is independent of scaling and was found while checking it.** `§2.3` describes grey as sustainable, which is true — but it is sustainable the way a tightrope is, not the way a valley is. **The section should be read that way.**

---

## 9. Change log

| Version | Change | Cause |
|---|---|---|
| v1 | 55-point scale, flat drift | Initial design |
| v1 | 100-point scale, tiered drift, Wisdom resistance, story shifts | Test 1: dabbling had zero consequence; the fall was a cliff |
| v1 | Passive recovery below 50 only | **Test 2: the disciplined Jedi scored lower than the dabbling one — systemic inversion** |
| v1 | Neutral band drift reduction | **Test 2: grey declined monotonically with no equilibrium** |
| v1 | Wisdom resistance minimum 1 | **Test 2: cliff at Wisdom 14 left 12–13 unprotected** |
| **v2** | **Hysteresis at band boundaries** | **Book check: RCR has it, we did not. 72 flips in 72 actions at the boundaries.** |
| **v2** | Drift authorship withdrawn; score replaces Dark Side Points | **Book check: RCR p.181 already awards a point for dark-power use** |
| **v2** | Four-route atonement, depth-gated | **Book check: RCR p.182 is richer than a flat award** |
| **v2** | Story tiers become the package interface | Consistency and difficulty scaling |
| **v2** | Mastery at the poles, losable | KOTOR's design, adopted whole |
| **v2** | **Drift assessed once per encounter, at the highest tier used** | The moral event is the decision to reach for the dark side, not the repetition after |
| **v2** | **Minimum 1 net drift whenever a dark power is used** | Band reduction plus Wisdom resistance had restored v1's blocking failure — dabbling cost nothing |
| **v2** | Position-scaled story shifts declined | 6 sessions flat vs 7 scaled. Scaling acts only where the journey has already ended. |
| **v2** | Position-scaled drift declined | The odd-value exemption inverts consecutive tiers — Tier 2 would out-drift Tier 3 |
| **v2** | `+4/−8` recorded as the dark tier; referent recorded as open, not absent | **Book check: p.181 names five, outside the recorded search scope** |

---

## Drift from combat — the Ferocity rule

**`ATTACKS-06` introduces the only source of alignment drift that comes from a combat choice rather than a narrative one.**

**Form VII, Ferocity — Juyo — runs on anger.** *"Juyo not only employed a fiercely aggressive offense but also necessitated that practitioners actively harness their anger and negative emotions to fuel the constant attack."*

| Band | Drift per encounter in which a Ferocity attack is declared |
|---|---|
| **Deep Light** · **Committed Light** · **Leaning Light** | **2 points** |
| **Neutral** | **1 point** |
| **Leaning Dark** · **Committed Dark** · **Deep Dark** | **None** |

**Charged once per encounter regardless of how many Ferocity attacks are declared in it.**

### The floor

> **Drift from this rule alone cannot carry a character past the Leaning Dark threshold.**

**Reaching Committed Dark or beyond requires choices made in play.** *A Jedi who fights with Juyo becomes someone who is slipping. Becoming Sith is still something you do, not something a lightsaber form does to you.*

### Why the floor exists

**Without it the rule is self-accelerating with an absorbing state.** **A light-band Jedi using Ferocity drifts toward the bands where it costs less, and eventually to where it costs nothing.**

> **This document already carried a defect of that exact shape — a permanent zero-drift hole. The Ferocity rule without a floor is its mirror: a permanent drift slope with an absorbing state at the bottom.**

### Interaction with hysteresis

**§1.2's asymmetric hysteresis applies unchanged.** **Ferocity drift is drift** — it moves the number, and band membership is resolved by the existing rule. **A character sitting one point above a threshold and using Juyo crosses immediately; climbing back out still requires three points past it.**
