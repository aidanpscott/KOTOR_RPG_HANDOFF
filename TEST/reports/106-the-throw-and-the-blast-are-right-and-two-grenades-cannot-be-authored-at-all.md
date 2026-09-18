# TEST 106 — The throw and the blast are right, and two grenades cannot be authored at all

**Build under test.** KOTOR-RPG-APP `cda01b4` *"PT-2323: `o` throws a grenade"*. ⚠ **The working
tree was dirty** — `lib/play/play_screen.dart`, `lib/chargen/abilities_screen.dart` and
`lib/chargen/skills_screen.dart` all modified — so everything below was built from a `git archive`
of the commit, not from the tree. Lodestar **`54e21404`**, Lens `32b77e3b`; `package_config.json`
resolves to the checkouts that compiled, which are the ones I read the engine from. `fresh.py
--debug --build` printed `✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29
rules files, 65 standard blueprints.

Items 1, 2 and 5 confirmed. Items 3 and 4 **cannot be confirmed** — in both cases the grenade the
routing names cannot be resolved as an item at all, for two different reasons.

---

## 1. The throw lands at a location and the save decides — confirmed, in one throw

`Frag Grenade`, the catalogue's 20 piercing / DC 15 reflex / half-on-save. Board at the throw:
player (0,2), enemies at (1,1), (1,2), (3,2) and **(6,2)**.

```
throw Frag Grenade at nade-a.nd.01 —
  nade-a.nd.01 — d20 17 + reflex 1 vs 15 · 10 damage      made  18 ≥ 15  → half of 20
  nade-b.nd.02 — d20  2 + reflex 1 vs 15 · 20 damage      failed 3 < 15  → full
  nade-c.nd.03 — d20 15 + reflex 1 vs 15 · 10 damage      made  16 ≥ 15  → half
  Nader        — d20  4 + reflex 3 vs 15 · 20 damage      failed 7 < 15  → full
  · 2 left
```

- **No attack roll anywhere.** Every creature caught rolled a *reflex save* against the item's own
  DC. Nothing rolled against anyone's defence.
- **Half and full both appear in the same throw**, matching `on_save = "half"`.
- **The radius is read.** `nade-d.nd.04` at 5 squares from the centre is **absent from the list**
  and sat at `60 of 60` afterwards. Without it, "everyone took damage" and "the blast is not
  bounded" would read alike.
- Vitality agreed with every line: a `50/60`, b `40/60`, c `50/60`, d `60/60`.

## 2. Friendly fire includes the thrower — confirmed, and it spends the Action

`Nader — d20 4 + reflex 3 vs 15 · 20 damage`. The thrower stood 1 square from the centre, inside
the 2-square blast, failed his own save and took the **full 20**. Real, not assumed.

**And the budget:** immediately after throwing, attacking answered **"you have already acted"**,
the `action` dot was greyed and `gear` still lit. The throw spends the **Action**, as `PT-2323`
states — worth noting because the item's own effect row says `spends = "gear"`, so that field is
not what governs a throw.

## 3. ⚠ The ion droid bonus CANNOT BE AUTHORED — `plus_vs_droid` has a reader and no path

Two blueprints, identical but for one line:

| blueprint | `plus_vs_droid` | result |
|---|---|---|
| Ion Grenade | `30` | **`throw — no grenade`** — with three of them in the bag |
| Ion Grenade Plain | absent | `throw Ion Grenade Plain at nade-droid.dr.01 — d20 16 + reflex 1 vs 15 · 7 damage` |

`carrying — ion · ion · ion` confirmed the bag held them, so this is a **resolution** failure, not
a bag failure. The cause is in the data contract: `charge`'s own `takes` list is

```
damage = ["amount", "kinds", "save", "deploy"]
```

and `consumableFromBase` refuses an item for **extra** fields as well as missing ones. So any
blueprint carrying `plus_vs_droid` is refused outright — while `_grenadeLands` reads exactly that
key, `amount += bonus`, to apply the bonus. A reader with no authorable path to it.

**What the droid actually took was 7** — half of the 15 base — where the routed claim is 45 before
the save and 22 after. The flat-versus-multiplier question cannot be reached: nothing gets as far
as adding anything. I confirmed the arithmetic is written as a flat `+=` in the source, which is
what item 3 wanted, but that is a source reading and not an observation.

⚠ Note the catalogue rows cannot be blueprints either, on the same rule: every shipped grenade
writes `base = 20` where `takes` wants `amount`, and carries `spends`, which `takes` does not
admit. Blueprints are what `consumableAt` opens, so mine are authored to the parser's contract
with the catalogue's numbers — that part is fine. `plus_vs_droid` is the one field with nowhere
legal to live.

## 4. ⚠ The Adhesive Grenade does not entangle — and the routing contradicts itself here

Both variants in one bag, so whichever resolved would name itself:

```
throw Adhesive Grenade Saved at nade-a.nd.01 —
  nade-a.nd.01 — ⚠ condition is not thrown yet · nade-b.nd.02 — ⚠ condition is not thrown yet ·
  nade-c.nd.03 — ⚠ condition is not thrown yet · Nader — ⚠ condition is not thrown yet · 1 left
```

Two findings in one line:

1. **The shipped Adhesive Grenade never resolved.** It names *"Adhesive Grenade Saved"* — my
   variant with a save bolted on. `carrying — adhesive · adhesive · adhesive-saved` afterwards:
   both catalogued copies still in the bag, one saved copy spent. The catalogue row states no
   save, and `takes.condition` is `["condition","rounds","save","deploy"]`, so as shipped it is
   incomplete and cannot be carried as a consumable.
2. **Even with a save, no Entangle lands.** `_grenadeLands` has
   `if (e.does != EffectKind.damage) return '⚠ ${it.does} is not thrown yet'`. All four caught
   creatures got that sentence and finished at `60 of 60`.

⚠ **This is the routing disagreeing with itself, not a surprise about the code.** Item 4 asks me
to confirm Entangle lands, and the same message's *"NOT YET BUILT, DON'T EXPECT"* note excludes
*"thrown condition grenades … flagged as needing separate wiring, not yet done."* The Adhesive
Grenade is a thrown condition grenade. The note is right and the item is not built; I am reporting
it as unbuildable rather than as a defect, and flagging the contradiction so the next routing does
not ask for it again.

## 5. Grenade versus mine — confirmed in both directions

The refusal here is the **absence** of a verb, which means nothing on its own, so both halves were
run on the same board:

| bag | right-click bare ground | result |
|---|---|---|
| 2 × Frag Grenade | *no menu at all* | **`nothing to do there`** |
| 2 × Minor Frag Mine + 2 × Frag Grenade | **`Set mine`** offered | **`set — armed at easy (10)`** |

And in the second run the grenade still threw normally in the same session, with the full blast
resolution of §1. Afterwards: `carrying — mine · frag`, down from two of each — **each verb took
the right kind**, `Set mine` a `deploy = "placed"` charge and `throw` a `deploy = "thrown"` one.
A grenade can no longer be planted, and nothing about the mine or the throw regressed.

---

## An adjacent check, since it touches what I reported yesterday

`de55a3f` *"PT-2320: the strike site shields per part"* landed after TEST 105, and per-part
shielding could plausibly have made the ion hole per-part too — which is the defect TEST 105 §2
confirmed was avoided. It has not: `afterShieldParts` checks vulnerability **first and
whole-blow**, returning the untouched total if any part carries a vulnerable kind, and only then
sums the covered parts. TEST 105's ion result still describes this HEAD. Read from the source, not
re-run.

## Fixture note

⚠ **My scratchpad was cleared at the session boundary** — `mksave.py` and the launch/click helpers
were gone. I rebuilt the save writer from Lodestar's own `writeSave` in `save_file.dart` for the
header layout, and recovered the chargen event sequence by decoding a save the product had already
accepted, rather than reconstructing either from memory. Worth knowing that authored-save work
carries that restart cost across sessions.

## Not tested

- The Thermal Detonator's knockdown and thrown damage-over-time, as routed — both excluded by the
  brief, and the DoT grenade would hit the same `is not thrown yet` branch as the adhesive.
- Whether a thrown grenade's blast is bounded by line of sight as well as distance. `blastReaches`
  is passed `seen:` from the centre and the fixture is an open floor, so nothing there was
  exercised.
- A grenade thrown at maximum range. `grenadeThrowSquares` is 12 and the boards are 9 wide; the
  too-far refusal exists but was never reached.
