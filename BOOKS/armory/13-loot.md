# Chapter Thirteen — Loot

**Status: DRAFT, for review.** Second of the Armory's four remaining chapters.

---

Chapter Eleven priced the catalogue and sorted it into tiers. **This chapter is how any of
it reaches a player.**

It answers one question — *what is in this container* — and it answers it the same way
every time, because the interesting variable is not the roll.

---

## The whole rule

> **Roll `d100`. Read the band. Take the item that band names on the area's table.**

**The roll never changes. The table does.**

Everything else in this chapter is about which table you are reading from.

## The bands

**Ported unchanged from `a_give_treas`, KOTOR 2's own compiled treasure script**
(`PT-307`):

| Roll | Band |
|---|---|
| **1–60** | 1 |
| **61–69** | 2 |
| **70–79** | 3 |
| **80–89** | 4 |
| **90–100** | 5 |

**60% / 10% / 10% / 10% / 10%**, and the thresholds — 60, 70, 80, 90 — are the source's own.

**A natural 100 reads as band 5.** The source gives it no special treatment and neither
does this game; there is no critical-loot rule hiding at the top of the range.

## The area tier — the part KOTOR 2 was missing

**KOTOR 2's tables are already tiered by grade** — `MEDEQPMNT01 → 02 → 03`.

> **But K2 never gated the tier by *level*.** It gated by which container a designer
> flagged, **which is why a level-3 character can pull a top-tier crystal out of a
> footlocker.**

**This game adds the missing gate:**

| Character level | Tier |
|---|---|
| 1–5 | 1 |
| 6–12 | 2 |
| 13–20 | 3 |
| 21–30 | 4 |

**Band 5 on a tier-1 table is the best tier-1 item.** It is still a moment — a good roll
still feels like one — **but it cannot break the curve.** That is the whole design: keep
the excitement of the roll and remove its ability to invalidate the next ten levels.

## How an area gets its tier

> **area tier = max( encounter level, container difficulty )**

### Encounter level — free, and it covers improvisation

**A GM who invents a room does not assign it a difficulty. But they do place something in
it.**

> **The loot tier is the tier of the thing guarding it.** Drop a level-12 zakkeg in a cave
> and **the cave is a level-12 cave. Nobody had to write that down.**

Use the average level of the encounter, or the highest if you would rather reward the
hardest fight. **GM's choice — state which at the table.**

**And it self-corrects in both directions:**

    wander somewhere too hard    the loot is too good — correct, you earned it
    backtrack to a starter zone  starter loot — also correct, the encounters
                                 there are still level 2

### Container difficulty — the floor

**A vault behind a hard lock is a high-tier container even if a rat guards it. A crate is a
crate even in a dragon's lair.**

**Its `Security` DC is its tier:**

| DC | Tier | Who opens it |
|---|---|---|
| up to 15 | 1 | 5 ranks, `Int +0` |
| 16–20 | 2 | 10 ranks |
| 21–27 | 3 | 15 ranks |
| 28+ | 4 | 18 ranks — a late-career build |

**A `Security` DC names a specific character rather than a probability**, because
`SKILL-RESOLUTION-01`'s take-10 makes the ceiling `10 + ranks + Intelligence`.

> **A GM setting a DC because it fits the fiction is setting a tier as a side effect.**

**⚠ This half is authored.** KOTOR's placeables carry no lock DC at all — 376 were sampled
and the field is simply absent. **The `Security`-DC ladder is ours, not the source's.**

### Neither? Fall back to party level

An empty room, a wandering merchant, a container with no fight attached.

**Party level is the highest character level in the party** (`PARTY-01 §2`, `PT-655`).
**Players only — companions do not count.**

### The explicit override

**A campaign-package author may set an area's tier directly, and it wins over both
derivations.**

> **The derivation is for improvisation; an authored campaign should say what it means.**

It also covers the one case the derivation gets wrong — **a trivial guard on a treasure
vault.** Container difficulty mostly handles that, but a GM who wants a specific outcome
should not have to reverse-engineer a lock DC to get it.

## World danger — a ceiling, never a floor

The Atlas supplies a **`danger` field per world, 1 to 4**, derived from what the setting
says about the place.

    288 worlds · 180 at danger 1 · 31 at 2 · 73 at 3 · 4 at 4
    the four:  Korriban · Rakata Prime · Taris · Yavin

**⚠ It is not a third term in the max**, and the reason is worth stating carefully:

> **A world danger of 4 does not make every room on Korriban a tier-4 room. It makes the
> Valley of the Dark Lords tier 4 and the spaceport tier 1.**

**The rule:**

    area tier = min( max(encounter, container), world danger + 1 )

**The `+1` is deliberate.** A world's danger describes the place as a whole, and one room
may exceed it. **A tier-1 world with a Sith vault in it is possible; a tier-1 world that is
entirely tier 4 is not.**

**Why a ceiling and not a floor.** The first two inputs are **local** — they describe the
room and the container in front of the party. Danger is not; it describes hundreds of
worlds at once and cannot know what is in this room.

> A rule that let it **raise** a tier would put Sith-vault loot in a Korriban cantina. A
> rule that lets it **cap** one stops a GM's improvised room on a quiet farming world from
> producing a lightsaber crystal.

**And the constraint bites, deliberately.** 180 of 288 worlds are danger 1, **which caps
most of the galaxy at area tier 2.** That is the intent: **most of the galaxy is quiet, and
a party wanting tier-3 loot should have to go somewhere that earns it.** A GM may override
— the field is a default, not a fence.

## Named sites — authored places on generated worlds

**Some places have names, and a name is a reason.**

The Atlas maintains **47 hand-curated named sites across 32 worlds** — the Dxun tomb, the
Korriban academy, the Rakatan temple, Dantooine's Jedi Enclave and Rakatan ruins,
Dellalt's decoy vaults, Lord Garu's temple on Ashas Ree.

**Two tests decide what goes in the list**, and both are narrower than they sound:

- **Named and visitable, not important.** *"Dellalt's decoy vaults qualify because a party
  can walk into them, not because Xim's treasure matters."*
- **Present at 3,956 BBY.** A site enters the field **only if it exists at the campaign
  date.** The alternative — recording every place ever named with an era note — **was
  declined because it would give the project two answers to one question**; `Bespin`'s
  world entry already excludes Cloud City in prose.

**The rule is smaller than it looks:**

    a container at a named site takes the explicit-override route — the GM names the tier
    everywhere else on that world, the normal derivation applies unchanged
    and world danger still caps both

> **A named site does not raise the tier. It moves the world from *generated* to
> *authored, here*.**

**A GM improvising in the Korriban academy does not roll a generic tier.** The place has a
name and therefore a reason.

## Unique items

**KOTOR 2's own failure: you could find *Onasi's Blaster* twice.**

> **An item marked unique can be obtained once per campaign. Once obtained, it is removed
> from every table it appears on.**

### What counts as unique — and the tell the flag missed

    plot-flagged in the blueprint    56 items — the source already says so
    named after a person             29 more

**Eighty-five items in total, and the `Plot` flag covers only two thirds of them.** The
rest are caught by a different signal: **a possessive in the name.** Nomi's Robe, Freedon
Nadd's Blaster, Ulic Qel-Droma's Mesh Suit, Thon's Robe.

> **There was one Nomi Sunrider and she had one robe.**

### Two halves, and both are needed

**Once per campaign.** Found, bought, or crafted — **the first acquisition is the only
one.**

**Once per roll.** A single loot roll cannot produce two of the same item, and a vendor
cannot stock two.

**⚠ The second half is not implied by the first.** A table that removes an item *after*
acquisition still allows a roll that produces two at once.

### And it interacts with two other rulings

**A unique item cannot be a droid bay upgrade** — those are `Mark I` through `Mark V` of a
repeatable type. **But a unique item *can* grant an attack chain:** *Arg'garok* is unique
and grants `Power Attack`. **That is the point of it.**

## Two rules that exist only for the engine

**This chapter contains the first rules in the project written for software rather than for
a table, and they are marked as such rather than dressed up as table rules.**

**Party composition.** A band-5 roll can produce a droid upgrade, and a party with no droid
gets nothing. **The table checks party composition and excludes items no party member can
use.**

**Unique-item enforcement.** The table removes an item on acquisition and de-duplicates
within a single roll.

    app   the table filters, removes and dedupes
    GM    no rule needed — they already know who is in the party and what
          they handed out

> **A GM at a table does not need a rule telling them not to give a droid upgrade to four
> organics.**

**Both are recorded as engine-only deliberately.** A rules document that scatters
software-only requirements through its table-facing text makes both harder to read.

## What this fixes

    K1   hand-placed   balanced, because a designer chose — but identical every replay
    K2   randomised    varied — but a level-3 character can pull a top-tier crystal

> **One has no surprise. The other has no restraint.**

**This is K1's balance emerging from the mechanism rather than from a designer's hand, with
K2's variety intact.**

**And it is why moving past the shipped worlds costs nothing.** Authored packages name
their tiers; a GM improvising uses the encounter that guards the container; a generator
runs the same rule. **The three routes produce the same kind of room, and only the author
differs.**

---

*Sources: `LOOT-01`, with `PT-307` (the bands, ported), `PT-308`/`PT-309` (the tier gate,
authored), `PT-323` (party composition), `PT-327` (unique items), `PT-404` (world danger),
`PT-651` (every item carries a tier), `PT-655` (party level), `PT-666` (authored versus
generated), `PT-912`/`PT-922` (named sites). `SKILL-RESOLUTION-01` for take-10;
`PARTY-01 §2` for party level; `ITEMS-01`–`08` for the tier data.*

## Open items, carried from review

**⚠⚠ Flag 1 — the band-to-table mapping is an inference, and the source document says so.**
This is the largest open item in the chapter. `PT-307` **read the constants out of
`a_give_treas`, not the control flow** — so the band *thresholds* (60/70/80/90) are
verified, but **which band draws from which list is unverified** until someone disassembles
the script properly.

**Everything above is written as though band 5 draws the best item on the table**, which is
the natural reading and matches observed play. **It is not confirmed.** If the mapping turns
out to be different, the bands table stands and only the interpretation moves.

**⚠ Flag 2 — every item carries a tier, and the count in circulation is stale.** `PT-651`
closed this: **1,385 rows across `ITEMS-01`–`08`, zero blanks** — tier 1: 634, tier 2: 427,
tier 3: 213, tier 4: 111. **The figure of 994 still appears in places** and is the blueprint
count, not the item count. `LOOT-01` notes the drift against itself: *"the corpus grew past
it and the paragraph did not."*

**⚠ Flag 3 — `LOOT-01` carries a duplicated paragraph with a broken cross-reference.** Its
`§7b` states *"Procedurally generated areas are not covered by ."* — the reference is
missing entirely — and then repeats the same paragraph immediately with the reference
filled in as *"section 4"*. **The first copy should be deleted.** Same shape as the
`EVENTS-01` heading defect from the Galactic Timeline: an edit that added a corrected
version without removing the broken one. **Reported, not fixed — `LOOT-01` is a rules
document.**

**⚠ Flag 4 — the named-site count appears twice with different values.** `PT-912` records
**45 sites across 31 worlds**; `PT-922` records **47 across 32**, hand-curated, delivered.
**Both sit in the document.** The later supersedes under `§3b`'s later-wins rule and this
chapter uses **47 / 32** — but a reader meeting 45 first has no way to know it is
superseded. **Same class as the Timeline's stale `"ranking fifth"` numeral.**

**⚠ Flag 5 — the world count does not match the Atlas's.** `LOOT-01` reports **288 worlds**
carrying a `danger` value; `PT-1705` establishes that `data/extracted/worlds.json` holds
**301 world entries** — a figure it explicitly corrected from 290 *"before it became the
working number."* **Thirteen worlds are unaccounted for.** They may simply lack a danger
value, in which case the fallback is party level and nothing breaks — **but the chapter
cannot say so, because no held source states it.** Worth one check by whoever owns the
Atlas.

**Not a flag: `§7` and `§7b` state `PT-651` twice in near-identical terms.** Harmless
duplication rather than contradiction, but it is the same edit pattern as Flag 3 and the
two were probably introduced together.
