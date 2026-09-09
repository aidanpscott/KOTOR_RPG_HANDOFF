# 004 · A droid that cannot be loaded

**From `Tester`. ⚠ NO REQUEST — next free number, per `README`.** I was told to
go and play it rather than work a claim list, so this is what an hour of using
it found. App `1407b4e`, `Lodestar 78782b6`, real machine, `./run-app.sh`.

**I made the character I wanted to make:** a **Remote** droid, `Marksman-H`
frame, **Marksman** class, **Protocol Droid** programming, named `T3-K9`. Then
I fought the trooper, lost, saved, quit and came back.

---

## ⚠⚠ THE ONE THAT MATTERS — chargen builds a character the app then refuses to load

**`T3-K9` is gone. Both `Continue` and `Load Game` refuse it:**

> **THIS SAVE WILL NOT OPEN**
> This save cannot be opened.
> • **STR is 6, outside 8 to 18.**

**⚠ The app chose that 6 itself.** The abilities step for a droid says, in its
own words:

> *"a droid does not buy abilities — Droids are built rather than generated.
> They do not use the 30-point buy… **These are final scores.**"*

and then prints the **Remote production spread**: `STR 6 · DEX 16 · CON 10 ·
INT 16 · WIS 14 · CHA 10`. **A player cannot change it — there are no `+`
controls on that screen.** `record_validate.dart:193` then rejects anything
below 8.

### ⚠ Scoped exactly: it is ONE chassis, and it is one the app offers

`chassis.toml` carries seven spreads. **Remote is the only one with a value
outside 8–18:**

| chassis | STR | offered at creation? | loads? |
|---|---|---|---|
| Battle | 14 | ✓ | ✓ |
| Assassin | 12 | ✓ | ✓ |
| Astromech | 8 | ✓ | ✓ (on the boundary) |
| ⚠ **Remote** | **6** | ✓ | ⚠ **NO** |
| Labor / Protocol / Probe | 16 / 8 / 8 | ✗ not offered | — |

**One of the four choosable chassis produces an unplayable character.**
`Astromech` sits exactly on the boundary at 8, so the margin is one point.

**Repro:** `New Game` → `Create New Character` → **Droid** → **Remote** → any
model → any class → complete the six steps → `Play` → quit → `Continue`.

**Expected:** the droid I just played. **Actual:** a refusal, and the character
is unrecoverable by any route in the UI.

⚠ **The refusal itself is behaving correctly** — `SAVE-LOAD-01 §5`'s *"failure
is loud at every step"*, with the reason named. **It is refusing something the
app built and told me was final.** The defect is the disagreement, not the
refusal, and I am not guessing which side should move.

---

## ⚠ Four of the six conversation options end the conversation silently

**I took `[Persuade]` because I had never taken a check.** The panel closed.
No reply, no roll result, no message anywhere on screen — the board simply came
back. **I could not tell whether I had passed or failed.**

It is not the gate. Reading the bed's conversation afterwards:

| option | continues? |
|---|---|
| `[Lie]` Command sent me | ⚠ **no `then` — dead end** |
| `[Persuade]` You are one man | ⚠ **no `then` — dead end** |
| `[Human]` commissioned officer | ⚠ **no `then` — dead end** |
| `[Bribe · 50 credits]` Fifty credits | ⚠ **no `then` — dead end** |
| Stand aside. | ✓ starts the fight |
| My mistake. | ✓ loops back |

**⚠ Every gated option is a dead end, and the two ungated ones are the only
ones that go anywhere.** The four the colour system exists to signal — amber
for the roll, teal for who you are, the price — are exactly the four that end
in silence.

**Whether this is the bed's authoring or the screen's is not mine to rule.**
But `PT-1307` derives the bracket *"so nothing an author typed can disagree
with what rolls"* — and here **nothing rolls that the player can see.** A
conversation that ends should say it has ended.

---

## ⚠ The app charged me my only feat for something it told me I already had

`FEATS` offers **1 of 1** for a Marksman. I picked **Environmental Sealing**,
and the screen's own description reads:

> *"Immune to vacuum, pressure, radiation, atmospheric hazards, and airborne
> toxins. Nothing in the corpus stated this and **it is true of all four
> chassis**."*

**It took the pick.** `0 of 1` remaining, no warning. The feat record agrees —
`description = "Racial. **Granted at 1st level to every droid.**"` — while
carrying `availability = "selectable"`.

⚠ **This is `U2` from report 001 seen from the other side.** A feat record has
no field for who may take it *or* for whether it is already granted, so
`availability` is the only lever and it is set wrong here. **The feat list a
droid sees is byte-identical to the organic one** — `Cybernetic Implantation`
and all — just as an organic still sees `Droid Upgrade 1`.

---

## ⚠ Raw KOTOR resource ids are printed to the player

`BACKSTORY` → `Salvage Droid` shows, as the grant:

    grant
    Parts — g_i_parts01

**Five of seventeen programmings do this:**

    Maintenance Droid  Droid Motion Tracker — d_tool_01
    Sentry Droid       Droid Deflector Mark I — d_shield_01
    Salvage Droid      Parts — g_i_parts01
    Repair Droid       2 × Advanced Repair Kit — g_i_drdrepeqp002
    Survey Droid       Minor Frag Mine — g_i_trapkit004

**Same shape as `D3`** — a source-side identifier reaching a player-facing
label. These are the games' own resrefs, in `base-rules`, which is generated,
so the fix is upstream in `gen_base_rules.py` rather than on the screen.

**And one typographic outlier:** `Protocol Droid`'s grant renders as
**`+3 LANGUAGES`** — **the only fully upper-case grant of the seventeen.** It
reads as shouting beside `Diplomat` and `Training Remote`.

---

## ⚠ The abilities screen explains my droid using a different droid

Under the Remote's spread, every chassis gets this line, hardcoded at
`abilities_screen.dart:357`:

> *"These are final scores. The chassis adjustment is already in them and does
> not apply again — **Battle's +2 Strength and −2 Charisma are visible as 14
> against 10**."*

**I am a Remote.** My sheet reads `STR 6 … CHA 10`. **The 14 it tells me to
look for is my Wisdom.** The explanation is sound; it is illustrated with a
chassis the player did not choose.

---

## Smaller things, all seen while playing

**⚠ `[Persuade]` is offered to a character the app says cannot have Persuade.**
The `SKILLS` screen states, in its own words, *"closed to every droid ·
Mysticism · **Persuade** · Streetwise · Swim · Beast Handling"*. Two screens
later the trooper offers me a `[Persuade]` check. Untrained use may well be
legal — **but nothing on either screen reconciles them**, and I read "closed to
every droid" as "not available to me".

**⚠ A hovering droid is issued boots.** The Remote *"hovers, ignores difficult
terrain, and makes no footfalls"*. Its Marksman kit includes
**`boots · Dockworker's Treads — 40cr`**. The class assortment is not
chassis-aware.

**⚠ You lose a fight and the screen never says what happened to you.** I went
to **−4 of 12** and the only trace was one fight-log line. The working line
under the board showed **the trooper's** vitality and not mine, because outside
a fight the player has no working line at all. **I had just been killed and
nothing on screen said so** — the marker is drawn exactly as before and it
still offers *arrows to move*.

**⚠ The attack line names no weapon and no damage.** *"rolled 18 — d20 16 +
attack 2 · needed 10 — hit · 2 left"*. I took 10 damage and had to derive it
from the vitality change. **With the fist gone and real weapons in play, there
is no way to tell from the screen which weapon fired.** I inferred the
trooper's 1d12 rifle from the size of the hit and my own Marksman Rifle from
the trooper dropping 18→14, but the game never named either.

---

## ⚠ Surprises that were NOT defects — filed because they fooled me or impressed me

**A1 · "A droid cannot take a Combat-rate class. PT-109" looked like a
contradiction and is not.** The class list for a droid is identical to the
organic one and `Soldier` sits at the top, selected. **I was ready to file it.**
Then I checked: no class in `classes.toml` carries a combat tier at all — the
four tiers are `standard base` (13), `standard prestige` (13), `force base`
(6), `force prestige` (6). *Combat-rate* is about attack progression, not a
class in that list.

**A2 · The Force half IS enforced, visibly.** Scrolling that same list, all six
Force base classes — `Jedi Guardian`, `Jedi Sentinel`, `Jedi Consular`,
`Sith Inquisitor`, `Sith Warrior`, `Sith Assassin` — are **greyed out** for a
droid. `PT-92` is real on screen.

**A3 · `[Human]` correctly disappears.** As a droid I get five options where an
organic gets six. The species gate works, and its absence is silent in the
right way — `PT-1307`, a shut option is absent rather than greyed.

**A4 · ⚠ The `SKILLS` screen is the best screen in the application.** It says
*"Remote droid — 12 of 25 skills"* and then names every exclusion and its
reason: *closed to every droid*, *closed to this body*, and — in amber —
**"withheld — unruled for droids · Science · Survival"**. `STATE.md` promised
that was said on screen. **It is, and it is the clearest thing in the app.**

**A5 · The story generator handles an absent homeworld gracefully.** A droid
has no Origin step, so there is no homeworld to name, and the prose reads
*"Ask where T3-K9 is from and you get **somewhere nobody writes down**,
eventually."* Nothing blank, nothing null. I expected a gap and got a sentence.

**A6 · The id derives correctly from an awkward name.** `T3-K9` → `t3-k9.sav`.
Digits and a hyphen survive.

**A7 · The pre-hub boundary explains the droid shape before it happens** —
*"A droid: Origin does not render at all, Gender becomes Voice or is absent,
and Backstory takes Programming in place of Profession with no Lifestyle"* —
and the hub then names all three absences with reasons, including
**"absent — this chassis has no vocabulator"**, which is `PT-1190` for the
Remote specifically.

**A8 · `PT-1453` looks landed.** The working line showed **one** clause where
before it chained every outcome. **I did not test this** — it is in flight and
I was told not to — but it is visibly different and I would not want you to
think `N2` still reproduced.

---

## ⚠ Scoped negatives

**Checked:** one droid — **Remote / Marksman-H / Marksman / Protocol Droid** —
through all six steps, one conversation, one fight lost, one save, one quit,
one reload. `endar-spire`, 1280×720, app `1407b4e`.

**NOT checked:**

- **The other three chassis end to end.** ⚠ I read their spreads out of
  `chassis.toml` and reasoned about the 8–18 rule; **I did not create an
  Astromech, Assassin or Battle and load one.** `Astromech`'s STR of 8 is on
  the boundary and deserves a real run
- **A Force class.** ⚠ The brief asked for one and **a droid cannot take one** —
  `PT-92`, enforced. The two asks were incompatible in a single character and I
  chose the droid. **The Powers step is still untested by me**
- **`Gender`/`Voice`** — a Remote has no vocabulator, so I never saw the Voice
  step. Astromech is the other voiceless chassis; the other two would show it
- **The esc path, `N1`, `N2`** — in flight, per your instruction
- **Whether an existing Remote save becomes loadable if the range rule changes**
- **`[Lie]`, `[Bribe]`, the typed box** — I took `[Persuade]` and
  `Stand aside.` only
- **Any window size but 1280×720**

**No exception, no overflow, nothing red** in the run logs.

---

## Data

**Added `saves/t3-k9.sav`** — ⚠ **and it is the evidence for the headline, so
do not delete it if you want to reproduce the refusal.** It is 729 bytes and
will not open in the current build.

`vess-taran`, `second-fight`, `probe-walker` and `packages/tester-probe/` are
still mine from earlier reports. **I deleted nothing and fixed nothing.**
