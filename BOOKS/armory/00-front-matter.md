# Armory — Front Matter

**Status: per `PT-1813`.** The three required elements. **The disclaimer is reproduced word
for word and must not be edited, paraphrased, shortened, or reformatted in any way that
changes its wording.**

---

## Disclaimer

> This is an unofficial, non-commercial fan project. It is not affiliated with, endorsed
> by, or produced by Lucasfilm Ltd., Disney, BioWare, or any rights holder of Star Wars or
> Knights of the Old Republic. All Star Wars trademarks, characters, and copyrighted
> material referenced herein remain the property of their respective owners. This work is
> created by fans, for fans, and is distributed free of charge. No part of it is sold, and
> no revenue is generated from it in any form.

**Placement: page two or three, before any content** (`PT-1813`).

---

## [INSERT PERSONAL NOTE HERE]

**⚠ Deliberately empty. This is the owner's own acknowledgment, in his own voice, and is
not to be drafted by anyone else.** The placeholder stays exactly as it is until he fills
it.

---

# Sources and Credits

**Scoped to what this book actually used.** Every entry carries one of **three**
confidence levels, and they are deliberately not blended:

| Mark | Meaning |
|---|---|
| **✔ verified** | Read directly from a source held on this machine |
| **◆ relayed** | Externally researched by MAIN against a live search and corroborated across multiple independent sources — **not** read from anything held here |
| **⚠ unverified** | General knowledge or assumption. Confirm before publication |

**The middle tier exists because collapsing it into either neighbour would be a lie.**
Relayed credits are far stronger than assumption and are not the same thing as having read
the source — the same discipline the Galactic Timeline applies to its three relayed
deep-history claims.

**✔ This list covers all sixteen chapters.** Refreshed after Chapters Twelve through
Sixteen were drafted; Chapter Three's family catalogue is complete at 122 items.

---

## The one thing this book owes most

**This book is a catalogue of other people's design work, and that should be said plainly
before anything else.**

Almost every number in the Armory — every weapon's dice, every armour's bonus, every
upgrade's effect, every price — **was designed by the teams who built the two games and
was read out of their own data files.** This book converts, organises, reconciles and
occasionally corrects those values. **It did not invent them.**

Where this project *has* invented something — the Training Lightsaber, the Sniper Rifle's
catalogue row, a handful of prices — **it is marked `⚠ AUTHORED` in place** and is not
passed off as extracted (`PT-1352`). **That tagging exists precisely so this credit stays
honest**, and a reader can tell at a glance which values are BioWare's or Obsidian's and
which are ours.

---

## Primary sources

### *Star Wars: Knights of the Old Republic* (2003)

**BioWare**, published by **LucasArts.**

**✔ BioWare's authorship is verified** from this project's own corpus, which quotes the
studio's internal developer comments out of the game's `.uti` files directly. **That is the
only credit on this page read from something held here.**

**◆ The following are relayed** — researched externally and corroborated across multiple
independent sources, not read from any held source:

| Role | Credited |
|---|---|
| **Director · Producer · Project Director** | **Casey Hudson** |
| **Executive Producers** | Raymond Muzyka, Greg Zeschuk |
| **Lead Designer** | **James Ohlen** |
| **Assistant Lead Designer** | Preston Watamaniuk |
| **Senior Writer** | **Drew Karpyshyn** |
| **Art Director** | Derek Watts |
| **Composer** | Jeremy Soule |
| **Core Game Design** | David Falkner, Steven Gilmour, Casey Hudson, Drew Karpyshyn, James Ohlen, Preston Watamaniuk, Derek Watts |
| **Designers** | Jason Booth, David Gaider, Lukas Kristjanson, Cori May, Andrew Nobbs, Brad Prince, Aidan Scanlan, Peter Thomas, John Winski |

### *Star Wars: Knights of the Old Republic II — The Sith Lords* (2004)

**Obsidian Entertainment**, published by **LucasArts.**

**◆ Relayed**, on the same basis. The corpus reads this game's data extensively but never
names its developer, publisher or staff:

| Role | Credited |
|---|---|
| **Lead Designer · Lead Writer** | **Chris Avellone** — wrote the overall storyline and most of the companions directly, **including Kreia** |
| **Producer** | Chris Parker |
| **Composer** | Mark Griskey |
| **Additional design and writing** | Ferret Baudoin, Michael Chu |

**⚠ Both lists are the core credits, not the full ones.** Each game was built by teams far
larger than the names above — programmers, artists, QA, audio, localisation — and a
complete credit roll is owed before publication. **What is here is a real start rather than
a studio name standing in for a hundred people.**

### The game data itself — **✔ verified, read directly**

The following files are the Armory's actual source of record, read from the extracted game
data rather than from any secondary description:

| File | Used for |
|---|---|
| `baseitems.2da`, `k1_baseitems.2da`, `k2_baseitems.2da` | Every base weapon and armour row — dice, threat range, wield class, size |
| `iprp_acmodtype.2da` | The armour-bonus property mapping behind Chapter One's Defence table |
| `.uti` item files | Individual item properties, names and descriptions across the catalogue chapters |
| `k2_itemcreate.2da` · `k2_chemicalcreate.2da` · `k2_upgrade.2da` | Chapter Twelve's crafting recipes and their DC ladder, ported unchanged |
| `k2_itemcreatemira.2da` | Named in Chapter Twelve as **deliberately deferred** — companion content |
| `hkpart01`–`hkpart05` | Chapter Twelve identified them as not-recipes; Chapter Fourteen builds droids from them |
| `a_give_treas` | Chapter Thirteen's loot bands — **constants read, control flow not disassembled** |
| `k2_swoopupgrade.2da` | The upgrade grammar Chapters Fifteen and Sixteen build ship parts on |
| `keymap.2da` | Chapter Fifteen's evidence for how little space combat the source had — two verbs |

**⚠ Two of these were read incompletely and both chapters say so.** `a_give_treas` gave up
its constants but not its control flow, so **which loot band draws from which list is an
inference** (Chapter Thirteen, Flag 1). And `k2_baseitems.2da` needs the project's own
binary-2DA parser rather than a text read — a fact found the hard way while checking
Chapter Three's ranged dice.

**These are BioWare's and Obsidian's design data.** Reading them is what let this book
correct several values that secondary sources had wrong — the K1 Lightsaber's `2d8`, the
Vibrosword's `1d12`, the `Hold Out Blaster`'s unhyphenated name — **and every one of those
corrections is a case of going back to the original designers' own numbers rather than
improving on them.**

---

## Not used in this book

**Recorded so a reader does not assume otherwise: the Armory cites no published rulebook
at any point.** No *Revised Core Rulebook*, no *Ultimate Alien Anthology*, no Saga Edition
material, no KOTOR Campaign Guide. **Verified by search across all sixteen chapters — zero
occurrences.**

**Chapters Fifteen and Sixteen do draw on out-of-game reference material** for the ship
roster and the faction navies — hull names, service dates and doctrine, sourced through the
project's own `STARSHIPS-01` and `SPACE-COMBAT-01` rather than read here directly. **Those
documents cite a Legends wiki index**, which sits at the bottom of this project's source
ladder and is **⚠ unverified from anything held on this machine.**

**That is a real finding about this book's character rather than an omission.** The Galactic
Timeline rests almost entirely on a published sourcebook; the Armory rests almost entirely
on game data. **They are different kinds of book and their credit pages should not look
alike.**

---

## This project's own documents

**Not third-party sources and not listed for credit** — recorded so the chapters' citations
resolve: `EQUIPMENT-01`, `ITEMS-01`–`ITEMS-09`, `STARTING-EQUIPMENT-01`,
`ACTION-ECONOMY-01`, `ATTACKS-01`, `WEAPON-MATRIX-01`, `CRAFTING-01`, `LOOT-01`,
`DROID-CONSTRUCTION-01`, `DROIDS-UPGRADE-01`, `STARSHIPS-01`, `SPACE-COMBAT-01`,
`MOUNTED-COMBAT-01`, `SKILL-RESOLUTION-01`, `REST-AND-MEDITATION-01`, `CLASS-ROSTER-01`,
and the playtest ruling ledger. **The project's own
rulings govern this book over any source above where the two disagree.**

---

## ⚠ Before this book is published anywhere

**✔ Only the data files and BioWare's authorship are read from something held here.
Everything else on this page is ◆ relayed** — strong, corroborated, and still not the same
as having read it.

**The gap that mattered most is now substantially closed.** This page previously credited
two studios by name alone for a book whose content is overwhelmingly their teams' work.
**It now names the people**, and that was the highest-priority item on it.

**What remains owed:** the **full** credit rolls. The lists above are core credits — the
programmers, artists, QA, audio and localisation staff who also built this material are not
on them, and a complete roll should be taken from the games themselves before publication.
**Still the highest-priority item on this page, above every factual flag in the eleven
chapters** — but it is now a matter of completing a real list rather than starting one.
