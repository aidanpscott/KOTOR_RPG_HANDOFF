# 007 · The player fights unarmed, and death is never said

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** Played, not read.
App `edaf92d` · `Lodestar 3a24455` · `Loom f5a5103`, via `./run-app.sh`.
**Pin checked first:** `pubspec.lock` `resolved-ref` = `3a24455bd449…` = engine
HEAD.

---

## ⚠ First, my own error, because it matters more than the finding

**I reported "I never saw my own attack line" as a limit of my coverage. It was
a defect reporting itself as one**, and you caught it, not me.

I had the evidence: **four fights, and the trooper's blows landed 18→17→14→12
so I knew mine were landing too.** I concluded "the log is one line and the
trooper acted last" — a plausible mechanism that happened to be wrong — and
filed it under my own sampling instead of asking why a computed line never
reached a frame.

**⚠ The lesson I am taking: a thing I never saw is a finding, not a gap, until
I can say why I did not see it.** "Unlucky sampling" is a claim and I did not
test it.

---

## ✓ All three slices confirmed, and one of them immediately paid

### 1 · My own attack line renders — and PT-1326's format is now verified on it

**Two lines, both present in the same frame:**

    unarmed · rolled 17 — d20 16 + attack 1 · needed 10 — hit · 1 damage · 17 left
    it is over — sith-trooper.command-deck.39: Blaster Rifle · rolled 11 — d20 9 +
    attack 2 · needed 10 — hit · 6 damage · -1 left

**Weapon named, damage stated, vitality stated — on the player's attack.** The
format that had only ever been verified on NPC attacks is now verified on mine.

### 2 · The bar is at the Class step, and it says what it is

Picking `Droid` and **not touching the class** — the path I took in `006`:

> `Soldier` · `Marksman` · `Brawler` · `Saboteur` **greyed out**, and the panel
> for the still-selected `Soldier` reads, in red:
> **"no droid takes this class — STARTING-EQUIPMENT-01 §3 opens nine of
> eighteen to a chassis"**, with `Accept` disabled.

**The four greyed are exactly the four I measured in `006`.** A rule at the
step where the choice is made, quoting the document. **And one of the nine
works:** `Astromech / T3-series / Scout` completed through Equipment to `OK`.

### 3 · The editorial notes are out of both tables — checked on screen, both halves

| | before | now, on screen |
|---|---|---|
| **droid** | `1 Sensor Probe — was Adrenal Stamina` | ✓ `1 Sensor Probe` |
| **organic** | `Ion Blaster — w_blaste_02, 50cr` | ✓ `Ion Blaster` · `2 × Computer Spike` |

**⚠ You were right that it was never a droid problem.** I checked
`class_arrays.toml` and `equipment.toml` as well: **0 raw resrefs remain in
either.** I built a Human Engineer specifically because that is the class you
named.

---

## ⚠⚠ WHAT READING MY OWN BLOW IMMEDIATELY FOUND: the player fights unarmed

**The very first line I could finally read says `unarmed`.**

That character is a **Human Engineer** whose Equipment step had just shown me:

    weapon   Ion Blaster

and I had also taken the profession's **melee upgrade**. **Neither reached the
fight.** I hit the trooper for **1 damage** with a fist while carrying a blaster.

### ⚠ And it is the same root as two things you already know about

    _playerCombatant()   builds handle · dex · con · vitality · budgets — and NO weapon
    play_screen:695      weapons: { for p in _here: p.combatant.handle: p.weapon }
    play_screen:727      weapon: f.weapons[f.playerTag] ?? unarmed

**The weapons map is built only from `_here`, the placed creatures. The player
is not a placement, so the lookup always misses and always falls back to
`unarmed`** — for every class, every array, every equipment choice.

⚠ **This is the third place the same root has surfaced.** The player has no
working line outside a fight because `_workingLines` folds `_here`. The player
was healed by walking out because it was not folded. **Now the player has no
weapon because it is not in `_here`.** `PT-1452` wired the trooper's blueprint
weapon through its placement — **and the player has no placement to wire.**

**Repro:** any class with a weapon in its array — I used Engineer — `Play`,
walk into the trooper, *"Stand aside."*, press `Down` once, read the first
line.

**⚠ And it makes one of the five promises untestable:** the Engineer's weapon is
an **Ion Blaster**, and the Species screen promises droids take *"1 Constitution
per hit"* from ion. **I cannot test ion vulnerability while the player cannot
hold the ion weapon.**

---

## ⚠ You asked me to push on death. Here is what a person understands: nothing.

**I died on purpose, then watched the screen rather than the log.**

### The moment of death

`Rell Vantt` drops to **-1 of 9**. On screen:

- **the marker is unchanged** — the same pale circle, same size, not dimmed,
  not hollow, not marked in any way
- the centred status line names **the trooper's** vitality, `17 of 18`. **Mine
  is not shown at all**
- the footer still reads **`Rell Vantt · arrows to move · esc to leave`** — it
  is still inviting me to move
- the only trace is the tail of a dim, wrapped, three-line log entry in the
  bottom-left corner: `… 6 damage · -1 left`, and the words before it are
  **"it is over"**, which reads as *the fight* is over, not *you* are

### ⚠ Then I pressed an arrow key twice, and the last trace disappeared

    a01-command-deck · 4, 3            Rell Vantt · arrows to move · esc to leave

**That is the entire screen.** The log line was replaced by the position
readout. **A dead character is now indistinguishable from a healthy one** — it
walks, the marker is identical, and nothing anywhere states a condition.

### ⚠ And the revive is announced retroactively, in the past tense, mid-next-fight

Walking back into the trooper and starting another fight finally prints:

    Rell Vantt: 1 of 9 — encounter a01-command-deck left you at -1 · revived at 1

**That is the first and only time the game tells me I died** — after it has
already un-died me, inside a line that exists only while a fight is running.

### What the loop feels like from the chair

> fight → die, told nothing → walk away, told nothing → fight again → be told
> *in passing* that I died and was revived at **1** → **die again to the first
> blow** → repeat.

**⚠ At 1 of 9 against a `1d12` rifle the next death is near-certain**, and I hit
that loop three times running with the Astromech in `006` before I understood
what was happening. **A player would not read this as a death rule. They would
read it as the game being broken.**

**I am not proposing the fix** — `STATE` already carries *losing a fight is
never stated* and *the player has no working line outside a fight* as open, and
`down → dead` as an unmade ruling. **What I can add is that the three combine
into something worse than any of them alone**, and that the revive — which is
presumably the deliberate part — is the one piece a player never gets told
about in time to use.

---

## The five promises — still none, and now one is blocked

**Across two more droids, an organic, and four more fights I met none of**
*constructed* · *ion vulnerability* · *shield projector* · *repulsorlift* ·
*fixed armature*. **It stays scope, not a defect.**

⚠ **But `ion` has moved from "not implemented" to "cannot be reached"** — see
above. If the player's weapon is ever wired through, ion becomes testable and I
will take an Engineer against something.

---

## ⚠ Scoped negatives

**Checked, real binary, 1280×720, `endar-spire`:** droid Class step with the
default untouched · `Astromech/T3-series/Scout` built through Equipment ·
`Human/Engineer/Hunter` built, played, killed, walked while dead, revived ·
both equipment tables read on screen · four fights.

**NOT checked:**

- **Whether any class's array weapon reaches play.** I saw `unarmed` for one
  class. **I read the mechanism in `play_screen` and it is class-independent,
  but I observed exactly one class**
- **The other three barred classes** — I saw `Soldier` and `Marksman` greyed in
  the list and read the other two from it; **I did not select each one**
- **Eight of the nine open classes** — only `Scout` was carried to `OK`
- **`[Lie]`, `[Human]`, `[Bribe]` replies.** Still only `[Persuade]` and
  `Stand aside.`
- **Whether `revived at 1` is stated anywhere I did not look** — I checked the
  board, the footer, the status line and the log. **I did not open a character
  sheet, because there is no way to**
- **`N1`/`N2`/the esc path**, per instruction. `N1` was plainly still present
- **Any window size but 1280×720**

**Not re-filed, per your list, though all three were in front of me:** the
feat groups, `Environmental Sealing`'s availability, and the hardcoded `Battle`
example — which an Astromech still reads on its own ability screen.
**Also still present and previously filed as `D3`:** the Equipment step's
*"TAKES THE CLASS'S OWN melee UPGRADE FROM §4a — Soldier → … Scout → … Duelist
→ …"* label, which the Engineer showed me again today.

**No exception, no overflow, nothing red** in any run log.

---

## Data

**Added `saves/rell-vantt.sav`** — the Human Engineer, **dead at -1 and
revived at 1**, carrying the `unarmed` fight in its log.

`t3-m4-probe.sav` (the `STR 8` boundary) and `t3-k9.sav` (the `PT-1456`
before-and-after) are both untouched and both still load. **I deleted nothing
and fixed nothing.**
