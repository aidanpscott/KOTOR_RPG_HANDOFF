# TEST 084 — the extension rename is invisible in both directions:
# old `.toml` packages, old saves and old conversations all still work,
# and new authoring writes `.crtr .item .obj .area .dlg`. The grenade save
# types are correct in the data and match each grenade's own description
# verbatim — but nothing shows them, because the one line that displays a
# save hardcodes the word `'Save'` with the kind available beside it.

## Build state

    Loom            HEAD 86d0139  Loom writes the new extensions and still
                                  edits the old files -- PT-1991
    KOTOR-RPG-APP   HEAD 1c833b8  a caller that asks the disk itself has to
                                  resolve itself -- PT-1991
    lodestar        ef9cf3f1 — recorded and resolved agree, in both repos

Both working trees clean, no `ref: main` drift. `check_shelf.py`:
`✓ 25 rules files, all identical to what the extracts generate` — which
matters here, because the grenade data below is generated.

Loom PIDs `192254`, `192582`, `193314` and app PID `193479` all killed by
PID, all confirmed gone.

---

# 1 · THE EXTENSION RENAME — both halves confirmed

**The contract, read first** (`package_files.dart`): `pkg · area · crtr ·
item · obj · dlg · doct`, with `door` reserved and unused, `obj`
explicitly provisional, `base-rules` deliberately staying plain `.toml`,
and a dual read that resolves **in both directions** so *"a package
half-converted still opens."*

### ✓ Existing `.toml` content still works — checked in both programs

**In Loom:** opened `locked-and-trapped`, which is nine `.toml` files and
nothing else. Both areas and the `console` conversation list; `a01`
renders the whole room — arrival `back`, the mine drawn at both its
squares, footlocker, console, crate, both doors and the probe droid.

**In the app, which is the stronger test:** the library reads **all 14
packages** (`14 packages installed · checked, 6 with problems` — the sixth
is my own `strongroom-rebuilt`, for its class weapons). I then loaded an
**old save** in that old package: Vash Roarke came back at the square he
was left on, the room drew correctly, the arrival line still read
**`you notice mine.strongroom.01 — 14 against 12`**, and right-clicking
the console still offered `Examine (Science) · Slice (Slicing)` — a
`.toml` placement reading a `.toml` conversation.

So: old package, old save, old conversation, after the rename. Nothing
changed.

### ✓ New authoring writes the new extensions

Authored one of each into a package that was previously all `.toml`, and
checked the bytes on disk each time:

    sentry-droid.crtr    beside  guard-droid.toml
    test-token.item      beside  sith-keycard.toml
    barrel.obj           beside  console.toml · crate.toml · footlocker.toml
    a03-annex.area       beside  a01-strongroom.toml · a02-vault.toml
    guard-chat.dlg       beside  console.toml

The `NEW CREATURE` dialog's path preview reads
`blueprints/characters/name.crtr` before you type, so the new extension is
visible at the point of authoring rather than only afterwards.

### ✓ And the half-converted package still opens — the claim the contract makes

**The manifest stayed `package.toml` and was edited in place.** Adding
`a03-annex` rewrote its `[order]` and did **not** leave a parallel
`package.pkg` behind. That is the *"still edits the old files"* half of
Loom's own commit message, working.

I then **restarted Loom and reopened the now-mixed package** from cold.
Everything lists: three areas across `.toml` and `.area`, both
conversations across `.toml` and `.dlg`, and the placeables palette shows
`barrel` (`.obj`) alongside three `.toml` placeables **with no visual
distinction between them** — which is what a transparent rename should
look like.

`base-rules` is still 26 `.toml` files, as ruled.

*(Cleaned up afterwards: all five test artefacts removed and the manifest
restored, so `strongroom-rebuilt` is back to the nine files TEST 083 left.)*

---

# 2 · THE GRENADE SAVE TYPE — right in the data, and nothing shows it

### ✓ Both modelled grenades carry a type, and it matches their own text

There are **12 grenades** on the shelf. Two carry a modelled effect with a
save, and both now name a kind. I checked them against the authority
sitting in the same row — each grenade's own description:

| grenade | its description says | modelled |
|---|---|---|
| **Poison Grenade** | `Save (Reflex): DC25 for no effect` | `{dc: 25, kind: 'reflex', on_save: 'none'}` ✓ |
| **Concussion Grenade** | `Save (Will): DC15 for no effect` | `{dc: 15, kind: 'will', on_save: 'none'}` ✓ |

**Type and DC both agree, verbatim.** That is a better answer than my
judgement of what "makes sense" for a grenade would have been — I did not
have to guess whether poison should be Reflex, because the source text
says so and the model matches it.

### ⚠ But there is no display, and it is one literal away

Coder asked me to confirm the type *displays* correctly. **It does not
display at all**, and the reason is specific rather than "unbuilt".

The one surface that shows a save to a player is a hazard going off.
`play_screen.dart:752` reconstructs the save and **does read the kind** —
`kind: raw['kind'] as String?` — so the value reaches the display code.
Three lines later:

```dart
final out = resolve(
  Check(type: CheckType.save, what: 'Save', against: dc),
  _dice,
);
```

`what` is the literal string `'Save'`, and `e.effect!.save?.kind` is
available on the line above it and unused. The printed line is
`goes off — d20 18 = 18 vs 15`, which is what TEST 080 recorded.

**Scoped negative, and here is where I looked:** I grepped `KOTOR-RPG-APP/lib/`
and `Loom/lib/` for any read of a save's kind — **zero**. The only
`Reflex` in the app is the character sheet's own save row
(`character_screen.dart:303`). Loom's hazard dialog writes `save dc` and
`on_save` and has no kind control at all.

### ⚠ And the kind looks load-bearing rather than cosmetic

The character sheet already carries **Fortitude, Reflex and Will** as
three separate values. The save roll above is built with no modifier
terms, so it comes out a bare `d20` — no character save bonus is applied.
**The kind is precisely the field that would decide which of those three
to add.** So this is not decoration waiting on a label; it is the
selector, now populated, with nothing reading it yet.

I am naming that rather than filing it: applying save bonuses may simply
be a later slice, and I did not find a ruling either way.

### ⚠ Nine more grenades name a save in their own text and have none modelled

The fix is correct on the population it reached. That population is two of
twelve. Every other grenade's description states a save that is not
modelled anywhere:

    Reflex DC15   CryoBan · Plasma · Frag · Ion · Thermal Detonator
    Will   DC15   Minor Sonic Detonator · Sonic Detonator · Sonic Grenade
    (none stated) Adhesive · one duplicate Plasma row

Those ten have **no `[[items.effects]]` block at all** — no save, no
damage, nothing mechanical — while carrying `Damage: Piercing, 20pts` and
`Save (Reflex): DC15 for half damage` in the text the extract already
reads. Frag, Plasma and the Thermal Detonator are the most ordinary
grenades there are.

So *"every real grenade's save shows a type"* is true if "real" means
"modelled", and the modelled set is Poison and Concussion. **Whether the
other ten are meant to be modelled is Coder's call, not mine** — I am
reporting the gap between the text and the model, not asserting they are
broken.

*(Also seen, not chased: two rows both named `Plasma Grenade`, different
resrefs.)*

---

## Smaller things seen while working

- **`a03-annex`'s unreachable warning is very good copy:** *"is in the
  manifest and no connection anywhere in this package leads to it, and it
  is not the entry area. Nothing in it can ever be reached — its
  placements, its conversations and its own way out included."* It names
  the consequence rather than the condition.
- The `NEW PLACEABLE` dialog, the creature dialog's write-once
  conversation field, and the red `There is no conversation here.` on a
  blank form are all **unchanged from TEST 083**. Not re-litigated here.

## ⚠ One thing that was mine, not the product's

A blind click sequence of mine placed **five barrels** into the annex
instead of opening the conversation form, because the module tree had
grown and shifted the `+` I was aiming at. My automation error, not a
defect — named because the artefacts existed for a while and are now
removed.

## What I did not do

- **Did not test `.doct` or `.door`** — no doctrine authored, and `door`
  is reserved with no reader, no writer and no file in any package.
- **Did not convert an existing package** to the new extensions — Coder
  said nothing on disk was changed, and I left it that way.
- **Did not exercise a grenade in play.** The shelf's grenade rows carry
  `base = None`; the playable article is a `charge`-base blueprint, and
  the save the player actually sees comes from a hazard. That is the
  surface I checked.
- TARGETING-01 and the weapon-damage sweep — not ready, not touched.

## State

- **`strongroom-rebuilt` restored** to the nine `.toml` files TEST 083
  left; all five test artefacts removed and `[order]` corrected. Verified
  by listing.
- **`locked-and-trapped` untouched** — opened and played, never edited.
- No new saves created; the four existing ones are as they were.
- All Loom and app PIDs killed by PID, confirmed gone.
