# EQUIPMENT-01 — Weapon Damage and the Defence Formula

**Source: StrategyWiki's KOTOR weapon tables and the Neoseeker ranged reference.** `source_system: kotor_game`, secondary. **Range values cross-checked against `baseitems.2da` and identical.**

---

## 1. Two findings that matter more than the numbers

> **Melee adds Strength to both attack and damage.** **⚠ Ranged adds Dexterity to damage — `PT-340`.**

*"Strength modifier is added to both Attack and Damage."* *"Ranged weapons do not get a bonus to damage from STR or DEX, so they can easily be outpaced by melee weapons."*

**That single asymmetry is why melee dominates late in both games**, and it is the reason our ranged Power chain — Charged Shot → Power Shot → **Blast**, +5/+8/+10 — **is doing more work than its melee mirror.** **A blaster's damage comes almost entirely from the attack you declare.**

> **Defence = 10 + armour bonus + Dexterity modifier, and the Dexterity contribution is capped by the armour.**

*"A character under attack will compare your attack roll to their defense, which is calculated as 10 + armor bonus + DEX. The DEX bonus to defense may be capped by your armor."*

**Heavier armour gives more Defence and a lower Dexterity cap.** **⚠ The specific values per armour class are still absent — see §5.**

---

## 2. Melee — base weapons

| Weapon | Damage | Type | Threat | Balanced | Attacks |
|---|---|---|---|---|---|
| **Stun Baton** | **1d4** | bludgeoning | 20 / ×2 | — | 1 |
| **Short Sword** | **1d6** | piercing | 20 / ×2 | **yes** | 1 |
| **Quarterstaff** | **1d6** | bludgeoning | 20 / ×2 | **yes** | **2** |
| **Gaffi Stick** | **1d8** | piercing | 20 / ×2 | **yes** | **2** |
| **Vibroblade** | **1d10** | piercing | **19–20 / ×2** | **yes** | 1 |
| **Wookiee Warblade** | **1d10** | slashing | 20 / ×2 | **yes** | **2** |
| **Long Sword** | **1d8** | slashing | 20 / ×2 | no | 1 |
| **Battleaxe** | **1d12** | slashing | 20 / ×2 | — | 1 |
| **Vibrosword** | **1d12** | slashing | **19–20 / ×2** | no | 1 |
| **Double-Bladed Sword** | **2d6** | slashing | 20 / ×2 | **yes** | **2** |
| **Vibro Double-Blade** | **2d8** | slashing | 20 / ×2 | **yes** | **2** |

**⚠⚠ LONG SWORD AND SHORT SWORD ARE DISTINCT AGAIN — `PT-2198`.** `1d8` against `1d6`. This paragraph read *"Long Sword is now mechanically identical to Short Sword, which is known and accepted"* from `PT-2011` until `PT-2198`, and the ruling that changed it cites this very sentence as its reason: two weapon categories a player would expect to feel different were indistinguishable in **every mechanic that actually runs**, separated only by a `damage_type` label nothing read.

**⚠ THE THREE MISSING LINKS ARE STILL MISSING, AND THAT IS WHY THE DIE HAD TO CARRY IT.** A weapon carries a kind, damage application takes one, a target resists it — `weaponFromBase` still takes damage, threat and range and no type. The overlap was accepted for as long as it was, rather than patched cosmetically, precisely so that the fix would not need undoing when that chain is built; raising the die is not that patch, because it distinguishes them on the one column every program already reads.

**⚠⚠ BATTLEAXE IS ITS OWN BASE TYPE AT `1d12` — `PT-2227`. THE NAME IS OURS; THE DIE IS THE GAME'S.** `PT-2200` made this its own base type at `1d10`, reasoning that the row called `Gamorrean Battleaxe` folded a base type and its best-known example into one thing. **The rename stands. The `1d10` is withdrawn — it was inferred from `Long Sword`'s shape and that shape does not hold here.**

**⚠⚠ `PT-2227` — A FOUR-SOURCE SWEEP, AND NO PLAIN AXE EXISTS ANYWHERE IN EITHER GAME.** The question `PT-2200` never asked was whether the second case shared the first one's structure. It does not:

    baseitems.2da        ONE axe row in each game, row 80, and its LABEL IS
                         `Gammorean_Battleaxe`. 1d12. No generic axe row.
    templates.bif        5 axe items across 1,550 blueprints. All Gamorrean —
                         the fifth is `propga01`, `{Prop GA 01}`, a dev prop.
    every module         532 archives, 374 distinct `.uti`, 0 unparsable.
                         ONE more, K1's g_w_waraxe002 — also Gamorrean.
                         ⚠ IT IS NOT IN THE ITEM HOLDINGS and the resref is
                         deliberately not cited as one: `data/items/` is
                         `templates.bif` only, and `audit_resrefs` is right to
                         say we do not hold that file.
    dialog.tlk           49,369 and 136,551 strings. Every short string
                         naming an axe is Gamorrean. Not one plain one.

**⚠⚠ AND `Long Sword` IS THE CONTRAST RATHER THAN THE PRECEDENT.** A PLAIN ITEM exists for it in both games — `g_w_lngswrd01` *"Long Sword"* and `w_melee_02` *"{02}Long Sword"* — with the named variants above it. **That is a real base-plus-variant shape, visible in the source.** The axe has no plain item at all, and **the game itself names the base item after the species.** The folding `PT-2200` identified is the GAME's, not the document's, and renaming it is us generalising a shape the source never had.

**⚠ THE ONE PIECE OF EVIDENCE POINTING THE OTHER WAY, KEPT:** row 80's default model is `w_waraxe`, a generic war-axe resref rather than a Gamorrean-specific one. **That is an art asset name, not a rule** — but it is the only trace of a generic axe in either game and it is recorded rather than dropped to keep the case tidy.

**⚠⚠ SO THE DIE IS `1d12`, AND IT IS ATTESTED TWICE OVER WHERE `1d10` WAS ATTESTED NOWHERE.** `baseitems` row 80 says `1d12` and this document's own Weapon column says `1d12` for all five catalogue rows. **⚠ `baseitems` IS NOT THE AUTHORITY FOR THAT COLUMN — `PT-2195` settled that, and `Long Sword` is the proof: its own `baseitems` row reads `1d12` while this table carries `1d8`.** The point is not a hierarchy. It is that two sources free to disagree, and which do disagree elsewhere, **agree here**, and nothing supports the third number.

    Battleaxe                    —      1d12   ⚠ the base type, and the game's
    Gamorrean Battleaxe        20cr     1d12   ⚠ states the base and no more
    Gamorrean War Axe         800cr     1d12 + 1d8 slashing
    Gamorrean Cleaver        4000cr     1d12 + 1d12 slashing
    Arg'garok               18500cr     1d12 + 1d12 slashing + 1d12 slashing

**⚠ THE FAMILY STILL LADDERS, ON THE RIDERS RATHER THAN ON THE DIE.** The three named axes sit above the base on the slashing bonuses the source actually gives them; the `Gamorrean Battleaxe` and the prop merely repeat `1d12` and so state nothing of their own, which is correct — **repeating a number is how two copies of it start to disagree.**

**⚠ AND NOTHING IS HIDING UNDER ANOTHER BASE TYPE.** `PT-2200` asked whether any axe-type item sat miscategorised the way the Force Pike sat under `Quarterstaff`. The same sweep answers it: **zero.** Not one axe-named item in either game sits on any base but row 80.

**⚠⚠ AND THEY ARE NO LONGER OVERRIDES AT ALL — `PT-2227`.** Under `1d10` all four stated `1d12` as an item-level override, which `check_weapon_dice` validated against the item's own `baseitems` row. With the base at the game's own `1d12` there is nothing to override: **the items agree with their base type**, and `check_weapon_dice` has one fewer exception to carry rather than one more. A sixth item claiming `2d12` would still fail, on the same check.

**⚠⚠ STUN BATON IS 1d4 BY OWNER RULING, AND IT IS NOT AN INVENTED NUMBER.** The source reads a flat **1** — not a die at all — and K2's own baton family already ladders `1d4 · 1d6 · 1d8 · 2d8` across the four tier bands, one weapon each. **`1d4` is exactly what K2 ships at tier 1**, on the 75-credit Energy Baton, so this restores a value the data already carries at that price rather than choosing one.

**⚠ AND THE FAMILY IS THE DAGGER ARCHETYPE** — light and fast, favouring threat range and finesse-style properties over raw damage. Carry that into any later question about this family's threat range or finesse eligibility; it is context, not a change to the values above.

**⚠⚠ LONG SWORD IS 1d8 BY OWNER RULING — `PT-2198`, AND IT IS THE BASE TYPE ALONE.** The source reads 1d12; every one of the ELEVEN weapons that inherits from this base type — including Naga Sadow's Poison Blade and the 24,000-credit **Shyarn** — also reads 1d12, so the family had **a 720× price spread and zero die variation**: the whole difference between the cheapest and the dearest was carried by properties.

**⚠ THREE RULINGS, AND ALL THREE STAY VISIBLE.** The figure has moved twice and the DESIGN once, and they are not the same event:

    PT-2000   1d8   base drops, named variants keep a flat 1d12
    PT-2011   1d6   ⚠ THE DESIGN CHANGES — flat variant dice are replaced
                    by a bonus ladder on the base
    PT-2198   1d8   the ladder is kept exactly; only the number it starts
                    from moves back up

**⚠⚠ `PT-2198` SUPERSEDES `PT-2011`'s FIGURE AND KEEPS ITS DESIGN.** That distinction is the whole of it. The bonuses are untouched and now stack on the new base:

    Long Sword                    25cr   1d8
    Krath War Blade              150cr   1d8 + 1
    Trandoshan Sword            2050cr   1d8 + 4 slashing
    Naga Sadow's Poison Blade  10000cr   1d8 + 3
    Shyarn                     24000cr   1d8 + 5 slashing

⚠ A BLOCK RATHER THAN A TABLE, AND THE EXTRACTOR IS WHY. Written as markdown
rows this sat inside `Melee - base weapons`, a six-cell section, and
`extract_equipment` refused the whole file: *"the row at EQUIPMENT-01.md:59 has
3 cells and this section is 6 wide."* It was right to — a short row shifts every
column after the gap. The ladder is prose here, not a table this document's
parser has to widen for.

**⚠ AND THE PARAGRAPH THAT STOOD HERE WAS STALE FOR FIVE WEEKS.** It read *"SO THE NAMED WEAPONS KEEP 1d12 AND ONLY THE BASE DROPS"* — `PT-2000`'s design, which `PT-2011` replaced outright with the ladder above. The number in the heading was corrected at `PT-2011` and the reasoning under it was not, so the section argued for a design the project had already abandoned. *A name that outlives its rule*, in prose rather than in code.

**⚠⚠ AND THE LADDER REACHED A FIGHT FOR THE FIRST TIME AT `PT-2194`.** Every one of those bonuses sat in the catalogue unread from `PT-2011` until the damage reader was built: `weaponFromBase` took the base type's die and nothing else, so Shyarn swung the same dice as the 25-credit sword for five weeks. The ladder is only worth the number it starts from because something finally reads it.

**⚠ LIGHTSABERS ARE EXCLUDED FROM THIS EXERCISE ENTIRELY**, ruled, as are the base types not yet decided — Vibroblade, Vibrosword, and every ranged type. **`Battleaxe` was on that list until `PT-2200` decided it**, below.

> **The "Attacks" column confirms our double-blade ruling.** **Quarterstaff, Gaffi Stick, Wookiee Warblade, and both double-bladed types are marked 2.** **Every one is also *Balanced*, which is exactly the reduced penalty `ACTION-ECONOMY-01 §7.6` gives them.**

**And the trade is visible in the threat range.** **A vibrosword threatens on 19–20; a double-bladed sword of identical damage threatens only on 20.** *"Capable of inflicting more damage — but also less precise — than the single-bladed variant."*

**Balanced weapons give +2/+0 against the two-weapon penalty when used off-hand.**

---

## 3. Melee — the progression

**Three points on the curve, all vibroswords, to see how far upgrades move the number.**

| | Damage | Threat | Attack |
|---|---|---|---|
| **Vibrosword** *(120 credits)* | **1d12** | 19–20 | — |
| **The One's Vibrosword** *(mid)* | **1d12 +5** | 19–20 | **+5** |
| **Bacca's Ceremonial Blade** *(2,480)* | **1d12 +4**, +4 energy, **+2d6 vs droid** | 19–20 | **+4** |
| **Baragwin Assault Blade** *(9,000)* | **1d12 + 2d6 energy + 2d6 sonic** | **17–20** | **+5** |

**And the best double weapon:**

| | Damage | Threat | Attack |
|---|---|---|---|
| **Vibro Double-Blade** *(180)* | **2d8** | 20 | — |
| **Yusanis' Brand** *(8,000)* | **2d8 +2**, +3 fire, **+6–9 ion vs droid** | **19–20** | **+3**, on-hit stun |

> **Base to best is roughly 7 average damage to 24**, plus an attack bonus of +5 and a threat range doubled from 10% to 20%. **A factor of three on damage across a campaign.**

---

## 4. Ranged

| Weapon | Damage | Type | Range | Threat | ⚠ Extends perception |
|---|---|---|---|---|---|
| **Hold Out Blaster** | **1d4** | energy | 24 m | **19–20** · on-hit stun | — |

> **⚠ THE HYPHEN GOES — `PT-1477`.** `BUILD 55` found **four classes unarmed by one character.** This document spelled it **Hold-Out Blaster** (the old spelling, quoted not cited); **`STARTING-EQUIPMENT-01` spells it without the hyphen 13 times and `ITEMS-01` once.** **Fifteen to one, and this was the one.**
>
> **⚠ And the catalogue is closest to the source** — `g_w_hldoblstr01` is the game's own resref, and `ITEMS-01..09` were converted from the shipped files. **The outlier is the document furthest from where the name came from.**
>
> **`Coder` did not normalise the matcher, and that was right:** *a matcher that stripped hyphens and case would resolve the eleventh name and would also quietly resolve the next one that only looks close* — **which is how a Remote ended up in Dockworker's Treads.**
| **Disruptor Pistol** | **1d6** | **unstoppable** | 24 m | 18–20 | — |
| **Ion Blaster** | **1d6** | ion | **16 m** | 20 · ×2 | — |
| **Sonic Pistol** | **1d4** | sonic | **16 m** | 20 · Dex damage | — |
| **Blaster Pistol** | **1d8** | energy | 24 m | 20 | — |
| **Heavy Blaster** | **1d10** | energy | 24 m | 20 | — |
| **Disruptor Rifle** | **1d10** | **unstoppable** | 28 m | 18–20 | — |
| **Ion Rifle** | **1d10** | ion | 28 m | 20 · ×2 | — |
| **Sonic Rifle** | **1d10** | sonic | 28 m | 20 · Dex damage | — |
| **Blaster Carbine** | **1d12** | energy | **24 m** | 19–20 · ×2 | — |
| **Blaster Rifle** | **1d12** | energy | 28 m | 19–20 | — |
| **Marksman Rifle** | **1d10** | energy | **40 m** | **19–20** | ⚠⚠ **yes** |
| **Sniper Rifle** | **1d12** | energy | **50 m** | **19–20** | ⚠⚠ **yes** |
| **Repeating Blaster** | **2d6** | energy | 28 m | 20 | — |
| **Heavy Repeating Blaster** | **2d8** | energy | 28 m | 20 | — |

> **⚠ TWO BASE TYPES ADDED — `PT-1473`, owner ruling — PLUS A THIRD, `PT-1783`.** `BUILD 53` found both named by a class array with nothing to map to. **A name that no base type carries is not a mapping problem; it is a missing row.**
>
> **`Marksman Rifle` — 1d10, 40 m, threat 19–20.** ⚠ **Revised at `PT-1783` — was `1d12`.** Blaster Rifle's dice at **longer range**: the same weapon reworked for reach, which is what the class it arms is for. **It is not a `blaster-rifle` alias** — `EQUIPMENT-01` already distinguishes four rifles by damage type, and this one differs on the columns that matter to a marksman.
>
> **⚠⚠ `Extends perception` IS `PT-1782`, AND IT CARRIES NO NUMBER OF ITS OWN.** The ruling is that the weapon extends its wielder's perception range **to match the weapon's own range** — so the distance is the `Range` column already beside it. **A second number in this column could disagree with that one**, and two fields answering one question is a defect this corpus has a name for.
>
> **⚠ AND IT IS A COLUMN BECAUSE A TABLE THAT IS EXTRACTED CANNOT BE READ FROM ITS PROSE.** The property was ruled at `PT-1782` and stated in the note below for two slices while `equipment.toml` shipped both rifles without it — *ruled and unbuilt*, which is exactly how `PT-1718` sat for months. `PT-1791`.
>
> **`Sniper Rifle` — `PT-1783`, owner ruling. 1d12, 50 m, threat 19–20, energy.** A new, separate weapon from `Marksman Rifle`, not a rename — the longer of the two rifles by both die and range. Carries `PT-1782`'s perception-extension property, alongside `Marksman Rifle`: passive, respects line of sight, extends the wielder's perception range to match the weapon's own range.
>
> **`Training Lightsaber` — 1d8, threat 19–20.** **⚠ NOT 2d10.** `lightsaber` is a war blade and **giving a padawan's practice weapon a master's dice is a ruling, and this is it.** A step below the `Short Sword`'s cousin and well below the real thing — **it is what you learn on.**
>
> **⚠ And `PT-1472` still governs the crystal:** a Training Lightsaber **carries a colour crystal like any other**, and the crystal supplies properties while **the base supplies these dice.**
| **Bowcaster** | **1d10** | energy | 28 m | **19–20** | — |

**All pistols are *Balanced*.**

**The best pistol in either game:** **Cassus Fett's Heavy Pistol — 6–19 damage, +5 attack, 25% chance to stun.** *"On top of its rifle-like damage."*

> **Note the ceiling.** **A base blaster pistol averages 4.5 damage (`1d8`). A base vibrosword averages 6.5 (`1d12`) and adds Strength.** **A Soldier at Strength 16 (+3) swings for 9.5 average with a weapon costing 120 credits, where a blaster does 4.5 at any Strength.** **⚠ The pistol figure here read `3.5` before this correction — `1d6`'s average, not `1d8`'s — and appears to have gone stale independently of today's `PT-1747`/`PT-1748` changes, possibly predating `PT-339` itself. The vibrosword figure (`7`, `2d6`'s average) is corrected for `PT-1747`'s move to `1d12`.**

---

**⚠⚠ RANGED TAKES K2's DICE; MELEE TAKES K1's. This has been what ships and was never written down.** Every ranged base type here is K2's value — Blaster Pistol `1d6 → 1d8`, Heavy Blaster `1d8 → 1d10`, Blaster Carbine and Blaster Rifle `1d8 → 1d12` — while every melee one is K1's, and `§4b` rules lightsabers to K1 explicitly. **So it is one rule with no exception, not a pattern with a carve-out**: a lightsaber is melee.

**⚠ WHICH IS ALSO THE BLASTER STEP-UP RULE IN ONE SENTENCE.** K2 bumped the common blasters a die step, and taking K2 for ranged IS taking that step — `1d6` becomes `1d8`. Bowcaster and Hold-Out Blaster are unchanged in both games and so are unchanged here.

### ⚠⚠ 4a-ii · The disruptor family is a NAMED EXCEPTION to `§4b`'s K1-era rule — `PT-2106`

**`§4b` rules *"Use K1's. Our campaign is 3956 BBY and K1 is the era."* The two
disruptors take K2's package instead — kind AND dice together — and this says so
out loud rather than letting the table quietly disagree with the rule two
sections down.**

| | K1 | K2 | ours |
|---|---|---|---|
| **Disruptor Pistol** | `1d4` · bludgeoning + piercing + slashing | `1d6` · **unstoppable** | `1d6` · **unstoppable** |
| **Disruptor Rifle** | `1d6` · bludgeoning + piercing + slashing | `1d10` · **unstoppable** | `1d10` · **unstoppable** |

**⚠⚠ THE DICE WERE ALREADY K2's AND THE KINDS WERE K1's.** Both rows had been
carrying one half from each game — the only rows in the corpus doing so — and
neither half was wrong on its own, which is why it survived. The choice was
never *change one thing*; it was *pick a game for these two rows*.

**⚠ AND THE MECHANIC ONLY EXISTS IN K2.** `damageflags` bit 4 is used by
**nothing at all** in K1 — no base item, no item property — and in K2 by exactly
these two base items plus six items named for disruption. Taking K1's kinds
would keep the weapons and retire the rule they are named for; taking K1's dice
as well would nerf both weapons to resolve a disagreement that the kinds column
had already resolved the other way.

---

## 4b. Lightsabers

**Confirmed from `baseitems.2da`. The games differ — K2 bumped every lightsaber one die step.**

**⚠⚠ EVERY LIGHTSABER DEALS `energy`, AND THIS TABLE HAS NO TYPE COLUMN TO SAY IT IN.** All four are `damageflags` **4096** in both games — *the same flag every blaster carries* — which decodes against `iprp_damagetype`'s row order (`1` bludgeoning, `2` piercing, `4` slashing, `1024` sonic, `2048` ion, `4096` energy). It is uniform with no exception, so it is stated here once rather than repeated in a column.

**⚠ AND THE `Training Lightsaber` ROW WAS `§4a`-SHAPED INSIDE THIS TABLE.** It read `1d8 | energy | 19–20 | yes | 1` — putting `energy` where a **K2 die** belongs and `§4a`'s *Balanced* and *Attacks* where *Wield* and *Size* do. Six cells either way, so nothing refused it; it was simply read as another table's row. It has no `baseitems` row of its own, so its K2 cell is `—`.


| Weapon | **K1** | K2 | Threat | Wield | Size |
|---|---|---|---|---|---|
| **Short Lightsaber** | **2d6** | 2d8 | **19–20 / ×2** | **2 — one-handed** | Small |
| **Lightsaber** | **2d8** | 2d10 | **19–20 / ×2** | **2 — one-handed** | Medium |
| **Training Lightsaber** | **1d8** | — | **19–20 / ×2** | **2 — one-handed** | Medium |
| **Double-Bladed Lightsaber** | **2d10** | 2d12 | **20 only / ×2** | **3 — two-handed staff** | Large |

> **Use K1's. Our campaign is 3956 BBY and K1 is the era.**
>
> **And K1's numbers make a cleaner system.** **A vibrosword is 2d6, so a K1 lightsaber sits exactly one die step above it.** **K2's 2d10 is two steps, which widens the gap between a Jedi and everyone else for no reason our port needs.** **⚠⚠ THIS COMPARISON IS STALE. `PT-1747` moved Vibrosword to `1d12`, a different die type entirely — "one die step above a `2d6`" no longer describes a real relationship, since there is no clean step from `1d12` to `2d8`. Not rewritten here: whether K1's lightsaber dice still make "a cleaner system" against the new Vibrosword value is a fresh comparison, not a mechanical correction of the old one.**

**⚠⚠ FULL CORRECTION HISTORY, RESOLVED.** An earlier draft cited **2d6** for the standard lightsaber — wrong for both games, and actually the Short Lightsaber's K1 value; the secondary source appears to have confused them. A later pass "corrected" it to **2d10**, which is ALSO wrong — that is K2's value and PT-339's own adopted "now" figure, mistakenly carried into this table's K1 column instead of K1's real number. **Confirmed directly against `data/2da/k1/baseitems.2da` (row 8: `numdice` 2, `dietoroll` 8): K1's real standard Lightsaber die is `2d8`.** This also resolves an odd stated progression the wrong value created — a two-handed Double-Bladed Lightsaber (`2d10`) tying with a one-handed standard Lightsaber (the erroneous `2d10`) had no in-universe reason to be equal; at the corrected `2d8`, K1's own three lightsabers form a clean ascending step (Short `2d6`, standard `2d8`, Double `2d10`), strengthening this section's own "K1 numbers make a cleaner system" argument rather than undermining it.

**`critthreat` 2 means 19–20; `critthreat` 1 means 20 only.** **Both as we had them.**

**Short Lightsaber is one-handed and Small** — **`weaponwield` 2, the same class as a standard lightsaber.** **So it may be paired, and its Small size makes it the natural off-hand.**

> **The threat ranges are confirmed and they are the whole trade.** ***"Single lightsaber: 19-20 critical threat ⇒ 10% critical chance. Double-bladed lightsaber: 20-20 critical threat ⇒ 5% critical chance."***

**Same shape as the vibrosword against the double-bladed sword** — **more attacks, less precision.** **And the double-bladed lightsaber is Balanced**, so it takes our reduced dual-wield penalty.

**Lightsabers inflict energy damage**, which matters: ***"disruptors aren't the only ranged weapons that don't"*** — **energy is absorbed by shields where physical is not.** *A vibrosword cuts through an energy shield; a lightsaber does not.*

**And a note that affects our roster:** ***"Lightsabers are not melee weapons, and a critical hit doubles bonus damage."*** **Two rules in one sentence** — **the lightsaber is its own weapon category, and its criticals multiply bonus damage where other weapons' do not.**

---

## 4c. Wield classes — `PT-169`

**⚠ `ACTION-ECONOMY-01 §697` already stated the pairing rule from this column. `PT-169` re-derived it without checking.**

**What was missing was here rather than there: `EQUIPMENT-01` stated a wield class for the three lightsabers and for none of the other sixteen weapons.**

**The table below is that gap filled. `§697` remains the authority on what may be paired.**

| | Class | Weapons | May be paired? |
|---|---|---|---|
| **1** | **One-handed light** | Stun Baton | **yes** |
| **2** | **One-handed** | Long Sword · Vibro Sword · Short Sword · Vibro Blade · Lightsaber · Short Lightsaber | **yes** |
| **3** | **Two-handed staff** | Quarterstaff · Gaffi Stick · Wookiee Warblade · Double-Bladed Sword · Vibro Double Blade · Double-Bladed Lightsaber | **no — it *is* the pair** |
| **4** | **Pistol** | Blaster · Heavy Blaster · Hold Out · Ion Blaster · Disruptor Pistol · Sonic Pistol | **yes** |
| **5** | **Rifle** | Ion · Bowcaster · Carbine · Disruptor · Sonic · Blaster Rifle | **no** |
| **6** | **Heavy** | Repeating Blaster · Heavy Repeating Blaster | **no** |

**Verified identical in K1 and K2.**

### ⚠ What it settles that was open

**`Two-Weapon Fighting` never said what may be paired.** > **Classes 1, 2 and 4 may be dual-wielded. Classes 3, 5 and 6 may not.**

**⚠ You cannot pair a rifle with anything.** **That was never stated and it is the difference between the `Gunslinger` and the `Sharpshooter` in mechanics rather than flavour** — **`PT-148` gave the Gunslinger *"two guns, fast draw"* and the Sharpshooter one shot. The source has been saying so all along.**

**And `Dueling` reads *"a single blaster pistol, melee weapon, or lightsaber"* — an enumeration where a class name would do.** **It is: any weapon of class 1, 2 or 4, wielded alone.**

**⚠ A class-3 staff wielded alone does not qualify for `Dueling`.** **It is already two weapons; that is what `weaponwield` 3 means and why every one of them is marked Balanced with 2 attacks.**

### The size column travels with it

    class 1   size 1        class 3   size 4
    class 2   size 2 or 3   class 5   size 4
    class 4   size 2        class 6   size 4

**⚠ Size 4 is exactly the set that cannot be paired.** **Two-handedness in this source is a size fact, not a separate flag** — **which is why the Short Lightsaber at size 2 is the natural off-hand and `§111` reached that conclusion without the column.**

---

## 5. Armour

**Defence = 10 + armour bonus + Dexterity modifier, and the Dexterity contribution is capped by the armour.**

### 5.1 One rule generates the whole table — confirmed from the data

> ***"The sum of armor and Max Dexterity Bonus is always 9."***

**Confirmed for all organic armour in both games. `baseitems.2da` rows 38–43, identical values.**

**⚠⚠ AND `Armor_Zeison_Sha` IS A NAMED EXCEPTION, NOT A CONTRADICTION — owner
ruling, and the same shape `§9a` gives the Kyber Dart.** Its `baseac 3` and
`dexbonus 4` sum to **seven**, not nine.

**⚠ THE RULE ABOVE STAYS CORRECT FOR THE POPULATION IT WAS MEASURED AGAINST.**
It says *rows 38–43*, and it is exactly right about those six; **this row is
outside that population entirely.** A rule that named its own scope is not
broken by something beyond it — and the alternative readings were both worse:
widening *always nine* to cover a row that is seven would make the sentence
false, and calling the seventh row an error would be correcting the source to
fit our summary of it.

**⚠ IT IS STILL A BASE TYPE, for the Kyber Dart's reason.** That dart is named
as the value the ladder does not reach AND is fully modelled at its flat 25;
naming an exception is not the same as declining to carry it. Six real items
sit on this row — `Zeison Sha Initiate Armor`, `Jal Shey Neophyte Armor` and
the rest — and without a base type not one of them could be authored.


| Row | Label | `baseac` | `dexbonus` | Sum | `armortype` |
|---|---|---|---|---|---|
| 38 | Armor_Class_4 | **4** | **+5** | 9 | **leather** |
| 39 | Armor_Class_5 | **5** | **+4** | 9 | **leather** |
| 40 | Armor_Class_6 | **6** | **+3** | 9 | armor |
| 41 | Armor_Class_7 | **7** | **+2** | 9 | armor |
| 42 | Armor_Class_8 | **8** | **+1** | 9 | armor |
| 43 | Armor_Class_9 | **9** | **+0** | 9 | armor |

**⚠⚠ AND THE SIX BASE TYPES THEMSELVES, WHICH IS WHAT AN ITEM BLUEPRINT
NAMES.** The table above transcribes `baseitems.2da` and keeps **the game's own
labels** — `Armor_Class_4`, American and underscored. This is the same six rows
under **this corpus's own names**, and it is a second table for `§8`'s reason:
*a position is not an identity*, and a reader that had to transform a foreign
label into an id would be inventing the id rather than reading it.

| Base type | Defence | Max Dex | Armour type | Grade | Restricts force |
|---|---|---|---|---|---|
| **Armour Class 4** | **+4** | **+5** | leather | light | no |
| **Armour Class 5** | **+5** | **+4** | leather | light | no |
| **Armour Class 6** | **+6** | **+3** | armor | medium | **yes** |
| **Armour Class 7** | **+7** | **+2** | armor | medium | **yes** |
| **Armour Class 8** | **+8** | **+1** | armor | heavy | **yes** |
| **Armour Class 9** | **+9** | **+0** | armor | heavy | **yes** |
| **Zeison Sha** | **+3** | **+4** | leather | light | no |

**⚠⚠ THE GRADE AND THE RESTRICTION ARE OURS — owner ruling. *Light armour
permits Force powers; medium and heavy restrict them.*** `§5.4` has carried
*"armour blocks Force powers"* since it was written with nothing enforcing it,
and this is the column that enforces it.

**⚠⚠ AND `§5.1` SAYS *"THERE IS NO THREE-WAY LIGHT/MEDIUM/HEAVY FLAG"*, WHICH
IS STILL TRUE OF THE SOURCE AND IS WHY THIS COLUMN IS AUTHORED RATHER THAN
EXTRACTED.** `armortype` splits leather from armor and nothing else; the
medium/heavy boundary is `baseac`-driven and the games never write it down. The
grades here are **ours**, and they fall where `armortype` already splits —
`leather` is light, `armor` is medium and heavy — so the restriction lands on
the same four rows either way and the grade is what a player is told.

**⚠⚠ AND THE ITEM CATALOGUE'S OWN `category` DISAGREES ABOUT ZEISON SHA, WHICH
IS WHY THE GRADE IS ON THE BASE TYPE AND NOT ON THE ITEM.** Every item sitting
on `Armor_Zeison_Sha` is catalogued `medium` — and **all six of them say in
their own description: *"Does not restrict use of Force Powers."*** Reading the
grade off the item would make the one armour the source explicitly exempts the
one that blocks. Its `baseac 3` is lighter than Armour Class 4's, and **that is
why it is light here**: `§5.1`'s named anomaly and this exemption are one fact.

**⚠ DROID PLATING IS GRADED light · medium · heavy IN THE SOURCE ITSELF and
carries no restriction, because no droid holds a Force class — `PT-92`,
`PT-569`.** The question cannot arise, and a `yes` there would be a rule with
nothing to bite.

**⚠⚠ THIS ROW READ `armor` AND THE SOURCE SAYS `leather` — a transcription
error, corrected at `PT-2254` and found only because the ruling made this
column mechanical.** `k2_baseitems.2da` row 102 reads `armortype = leather`,
and `PARTITION-01 §6.6` governs: *where this and the 2DA disagree, the 2DA
governs on mechanical values.*

**⚠⚠ AND TWO INDEPENDENT SOURCES AGREE ON THE CORRECTED VALUE, WHICH IS WHAT
MAKES IT A CORRECTION RATHER THAN A PREFERENCE.** `PT-2254` ruled that
`armortype = armor` is what blocks Force powers. With `armor` on this row,
`Zeison Sha` would block them — and **all six items that sit on it say in their
own description that it does not**: *"Does not restrict use of Force Powers."*
The wrong value produces the exact opposite of what the items state; the right
one produces exactly what they state.

**⚠ `armour type` KEEPS THE `2da`'s OWN TWO VALUES** — `leather` and `armor` —
because they are what the column holds and renaming them here would be a third
spelling of a thing that already has two.

> **There is no three-way light/medium/heavy flag.** **`armortype` splits leather from armor — Light from everything else — and the medium/heavy boundary is `baseac`-driven, not column-driven.**

**Two exceptions, both K2.** **The Armoured Flight Suit** *(row 98, 5/+4)* **obeys the rule.** **The Zeison Sha** *(row 102, 3/+4 = 7)* **breaks it** — the only organic armour in either game that does.

**So a Defence of 19 is the ceiling from body armour alone**, whatever you wear — **and the choice is only ever *where the 9 comes from*.**

> **A Smuggler at Dexterity 20 in light armour reaches 4 + 5 = 9. A Soldier at Dexterity 10 in heavy reaches 9 + 0 = 9.** **The armour classes are not better and worse. They are the same total, sorted by which ability you invested in.**

**K2 shifts the heavy band down one** — **armour 8 / Max Dex +1** where K1 tops out at **9 / +0** — **but adds upgrade slots that recover it.** *Heavy Bonded Plates up to +4 Defence, Flexible Underlay up to +3 Max Dex.*

### 5.2 Robes are the exception, and it is a bug that became a feature

**Jedi Robe Defence 1 · Knight Robe 2 · Master Robe 3 · Revan Robes 5.**

> ***"Robes display in game a Max Dexterity Bonus of +8, but actually act as if possessing an infinite Max Dexterity Bonus."***

**So a robe's Defence has no cap on Dexterity at all.** **A Jedi at Dexterity 28 in a Master Robe gets 3 + 9 = 12, beating every suit of armour in the game.**

**That is why Jedi wear robes**, and it compounds with the restriction: ***"many Force powers are restricted when using armor."***

**⚠⚠ AND THE FOUR GRADES ARE BASE TYPES NOW — they were stated here and
carried by no table.** A class array has named a robe since `STARTING-EQUIPMENT-01`
was written — three classes take a `Padawan Robe` and three a `Dark Padawan
Robe` — and **no item could name one**, because the rules carried six armour
classes, droid plating, and nothing a robe could resolve through. The values
below are transcribed from the sentence above them; nothing here is chosen.

| Base type | Defence | Max Dex | Armour type |
|---|---|---|---|
| **Robe 1** | **+1** | uncapped | robe |
| **Robe 2** | **+2** | uncapped | robe |
| **Robe 3** | **+3** | uncapped | robe |
| **Robe 5** | **+5** | uncapped | robe |
| **Clothing** | **+0** | uncapped | cloth |

**⚠ NAMED BY GRADE, BECAUSE THE GRADE IS WHAT IS MECHANICAL.** `§5.2` names the
four *Jedi · Knight · Master · Revan*, and the catalogue's own `Armor N`
property is what selects one: **a `Padawan Robe` is `Armor 1` and so is a `Jedi
Robe`** — the same row, and calling that row *Jedi Robe* would make a Padawan's
robe a Jedi's. `§5.1`'s classes are named by their number for the same reason.

**⚠ AND THE CATALOGUE CONFIRMS THE LADDER EXACTLY.** Forty-two robes carry
`Armor` **1 · 2 · 3 · 5** — thirteen, twelve, thirteen and three of them — and
**no other value appears.** `§5.2`'s four numbers are the whole set.

> **⚠⚠ `Clothing` IS `+0`, RULED.** Nothing in either game or this corpus states
> a Defence for ordinary clothes; `0` is what wearing them means. **It is the
> one number in this section that was decided rather than read**, and it is
> marked so nobody later mistakes it for an attested one.

**⚠ TWO ITEMS FILED UNDER `clothing` ARE NOT CLOTHES.** `Atton's Ribbed Jacket`
carries `Armor 4` and `Mira's Ballistic Mesh Jacket` `Armor 5` — and both are
`a_light_*` resrefs, which is the **light armour** family. They name an armour
class, not this row; the catalogue's category is a display grouping and the
resref is what says what a thing is.

---

### 5.3 Droid plating is a separate class and does not follow the rule

> **Droids cannot wear organic armour. They have plating, which is its own item class and was never bound by the sum of 9.**

**K1 droid plating sums to 9, 7, and 10 across its three grades.** **K2 changed Light and Medium plating to `dexbonus` = −1**, **which the engine reads as *uncapped*.**

> **So a K2-plated droid keeps its full Dexterity bonus on top of its plating.** **A droid in Light plating is the only body-armour case in either game with no Dexterity ceiling** — **the same property that makes Jedi robes worth wearing.**

**⚠ An earlier draft gave the Astromech pregen Defence 10 + 0 + 2 = 12 on the grounds that droids cannot wear armour.** **Corrected — they wear plating.**

### 5.4 Two restrictions worth porting

**Organic armour is not usable by droids or Wookiees.** *"Armor Proficiency is required to use armor, which is not usable by Droids and Wookiees."* **⚠ The Wookiee exclusion is new to our corpus** — the species chapter does not carry it.

**And armour blocks Force powers**, which `ACTION-ECONOMY-01 §12` already depends on to make the Heavy-Armour and Soresu gates on `Well Guarded` genuinely alternative paths. **Confirmed.**

---

## 6. Ability score generation — the blocker is closed

> ***"At character generation each of the six physical attributes is at 8, with 30 points to invest in them. Any attribute can be increased to a maximum of 18 at this time, but beyond 14 there are increased point costs."***

**And: *"Characters are granted an additional attribute point every fourth level, at levels 4, 8, 12, 16 and 20."*** *"These aren't subject to the increased point costs which apply at character generation, so any attribute can be increased to a maximum of 23 by investing points."*

**Point buy. Every ability starts at 8. Thirty points. Maximum 18 at creation, costs rising above 14. One point at levels 4, 8, 12, 16, and 20.**

> **This is the answer for a playtest specifically.** **It is repeatable — two runs of the same encounter are not confounded by one character having rolled an 18** — and it is the source's own method rather than RCR's 4d6-drop-lowest.

**⚠ The exact cost curve above 14 is not in the extract.** **Needed before a character can be built precisely; a flat 2-points-per-step above 14 is the usual d20 shape and would do for a first test.**

---

## 7. ⚠ On a complete equipment catalogue

**You asked for every item in both games with effects, bonuses, penalties, and restrictions.**

> **That is several hundred items across armour, robes, weapons, upgrades, implants, belts, gloves, headgear, masks, shields, and consumables — and it is a data-extraction job, not a research job.**

**The 2DA holder has the files that answer it properly:** **`baseitems.2da` for the categories, and the item instance files for the individual entries with their property lists.** **A wiki sweep would take dozens of fetches and still be secondary.**

**What this document holds instead: the structural rules, every base weapon, three points on the melee upgrade curve, and the complete armour arithmetic.** **That is enough to build a character and run a fight.**

---

## ⚠⚠ 7a · Damage that only lands on one kind of target — `PT-1740`

`EQUIPMENT-01`'s Ion Blaster read **`1d4 + 1d10 vs droid`** when `PT-1740` ruled this, and `PT-1452`'s reader takes `NdM` or a flat number — so it refused the whole string, **correctly**, and the weapon fell back to a fist. `TEST 065` met it in play: *"equips cleanly isn't quite true for Engineer yet: the weapon opens, but swinging it is functionally the same as being unarmed, silently."*

**⚠⚠ AND `§4`'s ION BLASTER ROW CARRIES NEITHER HALF OF THAT STRING NOW.**
`PT-1754` moved the head from `1d4` to K2's `1d6`, and `PT-2090` took the
`+ 1d10 vs droid` off the row entirely. The sentence above is kept in the past
tense because the refusal it narrates is real history and the mechanic below
was ruled on the strength of it.

**⚠⚠ THE CLAUSE WAS NEVER THE BASE TYPE'S.** It is `g_w_ionblstr01`'s own
`DamageRacialGroup (Droid) 1d10`, hand-folded onto the row every ion blaster is
made from — so **two props that carry no bonus were given one, the Aratech
Ionmaster's real `2d8` was flattened to `1d10`, and fifteen weapons across
seven OTHER base types got nothing at all**: Bastila's Lightsaber, Bacca's
Ceremonial Blade, Yusanis' Brand, a hold-out blaster, a blaster rifle. Twenty
weapons carry a racial bonus and five were being served by that one cell.

**⚠ THEY STATE THEIR OWN NOW — `PT-2090`**, extracted from each row's own
properties, and this section is what reads them. **Seventeen more are
deferred by name**: sixteen upgrades (ion cells, ionite edges, chargers) and a
droid's Anatomy Library, which grant the bonus to a host weapon or to their
carrier and have no damage of their own to add it to.

> **RULED: not a new mechanic, an extension of one already accepted.** Sneak Attack and Stealthy Shot both add conditional bonus dice *against a target unaware of you* — **extra damage gated on a fact about the target.** Ion damage vs droid is the same shape with the target's KIND as the condition.

**⚠ THE PRECEDENT IS A RULES PRECEDENT, NOT A CODE ONE.** Nothing in the tree implements Sneak Attack, so this is the **first conditional damage in the product** — built in the shape the corpus already accepted rather than one chosen at the keyboard.

| | |
|---|---|
| **grammar** | a base term, then **zero or more** bonuses, each a magnitude and at most one qualifier |
| | `N` or `NdM` — the magnitude · `<kind>` TYPED, always applies · `vs <kind>` CONDITIONAL, only against that target |
| **fires when** | the target's kind matches — `droid`, `sentient` |
| **null kind** | fires nothing: *a bonus against a kind nobody established is a bonus against everything* |
| **on a critical** | multiplies, because `§12` makes the multiplier a property of the BLOW |

**⚠⚠ THE ROW ABOVE SAID *optionally ONE* UNTIL `PT-2090`.** It was right when `PT-1740` wrote it — one row in the whole catalogue carried a `vs` clause — and the Long Sword ruling later widened the reader to a head term and **zero or more** bonuses, adding the TYPED form beside the conditional one. The code moved and this table did not. **Confirmed by parse, not by reading the source**: `1d6 + 1d10 vs droid + 2d10 vs droid` returns two conditional bonuses, and `1d6 + 5 vs droid` returns a flat one — both shapes the real catalogue contains. A documentation fix to match an already-ruled reality.

**⚠ THE GRAMMAR IS STILL CLOSED.** `PT-1452`'s *"anything else is refused rather than guessed at"* survives, **widened by exactly what the data contains**: censused, ten distinct damage strings in `equipment.toml` and this is the only one that is not `NdM` or a flat number. **A second clause is refused rather than dropped** — silently keeping the first is a weapon quietly weaker than its own datasheet.

**⚠ AND THE BONUS IS NAMED IN THE LINE**, not folded into the faces. `PT-1326` makes the derivation the answer: a player reading `damage 12 — 1d4 3 + 1d10 vs droid 9` can tell a rule from a bug, and one reading `damage 12` cannot.

---

## ⚠⚠ 7b · The damage kinds — the vocabulary, declared at last — `PT-2106`

**⚠⚠ NOTHING HAS EVER DECLARED THIS.** A weapon's `kinds` were decoded from
`damageflags` per base type, an item effect's from its own property, and the
only way to learn the whole set was to read the data and see what turned up —
which is exactly how `Loom`'s `damageKinds` was written, and its own comment
says so: *"nothing declares the vocabulary."* **A rule with only a first state,
in reverse: a vocabulary with no first state at all.**

**⚠ AND THE TWO HALVES HAD DRIFTED APART.** Weapons carried six kinds and
resistances carried eleven, because the weapon side came from a six-value
bitmask read and the effect side from whatever properties happened to appear.
**A weapon could not deal `fire` and a robe could resist it.**

**⚠⚠ THIS IS `iprp_damagetype.2da`, WHICH IS THE GAMES' OWN ANSWER**, read from
both installs. Row order is the bit order — bit `n` is row `n` — confirmed
against every `damageflags` value in `baseitems.2da` and `forceshields.2da`.

| Bit | Kind | K1's name | K2's name | Notes |
|---|---|---|---|---|
| 0 | `bludgeoning` | Bludgeoning | Bludgeoning | |
| 1 | `piercing` | Piercing | Piercing | |
| 2 | `slashing` | Slashing | Slashing | |
| 3 | `universal` | Universal | Universal | **⚠ THE ENGINE'S UNTYPED BUCKET** — the default `nDamageType` for `EffectDamage`, `EffectDamageIncrease` and `EffectDamageDecrease`. Damage of no particular kind. |
| 4 | `unstoppable` | **Acid** | **Unstoppable** | **⚠⚠ IGNORES RESISTANCE ENTIRELY — see below.** The one row the two games NAME differently. |
| 5 | `cold` | Cold | Cold | |
| 6 | `light_side` | Light Side | Light Side | **⚠ UNDERSCORED, AND THE GAME'S OWN COLUMN DECIDED IT** — `PT-2317`. Two producers reached this kind by different roads: item prose gives `DamageImmunity (Dark Side)`, lowercased to a spaced phrase, and `forceshields.2da`'s bit table gives `light_side`. Twelve effects said one and nineteen the other, and every resistance in the engine is matched by string. The 2DA's spelling wins as the more structurally authoritative of the two. ⚠ The **Use Limitation** label stays *"light side"* — that is English a person reads, not a kind the engine matches. |
| 7 | `electrical` | Electrical | Electrical | |
| 8 | `fire` | Fire | Fire | |
| 9 | `dark_side` | Dark Side | Dark Side | **⚠ Underscored for the same reason as bit 6** — `PT-2317`. |
| 10 | `sonic` | Sonic | Sonic | |
| 11 | `ion` | Ion | Ion | **⚠ Every force shield in both games is VULNERABLE to ion** — `forceshields.2da`'s `vulnerflags` is `2048` on all 21 rows, without exception. Not modelled; recorded so it is not re-discovered. |
| 12 | `energy` | Energy | Energy | **⚠ `nwscript` calls the constant `DAMAGE_TYPE_BLASTER`.** The 2DA label and the TLK both say Energy, and we take the label — the constant is a stale NWN holdover, the same pattern as the feat and class names. |

**⚠ `poison` IS NOT ON THIS LIST AND THAT IS CORRECT.** It is not a damage type
in either game; it is an on-hit effect with its own ladder at `§9a`. The two
vocabularies meet here and are not the same vocabulary.

### ⚠⚠ `unstoppable` ignores resistance entirely — owner ruling, `PT-2106`

**Nothing reduces it, whatever the target resists.** It does not change whether
an attack HITS: armour and Defence are untouched, and this is a rule about the
damage after the blow lands.

**⚠⚠ THE MECHANIC IS REAL AND IT WAS FOUND IN THE SHIELD TABLE, NOT REASONED
FROM THE NAME.** `forceshields.2da` carries a `damageflags` bitmask — the kinds
each shield actually stops — and **not one player-obtainable shield in either
game has bit 4 set.** The only row that does is `SHIELD_DREXL`, a creature's
innate shield in K2 whose mask is `16383`: every type there is. Nor does any
gear cover it — 103 `DamageImmunity` and `DamageResistance` terms across the
whole catalogue, in eleven kinds, and **none against this one.**

**⚠ SO IN THE SOURCE THE BYPASS IS AN ABSENCE, NOT A FLAG.** No rule says *this
type ignores resistance*; every shield simply declines to list it. We have no
shields, so the closest thing we own is resistance — and mapping it there is
what makes the rule exist at all rather than waiting for a system that does not.

**⚠ AND K2's NAME DESCRIBES THE CONSEQUENCE.** The type sat unused in K1 under
the name `Acid`; K2 wired a whole weapon family to it and renamed it after the
property it already had. We take K2's name because we take K2's disruptors
— `§4a-ii`.

---

## 8. ⚠⚠ Droid plating — EXTRACTED, and the placeholder is gone — `PT-1734`

**The rows are in holdings and they parse.** `baseitems.2da` rows **66–68** in both games, read with `scripts/parse2da.py`:

| Plating | Row | `baseac` | K1 `dexbonus` | K2 `dexbonus` |
|---|---|---|---|---|
| **`Droid_Light_Plating`** | 66 | **3** | 6 | **−1** |
| **`Droid_Medium_Plating`** | 67 | **4** | 3 | **−1** |
| **`Droid_Heavy_Plating`** | 68 | **9** | 1 | **1** |

**So the rule, taking K2's caps as `§223` already does:**

| Plating | Defence | Max Dex |
|---|---|---|
| **Light** | **+3** | **uncapped** |
| **Medium** | **+4** | **uncapped** |
| **Heavy** | **+9** | **+1** |

**⚠ THE SUMS CONFIRM THE READ INDEPENDENTLY.** `§223` has attested *"K1 droid plating sums to 9, 7, and 10"* since before the rows were readable, and K1's columns add to exactly that: `3+6`, `4+3`, `9+1`. **The figure that was attested and the figures that were guessed now come from the same rows.**

**⚠⚠ AND THE PLACEHOLDER WAS WRONG IN BOTH DIRECTIONS, WHICH IS WHY IT MATTERED.** It read `+4 / +6 / +8` — a smooth ladder. The real one is `+3 / +4 / +9`: **Medium is two lower than authored and Heavy is one higher**, and the jump is at the medium/heavy boundary rather than spread evenly. That is `§199`'s own sentence showing up in the data — *"the medium/heavy boundary is `baseac`-driven, not column-driven."*

> **⚠ EVERY DROID DEFENCE IN `PREGENS-01` COMPUTED FROM THE OLD TABLE MOVES** — Light by −1, Medium by −2, Heavy by +1. The note those entries carry can go, and the numbers under it need re-deriving.

**⚠ `armortype` IS EMPTY ON ALL THREE ROWS IN BOTH GAMES**, which is `§199` again: there is no three-way light/medium/heavy flag to read, and the grades are the labels plus `baseac`.

### ⚠ How this was checked, because the last attempt could not be

`PT-1734` queued this because a courier reported six numbers and the router could not reproduce them: *"the tab-delimited copy… is truncated… the fuller `k1_baseitems.2da` has no field delimiters I could parse."*

**Both of those are the wrong file or the wrong reader.** `data/2da/k1/k1_baseitems.2da` is a **TSV export** whose first bytes are `row	name	`; the parseable originals are the **binary `2DA V2.b`** files beside it, and `scripts/parse2da.py` reads them:

    data/2da/k1/baseitems.2da       92 rows · 61 columns   sha256 e9d031faf0a5d3d4…
    data/2da/k2/k2_baseitems.2da   104 rows · 61 columns   sha256 b1bac4f46a0fae3e…

**Ninety-two rows, so 66–68 were never past the end.** Anyone can repeat it:

```
python3 scripts/parse2da.py data/2da/k1/baseitems.2da --dump
```

**⚠ WHAT IS STILL NOT CONFIRMED IS AUTHOR'S SIX NUMBERS THEMSELVES.** Its report is not in `HANDOFF/` and `PT-1734` records the claim rather than the values, so **the list could not be compared to this one**. What is confirmed is the ground truth and the consistency check the claim rested on — the K1 sums — which agree exactly.


---

## ⚠ Base dice adopt the game's — `PT-339`. Supersedes `§105`.

    weapon              was      now
    Blaster Pistol      1d6      1d8
    Blaster Rifle       1d8      1d12
    Lightsaber          2d8      2d10
    Short Lightsaber    2d6      2d8
    Double Lightsaber   2d10     2d12
    Vibrosword          2d6      2d6   ⚠ already matched

**⚠⚠ THE THREE LIGHTSABER ROWS ABOVE ARE SUPERSEDED BY §4b FOR THE ACTUAL CAMPAIGN VALUE.** **This table's "now" column adopted K2's dice; §4b later ruled K1's dice instead (Short `2d6`, standard `2d8`, Double `2d10`) — narrower gap over a vibrosword, and matching the 3956 BBY setting.** **A reader wanting the ruled lightsaber die should read §4b, not this table's "now" column, for those three rows specifically.**

**⚠⚠ `PT-1747`, owner ruling: VIBROSWORD MOVES TO `1d12`.** **A new change `PT-339` never made — it was previously the one row already matching the game's data, and the owner has now moved it off that value entirely.**

    weapon              PT-339 gave it      now, `PT-1747`
    Vibrosword          2d6                 1d12  ⚠ new change

**Every other row `PT-339` set — Blaster Pistol, Blaster Rifle, Lightsaber, Short Lightsaber, Double Lightsaber — stands at the values above, unchanged.**

**⚠⚠ `PT-1747` ORIGINALLY ALSO REVERTED BLASTER PISTOL TO `1d6`, AND `PT-1748` ORIGINALLY MOVED BLASTER RIFLE TO `1d10`. BOTH ARE WITHDRAWN, IN THE SAME SESSION THEY WERE MADE.** **The owner reversed both immediately after: Blaster Pistol stands at `PT-339`'s `1d8`, Blaster Rifle stands at `PT-339`'s `1d12`. Recorded here rather than silently erased, since a change made and then withdrawn is still part of this document's history — the same discipline this corpus applies everywhere else a ruling gets corrected.**

**⚠⚠ ONE THING FROM THE WITHDRAWN `PT-1748` STANDS ON ITS OWN MERITS AND WAS NOT PART OF THE REVERSAL: Disruptor Rifle and Ion Rifle's summary lines two sections up were found stale (reading `1d6` against both weapons' actual, unchanged `1d10` in `ITEMS-01`) and were fixed to match reality.** **Confirmed correct by the owner directly.** **This was never a damage change to either weapon — only a correction to this document's own summary table, the same shape as `PT-1742`'s `ATTACKS-01` staleness — and it stands independently of the pistol/rifle reversal above.**

**⚠⚠ RESOLVED, PT-1773: `PT-1747`'s ORIGINAL SWEEP MISSED FIVE VIBROSWORD-FAMILY WEAPONS ENTIRELY.** **`Bacca's Ceremonial Blade` (all four variants, rows `05`–`08`), `Krath Dire Sword`, `Sith Tremor Sword` (both games), and `Echani Foil` all share the Vibrosword base item and were still reading `2d6` in `ITEMS-01` until caught by AUTHOR's Chapter Two format check. `PT-1750` already confirmed Bacca's Ceremonial Blade is genuinely Vibrosword-based via direct UTI/TLK resolution — the four-variant question `PT-1746` left open is about which VARIANT'S properties apply, not whether the base die follows Vibrosword, so this does not reopen that question. All five fixed to `1d12` alongside every other Vibrosword-family weapon.**

**⚠ `PT-1747` did not re-run `PT-339`'s ratio argument for Vibrosword or any of its family. That argument was specific to the lightsaber-over-pistol gap; it does not automatically bless or condemn a vibrosword-family value chosen for a different reason. If a ratio concern applies here, it has not been checked.**

**⚠ `§105` declined the higher lightsaber dice to avoid widening the Jedi gap. The arithmetic does not support that concern.**

    gap, lightsaber over pistol
      ours   2.57x
      game   2.44x   ⚠ NARROWER

**⚠ The pistol gains 29% and the lightsaber 22%.** **Adopting the game's dice CLOSES the gap slightly rather than widening it.**

**`§105`'s reasoning was sound and its conclusion was wrong, because it compared absolute values rather than the ratio.**


---

## ⚠ Ranged adds Dexterity to damage — `PT-340`

**Owner ruling. Neither KOTOR nor RCR does this; it is authored.**

    melee 1H    weapon dice + Strength
    melee 2H    weapon dice + 1.5x Strength
    ⚠ ranged     weapon dice + Dexterity

### ⚠ It does not overtake melee, and my first check said it did

    vibrosword 2H, 2d6 + 1.5x STR 5    14.0
    blaster rifle, 1d12 + DEX 5        11.5   ⚠ 18% behind

**⚠ I first compared it against ONE-HANDED melee and reported the gap as 4%.** **Two-handed gets `1.5x` Strength and the real gap is 18%.**

> **⚠ The alarm was mine and it was arithmetic, not design.**

**18% behind two-handed melee, with range, is a fair trade.**

---

## ⚠⚠ Enhancement — `+N` to attack AND `+N` to damage — `PT-2208`

**93 weapons state one. It is the most common stat this document carries, and nothing said what it DID.**

**⚠⚠ THIS IS AUTHORED CONVENTION, NOT EXTRACTED TEXT, and the distinction is the whole reason this section says so out loud.** `RULES-01-v2 §4`'s bonus registry lists Enhancement as a bonus TYPE — *"❌ highest · Per object / creature / ability score"* — which says how two of them COMBINE and never says what one of them does. **The corpus has a real gap here, not an ambiguity**, and `PT-2208` fills it with the near-universal convention for this genre family rather than leaving 93 weapons unread.

**⚠ THE SAME LABEL AS `Stun Baton`'s 1d4 AND `Long Sword`'s 1d8**, with one difference worth stating: both of those replaced a figure the source DID carry, and this replaces nothing. There is no prior value to keep beside it, because the source never stated one.

**⚠ THE MEASUREMENT THAT RULED OUT THE ALTERNATIVES — `PT-2207`.** Enhancement was tested against the idea that it restates *AttackBonus* in a second vocabulary. Seven weapons carry both; **two agree and five differ**, and `Cassus Fett's Heavy Pistol` carries `Enhancement 3` beside two separate `AttackBonus 1` rows, which no restatement explains. So it is a bonus of its own rather than a duplicate of either neighbour.

    Enhancement N     +N attack   ·   +N damage

**⚠ IT STACKS WITH *AttackBonus* AND WITH `Damage`, because `§4` folds by TYPE and these are different types.** Two Enhancement rows on one weapon take the better of the two; an Enhancement beside an AttackBonus is two types and both apply. That is `§4` working as written, not an exception to it.

**⚠⚠ AND TWO WEAPONS HAD IT FOLDED IN BY HAND, WHICH WOULD HAVE BEEN COUNTED TWICE.** `Krath War Blade` and `Naga Sadow's Poison Blade` are the whole of `PT-2011`'s long-sword ladder whose bonus came from an Enhancement rather than a `Damage (…)` property — `Krath` states `Enhancement 1` and nothing else, and its damage column read `1d8 + 1`. `PT-2013` is why: *"TRANDOSHAN USES THE REAL 4, NOT THE LOCKED 3"* — the ladder was deliberately aligned to each weapon's own real property value, so for these two the column WAS the enhancement, written out by hand because nothing read it.

**⚠ SO THE COLUMN GIVES IT BACK NOW THAT A READER EXISTS.** Both cells are `1d8`, and the enhancement supplies the `+1` and the `+3`. **The ladder's damage is unchanged to the point**; what each gains is the `+N` to ATTACK it always stated and never got. That is `PT-2090`'s own rule — *no weapon states a number its own effects already state* — applied to a stat rather than an effect, and the two are the only rows in the catalogue with an untyped flat matching their own enhancement, counted.

**⚠ AND 44 OF THE 93 CARRY NOTHING ELSE** — no attack row, no damage row. For those, this ruling is the only bonus the weapon has.

## ⚠ Massive Criticals — `2d8` converts to `2d6`, and nothing else converts — `PT-341`, narrowed at `PT-2252`

**Extra damage ON A CRITICAL, on top of the multiplier.**

**⚠⚠ THIS SAID *"45 weapons"* AND 45 IS THE NUMBER OF UPGRADE COMPONENTS — `PT-2249`.** Sixteen real weapons carry Massive Criticals. The 45 is exact and it counts something else entirely: `lightsaber-crystal` 11 · `melee-cell` 7 · `melee-edge` 6 · `ranged-cell` 15 · `ranged-chamber` 6. **A number landing exactly on the sum of five component categories is not a coincidence**, and the label was the thing that was wrong.

**⚠ AND THAT EXPLAINS WHY THE VALUE LIST BELOW WAS SHORT.** The six values this section used to enumerate are the weapon values **minus one**; the long tail — `1d3`, `1d12`, flat `1`, `2`, `5` — belongs almost entirely to the components, which is why it never appeared. Both counted together, the two populations carry twelve distinct values between them.

    THE 16 WEAPONS
    4 ×1 · 1d4 ×1 · 1d6 ×2 · 1d8 ×4 · 1d10 ×1 · 2d6 ×6 · 2d10 ×1

    THE 45 UPGRADE COMPONENTS
    1 ×2 · 2 ×2 · 4 ×2 · 5 ×1 · 1d3 ×3 · 1d4 ×4 · 1d6 ×7
    1d8 ×6 · 1d10 ×3 · 1d12 ×2 · 2d6 ×11 · 2d10 ×4

    2d8  ->  2d6                          ⚠ the ONLY conversion. Not a ceiling:
                                            2d10 is real and is left alone

**⚠⚠ THIS HEADING SAID *"capped at `2d6`"* AND THE CONVERSION NEVER DID THAT — `PT-2252`. THE RULE IS NARROWER THAN IT HAS BEEN DESCRIBED SINCE `PT-341`, AND IT IS THE DESCRIPTION THAT WAS WRONG.**

**⚠ `2d10` IS REAL, RETAIL, AND PASSES THROUGH UNTOUCHED.** `Droid Assassin's Rifle` carries it, and four components do too. Confirmed three independent ways rather than read off our own corpus: the item file's own property chain in `d_hk47_01` — `PropertyName 49` · `CostTable 4` · `CostValue 13`, which `k2_itempropdef.2da`, `k2_iprp_costtable.2da` and `k2_iprp_damagecost.2da` resolve to **`Massive_Criticals` · Damage · `2d10`** — and a sweep of **all 994 K2 item files**, which finds five carriers.

**⚠⚠ AND THE CONVERSION IS LIVE, WHICH IS WHAT SETTLED IT.** This is not intent sitting in a document. K2's archive carries **seven** items at `2d8` and our catalogue carries **none** — `Zhaboka`, a real weapon, reads `2d8` in the game and `2d6` here, and so do six components. Every one of the five `2d10` items reads `2d10` in both. **So the code has always implemented *`2d8` → `2d6`* specifically, and has been correctly passing a retail `2d10` through the whole time.**

**⚠ `PT-341` COULD NOT HAVE MEANT OTHERWISE, BECAUSE IT NEVER SAW ONE.** Its own list is seven values — `+4 · 1d4 · 1d6 · 1d8 · 1d10 · 2d6 · 2d8` — and `2d10` is not among them. *"Six of seven distinctions survive"* is exactly true of the seven it could see. **An original intent cannot cover a value the ruling never met**, so the choice was between changing five items that currently match the source to satisfy a sentence, or correcting the sentence. `PT-2252` ruled the sentence.

**⚠ THE NUMBER THE RULING ACTUALLY ARGUED ABOUT WAS `2d8`.** The arithmetic below prices it at **+41%** against `2d6`'s **+32%** on a `2d10` lightsaber's critical — a case `ATTACKS-01` had already refused on the grounds that critical multipliers *"change every round of every fight."* That case was always about `2d8`. **Nothing was ever measured for `2d10`, and nothing has been changed for it.**

**⚠ Six of seven distinctions survive** — of the seven `PT-341` measured. **A flat `2d6` for all of them would have collapsed every one of them onto one value**, which is what the owner proposed and what making it a conversion rather than a ceiling avoided.

    2d10 lightsaber, crit x2 = 4d10 = 22
                      + 2d6  =        29    ⚠ +32%
                      + 2d8  =        31    ⚠ +41%

**⚠ `ATTACKS-01` refused the `Commando` case on the grounds that critical damage multipliers *"change every round of every fight."*** **The `2d8` weapons were that case. Capping takes 9 points off the worst one and leaves the rest alone.**

---

## 9. ⚠⚠ Consumables — five base types that carry no magnitudes

**Every section above carries the numbers on the base type, because a weapon's
dice are a fact about the KIND.** `PT-1452`: *"an item blueprint names a BASE
TYPE from the rules, and the base type carries the dice."*

**⚠ Consumables do not work that way, and it was measured rather than
assumed.** The 42 gear-spent items in `item_effects.json` carry **36 distinct
effect value-sets** — 1.17 items per shape. A base-type row per distinct effect
is `EQUIPMENT-01`'s own model inverted: **1,424 items over 71 base-type rows**
here, 42 items over 36 there.

**⚠ THE SECOND NUMBER USED TO READ *25 base types* AND NOTHING ON THE SHELF IS
25 — `PT-2249`.** It could not be traced back to what it originally counted, so
it is replaced with the three real figures rather than preserved: **71 base-type
rows in all, 31 of them weapons** (11 melee · 16 ranged · 4 lightsabers), **and
62 distinct bases actually referenced by the catalogue's 1,424 items.** The
point the sentence makes — many items over few shapes — survives every one of
them.

**What separates one shield from another is its magnitudes and nothing else:**

    pool   20 · 40 · 50 · 70 · 80 · 100 · 110 · 130 · 170
    kinds  ["energy","electrical"] · ["bludgeoning","piercing","slashing"]
           · ["heat"] · ["energy","sonic","cold","heat","electrical"]

**Nine steps that do not lie on one line.** That is not a ladder with a grade
on it.

> **⚠⚠ RULED: a consumable base type names the SHAPE of its effect and carries
> NO magnitudes. The item blueprint supplies the values.**
>
> **And `PT-1452`'s reason does not forbid it.** `AuthoredItem` bars values on
> an item because *"an item that restated them could disagree with it"* — **a
> disagreement needs two copies.** A consumable base type carries no
> magnitudes, so there is nothing to contradict: **the shape has one home and
> the values have one home.**

### The five

| Consumable | Does | Takes | Used on | Note |
|---|---|---|---|---|
| Medpac | heal | amount | an ally within reach | `SKILL-RESOLUTION-01 §5.3` — Medicine spends one |
| Adrenal | ability | ability · amount · rounds | yourself | — |
| Shield generator | absorb | pool · kinds · vulnerable | yourself or an ally within reach | `ACTION-ECONOMY-01 §3` — *"using a consumable or activating a worn device, on yourself or an ally within reach"*; worn AND spent |
| Charge | damage · damage_over_time · condition · ability_penalty | damage → amount · kinds · save · deploy · plus_vs_droid? ; damage_over_time → amount · kinds · rounds · save · deploy · count? · sides? ; condition → condition · rounds · save · deploy ; ability_penalty → ability · amount · rounds · save · deploy | aimed at a target | thrown or placed, and the item says which — `deploy`; the placed half is `§5.2`'s Demolitions |
| Rocket | damage · damage_over_time · condition | damage → amount · kinds · save · deploy ; damage_over_time → amount · kinds · rounds · save · deploy · count? · sides? ; condition → condition · rounds · save · deploy | aimed at a target | ⚠⚠⚠ **CORRECTED AT `PT-2417`, AND IT WAS A CONTRADICTION NO BLUEPRINT COULD SATISFY.** This row admitted neither `deploy` nor the `damage` verb, so a faithful rocket stating `deploy = "thrown"` was refused by the schema, and one omitting it to satisfy the schema was discarded by the deployment filter before any rocket logic ran. **The shape is Charge's, which has been right all along** — minus `ability_penalty` and `plus_vs_droid?`, which no rocket states. `damage` joins `does` because `PT-2409` ruled a rocket's bare `Damage: X, N` a burst. REQUIRES A WRIST LAUNCHER, which is the gate that makes this its own row rather than a Charge. ACTION-ECONOMY-01 §6.2a: the launcher has no attack range at all — it is a launcher SLOT, not a fireable weapon, and the rocket carries the 24 m range and 20 m travel itself. Eleven items: the rockets and the darts. |

**⚠⚠⚠ `deploy` IS ON ALL FOUR OF `Charge`'S VERBS, AND IT IS THE ONLY FIELD
HERE THAT DESCRIBES THE ITEM RATHER THAN THE EFFECT.** `PT-2322`. This row has
said *thrown or placed* since it was written and **nothing made the item
choose** — so a Frag Grenade and a Minor Frag Mine opened identically: same
base type, same verb, same fields. `Set mine` would plant either, and no verb
could refuse the other's item because there was nothing to refuse it by.

**⚠⚠ IT IS A STATED FIELD AND NOT THE CATALOGUE'S `category` — ruled, against
the convenient answer.** `§11` says a base type is *a mechanical shape and not
a display taxonomy*, and how a charge gets where it is going is a mechanic. The
category column is right there and already joined for weapon on-hits; using it
here would be exactly the move `§11` warns about.

**⚠ AND NOT TWO BASE TYPES EITHER.** A grenade and a mine share their damage,
their area and their save — all of `Charge`'s real structure. Splitting the
type would duplicate every one of those to express one difference.

**⚠ IT SITS ON ALL FOUR VERBS BECAUSE THE QUESTION IS NOT VERB-SHAPED.** A gas
mine is a `damage_over_time` and an Adhesive Grenade is a `condition`; both
still have to say how they are used. `takes` is keyed by verb, so a field every
charge needs appears in every list.

**⚠⚠⚠ `damage` IS THE VERB THIS TABLE DID NOT HAVE, AND ITS ABSENCE WAS NOT
VISIBLE FROM THE TABLE.** `PT-2317`. A `Charge` could tick, apply a condition
or take an ability down, and **it could not simply go off.** Thirty-two real
items state a damage figure in their own properties that reached nothing:
**ten frag and plasma mines a player can set today**, eight grenades, and
seventeen droid utility devices.

**⚠⚠ IT TAKES NO `rounds`, AND THAT IS THE WHOLE DIFFERENCE FROM
`damage_over_time`.** A poison is carried across a round boundary and re-rolled
each tick; a frag mine resolves once and leaves nothing behind. The two are not
one verb with a duration of one — `PT-2280` already made this call: *a
different shape deserves its own word, not a repurposed one.*

**⚠ AND IT TAKES `kinds`, WHICH IS REQUIRED RATHER THAN OPTIONAL.** Every
resistance, immunity and shield in this ruleset is matched on kind, so a burst
that named none would pass through all three without any of them being wrong.

**⚠⚠⚠ `vulnerable` IS REQUIRED ON A SHIELD AND NOT OPTIONAL, AND THE REASON IS
THAT A HOLE NOBODY STATES IS A HOLE THAT CLOSES.** `PT-2310` ruled that a
shield's vulnerability overrides its stop-list — every one of `forceshields.2da`'s
**forty rows in both games** is vulnerable to `ion`, and several of them also
list `ion` among the kinds they stop. `takes` has no optional keys: a field is
required or it is refused as one the base type does not take. Left off, every
authored shield would open with an empty hole and stop ion, **silently
reinstating the exact reading the ruling rejected.** So it is required, which
also means an author cannot forget it — the refusal says which field is
missing.

**⚠⚠ THE ROCKET IS A FIFTH ROW AND NOT A `Charge`, AND THE DIFFERENCE IS A
GATE RATHER THAN A FLAVOUR.** A grenade needs a hand; a rocket needs a Wrist
Launcher, which `ACTION-ECONOMY-01 §6.2a` already describes — *"the Wrist
Launcher has no `maxattackrange` at all. It is a launcher slot, not a fireable
weapon — the Rocket, its ammunition, carries 24 m attack range and 20 m
travel."* **That is the same kind of distinction the three implant tiers have**
— a requirement stated in another document that the rules can act on — and
`§11`'s test admits it for exactly that reason.

**⚠ AND THE LAUNCHER ITSELF IS NOT A NEW BASE TYPE.** It sits in the forearm
slot and resolves as `§12`'s `forearm-band`, per the owner ruling that a slot
carries one id and what the item DOES lives on its own effects. The launcher is
a forearm band that fires; the rocket is the thing it fires.

**⚠ `amount` AND NOT `base`, WHICH IS WHAT `item_effects.json` CALLS IT.**
`[item]` already spends the key `base` on the base TYPE — `base = "medpac"` —
so an effect magnitude under the same name would overwrite the pointer to the
row that defines it. **A value used as a key**, and it would have been silent:
the item would open, name a base type of `20`, and resolve to nothing.

**⚠⚠ `Medpac` TAKES `amount` AND NOT `amount · terms`, BECAUSE THE MULTIPLIER
WAS DROPPED.** The ruled heal is *the medpac's amount plus the Medicine
check's own total, entered once* — KOTOR's `× Treat Injury` grade multiplier
is not ported, and with it goes the only thing `terms` carried. **A field with
no reader is `declared-and-read-by-nothing`**, which this corpus has paid for
before; it is removed rather than left as furniture.

**⚠ AND THE CHECK IS NOT A PROPERTY OF THE ITEM.** The roll is supplied where
the item is used, through `resolveEffect`'s `sources` — the same seam that
already refuses a term with no value rather than counting it zero. The medpac
knows its `amount`; the fight knows the roll.

**⚠ A ZERO DURATION IS NOT CARRIED.** `item_effects.json` writes `rounds` on
every effect and a medpac's is always `0`, because a heal is instantaneous.
`Medpac` therefore takes `amount · terms` and a blueprint that wrote
`rounds = 0` would be refused — **the absence IS the instant**, and a field
meaning *no duration* on every row of a kind is not a magnitude of that kind.

**⚠ `Takes` IS THE REFUSAL, NOT A DESCRIPTION.** The join reads it and rejects
a blueprint that omits a value the base type requires, or supplies one it does
not take. **A consumable that opened with no magnitude would be an item that
does nothing, silently** — which is `PT-1452`'s own argument, in the other
direction.

### ⚠⚠ `Takes` IS PER VERB WHERE A BASE TYPE HAS MORE THAN ONE — RULED

**Measured after the section was first written.** The 16 gear-spent charges
hold exactly **two** key-sets, and a single required set could satisfy neither:

    9  damage_over_time    amount · kinds · rounds · save
    7  condition           condition · rounds · save
    3  ability_penalty     ability · amount · rounds · save

**A gas mine has no `condition`; a flash mine has no `amount` and no `kinds`.**
⚠ **AND THE THIRD KEY-SET ARRIVED WITH `PT-2301`** — three sonic items reading
*"Secondary: −2 Dexterity for 30 seconds"*, which the first two sets cannot
state: `damage_over_time` has no ability and `condition` has no magnitude. The
count was two when this paragraph was written and the paragraph's argument is
why it can be three.
The row as first written refused every item it was drawn from.

> **⚠ THE WIDENING THAT WOULD HAVE "FIXED" IT WAS THE ONE THING THAT MUST NOT
> HAPPEN.** Reading `Takes` as *any of these* deletes the refusal that is the
> field's whole purpose — an item with no magnitude would open again, silently.

> **⚠⚠ RULED: `Takes` becomes per-verb. ONE base type, not a split into two.**
>
> *"This project has generally preferred one flexible mechanism with
> context-sensitive requirements over proliferating narrow variants for the
> same underlying idea — Repair already works this way (Effect and Resource
> modes on one skill, not two), and `Charge` fits the same pattern better than
> becoming two separate base types would. A `damage_over_time` charge item only
> needs what `damage_over_time` needs; a `condition` charge item only needs what
> `condition` needs."*

**The notation, and it is a rule rather than two shapes:**

    one verb     a bare list             amount · terms
    two or more  verb → its own list     a → x · y ; b → z

**⚠ A ROW WITH MORE THAN ONE VERB AND A BARE LIST IS REFUSED**, because that
list cannot say which verb it belongs to — the ambiguity is the thing the
ruling removes, and silently applying it to both would put the original defect
back.

### ⚠⚠ 9b · A TRAILING `?` MARKS A FIELD THE VERB **MAY** CARRY — owner ruling

**Measured after `PT-2329` asked for the `plus_vs_droid` widening to be checked
against every grenade rather than against the one that surfaced it.** `Takes`
cutting both ways is right for a field every item of a verb needs, and **three
shipped fields are not that**:

    charge / damage              plus_vs_droid    1 of 18 rows
    charge / damage_over_time    count · sides    6 of 6 rows
    rocket / damage_over_time    count · sides    2 of 3 rows

**⚠⚠⚠ THE LITERAL WIDENING WOULD HAVE BEEN STRICTLY WORSE.** Adding
`plus_vs_droid` to the required list does not merely permit the Ion Grenade —
it makes a droid bonus **mandatory on all eighteen `damage` charges**, refusing
every ordinary Frag Grenade that has none. *Required* refuses the Frag and
*absent* refuses the Ion, and before this notation the schema had no third
answer.

**⚠⚠ AND IT WAS NEVER ONE FIELD.** `count · sides` is `§9a`'s own rolled-tick
ladder, already shipped on every `damage_over_time` charge and already read by
the mine spring — the identical gap wearing different field names, on a live
reading path. A fix scoped to `plus_vs_droid` would have left it standing.

> **⚠⚠ RULED: mark the field optional rather than forcing degenerate values or
> un-building the feature.**
>
> *"These three fields genuinely only apply to some items within a broader
> shared verb, not all of them — a schema that can say so directly is more
> honest about what's actually true than one that either pretends everything
> needs everything or refuses to let anything be conditional."*

**The notation:**

    required     a bare name             amount
    optional     a trailing `?`          plus_vs_droid?

**⚠ IT WIDENS EXACTLY ONE THING.** A required field is still required, an
unknown key is still refused, and **a near miss still costs** — `plus_vs_droids`
is refused exactly as `round` for `rounds` always was. An optional field that
is absent stays **absent** and does not acquire a default on the way through.

**⚠⚠ AND THE `?` IS NOTATION, NEVER A KEY.** A blueprint writing
`plus_vs_droid?` is refused as an unknown field, because a schema that accepted
the marker would be teaching authors a spelling that means nothing anywhere
else. The refusal prints the legal list as `plus_vs_droid (optional)` for the
same reason.

**⚠⚠⚠ A ROW NAMING A FIELD BOTH WAYS IS REFUSED** — `amount · amount?` is two
answers to one question, and every reading of it is a guess: the permissive one
deletes a requirement, the strict one refuses a row the shelf said was fine.
**A bare `?` is refused too**, as a broken base type rather than as a field
called `?` that no blueprint will ever state — both refuse, and only one is a
refusal an author can act on.

### ⚠⚠ 9a · A POISON IS ROLLED, NOT FLAT — owner ruling

**The source states a flat tick** — *"Poison, 4 pts every 3 sec"* — **and a
flat per-tick number is a video-game convention rather than a tabletop one.**
Real damage over time is rolled, and it is rolled *every tick*, because that is
what keeps the same variance and tension in the fifth round that the first one
had. **A number that never moves removes the thing the mechanic is for.**

> **⚠⚠ THE LADDER IS NAMED TIERS, AND THE MEAN IS NO LONGER THE PORTED NUMBER.**
> Owner ruling, superseding the mean-exact version this section carried first.
> **It is a deliberate trade, confirmed, and it is recorded as a trade rather
> than quietly:** the earlier ladder matched each ported KOTOR value exactly
> and paid for it in `+ 1` modifiers on three of five rungs. Clean dice were
> judged worth more than arithmetic fidelity to the ported average.

**⚠ THE NAMES ARE GROUNDED, NOT INVENTED.** `Weak / Mild / Average / Strong` is
the real NWN module-author severity sequence, and **`Virulent` is KOTOR's own
term** — `POISON_DAMAGE_VIRULENT` is a genuine constant in `poison.2da`. One
sequence anchors both games rather than either one alone.

**⚠ The dice count scales with severity and the DIE SIZE scales with it** —
`BEASTS-FEATS-01`'s *"3e scales the DIE SIZE, not the number of dice"* still
holds across the rolled rungs, where `2d4 → 2d6 → 2d8` is die size alone.

| Tier | Rolled | Mean | Range |
|---|---|---|---|
| **Weak** | **`1`** | 1 | 1 |
| **Mild** | **`1d4`** | 2.5 | 1–4 |
| **Average** | **`2d4`** | 5 | 2–8 |
| **Strong** | **`2d6`** | 7 | 2–12 |
| **Virulent** | **`2d8`** | 9 | 2–16 |

**⚠⚠ AND WHICH TIER EACH PORTED VALUE TAKES.** The ported per-round values that
actually occur are **five**, and the tiers are five; the assignment is by rank
with the top rung anchored by name — `POISON_DAMAGE_VIRULENT` is the source's
own top poison and `Virulent` is this ladder's own top tier.

| Per round, as ported | Tier | Rolled |
|---|---|---|
| **4** | Weak | **`1`** |
| **5** | Mild | **`1d4`** |
| **6** — `POISON_DAMAGE_MILD` | Average | **`2d4`** |
| **8** — `POISON_DAMAGE_AVERAGE` | Strong | **`2d6`** |
| **10** — `POISON_DAMAGE_VIRULENT` | Virulent | **`2d8`** |

**⚠ KOTOR'S OWN MIDDLE LABELS DO NOT LAND ON THE MATCHING TIER NAMES, AND THAT
IS EXPECTED.** `POISON_DAMAGE_MILD` takes the `Average` rung here. The sequence
is a BLEND of NWN's four severity words with KOTOR's top one, so only the top
rung was ever going to align by name — recorded here so the mismatch reads as
the ruling rather than as a mistake nobody noticed.

**⚠⚠ `25` STAYS FLAT, AND IT IS OFF THE LADDER ENTIRELY.** The Kyber Dart's 25
a round has no dice form worth writing — `2d23` is not a die and `2d12 + 12` is
a modifier pretending to be a roll. **It keeps the number and is named here as
the exception rather than forced into the shape for uniformity's own sake.**

**⚠ IT IS NOT THE ONLY FLAT VALUE ANY MORE, WHICH IS WHY THIS SAYS *OFF THE
LADDER* RATHER THAN *THE ONLY ONE*.** The `Weak` rung is a flat `1`. The
distinction that matters is not flat-versus-rolled: it is that `Weak` is a tier
of this ladder and the Kyber Dart is a value the ladder does not reach.

**⚠ THIS APPLIES TO EVERY POISON, NOT TO THE BLADE THAT RAISED IT.** Ten effects
share this ladder — the gas mines, the poison grenades, the darts, the rocket
and `Naga Sadow's Poison Blade` — and **the same poison must behave the same way
however it is delivered.** A blade that rolled while a mine stayed flat would be
one rule applied to one path and not the next, on one effect.

---

### ⚠⚠ 9b · WHICH POISON A WEAPON CARRIES — `PT-2058`

**A thrown poison states its own tick in prose** — *"Poison, 4 pts every 3
sec"* — **and a weapon's does not.** A weapon carries `OnHit (ItemPoison) N`,
where `N` is the SAVE DC and the poison itself is named nowhere in the clause.
Three weapons reading identically as `10` are three different poisons.

**⚠ SO THE POISON IS NAMED IN THE PROPERTY NOW**, transcribed from the games'
own data alongside the DC that was always there:

    OnHit (ItemPoison: POISON_DAMAGE_AVERAGE) 10
                       ↑ which poison        ↑ the save DC

**⚠ AND THIS TABLE IS WHAT THE NAME MEANS.** Without it the label is a word no
reader can act on — a rule with no first state, which this corpus has now found
four times. The per-round column folds the sub-round tick exactly as `§9a`
does: a round is six seconds, so a 3-second tick lands twice.

| Poison | Per tick | Every | Lasts | Per round | Rounds | `§9a` tier |
|---|---|---|---|---|---|---|
| `POISON_DAMAGE_MILD` | 3 | 3 sec | 30 sec | **6** | 5 | Average `2d4` |
| `POISON_DAMAGE_AVERAGE` | 4 | 3 sec | 30 sec | **8** | 5 | Strong `2d6` |
| `POISON_DAMAGE_VIRULENT` | 5 | 3 sec | 30 sec | **10** | 5 | Virulent `2d8` |

**⚠⚠ AND THREE MORE EXIST THAT THIS BUILD DOES NOT MODEL.** They are named
here rather than omitted, because a table that silently listed only the half we
can do would read as the whole set:

| Poison | What it does | Status |
|---|---|---|
| `POISON_ABILITY_SCORE_MILD` | 1 to every ability, 36 sec | **deferred** |
| `POISON_ABILITY_SCORE_AVERAGE` | 1 to every ability, 36 sec | **deferred** |
| `POISON_ABILITY_SCORE_VIRULENT` | 1 to every ability, 72 sec | **deferred** |

**⚠ THEY DEAL NO VITALITY AT ALL** — `dam_hp` is `0` on all three — so they are
not a weaker version of the damage ladder above; they are the other half of the
mechanic. A `Combatant` carries ability MODIFIERS rather than SCORES, so there
is nothing for a point of Strength damage to come off yet. **Six of the eleven
poisoned weapons in the catalogue carry one of these**, and until that engine
work is ruled they must be REFUSED by name rather than mapped to the nearest
damage poison.

---

### ⚠ What this section is NOT

**It does not cover the 583 `spends = none` effects** — the implant that gives
+3 Constitution, the 54 lightsaber crystals, the robes. Those are properties of
equipment being WORN, no format carries them, and they are **fifteen times the
size of this**. Named here so this section is not mistaken for the whole of the
item-effect question.
---

## 10. ⚠⚠ Supplies — two base types a skill spends, stated here at last

**⚠⚠ THESE TWO WERE IN THE EXTRACT AND IN NO DOCUMENT.** `equipment.json` has
carried `spike` and `part` as base types since `PT-1957`, the app reads both by
id, and **`EQUIPMENT-01` said nothing about either.** A base type that exists
only in generated data is a rule with no first state: nothing can regenerate it,
nothing can review it, and the only copy is the output.

**A supply is not a `§9` consumable and the difference is which side spends it.**
A consumable is USED — an item with a verb, aimed at somebody. A supply is a
COST: something else does the work and charges you one. `SKILL-RESOLUTION-01
§5.2` is where the six skills that spend something are ruled; **two of them
spend an item this document has to name**, and the other four do not — Mines are
`§9`'s `charge`, Credits are already tracked, and Rations are `§5.4`'s.

| Supply | Name | Spent by | Note |
|---|---|---|---|
| spike | Security spike | Slicing | SKILL-RESOLUTION-01 §5.2 — Computer spikes are Slicing's cost, base by terminal grade. Security's spikes are the SAME item and are OPTIONAL there: that row is the one skill where the consumable is insurance rather than a cost, so a lock never requires one. |
| part | Repair part | Repair | SKILL-RESOLUTION-01 §5.2 — base cost by damage. |

**⚠ THE FIRST COLUMN IS THE id AND THE SECOND IS WHAT A PLAYER READS**, the same
shape `§4c`'s wield classes use. `spike` is what a blueprint writes and what the
app looks up; *Security spike* is what a line of text calls it. **Deriving one
from the other would make the id a spelling** — and this corpus has paid for a
check keyed to a spelling before.

**⚠ A SUPPLY CARRIES NO MAGNITUDES**, for `§9`'s reason exactly: how many a job
costs is the job's business, and `SKILL-RESOLUTION-01` holds those tables. The
base type says *this is a thing that gets spent*, and nothing more.


---

## 11. ⚠ Objects — one base type for everything carried that does nothing

**⚠ THIS ONE WAS IN THE EXTRACT AND IN NO DOCUMENT EITHER**, and its provenance
field pointed at another extract — `data/extracted/items.json` — rather than at
any rules text. It is `PT-1957`'s ruling and it belongs here.

| Object | Note |
|---|---|
| Object | ONE TYPE FOR FIVE CATEGORIES — PT-1957. items.toml carries plot (13), device (29), tool (18), misc (3) and datapad (2), and no base type had a home for any of them: an author making a keycard had to call it a Blaster Rifle. A base type is a MECHANICAL SHAPE and not a display taxonomy, and all five currently share the identical answer — carried, does nothing mechanical. Split one out if a real mechanical distinction ever emerges for it, against evidence rather than in anticipation. |

**⚠ THE FIVE CATEGORIES ARE A DISPLAY TAXONOMY AND THIS IS NOT.** They are how
`ITEMS-01..09` groups rows for a reader; a base type is what the rules do with
one. Five names for one identical mechanical answer would be `PT-1468`'s two
answers to one question, multiplied by five.


---

## 12. ⚠⚠ Worn slots — the five places a character wears something that is not armour

**⚠⚠ 241 REAL CATALOGUE ITEMS SIT ON THESE AND NONE OF THEM COULD BE AUTHORED.**
`§5` gives the body its armour and `§8` gives a droid its plating, and between
them the catalogue's masks, gauntlets, forearm bands, implants and belts had no
base type at all — so a blueprint for any of them was refused by construction.

**⚠ THE SLOTS ARE READ FROM `baseitems.2da`'s OWN BITMASK, NOT FROM THE
CONSTANT NAMES.** This corpus already records that KOTOR's nwscript constants
are stale NWN holdovers that must be matched by number; grouping every base type
by the bits it actually sets makes each slot self-evidencing instead. **K1 and
K2 agree exactly.**

**⚠⚠ AND THERE IS NO BOOTS SLOT AND NO SHIELD SLOT.** No base type in either
game matches boot, shoe, greave or foot — *the twenty-five pairs of boots in our
catalogue are entirely ours, every one `src: AUTHORED`.* And a shield is not
carried: `Droid_Shield` equips at the BELT, and the player's Echani, Arkanian
and Mandalorian shields are **forearm-band items.** Headgear is `Mask`; there is
no helmet type either.

| Base type | Name | Slot | Worn at | Requires feat | Note |
|---|---|---|---|---|---|
| mask | Mask | head | head | — | 59 items. Headgear of every kind — visors and the Force Shield are Masks too. |
| gauntlets | Gauntlets | hands | hands | — | 40 items. |
| forearm-band | Forearm band | arm_l · arm_r | forearms | — | 33 items, and THIS IS WHERE A SHIELD GOES — Energy Shield, Echani Shield, Mandalorian Power Shield are all forearm bands. Two slots, left and right. ⚠⚠ AND THE COLUMN SAYS BOTH NOW — `PT-2346`. It read `forearms` while the Note beside it said *"two slots"* and the format writes `arm_l` and `arm_r`; the first reader this column ever had faulted four correctly-equipped bands. |
| belt | Belt | belt | belt | — | 47 items, including the Stealth Unit. |
| implant-1 | Implant, level 1 | implant | implant | cybernetic_implantation · advanced_cybernetic_implantation · master_cybernetic_implantation | FEATS-LIBRARY-01 gates these — Cybernetic Implantation allows level 1, Advanced allows 1-2, Master allows 1-3. The three tiers are a ruled feat chain and not a display grade. ⚠⚠ THE COLUMN IS THE RULE NOW — `PT-2342`. It said this in prose and `§17.4` has to be READ, and a sentence is not a column. |
| implant-2 | Implant, level 2 | implant | implant | advanced_cybernetic_implantation · master_cybernetic_implantation | ⚠ THE LIST IS AN `OR` — `§17.2`, the same semantics every gate category has. A chain that allows 1-2 is named on BOTH rows rather than derived from a tier order nothing states. ⚠⚠ AND IT IS **IDS, NOT DISPLAY NAMES** — `PT-2344`. Every feat reader in the product matches an id; a display name is not a key. |
| implant-3 | Implant, level 3 | implant | implant | master_cybernetic_implantation | |

**⚠⚠⚠ THE `Slot` COLUMN IS THE EQUIPMENT MAP'S OWN KEY — `PT-2346`.** It is
what an author writes in `[equipment]`, and `PT-1252`'s locked lattice is where
the vocabulary comes from: **implant, head, hands, right arm, body, left arm,
belt, boots** and the weapon configs. **A row naming anything else is the
document being wrong, not the content** — that is the ruling, and it was made
because this column had never been read by anything until `PT-2344` tried, and
the first attempt faulted four correctly-equipped forearm bands.

**⚠⚠ NONE OF THEM CARRIES DEFENCE AND NONE OF THEM CAPS DEXTERITY.** Verified in
`baseitems.2da`: every row above is `baseac 0` and `dexbonus -1`, against
`Armor_Class_4`'s `4` and `5`. **Everything a mask or a belt does comes from the
item's own properties**, which is why these rows carry a slot and a note and no
numbers at all. A defence column here would be seven zeroes asserting a rule
nobody made.

**⚠ THE THREE IMPLANTS ARE SPLIT AND THE OTHER FOUR ARE NOT**, and the
difference is `§11`'s own test. A base type is a mechanical shape: the implant
tiers have a real gate in another document, so they are three shapes; a mask and
a visor have no distinction the rules can act on, so they are one.


---

## 13. ⚠ Droid slots — the same five places, and a genuinely different vocabulary

**A droid does not wear a mask; it mounts a sensor. It does not wear gauntlets;
it mounts a spike rig.** `§8` already gives droid plating the body slot, and
these are the other four — 105 catalogue items with nowhere to go.

| Base type | Name | Slot | Worn at | Note |
|---|---|---|---|---|
| droid-sensor | Droid sensor | head | head | 32 items. ONE TYPE FOR FOUR 2DA ROWS - Search Scope, Motion Sensors, Sonic Sensors and Targeting Computers are baseac 0 and dexbonus -1 alike, and no rule tells them apart. §11's test: a mechanical shape, not a display taxonomy. Split one out against real evidence if it ever appears. |
| droid-spike-mount | Droid spike mount | hands | hands | 26 items. The Computer and Security mounts, merged for the same reason. This is where the fifteen-step d_interface_ ladder lives. |
| droid-utility | Droid utility device | arm_l · arm_r | forearms | 33 items. ⚠ THE SAME PAIR AS `§12`'s forearm band — *"the slots are the same five"*, and `PT-2346` corrected both together. |
| droid-shield | Droid shield | belt | belt | 14 items. A SHIELD IS BELT-SLOT IN THIS GAME, which is the finding §12 records. |

**⚠ THE DROID SIDE IS NOT A RENAMING OF `§12`.** The slots are the same five and
the things that go in them are not interchangeable: a droid cannot wear a belt
and a person cannot mount a targeting computer. Two vocabularies, one anatomy.

---

## 14. ⚠⚠ The mapping — which `baseitems.2da` rows each base type is

**⚠⚠ THIS EXISTED NOWHERE, AND EVERY GAP FIGURE THIS PROJECT HAS QUOTED CAME
OUT OF A `normalise()` CALL AND A HAND-TYPED ALIAS LIST.** I wrote that list
three times in one session and got **923**, then **617**, then **309** — and
`PT-2074` reordered real work around the first of them. A rule with no first
state, and the fourth instance this corpus has found.

**⚠ THE NAMES DO NOT MATCH AND THEY WERE NEVER GOING TO.** 41 of 68 happen to
match after case-folding; the other 27 do not, and the reasons are ordinary:
the game says `Medical_Equipment` where we say `medpac`, `Jedi_Robe` where we
say `robe-1`, and `Forearm_Bands` where we say `forearm-band` — **that last one
fails on a plural.** A join keyed to a spelling was always going to drift.

**⚠ SO THE MAPPING IS WRITTEN DOWN RATHER THAN DERIVED.** Each row was decided
against the real data — the items that actually sit on that 2DA row, and what
they are — and not by matching text.

| Base type | Name | Section | `baseitems.2da` | Note |
|---|---|---|---|---|
| stun-baton | Stun Baton | Melee - base weapons | `Stun_Baton` |  |
| short-sword | Short Sword | Melee - base weapons | `Short_Sword` |  |
| quarterstaff | Quarterstaff | Melee - base weapons | `Quarter_Staff` · `Force_Pike` | TWO ROWS, ONE SHAPE — owner ruling. Twelve items across both, every one two-handed and 20/×2, differing only in dice: the Quarter_Staff nine roll 1d6 and the Force_Pike three roll 2d6. Force Pike, Gand Shockstaff and the Geonosian Electro-Staff are ITEMS of this type that state their own damage, which §11's test is exactly about. |
| gaffi-stick | Gaffi Stick | Melee - base weapons | `Ghaffi_Stick` |  |
| vibroblade | Vibroblade | Melee - base weapons | `Vibro_Blade` |  |
| wookiee-warblade | Wookiee Warblade | Melee - base weapons | `Wookie_Warblade` |  |
| long-sword | Long Sword | Melee - base weapons | `Long_Sword` |  |
| battleaxe | Battleaxe | Melee - base weapons | `Gammorean_Battleaxe` | ⚠ THE NAME IS OURS, THE DIE IS THE ROW'S — `PT-2200`, `PT-2227`. One `baseitems` row, named for the species that carries it, and `PT-2227`'s sweep found **no plain axe anywhere in either game** — so the generalisation to `Battleaxe` is ours and the `1d12` is the row's own. `Gamorrean Battleaxe` is a 20-credit item of this type stating nothing its base does not. |
| vibrosword | Vibrosword | Melee - base weapons | `Vibro_Sword` |  |
| double-bladed-sword | Double-Bladed Sword | Melee - base weapons | `Double_Bladed_Sword` |  |
| vibro-double-blade | Vibro Double-Blade | Melee - base weapons | `Vibro_Double_Blade` |  |
| hold-out-blaster | Hold Out Blaster | Ranged | `Hold_Out_Blaster` |  |
| disruptor-pistol | Disruptor Pistol | Ranged | `Disrupter_Pistol` |  |
| ion-blaster | Ion Blaster | Ranged | `Ion_Blaster` |  |
| sonic-pistol | Sonic Pistol | Ranged | `Sonic_Pistol` |  |
| blaster-pistol | Blaster Pistol | Ranged | `Blaster_Pistol` |  |
| heavy-blaster | Heavy Blaster | Ranged | `Heavy_Blaster` |  |
| disruptor-rifle | Disruptor Rifle | Ranged | `Disrupter_Rifle` |  |
| ion-rifle | Ion Rifle | Ranged | `Ion_Rifle` |  |
| sonic-rifle | Sonic Rifle | Ranged | `Sonic_Rifle` |  |
| blaster-carbine | Blaster Carbine | Ranged | `Blaster_Carbine` |  |
| blaster-rifle | Blaster Rifle | Ranged | `Blaster_Rifle` |  |
| marksman-rifle | Marksman Rifle | Ranged | **—** | AUTHORED. PT-1473 added it and the games have no such row. |
| sniper-rifle | Sniper Rifle | Ranged | **—** | AUTHORED. PT-1786. |
| repeating-blaster | Repeating Blaster | Ranged | `Repeating_Blaster` |  |
| heavy-repeating-blaster | Heavy Repeating Blaster | Ranged | `Heavy_Repeating_Blaster` |  |
| bowcaster | Bowcaster | Ranged | `Bowcaster` |  |
| short-lightsaber | Short Lightsaber | Lightsabers | `Short_Lightsaber` |  |
| lightsaber | Lightsaber | Lightsabers | `Lightsaber` |  |
| training-lightsaber | Training Lightsaber | Lightsabers | **—** | AUTHORED. PT-1473. |
| double-bladed-lightsaber | Double-Bladed Lightsaber | Lightsabers | `Double_Bladed_Lightsaber` |  |
| 1 | One-handed light | Wield classes | **—** | A wield class is not an item. |
| 2 | One-handed | Wield classes | **—** | A wield class is not an item. |
| 3 | Two-handed staff | Wield classes | **—** | A wield class is not an item. |
| 4 | Pistol | Wield classes | **—** | A wield class is not an item. |
| 5 | Rifle | Wield classes | **—** | A wield class is not an item. |
| 6 | Heavy | Wield classes | **—** | A wield class is not an item. |
| light | Light | Droid plating | `Droid_Light_Plating` |  |
| medium | Medium | Droid plating | `Droid_Medium_Plating` |  |
| heavy | Heavy | Droid plating | `Droid_Heavy_Plating` |  |
| armour-class-4 | Armour Class 4 | Armour | `Armor_Class_4` |  |
| armour-class-5 | Armour Class 5 | Armour | `Armor_Class_5` |  |
| armour-class-6 | Armour Class 6 | Armour | `Armor_Class_6` |  |
| armour-class-7 | Armour Class 7 | Armour | `Armor_Class_7` |  |
| armour-class-8 | Armour Class 8 | Armour | `Armor_Class_8` |  |
| armour-class-9 | Armour Class 9 | Armour | `Armor_Class_9` |  |
| zeison-sha | Zeison Sha | Armour | `Armor_Zeison_Sha` | §5.1's NAMED EXCEPTION — baseac 3 / dexbonus 4 sums to SEVEN, not nine. The rule names its own population (rows 38-43) and this row sits outside it. Same shape as §9a's Kyber Dart: named as the exception AND fully carried. |
| robe-1 | Robe 1 | Robes | `Jedi_Robe` |  |
| robe-2 | Robe 2 | Robes | `Jedi_Knight_Robe` |  |
| robe-3 | Robe 3 | Robes | `Jedi_Master_Robe` |  |
| robe-5 | Robe 5 | Robes | `Revan_Armor` |  |
| clothing | Clothing | Robes | `Basic_Clothing` · `Slave_Outfit` |  |
| medpac | Medpac | Consumables | `Medical_Equipment` · `Squad_Recovery_kit` |  |
| adrenal | Adrenal | Consumables | `Adrenaline` · `Combat_Shots` |  |
| shield-generator | Shield generator | Consumables | **—** | OURS, and deliberately. The real energy shields are Forearm_Bands items carrying Charges and a CastSpell property — worn AND spent, which §9 has said since it was written. This names the SPENT half; forearm-band names the slot. |
| charge | Charge | Consumables | `Trap_Kit` · `Fragmentation_Grenades` · `Stun_Grenades` · `Thermal_Detonator` · `Poison_Grenade` · `Flash_Grenade` · `Sonic_Grenade` · `Sonic_Grenade_Type2` · `Adhesive_Grenade` · `Cryoban_Grenade` · `Fire_Grenade` · `Ion_Grenade` |  |
| rocket | Rocket | Consumables | `Rocket` |  |
| spike | Security spike | Supplies | `Security_Spikes` · `Programming_Spikes` |  |
| part | Repair part | Supplies | `Droid_Repair_Equipment` |  |
| object | Object | Objects | `Data_Pad` · `Aesthetic_Item` · `Disguise_Item` |  |
| mask | Mask | Worn slots | `Mask` |  |
| gauntlets | Gauntlets | Worn slots | `Gauntlets` |  |
| forearm-band | Forearm band | Worn slots | `Forearm_Bands` · `Wrist_Launcher` |  |
| belt | Belt | Worn slots | `Belt` |  |
| implant-1 | Implant, level 1 | Worn slots | `Implant_1` |  |
| implant-2 | Implant, level 2 | Worn slots | `Implant_2` |  |
| implant-3 | Implant, level 3 | Worn slots | `Implant_3` |  |
| droid-sensor | Droid sensor | Droid slots | `Droid_Search_Scope_x` · `Droid_Motion_Sensors_x` · `Droid_Sonic_Sensors_x` · `Droid_Targeting_Computers` |  |
| droid-spike-mount | Droid spike mount | Droid slots | `Droid_Computer_Spike_Mount_x` · `Droid_Security_Spike_Mount` |  |
| droid-utility | Droid utility device | Droid slots | `Droid_Utility_Device` |  |
| droid-shield | Droid shield | Droid slots | `Droid_Shield` |  |

**⚠ A BASE TYPE MAY CLAIM SEVERAL ROWS AND NO ROW IS CLAIMED TWICE.** `charge`
is twelve — eleven grenade types and the trap kit — because `§11`'s test is
mechanical shape and not display taxonomy; `droid-sensor` is four for the same
reason. **Eighty rows are claimed, none of them twice**, and the check enforces
that rather than trusting it.

### 14a · The rows no base type claims

**⚠ NAMED, NOT OMITTED.** A row missing from both tables would be invisible;
these are here so that *we have no base type for this* is a statement somebody
made rather than an absence nobody noticed.

| `baseitems.2da` | In | Why not |
|---|---|---|
| `Armor_Armd_Flight_Suit` | k2 | baseac 5 / dexbonus 4 = 9, so it obeys §5.1 and is simply a seventh row the table does not list. 2 items. |
| `Chemicals` | k2 | One item, K2. |
| `Collar_Light` | k1, k2 | A light source. |
| `Components` | k2 | Two items, K2. |
| `Creature_Hide_Item` | k1, k2 | A creature's own hide — 18 items. |
| `Creature_Item_Pierce` | k1, k2 | Creature natural weapons. |
| `Creature_Item_Slash` | k1, k2 | Creature natural weapons — not carried, not authored. |
| `Creature_Weapon_Sl_Prc` | k1, k2 | Creature natural weapons. |
| `Credits` | k1, k2 | Money is tracked, not carried as an item. |
| `Glow_Rod` | k1, k2 | A light source. Our rules model no light radius, so nothing could read it. |
| `Lightsaber_Crystals` | k1, k2 | THE UPGRADE SYSTEM, 104 items. A separate feature; upcrystals.2da and upgradetypes.2da are its own tables. |
| `Miner_Uniform` | k2 | baseac 1 / dexbonus -1. One item. |
| `Pazaak_Card` | k1, k2 | A card game, 23 items. Not equipment. |
| `Pazaak_Sideboard` | k1, k2 | A card game. |
| `Plot_Useable_Items` | k1, k2 | ⚠⚠ DELIBERATELY UNCLAIMED, AND THIS ROW IS A TRAP. 152 items, of which only THIRTEEN are plot items — the rest are upgrade components (emitters 26, ranged cells 30, melee cells 15, edges 15, scopes 16, grips 12). K1 has no Upgrade_Items row and files its upgrade parts here. `object` would claim 152 items to serve 13. |
| `Restrictive_Jedi_Robe` | k2 | ZERO items in either game. A row the games ship and never use. |
| `Stealth_Unit` | k1, k2 | 13 items, belt slot AND the creature-hide bit (0x20400). Belongs with `belt` or its own row; undecided rather than absent. |
| `Torch` | k1, k2 | A light source. |
| `Upgrade_Items` | k2 | THE UPGRADE SYSTEM, 60 items. |

**⚠⚠ THREE OF THESE ARE REAL GAPS AND THE REST ARE DECISIONS.**
`Repeating_Blaster`, `Heavy_Repeating_Blaster` and `Force_Pike` are twenty-four
items of ordinary weaponry with no base type — nobody chose that, it was simply
never noticed. **And `Armor_Zeison_Sha` needs a ruling rather than a mapping:**
its `baseac 3 / dexbonus 4` sums to **seven**, and `§5.1` states the sum is
always nine.

---

## 15. ⚠⚠ The palette tree — where a base type appears in the builder

**Owner-drawn, `PT-2073` and `PT-2078`.** Aurora's own palettes nest **two
levels and never three** — a category, optionally a subcategory, then the item
— and some categories hold items directly. This mirrors that SHAPE; the names
are ours.

**⚠ IT IS A TABLE AND NOT CODE.** The builder reads it. A tree written into
Loom would be a rule with no first state, which this document has now found
five times, most recently in `§14`'s own mapping.

**⚠ `subcategory` OF `worn_at` MEANS *USE THE ROW'S OWN `Worn at`*.** `§12`
and `§13` already carry one per base type — head, hands, forearms, implant,
belt — and restating them here would be a second copy that could disagree.

**⚠⚠ AND `Worn at` IS NOT `Slot` — `PT-2346`.** One column did both jobs while
they happened to read the same, and they stopped the moment `Slot` became the
**equipment map's key**: a forearm band is worn at `forearms` and equipped at
`arm_l` or `arm_r`. **The palette shows a place on a body; the slot is what an
author types.** A display name is not a key — the same sentence `replaces` and
`requires_feat` are both written from.

| Section | Category | Subcategory |
|---|---|---|
| Melee - base weapons | Weapons | Melee |
| Ranged | Weapons | Ranged |
| Lightsabers | Weapons | Lightsabers |
| Armour | Armour | Armour |
| Robes | Armour | Robes |
| Worn slots | Armour | worn_at |
| Droid plating | Droid Armour | Plating |
| Droid slots | Droid Armour | worn_at |
| Consumables | Consumables | — |
| Supplies | Utility | — |
| Objects | Objects | — |
| Wield classes | — | — |

**⚠⚠ A CATEGORY OF `—` MEANS THE SECTION DOES NOT APPEAR IN THE TREE AT ALL**,
and `Wield classes` is the only one: `1`–`6` are not items, they are how a
weapon is held. `gen_base_rules` has excluded them from the palette since it
was written and this says the same thing where a reader can see it.

**⚠ A SUBCATEGORY OF `—` MEANS THE CATEGORY HOLDS ITS ITEMS DIRECTLY**, which
Aurora does too — K1's `Armor` holds 157 items and no subcategory at all. It is
not a gap.

**⚠⚠ AND `Consumables` IS DELIBERATELY FLAT HERE, AGAINST THE DRAWN TREE.**
The drawing gives it *Medical · Stimulants · Grenades · Mines*, and those are
real groupings of the CATALOGUE. They are not groupings of our five base types:
`charge` is grenades AND mines at once — eleven source rows collapsed into one
mechanical shape at `§9` — and `shield-generator` is none of the four. **Four
subcategories over five base types would put one of them in two places and one
in none.** The drawn subcategories belong to the catalogue half of the palette,
which is its own slice; this table covers the base types that ship today.

---

## 16. Creating your own items — `PT-2210`, `PT-2211`

**Every base type in `§2` through `§13` is a real row this project either
ported from `baseitems.2da` or authored deliberately and marked as such. That
covers the great majority of what a weapon or a piece of armour will ever need
to be. Occasionally it does not, and this section is for that case.**

**The motivating example is Force Pike.** Its own base item genuinely exists
in `baseitems.2da` — row 93, `2d6` — but nothing in this project's own,
coarser set of base types matched it, so it sat collapsed onto Quarterstaff's
`1d6` for as long as nobody built anywhere else for it to go. The custom shape
below is what a future item like that declares instead of quietly halving its
own stated damage.

**⚠⚠ THIS IS A PARALLEL PATH, NOT A PARALLEL VOCABULARY — `PT-2211`.** A custom
item does not invent a second way of saying `ranged`, `melee`, `two-handed`, or
any other fact `§2`–`§15` already has a name for. It reuses those names. What
it skips is the BASE TYPE itself — the row in `§14`'s mapping that would
normally supply dice, threat, and multiplier by inheritance. A custom item
states those three directly, on the item, because there is no base type behind
it to inherit them from.

**⚠ REACH FOR A REAL BASE TYPE FIRST, EVERY TIME ONE GENUINELY FITS.** This
section exists for the genuine edge case, not as an equally-standing
alternative to `§2`–`§13`. An item that could honestly be `Vibrosword` or
Blaster Pistol with a named-variant bonus on top — the base-plus-ladder
shape `§3` already uses for Long Sword — should be that, not a custom
declaration. Custom is the fallback, not the default.

**WHAT A CUSTOM ITEM DECLARES:**

| Field | Values | Meaning |
|---|---|---|
| `kind` | `ranged` · `melee` · `lightsaber` | Which of the three weapon families it belongs to — governs which era rule (`§4b`'s K1/K2 split) would apply if this item were ever folded back into a real base type later. |
| `attacks` | as `§16.1` below | One-handed or two-handed, stated the same way an ordinary base type states it — `PT-2223` ruled this is the field a custom item uses, not `wield`, so nothing new needs inventing for `isDoubleWeapon` or `§7.4`'s own reader to understand it. |
| damage | `NdM`, plus any bonus dice or flat modifier | Stated directly. No base type supplies this by inheritance, so the item's own row is read exactly as authored — no folding, no layering against a base that does not exist. |
| threat / multiplier | as a base type would state them | Same reasoning as damage — nothing to inherit, so the item states its own. |

**⚠ `openItem` REFUSES AN ITEM THAT NAMES BOTH A BASE TYPE AND A CUSTOM
DECLARATION.** A custom item has nothing behind it to fall back to if its own
fields are incomplete — that is the whole point of the shape — so it cannot
also claim a base type without making the two disagree about where its real
numbers live.

**⚠⚠ A CUSTOM WEAPON IS EXCLUDED FROM `§7.4`'S TWO-HANDED STRENGTH BONUS ON
THE SAME TERMS A BASE-TYPE DOUBLE WEAPON IS — NOT ON ANY TERMS OF ITS OWN.**
`§7.6`'s double-weapon exclusion and `§16`'s custom shape are unrelated
mechanisms answering the same underlying question (does this weapon already
get compensated for the tradeoff `§7.4` exists to offset), and a custom
double-bladed item is read by the identical rule an ordinary one is, per
`PT-2223`.

### 16.1 · Handedness on a custom item

**`attacks` is a whole number, the same field an ordinary base type carries at
`§14`.** `1` means one-handed. `2` means two-handed. Nothing else is a valid
value, and the fitted-component fold and `isDoubleWeapon`'s own reader both
already expect exactly this shape — a custom item that states `attacks: 2`
is read by the same logic Vibro Double-Blade and Quarterstaff already are.

**⚠ `§4a`'s Attacks column and `§4b`'s `wield` STRING BOTH EXIST FOR
HISTORICAL REASONS ON THE SHIPPED BASE TYPES — `isDoubleWeapon` READS BOTH,
BECAUSE THE DOCUMENT ITSELF USES BOTH.** A custom item does not inherit that
history. It states `attacks` and nothing else, because there is no reason for
new content to carry an inconsistency that only exists because two sections of
this book were written at different times.

---

## 17. ⚠⚠ Item gates — who may equip a thing, and how several of them combine — `PT-2122`, `PT-2128`, `PT-2342`

**The channel has existed since `PT-2122` and has never had a section.**
`extract_item_gates` reads it, `check_item_gates` holds it, `item_gates.json`
carries **401 gates on 302 of 1,424 items** — and no rules document said what
one was. This is that section.

### 17.1 A gate is a refusal to EQUIP, not a penalty for using it anyway

**Measured from the games' own feedback strings, which is also how we know the
six categories are one mechanism rather than six similar ones:**

    1475   You do not have the proficiencies required to equip that item.
    1512   You do not have the required alignment to equip this item.
    1513   You do not have the required class to equip this item.
    1514   This species cannot equip this item.              ⚠ K2 only
    38450  You cannot equip this item. You don't have the
           prerequisites. Please see the item description.   ⚠ K2 only

**⚠ THE WORD IS `equip`, NEVER `use`.** A gate decides whether the thing goes
on. **Once it is on, it works exactly as any other item does** — there is no
reduced effect and no penalty anywhere in the mechanism.

### 17.2 ⚠⚠⚠ Several gates of ONE category are `OR`. Across categories they are `AND` — RULED, `PT-2342`

**This is the rule that is easiest to get wrong by assumption and it is not a
reading — the shipped data states it about itself.** Two real items are
equippable by **nobody at all** under a whole-`AND` reading:

    Cassus Fett's Heavy Pistol    Power Attack · Power Blast ·
       `g_w_hvyblstr09`           Rapid Shot · Sniper Shot
                                  ⚠ four attack chains a character picks ONE of

    Personal Crystal `{01_D}`     Dark Side · Neutral
       `qcrystal_1_1`             ⚠ and `{01_VD}` is Dark Side ALONE,
                                  so the two must be distinguishable

> **⚠⚠ RULED:** *"A fact this decisively proven and this easy to get wrong by
> assumption shouldn't be left implicit for six different future
> implementations to each infer on their own."*

**So `Dancer's Outfit` is `Female` AND (`Handmaiden` OR `Mira` OR `Player`).**
**43 items carry more than one gate in a single category** — it is the ordinary
case, not an edge one.

**⚠⚠ AND IT REFRAMES THE 55 ATTACK-CHAIN FEAT GATES.** They are not four
separate requirements. They are **one test — *does this character have any
attack chain at all*** — and reading them as four would have barred every
character in the product from the items carrying them.

### 17.3 The six categories, and which game can express each

    feat        217 gates / 183 items    both games
       118 bay gate (Droid Upgrade 1·2·3) · 55 attack chain · 44 other
    alignment    73 /  54     both games        ⚠ 57 of them are §17.5
    character    63 /  61     ⚠ K2 only         46 `Player` · 17 named
    attribute    42 /  42     ⚠ K2 only         ALL implants, ALL Constitution
    class         5 /   3     property in both, used only by K2 items
    gender        1 /   1     ⚠ K2 only

**⚠⚠ FOUR OF THE SEVEN USE-LIMITATION PROPERTIES DO NOT EXIST IN K1's ENGINE** —
character, attribute, gender, and a `Subrace` one **no shipped item uses at
all**. `nwscript.nss` declares constants only for the four K1-era rows, so the
K2 four are engine-side and invisible to script in both games.

**⚠ `UseLimitationRacial` IS OMITTED BY `PT-2128`** — 163 rows, every one
reading `(Human)`, proven redundant. `extract_item_gates` refuses any racial
row at another subtype rather than dropping it, so the omission keeps checking
that it is still true.

**⚠ AND TWO ALIGNMENT GROUPS THE GAMES DEFINE ARE USED BY NOTHING** — `100%
Dark` and `100% Light`. Measured absence, not an assumption.

### 17.4 ⚠⚠ Implants carry TWO real gates, and both apply — RULED, `PT-2342`

**`§14`'s implant rows are gated by a feat chain** — *Cybernetic Implantation
allows level 1, Advanced allows 1-2, Master allows 1-3* — **and the K2
catalogue gates the same items by Constitution:**

    implant-1 → CON ≥ 12        implant-3 → CON ≥ 16 **or** 18
    implant-2 → CON ≥ 14

> **⚠⚠ RULED: both apply.** *"This isn't two answers to one question competing
> for the win; it's two real constraints that happen to overlap on the same
> items."* A character needs the correct feat tier **and** the Constitution
> score — `§17.2`'s `AND` across categories, applied consistently.

**⚠⚠ THEY ARE NOT REDUNDANT AND THE PROOF IS STRUCTURAL: the feat chain has
three tiers and cannot express `implant-3`'s split into 16 and 18.** The CON
gate, in turn, says nothing at all about feat prerequisites.

**⚠⚠⚠ AND THE 22 K1 IMPLANTS STAY UNGATED, FAITHFULLY — `PT-2342`.** All 40 K2
implants carry a CON gate and **not one K1 implant does, because the property
does not exist in K1's engine.** This is not `PT-2184`'s shape, where K2 is the
later and more complete standard for a mechanism both games have; it is the
same structural absence already honoured for the shields' K1 Repair-duration
term. **Each game gets its own real capability rather than K2's mechanism
imported onto an engine that cannot carry it.**

### 17.5 ⚠⚠ Two things this section deliberately does NOT cover

**⚠ ALIGNMENT GATES ARE WIELDER-ONLY and need no target tracking** — the
engine's own message is *"You do not have the required alignment to **equip**
this item."* But they need a character alignment VALUE, and there is none:
`CHARACTER-RECORD-01` has no such field and `PlayState` names it deliberately
unbuilt, *"nothing emits `character.alignment-shifted`, so it is not built."*
**`ALIGNMENT-01-v2` authors seven bands and the gate speaks in three groups; the
mapping is held for that thread and is not pre-decided here.**

**⚠⚠ AND THE PERSONAL CRYSTAL IS NOT A GATE AT ALL.** The 45 `qcrystal` items —
nine tiers × five variants — carry **57 of the 73 alignment gates**, and what
they express is **variant selection as the player drifts**, not permission:

    {01_VD}  Dark Side                 {01_L}   Light Side · Neutral
    {01_D}   Dark Side · Neutral       {01_VL}  Light Side
    {01_N}   ⚠ no alignment gate at all

**It has no base type**, so it is a fitted component rather than equipment, and
the equip refusal in `§17.1` was never going to apply to it. **Held as its own
item, once alignment tracking exists to drive it.**
