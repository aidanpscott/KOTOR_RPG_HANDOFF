# STUDY 23 — the dying band, and what a dead creature leaves behind

**KOTOR 1 and 2 read with `STUDY 19`'s readers; BG3 as contrast. Files only.
The games were not launched.**

---

## 1 · ⚠⚠ KOTOR HAS NO DYING BAND. NOT ONE CREATURE EVER OCCUPIED IT.

> The owner: *"Does an enemy have a dying state at all, or does it die at 0? Is
> the bleed-out rule a party rule there too? `PT-559` is ours and it was read
> FROM the games — find out whether their creatures ever occupied that band."*

### The negative, and it is scoped

`nwscript.nss` is KOTOR's whole scripting surface — **216,650 bytes, the
complete API.**

| token | K1 `nwscript.nss` | NWN `nwscript.nss` |
|---|---|---|
| `DYING` | **0** | 1 — `EVENT_SCRIPT_MODULE_ON_PLAYER_DYING = 3010` |
| `BLEED` | **0** | **0** |
| `Min1HP` / `MinOneHP` | 0 as a constant | 0 |

**`GetIsDead(object)` returns an `int`. There is no `GetIsDying`, no
`GetIsBleeding`, no dying event, and no negative-HP band anywhere in the API.**

⚠ **The control matters:** NWN keeps one hook — a module event for a **player**
dying. **KOTOR removed even that.** So this is not "BioWare never modelled
bleed-out"; it is **KOTOR deliberately dropping the one hook its own ancestor
kept.** `TRACE-107`'s pattern again.

### What KOTOR has instead — three authored flags on the blueprint

A `.utc` carries 68 fields. Three of them govern death:

| field | what it does |
|---|---|
| **`Min1HP`** | cannot be reduced below 1 HP |
| **`Plot`** | plot-protected |
| **`NoPermDeath`** | dies, but not permanently |

**Surveyed across every creature blueprint in both games:**

| | K1 (205) | K2 (284) |
|---|---|---|
| `Min1HP = 1` | **1** | **1** |
| `Plot = 1` | **0** | **0** |
| `NoPermDeath = 1` | **17** | **35** |

### ⚠⚠ And `NoPermDeath` is *literally* the party rule

The 17 in K1, named:

```
p_bastilla  p_carth  p_mission  p_zaalbar  p_cand
p_jolee     p_juhani p_t3m4     p_hk47                ← ALL NINE recruitable party members
g_davink  g_jagi  g_jordo  g_lena  g_malare
g_tuskenmale01  g_tuskenmale02  g_xor                 ← 8 plot NPCs
```

**Every recruitable companion carries it. No enemy does.** And the single
`Min1HP` creature in K1 is **`g_xor`** — a plot confrontation who must survive to
finish talking.

> **⚠ ANSWER: an enemy in KOTOR dies at 0. There is no band. The
> "doesn't-stay-dead" property is an authored per-creature flag, and it belongs
> to the party — exactly as the owner suspected, and now counted rather than
> assumed.**

**`PT-559`'s bleed-out band is ours. KOTOR's creatures never occupied it, because
it does not exist in their engine.**

### PT-1496

1. **What did they do?** Binary alive/dead for everyone, plus three authored
   exceptions — never below 1, plot-immune, or dies-but-comes-back — with the
   third given to all nine companions.
2. **Why?** KOTOR is real-time-with-pause with a party of three. A bleed-out band
   needs a timer the player can act against; in RTwP there is no turn in which to
   act, so the band would be either invisible or unfair. **Making it a per-actor
   flag instead moves the decision from the clock to the author.**
3. **Does the reason still hold for us?** ⚠ **No — and this is the divergence.**
   We are turn-based on a grid, so a band *is* actionable: there are turns in
   which to reach someone. **The reason KOTOR had no band is the reason we can
   have one.** But note what KOTOR proves: **a band is not required to feel like
   KOTOR.** The anchor does without it entirely.
4. **What is the modern form?** **If a creature can be down-not-dead, that must be
   an authored property of the creature, not a universal rule** — KOTOR's answer,
   and it is the one that survives. `NoPermDeath` is the shape: a blueprint field,
   defaulting to off, that the author sets on the few who deserve it. ⚠ **And it
   names the live defect directly** — a dying enemy nothing ticks out of combat is
   a *universal* band applied where KOTOR applied a *flag to nine characters*.

---

## 2 · ⚠⚠ A KOTOR CORPSE IS THE CREATURE ITSELF

> The owner: *"Is a corpse a placeable, a state on the creature, or something
> else? That answer decides whether our 'nothing' is a limitation or a different
> design."*

### The mechanism, in BioWare's own words

`k_def_spawndead.nss`, shipped, entire:

```c
void main()
{
    SetIsDestroyable(FALSE,FALSE,FALSE);
    ApplyEffectToObject(DURATION_TYPE_INSTANT,EffectDeath(),OBJECT_SELF);
}
```

And the API comment in `nwscript.nss`:

```
// 323: Set the destroyable status of the caller.
// - bDestroyable: If this is FALSE, the caller does not fade out on death, but
//   sticks around as a corpse.
// - bRaiseable: If this is TRUE, the caller can be raised via resurrection.
// - bSelectableWhenDead: If this is TRUE, the caller is selectable after death.
void SetIsDestroyable(int bDestroyable, int bRaiseable=TRUE, int bSelectableWhenDead=FALSE);
```

> **⚠ THE CORPSE IS NOT A NEW OBJECT. It is the same creature, not removed.**
> Its inventory is its inventory; looting it is looting the creature. Whether you
> can click it is a third, separate flag.

### The other half — `bodybag.2da`, and it ships unused

There is a second path, for when a creature *is* destroyed. `bodybag.2da`,
**byte-identical in K1 and K2** — 10 rows:

| # | label | appearance → `placeables.2da` | `corpse` |
|---|---|---|---|
| 0 | default | *(blank)* | 0 |
| 1–7 | Backpack · Equipment_Pack · Bag_and_Strap · Metal_Case · Pile_of_Cloth · Pouch · Tuskan_Rag_Pile | 3, 33, 140, 138, 139, 137, 178 | 0 |
| 8–9 | **RancorCorpse · KraytCorpse** | 217, 218 | **1** |

The `name` column is strref **38151 = `Remains`** for every row — ⚠ **every body
in KOTOR is called the same thing.** The appearances resolve to real models
(`PLC_Backpack`, `PLC_Bag01–04`, `PLC_bodyRanc`, `PLC_bodyKray`), and the
`corpse` flag separates *a dropped container* from *an actual body*.

**A `.utc` carries a `BodyBag` field selecting the row.**

### ⚠⚠ CONTROL — and it changed the conclusion

`BodyBag` non-zero came back **0 of 205** in K1's palette. **Zero across a table
with nine populated rows is exactly the result that is too neat**, so it was
re-derived against a second, independent population: **274 module archives**.

| population | creatures | `BodyBag ≠ 0` |
|---|---|---|
| `chitin.key` palette, K1 | 205 | **0** |
| `chitin.key` palette, K2 | 284 | **0** |
| K1 module archives (274 files) | **2,451** | **0** |

**2,940 creatures. Not one selects a body bag.**

And the corpse *placeables* were checked too — **2,177 type-2044 objects across
every K1 module**. The body-bag appearances that appear are **hand-authored set
dressing**: 25 backpacks, 10 equipment packs, 2 pouches, 2 cases, 3 rag piles —
named `backpack001`, `lev40_bandoleer`, `ldr_case`, `tat20_ragpile`. **Appearances
217 and 218 — RancorCorpse and KraytCorpse — have ZERO placed instances.**

> **So the placeable path exists in data and is not used. The state-on-the-creature
> path is the one KOTOR actually ships.**

### PT-1496

1. **What did they do?** Left the creature in the world. `SetIsDestroyable(FALSE)`
   stops the fade; the body *is* the object; its inventory *is* the loot. A
   parallel placeable mechanism was built, given nine rows and a per-creature
   field, and then used by nothing.
2. **Why?** Because it costs nothing. The creature already exists, already has an
   inventory, already has a position. **Spawning a container means creating an
   object, transferring items, and choosing an appearance** — three operations
   and a table — to reach a state you already had by *not deleting something*.
   The unused table is the evidence: they built the expensive path and then took
   the free one.
3. **Does the reason still hold for us?** ⚠⚠ **This is the answer to the owner's
   real question, and it reframes it.** `Coder` ruled our dead leave nothing
   *"as a consequence rather than a choice: no corpse tile type, `[[contents]]`
   is authored, and the engine may not edit a package."* **But KOTOR's corpse
   needs none of those three things.** It needs no tile type — the body is where
   the creature was standing. It needs no `[[contents]]` edit — the inventory is
   already on the combatant. It needs no package write — **the creature is
   runtime state, and `PLAY-STATE-01` is already a projection over the log.**
   **The three blockers are blockers for the PLACEABLE path, which is the one
   KOTOR abandoned.**
4. **What is the modern form?** **Do not remove the dead combatant.** Mark it
   dead and leave it on its square, with its equipment still attached — which is
   `PT-1452`'s `[equipment]` chain already built. **A corpse is a state on a
   combatant, not a new object**, and it is a projection question rather than a
   format one. ⚠ **And take `bSelectableWhenDead` with it**: whether a dead thing
   can be clicked is a *separate* decision from whether it is drawn, and KOTOR
   made it a third argument rather than an implication.

⚠ **So: our "nothing" is a limitation, not a different design — but the
limitation is not the one that was recorded.** The blockers named are real for
spawning a container and irrelevant to leaving a body.

---

## 3 · BG3 — the contrast, and it has the band KOTOR lacks

Cheap, from the stats already extracted at `STUDY 19`.

**`DOWNED` is a first-class `StatusType`** — one of ten, alongside `BOOST` (897),
`INCAPACITATED` (19), `KNOCKED_DOWN` (11). And the transition is explicit:

```
data "SpellSuccess" "RemoveStatus(DOWNED); ApplyStatus(DYING,100,-1,DoT)"
```

**Two statuses, not one.** `DOWNED` → `DYING`, the latter applied as a
**damage-over-time with duration `-1`** — an unbounded bleed that something must
interrupt. Both sit under **`SG_Incapacitated`** (39 references), the same
status-group mechanism `STUDY 19` found for `SG_DifficultTerrain`.

The four `DOWNED` entries in `Shared.pak` are all *cheat-death* effects —
`DEATH_WARD_DOWNED`, `RELENTLESS_ENDURANCE_DOWNED`, `RELENTLESS_RAGE_DOWNED`,
`STEEL_WATCHER_INVULNERABILITY` — each carrying
`OnApplyFunctors "RemoveStatus(X);RegainHitPoints(1,Guaranteed)"`. ⚠ **That is
`Min1HP` rebuilt as a status**: KOTOR's blueprint boolean is BG3's composable,
removable effect.

⚠ **Not checked:** the *base* `DOWNED`/`DYING` definitions for an ordinary
character are **not in `Shared.pak`** — searched all 68 extracted stat files. They
are engine-side or in a pak not opened.

**Three answers to one question:** NWN keeps a player-only dying hook; **KOTOR
deletes the band and gives nine characters a flag**; BG3 restores the band as two
composable statuses with an unbounded DoT.

---

## 4 · The active roll, in words — `PT-1326`

Carried over from `STUDY 22`. All 20 handles in `ActiveRoll.xaml`, resolved:

```
Available Bonuses · Add Bonus · Total Bonus · Situational
Proficiency · Expertise · Advantage · x1
<hl>Click</hl> dice to roll
Use Inspiration · Roll Again · Try Again · Continue · Cancel
Choose Die Design · Customise Dice
Uses 1 Thieves' Tools
Waiting for <hl>[1]</hl> to roll
Waiting for <hl>[1]</hl> to re-roll or continue...
Waiting for <hl>[1]</hl> to continue...
```

**Three things worth having:**

* ⚠⚠ **`<hl>Click</hl> dice to roll` — the roll does not happen. The player
  makes it happen.** That is the floor of *ceremony proportional to agency*: an
  active check is not merely *shown* to you, it **waits for you**. `STUDY 21`
  measured 152 keyframes; this is the reason they are affordable — the player
  asked for them.
* **`Available Bonuses` / `Total Bonus` / `Situational`** — the modifier list is
  headed, categorised and **summed on screen**. `PT-1326` requires the line carry
  its derivation; this is that derivation with a title.
* ⚠ **`Uses 1 Thieves' Tools`** — the cost-in-words phrasing, and it complements
  `STUDY 22`'s `FooterCosts`. **`Uses <n> <thing>`**, not `Cost: 1`.

**`<hl>…</hl>` is a second inline markup tag** beside `<LSTag>` — this one for
emphasis rather than lookup.

⚠ **`CombatLog.xaml` carries only two strings — `Combat Log` and `Latest`.** The
log's entry text is **assembled by code from other strings**, so **how a BG3
combat-log line actually reads is still unanswered**, and it is still the closest
analogue to our working line.

---

## 5 · A correction to `STUDY 19`

⚠ **`STUDY 19`'s container histogram mislabelled two resource types.**
`nwscript` is type **2009**, so **2009 is `.nss` and 2010 is `.ncs`** — the table
in `keybif.py` had 2009 as `utc` and 2010 as `nss`, and **2027 is `.utc`**.
`STUDY 19 §0`'s "utc 1,774 / nss 1,784" for K1 should read "**nss 1,774 / ncs
1,784**".

**Incidental, not load-bearing:** the histogram was context, and no finding in
`STUDY 19` rests on it. **But it is the third wrong-directory error in this
series and it is worth the entry** — the type map was written from a remembered
table rather than verified, which is exactly what `archive.py`'s own comment
warns about (*"verified by reading contents, not assumed from a table"*).

---

## 6 · What was NOT checked — scoped

* **The games were not launched.** No claim here rests on watching anything.
* **K2's module archives were not scanned.** The `BodyBag` control covered K1's
  274 archives and both games' palettes. **K2's placed creatures are unchecked**,
  though K2's `bodybag.2da` is byte-identical.
* **Placed-instance survey used type 2044 only.** 2,177 objects were parsed as
  placeables in K1 modules; **the type code was inferred from resref names**
  (`invisible001`, `light001`) rather than confirmed against a format spec.
* **`GIT` files were not read.** Placed-object *instances* in an area live in the
  `.git`; I read the blueprints in the archives. A corpse placeable instantiated
  only in a `GIT` would not appear in my count.
* **`k_ai_master` was not read** — `k_def_death01` delegates every death to it
  with `KOTOR_DEFAULT_EVENT_ON_DEATH`, so **what KOTOR actually does on death at
  runtime is one file deeper than I went.** That is the first thing to read next.
* **Whether `SetIsDestroyable(FALSE)` is the common case was not established.**
  It is proven present and documented; `k_def_spawndead` is a *spawn-in-dead*
  script, i.e. set dressing. **How often live enemies get it is a question about
  `k_ai_master` and module scripts, unread.**
* **BG3's base `DOWNED`/`DYING` definitions were not found** — see `§3`.
* **No death-related loca strings were resolved** for either game.
* ⚠ **Nothing from BG3 may ship** — `ASSET-REPLACEMENT-01`; `PT-1350`'s
  extraction bargain covers KOTOR, not BG3.
