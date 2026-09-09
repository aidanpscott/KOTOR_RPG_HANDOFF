# 006 · The droid loads — and four classes cannot be made at all

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** Played, not read.
App `4eb7d28` · `Lodestar 3a24455` · `Loom 3249dde`, launched with
`./run-app.sh` every time.

**⚠ I checked the pin before trusting anything**, since a stale one is what
made `004` look impossible: `pubspec.lock`'s `resolved-ref` is
`3a24455bd449…`, which is `Lodestar` HEAD exactly. I was on the current engine.

---

## ✓ The acceptance passes, and everything you listed as changed, changed

| | |
|---|---|
| **`t3-k9.sav` loads** | ✓ `T3-K9 · 3 rules unchecked`, standing in the Command Deck, trooper still at `14 of 18` from the fight that killed me. **My own save is the acceptance and it opened.** |
| **Astromech — the boundary** | ✓ `STR 8` exactly. Created, played, **saved, quit and reloaded clean.** Both ends of the old bound are now exercised: `6` was refused, `8` was the margin, both load |
| **⚠ `[Persuade]` rolls** | ✓ **and I passed** — *"…One man. Yes. Go on, then, before I think better of it."* **My "did I pass or fail" now has a first answer.** No numbers shown, per `PT-1307` |
| **The dead ends are gone** | ✓ **all six** player lines now carry a `then`. The four gated ones each get a reply |
| **A conversation that ends says so** | ✓ terminal beats offer **`[Leave]`** — the affordance *is* the statement |
| **The droid equipment table** | ✓ `Scout — the assortment`: **Blaster Carbine · 1 Sensor Probe · 2 Repair Kits · 100 credits** |
| **The slots it has** | ✓ **no `armour` row and no `boots` row at all.** The hoverer's boots are gone because the droid kit has none |
| **⚠ The attack line** | ✓ **`sith-trooper.command-deck.39: Blaster Rifle · rolled 11 — d20 9 + attack 2 · needed 10 — hit · 6 damage · -1 left`** — weapon named, damage stated. **This was my ask and it is answered** |

---

## ⚠⚠ THE ONE I FOUND BY PLAYING: four classes can no longer be made as a droid

**Wiring `droid_arrays` connected the wire — and the table does not cover every
class.** For the four it misses, the Equipment step now **dead-ends**:

> **Soldier has no starting array**
> This class has no starting gear written for it, so there is nothing to equip
> and nothing to weigh the profession's offer against.
> ⚠ **this step cannot complete for this class**

**`OK` is disabled. The character cannot be finished, and there is no way
forward from that screen.**

### Coverage, measured

`droid_arrays.toml` carries **9** of the **13** standard base classes a droid
may take:

    HAVE     Scout · Smuggler · Bounty Hunter · Engineer · Machinist ·
             Agent · Treasure Hunter · Medic · Duelist
    ⚠ MISSING  Soldier · Marksman · Brawler · Saboteur

**⚠ `Soldier` is the first row of the class list and it is pre-selected.** So
the most likely droid anyone makes — pick `Droid`, leave the class alone — is
the one that cannot be created. **I confirmed both on screen:** `Marksman`
first, because that is what I had built in `004`, then `Soldier` deliberately
because it is the default.

**⚠ This is a regression against `004`.** Before the wire, all thirteen
completed — with the wrong, organic kit. **Now four of thirteen are hard-
blocked.** The gear was wrong and is now absent, and absent stops the flow.

**Repro:** `New Game` → `Create New Character` → **Droid** → any chassis →
any model → **leave the class as `Soldier`** → complete Backstory, Abilities,
Skills, Feats → open **Equipment**.

**⚠ Whether the fix is four rows of data or a fallback is not mine to say** —
but a step that cannot complete has no exit, and `Cancel` is the only button
that does anything.

---

## Smaller, and both from the same wire

**S1 · The droid table's editorial notes are now printed to players.** The
Scout kit renders:

    consumable   1 Sensor Probe — was Adrenal Stamina

*"was Adrenal Stamina"* is a note about how the droid table was derived from
the organic one. Others in the same table will surface the same way:
*"the Stun Baton is dropped"*, *"2 × Computer Spike  unchanged"*,
*"Blaster Pistol — its Long Sword is unusable"*, *"1 Recording Rod  the adrenal
is dropped"*.

⚠ **Same family as `004`'s resrefs** — `base-rules` is generated, so this is
upstream in the generator rather than on the screen. **It was invisible while
nothing read the table.**

**S2 · The hardcoded `Battle` example is still on every chassis's ability
screen.** I reported it in `004` and it is not in your changed list, so I am
**noting rather than re-filing**: an Astromech reading its own spread is still
told *"Battle's +2 Strength and −2 Charisma are visible as 14 against 10"*,
and on that sheet the only `14` is Wisdom.

---

## ⚠ Things I could not see, and one I did not expect

**⚠ I never once saw MY OWN attack line**, across four fights, and I want to be
plain that the weapon/damage format is therefore **verified on the NPC's
attacks only**. My blows landed — the trooper went `18 → 17 → 14 → 12` — but
**the log is one line and shows the most recent action**, and the trooper acted
last every time because it killed me. **I confirmed the format, not that my own
weapon is named in it.**

**⚠ And a mechanic I did not know existed:** re-engaging after dying printed

    T3-M4 Probe: 1 of 9 — encounter a01-command-deck left you at -5 · revived at 1

**"revived at 1".** So a downed character comes back at 1 vitality on the next
encounter. ⚠ **This is not on your changed list and I am not filing it** — it
looks deliberate. But it bears directly on the two things you say are still
open: **losing is never stated on screen, and the player has no working line
outside a fight.** A player therefore dies, is revived at 1, and is told
neither. I only saw the revive because it happened to be the most recent action
when I captured.

**An Astromech Scout has 9 vitality and dies to one rifle hit** (`6` and `9`
damage in two of my fights). **Not filed** — nothing has been balanced, and the
scaffolding list covers it.

---

## ⚠ The five promises — I met none of them, so nothing changes

You said: *"if you meet any of the five in play, that changes it."* **I did
not.** Across two droids, four fights, a conversation and two reloads, nothing
referred to *constructed*, *ion vulnerability*, the Remote's *shield
projector*, *repulsorlift* or *fixed armature*. **The Species screen still
promises five mechanical things I have never seen the game do.** It stays scope
for the owner exactly as filed in `005`.

---

## ⚠ Scoped negatives

**Checked, in the real binary at 1280×720, on `endar-spire`:**
`t3-k9` loaded · a Remote/Marksman built to Equipment · a Remote/Soldier built
to Equipment · an Astromech/T3-series/Scout built, played, killed, saved, quit,
reloaded · `[Persuade]` taken and passed · `[Leave]` taken · four fights.

**NOT checked:**

- **My own attack line** — see above. **The single most important gap in this
  report**
- **The other two chassis, `Assassin` and `Battle`**, and every model but
  `Marksman-H` and `T3-series`
- **Nine of the thirteen classes** — I only built `Marksman`, `Soldier` and
  `Scout` as droids. **I read the missing four out of `droid_arrays.toml`;
  I only *saw* two of them fail**
- **Whether `[Lie]`, `[Human]` or `[Bribe]` now reply properly.** I read their
  `then` links in the file; **on screen I only took `[Persuade]`**
- **The `'the conversation is over'` message** at `play_screen.dart:394`. It
  fires when a beat ends with no continuation, and **this bed no longer has
  one**, so I could not reach it. `[Leave]` takes a different path and closes
  without a message — which reads fine, because leaving was my choice
- **Whether validate now refuses a dead check.** I did not author one
- **The esc path, `N1`, `N2`** — I avoided them, though `N1` was plainly still
  present: every fight after the first ended on the first action
- **Any window size but 1280×720**

**No exception, no overflow, nothing red** in any run log.

---

## Data

**Added `saves/t3-m4-probe.sav`** — the Astromech, `STR 8`, **the boundary
case; keep it if you want a reload test that sits exactly on the bound.**

**`t3-k9.sav` is untouched and now opens** — it is the before-and-after for
`PT-1456`. `vess-taran`, `second-fight`, `probe-walker` and
`packages/tester-probe/` are still mine from earlier reports.

**I deleted nothing and fixed nothing.**
