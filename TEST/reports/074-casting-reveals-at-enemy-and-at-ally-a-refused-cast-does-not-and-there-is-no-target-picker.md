# TEST 074 — PT-1845 confirmed live: casting reveals you, at an enemy AND
# at an ally, and a refused cast leaves you hidden with the pool untouched
# — plus the thing that made the ally case hard to reach: there is no
# target picker, so who a power is aimed at is the room's authoring order

**Built against:** `run-app.sh` (always rebuilds), two runs. Run 1 started
12:43:27, run 2 started 12:50:09; local `KOTOR-RPG-APP` HEAD at both was
`068ecfc` (12:38:51, *PT-1845: casting gives you away*) — the commit under
test. `d2d28d0` (12:50:55, *PT-1846: the fallen say so in their own
words*) landed 46 seconds after run 2 began and is in neither build.
`pubspec.lock` pins (`ref: main`, floating): `lodestar`
`17bba42abe4f40940e78c06d848d7e4f1700544d`, `lens`
`e79bc066233fabc7776c8b94737029646d762e6e`, both confirmed present as
checkouts. `check_shelf.py` at session start: `✓ 25 rules files, all
identical to what the extracts generate`.

App PIDs `753972` (run 1) and `957073` (run 2) killed by PID, both
confirmed gone. Coder's Loom (`12445`/`12443`) checked running, untouched,
throughout. A third `kotor`-matching window on the display belongs to a
Firefox process (`161799`) that is not mine — left alone.

**Character:** Human **Jedi Consular** ("Veya Roarke" run 1, "Oreth Tarn"
run 2), WIS 18 / CON 17, **Stealth rank 2**, **force 11 of 11**, powers
**Force Push** (6f) and — deliberately — **Force Crush** (30f), chosen so
the pool could never pay for it.

*(Incidental, and it closes a gap TEST 069 had to leave open: the player's
row does render the **Force wing** and a `force 11 of 11` line. Also, per
`29cdc71`, the `hidden` indicator now sits on the **name line** — the row
reads `Veya R… hidden`, truncating the name to make room.)*

---

## 3. A refused cast does not reveal, and costs nothing — CONFIRMED

Taken first, because a refusal that preserves cover is what lets one hide
serve two checks. Hidden, on my turn, opened the cast menu with `f`. The
menu itself pre-warns: **`cast — 1 Force Push 6f · 2 Force Crush 30f ⚠ you
have 11 · esc`**. Chose Force Crush:

- Screen said **"Force Crush costs 30 and you have 11"**
- The row still read **`hidden`**
- The pool still read **`force 11 of 11`** — nothing spent, ceiling
  undegraded

So the refusal is complete: no cast, no cost, no reveal. This is the same
shape as the swing defect from TEST 073, and here the placement is right
the first time — the reveal sits past every refusal, beside the spend.

## 1. Casting at an enemy reveals — CONFIRMED

Same hide, same turn. Chose Force Push:

**`Force Push · 6f — 11 → 5 · ceiling −1 to 10 · at starter.corridor.01 ·
⚠ Force Push does not say what it may be aimed at · …`**

Pool 11→5, ceiling degraded to 10, target named as `starter.corridor.01` —
an enemy — and **the `hidden` marker was gone** from the row.

## 2. Casting at an ALLY reveals identically — CONFIRMED, but see below

This one could not be driven as shipped, for a reason worth its own
section (§4). `_cast` has **no target picker**: it takes the *first*
non-player combatant in the room's contents that is in the fight, and
`companion-fixture`'s `a01-corridor` declares `starter` first, so every
cast in that room aims at the enemy.

To reach the ally case honestly I temporarily reordered **my own** fixture
so `mate.corridor.02` (the `role = "henchman"` companion) is declared
before `starter`, relaunched, and rebuilt an identical Consular. Hidden,
cast Force Push:

**`Force Push · 6f — 11 → 5 · ceiling −1 to 10 · at mate.corridor.02 · ⚠
Force Push does not say what it may be aimed at · …`**

Target named as **`mate.corridor.02` — my own companion** — pool spent
identically, and **the `hidden` marker was gone**. Casting at an ally
breaks cover exactly as casting at an enemy does, which is the ruling
(*"a hidden character healing an ally is exactly as visible as one
attacking an enemy"*). The fixture was reverted immediately afterwards and
re-read to confirm the shipped order is back.

## 4. ⚠ Worth flagging: a power is aimed by authoring order, not by choice

Not a PT-1845 defect — the reveal is target-independent *by construction*,
one line past every refusal with no branch on who `at` is, which is why
§2 holds — but it is what §2 ran into, and it is visible in the product:

- There is **no target picker**. `_cast` takes `target.first` from the
  room's placements and the screen's own comment says why (*"inventing a
  target picker to aim at the only thing present would be building
  ahead"*). Reasonable when the only thing present is an enemy.
- But the filter is `!x.isPlayer` — which **includes your own party** —
  and the relation handed to the gate is hardcoded `Relation.enemy`. So a
  companion who happens to be declared first in a room is selected as the
  target of an offensive power and evaluated *as if she were an enemy*.
  That is exactly what I saw: Force Push aimed at Mate, with the gate
  saying only *"Force Push does not say what it may be aimed at"* rather
  than anything about her being on my side.
- Today the consequence is aim rather than harm: Mate read **46 of 60**
  both before and after the cast, so no damage landed — power effects
  don't appear to resolve yet. The day they do, this is friendly fire
  chosen by a `[[contents]]` ordering rather than by the player.

Naming it because it is the mechanism §2's confirmation depended on, and
because it will stop being cosmetic the moment effects apply.

---

## What I did not check

- The other two refusal paths named in the source — **no target at all**
  (`'— there is nothing here to aim it at'`) and **gate excluded**
  (`'… — nothing spent'`). The first needs no fight, and hiding requires
  one (and now ends with it), so the two states cannot be combined; the
  second needs a power the gate refuses against `Relation.enemy`, which
  neither of my two picks was. Both sit above the reveal in the same
  straight-line function as the affordability refusal I did drive.
- Whether a power's **effect** actually resolves — the derivation line
  quotes the power's description, and the ally's vitality did not change.
- Whether casting spends the **Action**: I hid (which spends it) and then
  cast twice in the same turn, so it appears not to. Observed, not judged
  — `ACTION-ECONOMY-01` may well rule it that way.
- `d2d28d0` (*the fallen say so in their own words*), which landed after
  my builds and appears to address the "a fallen combatant reads as
  `hidden`" wrinkle the casting commit mentions. Not in scope and not in
  my build.

## State

- `companion-fixture` (mine) — `a01-corridor.toml`'s `[[contents]]` order
  was temporarily changed for §2 and **reverted**; re-read afterwards to
  confirm `starter` → `mate` → `chaser` as shipped. Only the file's mtime
  differs; the content matches. Nothing else touched.
- Two saves created ("Veya Roarke", "Oreth Tarn"), neither cleaned up —
  ordinary Tester artifacts.
- Both app PIDs killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) checked running, untouched, before and after.
