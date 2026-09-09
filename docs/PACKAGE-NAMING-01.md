# PACKAGE-NAMING-01 — how things are named and found

**The addressing layer of the package format.** Written against the seven-batch study (`TRACE-81`–`TRACE-89`), which established both what to take and what to avoid.

**⚠ The finding that started this.** KOTOR's `blstrpstol01` is not a naming philosophy. `baseitems.2da` already carries readable labels — `Droid_Computer_Spike_Mount_x`, 28 characters — while its resrefs top out at **15**. A resref *is* a filename inside an archive, and it was capped at 16. **They were not choosing terse names; they were choosing names that fit.** We have no such constraint.

---

## 1 · Three concepts, three words

KOTOR distinguished two of these and collapsed the third into a global string table. **All three are separate here.**

| Word | Is | Changes | Example |
|---|---|---|---|
| **`path`** | identity of a **definition** — and where it lives | rarely | `items/weapons/echani-vibroblade` |
| **`tag`** | identity of a **placed instance** | never | `dock-guard-02` |
| **`name`** | what a **player reads** | freely | *"Echani Vibroblade"* |
| **`role`** | a slot an author writes against — **`PT-1331`** | **refillable** | *the town guard* |

**Why `path` rather than "handle":** it *is* a path, so the word needs no explaining — and it makes identity and location **the same thing**, which is where findability comes from for free.

**Why `tag`:** short, familiar, and it matches the source's own vocabulary for exactly this concept (`TRACE-86`: quests are tag-addressed; `TRACE-83`: instances carry a template reference). **⚠ One caution — most tagging systems are many-to-one. Ours is one-to-one.** A tag names one placed thing.

---

## 2 · Path shape

```
items/weapons/echani-vibroblade
items/armor/czerka-vest
areas/a01-endar-spire
```

**Lowercase. Hyphens. No numbers** — except areas, `§4`.

**Hyphens over underscores** for one concrete reason: a hyphen survives being a filename, a URL **and a spoken word**. *"blaster-dash-pistol"* reads aloud; *"blaster underscore pistol"* does not. It also does not need the shift key, which matters at volume.

### ⚠ Two levels, and nothing tunable in the path

**The path says what a thing IS. Not what it is worth.**

An earlier sketch went `items/armor/chest/light/` — but **weight class is a stat that gets tuned.** Move an item from light to medium during balancing and you have moved the file and broken every reference to it.

**So: `slot` and `weight` are fields. `items/armor/` is the path.**

**The Builder can display four levels of grouping** — by slot, then weight, sorted by cost, filtered by faction. **A view costs nothing and breaks nothing.** `TRACE-88` found KOTOR conflating these; we do not have to.

**⚠ Two levels is now EVIDENCED, not a judgement — `TRACE-90`.** A census of every item in both games mapped their readable labels onto two-level paths: **4,178 items in K1 and 5,000 in K2, with ZERO collisions.** Flattened to a *single* level it is still only 6 collisions in K1 and 0 in K2. **Two levels has margin.**

**And the volume is far lower than the totals suggest**, because the distribution is extremely lopsided: **weapons are 12% of items, not 40%.** `items/weapons/` holds ~500 files in a game the size of K1 — browsable. **The fear of a wall of four thousand files was unfounded.**

**⚠ BUT THE CENSUS FOUND THE REAL RISK, AND IT IS NOT DEPTH — IT IS THE CATCH-ALL.** BioWare's own prefix `g_` (generic) covers **55.9% of prefixed items in K1.** *Over half their catalogue lives under "unclassified."*

**So `misc/` must not exist as a default.** If the Builder offers it, it becomes the path of least resistance and swallows the catalogue exactly as `g_` did. **Either it does not exist, or choosing it is a deliberate act the Builder makes slightly awkward.**

---

## 3 · ⚠ Path is identity — and the file knows its own path

> **⚠ A LOG RECORDS THE `id`, NEVER THE NAME — `PT-1445`.** Four app tests expect `packageName` (*"Endar Spire"*) where `hub.dart` logs `packageId` (`endar-spire`). **`hub.dart` is right and the tests are wrong.**
>
> **A name is what a player reads and it CHANGES.** An id is **derived and stable.** A log entry is **permanent** (`PT-1418`) — **so a permanent record carrying a mutable display string goes stale the first time somebody renames a package**, and nothing would catch it because the string was valid when written.
>
> **⚠ And `SaveStore.listFor` already carries a both-ways concession for saves written before the change.** That is a migration allowance, not a second opinion — **it reads both and writes one.**

**Moving a file changes its identity.** That is the cost of making location and identity the same thing, and it is accepted deliberately.

**Three safeguards:**

1. **In the Builder, a move is one operation.** It knows every reference and rewrites them together.
2. **Every file carries its own path as a field.** A hand-moved file is **self-describing** — the app reads it and can say *"this file says it belongs at X and is sitting at Y"* rather than guessing.
3. **A broken reference fails loudly**, naming the reference and the likely new location.

**⚠ Why loud failure is a rule and not a preference.** The study's `F35`: **KOTOR's engine wrote an appearance index past the end of the table it indexes, and nothing rejected the write.** A silent bad reference is worse than a loud broken one — and **we are inviting modders into the raw folder**, so the format must tell them immediately when something is broken rather than degrading quietly.

**And the mitigation is structural:** if the path encodes only what a thing **is**, moves are rare by construction. Retuning, rebalancing and reclassifying by weight never touch it.

---

## 4 · Areas are numbered. Nothing else is.

```
areas/a01-endar-spire
areas/a02-taris-hideout
```

**⚠ This is a deliberate exception to `§2`, and it is the one seam in this document.**

**Why areas get it:** a campaign's areas have a **canonical play order** that rarely changes, there are few enough that renumbering is survivable, and **modders read raw folders** — where alphabetical order is useless and play order is what you want.

**Why nothing else does:** there is no first vibroblade. A number on an item is `blstrpstol01` wearing better punctuation.

**⚠ The cost is real and is accepted:** a number in a name is position-as-identity, which the study found fatal five separate times — most vividly in K2 shipping a class literally labelled `BountyHunter(CUT!!!)` because deleting the row would renumber the world.

**So: inserting an area between `a01` and `a02` gets `a03`, out of numeric sequence, and the manifest carries the real order.** Renumbering is permitted only as a Builder operation that rewrites references, never by hand.

**⚠ Do not "tidy up" by numbering items later.** This exception is load-bearing and narrow.

---

## 5 · No auto-numbered duplicates

**The Builder refuses `echani-vibroblade(02)` and asks for a real name.**

`vibroblade(01)` and `vibroblade(02)` **is `blstrpstol01` with nicer punctuation** — six months on, nobody knows which is which without opening both.

**A second thing needing the same name is a signal the first was named badly.** One moment of friction prevents a permanent ambiguity.

---

## 5a · ⚠ Four name shapes the Builder must refuse — `TRACE-90`

**The census sampled BioWare's real labels. Most are exactly what we want** — `Quarter_Staff`, `Vibro_Double_Blade`, `Jedi_Robe`, `Ghaffi_Stick`. **Those map straight onto `items/weapons/quarter-staff`.**

**But four failure shapes ship in the same table, and each has a rule already:**

| Real label | Why it fails | Rule it breaks |
|---|---|---|
| `Armor_Class_8` | **a stat in the name** — rebalance it and the name lies | `§2` nothing tunable in the path |
| `Implant_2` | **a bare number** — carries no meaning | `§5` no auto-numbering |
| `Plot_Useable_Items` | **a category posing as an item** | `§2` the path says what a thing *is* |
| `Droid_Sonic_Sensors_x` | **a trailing disambiguator** — someone needed a second one and appended a character | `§5` no auto-numbering |

**⚠ `Armor_Class_8` is the instructive one.** It is `items/armor/chest/light/` in miniature — **a tunable value baked into an identifier** — and BioWare shipped it. Change the item's class and either the name is wrong or every reference breaks.

**⚠ And this sharpens `TRACE-90`'s own caveat rather than softening it.** The collision test came back clean partly *because* a meaningful slice of their labels are not names at all — numbers, categories and disambiguators **do not collide, because nothing else would ever be called `Implant_2`.** The scheme survives real content; the Builder is what keeps the content worth the scheme.

---

## 6 · Scoping — relative paths, declared dependencies

**A path is relative to its package.** `items/weapons/echani-vibroblade` means *this package's* vibroblade, so **two campaigns can both have one** without collision.

**To reference another package's content, declare the dependency first.** That is `TRACE-89`'s central mechanism, and it is the thing KOTOR removed:

> **A module declares what it needs, by name, in its manifest. Nothing is discovered by scanning a folder.**

**⚠ `TRACE-82` found KOTOR has NO module-local rules table — not one, in either game.** Every archive under `modules/` in both games searched; zero. **A campaign could not say "in my content this weapon hits harder" without changing it for every campaign installed.** Package-relative paths are the fix.

---

## 7 · What is deliberately NOT here

**⚠ No per-file KOTOR export metadata.** A `kotor_baseitem` field on every item, for an exporter declined at `PT-1269`, is how dead capabilities are born. **The study found four** — `racialtypes.2da`'s adjust columns (every value zero, both games), `LawfulChaotic` (on blueprints, dropped from live records), `Mod_CutSceneList` (declared on every module, length 0 in all 239), and unvalidated `SkillList` slots past eight.

**If a mapping is ever wanted, it belongs in one table** — the study already produced `NAMING.md` doing exactly that. **A table can be validated as a unit and deleted cleanly. Metadata on a thousand files cannot.**

---

## 8 · Open

- ~~Path depth~~ **Closed at `TRACE-90`: two levels, evidenced.** Zero collisions across 9,178 real items in both games.
- **⚠ `misc/` — whether it exists at all.** The census found BioWare's catch-all absorbing **55.9%** of their items. **If it exists, it must not be the easy choice.**
- **Whether `tag` is required on every instance or only on referenced ones.**
- **Reserved path segments** — whether `misc/` exists, and what goes in it.
- **Case and character rules** beyond lowercase-and-hyphens — length limits, permitted punctuation, unicode.
