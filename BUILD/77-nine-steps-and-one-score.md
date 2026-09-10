# BUILD 77 — `PT-1528`: nine chargen steps feeding a fight that read one score

**824 green** — Lodestar 378 · Lens 5 · Loom 131 · app 309.

---

## ⚠ WHAT THE CORPUS SPECIFIES — and it assembles it itself

`ATTACKS-01 §12.5` exists **because no document assembled the expression**, and
it says so in those words:

    attack   d20 + base attack bonus + ability modifier + Weapon Focus
                 + declaration modifier + situational
    damage   weapon dice + ability modifier + Weapon Specialization
                 + declaration modifier

- **Melee and lightsaber use Strength. Ranged uses Dexterity.**
- **Melee adds Strength to damage. RANGED ADDS NOTHING** — `EQUIPMENT-01 §1`,
  and the asymmetry is the rule: a blaster's damage is the weapon's.
- **Two-handed adds 1.5× Strength.** Rounded **down** — the expression gives no
  rounding, and rounding a *bonus* up is the generous reading. Nothing
  authorises generosity.
- **Lightsabers add Strength for this playtest** — `§12.5`'s own flag, worth ±3
  a hit on every Jedi.

**All of that is built**, term by term, with `Term.from` carrying the source —
so `PT-1326`'s derivation line writes itself instead of arriving as a total
nobody can inspect. **A test asserts `resolve()` keeps the sources**, because
that is the distinction you asked me to get right once.

⚠ **The weapon kind comes off `EQUIPMENT-01`'s own `section` column** —
`Melee - base weapons` · `Ranged` · `Lightsabers` — **not from a name.**
Guessing "blaster" out of a name is how a rule reaches a weapon called *Blaster
Sword*.

## ⚠⚠ WHERE IT IS SILENT — two rows, and each had a constant in its place

### `defence` — **no expression exists anywhere**

`CHARACTER-RECORD-01 §3` gives the inputs — *classes + abilities + feats* — and
**no document states the sum.** **No class carries a defence column.** Features
grant `+N Defence` and beasts carry an `AC`, **so the pieces assume a base that
was never written.**

> **⚠ The only defence sum in the corpus is KOTOR's own:** *"Defense Breakdown:
> 18 = base 10 + dex mod 4 + class 4"* — `TRACE-85`, quoted in **three**
> documents **to argue that a derivation should be SHOWN.** Never adopted as a
> rule.

**So `defence: 10` stays, and the line above it now names the gap.** Adopting
KOTOR's arithmetic because it is the only number in sight is precisely the
"modifier invented" you said you would rather not have. **Dexterity still buys
no defence, and that is now a stated absence rather than a hardcoded 10.**

### `base attack bonus` — **`§12.5` names it and we do not have one**

`CLASSES-STANDARD-PHB` says what `rate` is: *"how fast you acquire **attack
picks** — `Combat`, `Middle` or `Specialist`."* **A count of chains, not a
bonus.** The per-level `bab` column survives in *some* class progressions and
not others — source residue.

**The engine takes it as nullable and omits the term.** A zero would claim it
was computed and found to contribute nothing.

---

## ⚠⚠ AND REMOVING THE INVENTED CONSTANTS CHANGED THE GAME, VISIBLY

`fight.dart` swung at `Term('attack', 2)`. That was made up. A Sith Trooper's
abilities are **all tens**, so its attack is now **+0 against defence 10** — and
a `Str/Dex 14` soldier **wins the fight it used to lose.**

⚠ **`who_is_here_test` needed the player to die and the player stopped dying.**
The fixture loses by being **unarmed** now — *not* by handing the trooper its
invented bonus back. **The fixture changed because the game changed, and the
game changed because a constant left.**

> **That is the base-attack-bonus gap biting rather than a regression.** Every
> creature is markedly worse at hitting until something supplies that term.

⚠ **`Combatant` did not carry Strength.** `combatantFrom` computed the modifier
and threw it away — Dexterity and Constitution were kept **because something
already needed them**, and this was dropped for want of a consumer. It is the
same shape as `character.moved`, one field down.

⚠ **One function, both sides.** `play_screen` and `fight.dart` are exactly the
pair a rule gets applied to one of, so `§12.5` lives in `Lodestar` and both call
it.

## Still open

- ⚠⚠ **`defence` needs an expression** — inputs named, arithmetic nowhere.
  **The owner's.**
- ⚠⚠ **base attack bonus needs a source** — or `§12.5`'s first term should be
  struck and `rate`/attack picks named in its place.
- ⚠ **A creature's weapon kind is not known in `fight.dart`** — `weapons`
  carries a `Weapon`, which has no section. Absent reads as melee, which *adds*
  Strength; named in `weaponKinds` rather than left silent.
- ⚠ `PT-1509`'s perception half; `tester-probe`'s failure node; no `unlink`
  button; `PT-1484`, `PT-1485`, effect columns, 45 annotation cells.
