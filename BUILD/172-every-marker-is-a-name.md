# BUILD 172 — every marker in Armory Seven is a name, and Scan is blocked

---

## 1 · ⚠⚠ `PT-1853` — THE OTHER 22 ROWS RESOLVED, FROM THE TABLE THE DATA NAMES

`itempropdef` carries a **`subtyperesref`** column saying which 2DA each
property's subtype indexes. `PT-313` already derived the engine's property
vocabulary from that column; **this is the same column answering the same
question one document over.** Nothing was matched to a vocabulary by hand.

    8 saving throws · 10 character-locks · 4 racial subtypes · 1 Defence type
    → zero unresolved rows left in the chapter

**⚠⚠ A SUBTYPE COLLIDES ACROSS VOCABULARIES, AND THE MARGIN SEPARATES THEM.**
`Droid Energized Armor Mark II` carries `DamageResist` **and**
`ImprovedSavingThrowsSpecific` **both at subtype 1** — so *"whatever this item
calls 1"* is two answers, and the first pass **refused all three such rows,
correctly.** The margin names `iprp_savingthrow`; requiring a property that
indexes *that* table resolves it, and the blueprint must still carry one —
**so the margin is checked rather than believed.** Using both is stronger than
either alone.

**⚠ AND THE CHARACTER-LOCKS NAME THE DROIDS YOU WOULD EXPECT** — `G0-T0`,
`HK-47`, `T3-M4` — on a page of droid equipment, from `iprp_pc`, which nothing
told the resolver to look for. `d_g0t0_01` resolving to `G0-T0` is the mapping
**confirming itself against the resref.**

**⚠ ONE LABEL WAS A RAW ENUM TOKEN PROSE CANNOT CARRY.** The chapter renders a
clean label verbatim — `Ability (Dexterity)` — and `AC_Armor` inside a row that
already reads *"Defence penalty −3"* is the game's token in the book's own
vocabulary. **The row was already translating AC to Defence**; `(armour)`
finishes that translation rather than starting a new one.

⚠ A blank label is not an answer: `racialtypes` rows 0–4 are empty in **both**
games, and a row indexing one would be refused.

## 2 · ⚠ AND THE OTHER THREE CHAPTERS CARRY 248 MORE — NOT APPLIED

    Five  29 · Six  51 · Eight 168   (+32 needing the margin filter)

The same method resolves them. **Not done:** that is a sweep across AUTHOR's
book rather than the chapter that was assigned, and it is the owner's call.

## 3 · ⚠⚠ `Scan` IS BLOCKED, AND A FEAT IS WHAT BLOCKS IT

`ACTION-ECONOMY-01 §1`: *"**Scan** — an Awareness or Alertness check to find
what you have missed."* It is the obvious next Action: `PT-1550` lets an author
hide a creature and **the only way to find one today is to walk into it.**

But `FEATS-LIBRARY-01` has **Vigil**, at 1st level:

> *"You may `Scan` as a free action once per round, **and you use the better of
> `Awareness` or `Alertness` for it**."*

**So an unfeated Scan does NOT use the better of both** — otherwise half of a
1st-level feat is worth nothing. Which one it uses, or whether the player
chooses, **no document states.**

⚠ And the contrast makes it sharper rather than an oversight:
`SKILL-RESOLUTION-01 §4` says a creature **resisting** a Hide *does* roll the
better of the two. Passive noticing takes whichever sense serves; an active
Scan apparently commits to one. That reads deliberate — and the commitment is
unspecified.

**Building it either way sets a feat's value by fiat.** Named, not built.

---

## Tests

Unchanged — this slice is data and a blocked build. App 595 · Lodestar 734.

## Still open

- **`Scan`'s default sense** — a ruling.
- **248 markers** in `Armory` Five, Six and Eight.
- **A real target picker**, before power effects resolve — `PT-1847`.
- `§2`'s character screen (the click, `PT-1443`'s) · `Slice`, `Treat`, `Repair`
  unbuilt · the stealth field generator has no item.
- ⚠ The suite is flaky under load — `BUILD 167`.
