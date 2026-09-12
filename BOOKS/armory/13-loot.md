# Chapter Thirteen — Loot

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

**Ported unchanged from KOTOR 2's own treasure script:**

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

**⚠ One honest caveat about the bands.** The roll thresholds above — 60, 70, 80, 90 — were
read directly out of the game's own script and are certain. **Which band draws from which
list is an inference**, taken from how the tables are ordered and from how loot behaves in
play. **It has not been confirmed against the script's own logic.**

**Everything below assumes band 5 draws the best item the table can offer**, which is the
natural reading. **If that turns out to be wrong, the bands stand and only their mapping
moves.**

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
taking 10 on a skill check makes the ceiling `10 + ranks + Intelligence`.

> **A GM setting a DC because it fits the fiction is setting a tier as a side effect.**

**⚠ This half is authored.** KOTOR's placeables carry no lock DC at all — 376 were sampled
and the field is simply absent. **The `Security`-DC ladder is ours, not the source's.**

### Neither? Fall back to party level

An empty room, a wandering merchant, a container with no fight attached.

**Party level is the highest character level in the party. Players only — companions do
not count.**

### The explicit override

**A campaign-package author may set an area's tier directly, and it wins over both
derivations.**

> **The derivation is for improvisation; an authored campaign should say what it means.**

It also covers the one case the derivation gets wrong — **a trivial guard on a treasure
vault.** Container difficulty mostly handles that, but a GM who wants a specific outcome
should not have to reverse-engineer a lock DC to get it.

## World danger — a ceiling, never a floor

**Every world in the Planetary Atlas carries a danger rating from 1 to 4**, derived from
what the setting says about the place.

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

**The Planetary Atlas names 47 such sites across 32 worlds** — the Dxun tomb, the
Korriban academy, the Rakatan temple, Dantooine's Jedi Enclave and Rakatan ruins,
Dellalt's decoy vaults, Lord Garu's temple on Ashas Ree.

**Two tests decide what goes in the list**, and both are narrower than they sound:

- **Named and visitable, not important.** *"Dellalt's decoy vaults qualify because a party
  can walk into them, not because Xim's treasure matters."*
- **Present at 3,956 BBY.** A site qualifies **only if it exists at the campaign date.** The alternative — recording every place ever named with an era note — **was
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

## Sources for this chapter

**The roll and its bands are KOTOR 2's own**, read out of the game's treasure script and
ported unchanged.

**Everything else is this game's addition**, and the chapter says so where it matters: the
tier gate the games never had, the `Security`-DC ladder — **KOTOR's containers carry no
lock difficulty at all, across 376 sampled** — the world-danger ceiling, and the named-site
override.

**The tier data behind it all** comes from this book's own catalogue chapters, where every
item carries a tier from 1 to 4.
