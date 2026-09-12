# TEST 065 — taris-undercity's stock weapons equip cleanly, and a second,
# unrelated weapon defect turned up checking it

**Built against:** `run-app.sh`/`run-loom.sh` (always rebuild). KOTOR-RPG-APP
`0458965` (*PT-1732 — the name is a full-screen step again, pre-filled, with
a button*). `pubspec.lock`'s `lodestar` pin unchanged since `TEST 062`
(`6fd064a`). Loom `dd0c26c` (*PT-1730 — the Builder computes the stock-weapon
paths and hands them over*). Both HEADs moved again while I was writing this
up (KOTOR-RPG-APP to `6d51fbf`, Loom to `e508480`) — named for precision, not
because either move touches this report's subject by its own commit message.

App PIDs `861464`/`861746` (transient)/`835270` region — final: `861464`,
killed by PID. Loom PIDs `861170` and `861168` (the launcher wrapper), both
killed by PID. Coder's Loom `517968` checked running, untouched, before and
after.

**The shelf, confirmed directly:** `taris-undercity/blueprints/items/weapons/`
now carries all eleven files `endar-spire` ships — diffed by name, matches
exactly. No commit touches this, as flagged — it's on-disk data, invisible
to `git log`.

---

## Method — `taris-undercity` ships no creatures, so I had to build a fixture

Both of `taris-undercity`'s areas (`a01-sewer-junction`, `a02-rakghoul-warren`)
are genuinely empty — no `[[arrivals]]`, no `[[contents]]`, matching the
package's own summary, *"made to give the library a second tile."* The
weapon-resolution note is fight-gated **by design** — `play_screen.dart`'s
own comment: *"why you have no weapon belongs beside the swing, not on the
screen for the whole walk"* — so there is no way to observe it without a
fight, and no way to have a fight without an opponent.

I added one temporary, clearly-marked fixture: an `[[arrivals]]` and one
`punch.bag.01` placement (a stock human Soldier blueprint, `punch-bag.toml`)
to `a01-sewer-junction.toml`, used it for all three characters below, then
restored both files from a backup taken before the edit and deleted the
blueprint. Diffed clean against the pre-edit backup afterward. This is the
same category of action as switching a package's `[entry]` in earlier
reports — a Tester fixture, built, used, and reverted — not left in the
package.

**Full-coverage cross-check, before playing anything:** opened
`taris-undercity` in Loom and ran verify. `PT-1730`'s own new validator
(`startingWeaponMissing`) checks **every one of the nineteen class arrays**
against this package's item blueprints regardless of what's placed —
read the source (`validateStartingWeapons` in `package_validate.dart`) to
confirm this before trusting the silence. Result: **`2 problems`, both the
standard "no connection" notices for the two empty areas — zero
`startingWeaponMissing` faults.** That's full-coverage confirmation the
shelf-copy fix covers every class's stock weapon file, not just the ones I
went on to play-test.

## Play-tested three classes not touched in TEST 063 (Soldier, Scout)

**Marksman** (`Marksman Rifle · Hold Out Blaster`) — clean. Bumped into
`punch.bag.01`, attacked: `Marksman Rifle` resolved, hit for real damage, and
the guard's own attack line even read `+ closed on a ranged weapon 2` —
confirming the engine correctly read it as a ranged weapon, not just that
the file opened.

**Engineer** (`Ion Blaster`) — the file opens (no `will not open` message,
confirming the shelf fix), but attacking with it silently fell back to
unarmed (`1d3`, "adds nothing to a ranged weapon"), and the fight's opening
recap line said why:

> `` `Ion Blaster` has damage `1d4 + 1d10 vs droid`, which is not a single
> die expression. PT-1452 reads `NdM` and a flat number; anything else is
> refused rather than guessed at. ``

Traced this to `base-rules/rules/equipment.toml` line 133:
`damage = "1d4 + 1d10 vs droid"` — a compound, conditional damage string
the engine's own dice parser (`PT-1452`, "NdM or a flat number") cannot
read. **This is a different defect from TEST 063's** — not a missing file,
a malformed value in a field that *is* found — and it's in `base-rules`
itself, not anything the shelf-copy touched. Named because it means
"equips cleanly" isn't quite true for Engineer yet: the weapon opens, but
swinging it is functionally the same as being unarmed, silently.

**Jedi Guardian** (`Training Lightsaber blue`) — clean, and confirmed past
just "no error message": attacked, and the log read
`Training Lightsaber · rolled 18 … hit · damage 7 — 1d8 6 + Strength 1` —
the actual weapon, correct dice, correct Strength addition for a melee
weapon. Chosen specifically because a lightsaber is a third item
*section* (`Lightsabers`, neither `Ranged` nor `Melee - base weapons`),
not just a third class.

---

## What I did not check

- The other fifteen class arrays' actual play-time behavior — covered only
  by Loom's `startingWeaponMissing` validator (full coverage for file
  *existence*), not by an in-play attack the way Marksman/Engineer/Jedi
  Guardian were. Worth naming since Engineer's finding shows file-exists is
  not the same guarantee as damage-resolves.
- Whether any other base-rules weapon besides `ion-blaster` carries a
  similarly malformed `damage` string — did not audit
  `equipment.toml`'s other ~40 rows for the same shape.
- Droid designations — told explicitly not to chase this, and didn't.

## State

- `taris-undercity` — confirmed byte-identical to a pre-edit backup after
  the session; the temporary `punch-bag.toml` blueprint was deleted. No
  saves were created in this package this session (never reached a save
  point — each of the three characters was played, checked, and abandoned
  via `Exit to Library`/`New Game` without saving).
- No other package touched — `base-rules`, `droid-melee-gate`,
  `endar-spire`, `mixed-faction`, `opportunity-attacks`, `ranged-detection`,
  `tester-probe`, `two-enemies` all confirmed untouched by mtime.
- The NWN install was not read or written.
- Every app and Loom process I started was killed by PID; Coder's Loom
  `517968` checked running and untouched before and after.
