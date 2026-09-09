# 013 · The four gaps closed — and a power that costs but does nothing

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** App `792187e` ·
`Lodestar 12fabf7`; **pin checked, `resolved-ref` = engine HEAD.** Played.

**Five characters built and fought:** `Kesh Alaan` (Human Jedi Guardian) ·
`Wren Ossik` (Human Medic) · `IG-Seven` (Astromech Agent) · `Bran Vex` (Human
Brawler), plus the data pass for the fifth question.

---

## ⚠⚠ THE NEW ACCEPTANCE IS MET — armed AND casting, which no character has been

**`Kesh Alaan`, Jedi Guardian.** Pressing **`f`** in a fight opens:

    force 6 of 6  ·  cast — 1 Force Push 6f · 2 Beast Control 6f · esc

**Pressing `1` casts, and the line is the derivation:**

    Force Push · 6f — 6 → 0 · ceiling −1 to 5 · An opponent targeted by this power is
    pushed back 4 metres — 2 squares, thrown to the ground stunned for 1 round…

**and the pool reads `force 0 of 5 (max 6)`** — current, ceiling and trueMax, the
three-value pool from `pools.dart`, projected for the first time.

**And the same character then swung:**

    Training Lightsaber · rolled 17 — d20 16 + attack 1 · needed 10 — hit · 6 damage · 12 left

⚠ **Armed and able to cast, in one character, in one fight.** `011`'s finding is
closed and the wire runs end to end.

**Casting with an empty pool refuses cleanly:** *"Force Push costs 6 and you have
0."* No jargon, no citation.

### ⚠ But the cast pays a cost and does nothing to the target

**After Force Push resolved, the trooper was `18 of 18`, in the same square,
adjacent — not pushed the 2 squares the text describes, not stunned, undamaged.**

**Compare the two lines the app produces:**

| | derivation shown | outcome shown |
|---|---|---|
| attack | `rolled 17 — d20 16 + attack 1 · needed 10` | ✓ `hit · 6 damage · 12 left` |
| ⚠ cast | `6f — 6 → 0 · ceiling −1 to 5` | ⚠ **none** — the power's *description* is printed instead |

**There is no Reflex save rolled, no damage rolled, no movement, no stun.** The
**cost** half is fully modelled and the **effect** half is prose. A player spends
their whole Force pool and the enemy is untouched.

⚠ **I am filing this as the next question rather than as a regression** — the
verb landed this slice and nothing claims the effects did. But the screen does
not say so, and *"suffers 1d6 per two Force levels — maximum 12d6"* reads as a
promise.

**Smaller, same screen:** the cast menu **does not mark what you cannot
afford** — at `force 0` it still lists `1 Force Push 6f · 2 Beast Control 6f`
with no dimming. You find out by pressing and being refused. **The app disables
with a reason everywhere else** — `Continue`, the premade row, the barred
classes — and this is the one menu that lets you try.

---

## ✓ 1 · The Medic is armed

    Hold Out Blaster · rolled 17 — d20 16 + attack 1 · needed 10 — hit · 2 damage · 16 left

**`PT-1477` holds for both of its classes.** ⚠ **And the spelling is now
consistent** — `012`'s `S1` is closed: the Medic's line reads **`Hold Out
Blaster`** without the hyphen, matching the Equipment screen and the data. The
hyphenated form I saw yesterday is gone.

## ✓ 4 · The droid Agent is armed

    Hold Out Blaster · rolled 17 — d20 16 + attack 1 · needed 10 — hit · 2 damage · 16 left

`IG-Seven`, Astromech Agent — **the droid table arms too.**

## ✓ 2 · `item_unresolved` — and it is neither a second path nor a contradiction

**`Kesh Alaan` took the §4a upgrade and recorded:**

    character.grant-resolved
      { "taken": "item", "kind": "upgrade",
        "item_unresolved": "this profession grants an upgrade to what the class
                            already carries, and nothing applies it yet — no item was added" }

**A clean sentence. No §4a label, no citation, no document name.**

⚠ **So my open question resolves as a BUILD difference, not a class one.** The
Agent I reported in `012` recorded the raw §4a label at **12:24**; the app moved
to `792187e` at **12:59**. **Same grant kind, same profession — different
build.** `012`'s `S4` is closed, and I was wrong to suspect a second path.

## ✓ 3 · Only ONE array does not arm, and it is the correct one

**I simulated the resolver's own rules** — first token before `·`, strip a
leading count, split on 2+ spaces, `NONE` → unarmed-by-design, else exact match
against `equipment.toml` rows in `{Melee - base weapons, Ranged, Lightsabers}`:

    class_arrays.toml   ⚠ Brawler   UNARMED-BY-DESIGN   cell='NONE'
    droid_arrays.toml   (none)

**Every other array in both tables resolves.** ⚠ **So the five became one, and
the other four were `Agent` and `Medic` in both tables — exactly `PT-1477`'s
four.** The hyphen armed all of them, and the only remaining non-arming array is
the one where that is right.

⚠ **My earlier count was wrong and this corrects it:** in `012` I said I had
checked one of five and not identified the rest. **There is no list of four to
find — they were `PT-1477`'s, and they are fixed.**

---

## ✓ AND `012`'s HEADLINE IS CLOSED, ON SCREEN

**`Bran Vex`, Human Brawler, in a fight:**

    sith-trooper.command-deck.39: 18 of 18 · Bran Vex: 11 of 11
    · the array names no weapon — this class starts with its hands

**That is the record's own sentence, shown to the player** —
`play_screen.dart:775` now reads `eq['unarmed'] ?? eq['weapon_unresolved']`, and
the hardcoded *"your record carries no [equipment]"* string is gone from the
tree. **The bracketed `[equipment]` went with it.**

**And the Equipment screen fixed it with the app's own idiom, which is what I
hoped for:**

    weapon    —
    kit       Adrenal Strength · Sparring Gloves
    empty by design — implant · head · hands · arms · belt
                    · and the weapon slot: the class feature is the weapon

⚠ **`NONE` in shouting capitals is gone**, the row is an em-dash, the
`consumable` label became **`kit`**, and *"the class feature is the weapon"* says
the thing the screen had never said. **A Brawler now reads as designed rather
than as broken.**

**`012`'s `S2` is closed too** — the death line now reads *"YOU FALL. The fight
ends and you stand at 1 — anyone left down stands at 1 when combat ends"* with
**no `PT-559`**.

---

## ⚠ Scoped negatives

**Built and fought:** Jedi Guardian (cast + attack) · Medic · Astromech Agent ·
Brawler. **Data-simulated:** every row of both array tables against the
resolver's rules.

**NOT checked:**

- **Whether any power's effect is modelled anywhere.** ⚠ I observed **one**
  cast of **one** power. `Beast Control` is untested, and I did not read the
  engine for a cast-effect path — **so "does nothing" is an observation of Force
  Push against one target, not a proof about all powers**
- **Whether the Force pool restores** — `pools.dart` has `restore`, `sleep` and
  `meditate`; I emptied the pool and never got it back, and **I did not test
  whether resting or reloading refills it**
- **The ceiling drop.** `−1 to 5` matches `ForcePool`'s three values, but **I do
  not know what re-raises a ceiling**, or whether it is meant to
- **A droid Medic** — I did the droid Agent; the fourth of `PT-1477`'s four is
  confirmed only by the resolver simulation
- **Casting outside a fight** — I only pressed `f` mid-encounter
- **Any window size but 1280×720**

**Not re-filed:** the §4a label itself, the droid gender assertion. **Reported
as CLOSED rather than re-filed:** `012`'s Brawler message, `NONE`, the hyphen,
the `PT-559` citation, and the §4a label in the record.

**No exception, no overflow, nothing red.**

---

## Data

**Four new saves — 16 now.** ⚠ **`kesh-alaan.sav` is the one to keep:** the only
save carrying **a weapon path AND two powers**, and the first character able to
do both. `bran-vex.sav` is the Brawler acceptance; `wren-ossik.sav` and
`ig-seven.sav` are the Medic and droid-Agent confirmations.

**I deleted nothing and fixed nothing.**
