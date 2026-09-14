# TEST 090 — THE 975-ENTRY PALETTE IS RIGHT ON ALL FIVE COUNTS, and the counts
# are real: 358+132+403+66+9+7 = 975, and 65 + 910 is what the data says too.
# Collapse, search across name/base/category with auto-open, an explicit empty
# result, and the dimmed prop rows refusing with a reason — all confirmed.
# Edit Copy on real named rows carries their OWN stats: three items off ONE base
# type with three DIFFERENT droid bonuses, and the base type with none.
# All three weapon fixes hold — lightsabers on K1's dice across all 42 rows,
# Naga Sadow's duplicate gone exactly as ruled, and the racial bonus per-weapon.
# ⚠ Both confirmed LIVE: `1d6 6 + 2d8 vs droid 3+8` and `2d10 … + 1d6 vs droid`.
# ⚠ One new thing: every double-bladed lightsaber prints `only is not modelled`
# on every swing, for a word that carries no mechanics.

## Build state

    Loom            HEAD 1fe9a79  PT-2090: 45 weapons state their own damage
    KOTOR-RPG-APP   HEAD 3e969ec  PT-2081: the armour guard carries both clauses
    lodestar        2225db8b — lock, pubspec ref and the pub-cache checkout all
                    agree, in both repos

Both trees clean. `check_shelf.py` green at start and end:
`✓ 25 rules files and 65 standard blueprints`.

### ⚠⚠ BOTH SHIPPED BUNDLES WERE STALE — third session running

| | kernel_blob | oldest commit it is missing |
|---|---|---|
| **Loom** | `2026-09-13 16:15:48` | `603f31e` (14:54 on the 14th) — **the entire palette** |
| **app** | `2026-09-14 00:17:40` | every commit made that day |

Loom's was **a day and a half old**: launching it from the tree gets a build
with no tree, no search and no catalogue pour at all. I rebuilt both Dart sides
with `flutter assemble … debug_bundle_linux-x64_assets`, ran from private copies
in my scratchpad, and **left both shared bundles byte-for-byte as I found them**
— verified after, and both trees are still clean.

I have now flagged this in three consecutive reports. It is not costing me much
any more, because I check the timestamp first; it will cost whoever doesn't.

---

# 1 · THE PALETTE — all five counts

### ✓ The count is real, and it is two numbers honestly kept apart

> `65 shipped with the rules · 910 more from the catalogue — tap one to copy
> it into this package and edit the copy`

**I derived 975 from the data before looking at the UI.** Parsing `items.toml`:
1,424 rows, of which **910 carry both a `base` and a `palette` entry** — the two
facts `_catalogue` requires — and the shelf ships **65** blueprints. `65 + 910 =
975`. The palette's own six category counts then sum to exactly the same:

| Weapons | Droid Armour | Armour | Consumables | Utility | Objects | |
|---|---|---|---|---|---|---|
| 358 | 132 | 403 | 66 | 9 | 7 | **= 975** |

*(A small correction to the brief: I checked **50** at TEST 088, not 65 — the
palette said `50 shipped with the rules` then and the count is computed from the
list. The shelf has grown by fifteen since.)*

### ✓ Collapsed by default, each with a count, and one opens alone

All six render with a `+` and their count on first open. Tapping **Utility 9**
flipped that one to `−` and listed its children; **every other category still
read `+`**. And the count is the real number of children rather than a separate
tally — Utility's nine are all nine there are:

    Advanced Repair Kit · Computer Spike · Construction Kit · Parts ·
    Repair Kit · Repair part · Security spike · Security Spike Tunneler ·
    Security Tunneler

### ✓ Search covers name, base type AND category — and opens what it finds

| typed | result | |
|---|---|---|
| `Ionmaster` | `Weapons 1` → `Ranged` → **Aratech Ionmaster** | by **name** |
| `ion-rifle` | `Weapons 14` → the fourteen | by **base type** |
| `Droid Armour` | `Droid Armour 132` → `Plating` → … | by **category** |

**Every one arrived already open** — the matched branch and its sub-group are
expanded with no second tap, which is what makes searching 975 entries usable.

**And the filtered count is the true count, not a guess.** I checked `ion-rifle`
against the data first: 13 catalogue rows on that base type carry a palette
entry, plus the one shelf blueprint = **14**. The palette said 14.

### ✓ An empty result says so

> `nothing matches "zzqqxx"`

Explicit, and it quotes the term back rather than leaving a blank pane.

### ✓ The unnamed rows are distinct, and they refuse with a reason

Among the fourteen `ion-rifle` hits are three with no display name, shown by
their catalogue id — `propir01`, `propir02`, `propir03`. **Measured rather than
eyeballed:** a named row renders `#159374` and a prop row `#4A4438` — a
different hue, not merely dimmer. Tapping one:

> `` `propir01` has no name in the catalogue — `ITEMS-01` writes an em dash for
> this row, and a blueprint cannot be generated without one ``

It names the row, says why, and **writes nothing** — the package file count was
unchanged. *(80 of the 910 poured rows are in this state, which matches the
source's own "the eighty with no display name".)*

### ✓ And the TEST 088 refusal still holds on a poured row

Copying `Aratech Ionmaster` twice:
`` this package already has `items/weapons/w_blaste_21` — `Edit Copy` never
replaces what is already here ``, md5 unchanged.

---

# 2 · EDIT COPY CARRIES THE ITEM'S OWN STATS — the decisive demonstration

Four taps, four files, **one base type**:

| file | name | `damage` |
|---|---|---|
| `ion-blaster.item` | Ion Blaster *(the base type)* | *(none — inherits `1d6`, **no droid bonus**)* |
| `g_w_ionblstr01.item` | Ion Blaster | `1d6 + **1d10** vs droid` |
| `w_blaste_02.item` | Ion Blaster | `1d6 + **1d12** vs droid` |
| `w_blaste_21.item` | Aratech Ionmaster | `1d6 + **2d8** vs droid` |

**Three items, three different droid bonuses, and the plain base type with
none** — in one folder, from one palette, off one base type. That is exactly
*"rather than every ion weapon in the family sharing one uniform bonus"*, and it
is not a claim about the data: it is four files Edit Copy wrote.

Two more, and each carries its row's own facts plus the `catalogue` id that
keeps the effect join working:

    g_w_lngswrd03.item   Naga Sadow's Poison Blade   damage = "1d6 + 2"
    g_w_dblsbr006.item   Bastila's Lightsaber        damage = "2d10 + 1d6 vs droid"

---

# 3 · THE THREE WEAPON FIXES

### ✓ Lightsabers take K1's dice — all 42 rows, not just the four base types

The base types read `2d6 · 2d8 · 1d8 · 2d10`. **Checked against the source
rather than against the brief:** `EQUIPMENT-01 §4b`'s own table gives K1
`2d6 / 2d8 / 2d10` and K2 `2d8 / 2d10 / 2d12`, and the shelf carries the K1
column exactly.

Then the whole family, because four base types is not 42 weapons:

| base type | leading die | rows | |
|---|---|---|---|
| `short-lightsaber` | `2d6` | 13 | K1 ✓ |
| `lightsaber` | `2d8` | 15 | K1 ✓ |
| `double-bladed-lightsaber` | `2d10` | 14 | K1 ✓ |

**Rows leading with a non-K1 die: zero.**

### ✓ Naga Sadow's duplicate is gone — and precisely as ruled

`damage = "1d6 + 2"`. The `+ 2d6` is gone; the poison remains as the catalogue
effect (`2d6`, five rounds, DC 10) that TEST 089 measured ticking.

⚠ **One precision, because the brief and the ruling differ slightly.** The brief
says *"no longer deal a flat bonus on top of its poison — just the base die plus
the poison"*. The **flat `+2` is still there**, and that is correct: `PT-2090`
ruled *"REMOVE THE DUPLICATE FLAT **+2d6**"*, and the later ruling explicitly
left the Enhancement-conversion question alone as *"a magnitude question
rather than a spurious-term question"*. So the shelf matches the **ruling**
exactly. I am flagging it only so nobody reads the brief, finds `1d6 + 2`, and
thinks the fix half-landed.

### ✓ The racial bonus is per-weapon — 20 rows carry one, and they differ

Exactly **20** catalogue rows carry a `vs droid` term, matching
`PT-2090`'s *"the 20 weapons that actually carry it"*. Within the ion family
alone: `1d10`, `1d12`, `2d8`, `2d6`, `2d10`, and several with **none**
(`Ion Rifle: Null`, and the unnamed prop rows). `Aratech Ionmaster` is the
single `2d8`.

*(Also seen: the bonus is not confined to ion weapons — Bastila's Lightsaber,
Bacca's Ceremonial Blade, the Sith Assassin Pistol and Jurgan Kalta's Assault
Rifle each carry one. And two rows carry **two** `vs droid` terms — Yusanis'
Brand and the Verpine Droid Disintegrator. Naming that, not filing it.)*

---

# 4 · AND BOTH FIXES HOLD LIVE, THROUGH THE PALETTE'S OWN OUTPUT

I copied the Edit Copy files **verbatim** to the path chargen equips, so the
weapon in the player's hand is literally what the palette generated. Two
targets identical but for one word — `species = "human"` and `species = "droid"`.

**Aratech Ionmaster** (`1d6 + 2d8 vs droid`):

> vs the organic — `damage 6 — 2d6 2+4 × 2 critical · 394 left` — **no droid term**
> vs the droid — `damage 17 — 1d6 6 + **2d8 vs droid 3+8** · 383 left`

**Bastila's Lightsaber** (`2d10 + 1d6 vs droid`), four hits on the droid and
one on the organic:

> `damage 17 — **2d10** 4+4 + 1d6 vs droid 5 + Strength 4 · 339 left`
> `damage 26 — **2d10** 9+8 + 1d6 vs droid 5 + Strength 4 · 313 left`
> `damage 44 — 4d10 6+8+9+10 + 1d6 vs droid 1+6 + Strength 4 × 2 critical`
> vs the organic — `damage 8 — **2d10** 2+2 + Strength 4 · 392 left` — **no droid term**

**`2d10` is K1's double-bladed die printed in a live fight** (K2's is `2d12`),
and every individual die across all those rolls is ≤ 10. So: a blueprint the
palette generated from a real named catalogue row reaches a fight, uses its own
damage rather than the base type's, rolls K1's dice, and applies its own racial
bonus only against a droid.

---

## ⚠ ONE NEW THING — a false *not modelled* on every double-bladed lightsaber

Every swing printed, beside the damage:

> `Bastila's Lightsaber  UNIQUE: **only** is not modelled`

`weaponFromBase` builds `notModelled` from whatever is **left of the `threat`
string** after the crit range and the multiplier are stripped
(`item_open.dart:632–647`). The double-bladed lightsaber's threat is
`"20 only / ×2"`; `20` and `×2` both parse, and the leftover is the English word
**`only`**.

**Nothing is actually unmodelled.** The crit range is right, the multiplier is
right, and `only` is prose meaning *20 and not 19–20* — a fact the parser has
already captured by reading `20`.

**Why it is worth raising.** The same mechanism is doing real work on the other
three base types that leave something behind — `hold-out-blaster` leaves
`on-hit stun`, `sonic-pistol` and `sonic-rifle` leave `Dex damage`, and those
**are** unmodelled mechanics a player should be told about. One false positive
in a set of four teaches a player to ignore the sentence. And it is now on every
attack line of **15 weapons** (14 catalogue rows plus the base type) that the
palette has just made copyable; **46 catalogue rows sit on the four affected
base types**.

*Offered as one: strip a bare `only` the way `/` and `·` are already stripped,
since it qualifies a number that has been read rather than naming a mechanic.*

## Also seen, not chased

- The status line keeps the **previous** message after an action that produces
  none — my `propir01` refusal was still showing several taps later. Cosmetic.
- In play the app notes `1 at the default speed — no rule for \`droid\`` for a
  droid creature. Unrelated to this slice; naming it in case it is news.

## What I did not do

- **Did not exercise every one of the 975.** I opened one category in full,
  three searches, and copied six items across two base types and three
  categories.
- **Did not test the 45 weapons that state their own damage** as a set — I
  confirmed the mechanism on six, and the lightsaber family exhaustively from
  the data.
- **Did not re-test** the TEST 088 palette basics beyond the double-copy
  refusal, nor the `vs droid` mechanism itself (TEST 065 / `PT-1740`, closed) —
  what is new here is that each weapon carries **its own** bonus, which is what
  I measured.
- **Did not verify Shyarn's `+2d6`**, which the ruling routed for separate
  evidence and which is not in this brief.

## State

- **New package `catalogue-probe` is mine and left on disk**: one area, one
  hand-authored item, and **six blueprints written by Edit Copy** across
  weapons of three different base types. It loads with **no problems** in both
  programs.
- ⚠ **`items/weapons/blaster-rifle.item` and `short-sword.item` are verbatim
  copies of Edit Copy's output**, placed at the path chargen equips so the
  player would wield them. They currently hold Bastila's Lightsaber. Declared so
  nobody reads them as mis-authored.
- ⚠ **My `flutter assemble` output sits in both repos' `build/` and in my
  scratchpad** — gitignored, regenerable, and it does not shadow either desktop
  bundle. Both shared bundles verified unchanged; both trees clean.
- Saves from two runs in `catalogue-probe`, not cleaned up.
- My Loom PID `199941` and app PIDs `200975`, `201876` all killed by PID, all
  confirmed gone. Nothing of Coder's was touched.
