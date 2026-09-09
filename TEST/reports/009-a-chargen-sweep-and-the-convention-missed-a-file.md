# 009 · A chargen sweep — and the convention missed a whole file

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** Played, not read, with
one data scan used to **target** the sweep and a second used to **quantify**
what the screen showed. App `9fb1762` · `Lodestar b7e9198`; **pin checked, lock
`resolved-ref` = engine HEAD.**

⚠ **No character was completed and no save was written.** Seven saves before,
seven after.

---

## ⚠⚠ THE FINDING: `powers.toml` was never swept, and it feeds the step I had never opened

**You predicted a screen that renders every field would render a new one. It is
worse than that: an entire file the convention never reached.**

    powers.toml       note fields: 0        ⚠ never swept
    species.toml      note fields: 5
    programmings.toml note fields: 6
    professions.toml  note fields: 1
    upbringings.toml  note fields: 2
    feats.toml        note fields: 24
    items.toml        note fields: 45

**⚠ 41 of 104 powers carry a `PT-` citation inside `effect` — and `effect` is
the field the POWERS screen renders in full.**

**Seen on screen**, expanding `Beast Control` on a Jedi Consular:

> Beast Control distracts a creature or beast… Distracted targets will not
> notice the player unless the player gets too close or interacts with them.
> **△ targets: beast — PT-462. △ Renamed from Beast…**

**`PT-1467` swept nine files and `powers.toml` was not one of them.** It is the
largest single exposure I have found: **41 citations**, in the step a Force
class reaches and nothing else does — which is very likely why it was missed,
and it is the step I had never opened until today.

---

## ⚠ And the species screen renders citations too — four confirmed on screen

`species_screen` renders every field it is given, so every citation left in a
**value** reaches a player. **I read these off the screen, not the file:**

| species | rendered value |
|---|---|
| **Cathar** | *"Cathar may take the Pounce and Claw unarmed attacks — **ATTACKS-07**. Both are attacks, not feats…"* |
| **Echani** | *"…the Echani Strike attack chain from character level 5 — **ATTACKS-07**."* |
| ⚠ **Droid · Assassin** | *"…Heavy weapons no longer gate a prestige class — so this is a **CAPABILITY** rather than a class route. Astromech and Remote may **NOT**. It may not equip melee weapons — **ATTACKS-05** closes melee to every droid."* |
| **Droid · Battle** | *"…Already a three-tier chain in **FEATS-LIBRARY-01**."* |

⚠ **The Assassin one is the worst I have seen in this project.** It is a
document citation, two shouted words, and a paragraph of *design rationale*
(*"no longer gate a prestige class"*) rendered as a species trait.

**The data scan behind it**, for scope: **6** citation-shaped values in
`species.toml`, **2** in `programmings.toml`, **3** in `professions.toml`.

---

## ⚠ A plural verb on a one-item list

The POWERS screen's withheld line reads:

> **withheld — no cost**  **Precognition have** no Force cost written for them
> yet, so there is nothing to spend to use them.

**`Precognition` is one power.** *"have … them … them"* is a plural template
meeting a single-item list. ✓ I checked the cause: **9 powers lack a cost in
the data, but only `Precognition` is offered to a level-1 Consular**, so the
list genuinely has one member.

---

## ⚠ AS DESIGNED — and one of them corrects my own earlier report

**A1 · ⚠ `PT-92` is narrower than what is actually built, and I said the wrong
thing in `004`.** I wrote *"the Force half IS enforced — `PT-92` is real on
screen"* after seeing the six Force classes greyed for a droid. **Today
`Rakata` — an organic — greys them too, and `Human` does not.**

The mechanism is not "droids are barred". It is a species field:

    Rakata   force_blind = "A Rakata cannot take Force-Sensitive. They still accrue
                            Dark Side Points and are still affected by Force powers —
                            they simply cannot wield the Force."

**Two unrelated species carry `force_blind` and the class step honours both.**
That is more general and better than I credited it with. **My `004` line
attributed a general mechanism to one rule**, which is the same shape as a
wrong-place negative pointed the other way.

**A2 · `PT-1469`'s near-miss resolved correctly.** `Snivvian` renders
**`size — Small — +1 Defence.`** with **no `PT-623`**. The citation went to the
note and **the Defence bonus stayed on the player's screen**, which is exactly
what the dry run caught and the final version got right.

**A3 · Notes are correctly invisible wherever they exist.** `Snivvian`,
`Quarren`, `Droid`, `Droid · Assassin`, `Bastard`, `Unknown` and `Merchant`'s
`detail = "see §2"` all carry notes and **none of them rendered.** ⚠ **The
convention works. Its coverage is the problem, not its design.**

**A4 · The compound field name renders cleanly.** `Rakata`'s
`"ability_adjustments,_skill_bonuses_and_languages"` becomes the label
*"ability adjustments, skill bonuses and languages"* with the value *"set by
subrace. See each entry."* — the key-to-label renderer handles it.

---

## Smaller things, from pressing rather than reading

**B1 · Flavour rides inside an ability-adjustments value on all three Aqualish
subraces**: *"+2 Strength, −2 Wisdom, −2 Charisma. **Wetland hunters.**"*
(Aquala: *"Cold water and blubber."* · Ualaq: *"Dexterous hands, dark
places."*). ⚠ **Not a citation, so not obviously the convention's business** —
but it is a value cell carrying something that is not the value, which is the
shape you asked me to watch for. `Echani`'s subrace, by contrast, is clean:
*"+2 Dexterity, −2 Constitution."*

**B2 · Choosing a subrace hides the parent's traits.** `Aqualish` shows
waterbreathing, low-light vision, size, speed and languages; picking `Quara`
replaces the panel with three fields and **the parent traits are no longer
visible anywhere.** A player cannot see their whole species on one screen.

**B3 · 28 professions in the data, 12 offered.** `Antiquarian`, `Hermit` and
`Mysterious Stranger` are not in the list — **which is why their citations
(*"ONE FRAGMENT OF A PUZZLE THE CAMPAIGN HAS NOT POSED YET — §2b"*, *"a random
tier-1 item — LOOT-01 §3"*) do not reach a player.** Filed as scope, not as a
defect: I do not know whether the 16 are meant to be offered.

**B4 · A grant option that is a fragment.** `Merchant` offers **"a tier
above"** as a clickable label. A tier above *what* is not on the screen. The
opposite failure to `D3`'s over-full label, in the same control.

---

## ✓ Everything I pressed that behaved

- **`Accept` while disabled** (Aqualish with no subrace chosen) — nothing, no
  trace, no state change
- **Locked steps** — clicked `Powers` and `Play` while locked: nothing
- **`Escape` on the hub** — nothing
- **A second click on a chosen power** — **deselects**, and the counter tracks
  it (`1 of 2` → `2 of 2`)
- **A second click on a chosen subrace** — stays chosen, `Accept` stays enabled
- **Arrow keys on the species list** — no effect; the list is pointer-only
- **The four corner icons** — `Characters`, `Profile`, `Settings` each print a
  trace; `Import` opens a real screen
- **`Import` → "Choose a game folder"** — says *"Reading a game folder is not
  built yet, so this button does nothing today"* **and does nothing.** ⚠ The
  best-behaved dead button in the app
- **`Cancel` / `Back`** everywhere I used them
- **Force-class strip** — *"A Force class: the Powers step exists and the strip
  has nine steps"*, and the hub shows **nine of nine** with `Powers` between
  `Feats` and `Equipment`

**No exception, no overflow, nothing red** in the run log.

---

## ⚠ What I sampled, and what I did not — the combinatorics are not exhaustible

**Species sampled — 9 of 57:** `Aqualish` (+ `Quara`), `Cathar`, `Echani` (+ a
subrace), `Human`, `Quarren`, `Rakata` (+ a subrace), `Snivvian`, and `Droid`
in **three** of its four bodies — `Astromech`, `Assassin`, `Battle`.

⚠ **`Remote` I did NOT re-open this session** — I have it from `004`/`006`.
So **three of four bodies today, four of four across all reports.**

**Classes sampled — 4 of 38:** `Soldier` (default, non-Force), `Scout` (open to
a droid), `Marksman` (barred for a droid), `Jedi Consular` (Force). ⚠ **I did
not select the other five Force classes**, only observed them enabled for
`Human` and greyed for `Rakata` and `Droid`.

**Pairs walked end to end: 0.** ⚠ **This sweep completed no character**, by
design — I stood on screens instead. So **nothing here is evidence about
Play, saves, or the hub's later steps**, and `Identity`/`Play` were not opened
at all.

**Also NOT checked:**

- **`Nikto` (5 subraces), `Sith` (2), `Zabrak` (2), `Arkanian` (2)** and the
  other 48 species — **22 subraces exist and I opened 3**
- **The remaining 2 citation-carrying species values** my scan found; I
  confirmed 4 of 6 on screen
- **Whether all 41 power citations render** — I confirmed **one**,
  `Beast Control`, and read the other 40 from `effect` fields in the file
- **`feats.toml` (24 notes) and `items.toml` (45 notes)** — I did not open the
  Feats step this session beyond picking one, and never reach items in chargen
- **Any window size but 1280×720**
- **`Loom`** — this was the app only

**Not re-filed, per `STATE`:** the feat groups, `Environmental Sealing`'s
availability, the hardcoded `Battle` example on the abilities screen, and `D3`'s
*"TAKES THE CLASS'S OWN melee UPGRADE FROM §4a…"* label — **all four were in
front of me again today.**
