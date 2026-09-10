# 033 · The Gamorrean swings at fourteen — twice, for two different reasons, and Loom shows the author neither

**From `Tester`. Unrequested number.** `PT-1512` followed: packages backed up to
`BK9/` and saves to `SV-T032/` **before the app was opened**.

**⚠⚠ THREE BUILDS, AND EACH FINDING BELONGS TO EXACTLY ONE.** The tree moved
under me twice while I worked, both times deliberately — Coder was landing
`PT-1593` from my `032`.

    §1, §2   app fe39ada · Lodestar e7a9fbd · Lens 6b55219      built 11:45
    §3       Loom dafc553  (pins Lodestar e7a9fbd — the same engine)  built 11:52
    §4, §5   app df36271 · Lodestar 0cd34bb · Lens 6b55219      built 12:00

**Every build was made on a CLEAN tree with the app's `resolved-ref` checked
against `Lodestar` HEAD.** As I write: **`Loom 0dd361b`** (moved after `§3`),
app `df36271`, `Lodestar 0cd34bb`, all clean.

**⚠ CONTAMINATION, declared.** This run rewrote `grave-digger.sav` and
`grukk-ironjaw.sav`. **Both restored from `SV-T032/`; all 20 saves verified
byte-identical to pre-run.** The only package changes left behind are the two
deliberate fixtures in `§7`.

---

# ⚠⚠ 1 · THE GAMORREAN SWINGS AT FOURTEEN. `PT-1533` HAS NOT LANDED, AND I CAN NAME THE LINE

**`grukk-ironjaw.sav` — Gamorrean duelist, bought `str 14`, vibroblade
equipped.** `species.toml` gives a Gamorrean **`+4 Strength, −2 Dexterity, −2
Intelligence, −2 Charisma`**, so the blow should read `+ Strength 4`.

    Vibroblade · rolled 18 — d20 16 + attack 0 + Strength 2 · needed 13 — hit

> **⚠⚠ `+ Strength 2`. The modifier of the BOUGHT 14 — the same number, on the
> same line, as `TEST 026`.**

## ⚠⚠ And Dexterity proves it is not one ability going wrong

**On the same screen, one line above:**

    defence base 10 + Dexterity 2 = 12

**Bought `dex 14`; a Gamorrean's is `−2` → 12 → modifier `+1`.** It reads **2**.

> **⚠⚠ TWO ABILITIES, TWO DIRECTIONS (`+4` and `−2`), BOTH THE BOUGHT SCORE.
> That is not a species lookup that missed; it is a lookup that never ran.**
>
> **⚠ And the wrong Dexterity makes Grukk HARDER TO HIT than a Gamorrean is —
> `needed 12` where it should be `needed 11`. The defect is not only on the
> player's own blow.**

## ⚠⚠ THE LINE. `_ability` IS CORRECT AND THE MAP IS BUILT WITH THE WRONG KEYS

`play_screen.dart:1652` is right — it adds `widget.abilityAdjustments[key]`.
`main.dart:387` fills that map, and `abilities_screen.dart:8` declares:

    enum Ability {
      str('Strength', 'STR'), dex('Dexterity', 'DEX'), … cha('Charisma','CHA');
      final String name;               ⚠⚠ SHADOWS Dart's own `EnumName.name`
      const Ability(this.name, this.abbr);
    }

**So `Ability.str.name` is `"Strength"`, not `"str"`** — an instance field beats
the extension getter. And `main.dart:395` builds the keys with it:

    (e.key == Ability.intl ? 'int' : e.key.name): e.value,

**⚠ I measured this rather than reasoning about it** — a throwaway Dart file
copying only the enum declaration, run in the scratchpad:

    keys the adjustment map is built with: [Strength, Dexterity, Constitution,
                                            int, Wisdom, Charisma]
      _ability("str") finds adjustment? false
      _ability("dex") finds adjustment? false
      _ability("con") finds adjustment? false
      _ability("int") finds adjustment? TRUE
      _ability("wis") finds adjustment? false
      _ability("cha") finds adjustment? false

> **⚠⚠ FIVE OF SIX KEYS NEVER MATCH, AND `int` IS THE ONLY ONE THAT LANDS —
> BECAUSE IT WAS THE ONE SPECIAL-CASED.**

**⚠ AND THE COMMENT ON THAT LINE IS THE MISTAKE, WRITTEN DOWN:**

> *"⚠ `intl` IS THE ENUM NAME AND `int` IS THE RECORD'S KEY — `int` is a Dart
> keyword, which is why they differ."*

**The author noticed that ONE member's enum name differed from the record's key
and concluded the other five agreed.** The custom `name` field means **none of
them do.** `int` was patched by hand and is the only one that works.

**⚠ It is untestable through the seam it fails at.** `_ability` is correct in
isolation and the map is correct in isolation; **only the pair is wrong**, and
nothing joins them but a string.

---

# ⚠ 2 · AND VITALITY IS THE CONTROL, NOT THE EVIDENCE — a correction

**The brief said to check the vitality because a Gamorrean's Constitution
adjustment changes what it can take. ⚠ A Gamorrean has no Constitution
adjustment** — `+4 Str, −2 Dex, −2 Int, −2 Cha` and nothing else.

    Grukk Ironjaw: 5 of 10      ⚠ con 14 → +2 · d8 duelist level 1 → 8 + 2 = 10

**10 is what an adjusted and an unadjusted read BOTH produce**, so this reading
cannot distinguish them. **It is the control that shows the arithmetic is
otherwise sound, and I would have reported a pass if I had stopped there.**

> **⚠ The ability that discriminates for a Gamorrean is DEXTERITY, and it is on
> the defence line — `§1`.** For a species test to exercise vitality it needs
> one of the **21 species that adjust Constitution** — `Nautolan +2`,
> `Bothan −2`, and so on.

---

# ⚠⚠ 3 · LOOM WRITES THE SPECIES AND SHOWS THE AUTHOR NOTHING IT DOES

**✅ The writer half has landed.** `New creature` now carries the 35-button
species list below the abilities row, single-select, none preselected. I made
one and the file is right:

    [character]
    name       = "Probe Tusk"
    class      = "soldier"
    species    = "gamorrean"        ⚠ WRITTEN
    [abilities]
    str = 14

## ⚠⚠ But the derivation line does not move, and it is the one surface built to show a derivation

**`STUDY 28` asked for `derived · override · result` after seeing Aurora's
`Calculated 2.19 · Adjustment 0 · Challenge Rating 2`, and `030 §5` praised it
for arriving. It ignores the species.**

With `con 10` and a `d8`:

| species picked | Constitution adjustment | the line reads |
|---|---|---|
| *(none)* | — | `derived 8 · override 0 = vitality 8` |
| **Gamorrean** | none | `derived 8 · override 0 = vitality 8` ✅ correct |
| **⚠⚠ Nautolan** | **`+2 Constitution`** | **`derived 8 · override 0 = vitality 8`** |

**Nautolan's `+2` makes the modifier `+1` and the derived vitality `9`.** The
button was lit — I checked the screenshot rather than assuming the click landed
— **and `derived` did not move.**

> **⚠⚠ THE ONE ROW IN LOOM THAT EXISTS TO SHOW ITS WORKING SHOWS THE WRONG
> WORKING**, and it does it for the exact quantity `PT-1536` says the adjustment
> reaches.

**⚠ And nothing else on the sheet moves either.** Picking Gamorrean leaves
`str 14` on screen. **An author choosing a species is told nothing about what
they just chose** — not the adjustments, not the resulting scores, not the
`bred_to_the_axe` grant. **The species button is the only control in the dialog
with no visible consequence.**

---

# ⚠⚠ 4 · AND A LOOM-AUTHORED GAMORREAN DOES NOT HIT LIKE ONE — a SECOND cause

**`probe-tusk` placed at `1,7` in `a03-probe-yard`, walked into on `df36271`:**

    probe-tusk.probe-yard.05: unarmed · rolled 19 — d20 16 + attack 1
        + Strength 2 · needed 13 — hit · 3 damage

**`species = "gamorrean"`, `str = 14`, and it swings at `+2`.**

## ⚠⚠ THIS IS NOT `§1`'s BUG. IT IS A DIFFERENT ONE, AND IT IS SIMPLER

`round.dart:499` —

    Combatant combatantFrom(OpenedCharacter template, {…}) {
      final con = template.abilities.con;
      …
      strengthModifier: (template.abilities.str - 10) ~/ 2,

> **⚠⚠ THERE IS NO ADJUSTMENT STEP AT ALL. `OpenedCharacter` CARRIES `species`
> — `character_open.dart:228` reads it — and the function that turns a
> blueprint into a combatant never asks for it.**

**So the same wrong number has two unrelated causes:**

| path | species reaches the read? | why not |
|---|---|---|
| **player** | ✗ | the map is keyed `"Strength"` and read as `"str"` — `§1` |
| **creature** | ✗ | **`combatantFrom` has no adjustment step to key wrongly** |

**⚠ And the blueprint's `species` is not unused — it reaches two consumers and
neither is mechanical:** `attack.dart:132` uses it for **target kind**
(`droid` vs `sentient`), and `play_screen.dart:1200` for **speed**. **It reaches
what a power may be aimed at and how far it walks, and not what it hits with.**

---

# ✅ 5 · `PT-1593` CONFIRMED ON THE BOARD, AND `PT-1594` IS A LABEL

**`032`'s headline is fixed and I used it rather than reading it.** Six squares
from `probe-tusk`, on my end-turn:

    probe-tusk.probe-yard.05: unarmed ·  out of reach — unarmed reaches 1
    square and Grave Digger is 6 away

> ✅ **It names the reach AND the distance AND the weapon**, and — as the commit
> says — **it does not print a `needed 13`, because nothing was rolled.** *"A
> miss is a swing that failed; this is a swing that could not be taken."*

## ⚠ `PT-1594` changed the LABEL, and the screen is unchanged

**Re-run of `032 §2b` on `df36271`, same squares:**

    a03-probe-yard · 5, 3      ◆ 4 → 2 move
      press Up onto plain floor
    a03-probe-yard · 5, 2      ◆ 3 → 1 move        ⚠ I have 3, as before

**The visible number is identical to the broken build.** The fix is in the
accessible label — *"the label says what it is conditional on"* — and the gear
pip's is the same shape: `unspendable: 'nothing spends it yet'`, with the pip
still drawn bright and still labelled `gear` on screen. **I zoomed the strip to
be sure.**

> **⚠ I am not calling either wrong — the commit argues the caveat belongs in
> the label "because the shape cannot carry it", and that is a real argument.
> ⚠ But BOTH corrections are invisible to a sighted player**, and both defects
> were found by reading the screen. **The reader who found it cannot see the fix.**

**⚠ NOT MEASURED: the label text itself.** I could not read Flutter's semantics
tree from outside the process. **Everything I say about the new labels is a
source read of `df36271`, not an observation.**

---

# ⚠⚠ 6 · THE CLEAVE SHAPE — and the shipped data already cites the table that does not exist

**`PT-1592` settles ours as a SWEEP: two adjacent enemies at once, not d20's
on-kill version. `ATTACKS-05 §139` writes three rows:**

    Cleave          Level 1, requires Strength 12   two adjacent enemies   Attack −3
    › Wide Cleave   Level 4                         three adjacent enemies Attack −2
    ›› Great Cleave Level 8                  every enemy within 2 squares  Attack −1

## ⚠⚠ First: this is not a gap nobody noticed. The VALIDATOR ALREADY DECLARES IT

`record_validate.dart:260`, rule **10 of 12**, and it is **one of the two the
play footer reports as `2 rules unchecked`** on every character I have loaded:

> *"every chosen feat's prerequisites are met"* — **`feats.json` carries no
> prerequisite field. Chain order is implied by `is_chain_head` and nothing
> states a prerequisite.**

**⚠ So `031`'s "no ability-requirement field" was already written down, in
machine-readable form, and surfaced to the player.** I should credit that rather
than claim it. **⚠ One stale word in it: it says `feats.json`, and the shipping
file has been `feats.toml` since `PACKAGE-FORMAT-01 §3c` chose TOML.**

## ⚠⚠ AND FOUR SPECIES RECORDS CITE ATTACK CHAINS BY NAME

**In `species.toml`, which DID ship:**

> `bred_to_the_axe` — *"A Gamorrean receives **the Power Attack chain's tier 1**
> free at 1st level, in addition to **the four attack credits every class
> receives**."*
>
> `echani_combat_training` — *"Grants access to **the Echani Strike attack
> chain** from character level 5."* (three records)
>
> `fixed_armature` — *"A chassis reaches **eleven ranged attack chains** and no
> melee at all — **thirty-three tiers** against a Combat class's **forty**."*

> **⚠⚠ THE DATA NAMES TWO CHAINS, A CURRENCY THAT BUYS THEM, AND THE TABLE'S
> SIZE — ABOUT FORTY TIERS — AND THE TABLE IS IN NEITHER `rules/` NOR
> `data/extracted/`. I looked in both.**
>
> **⚠ And it is on the species I just tested.** `probe-tusk` is a Gamorrean that
> should have Power Attack tier 1 for free and has no table to take it from.

## ⚠ What the shape needs — the fields, from the three rows

**`feats.toml`'s ten columns (`id · name · chain · is_chain_head · section ·
effect · availability`, plus `description` 104/320, `level` 91/320, `note`
22/320) hold three of what is needed and cannot hold five.**

| field | from the rows | in `feats.toml`? |
|---|---|---|
| `id` · `name` · `chain` · `section` | — | ✅ as-is |
| `level` | 1 · 4 · 8 | ✅ exists, 91 of 320 carry it |
| **`tier`** | 1 · 2 · 3 | ⚠ **NO.** `is_chain_head` is a **bool** — it separates the head and **leaves Wide and Great unordered.** Today only their differing `level` accidentally sorts them. `powers.toml` already has `tier` |
| **`requires`** | **`Strength 12`** | ⚠⚠ **NO — and this is rule 10** |
| **`targets`** | 2 · 3 · **all** | ⚠ **NO.** `powers.toml`'s `targets` is a **kind** list (`sentient`/`beast`/`droid`), not a count |
| **`within`** | 1 · 1 · **2 squares** | ⚠ **NO** |
| **`attack_modifier`** | **−3 · −2 · −1** | ⚠ **NO** — `effect` is prose for all 320, and this number enters `attackTerms` |

**⚠⚠ AND `requires` MUST NOT COPY `powers.toml`.** That file has
`prerequisites = ["Character Level 9", "Throw Lightsaber"]` — **free-text
strings**, and the only code that touches them is
`records.dart:694: openAtFirstLevel => prerequisites.isEmpty`, **a presence test
that never parses one.** **Copying that shape would reproduce, in a second file,
exactly the unenforceable requirement rule 10 already reports.**
`Strength 12` must be structured: `requires = { str = 12 }`.

**⚠⚠ AND `within` IS THE FIELD THAT MAKES `PT-1581` PAY.** *"Adjacent"* is
`within = 1` and *"every enemy within 2 squares"* is `within = 2` — **one field,
one unit, and both tiers then read `squaresBetween`.** Written as *"adjacent"*
versus *"within 2 squares"* they become **two measurements**, which is the
defect `PT-1581`'s commit exists to prevent. **`areAdjacent` — still zero
callers, re-checked on `0cd34bb` — is what `within = 1` compiles to.**

**⚠ ONE THING THE THREE ROWS DO NOT SAY, and I am not inventing it: ADJACENT TO
WHOM?** The attacker, each other, or the first target? *"Two adjacent enemies"*
admits all three, and they are different rules on a board. **`Great Cleave`'s
*"every enemy within 2 squares"* is unambiguous — within 2 of the attacker — so
the tier that is clearest is the one that arrives last.**

**⚠ And a separate file, on the product's own precedent.** `two_weapon.toml` and
`powers.toml` both exist because `feats.toml`'s columns did not fit. Five new
columns null for 320 rows is the same argument, and `availability` is a sixth
reason: **feats are `selectable`; chains are bought with "attack credits", a
currency the species data names and nothing implements.** → **`attack_chains.toml`.**

---

# 7 · Scoped negatives, and what I left behind

- **`§1` and `§2` are `fe39ada`; `§4` and `§5` are `df36271`.** I re-read the
  enum, `main.dart:395` and `combatantFrom` on the **later** build before
  claiming either still stands. **Both do.**
- **⚠ I did not open a character sheet.** `026` read `STR 18` off one; I proved
  the same thing from **two abilities moving in opposite directions**, which
  needs no sheet. **The sheet's own value on `fe39ada` is unverified by me.**
- **⚠ The new accessible labels (`§5`) are a SOURCE READ.** Not observed.
- **`PT-1596`'s free interaction — NOT TESTED.** `a03-probe-yard` has no
  connection and `probe-tusk` has no conversation, so I could reach neither door
  nor speech. **The one of the three fixes I did not exercise.**
- **`wantRange` — still read by nothing**, and the commit says so itself: *"a
  doctrine that wants to be close has to be able to MOVE, and nothing moves an
  enemy."* **I did not re-census the other spenders on `0cd34bb`.**
- **The gear pip** is still drawn bright on `df36271`; `spendGear` still has zero
  callers. **The verb is still absent — only the label changed.**
- **`doors`/`waypoints`, the item dialog and the wizard `owner` are `dafc553`.**
  Loom moved to `0dd361b` after I built and **I did not re-check them on it.**
- **I did not press `Generate` in the conversation wizard**, so the bogus owner
  was never written. **What a generated file containing it does is untested.**
- **Painting tiles in Loom** — still not done, **nine sessions running.**

## What I left behind — two deliberate fixtures, and nothing else

    blueprints/characters/probe-tusk.toml   ⚠ species = "gamorrean", str = 14
    a03-probe-yard  tag_seq 5
      probe-tusk.probe-yard.05  at 1,7      ⚠ the Loom-authored Gamorrean

**`probe-tusk` is the bed for `§4` and it is the one fixture that proves a
species reaches the FILE and not the BLOW.** It is deliberately a plain
`soldier` with `str 14` so the expected `+4` and the observed `+2` differ by
exactly the adjustment.

**⚠ Everything else is restored.** All 20 saves byte-identical to `SV-T032/`;
`diff -rq` against `BK9/` reports only the two fixtures above.

**Backups: `BK3/`–`BK9/`, `SV-T031/`, `SV-T032/`.**
