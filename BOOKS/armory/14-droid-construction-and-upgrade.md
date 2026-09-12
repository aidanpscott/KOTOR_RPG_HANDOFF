# Chapter Fourteen — Droid Construction and Upgrade

**Chapter Seven covers 135 droid items. Chapter Twelve found five entries on the crafting
bench that were not recipes at all** — a processor, a chassis, a control cluster, a
vocabulator and a protocol pacifist package — and said they belonged here.

**Four of the five are where they belong.** A droid is the one thing in this book you can
build from nothing, and the one thing that can be upgraded past the ceiling every other
character sits under.

**⚠ The fifth has no rule, and this chapter would rather say so than invent one.**
`hkpart05`, the **HK Protocol Pacifist Package**, belongs to KOTOR 2's rebuild of one
particular droid rather than to droid construction in general. **It has no cost, no tier and
no place in a build here.**

---

# Part One — Building a droid

## The model, and the one place it departs

**The system is modelled on KOTOR 2's lightsaber quest, and made deliberately easier.**

That quest needs four components — emitter, energy cell, lens, crystal — at roughly 2,350
credits for a basic set. **A droid also takes four parts. The difference is where you get
them:**

> **The lightsaber's parts are quest-gated. A droid's are not.** *"These parts should be
> available at droid merchant kiosks and whatnot."*

**You do not travel the galaxy for a motivator. You buy one.** That is the single
deliberate departure from the model.

## The four parts, and they were in the files all along

**The parts are not invented.** KOTOR 2 has its own droid-parts quest, and it carries them
with prices attached:

| Part | File | What it is |
|---|---|---|
| **Chassis Frame** | `hkpart02` | The physical structure. **It decides which chassis the droid is** |
| **Droid Processor** | `hkpart01` | *"A cognitive module or logic processor… without one, a droid could not function"* |
| **Control Cluster** | `hkpart03` | Actuation and coordination. **Without it the droid does not move** |
| **Vocabulator** | `hkpart04` | Speech |

**Three are universal. One decides the chassis.**

**And the Vocabulator quietly settles two things the setting had already established.** A
droid has no sex, but its voice module can read masculine, feminine or neither — **this is
that component, and it is a part you buy.** And the `LB-series`, described as *"a
fifth-class drone, no speech center"*, **is simply a droid built without one.**

**⚠ There is no Power Cell.** The lightsaber quest has an energy cell and it is an easy
assumption that a droid needs one too. **The droid quest has no power component, and this
game did not invent one to match it.**

## The chassis is the price. Everything else is nearly flat

**This is the finding that reshaped the whole system**, and it inverted the original
assumption:

    the HK Chassis        1,500
    the other three       691 together

**The body is the cost; everything inside it is cheap.**

    Marksman-H chassis            ~200      a remote
    HK Chassis                   1,500      an assassin droid
    the three internal parts, light  350
    the three internal parts, heavy 1,390

**The three internal parts scale ×4 across the tiers. The chassis scales ×7 across the
roster.**

> **A build's cost is mostly the frame — which is what a player already chose when they
> picked a model. The parts are the tax; the chassis is the decision.**

## Brain first, body second

**The setting gives the build order, and it is the reverse of the obvious one:**

> *"When a droid was built properly, it was usually **the processors that were the starting
> point**, followed by the physical structure."*

**A droid is a mind you then build a body around.**

### The two-part minimum

    Droid Processor + Chassis Frame     a droid that thinks and exists

**That is the source's own pair.** Such a droid **does not move** — no Control Cluster — and
**cannot speak** — no Vocabulator.

> **A two-part droid is a legal build and a useless companion.** It is what a player finds
> in a wreck.

## The parts ladder

**Parts scale by chassis tier**, and the three-tier shape is the game's own rather than
something imposed on it — **KOTOR's droid plating already sorts into Light, Medium and Heavy
with three types each**: `g_i_drdltplat001`–`003`, `g_i_drdmdplat001`–`003`,
`g_i_drdhvplat001`–`003`.

| Part | Light | Medium | Heavy |
|---|---|---|---|
| **Droid Processor** | 165 | 330 | 660 |
| **Control Cluster** | 125 | 250 | 500 |
| **Vocabulator** | 60 | 115 | 230 |
| **Chassis Frame** | *per model* | *per model* | *per model* |
| **Parts subtotal** | **700** | **1,400** | **2,800** |

    Light    Remote · Protocol
    Medium   Astromech · Probe · Labor
    Heavy    Battle · Assassin

**The Droid Processor is the dearest of the three at every tier** — it is the part that
makes a droid a character rather than a machine.

**A flat 2,800 at every tier would break the low end.** Against model prices running 350 to
4,200, it would make building a `Marksman-H` **nine times** the cost of buying one.
**Tiered, a Marksman-H costs 900 to build against 350 to buy** — still a bad deal, which is
right for a mass-produced throwaway, **but a bad deal rather than an absurd one.**

## Build or buy

| Frame | Frame price | Built total | Assembled price |
|---|---|---|---|
| **Protocol** | 400 | 3,200 | **2,000** |
| **Labor** | 400 | 3,200 | **2,000** |
| **Astromech** | 1,400 | 4,200 | 4,000 |
| **Remote** | 1,400 | 4,200 | 4,000 |
| **Probe** | 1,900 | 4,700 | 5,000 |
| **Battle** | 2,900 | **5,700** | 7,000 |
| **Assassin** | 4,100 | **6,900** | 9,000 |

> **Building is cheaper at the top and dearer at the bottom, and that is the point.**

An Assassin frame built costs 6,900 against 9,000 assembled — **a saving of 2,100.** A
Protocol droid built costs 3,200 against 2,000 — **you lose 1,200 by building it.**

**The universal parts do not scale, so they dominate a cheap droid and vanish into an
expensive one.** Nobody builds a protocol droid; everybody builds an assassin droid.
**That is what a crafting system should do.**

## Who may build one

    Machinist       yes
    Droid Master    yes
    Engineer        yes
    anyone else     no

> **A Machinist builds droids as a trade. A Droid Master builds the ones he will use. An
> Engineer builds one and usually stops.**

**The Machinist keeps what distinguishes it:** it is the only one who can build a droid
**for someone else**, and the only one whose `Repair` and `Scavenging` reduce the parts
bill.

**⚠ `Droid Master` is a prestige class**, and prestige classes live in the Advanced
Player's Guide rather than the Player's Handbook. **A reader working from the Player's
Handbook alone will not find it there.**

## Assembly

    Requires    all four parts, and a workbench — or a Portable Workbench,
                which an Astromech is
    Check       Repair, DC 15 + 5 per chassis price tier
                Protocol/Labor 15 · Astromech/Remote 20 · Probe 20
                Battle 25 · Assassin 30
    Time        one day per 1,000 credits of total parts cost
    On failure  the parts are NOT lost. A day is. Try again tomorrow.

> **Failure costing time rather than parts is the departure that makes this easier than the
> lightsaber quest.** A quest component you cannot replace is a quest; **a day is an
> inconvenience.**

**Crafting's downtime rule applies** (Chapter Twelve): one period, one choice among rest,
meditation, crafting, or droid construction.

## Building from salvage — the junk droid

**The setting already has a name and a consequence for building cheap:**

> *"**Monster droid**, also known as a **junk droid**, was the term used to describe any
> droid created by piecing together component parts of many other droids… because of their
> mashed-together programming they were considered dangerous by most civilized people, for
> they could **go on a rampage, confuse orders**, or even start building more of their own
> kind."*

    Cost    half the tier's part price — 350 / 700 / 1,400
    Check   Repair at the model's DC +5

**And it is a junk droid, permanently:**

- **Its Droid Processor is scavenged, so it takes `−2` to every chassis action.**
- **On a natural 1 on any attack or chassis action it confuses the order** — it does
  something adjacent and wrong, and the GM decides what.

**That is *"confuse orders"* as a rule and *"rampage"* as the GM's option.** The source
names both.

**A junk droid cannot be upgraded above `Droid Upgrade 1`** — its sockets are already full
of somebody else's parts.

> **A found frame rebuilt with scavenged parts is a junk droid. One rebuilt with bought
> parts is not.**

## Rebuilding a destroyed droid

**The frame always survives.** It is wreckage, and wreckage is repairable.

    the Chassis Frame survives
    the three internal parts are destroyed
    the same Repair check, at the same DC
    one day, regardless of chassis

**So a rebuild costs the tier's parts bill and nothing more** — **700 light, 1,400 medium,
2,800 heavy.** A destroyed Assassin droid costs **2,800** against the 6,900 a fresh build
costs; a destroyed Remote costs **700**. The expensive part of a droid is its body, and the
body is what is left.

**⚠ But every installed upgrade is lost.** Bay installations are permanent **and consumed**
— they do not come out of a wreck. **Socket items are gear and are recovered.**

> **That is the real cost of losing a droid, and it is not the credits.** A nine-bay droid
> at tier-3 socket prices has more value installed than the chassis ever cost.

**A droid PC rebuilds on all three difficulty modes**; **on `Hard` the bays come back
empty.**

---

# Part Two — Sockets and Bays

**Two systems, not one**, and the reason is worth stating before any of the detail:

> *"What we're designing is not a replacement for the stuff that's already there. They're
> different entirely."*

    sockets        ported from KOTOR 2. Gear. Swappable.
    installations  AUTHORED. Permanent. Consumed. The reason to play a droid.

## Sockets — ported

**The source has six slots, not four:**

| Socket | What it grants |
|---|---|
| **Tool** | capability — feats, skills, attack bonus |
| **Interface** | raw statistics — abilities, skills, saves |
| **Plating** | defence |
| **Device** | active abilities — things you press |
| **Shield** | a device subtype |
| **Named** | HK-47, T3-M4, G0-T0 only |

> **The six are genuinely distinct. `Interface` gives you numbers, `Tool` gives you
> capabilities, `Device` gives you buttons to press.**

**Each socket item requires `Droid Upgrade 1`, `2` or `3`** — 71 items across the three
tiers, from 1 credit to 30,000.

**Swappable, like any equipment.** Unequip and the bonus goes.

**⚠ `Named` items are character-locked in the source, and a KOTOR-era campaign has no
HK-47.** They become **a template for unique droid gear** rather than three specific
characters.

## Bays — authored

> **A droid has bays. Any upgrade fits any bay. Filling one is permanent.**

**Permanence is the whole point. It is what makes an upgrade different from gear.**

    socket item   swap freely. Unequip and the bonus goes.
    bay upgrade   installed once. It does not come out.

### How many bays

    Droid Upgrade 1    3 bays
    Droid Upgrade 2    6 bays
    Droid Upgrade 3    9 bays

### Class grants the ladder; level is the floor

**`Droid Upgrade` and `Plating Proficiency` arrive at levels 1 / 7 / 13 for every droid.
A class may bring them earlier. Nothing brings them later.**

| Class grants | Tier 2 at | Tier 3 at |
|---|---|---|
| **Soldier · Brawler · Sith Warrior** | **4** | **9** |
| **Marksman · Bounty Hunter · Engineer · Machinist · Droid Master** | 5 | 11 |
| **Scout · Agent · Smuggler · Treasure Hunter · Medic · Duelist · Sith Assassin · Sith Inquisitor** | 7 | 13 — *the floor* |

> **The fighters and the engineers plate up early. Everyone else waits.**

**No class raises the ceiling.** A Soldier reaches `Droid Upgrade 3` at character level 9 —
four levels early — and that is **earliness rather than a higher ceiling.**

### The chassis caps the ladder

    Assassin · Battle · Labor · Probe · Protocol    up to Droid Upgrade 3
    ASTROMECH · REMOTE                              STOP AT Droid Upgrade 2

> **Those two chassis cap at six bays, permanently.**

**A diagnostic computer and a floating sensor do not accept nine hardpoints.**

**It also closes a prestige class without a special rule:** `Juggernaut` requires
`Droid Upgrade 3`, so **an Astromech or Remote can never hold it.**

## Bays are untyped. Sockets are typed.

    sockets       six, and each takes one KIND of item
    upgrade bays  nine at most, and ANY upgrade fits ANY bay

> **A socket asks *what kind of thing is this*. A bay asks only *do you have room*.**

**Which makes the bay the interesting choice** — a droid with six bays picks *which* six
upgrades to run, from every type at once.

## What an upgrade can be

| Type | Marks | What |
|---|---|---|
| **Skill** | I · II · III | `+1` / `+2` / `+3` to one skill |
| **Ability** | I · II · III | `+1` / `+2` / `+3` to one score |
| **Feat** | tiered by the feat | some feats are worth far more than others |
| **Attack chain** | tiered | grants tier 1, 2 or 3 of one chain |

**No cap on feats, no cap on attack chains, no escalating price** — **because the bay count
already caps everything.** A droid with six bays running six feat upgrades has spent all
six bays. **A second cap on top of a hard slot limit is a rule that never fires.**

## Why bays exist at all

**A droid cannot be a Jedi, cannot spend attack credits on melee, cannot take a Force or
Combat-rate class, and cannot exceed eleven chains.**

> **Five hard restrictions, and nothing had ever paid for them.**

**Bays do.** A droid climbs past the ceiling every other class sits under by running
upgrades an organic has to be born with or train for.

**It is how a droid becomes the equivalent of a Jedi — with the restrictions still in
place.**

## Where a droid upgrade comes from

    CRAFTED   Chapter Twelve's rules, which name droid work explicitly
    BOUGHT    droid specialists
    FOUND     Chapter Thirteen, band 5 at the area's tier

**All three routes exist and are built.** And the loot table checks party composition —
**a party with no droid gets nothing** — which is one of Chapter Thirteen's two engine-only
rules.

---

## Sources for this chapter

**The four parts are KOTOR 2's own.** `hkpart01` through `hkpart04` are real items in the
game's files, carrying real prices, and this chapter takes its parts list from them rather
than inventing one.

**The build order, the junk droid and the `LB-series` come from the setting**, quoted
directly where they are quoted.

**Everything else is this game's addition**, and the chapter says so where it matters: the
tiered parts ladder, the build-or-buy economics, the `Repair` DCs and build times, the junk
droid's two penalties, and the whole of Part Two's bay system. **Sockets are ported from
KOTOR 2. Bays are not** — and the chapter keeps the line between them visible throughout,
because it is the line between gear and permanence.

**The model prices, plating tiers and socket-item counts** all come from this book's own
catalogue chapters.
