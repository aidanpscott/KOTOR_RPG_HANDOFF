# TEST 063 — Identity step baseline for PT-1719, and the blaster-rifle
# finding is not a Soldier thing

**Built against:** `run-app.sh` (always rebuilds). KOTOR-RPG-APP `a32f8d9`
(*PT-1715*), `pubspec.lock`'s `lodestar` still pins `resolved-ref
6fd064a516f0d3f70b89e75e0b8084d3b3b66392` (*PT-1713*), present and current at
`~/.pub-cache/git/Lodestar-6fd064a.../`. Loom `7e22d6b` (*PT-1713*) — not
launched this session, only checked untouched. Same three artifacts as
`TEST 062`, no drift since.

App PID `835270`, killed by PID when done. Coder's Loom `517968` checked
running, untouched, before and after.

---

## 1. Identity step, as it exists today — the PT-1719 baseline

Ran a fresh character (`ranged-detection`, Human Scout, "Carbine
Cross-Check") through to the Identity step and observed it directly rather
than recalling it from an earlier session's incidental screenshots, since the
ask was specifically to look again before Coder changes it.

**Order:** portrait first, name second — already true today, not something
`PT-1719` would be introducing.

**What holds the name field right now:** *not a popup.* Identity is three
sequential full-screen sub-steps, each carrying the same chrome as every
other chargen screen (`CHARACTER GENERATION` header, a titled sub-header
underneath):

1. **`IDENTITY`** — a portrait row (placeholder circle avatar, label
   "placeholder"), two lines of static text explaining portraits aren't
   drawn yet and importing game art won't fill it, and two buttons:
   `Cancel` / `Name ▶`.
2. **`IDENTITY — NAME`**, reached via `Name ▶` — a single-line text field
   labelled `name`, helper text *"A name is required. Everything else on
   this step is not."*, and `BACK` / `Story ▶`.
3. **`IDENTITY — YOUR STORY`**, reached via `Story ▶` — the assembled bio
   preview (portrait, name, species · class, abilities, origin/upbringing/
   profession tags, generated paragraph), with `Try another` / `CLEAR` /
   `BACK` / `Accept`.

So today: portrait-first is already the order, but "name" is a routed
step-screen in the same stack as Origin/Gender/Backstory/etc. — a full page
you navigate forward into and back out of with the same buttons every other
step uses, not an overlay drawn on top of another screen. Whatever
`PT-1719` means by "name last as a popup," the popup half is the part that
doesn't exist yet.

## 2. The blaster-rifle finding — reproduces on Scout too, so it's a
## weapon-reference problem, not a class-gate problem

Read the mechanism before testing further, to know what a second character
would actually be checking: `LedgerWriter.equipmentPayload` (`ledger_writer.dart`)
computes `weapon_r_1` from `resolveStartingWeapon(a?.weapon, …)` alone — `a`
being the class's own base starting array. The Equipment screen's *"TAKES
THE CLASS'S OWN melee UPGRADE"* choice is recorded as a separate
`grant_resolved` event carrying `item_unresolved: "this profession grants an
upgrade to what the class already carries, and nothing applies it yet — no
item was added"` (the comment above it says so explicitly: writing the
upgrade as an item would have "persisted a table's label as an item's name…
and no item was ever added"). **So the upgrade choice never touches
`weapon_r_1` at all, on any class** — `weapon_r_1` is always whatever the
class's stock array names, upgrade or not. Confirmed against
`base_rules/rules/class_arrays.toml`: exactly one class array's `weapon`
field contains the literal string `"Blaster Rifle"` — `soldier`'s. Every
other class names something else (`scout` → `Blaster Carbine`, `marksman` →
`Marksman Rifle`, etc.), so no other class was ever going to reproduce the
identical `blaster-rifle` path — the useful question was whether the same
*shape* of failure reproduces for a class whose own default weapon is
missing the same way.

Built a second throwaway character, same package (`ranged-detection`,
Human **Scout** this time — array weapon `Blaster Carbine · Short Sword`),
made the identical choice at Equipment (`TAKES THE CLASS'S OWN melee
UPGRADE`, the same option type Scout is offered too), entered play, bumped
into `starter.ranged.01` to start the fight. First line of the status log:

> `equips \`items/weapons/blaster-carbine\`, which will not open: There is
> no item here.`

Same shape, same wording, different weapon name — matching exactly what the
source predicts. **Confirmed: not scoped to Soldier.** The mechanism is
general — `weapon_r_1` always resolves to the class's stock array weapon
regardless of any Equipment-step choice, and it fails to open in any
package (this session's two fixtures included) that doesn't ship a
blueprint for that specific stock weapon under `blueprints/items/weapons/`.
`endar-spire` and `tester-probe` do carry a `blaster-rifle.toml`; neither of
this session's two test packages carries `blaster-rifle.toml` or
`blaster-carbine.toml`, which is why both fired. This reads as two separate,
nameable facts rather than one bug: **(1)** the melee-upgrade grant is
recorded but never resolved into an equipped item, on every class it's
offered to, and **(2)** a package that doesn't ship a class's stock weapon
blueprint gets no earlier warning than a runtime "will not open" the first
time that class's default gear is read in a fight — Loom's own `verify`
didn't catch this in either package (checked `ranged-detection`'s "5
problems" list from `TEST 062`'s Loom session; none of the five are about a
missing weapon blueprint).

---

## What I did not check

- Whether every class's stock weapon is missing from every package on the
  machine, or just these two Tester fixtures — did not audit `endar-spire`,
  `mixed-faction`, `taris-undercity`, or `two-enemies`'s
  `blueprints/items/weapons/` contents against all nineteen class arrays.
- Whether Loom's validator *should* flag a class array's weapon against a
  package's own item blueprints (i.e., whether (2) above is a validator gap
  Coder would want named separately from (1)) — flagged as two facts, not
  triaged into one fix or two.
- Whether the melee-upgrade grant ever gets applied for ANY existing
  character on the machine — did not check saves outside this session's own
  two throwaway characters.

## State

- `ranged-detection` — unchanged, `[entry]` still `a01-corridor`. New save:
  `carbine-cross-check.sav`.
- No other package touched — `base-rules`, `droid-melee-gate`,
  `endar-spire`, `mixed-faction`, `opportunity-attacks`, `taris-undercity`,
  `tester-probe`, `two-enemies` all confirmed untouched by mtime.
- The NWN install was not read or written.
- App process killed by PID; Coder's Loom `517968` checked running,
  untouched, before and after. Loom was not launched this session — nothing
  needed it.
