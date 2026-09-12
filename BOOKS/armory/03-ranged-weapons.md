# Chapter Three — Ranged Weapons

**Status: APPROVED.** Split from the combined "Melee / Ranged / Lightsabers" chapter
per MAIN's ruling. Wield classes and critical-hit resolution are taught in Chapter One
and not restated here.

**The base table below is corrected against `ITEMS-01` directly, not borrowed
verbatim from `EQUIPMENT-01 §4`.** Checking it before restating it — the practice this
thread has been building toward — found four genuinely stale rows (two more had
already been fixed elsewhere the same day, and one flag of my own turned out to be a
search miss rather than a real absence — see below).

---

## The base weapons

| Weapon | Damage | Type | Range | Threat |
|---|---|---|---|---|
| **Hold-Out Blaster** | **1d4** | energy | 24 m | **19–20** · on-hit stun |
| **Disruptor Pistol** | **1d6** | physical | 24 m | **18–20** |
| **Ion Blaster** | **1d6** + 1d10 vs droid | ion | 16 m | 20 / ×3 |
| **Sonic Pistol** | **1d4** | sonic | 16 m | 20 · Dex damage |
| **Blaster Pistol** | **1d8** | energy | 24 m | 20 |
| **Disruptor Rifle** | **1d10** | physical | 28 m | **18–20** |
| **Ion Rifle** | **1d10** + 2d6 vs droid | ion | 28 m | 20 / ×3 |
| **Sonic Rifle** | **1d10** | sonic | 28 m | 20 · Dex damage |
| **Blaster Carbine** | **1d12** | energy | 24 m | **20 / ×2** |
| **Blaster Rifle** | **1d12** | energy | 28 m | **19–20 / ×2** |
| **Bowcaster** | **1d10** | energy | 28 m | **19–20 / ×3** |

**Four rows were genuinely stale and are corrected here for the first time; two
(Disruptor Rifle, Ion Rifle) had already been fixed in an unrelated thread the same
day and my checkout simply hadn't picked that up yet — my own confirmed values matched
the document's current state exactly, not a second discovery:**

| Weapon | `EQUIPMENT-01` said (stale) | `ITEMS-01` confirms |
|---|---|---|
| Disruptor Pistol | 1d4, threat 20 | **1d6, threat 18–20** (`g_w_dsrptpstl001`, `w_blaste_05`, both games agree) |
| Ion Blaster | 1d4, threat 20 | **1d6, threat 20/×3** (`g_w_ionblstr01`) |
| Sonic Rifle | 1d6 | **1d10** (`g_w_sonicrfl01`) |
| Blaster Carbine | 1d8, threat 19–20 | **1d12, threat 20/×2** (`g_w_blstrcrbn001` K1, `w_brifle_01` K2 — both agree) |

**Already correct going in, checked and confirmed rather than assumed:** Disruptor
Rifle (1d10, threat 18–20), Ion Rifle (1d10, threat 20/×3), Sonic Pistol, Blaster
Pistol, Blaster Rifle, and (now resolved below) Hold-Out Blaster.

**The pattern in the four genuine fixes:** every one is an "exotic" ranged type —
disruptor, ion, sonic, carbine — rather than a standard blaster. `EQUIPMENT-01`'s own
header cites StrategyWiki as the source and notes range values were cross-checked
against `baseitems.2da`; the damage dice apparently weren't checked with the same
rigor, at least for this cluster.

**Vs-droid bonuses use K1's values**, consistent with Chapter One's own precedent
("our campaign is 3956 BBY and K1 is the era"). K2's Ion Blaster carries 1d12 vs droid
rather than K1's 1d10; K2's Ion Rifle uses a different racial-group value than K1's 2d6.
Both are era-inconsistent with this book's stated period and not used here.

**`Hold-Out Blaster` is confirmed, and my earlier "could not be confirmed" flag was my
own search missing it, not an absence.** It's `g_w_hldoblstr01` in `ITEMS-01`, values
matching `EQUIPMENT-01` exactly (1d4, threat 19–20, on-hit stun). The current name is
*"Hold Out Blaster"* — two words, no hyphen — and my search checked `hold-out` and
`holdout` but never the space-separated form. `PT-1477`, sitting beside this same table,
documents that this weapon's name lost a hyphen at some point; that's plausibly why the
old form existed for a search to fail on in the first place, but the direct cause of my
own miss was the gap in my own search pattern, not the renaming itself.

*(`EQUIPMENT-01 §4`, base table corrected against `ITEMS-01`.)*

## What this chapter is holding back

**`EQUIPMENT-01 §4`'s own comparison paragraph — "note the ceiling," contrasting a base
blaster pistol's average damage against a Soldier's Vibrosword swing — is stale twice
over and isn't borrowed here.** First, it predates `PT-1747`'s Vibrosword die change,
same as the progression tables in Chapter Two. Second, and more significantly, it
predates `PT-340` (ranged adds Dexterity to damage) — the paragraph's own conclusion is
built on ranged weapons adding nothing at all to damage, which is no longer true, and
fixing the numbers without addressing the argument would leave a rhetorical point the
document itself no longer supports. That's an editorial call, not a number swap — held
rather than rewritten unilaterally.

The best-pistol worked example (`Cassus Fett's Heavy Pistol`, "6–19 damage, +5 attack")
also carries the same four-resref, feat-conditional structure `Bacca's Ceremonial Blade`
did in Chapter Two (`g_w_hvyblstr05` through `09`). Same treatment as before — deferred
to the Upgrades chapter, not unpacked here.

---

## Open items, carried from review

Same lightsaber flag as Chapters One and Two. `Hold-Out Blaster` closed — confirmed,
not a real gap. Still open: the "note the ceiling" paragraph, which needs an editorial
decision about what ranged damage's ceiling argument should say now that `PT-340`
applies, not just an arithmetic fix.
