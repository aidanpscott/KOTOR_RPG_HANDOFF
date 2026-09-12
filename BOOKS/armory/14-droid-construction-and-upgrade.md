# Chapter Fourteen — Droid Construction and Upgrade

**Status: DRAFT, for review.** Third of the Armory's four remaining chapters.

---

**Chapter Seven catalogued 135 droid items. Chapter Twelve found five entries on the
crafting bench that were not recipes at all** — a processor, a chassis, a control cluster,
a vocabulator — and said they belonged here.

**This is where they belong.** A droid is the one thing in this book you can build from
nothing, and the one thing that can be upgraded past the ceiling every other character sits
under.

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
with prices attached (`PT-612`):

| Part | File | What it is |
|---|---|---|
| **Chassis Frame** | `hkpart02` | The physical structure. **It decides which chassis the droid is** |
| **Droid Processor** | `hkpart01` | *"A cognitive module or logic processor… without one, a droid could not function"* |
| **Control Cluster** | `hkpart03` | Actuation and coordination. **Without it the droid does not move** |
| **Vocabulator** | `hkpart04` | Speech |

**Three are universal. One decides the chassis.**

**And the Vocabulator quietly closes two rulings made from lore**: a droid's voice module
reads masculine, feminine or neither (`PT-594`) — **this is that component, and it is a part
you buy.** And the `LB-series`, *"a fifth-class drone, no speech center"* (`PT-598`), **is
simply a droid built without one.**

**⚠ There is no Power Cell.** An earlier draft borrowed one from the lightsaber quest;
**the droid quest has no power component and the project declined to invent one**
(`PT-612`).

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

**The source gives the build order, and the project's first draft had it backwards:**

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

**Parts scale by chassis tier** (`PT-608`), and the three-tier shape is the corpus's own —
droid plating already sorts Light, Medium and Heavy with three types each.

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

**An earlier flat 2,800 broke the low end**: against model prices running 350 to 4,200, it
made building a `Marksman-H` **nine times** the cost of buying one. **Tiered, a Marksman-H
costs 900 to build against 350 to buy** — still a bad deal, which is right for a
mass-produced throwaway, **but a bad deal rather than an absurd one.**

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

**⚠ `Droid Master` is a prestige class** and lives in the Advanced Player's Guide, not the
Player's Handbook — see Flag 4.

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

**So a destroyed Assassin droid costs its parts bill to rebuild — not the 6,900 a fresh
build costs.** The expensive part of a droid is its body, and the body is what is left.

**⚠ But every installed upgrade is lost.** Bay installations are permanent **and consumed**
— they do not come out of a wreck. **Socket items are gear and are recovered.**

> **That is the real cost of losing a droid, and it is not the credits.** A nine-bay droid
> at tier-3 socket prices has more value installed than the chassis ever cost.

**A droid PC rebuilds on all three difficulty modes** (`PT-953`); **on `Hard` the bays come
back empty.**

---

# Part Two — Sockets and Bays

**Two systems, not one**, and the owner's ruling is the clearest statement of why:

> *"What we're designing is not a replacement for the stuff that's already there. They're
> different entirely."*

    sockets        ported from KOTOR 2. Gear. Swappable.
    installations  AUTHORED. Permanent. Consumed. The reason to play a droid.

## Sockets — ported

**The source has six slots, not four** (`PT-274`, corrected at `PT-316`):

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

> **A light chassis caps at six bays, permanently.**

**A diagnostic computer and a floating sensor do not accept nine hardpoints** — and the
roster already carried the same fact in three other places, so this reuses an existing gate
rather than inventing a second one.

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

*Sources: `DROID-CONSTRUCTION-01` (`PT-572`, `PT-607`–`PT-613`, `PT-225`, `PT-558`,
`PT-594`, `PT-598`, `PT-599`, `PT-609`, `PT-953`) and `DROIDS-UPGRADE-01` (`PT-274`,
`PT-316`, `PT-323`, `PT-577`, `PT-616`, `PT-654`). `CLASS-ROSTER-01` for the prestige-class
check. `DEATH-AND-DIFFICULTY-01 §5b` for rebuild by difficulty mode.*

## Open items, carried from review

**⚠⚠ Flag 1 — this chapter contradicts Chapter Twelve, and Chapter Twelve has the weaker
source.** `CRAFTING-01` states the `Machinist` *"is the **only class** that can build a
droid — `PT-225`"*, and **Chapter Twelve repeats that.** `DROID-CONSTRUCTION-01 §4` says
otherwise: **Machinist, Droid Master and Engineer may all build**, and explains the
relationship — *"`PT-225` is explicit that construction belongs to the Machinist, and
`PT-572` does not take it away — it **extends** it to the two classes whose premise is
droids."*

**`PT-572` is the later and more specific ruling, and it is the one this chapter follows.**
`CRAFTING-01`'s sentence was true when written and was not updated when `PT-572` extended
it — **`PT-961`'s shape again.**

**✔ Fixed.** Chapter Twelve now reads that the Machinist is **the only class that can build
a droid *for someone else***, and states that `PT-572` extended building itself to
`Droid Master` and `Engineer`. **Both citations were verified against `PT-225`'s own
heading and `DROID-CONSTRUCTION-01`'s reconciling text before the edit.**

**⚠ Flag 2 — `DROID-CONSTRUCTION-01 §6` uses part names that `PT-612` retired.** The
rebuild section reads *"the **Motivator**, **Processor Core** and **Power Cell** are
destroyed"*. But `PT-612` **renamed `Motivator` to `Control Cluster`**, uses **`Droid
Processor`** rather than *Processor Core*, and **withdrew `Power Cell` entirely** — *"the
droid quest has no power component and we should not invent one."*

**So §6 lists a part that no longer exists.** This chapter states the three current parts
instead. **Reported, not fixed.**

**⚠ Flag 3 — and the same section carries a figure from the superseded flat-cost model.**
§6 gives the rebuild cost as **2,800 credits** and *"one day, regardless of chassis"*. But
`PT-608` replaced the flat 2,800 with the tiered ladder — **700 / 1,400 / 2,800.** 2,800 is
now the **heavy-tier** figure only; **rebuilding a Remote should cost 700, not 2,800.**
This chapter states it as *"its parts bill"* rather than repeating the stale number.
**Same edit-lag as Flag 2 and probably the same moment.**

**⚠ Flag 4 — the Armory references a class the Player's Handbook does not contain.**
`Droid Master` appears in this chapter's build permissions and in the bay-grant ladder, and
`CLASS-ROSTER-01` lists it among the **prestige** classes. **`PT-1705` moved prestige
classes to the Advanced Player's Guide**, so a reader of the Armory and the PHB together
will not find it. **Not an error — a cross-book reference that wants a pointer** when Book
Eight exists.

**⚠ Flag 5 — `DROIDS-UPGRADE-01` documents its own staleness and leaves it.** Its closing
paragraph reads: *"`LOOT-01` answered this in the same words as the worry — 'a party with no
droid gets nothing' — **and this paragraph never moved.**"* The document knows the text is
superseded, says so, and keeps it. **Harmless here because the two agree**, but it is the
third instance in two chapters of a rules document carrying a retracted or superseded
passage alongside its replacement.
