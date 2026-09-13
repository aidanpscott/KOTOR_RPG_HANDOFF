# TEST 085 — both weapon dice changes confirmed twice over: in the shelf
# data, and live in a fight where the damage line names the die. A plain
# Long Sword rolls 1d8, an item carrying its own damage rolls 1d12, and a
# plain Stun Baton rolls 1d4. Separately, and found while building the
# fixture: a creature equipped through Loom fights UNARMED unless the
# author guesses `weapon_r_1`, which nothing on screen names.

## Build state

    Loom            HEAD de8b5e4  Loom can author a damage override, and
                                  blank still means the base
    KOTOR-RPG-APP   HEAD 9b48af6  the item's own damage reaches the fight
                                  -- owner ruling
    lodestar        9e1fa4b8 — recorded and resolved agree, in both repos

Both trees clean, no drift. `check_shelf.py`: `✓ 25 rules files, all
identical to what the extracts generate` — the gate that matters, since
both changes are data. Loom PID `204370` and app PIDs `206178`, `210673`,
`211711` all killed by PID, all confirmed gone.

---

# 1 · LONG SWORD — both halves confirmed

### The base type dropped

`equipment.toml`, `id = "long-sword"`: **`damage = '1d8'`**, down from 1d12.

### Every named variant kept 1d12

All four Coder named, and the rest of the family, read from `items.toml`:

| | weapon | resref |
|---|---|---|
| **Krath War Blade** | **1d12**, 20–20 ×2 | `g_w_lngswrd02` |
| **Naga Sadow's Poison Blade** | **1d12** | `g_w_lngswrd03` |
| **Trandoshan Sword** | **1d12** | `w_melee_13` |
| **Shyarn** | **1d12** | `w_melee_24` |
| Long Sword | 1d12 | `g_w_lngswrd01` · `w_melee_02` |

### And it holds in a fight, not just in the file

Loom now carries a **`damage — optional, blank uses the base type`** field
on `NEW ITEM`, so I authored the two cases directly and put them in the
hands of two creatures:

```toml
[item] name = "Plain Blade"  base = "long-sword"                    # no damage
[item] name = "Named Blade"  base = "long-sword"  damage = "1d12"   # override
```

The damage line names the die, so one swing settles each:

> `plain-wielder: Plain Blade · rolled 16 — d20 15 + attack 1 + Strength 0
> · needed 15 — hit · **damage 8 — 1d8 8**`

> `named-wielder: Named Blade · rolled 18 — d20 17 + attack 1 + Strength 0
> · needed 15 — hit · **damage 6 — 1d12 6**`

**The plain base weapon actually dropped, and an item with its own damage
actually didn't.** Both halves, live.

The mechanism matches: `attack.dart:604` is now
`damage: itemOrBase(r.item, base, 'damage')`, and `itemOrBase` returns the
item's value when it is a non-empty string, else the base's — *"a blank is
absence, not an override."*

---

# 2 · STUN BATON — confirmed, and the whole family follows

`equipment.toml`, `id = "stun-baton"`: **`damage = '1d4'`**, up from a flat
1. Live, from a third authored weapon with no override:

> `baton-wielder: Plain Baton · rolled 17 — d20 16 + attack 1 + Strength 0
> · needed 15 — hit · **damage 2 — 1d4 2**`

And the named K1 variants are exactly as described:

| | weapon | resref |
|---|---|---|
| Stun Baton | **1d4** | `g_w_stunbaton01` |
| **Bothan Stun Stick** | **1d4** | `g_w_stunbaton02` |
| **Bothan Chuka** | **1d4** | `g_w_stunbaton03` |
| **Rakatan Battle Wand** ×4 | **1d6** | `g_w_stunbaton04`–`07` |

Three at 1d4 and four wands at 1d6, as stated.

---

## ⚠⚠ FOUND WHILE BUILDING THE FIXTURE — a creature equipped through Loom fights unarmed

This is not part of either change, but it is what the run turned up, and
it is the shape this corpus keeps naming.

Loom's `NEW CREATURE` dialog has a **`slot` / `item` / `equip`** row. I
typed the obvious thing:

    slot = weapon        item = items/weapons/blade-named

Loom accepted it, showed `weapon = items/weapons/blade-named` back to me
as confirmation, and wrote `[equipment] weapon = "…"` into the `.crtr`.

**In the fight, that creature was `unarmed` and rolled `1d3`:**

> `named-wielder: **unarmed** · rolled 18 … hit · damage 3 — **1d3 3**`

The app reads exactly one key — `attack.dart:482`:

```dart
equippedFrom(c.equipment['weapon_r_1'], packageDir, baseTypes);
```

Changing the key to `weapon_r_1` in the same file made the same creature
fight with its blade at `1d12`. **Nothing else changed.**

**Why this is worth raising rather than filing as my mistake.** It *was*
my mistake — but nothing could have told me. Loom's field is free text
with no hint, no pick-list and no validation, and its own source comment
explains why:

> `PT-1252` locks eleven slots and only two KEY names are written down
> anywhere — `body` and `weapon_r_1` — so the author names the slot and
> Loom writes it. **Loom does not invent the other nine.**

That is a reasoned choice, and I am not arguing against it. The problem is
what happens after: **the wrong key is silent at every layer.** Loom
accepts it and echoes it back as though it landed. Loom's Verify does not
flag it. The app does not mention it. The creature simply fights with its
fists, and the only way to find out is to read `1d3` in a combat line and
know what it means.

Contrast the app's own behaviour one line away — for an item path it
cannot open it says so out loud, in this very run:

> `equips 'items/weapons/blaster-rifle', which will not open: There is no
> item here.`

So an unreadable **path** is reported and an unrecognised **slot** is not.
The field it would take is already known to Loom's own comment: naming the
two keys that are written down, in the hint text under the slot box, would
close it without inventing the other nine.

---

## Method, and what is mine

- **The named catalogue variants are shelf rows, not package blueprints**,
  so they cannot be equipped directly. Coder's *"if you can
  authorable/access one"* anticipated this. I tested the authorable
  equivalent — an item carrying its own explicit `damage` — which is the
  same mechanism the catalogue rows use and the one the owner ruling
  added. The catalogue values themselves I verified in the data.
- **Instrumentation, declared:** three weapons, three creatures and three
  placements added to **my own** `strongroom-rebuilt`, plus one direct
  edit of the slot key described above. **All removed afterwards** — the
  package is restored from a pre-test backup and verified byte-identical
  by `diff -r`.
- **The party died** in the first fight (three armed enemies against a
  level-1 Soldier whose class weapon this package does not carry). That
  cost nothing: both blade lines had already printed. I thinned the fight
  to one wielder for the baton reading.

## Also seen, not chased

- Two catalogue rows are both named plain **"Long Sword"**
  (`g_w_lngswrd01`, `w_melee_02`) and both carry 1d12, while the base type
  they share now rolls 1d8. That is consistent with the ruling — a
  catalogue row states its own damage — but it does mean two things a
  player can call a Long Sword roll different dice. Naming it in case the
  catalogue rows were meant to be re-derived rather than pinned.
- The engine comment says *"eleven weapons inherit from `long-sword`"*; I
  found six rows by name. The mapping from resref to base type is not
  something I read, so I am not claiming a discrepancy — only that I did
  not verify the other five.

## What I did not do

- **Did not re-test the extension rename or the grenade save types.** Both
  were confirmed in TEST 084 and nothing this session touched them.
- **Did not test the four Rakatan wands or the Bothan variants in a
  fight** — they are catalogue rows, and the authorable-override path they
  rely on is the one confirmed above.
- TARGETING-01 — not ready, not touched.

## State

- **`strongroom-rebuilt` restored from backup and verified identical** —
  nine `.toml` files, exactly as TEST 083 left it.
- `locked-and-trapped` and `tester-strongroom` untouched.
- Saves created in `strongroom-rebuilt` during the fights, not cleaned up.
- All Loom and app PIDs killed by PID, confirmed gone.
