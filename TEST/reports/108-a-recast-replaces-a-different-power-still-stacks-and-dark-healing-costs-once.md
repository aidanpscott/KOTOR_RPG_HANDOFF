# TEST 108 — A recast replaces, a different power still stacks, and Dark Healing costs once

**Build under test.** KOTOR-RPG-APP `380bdd2` *"PT-2336: a penalty replaces rather than stacking"*.
⚠ **`pubspec.lock` was modified in the working tree** — uncommitted, bumping Lodestar from the
committed `6a7a6ced` to `4032d57c`. Built from a `git archive` of the commit, so the pairing under
test is the committed one (Lodestar `6a7a6ced`, Lens `32b77e3b`), and it compiles and carries the
fix. `fresh.py --debug --build` printed `✓ FRESH — built from exactly this source`.
`check_shelf.py` green: 29 rules files, 65 standard blueprints.

All four routed items confirmed.

## How each of these is read

An ability penalty is a **score** the derivations re-read, so the accumulated total shows in the
`Strength` term of an attack line — not in the cast's own sentence, which only ever prints the
rows *that cast* applied and would look identical whether they stacked or not. The target carries
**Strength 18 (+4)**, Constitution 8 and Wisdom 3 at level 1: every `ability_penalties` row on
both Force Scream and Force Choke carries `on_save = "negate"`, so a made save would show nothing
and prove nothing. Against a level-12 Consular's DC 25 it fails reliably.

## 1. Three Master Force Screams — confirmed, it stays at Master's own −6

Pool `159 → 135 → 111 → 87`, twenty-four each, so all three genuinely cast:

| after | target's attack line | Strength score |
|---|---|---|
| baseline | `+ Strength 4` | 18 |
| Master Force Scream ×1 | `+ Strength 1` | 12 |
| Master Force Scream ×2 | `+ Strength 1` | 12 |
| Master Force Scream ×3 | `+ Strength 1` | 12 |

Stacked, three casts of −6 would be −18 — Strength 0, a term of **−5**. It never moved off **+1**.
The exploit is closed.

## 2. Force Slow twice — confirmed on a second carrier

Force Slow is the `modifiers` carrier rather than `ability_penalties`, and one of the rows that
was silent on `replaces`. Its −2 **defence** is read from the caster's own attack line, where
`needed N` is the target's Defence:

```
baseline        needed 13
Force Slow ×1   needed 11      pool 159 → 153
Force Slow ×2   needed 11      pool 153 → 147
```

The pool moving the second time is what says the cast really happened; stacking would have read
`needed 9`.

## 3. A different power still stacks — confirmed, and the clocks are independent

Master Force Scream (−6, ten rounds) then **Force Choke** (−4, three rounds) on the same target:

```
round 1   stackee.st.01 is stunned                              (Choke's own 2-round stun)
round 2   rolled 4 — d20 4 + attack 1 − Strength 1 · miss       18 − 6 − 4 = 8  →  −1
round 3   rolled 13 — d20 11 + attack 1 + Strength 1 · hit      18 − 6      = 12 →  +1
```

Round 2 reads **`− Strength 1`**, minus — both penalties standing at once. Round 3 is back to
`+ Strength 1`, because Choke's three rounds ran out while Scream's ten kept going. So the two are
additive *and* on separate clocks, which is a stronger reading than the sum alone: only the
same-power case was prevented, exactly as the ruling intends.

⚠ Force Choke stuns for 2 rounds and penalises for 3, so there is at most a one-round window in
which the target both acts and still carries the penalty. Round 2 is that window. A run that
sampled a round later would have seen `+1` and concluded the penalties did not stack.

## 4. Dark Healing — confirmed, the self-inflicted cost replaces

Read on the caster's own attack line; Dark Healing takes −2 Strength and −4 Constitution, with no
save, so it always lands.

```
baseline          + Strength 4      18
Dark Healing ×1   + Strength 3      16      pool 147 → 123
Dark Healing ×2   + Strength 3      16      pool 123 →  99
```

The pool moved both times. Compounding would have read **Strength 2** at Strength 14. Recasting is
now genuinely cheaper than it was, which is the ruled change rather than a regression.

## Fixture notes — two of my own errors, recorded

⚠ **My rebuilt `mksave.py` wrote the wrong event kind for powers.** I reconstructed the helper last
session after the scratchpad was cleared, and recovered the chargen sequence by decoding a save
the product had accepted — but that save was a **soldier with no powers**, so the power line was
the one part I filled in from memory. I guessed `character.power-learned`; the real kind is
`character.power-taken` with `{'id', 'at_level'}`, from `ledger_writer.powers()`. The save loaded
perfectly and the character simply knew nothing — *"you know no Force powers"* on the first cast.
A template recovered from a real artefact only covers the parts that artefact exercised, and the
part it did not cover is exactly where the guess survived.

⚠ **The launcher wrote an empty window id and every later click hung on it.** Two windows share
the app's PID and the real surface can appear later than a fixed sleep allows; the helper now
polls for the named window instead of sleeping and hoping. Separately, I reached for
`pkill -f sleep` to clear a stuck job and killed my own shell with it — the hazard my own notes
already name. No damage beyond the command.

## Not tested

- **A lower tier landing on a higher one.** The commit says it is now a no-op on the rows rather
  than a downgrade, which is the correction to what I reported for the Valor chain in TEST 104.
  My caster carried only Master Force Scream, so confirming it needs a save with the base tier as
  well; I did not re-author for it and am not claiming it either way.
- Crush Opposition and the Battle Meditation chain, the other two families named in item 2. Force
  Slow is the same `modifiers` carrier through the same `superseded`/`outranks` pair, and it is
  the one whose effect I could read exactly from my own action rather than from an enemy turn.
- The three guards the commit names. Running Coder's own tests is not a confirmation of behaviour.
