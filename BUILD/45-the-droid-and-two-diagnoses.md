# 45 · `PT-1458`, and two diagnoses asked for before any fixing

**623 green** — Lodestar 289 · Lens 4 · Loom 114 · app 216.
`Lodestar 4b3a482` · `app d95ad2c`.

**Fixed: `PT-1458` and the attack line. Diagnosed and NOT fixed: the dead-end
conversation and the droid path** — both were asked for as diagnoses first, and
both change what the fix should be.

---

## 1 · `PT-1458` — the droid loads, and the evidence is `Tester`'s own save

**The validator refused a character the app had just built and called final.**
`PT-1260`'s 8 is the **organic point-buy base**; a droid bases at **10**, so
Remote's `STR 6` is `10 − 4` and −4 is the only one in the set. `PT-1456` had
already ruled the floor belongs to the **generation** rather than to the
record — this is that ruling reaching the validator.

**⚠ Verified against the real artifact:** `t3-k9.sav`, the save `Continue`
refused, now validates **legal**.

**⚠ And the arithmetic nobody had stated is asserted now.** Base 10 plus
adjustment totals **60**; a 30-point organic build reaches about **72**.
Deriving each spread would have made **every droid twelve points weaker than
any organic** — `PT-1403` authored to parity, and all seven spreads total 72
exactly. One score in the whole set is below 8, and it is the Remote's.

> **The base says how low a score may legitimately go. The spread says what a
> chassis actually gets. Neither is derived from the other.**

**The droid check is returned, not skipped** — what would mean something is
checking a spread against its chassis, and `RulesFacts` does not carry them.

---

## 2 · ⚠ The dead-end options — the bed's content, and a validator that cannot see it

**Asked: content or runtime. The answer is content — but the content is wrong
because nothing checks it.**

**The bed's file, read directly:** four player lines carry no `then` —
`command-sent-me`, `you-are-one`, `you-are-speaking`, `fifty-credits-says`.
Two do. **So it is authoring**, and it is authoring I did, through Loom, at
`BUILD 31`/`33`.

### ⚠ But the runtime is not innocent, and the gap is sharper than the symptom

**A check only rolls on a PICK-ONE link.** `_pick` resolves a `skill` gate with
the same `resolve()` combat uses. **A SHOW-ALL reply carrying a `skill` term is
rendered amber and never rolled** — the roll would happen on the chosen player
line's `then`, and these have none.

> **So the amber bracket promises a roll the structure cannot deliver.**
> `PT-1307` derives the bracket *"so nothing an author typed can disagree with
> what rolls"* — and here **nothing rolls at all.**

**⚠ AND THE VALIDATOR REPORTS ZERO PROBLEMS.** Run against this exact file it
finds nothing: it checks unreachable nodes, dead links, unknown skills and
unknown effect kinds — **and not *a check with nothing to roll toward*.**

**Where the fix belongs, in order:**

1. **The validator** — an option shown as a check whose target line has no
   `then` is a promise the format cannot keep. **Nothing refuses or reports it
   today**, which is why the authoring error was invisible.
2. **Then the bed's content**, once something can tell an author it is wrong.
3. **And the screen** — a conversation that ends should say it has ended.
   `Tester` took `[Persuade]`, the panel closed, and **nothing anywhere said
   whether it passed.**

**Not fixed here. The diagnosis changes the order.**

---

## 3 · ⚠⚠ The droid path — the class, swept before the six

**Asked: sweep for the class. It is two causes, not six bugs, and the sweep
names them precisely.**

### Which screens know a droid exists

    abilities 11 · skills 18 · backstory 7 · hub 9 · pre_hub 8 · step_strip 6
    model 3 · records 29 · class 1 · gender 1 · origin 1 · powers 1 · species 1

    ⚠ equipment_screen  0        ⚠ feats_screen  0

> **A screen consults `isDroid` when the answer changes WHETHER it renders. It
> does not when the answer would only change WHAT IT OFFERS.**

Species, Model, Gender, Origin, Backstory, Powers and the step strip all
**appear, disappear or change shape** for a droid — and all of them were built.
**Equipment and Feats render a list, and the list is the organic one.**

### ⚠ And the second cause is underneath the first: there is nothing to filter on

| file | carries a droid distinction? |
|---|---|
| `droid_skills.toml` | ✓ **a whole file**, and `skills.toml` names exclusions |
| `feats.toml` | ⚠ **63 mentions, ALL PROSE.** Fields are `id · name · chain · is_chain_head · section · description · effect · availability` — **no field says who may take a feat, or that it is already granted** |
| `class_arrays.toml` | ⚠ **zero.** Starting equipment is keyed by CLASS, and a class is not chassis-aware |

**So `Environmental Sealing` says *"Granted at 1st level to every droid"* in its
`description` and still carries `availability = "selectable"` — and the screen
charges a Marksman's only feat for it.** The screen could not have known.

> **⚠ THIS IS WHY `SKILLS` IS THE BEST SCREEN IN THE APP, and it is not because
> that screen is better written. It is the only list whose DATA carries the
> distinction as a field.**

**And it is `U2` from report 001 seen from both sides at once:** an organic is
offered `Droid Upgrade 1` for exactly the same reason. **One missing field,
two symptoms.**

### The six, sorted by cause

| | cause |
|---|---|
| the granted feat charged · `Droid Upgrade` to an organic | **no field to filter on** — `feats.toml` |
| boots for a hoverer | **class-keyed data is not chassis-aware** — `class_arrays.toml` |
| `[Persuade]` offered to a droid | ⚠ **neither — a RULING.** `_rank` returns 0 for an absent skill, so a droid rolls untrained. That may be legal; **`SKILLS` says *"closed to every droid"* and nothing reconciles the two.** For the owner |
| raw resrefs on screen | **generation** — five of seventeen programmings, upstream in `gen_base_rules.py` |
| the abilities screen explaining a Remote with Battle's numbers | ⚠ **the one true screen bug** — a hardcoded example string in a screen that otherwise knows about droids |

**Not fixed here.** Two of the five need a **format field** before any screen
can behave, one needs a **ruling**, one is **upstream in generation**, and only
one is a screen fix. **Fixing "the six" as six would have written five
workarounds.**

---

## 4 · The attack line — `PT-1326`, fixed

*"rolled 18 — d20 16 + attack 2 · needed 10 — hit · 2 left"* named the roll and
the target number and stopped. **The two facts a player most wants — what hit
me, and for how much — were the two it did not carry.** `Tester` derived 10
damage from watching a number change and inferred the weapon from the size of
the hit.

    Blaster Rifle · rolled 17 — d20 15 + attack 2 · needed 10 — hit · 4 damage · 16 left

**With a fist for everybody it did not matter.** `PT-1452` put real weapons in
play and the line still named neither.

**⚠ And three test assertions asserted the string's SHAPE rather than its
facts** — `': rolled '`, with the colon adjacent to the roll. The weapon now
sits between them. **A test that pins a format string pins the format.**
