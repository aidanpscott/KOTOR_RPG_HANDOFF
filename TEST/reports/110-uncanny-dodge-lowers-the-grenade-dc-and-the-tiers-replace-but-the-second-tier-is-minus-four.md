# TEST 110 — Uncanny Dodge lowers the grenade DC and the tiers replace, but the second tier is −4

**Build under test.** KOTOR-RPG-APP `d060423` *"PT-2348: Uncanny Dodge reaches the two save
sites"*, **working tree clean**. Lodestar `36d4149c`, Lens `32b77e3b`; `package_config.json`
resolves to the checkouts that compiled, which are the ones I read the engine from. `fresh.py
--debug --build` printed `✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29
rules files, 65 standard blueprints.

The mechanism is confirmed on all three routed points. **One correction to the routing's own
numbers**, below.

## The readings

Four runs, one frag grenade (stated DC 15) thrown at an adjacent target so the thrower is caught
in his own blast. **The dice are identical in every run** — `d20 18 + reflex 7 + Dexterity 2` each
time — so the DC is the only thing that moves:

| the player holds | player's save line | DC | reduction |
|---|---|---|---|
| nothing | `Dodger — d20 18 + reflex 7 + Dexterity 2 vs 15` | **15** | 0 |
| `uncanny_dodge_1` | `… vs 13` | **13** | **−2** |
| `uncanny_dodge_2` | `… vs 11` | **11** | **−4** |
| **both tiers** | `… vs 11` | **11** | **−4** |

- **Item 1 — tier 1 alone reduces by exactly 2.** 15 → 13.
- **Item 3 — no feat, full stated DC.** 15, unreduced.
- **Item 2 — the tiers replace.** Holding both reads **identically to holding tier 2 alone**, which
  demonstrates replacement rather than inferring it from a number that merely happens to match.
  Summing would have given 15 − 6 = 9.

**And the sentence prints the DC actually rolled against.** In the tier-1 and both-tier runs the
*same line* shows the creature at `dodgee.dg.01 — d20 16 vs 15` and the player at `vs 13` / `vs 11`
— per-saver, and matching the roll rather than the item's raw number.

## ⚠ The routing's numbers are wrong, and the build is right

The brief says *"Uncanny Dodge has always stated 'Grenade DC −2' in its own text (both tiers)"* and
asks me to confirm the both-tiers case *"reads as −2 total, not −4."* It does not, and it should
not. The shipped data says:

```
uncanny_dodge_1   "Retains Dexterity bonus to defence when surprised. Grenade DC −2. Level 4 Scout."
uncanny_dodge_2   "Grenade DC −4. Granted at 7."
```

and the engine agrees, in both the rule and its own doc comment (*"and, one tier up, **Grenade DC
−4**"*):

```dart
int grenadeDcReduction(Set<String> feats) {
  if (feats.contains('uncanny_dodge_2')) return 4;
  if (feats.contains('uncanny_dodge_1')) return 2;
  return 0;
}
```

So the correct statement of item 2 is **"−4 total, not −6"**, and that is what I measured. The
defect the fix was guarding against — every Scout past level 7 holding both and summing them — is
closed; the figure it lands on is 4, not 2. I am reporting this as a mis-statement in the routing
rather than a defect, because data, engine and behaviour all agree with each other.

## Scope — the reduction is the player's, and that is the only reachable case

Both save sites read `_myFeats`, which folds `widget.character.feats`, and the throw site gates on
`who.handle == _me?.handle`, so a creature caught in the same blast never gets the reduction. That
is visible in every run above: the creature stayed at `vs 15` while the player dropped.

⚠ I checked whether that leaves anything unreachable, and it does not: **character blueprints
parse no `feats` key at all**, so no placed creature can hold Uncanny Dodge in the first place.
Correct as scoped, and worth recording only so the next person does not read the player-gate as a
gap — if creature feats ever become authorable, this is the line that will need revisiting.

## Fixture notes

- The player is both thrower and saver. A board of three differently-featted **creatures** would
  have read `vs 15` three times and proved nothing, for the reason above. The target is adjacent
  so the thrower stands 1 square from the blast centre and is caught by his own grenade
  (TEST 106 §2).
- ⚠ Every featted run showed **"Dodger · 1 rule about this character not checked"** in the status
  bar. That is my authored character, not the fix: I wrote the feats onto a Scout via
  `character.feat-taken` without the class grants that normally accompany them. Noting it so the
  notice is not mistaken for a symptom.

## Not tested

- The **mine spring** site, the other of the two the commit names. It uses the same
  `dcAfterDodge(dc, _myFeats)` call on the same feat set; I exercised the throw site because the
  thrower's own blast puts the reading and the control in one sentence.
- The floor at zero (`dcAfterDodge` clamps a negative DC to 0). It needs a grenade with a stated
  DC below 4, and the lowest in the catalogue is 15.
