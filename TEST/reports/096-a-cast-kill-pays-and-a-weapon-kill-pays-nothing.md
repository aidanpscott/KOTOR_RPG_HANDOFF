# TEST 096 — THE LOOP RUNS, END TO END, FOR THE FIRST TIME. A kill paid
# `3000` XP, a rest took `level 2 — jedi_consular`, and both are in the ledger.
# CR 0 paid its real `100` at level 1 and recorded itself as `cr: 0.0`. A LOST
# fight paid nothing even though I had killed two enemies inside it. Force
# Plague rolled a real Fortitude save: `d20 20 = 18 vs 25`.
# ⚠⚠ AND THE HEADLINE DEFECT, ISOLATED TO ONE VARIABLE IN ONE FIGHT: **a kill
# made with a WEAPON pays nothing. A kill made with a FORCE POWER pays.** Two
# priced enemies, same fight, same fight-end, both with `character.died` — the
# one I shot with Force Lightning paid 125 and the one I hit with a vibrosword
# paid nothing at all. `a_kill_pays_test` is green because its only live
# fixture kills with Force Lightning.
# ⚠⚠ AND THE LEVEL ONLY LANDS AFTER A RELOAD. Two rests in the session that
# earned the XP did nothing and said nothing; loading the save and resting once
# took the level immediately.
# ⚠⚠ AND THE PRODUCT WROTE A SAVE ITS OWN READER REFUSES. Two of 112 saves on
# this disk are `Damaged save: the contents could not be unpacked` — and they
# still appear in `Load Game`, because the listing only reads the header.

## Build state

    KOTOR-RPG-APP   38c7163  PT-2235 — built and measured from this
    lodestar        25086d6  — HEAD's own pin, and the pub-cache checkout
    lens            32b77e3

    ✓ FRESH — built from exactly this source at 09-16 19:43:35

Both trees were clean at the start and the lock matched Lodestar's HEAD.
⚠ HEAD moved under me during the run — you are at `852c52a`/`bf78e6d` (PT-2238)
now. Nothing below is from that. `check_shelf.py` green at both ends, **29**
rules files, the new one being `xp_awards.toml`.

⚠ **Routing note:** you said the Dark Healing self-cast fix is *"ruled but not
yet built"*. It is built — `38c7163 PT-2235: a negative permits, and Dark
Healing can be aimed at its caster` is HEAD. I did not test it; it is only that
the note and the log disagree.

**And TEST 095's two findings are closed.** `PT-2224` cites it by name —
*"`progress.level` has no writer"* — and a level-12 Consular now loads where
nothing above level 1 could exist before. The `save_kind` gap is gone too: 22
of 22 damage powers that state a save branch can now fire, where 18 could not.

---

# ⚠⚠ THE FINDING — A WEAPON KILL PAYS NOTHING

One fight, two priced one-vitality enemies, killed seconds apart:

    x-cr0.probe.01   killed by a VIBROSWORD BLOW
    x-cr1.probe.02   killed by FORCE LIGHTNING

and the ledger the product wrote:

    character.died        {subject: x-cr1.probe.02, …}
    character.died        {subject: x-cr0.probe.01, …}
    encounter.ended       {subject: x-cr1.probe.02, vitality: -5}
    encounter.ended       {subject: x-cr0.probe.01, vitality: -23}
    character.xp-awarded  {subject: Both Ways, amount: 125, from: x-cr1.probe.02, cr: 1.0, level: 1}

**One award, not two.** Both died, both were priced, both are named in
`encounter.ended`, and only the one killed by a cast paid. The fixture is one
variable away from itself.

### The mechanism, and the source says it out loud

`_xpFor` builds `beaten` from the fight's dead enemies and asks `_challengeOf`
for each one's CR. `_challengeOf` looks the handle up **in `_here`** —

    double? _challengeOf(String handle) {
      for (final p in _here) {
        if (p.combatant.handle == handle) return p.character?.challenge;
      }
      return null;
    }

— and `_here` is exactly where the dead are not:

    line  601  ⚠ CREATURES STILL COME THROUGH `_here`, because the DEAD are removed
    line 4971  `_here` never holds the DEAD any more — the filter …
    line 5439  `_theFallenLeaveTheBoard` drops a dead creature from `_here` …

`_theFallenLeaveTheBoard()` is called at `5107`, `6368` and `7117`, and `7117`
is on the fight-end path **above** the award block. So by the time `_xpFor`
asks, the body is gone from `_here`, the lookup returns null, and `awardsFor`
skips it through the one branch built to be kind:

    // ⚠⚠ ABSENT IS NOT ZERO … A creature whose blueprint never priced it
    // pays NOTHING
    if (cr == null) continue;

⚠ **The bug is hiding inside a correct rule.** `PT-2233` built that refusal
deliberately and `_challengeOf`'s own comment already knew the risk — *"NULL IS
… the answer for a handle nothing is holding too"* — it simply did not follow
that at fight end **every** beaten handle is a handle nothing is holding. An
unpriced creature and a dead one are now indistinguishable.

### Why the guard is green

`a_kill_pays_test.dart` asserts the live path properly — `expect(paid,
hasLength(1))`, the amount, the `cr`, the `from`. It passes because its killer
is a Consular 20 casting Force Lightning, which your own commit message says in
as many words. **The one path it exercises is the one path that works.** A
player hitting something with a sword is the case nothing covers.

### What I measured around it

Before concluding this I checked that the fixture and the pure function were
not the problem, through the product's own readers:

    BLUEPRINT x-cr0  challenge=0.0     TABLE level 1 cr 0.0 = 100
    BLUEPRINT x-cr1  challenge=1.0     TABLE level 1 cr 1.0 = 125
    BLUEPRINT x-cr8  challenge=8.0     TABLE level 1 cr 8.0 = 400
    BLUEPRINT x-none challenge=null    TABLE floor = 25
    AWARDSFOR = [(amount: 100, cr: 0.0, from: x-cr0), (amount: 125, cr: 1.0, from: x-cr1)]

The blueprints are priced, the table answers, and `awardsFor` pays the priced
pair while skipping the unpriced one. Everything is right except the arrival.

⚠ And I ruled out the blueprint extension: your bed uses `.crtr` and my first
fixture used `.toml`. I rebuilt every character as `.crtr`, deleted the `.toml`,
and a weapon kill still paid nothing.

**Scale of it in play:** across two areas and three runs, **eleven** weapon
kills paid nothing between them. Six of those were in one won fight whose
`encounter.ended` names all six bodies, with zero `xp-awarded` in the file.

---

# ⚠⚠ AND THE LEVEL ONLY LANDS AFTER A RELOAD

With `3000` XP in the ledger — well past the `1000` that level 2 costs —
**two rests in the same session did nothing**:

    you rest a day. Nothing needed mending.
    you rest a day. Nothing needed mending.

No level, no refusal, no sentence saying why. I loaded the same save and rested
once:

    you rest a day. Nothing needed mending. · level 2 — jedi_consular

    character.xp-awarded  {subject: Level Up, amount: 3000, from: x-cr9.probe.02, cr: 9.0, level: 1}
    character.levelled    {level: 2, class: jedi_consular, xp: 3000}

`PT-2224`'s own note names the cause — *"`widget.character` is re-replayed only
after the append reaches disk"* — and `_persist` fires its append through
`unawaited(...)`. Within the session that earned the XP the screen is still
holding the record it loaded with, so `_rest` reads `xp: 0` and quietly takes
nothing. **The loop works; it just cannot be completed in one sitting**, which
is precisely the thing a player would try first.

⚠ A rest that takes no level says the same sentence as a rest that had nothing
to do. `_rest` already refuses mid-fight with a reason; this path has none.

---

# ⚠⚠ A SAVE THE PRODUCT CANNOT READ BACK

Run through `readSave`, **2 of 112** saves on this disk fail:

    FAIL xp-two.sav       812B  Damaged save: the contents could not be unpacked.
    FAIL kaeda-sabek.sav  903B  Damaged save: the contents could not be unpacked.

`xp-two.sav` was written by the app minutes earlier, in the run with four kills
and a walk-away; it is still damaged after the app exited cleanly, so it is not
a half-finished write I caught mid-flight. **`kaeda-sabek.sav` is not mine** —
it was on the disk before this session, which is what says this is not an
artefact of my authored fixtures.

Decoded by hand, the file is one **complete, valid** gzip member holding the
original 18-event log, followed by **149 bytes that are not gzip**.

⚠ Mechanism, stated as a hypothesis rather than a finding: `SaveStore.write` is
a plain `writeAsBytes(bytes, flush: true)` — correct on its own, and truncating
— but `_persist` dispatches through `unawaited(widget.onAppend?.call(keep))`
from **eight call sites** with nothing serialising them, and every append
rewrites the whole file. Two overlapping rewrites of different lengths would
leave exactly this: a shorter complete stream with the tail of a longer one
behind it. A blow that kills several creatures at once fires several appends.

⚠ **And a damaged save is still offered.** Both files appear in `Load Game`
with a correct name, class, level and area, because the listing reads only the
header — which is intact. The failure arrives after the player chooses.

---

# THE FOUR ASKS

## 1 · the full loop — CONFIRMED, with the two caveats above

    character.xp-awarded  {amount: 3000, from: x-cr9.probe.02, cr: 9.0, level: 1}
    character.levelled    {level: 2, class: jedi_consular, xp: 3000}

Real XP on the record, a real level taken at rest, one level for one rest,
attributed to the class, with the XP total snapshotted beside it. `Load Game`
afterwards reads **`level 2 jedi_consular`**. This is the first time the two
systems have run together and they do fit — for a cast kill, across a reload.

## 2 · the three refusals

**A fight where the enemy DIES pays** — ✓, for a cast kill (above), at three
separate CRs: `100`, `125`, `3000`.

**A LOST fight pays nothing** — ✓, and more strongly than asked. I lost a fight
in which I had already killed two priced enemies. The file records all three
deaths and **no award at all**:

    character.died  {subject: x-cr1.probe.02, …}
    character.died  {subject: XP One, …}
    character.died  {subject: x-cr0.probe.01, …}
    — and zero character.xp-awarded

The kills are in the log, so "no award" cannot be passing because nothing ran —
which is the argument your own guard makes, here in a real fight.

**A fight where the enemy SURVIVES pays nothing for it** — ⚠ **NOT CONFIRMED,
because I could not reach it.** `_endFight` fires on `f.over`, and `over` wants
every enemy down. I disengaged and walked two full turns' worth of squares away
from a 4000-vitality enemy and the encounter stayed open; leaving by `esc`
writes the outcome but I never saw a fight *end* with an enemy standing. If
walking away is meant to end a fight — your `PT-2233` note says the third case
*"needed a second live body anyway: a fight the player walks away from"* — then
either that path is not wired to `_endFight`, or it needs something I did not
find. The filter itself (`_isDead`) is right there in `_xpFor` and reads
correctly; I simply could not make the situation happen in play.

## 3 · CR 0 — CONFIRMED, live and by name

    character.xp-awarded  {subject: CR Zero Cast, amount: 100, from: x-cr0.probe.02, cr: 0.0, level: 1}

**100 at level 1**, and recorded as `cr: 0.0` rather than as an absence — the
distinction `AUTHORED-CHARACTER-01 §2b` is about. The unpriced creature in the
same fight produced no award, and `awardsFor` confirms the pair directly:
priced-at-zero pays 100, unpriced is skipped.

## 4 · Force Plague — CONFIRMED

    Force Plague · 20f — 159 → 139 · ceiling −6 to 153 · at x-none.probe.01 ·
    x-none.probe.01 — d20 20 = 18 vs 25 · slowed

A real Fortitude save, rolled and shown, rather than a condition landing
automatically. `DC 25 = 5 + Force levels 12 + WIS 4 + CHA 4`, and the target's
total of 18 against its own −2 Fortitude. It failed, so `slowed` applied — which
is `force_plague`'s authored condition. The `−6` ceiling degradation is its
authored value too.

---

## Method, and what is mine

⚠⚠ **Every player here is an authored save**, written in the product's own
format by `scratchpad/mksave.py` — the same lever as TEST 095, and still the
only route to a levelled character, since chargen gives one class at level 1
and premades remain unimplemented. Your reader accepted them and refused the
illegal ones by name. `character.levelled` events carry the class so the
ledger's upsert keeps `record_validate` rule 5 satisfied.

⚠ **I read the saves through `readSave` and `replay`, not my own decoder.** My
hand decoder searched for the gzip magic and found it inside the millisecond
stamp; the product's reader is the one implementation that decides what a save
says, and the damaged-save finding is its verdict rather than mine.

⚠ The `zz_tester_*.dart` files I wrote are in **my scratchpad copy only** —
your `test/` was never touched.

## What I did not do

- **Did not reach a fight that ends with a living enemy** — see ask 2.
- **Did not confirm the level-up without a reload**, because it does not happen.
- **Did not test the Dark Healing self-cast or the droid targeting** — you said
  they were unbuilt; one of them is built, and I left both alone.
- **Loom not launched.**

## State

- **New package `xp-probe` is mine and left on disk**, with six areas — the
  discriminator `a04-both` is the one that isolates the finding in a single
  fight. ⚠ Its display name is `AAA XP Probe` only so it sorts to the front of
  a 25-package library; the id is `xp-probe`.
- ⚠ **`xp-two.sav` is left deliberately damaged** so the unreadable-save
  finding reproduces without rebuilding it.
- Ten authored saves in total; `level-up.sav` is the one carrying thewhole loop.
- My build lives in the scratchpad copy only. **Your `build/` was never written
  to and neither shared bundle was touched.**
- App pids `306527`, `307328`, `309530`, `312354`, `313128`, `313730`,
  `314553`, `315287`, `315790`, `316119`, `316314` all killed by pid and
  confirmed gone; no Loom; nothing of yours touched.
