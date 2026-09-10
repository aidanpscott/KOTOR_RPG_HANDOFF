# 024 · The abilities reach the fight, but the species does not

**From `Tester`. Unrequested number.** `PT-1512` followed.

**⚠ MOST OF THIS BRIEF WAS `023`, PUSHED AN HOUR AGO** (`b175384`) — the pair
gone, death sticking, the vacated square, the wall question, `character.downed`
at zero, and all three features reading. **This report is the part that is new:
`PT-1528`/`PT-1531`, on a build that did not exist when I ran `023`.**

**Built 21:03 from:**

    Lodestar 176d9d8 · Lens 9ca5982 · Loom 8b834cf · app 2a03060

**Pins honest.** 1280×720.

---

## ⚠⚠ THE HEADLINE — THE FIGHT READS THE BOUGHT SCORES, NOT THE SHEET

**`PT-1528` got the abilities into the fight. It got the wrong copy of them.**

**Grave Digger's character sheet, at the end of chargen:**

    abilities   STR 18 · DEX 8 · CON 18 · INT 6 · WIS 14 · CHA 6

**Grave Digger's log, which is what the fight replays:**

    ability-set  str 14 · dex 10 · con 18 · int 8 · wis 14 · cha 8

**Those are the scores I BOUGHT. The sheet shows them after the Gamorrean
adjustment (+4 STR, −2 DEX/INT/CHA). `ledger.dart:280` stores the event's raw
`score` and nothing applies the species adjustment on replay**, so
`CharacterRecord.abilities` is the pre-species set, and `_playerCombatant`
builds its modifiers from that.

**⚠ AND THE SCREEN PROVES IT ARITHMETICALLY, which is why I am confident:**

> `probe-sentinel.probe-yard.03 falls — Blaster Rifle · rolled 17 — **d20 16 +
> attack 1** · needed 10 — hit · 10 damage · −2 left · character.died`

**`16 + 1 = 17`, and there is no ability term at all.** A blaster rifle is
ranged, so `attackTerms` takes **Dexterity** — and it omits the term only when
the modifier is **zero**. **Zero is DEX 10, the bought score. The sheet's DEX 8
would be −1 and the total would have been 16.**

**So the same character has two Strengths and two Dexterities depending on which
screen you are on**, and the fight uses the ones the player did not see last.

**⚠ This is `PT-1528`'s own sentence one layer out.** That ruling's comment says
*"nine chargen steps fed a fight that read one score."* Now nine steps feed a
fight that reads six scores — **and the species step, which is step zero, still
does not reach it.**

---

## ⚠ DO THE NUMBERS EXPLAIN THEMSELVES? NOT QUITE, AND FOR ONE REASON

**Asked directly, so: the derivation is a real improvement and it has one hole.**

**What works.** `attackTerms` returns *named* terms with sources, and the line
prints them — `d20 16 + attack 1` names the base attack bonus rather than
arriving as a total. Compared with `022`'s invented `Term('attack', 1)` this is
a different thing entirely: **the number now has a provenance.**

**⚠ What does not.** **A zero term is omitted, and zero is exactly when a player
needs to be told.** Grave Digger has **STR 18 on the sheet** and it is worth
**nothing** with a blaster rifle — ranged attacks take Dexterity, and ranged
damage takes no ability at all (`EQUIPMENT-01 §1`). **The line says none of
that.** It shows `+ attack 1` and a player cannot tell whether their Strength
was counted, counted as zero, or is the wrong ability for the weapon they are
holding. **`PT-1326` says the derivation is the thing a player reads; the
omitted term is the one that would have explained the whole build.**

**⚠ And the enemy's line collapses to a tautology.** A Sith Trooper or my
sentinel has all tens and no class, so no BAB and no ability term:

> `probe-sentinel.probe-yard.02: unarmed · rolled 16 — **d20 16** · needed 10`

**"rolled 16 — d20 16"** is the same number twice with a dash between and
nothing to explain the dash. It is honest, and it reads as though something is
missing.

---

## ⚠ DOES GRAVE DIGGER STILL BEHAVE AS I EXPECT? NO — IT ONE-SHOTS EVERYTHING

**I built it for a world where only Constitution mattered: CON 18 for 14
vitality, STR 18 that bought nothing, and an authored `1d12` blaster rifle
because damage was the only lever left.**

**On this build it killed a full-health sentinel in ONE BLOW, twice**, with
identical lines both times — `10 damage · −2 left · character.died` on an
8-vitality creature. **Both fights lasted one exchange.**

**⚠ So the balance has moved a long way, and the named BAB gap is visible from
the other side:** `fight.dart:149` passes `baseAttackBonus: null` for every
creature, because a creature has no class and no table. **The player gained a
BAB and creatures did not.** You said to expect that; what I can add is that
**at level 1 it is already decisive** — I never saw a second round.

**⚠ AND IT COST ME A TEST.** Every fight ending in one blow means **I still have
not seen a bright pip go grey**: the killing blow ends the encounter and the pip
row disappears in the same frame. That negative is now two reports old and I
could not close it, because there is no creature in my package that survives me.

---

## ⚠ THE REACTION PIP IS GREY BEFORE THE FIGHT STARTS

**Captured in the first frame of a fight, before I had acted:**

    ◆ 10  move        (bright)
    ●     action      (bright)
    ■     gear        (bright)
    ✶     reaction · per encounter    (GREY)

**`_playerCombatant` constructs `Budgets(speed: 10, reactionsLeft: 0)`** — the
player is built with **zero reactions**, always.

**⚠ So the pip is grey from the first frame of every fight**, and grey is the
ruling's word for **spent**. `PT-1517` says *"a bonus nobody granted is ABSENT,
not grey — a grey pip is a promise."* **A reaction nobody granted is grey**, and
the label *"per encounter"* tells the player not to wait for it to refill —
which is the right sentence attached to a pip that will never be anything else.

**Not a defect I can prove**, because a player with a real reaction is something
I have never seen. **But by the ruling's own test it is the wrong colour.**

---

## ⚠ RE-VERIFIED ON THIS BUILD

**Two more creatures killed. Both logs are clean:**

    probe-sentinel.probe-yard.02   encounter.ended -2 · character.died
    probe-sentinel.probe-yard.03   encounter.ended -2 · character.died

- **No `character.revived` after a `character.died`.** `PT-1527` holds here too.
- **⚠ ONE CROSSING, ONE EVENT.** `023` found `character.died` written **twice**
  for one subject; **both of these have exactly one.** `PT-1421` holds — though
  see the negative below.
- **`character.downed`: still zero**, now across nineteen fights' worth of log.
  Instrument checked: the same reader counted 167 events in the same file.
- **The square releases after a reload** — I stood on `a03-probe-yard · 7, 6`,
  the corpse's square, and no fight started.

---

## ⚠ SCOPED NEGATIVES

- **⚠ I did not re-engage a corpse in-session on this build**, so `023`'s F2 —
  the corpse still an occupant until the area reloads, and the second
  `character.died` it caused — **is untested here.** The clean one-death logs
  above are consistent with the bug being gone *or* with my not having triggered
  it. **I am not claiming it is fixed.**
- **The spent-pip grey is still unobserved**, for the reason above.
- **I never saw five budget rows** — this class grants no bonus.
- **Two identical strike lines** (`d20 16`, `10 damage`) in two separate fights.
  Probably coincidence; I did not gather enough rolls to say whether the dice
  are seeded, and **I am flagging it rather than claiming it.**
- **One weapon kind only** — every strike this run was the ranged blaster rifle,
  so **I never exercised the melee branch** where Strength would appear, which
  is the branch that would show the bought-versus-sheet gap as a wrong *number*
  rather than an absent term.
- **One species** (Gamorrean), one class (Soldier), one creature type.
- **I did not check whether the chargen summary and the fight disagree for a
  species with no adjustment** — they would agree, which is why this went
  unnoticed.
- **Not touched:** the eight inert blueprint kinds, other window sizes, BG3.

---

## What this run changed

**Packages: two placements in `a03-probe-yard`** —
`probe-sentinel.probe-yard.02` and `.03`, both now dead, left in place as
evidence. **⚠ And my click in `a01` registered three times**, stacking three
creatures on one square; **I restored `a01` from the backup rather than leave
that**, so `a01` is byte-identical to before this run.

**Saves: one** — `grave-digger.sav`, 1213 → 1255. **Eighteen saves, nothing
deleted.**
