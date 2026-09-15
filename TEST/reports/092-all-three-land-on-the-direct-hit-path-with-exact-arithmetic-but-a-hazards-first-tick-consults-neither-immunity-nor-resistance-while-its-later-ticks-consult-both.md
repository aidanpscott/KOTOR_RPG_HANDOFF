# TEST 092 — ALL THREE LAND ON THE DIRECT-HIT PATH, to the point.
# The Mandalorian Combat Suit read `needed 16` (its own +3, not its base's +4)
# AND reduced slashing by exactly 2 — one item proving both PT-2144 and
# PT-2153. Droid Desh Plating read `needed 19` where its base type would give
# 22. The Thermal Shield Generator, a BELT, added no Defence and took the fire
# part to zero.
# ⚠⚠ BUT THE TWO OVER-TIME PATHS DO NOT AGREE, which is the thing this routing
# asked me to confirm. A hazard's FIRST tick consults neither immunity nor
# resistance; its later ticks consult both. Measured on both mechanisms:
#   fire mine on a FIRE-IMMUNE player   spring 6 damage · then 0,0,0,0,0
#   poison mine on a `poison = 15` wearer  spring 5 damage · then 0,0,0,0
# The control rules out a dead instrument: an unresisted poison ticked and
# killed the same character.

## Build state — and it moved three times while I worked

    Loom            HEAD 69a3de7 when I started, 42a80f4 by the end
    KOTOR-RPG-APP   HEAD 487794c → 047037d → cf29052
    lodestar        533ec3ad — lock and the pub-cache checkout agree, both repos

`check_shelf.py` green at start and end: `✓ 26 rules files and 65 standard
blueprints`.

**⚠ I built the app from `047037d` and say so because HEAD is no longer that.**
Coder committed twice more while I was running. I re-checked afterwards: the
only later commit touching this path is `cf29052`, which adds a third map
(`immuneEffects`, the poison/critical-hit work Maine says is next) — and
**`_springsAs` still calls `applyDamage(amount: left, …)` at HEAD**, so the
finding below is not stale.

⚠⚠ **Both bundles were stale again — fifth session running.** Loom's blob was
from the 13th, the app's from the 14th, against HEADs from the 15th. Rebuilt
the app's Dart side with `flutter assemble … debug_bundle_linux-x64_assets`,
ran from a private copy, **left both shared bundles byte-for-byte as I found
them**.

### ⚠ And I did NOT use Edit Copy to get the items — deliberately

Loom's tree was mid-edit on **exactly** `lib/item/standard_blueprints.dart` and
`lib/item/item_writer.dart`, plus a `pubspec.lock` repin. Running that build
would have measured unshipped work and called it the palette. So I read the
**shipped** writer at `HEAD` instead and transcribed each blueprint into the
format it emits — `defence = "+3"`, `immune = ["fire"]` sorted, `[item.resists]`
last with quoted keys — taking every value from the item's own catalogue row.
Declared because it matters: what I measured is **the app reading a blueprint**,
which is what this routing asked for; that Edit Copy *writes* that blueprint is
`TEST 090`'s question and I did not re-open it.

*(Routing note, not a defect: the brief's PT numbers are a few off the log. The
commits are `PT-2153` for the resist table, `PT-2144` for the Defence override
and `PT-2157` for the immunities.)*

---

## The instrument

One firing line, six targets that differ only in what they wear — all unarmed,
400 vitality, `never-player`, dex 10 and soldier, so an unarmoured one is
`needed 13`. The weapon is **Ajunta Pall's Blade**, `2d6 + 4 fire`, whose base
type is slashing: **two parts of two kinds**, so one blow reads a slashing
resist and a fire immunity separately.

# 1 · THE ITEM'S DEFENCE WINS OVER ITS BASE TYPE'S — `PT-2144`

| target | item | base type | item states | **needed** |
|---|---|---|---|---|
| `t-plain` | — | — | — | **13** |
| `t-light` | Light Combat Suit | `armour-class-4` **+4** | **+3** | **16** |
| `t-mando` | Mandalorian Combat Suit | `armour-class-4` **+4** | **+3** | **16** |
| `t-desh` | Droid Desh Plating | `heavy` **+9** | **+6** | **19** |
| `t-bastion` | Environmental Bastion Armor | `armour-class-6` **+6** | *(none)* | **19** |

**Droid Desh Plating is the decisive one** — three points apart, so there is no
reading of 19 that the base type's +9 could produce. Three misses, all `needed
19`. The two suits at 16 rule out +4 the same way, one point at a time.

**And silence still means the base type's.** Environmental Bastion Armor states
no override and came out at `13 + 6 = 19`, its class's number.

*(Precision on the brief: the catalogue does not carry a `+3` field. It carries
`DecreaseAC (AC Armor) Penalty_-1` as an effect, and the blueprint is written
with the arithmetic already done. `+4 − 1 = +3` and `+9 − 3 = +6` — which is
what I measured, but the item is stating a penalty, not a Defence.)*

# 2 · A PALETTE ITEM'S RESIST TABLE APPLIES — `PT-2153`

The Mandalorian Combat Suit carries three real resist effects at **2** each
(bludgeoning, piercing, slashing). Against it:

| line | printed | **dropped** | reduced by |
|---|---|---|---|
| `damage 14 — 2d6 5+1 + 4 fire 4 + Strength 4` | 14 | **12** | **2** |
| `damage 12 — 2d6 1+3 + 4 fire 4 + Strength 4` | 12 | **10** | **2** |

The slashing part (2d6 + Strength) lost exactly 2; the 4 fire part was
untouched, because this item resists no fire. **One item, both features:** it
read `needed 16` *and* reduced by 2 in the same blow.

# 3 · IMMUNITY ON A DIRECT HIT — `PT-2157`

| target | item | **needed** | printed → dropped | reduced by |
|---|---|---|---|---|
| `t-thermal` | Thermal Shield Generator *(a **belt**)* | **13** | 13 → **9** | **4** |
| `t-bastion` | Environmental Bastion Armor | **19** | 19 → **15**, 17 → **13** | **4** |

The whole 4-point fire part went, both times, on both items. And the belt is
worth its own line: **`needed 13`** — `belt` has no `defence` column, so it
contributed nothing to Defence while still carrying its immunity. That is the
slice-d behaviour working, and it is the case the comment says was previously
throwing the resist table away with the Defence.

---

# 4 · ⚠⚠ AND THE TWO OVER-TIME PATHS DISAGREE

This is the one the routing asked to confirm specifically, and the answer is
that they do not agree.

A hazard's damage is applied in **two different places**. `_springsAs` applies
the first tick when you step on it; `endRound` applies every later one. The
round-boundary path takes `resists:` and `immune:` — the work this session did.
**`_springsAs` takes neither:**

```dart
final left = out.succeeded ? (afterSave(e.effect!, amount).amount ?? 0) : amount;
…
final d = applyDamage(vitality: me.vitality, amount: left, …);
```

`left` goes straight into `applyDamage`. The save is honoured; resistance and
immunity never enter it. **Still true at HEAD**, two commits later.

### Measured, on both mechanisms, with a live control

The player wore the **real Thermal Shield Generator** (`g_i_belt014`, immune
fire), put in the body slot through the path chargen equips. Two mines, one
kind each, same player, same round loop:

| | mine springs | round boundaries |
|---|---|---|
| **fire**, player **immune to fire** | **6 damage** ⚠ `14 → 8` | **0 · 0 · 0 · 0 · 0** ✓ |
| **poison**, player `poison = 15` | **5 damage** ⚠ `8 → 3` | **0 · 0 · 0 · 0** ✓ |
| **poison**, player resists nothing | 5 damage ✓ | ticked on and **killed the character** ✓ |

> `goes off — d20 16 = 16 vs 99 · 6 damage · 8 of 14 · 4 more rounds`

**Why the control matters.** A zero proves nothing by itself — a tick that never
fired would look identical. The third row is the same mine on the same boundary
with nothing resisting it, and it ran the character to a total party defeat. So
the boundary path is alive and honouring both mechanisms; the spring path is
alive and honouring neither.

**And it is not a loading race.** The immunity that failed on the spring is the
same immunity that worked five times at the boundary, in the same fight, from
the same `_armour` read — which was complete before the fight was built,
because I started the fight before stepping on anything.

**Why it matters rather than merely being untidy.** The first tick is the one a
player always takes — you cannot reach the later ones without it — so a fire
immunity currently stops four ticks out of five and lets the one you definitely
receive through. It is the same shape this corpus keeps finding: a rule wired
into one of two call sites. `PT-2035` slice (c) already did this journey once
for the *expression*, so that a mine "cannot roll one thing when you step on it
and a different thing at the boundary"; the amounts now agree and what is done
to them does not.

*Offered as one: `_springsAs` has `_fight` in hand two lines below, so
`f.resistsFor` / `f.immuneFor` for the player's handle are already reachable at
that call site.*

---

## ⚠ Also found — two catalogue rows per name, with different mechanics

Both belts Maine named exist **twice**, and the two rows are not the same item:

| name | id | src | what it actually does |
|---|---|---|---|
| Electrical Capacitance Shield | `g_i_belt013` | K1 | **immune** electrical |
| Electrical Capacitance Shield | `a_belt_12` | K2 | **resist** electrical **15** |
| Thermal Shield Generator | `g_i_belt014` | K1 | **immune** fire |
| Thermal Shield Generator | `a_belt_13` | K2 | **resist** fire **15** |

So "the four items with full immunity" is true of two of the four names only on
the K1 row; an author who taps the other one gets a large resist instead. This
is the `Long Sword` collision the join was designed around — `PT-2059` made the
id the identity precisely for this — so nothing is broken. But the palette shows
both under one name with nothing to tell them apart, and the difference is
immunity versus a number.

*(A 15-point resist and an immunity are also indistinguishable against these
weapons — no fire or electrical part in the catalogue exceeds 15 — so the
distinction is currently invisible in play as well as in the palette.)*

## What I did not do

- **Did not test cold or sonic immunity**, only fire and electrical-by-proxy.
  Environmental Bastion Armor carries all three and one function reads them.
- **Did not test `Droid Quadranium Armor`** — fire immunity plus three resists
  at 5, the same two mechanisms measured separately above.
- **Did not exercise the effect-vocabulary immunities** (mindspells, poison,
  critical hits, paralysis, drain) — 81 of the 87 immunity properties in the
  catalogue. Maine says the condition system they need does not exist, and
  `cf29052` landed the first of them after I had built.
- **Did not re-open Edit Copy** (TEST 090) — see the build-state note.

## State

- **New package `immunity-probe` is mine and left on disk**: one area, seven
  creatures, one doctrine, seven worn-item blueprints and one weapon. It loads
  with **no problems**.
- ⚠ **`items/armour/clothing.toml` is the real Thermal Shield Generator**, put
  at the path chargen equips so the immunity could be on the player; it also
  carries a `poison = 15` table from run 3. **`clothing.item` was deleted** to
  make room for it, so this package no longer carries the shelf's clothing.
- ⚠ **`items/weapons/blaster-rifle.toml` and `short-sword.toml` are Ajunta
  Pall's Blade**, at the chargen weapon path. Declared so nobody reads them as
  mis-authored.
- ⚠ The worn-item blueprints were **hand-transcribed** from their catalogue
  rows into the shipped writer's format, not produced by Edit Copy — see above.
- ⚠ My `flutter assemble` output sits in the app repo's `build/` and in my
  scratchpad — gitignored, regenerable, shadowing neither desktop bundle.
- Saves from three runs, not cleaned up. One total party defeat, deliberately.
- App PIDs `113525`, `117388`, `119362` all killed by PID, confirmed gone. I
  launched no Loom. Both repos had uncommitted files of Coder's throughout and
  **nothing of theirs was touched** — I built only from a moment when the app
  tree was clean, and named the commit.
