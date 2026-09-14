# TEST 091 — THE WHOLE DAMAGE CHAIN LANDS IN REAL COMBAT, and every reading is
# exact rather than plausible. Against energy 99, Bastila's Lightsaber dropped
# EXACTLY 4 — the universal term and nothing else. Against a target resisting
# ALL THIRTEEN KINDS AT 99 it dropped EXACTLY 0. The `vs droid` term appeared on
# the droid and on none of the other four. And the Dashade Sonic Disruptor split
# a single blow in two: the sonic half zeroed, the unstoppable half whole.
# The Mandalorian Disintegrator went through that same all-resisting target at
# FULL damage four times, because its base type is unstoppable too.
# ⚠ One precision: `universal` is NOT flagged `ignores_resistance` — a target
# resisting it BY NAME reduced it, and I measured that. Only `unstoppable` is.
# ✓ And TEST 090's `only is not modelled` is fixed — confirmed in play and in
#   the source, which cites the finding.

## Build state

    Loom            HEAD 6e84ded  PT-2110: 119 weapons state their own damage
    KOTOR-RPG-APP   HEAD 6e3bdc0  PT-2111: the damage chain, end to end, on a
                                  real catalogue weapon
    lodestar        df7e1692 — lock, pubspec ref and the pub-cache checkout all
                    agree, in both repos

Both trees clean at the end. `check_shelf.py` green at start and end, and it now
counts **26** rules files — `damage_kinds.toml` is the new one, and it is the
thing this whole slice rests on.

### ⚠⚠ BOTH BUNDLES STALE AGAIN — fourth session running

    Loom  blob 2026-09-13 16:15   HEAD 2026-09-14 16:42
    app   blob 2026-09-14 00:17   HEAD 2026-09-14 16:52

Rebuilt both Dart sides with `flutter assemble … debug_bundle_linux-x64_assets`,
ran from private copies, **left both shared bundles byte-for-byte as I found
them** — verified after, both trees clean. I check the timestamp first now, so
it costs me little; it will cost whoever doesn't.

---

## The instrument, stated first

Everything below is **printed damage against the vitality drop**, on my own
attack line, with five targets that differ only in what they wear:

| target | wears | |
|---|---|---|
| `t-plain` | nothing | the control |
| `t-energy` | `energy = 99` | |
| `t-universal` | `universal = 99` | the precision test |
| `t-droid` | nothing, `species = "droid"` | |
| `t-all` | **all 13 kinds at 99, `unstoppable` included** | |

All five are unarmed, 400 vitality, and carry a `never-player` doctrine, so
nothing but my own blow ever moves a bar. **`t-all` resists `unstoppable`
itself at 99** — so anything that lands on it is something resistance is not
permitted to touch, rather than something merely unlisted.

The three weapons are **Edit Copy's own output**, copied verbatim to the path
chargen equips:

    Bastila's Lightsaber       2d10 + 1d6 energy + 3 energy + 4 universal + 1d6 vs droid
    Dashade Sonic Disruptor    1d4 + 1d10 unstoppable
    Mandalorian Disintegrator  1d6 + 1d6 unstoppable + 2 unstoppable

*(That the palette folds these full strings correctly is `PT-2110` working, and
it is how I got the weapons at all.)*

---

# 1 · A TYPED KIND IS REDUCED BY A TARGET THAT RESISTS IT

Bastila's Lightsaber, whose base type `double-bladed-lightsaber` is itself
`kinds = ["energy"]`, so **the 2d10 and the Strength modifier riding on it are
energy too**. Against `t-energy` (`energy = 99`):

| line | printed | **dropped** |
|---|---|---|
| `damage 49 — 4d10 10+3+1+9 + 1d6 energy + 3 energy + 4 universal 3+5 14 + Strength 4 × 2 critical` | 49 | **8** |
| `damage 19 — 2d10 2+2 + 1d6 energy + 3 energy + 4 universal 4 7 + Strength 4` | 19 | **4** |

**Everything energy went to zero and the `4 universal` survived, to the point.**
On the critical it survived **doubled** — 8 — which is the flat bonus doubling
with the dice, exactly as the rest of the line does.

Against the control `t-plain`, the same weapon: printed **34 / 24 / 33**,
dropped **34 / 24 / 33**. Nothing reduced.

# 2 · ⚠ AND `universal` IS AN ORDINARY KIND — the precision worth having

The brief says the Universal term should be *"plain, unresisted bonus damage —
not tied to any particular kind"*. The first half is exactly right and §1 shows
it. **The second half needs one word of care**, and I built a target for it:
`damage_kinds.toml` gives `universal` `ignores_resistance = false`; **only
`unstoppable` is `true`**.

Against `t-universal` (`universal = 99`):

> `damage 20 — 2d10 2+5 + 1d6 energy + 3 energy + 4 universal 2 7 +
> Strength 4 · 384 left`

400 → 384 = **16 dropped from 20 printed**. The `4 universal` was reduced and
everything else landed — the mirror image of §1.

**So universal is not a bypass; it is a kind nothing normally resists.** That is
the right design and it matches the data, but *"unresisted"* and *"ignores
resistance"* are two different claims and only one of them is true of it. Worth
having straight before someone authors an item that resists it.

# 3 · UNSTOPPABLE GOES STRAIGHT THROUGH — and one blow shows both rules

The **Dashade Sonic Disruptor** is the decisive weapon because it is mixed: its
base `1d4` is **sonic** (from `sonic-pistol`), and its `1d10` bonus is
**unstoppable**. Against `t-all`, which resists all thirteen kinds at 99:

| line | printed | **dropped** |
|---|---|---|
| `damage 11 — 1d4 2 + 1d10 unstoppable 5 + Dexterity 4` | 11 | **5** |
| `damage 7 — 1d4 1 + 1d10 unstoppable 2 + Dexterity 4` | 7 | **2** |

**The drop is the unstoppable die exactly, both times.** The sonic part and the
Dexterity modifier riding on it went to zero; the unstoppable part was
untouched. Resistance demonstrably working and demonstrably bypassed **in the
same line**, which is the strongest form this evidence can take.

The same weapon against `t-plain`: printed **13 / 19**, dropped **13 / 19**.

### ✓ And the disruptor base types take it too — on Coder's named weapon

`disruptor-pistol` and `disruptor-rifle` both carry `damage_type = unstoppable`
and `kinds = ["unstoppable"]`, so a disruptor's **base die** bypasses as well.
The **Mandalorian Disintegrator** (`1d6 + 1d6 unstoppable + 2 unstoppable`,
base `disruptor-pistol`) against `t-all`, four hits:

| printed | 13 | 15 | 27 | 12 |
|---|---|---|---|---|
| **dropped** | **13** | **15** | **27** | **12** |

**Full damage every time, including the base `1d6` and the Dexterity modifier**,
against a target that resists all thirteen kinds at 99. That is *"the disruptor
family takes K2's full package"* confirmed at the base type, not just on the
folded bonus.

# 4 · THE RACIAL CONDITIONAL FIRES ONLY ON THE RIGHT TARGET

Bastila's Lightsaber against `t-droid`:

> `damage 28 — 2d10 1+7 + 1d6 energy + 3 energy + 4 universal + **1d6 vs droid**
> 5+4 7 + Strength 4 · 372 left`

**`+ 1d6 vs droid` is in the term list here and in none of the other four
targets' lines.** 400 → 372 = **28 dropped from 28 printed** — the droid resists
nothing, so the whole blow including the racial bonus lands.

# 5 · AND EVERYTHING TOGETHER, AGAINST EVERYTHING

Bastila's Lightsaber against `t-all` — every part of it a resisted kind:

| printed | 22 | 19 | 45 *(critical)* |
|---|---|---|---|
| **dropped** | **0** | **0** | **0** |

**The bar never moved off 400.** Which is the other end of §3: the same target
that stops this weapon completely cannot touch a single point of the
Disintegrator.

---

## ✓ TEST 090's `only is not modelled` is fixed

It printed on every swing of every double-bladed lightsaber last session. This
session Bastila's Lightsaber printed **no such note** across a whole run, while
the Dashade Sonic Disruptor still correctly printed `Dex damage is not
modelled` — so the mechanism is intact and only the false positive is gone.

The source says so too, and cites the finding:

```dart
// ⚠⚠ A BARE `only` IS PUNCTUATION, NOT AN UNMODELLED RULE — `TEST 090`,
// owner ruling. … ⚠ AND ONE FALSE POSITIVE IN A SET OF FOUR TEACHES A
// PLAYER TO IGNORE THE SENTENCE.
rest = rest.replaceAll(RegExp(r'\bonly\b', caseSensitive: false), '');
```

The base type's `threat` is still `"20 only / ×2"`, so the fix is in the reader
rather than in the data — which is the right end, since the document's wording
is correct English.

## Smaller things seen

- **The damage line groups its rolls by kind**, so a term list is followed by
  that group's dice and its total — `+ 1d6 energy + 3 energy + 4 universal 4 7`
  reads as *the energy group rolled 4 and comes to 7*. Every one of the
  seventeen lines I checked reconciles to the printed total, so this is a note
  about density rather than a defect. It does take a second read.
- `1 at the default speed — no rule for \`droid\`` appears for a droid creature.
  Unrelated to this slice; still there.

## What I did not do

- **Did not test `light side`, `dark side`, `ion`, `cold` or `sonic` as typed
  kinds individually.** `energy` was measured to the point and the mechanism is
  one function with no per-kind branch; the other twelve were exercised only as
  part of `t-all`.
- **Did not test a target resisting a kind PARTIALLY** — every ward here is 99,
  chosen so a surviving part is unambiguous. `TEST 087` measured a partial
  reduction (fire 5) and `TEST 089` a partial tick, so the arithmetic is covered
  elsewhere.
- **Did not test the Sonic Disruptor (`w_brifle_27`)**, the rifle sibling of the
  Dashade — same shape, same base-type kind.
- **Did not re-test the palette** beyond using Edit Copy to obtain the weapons.

## State

- **New package `damage-probe` is mine and left on disk**: one area, five
  targets, one doctrine, three resist wards, and **three weapons written by
  Edit Copy**. It loads with no problems.
- ⚠ **`items/weapons/blaster-rifle.item` and `short-sword.item` are verbatim
  copies of Edit Copy output** at the path chargen equips, swapped between runs;
  they currently hold the Mandalorian Disintegrator. Declared so nobody reads
  them as mis-authored.
- ⚠ **`resist-all.toml` is generated from `damage_kinds.toml` itself**, so it
  lists whatever the shelf lists — it will not silently miss a kind added later.
- ⚠ My `flutter assemble` output sits in both repos' `build/` and in my
  scratchpad — gitignored, regenerable, shadowing neither desktop bundle.
- Saves from three runs, not cleaned up.
- Loom PID `216117` and app PIDs `216411`, `217161`, `217746` all killed by PID,
  all confirmed gone. Nothing of Coder's was touched; Loom's tree was briefly
  showing an uncommitted file when I started and I left it alone — it was clean
  again by the time I used it.
