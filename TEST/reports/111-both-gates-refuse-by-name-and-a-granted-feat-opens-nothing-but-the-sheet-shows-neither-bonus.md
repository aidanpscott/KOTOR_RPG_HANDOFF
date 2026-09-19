# TEST 111 — both gates refuse by name, a granted feat opens nothing, and the sheet shows neither bonus

**Build.** App `02005d9` (tree clean), `pubspec.lock` resolved-ref
`463245ce`, and the pub-cache checkout `package_config.json` actually
compiles against is `Lodestar-463245ce`. Built from `git archive 02005d9`
into the scratchpad in 17.4s. `check_shelf.py`: 29 rules files and 65
standard blueprints identical to what the extracts generate.

**Verdict.** All four items confirmed. Both implant gates enforce and both
name their requirement precisely; the mask is unaffected by the implant's
refusal; and a granted feat does **not** satisfy another item's gate —
measured with the grant proven live at the same instant, not inferred.

One thing routed cannot be seen where the routing says to look, and it is a
real gap rather than a wording quibble: **neither bonus appears on the
character sheet**, and `gate-and-grant`'s own room cannot show them either.

---

## 0. The sheet does not carry worn contributions — and Coder's bed cannot show them

Item 1 says *"wear it, read the sheet. Confirm both bonuses land."* On
Coder's `gate-and-grant.sav`, loaded as authored, the sheet reads:

```
DEX        12  (+1)          ← the mask's +2 Dexterity is NOT here
Defence    11
Reflex     +3                ← the implant's +2 reflex is NOT here
```

Both items **are** worn and accepted — `Defence` shows a number rather than a
refusal — but neither bonus reaches that screen, and the code says why:

* `_characterScreen` takes `abilities` from `me?.abilities`, the **record's**
  scores. `abilitySources` is not folded in, so a worn ability change can
  never appear there.
* `ratingsFor` builds `Reflex` as class base + `abilityModifier(dex)`. It
  takes no `saveBonuses` parameter at all, so a worn save table cannot appear
  there either.

Both bonuses are real, but only inside a fight: worn abilities fold through
`Combatant.modifierOf` (`round.dart:518`) and the implant's table arrives as
`saveTerms`' `gear` term.

**And `gate-and-grant` has no fight to have.** `a01-fitting-room` is a 2×2
room with no creatures, and `_springsAs` builds its save from
`_fight?.saveCheckFor(...)`, falling back to a bare `Check(what: 'Save')` with
**no modifiers at all** when `_fight` is null. So in that package the
Dexterity is invisible on the sheet and there is nothing to read it against.

I built `tester-gate-grant` — the same wearer, a dummy adjacent to the spawn
and a 1-point mine one step away — and measured both there.

## 1. Both bonuses land, on two independent instruments

One Reflex save prints `reflex`, `Dexterity` and `gear` as separate terms, so
a single line reads both halves. Same `d20 16` in every run below (the dice
are deterministic across a fresh load), so these are exact pairs, not means.

| worn | enemy's attack line | mine's Reflex save |
|---|---|---|
| implant + mask | `needed 12` | `d20 16 + reflex 2 + Dexterity 2 + gear 2 = 22 vs 15` |
| **nothing (control)** | `needed 11` | `d20 16 + reflex 2 + Dexterity 1 = 19 vs 15` |

* **Dexterity +2 (mask, from the catalogue row).** Defence 12 vs 11, and the
  `Dexterity` term 2 vs 1 — two independent readings of the same +2 on the
  score.
* **Reflex +2 (implant, from the blueprint's own save table).** The `gear`
  term is `2` when worn and **absent** when not.

## 2. Constitution gate — the implant refuses, the mask does not

Constitution 11, everything else unchanged. The sheet's Defence row:

```
Defence    —
`Reflex Package` needs Constitution 12.
```

It names the item and the exact score. Only one line: nothing is said about
the mask. And the mask is demonstrably still working, from the same mine:

```
d20 16 + reflex 2 + Dexterity 2 = 20 vs 15
```

`Dexterity 2` — the mask is still on and still contributing — with **no
`gear` term**, the implant having contributed nothing. Note the three runs
read 22, 19 and 20: each combination is distinguishable from the other two.

## 3. Feat-chain gate — the refusal names every way in

Constitution restored to 12, `cybernetic_implantation` dropped:

```
Defence    —
`Reflex Package` needs `cybernetic_implantation` or
`advanced_cybernetic_implantation` or `master_cybernetic_implantation`.
```

All three tiers, as an OR. That is `requiresAnyFeat`'s stated behaviour —
*"the refusal names every way in, not the first one it tried"* — and it is
the `§12` column rather than the catalogue's display names.

## 4. The negative worth having — a granted feat opens nothing

I did not author a gate for this. `item_gates.dart`'s own comment names the
real case — *"`Droid Upgrade 2` is granted by one tool and gates 41
devices"* — and both halves ship:

* `d_tool_02` **Droid Upgrade Slot** grants `Droid Upgrade 2`, and is itself
  gated on `Droid Upgrade 1`.
* `d_device_13` **Droid Ion Blast Mark II** is one of the 41 gated on
  `Droid Upgrade 2`.

The volunteer holds `droid_upgrade_1` permanently and wears both, the tool
**first** in the equipment map — the order that would leak if the grant were
merged into the wearer.

```
`Droid Ion Blast Mark II` needs `Droid Upgrade 2`.
```

Exactly one refusal, and it is the gated device. The tool is not refused,
which is also the proof that the grant fired: `wornAt` returns an empty grant
set on every refusal path.

**The control, because the refusal alone proves nothing.** A refusal reads
identically whether the rule is working or the join simply failed. Same
device, same gate, same worn set, `droid_upgrade_2` held **permanently**
instead of granted:

```
Defence    11        (no refusal at all)
```

So the gate resolves `Droid Upgrade 2` → `droid_upgrade_2` and can say yes.
The only difference between the two runs is where the feat came from.

**And the grant was live at that moment.** The remaining hole was that an
empty grant set would make the refusal true for the wrong reason. One call to
the production `wornBy`, on the real package with the real catalogue, prints
both halves together:

```
GRANTS   : {weapon_focus_blaster, weapon_focus_blaster_rifle, droid_upgrade_2}
REFUSALS : [`Droid Ion Blast Mark II` needs `Droid Upgrade 2`.]

permanent -> GRANTS   : {weapon_focus_blaster, weapon_focus_blaster_rifle, droid_upgrade_2}
permanent -> REFUSALS : []
```

`droid_upgrade_2` is **in the grant set** while the gate naming it refuses.
Not inferred — printed from one call. The mask's two feats resolve in the
same line, so *"confirm the grant happened"* is directly observed rather than
read off the +2 Dexterity.

## The stated limitation is accurate, and here is the measurement

The routing says the granted feats are consumed by nothing. Confirmed from
both ends rather than agreed with:

* 27 catalogue rows grant anything at all, **32 distinct feat names** between
  them (12 × `Weapon Focus Blaster`, 11 × `Weapon Focus Blaster Rifle`, then
  a long tail).
* `_featsInPlay` — the set that merges grants with own feats — is read at
  exactly three places: `dcAfterDodge` (twice), `vigil`, `evasion`.
* No shipped grant is any of those three, and nothing anywhere reads
  `weapon_focus_*`.

So no grant in the product can produce an observable effect today. That is a
coverage gap in the data, not a defect in the mechanism — and the mechanism
itself is now confirmed end to end by §4.

## Not defects, recorded

* **`1 rule about this character not checked`** on the status line throughout
  is `record_validate` coverage, not gates — its own documented line.
* **`badlen.sav`** is listed as unreadable at every load. It is my own
  fixture from an earlier batch, not this build's doing.

## Fixtures

`tester-gate-grant` on the shelf — the bench, the dummy, and blueprints for
`d_tool_02` / `d_device_13`. Save variants `t111-a` … `t111-f` were written
one at a time so `Continue` could not pick the wrong one; the last one
written, `t111-f`, is the item-4 control. Coder's `gate-and-grant` package
and its save are untouched.
