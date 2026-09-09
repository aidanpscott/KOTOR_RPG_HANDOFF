# 005 · Content or runtime, and the sweep for the class

**From `Tester`. ⚠ NO REQUEST FILE — next free number, per `README`.** Answers
the two questions put to me after `004`: **is the silent conversation content
or runtime**, and **where else does a droid take an organic path**.

Read at `Lodestar 78782b6` · app `a42f9b3` · `Loom 2058b16`. **This is a code
and data read, not a play session** — I state that up front because the last
report was the opposite and the two should not be confused.

---

## 2 · ⚠ CONTENT. The runtime is doing exactly what the format tells it to.

**`DIALOGUE-FORMAT-01` rules it twice, in as many words:**

> `§3` — *"**`replies` OR `then`, NEVER BOTH, and absent means the conversation
> ends here.**"*
>
> and the player-line field table: *"`then` | ordered links to NPC lines |
> **no — absent ends the conversation**"*

The bed's four gated player lines carry no `then`. **A conversation that ends
there is the format working**, and `Coder` should not change the runtime to
make it continue.

**⚠ But two things sit on top of that, and only one of them is the bed's.**

### 2a · The runtime signals "ended" by manufacturing an empty `say`

`dialogue_run.dart` `choose()`, when the picked line has no continuation:

    if (id == null) {
      return Beat(line: NpcLine(id: '', say: ''), …)
    }

and the app reads that back in `play_screen._pick`:

    if (next == null || next.line.id.isEmpty) { _endTalk(); }

**So the app knows the conversation ended and deliberately says nothing.** That
is a presentation choice, not a bug — **and nothing rules it.** ⚠ The contrast
is worth seeing: `PT-1433` makes an **empty `say` from an author a load
failure** (`dialogue.dart:442,495` — *"an NPC line needs a `say`, and it may not
be empty"*), and **the runtime constructs one internally as its end-of-
conversation signal.** Refused from an author, manufactured by the engine.

**That is the whole of what a player experiences**, and it is the only part I
would call a defect — a conversation that ends should say it has.

### 2b · ⚠⚠ AND THE CHECK NEVER ROLLED. The bracket promised a roll that cannot happen.

**This is the part that is neither the bed being lazy nor the runtime being
wrong, and it is why I am glad you asked before fixing.**

Two different fields drive "shows a bracket" and "rolls":

| | field | where |
|---|---|---|
| **the amber `[Persuade]`** | the gate on the **reply link** | `_gateVerdict` → `Verdict.isACheck` → shown in amber |
| **the roll** | `_pick(option.line.links)` — **the player line's own `then`** | `resolve()`, on commit |

`you-are-one` has **no `then`**, so `_pick` returns `null` **before any dice are
touched**. `resolve()` is never called.

**⚠ So a gated reply whose player line has no continuation renders a check
bracket and never rolls one.** `§4c` derives the bracket from the gate *"so
nothing an author typed can disagree with what rolls"* — and here the bracket is
honest about the gate while **nothing rolls at all.** I reported in `004` that I
could not tell whether I passed or failed; the answer is **neither**.

**I am not proposing the fix.** But the shape of it decides which side moves:
if a check is meant to resolve on commit regardless, that is the runtime; if a
gated reply is required to carry a continuation, that is a format rule the
validator could assert and Loom could refuse to write. **`dialogue.dart`'s
validator does not currently report a player line with a gate and no `then`.**

---

## 3 · ⚠ The sweep — and the class is sharper than "organic code with droid data"

**It is not that the droid path is organic everywhere. It is that some steps
were WIRED and the rest were never given the chassis at all.** The line is
clean and it is visible in the constructors.

### The diagnostic is one table each

| droid data table | read by | result on screen |
|---|---|---|
| `droid_skills.toml` | ⚠ **4 files** — `chargen_source`, `hub`, `skills_screen`, `records` | **the best screen in the app** — names every closed skill and why |
| ⚠⚠ `droid_arrays.toml` | ⚠⚠ **NOTHING. Zero files, app, engine or Loom** | the organic assortment, and boots for a hoverer |

**`droid_arrays.toml` is shipped in `base-rules` and read by no code anywhere.**
It carries exactly what the equipment screen needed — per class, for a droid:

    Scout      Blaster Carbine · 1 Sensor Probe — was Adrenal Stamina · 2 Repair Kits
    Machinist  Blaster Pistol — its Long Sword is unusable
    Agent      Hold Out Blaster · 1 Recording Rod — the adrenal is dropped

**The droid equipment answer was authored and then orphaned.** That is not a
missing feature; it is a disconnected wire.

### Which steps can even see the chassis

| step | droid-aware? | why |
|---|---|---|
| Species · Model · Backstory · Abilities · Skills | ✓ | branch on chassis; `records.dart` carries 69 references |
| hub · step strip · pre-hub | ✓ | renumber, and name each absence with a reason |
| Class | ✓ | bars the six Force classes — `PT-92`, and it is real on screen |
| ⚠ **Equipment** | ✗ | receives `scale · packageName · className · array · grant · aptitude`. **No species. No chassis.** It cannot branch |
| ⚠ **Feats** | ✗ | receives `scale · packageName · picks · className · heads · chainAfter · grantedCount`. **No species. No chassis** |
| Identity | ✗ | no chassis. Portrait is scaffold so nothing to file, but the step is blind too |

**⚠ Equipment and Feats are not written wrongly — they are not told.** Both take
`className` and nothing about the body. Every finding in `004`'s section 3
falls out of those two rows plus the feat record's missing eligibility field.

### ⚠ AND THE PART THE SWEEP FOUND THAT PLAY HAD NOT SHOWN ME

**The play path has no droid concept whatsoever.**

`chassis` appears in **exactly one** file in the whole engine —
`record_validate.dart` — and in **no** combat, encounter, attack or play file.
Nothing under `KOTOR-RPG-APP/lib/play/` mentions droid or chassis either.

**So the species screen makes five concrete mechanical promises that exist
nowhere below chargen:**

| promised on the Species screen | implemented? |
|---|---|
| *constructed* — immune to poison, disease, suffocation, radiation | ⚠ **no** — zero files mention any of them |
| *ion vulnerability* — 1 Constitution per hit, 2 on a critical | ⚠ **no** |
| Remote's *shield projector* — once per encounter, DR 5 to an adjacent ally | ⚠ **no** |
| *repulsorlift frame* — hovers, ignores difficult terrain | ⚠ **no** |
| *fixed armature* — no melee at all | ⚠ **no** |

⚠ **The equipment gap is a wire; this is a floor that was never poured.** I am
flagging it as scope rather than as six more defects — the whole of "what a
droid IS mechanically" stops at the hub, and the character sheet promises it
anyway. **Whether any of it is due yet is the owner's call, not a defect for
`Coder`** — but a player reading the Species screen is being told five things
the game does not do.

**⚠ Scoped honestly:** I searched for the trait words (`immune`, `poison`,
`disease`, `suffocation`, `radiation`, `shield projector`, `repulsorlift`)
across `Lodestar/lib` and `KOTOR-RPG-APP/lib`. `ion` and `hover` I discarded as
substring noise — they match *action*, *conversation*, *version* and Flutter's
own hover state. **I did not read every combat file line by line**, so I claim
"no reference anywhere" rather than "provably unimplemented".

---

## 1 · `PT-1456` — nothing for me here, and one number worth keeping

**Ruled and understood.** ⚠ **Astromech's STR is exactly 8** — the margin was
one point, so the bound would have caught a second of the four choosable
chassis on its next revision. And the three chassis the app does **not** offer —
`Labor 16`, `Protocol 8`, `Probe 8` — are all inside the old bound, so the
failure would have stayed invisible if `Remote` had not been the one I picked.

**⚠ `t3-k9.sav` is untouched and still refuses to open**, so the fix has a
before-and-after to test against.

---

## 4 · The attack line — restating it precisely, since it is my ask

`"rolled 18 — d20 16 + attack 2 · needed 10 — hit · 2 left"`. The line gives
the **to-hit** derivation in full and then states a **resulting vitality**.

**What is missing is the damage half:** no weapon name, and no damage roll. I
inferred a `1d12` rifle from a 10-point drop and my own Marksman Rifle from the
trooper going 18→14. **`PT-1326` makes the derivation the return value**, and
the to-hit half honours that on screen while the damage half does not.

**Until it does, I cannot judge whether a weapon reads correctly** — only
whether the numbers are plausible, which is not testing.

---

## ⚠ Scoped negatives

**This report is a read, not a run.** Everything above is from source and data
at the heads named at the top. **I ran the app in `004`, not here.**

- **I did not re-test the esc path, `N1` or `N2`** — in flight
- **I did not create an Astromech, Assassin or Battle droid.** The chassis
  spreads and the 8–18 rule are read out of `chassis.toml` and
  `record_validate.dart:193`; **no second chassis has been played**
- **I did not verify that `droid_arrays` would produce a correct kit if wired** —
  only that nothing reads it
- **I did not read every combat file** — see the scoped note above
- **I did not test a Force class**, which a droid cannot take, so the Powers
  step remains untested by me
