# 006 · A code review of every file, and the eight things it found

**⚠ THIS REQUEST IS A DIFFERENT SHAPE FROM THE FIVE BEFORE IT, AND SAYS SO.**
`README.md` is clear that *"a request is a JOURNEY TO WALK, not a suite to
run"* and that *"a request that says 'run the app suite' is a defect in the
request."* **That still governs and §1 is still a journey.** But this request
comes out of `PT-2325`'s codebase-cleanup thread rather than out of a build,
so some of what it claims is about **code that cannot be walked to** — a
latent gap, a duplicated rule, a guard that cannot fail.

**⚠ SO EVERY CLAIM BELOW IS MARKED.** `WALK` is a journey. `READ` is a
statement about the source that `Tester` can check without launching
anything. **Do not spend a session trying to walk a `READ`.**

---

## ⚠⚠ 0 · READ THIS FIRST — THE TREE WAS BEING EDITED WHILE THIS WAS WRITTEN

**Another `Coder` session is working in this tree right now.** At the moment
of writing, `Lodestar` had **six modified files and one untracked new file**:

    M lib/lodestar.dart   M lib/src/abilities.dart   M lib/src/combat.dart
    M lib/src/conditions.dart   M lib/src/modifiers.dart   M lib/src/round.dart
    ?? lib/src/timed.dart                    ← written 14:41, one minute before

**That is `PT-2325 (3)` being built** — the `Timed` interface, `round.dart`
down 83 lines. **It is not mine and I did not touch it.**

**⚠⚠ I DID NOT RUN ANY SUITE, DELIBERATELY.** A suite run against a tree
somebody else is mid-edit in reports on their half-finished work, not on
mine — and `README.md` already says a green suite `Tester` has to reproduce
is a wasted turn. **The last number I have is `Lodestar`, 1,366 green, taken
at the start of this review before those edits existed.**

**⚠ LINE NUMBERS BELOW ARE FROM 14:45 AND WILL MOVE.** `combat.dart` shifted
by about a thousand lines under me during the review. **Every finding names
its symbol as well as its line; trust the symbol.**

---

## 1 · The journey — `WALK`

**Two of the eight are visible in play. Do these two first; the rest are
reading.**

### 1a · Evasion, twice

1. Make or load a character **with the `Evasion` feat** — it is on the
   Scout's list, `feats.toml:418`.
2. Get into a fight where a **frag mine or a thrown grenade** goes off on
   you, and **make the Reflex save**. Note the damage.
3. Now have a **Force power** land on you that saves against Reflex for
   half — **`Force Wave`** or **`Overload`** — and **make that save**. Note
   the damage.
4. **Compare the two numbers against what the screen says the save did.**

### 1b · A critical with a weapon that carries "massive"

1. Equip one of these — they are in `items.toml` and they carry a
   `massive` row: **Mandalorian Heavy Repeater · Bastila's Lightsaber ·
   Bacca's Ceremonial Blade · Trandoshan Sword · Trandoshan Double-Blade**.
2. **Land a critical hit** with it.
3. **Read the damage line, then read how much vitality the target actually
   lost.** Compare the two numbers.

---

## 2 · What `Coder` claims is true — numbered, so a reply can name one

**⚠ Claims 1 and 2 are DEFECTS I am confident of and have traced end to
end. Claims 3 to 6 are for the OWNER, not for me. Claims 7 and 8 are small.**

---

**⚠⚠ CLAIM 1 — `WALK` — EVASION WORKS ON A GRENADE AND NOT ON A FORCE POWER.**

There are **two** sites where a burst of damage meets a save, and **only one
reads the feat.**

    play_screen.dart:9208   the item/grenade/mine path
        amount = afterSave(e, amount,
                   evasion: who.handle == _me?.handle && _hasEvasion).amount ?? 0;

    play_screen.dart:9971   inside _applyPower (line 9390), the Force power path
        else if (onSave == 'half') { amount = amount ~/ 2; }

**The power path does not call `afterSave`, does not consult `_hasEvasion`,
and does not read `save_kind` at that site at all.** Verified: the string
`vasion` does not occur anywhere between lines 9700 and 10050.

**Two shipped powers are exactly the shape `Evasion` exists for** —
`save_kind = "reflex"` with `on_save = "half"`:

    Force Wave    1d6, cap 12
    Overload      1d6, cap 12

**So a Scout with `Evasion` who makes the save takes ZERO from a frag mine
and HALF from `Force Wave`.** Same feat, same save type, same stated on-save
outcome, two answers.

> **⚠ `_hasEvasion`'s own comment says *"THE ENGINE DECIDES WHAT IT DOES, NOT
> THIS GETTER."*** That is true of the path that asks the engine. **The power
> path never asks it.**

---

**⚠⚠ CLAIM 2 — `WALK` — MASSIVE CRITICAL DAMAGE IS ROLLED, PRINTED, AND NEVER
DEALT.**

`resolveAttack` (`combat.dart:664`) rolls `weapon.massiveCriticals` on a
critical and adds them to `rolled`, which becomes `DamageOutcome.total`.
**It does not put them in any `DamagePart`** — `parts:` is built at
`combat.dart:710` and the massive dice are not in it.

    sum(parts) = faces + bonusFaces + bonusFlat + mods
    total      = faces + bonusFaces + bonusFlat + mods + massive

**And the app deals PARTS, not TOTAL** — `attack.dart:1544-1573`:

    resisted = resistedParts(a.damage!.parts, ...)
    shielded = afterShieldParts(resisted, ...)
    applyDamage(amount: shielded.landed)

**So the target loses `total` minus the massive, while `DamageOutcome.line`
prints `damage $total`.** The number on screen is bigger than the number
taken off the target, by exactly the massive roll.

**66 item blocks in `items.toml` carry `stat = "massive"`**, and
`attack.dart:1127` populates `Weapon.massiveCriticals` from `stats.massive`
— `PT-2207` wired it, its own note reading *"45 massives reached a
`FittedStats` and stopped."*

> **⚠⚠ AND THE GUARD FOR THIS EXISTS AND CANNOT FAIL.**
> `resistance_test.dart:186`'s `addsUp()` asserts
> `afterResistanceParts(d.parts, resists: {}) == d.total`, and its own
> comment calls it *"THE INVARIANT, AND IT IS THE POINT OF THE WHOLE SLICE
> … a split that lost or gained damage would be `PT-1468`'s two answers to
> one question."*
> **Its fixture is `FixedDice(List.filled(40, 3))` — the d20 always rolls 3,
> so `mult` is never above 1 and the `if (mult > 1)` massive branch is
> unreachable** — and no fixture weapon carries a massive anyway. **Two
> independent reasons the guard cannot see the case it is named for.**
> **The one-line fix to the guard: put a massive weapon and a natural 20
> into `addsUp`'s set.**

---

**⚠⚠ CLAIM 3 — `READ` — OWNER — THE ENGINE HAS THREE FOLDS OF
`RULES-01-v2 §4` AND TWO OF THEM DISAGREE.**

`§4`, in its own words, carries two rules:

> **Master rule:** where modifiers don't stack, apply the **best bonus and
> the worst penalty**.
>
> **Penalties** stack regardless of type unless from the same source.

Three functions implement it:

    bonusOn / penaltyOn   abilities.dart:360, 392   SUM both directions
    modifierOn            modifiers.dart:135        best bonus, WORST penalty
    mergedSaveBonuses     saves.dart:197            best bonus, SUMMED penalties

**The first two handle the same category of thing** — timed rows granted by
Force powers, carrying `roundsLeft`, `negatedBySave` and a `from`.
`AbilityPenalty`'s own doc argues for summing in as many words: *"it SUMS
rather than folding per `§4`. Two Force Screams are `−4`, not `−2` … this is
a stack of separate insults from separate castings."*

**`modifierOn` takes only the worst.** So **two Force Screams stack on an
ability score, and two debuffs do not stack on Defence**, and both are power
rows with a clock.

**⚠ AND THE TWO MEET INSIDE ONE EXPRESSION.** `saveTerms` builds
`Term('gear', worn)` through `mergedSaveBonuses` (penalties summed) beside
`Term('power', power)` through `modifierOn` (penalties worst-only). **One
Fortitude save's arithmetic applies two different penalty rules.**

`saves.dart:189` knows it is asymmetric and explains the asymmetry *within
its own function*. **Nothing anywhere notices it disagrees with
`modifierOn`.**

**Reachable, cross-chain** — same-chain rows replace by tier rank
(`PT-2309`), so the case needs two chains. On `attack`, two do:
**`Crush Opposition` (`−1`…`−5`)** and **`Improved`/`Master Battle
Meditation` (`−2`/`−4`)**. Both landing gives `−4` where `§4` reads `−7`.

> **This is an owner question — which fold is right — and not a `Coder` fix.**

---

**⚠ CLAIM 4 — `READ` — OWNER — THERE ARE TWO `on_save` VOCABULARIES AND ONE
OF THE MISMATCHES IS SILENT.**

    items   via effect.dart's _onSave      none | half | instead
    powers  via _applyPower's if-chain     negate | half | dice_only

Counted in the shipped shelf: `powers.toml` carries `negate` **54**, `half`
**15**, `dice_only` **1**. **Only `half` is common to both.**

**The mismatch runs both ways and only one way is safe:**

- an **item** effect stating `negate` is **refused at load, loudly** —
  *"`x` saves for `negate`, which this engine has no shape for"*
- a **power** stating `none` **matches no branch in the if-chain**, so the
  damage **silently stands in full** and the derivation line never mentions
  the save

**The second has no guard.**

---

**⚠ CLAIM 5 — `READ` — OWNER — A SET MINE'S IDENTITY IS ITS POSITION IN THE
LOG, AND THAT IDENTITY IS SAVED TO DISK.**

`remains.dart:143`:

    tag: 'mine.set.${out.length}.$area',

`ENGINE-INTERFACE-01 §2`, rule 1: **"NEVER EXPOSE AN ORDINAL … position-as-
identity [is] the defect that made KOTOR's own tables unextendable. Every
handle in and out is a name."**

**This tag is not internal.** It is written into the ledger as the `subject`
of `hazard.disarmed` and `hazard.sprung`, **both `campaign` lifetime**, so
it persists into save files.

**⚠ IT IS NOT BROKEN TODAY AND I CHECKED:** all three hazard kinds are
`campaign`, nothing compacts them, and `discardableSteps` covers chargen
steps only — so the prefix is stable and the indices hold.

**⚠⚠ THE LATENT FAILURE IS SILENT.** `setMinesIn` **`continue`s past any
`hazard.set` whose payload does not match the expected shape, without
incrementing.** One malformed or shape-changed set event shifts every later
index by one, and **every previously recorded disarm or spring then refers
to a different mine.** Counts and names still verify while the save is wrong.

---

**⚠ CLAIM 6 — `READ` — OWNER — `ability_penalty` IS NOT VALIDATED AT LOAD AND
IS DROPPED IN SILENCE WHEN IT FIRES.**

`effect.dart` refuses an `ability_damage` naming no valid ability, with a
reason. **`ability_penalty` gets no such branch** and loads cleanly. Then at
the moment it fires, `play_screen.dart:995`:

    final which = Ability.named('${e.effect!.ability}');
    if (which == null) return;

**A bare, silent return.** The mine or item goes off, nothing happens, and
nothing says why. That is `ENGINE-INTERFACE-01 §2` rule 4 — *"FAIL LOUDLY,
RETURN A REASON"* — and the corpus's most-counted fault, a rule applied to
one path and not the next.

**⚠ LATENT, NOT LIVE, AND I CHECKED:** all **3** `ability_penalty` rows in
the shipped `items.toml` name `dexterity`, and `powers.toml` has none.
**The gap is in the gate, and the gate is what an authored item would hit.**

---

**⚠ CLAIM 7 — `READ` — TWO-HANDED STRENGTH DAMAGE TRUNCATES WHERE IT SHOULD
FLOOR.**

`combat.dart:1711`, in `damageTerms`:

    ? (strengthModifier * 3) ~/ 2

**`~/` truncates toward zero.** `defence.dart` deliberately uses `.floor()`
and says so in capitals, for exactly this reason.

    strMod −1  →  (−3) ~/ 2 = −1      d20 reads floor(−1.5) = −2
    strMod −3  →  (−9) ~/ 2 = −4      d20 reads −5

**Positive values are unaffected, which is why it has never shown.**
**⚠ Flagged rather than asserted:** whether a `1.5×` multiplier floors a
**penalty** is a ruling. **The engine flooring in one derivation and
truncating in another inside the same damage chain is the part worth
raising.**

---

**⚠ CLAIM 8 — `READ` — A COUNT IN A COMMENT IS STALE BY ONE.**

`conditions.dart:77` reads *"eighteen conditions are named, ruled, and do
nothing yet."* **There are nineteen** — twenty named, one honoured. **The
same file says "nineteen" at two other places and `conditions_test.dart:51`
asserts `hasLength(19)`.** `held` was added as the twentieth at `PT-2264`
and this count was not carried.

---

## 3 · ⚠ What `Coder` could NOT see from where it sits

**This is the honest gap and it is large.**

**⚠⚠ I READ CODE. I DID NOT PLAY THE GAME, AT ALL, IN THIS WHOLE REVIEW.**
Every claim above comes from source, shipped shelf data, and the test
fixtures. **Claims 1 and 2 predict something a player would see and I have
not seen either of them happen.**

**What I cannot tell you about Claim 1:** whether an enemy ever actually
casts `Force Wave` or `Overload` at you, and whether a Scout with `Evasion`
is reachable through chargen today. **The code path is real; whether play
reaches it is yours.**

**What I cannot tell you about Claim 2:** whether a critical is landable
against the one trooper in the bed with a massive-carrying weapon, given
`README.md` says **nothing resolves equipment in play yet and `strike()`
still uses a fist.** **If the player cannot hold one of those six weapons in
a real fight, Claim 2 is true of the code and unreachable in the product —
and that is a finding I want back.**

**What I cannot tell you about Claim 3:** whether one caster can hold both
`Crush Opposition` and a `Battle Meditation`, and whether enemy doctrine
ever casts two debuffs at one target. **The engine-level disagreement is
proven by the two functions; the reachability is not.**

---

## 4 · What `Coder` already ran, with numbers

**⚠ `Lodestar`, 1,366 tests, all green** — run at the start of this review,
**before** the `Timed` edits described in §0 existed.

**⚠⚠ AND NOTHING SINCE, DELIBERATELY.** See §0. **Do not treat a red suite
today as a finding against this request without first checking
`git status` in `Lodestar`.**

**What I did run, and it is all reading:**

- a uniform sweep of `(x − 10) ~/ 2` across all four `lib/` trees
- a census of `on_save`, `condition_on_save`, `massive`, `ability_penalty`
  and the modifier rows in the shipped `base-rules` shelf
- a check of every public `Lodestar` name for a consumer outside its own file
- a check of every `const` collection whose doc comment states a count

---

## 5 · ⚠ KNOWN SCAFFOLDING — things that are NOT bugs

**`README.md`'s nine still stand and I am not repeating them.** Three more
that this review specifically touched:

| what you will see | why |
|---|---|
| **`defenceIsUnspecified` is dead code** | `@Deprecated`, kept on purpose so a reader meeting the old comment finds the ruling beside it. **Not an unused constant to delete.** |
| **`legalityOf`'s `divisor` is never assigned** | correct today — only `stunned` is honoured and it does not touch movement. **It is a placeholder with a reason.** |
| **nineteen of twenty conditions restrict nothing** | declared in full on purpose; `honouredConditions` is what runs and the gap is a test rather than a comment. |

---

## 6 · ⚠ WRONG versus UNDECIDED

**Claims 1, 2 and 8 are `DEFECT`** — wrong, and mine to fix.

**Claims 3, 4, 5 and 6 are `UNDECIDED`** — the code had to behave somehow and
no document settles which way. **File them for the owner, not against me.**
The rulings live in `MAIN_WORK/rules/RULES-01-v2.md §4`,
`MAIN_WORK/design/ENGINE-INTERFACE-01.md §2`, and
`MAIN_WORK/playtest/PLAYTEST-RULINGS-01.md`.

**Claim 7 is a `DEFECT` wearing an `UNDECIDED` hat** — the inconsistency is
real, the correct rounding for a penalty is a ruling.

> **⚠⚠ AND USE `MAIN_WORK/playtest/`, NOT `HANDOFF/docs/`.**
> **`HANDOFF/docs/PLAYTEST-RULINGS-01.md` is stale — it stops at `PT-1548`
> and is missing 775 rulings.** The canonical copy runs to `PT-2325`. **I
> checked three ruling numbers against the stale copy first and two came
> back absent; both exist.** Two of my own citations were wrong until I
> re-checked, and `README.md` calls `HANDOFF` *"what you read."*

---

## 7 · Data safety, and what is real

**I wrote nothing.** No source file, no shelf file, no save, no package.
**The only files this review created are this request and a scratch
findings log outside the repos.**

**⚠ The journeys in §1 are REAL PLAY** and will write real saves into
`~/.local/share/kotor-rpg/saves/`. That is the product working, not a test.

**⚠⚠ AND THE SHARED DISK — `TEST request 005`.** `/tmp` is a 3.9GB tmpfs
shared with whoever else is running. **If anything hangs, check `df` before
suspecting the code.**

---

## 8 · What not to touch

**Per `README.md`'s table: `Coder` writes `TEST/requests/`, `Tester` writes
`TEST/reports/`, and neither edits the other's directory, ever.**

**⚠⚠ AND DO NOT TOUCH `Lodestar`'s WORKING TREE.** Somebody else's
uncommitted `Timed` work is sitting in it — see §0. **Not a stash, not a
checkout, not a `git clean`.**

---

## ⚠ Two things I looked for and did not find — scoped, per §1 of the report rules

**`README.md` calls this *"the most under-valued half"*, so it is here.**

**1 · I swept every `const` collection in all four `lib/` trees for a doc
comment stating a count that the collection no longer has.** Seventeen
candidates came back; **sixteen were my own regex counting quoted strings
inside nested comments, and `matchKeys`' "3" was a `§3` reference.** **Claim
8 is the only real one.**

**2 · I checked every public name in `Lodestar` for a consumer outside its
own file.** 102 came back with none. **All but one are sealed result types
consumed without being named, or constants read within their own file.**
**The single genuinely unreferenced name is `defenceIsUnspecified`, and it
is `@Deprecated` on purpose.** **There is no dead public API in the engine.**

**3 · I read `Lens` in full** — four files. **`shouldRepaint` compares every
field it holds, each with the ruling that made it compare it.** Nothing
found.

---

## ⚠ Coverage — where this review actually went

**Say so plainly, because a negative is worth nothing without its scope.**

| repo | files | what they got |
|---|---|---|
| **`Lodestar`** | **50 of 50** | **every file read.** Most in full with comments; the rest code-only with the comments read wherever the logic looked wrong. |
| **`Lens`** | **4 of 4** | **every file read in full.** |
| **`Loom`** | **42** | **sweeps across all of them**, plus `new_creature.dart` and `manifest_writer.dart` read. **Not every file line by line.** |
| **`KOTOR-RPG-APP`** | **48** | **sweeps across all of them**, plus the damage, save, power and ability-modifier paths in `play_screen.dart` and `attack.dart` read closely. **Not every file line by line.** |

**⚠ So `Loom` and the app have had a net passed over them and a few rooms
searched. `Lodestar` and `Lens` have been walked.**

---

## ⚠⚠ And one thing that was already closed before I could report it

**`PT-2325 (2)` — the seven `abilityModifier` copies — is DONE and I
verified it rather than taking the commits' word.** The sweep that found
seven now returns **zero**: the only `(score − 10)` in any `lib/` tree is
`abilityModifier` itself, with its `.floor()`. **And the comment that
claimed *"One derivation now"* when it was not true has been corrected in
place rather than deleted** — `play_screen.dart:5044` now opens *"AND THIS
LINE USED TO END 'One derivation now.' — IT WAS NOT."*

**That is the claim this whole thread started from, and it is now true.**
