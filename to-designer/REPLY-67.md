# REPLY-67 — Force powers mapped and rebalanced. Four new scenarios. Something for you.

---

## `PT-251` — ⚠ the K2 data was in holdings the whole time

**`force_power_extract.tsv` — 247 rows, both games, cut content already flagged.**

    against K1's spells.2da alone    38 of 88
    against the TSV                  ⚠ 86 of 88

**⚠ `PT-250` asked the owner for `k2_spells.2da`. The contents were already here in a better form.**

---

## `PT-249` and `PT-252` — two hard negatives on the numbers

**`spells.2da` carries cost, range, immunity, prerequisites and class access.** **It does NOT carry damage, duration, save DC or magnitude** — **those are in a compiled script.**

**⚠ And the wiki text is not evidence of the game's behaviour.** **Obsidian's own forums record `Affliction` and `Plague` as improperly coded — the delivered penalties are far smaller than the menu text describes.**

> **⚠ Same shape as `Logic Upgrade` — `PT-210`. A description that promises what the code does not deliver.**

**So every number needs provenance:**

    source_system: kotor_game    the 2DA carried it
    source: wiki_description     the menu text says so
    ⚠ source: wiki_observed      someone measured it in play
    authored                     neither had it

---

## `PT-253` — the ported numbers do not balance, and the cause is structural

**Against `Barrage` at `27.3` a round:**

    Force Push @30      1.10x Barrage   ⚠ exceeds it
    Force Wave @30      1.65x Barrage   ⚠ and it is an area
    Whirlwind @30       1.10x Barrage   ⚠ and the target cannot act

**KOTOR's cap is 20; ours is 30.** **⚠ And in KOTOR a Jedi could cast *and* swing.**

### Rule 1 is your own argument at a different layer

> **Level-scaling powers scale on FORCE levels, not character levels.**

**⚠ Which is `PT-102`'s pool rule, and it does at the Force layer what `PT-239` did for class features.**

    pure Jedi 30            30 dmg   1.10x
    Soldier 24 / Jedi 6      6 dmg   0.22x

**Rules 2–4: seconds convert at 6 a round · per-tick damage becomes per-round · every distance snaps to the grid.**

---

## `PT-254` — ⚠ S1–S8 test nothing the class workstream ruled

**No forms, no unarmed chains, no prestige, no multiclass, no area powers on a grid.**

**Five pregens and four scenarios added. `S9 The Hangar` is 20 by 14.**

> **⚠ `PT-170` derived that the old 5-wide corridor meant the range increment ladder never fired once across eight scenarios.** **A whole subsystem written and never tested, because no map was large enough.**

---

# ⚠ Something for you, and it is in your lane

**Two powers in `FORCE-POWERS-01` return nothing on either wiki:**

    Force Distraction
    Force Strangle

**They are either our names for a source power or authored entries nobody marked.**

**⚠ And there is a third thing to check while you are there:** **`Force Deflection` and `Force Redirection` are a chain in the source — level 6 then level 12, the second adding *bolts go back at the enemy*.**

**Our roster has them as two separate powers.**

**⚠ Check whether any other pair in the 88 is a source chain we flattened.** **`prerequisites` in the TSV names 18 parent-child links and I have not walked all of them against our list.**

**That is the same shape as the `Sneak Attack` ladder: a source structure we ported as loose items.**
