# 011 · A power cannot be used — and what would break the acceptance

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** App `0cd77e0` ·
`Lodestar b7e9198`; pin checked. **Read plus one play session.**

---

## ⚠⚠ 1 · A POWER CANNOT BE USED — and the gap is a wire, not a missing floor

**Nothing in any report said a power had ever been used. It cannot be.**

I loaded `Ilyana Sorr` — Jedi Guardian, `Force Push` and `Beast Control` taken
at the POWERS step and both in her save — walked into the trooper, started the
fight, and **tried every key I could think of**: `1` `2` `3` `p` `f` `q` `e`
`space` `Tab`. **Nothing. No panel, no target picker, no message, no change of
any kind.** The footer offers `arrows to move · esc to leave` and that is the
whole verb set.

Then I settled it in the code rather than reporting a failed key hunt:

    KOTOR-RPG-APP/lib/play/*.dart      mentions of "power": ZERO
    Lodestar combat.dart                one — inside a doc comment
    CheckType                           { attack, save, opposed, skill }   ← no cast

⚠ **But the floor IS built, which is what makes this a wire and not a feature
request:**

    Lodestar/pools.dart      class ForcePool
                             cast(p, {required int cost, required int tier})
                             restore() · sleep() · meditate()
    play_state.dart          PlayState.force — "Force classes only, §3"
                             projectPlayState(..., int? forceCapacity)

**The engine can hold a Force pool and spend from it by cost and tier. The
projection can track one.** And then:

⚠⚠ **The app calls `projectPlayState` in three places and passes
`forceCapacity` in none of them.** It is an optional named argument, it defaults
to null, so `PlayState.force` is null for every character the app has ever
projected — **including a Jedi.**

### The chain, end to end

| | |
|---|---|
| choose a power | ✓ the POWERS step works |
| record it | ✓ `character.power-taken {id, at_level}` |
| survive a save | ✓ proved in `010` — `Ilyana` reloads with both |
| validate it | ✓ `record_validate` rule 11 — *powers only if a held class grants them* |
| **project a Force pool** | ⚠ **never asked for** — `forceCapacity` omitted at all three call sites |
| **spend one** | ⚠ **no action exists** — `combat.dart` has no cast, `CheckType` has no power |
| **invoke one** | ⚠ **no control** — `play/` has no concept of a power |

**⚠ It is the fist's shape, one level worse.** `STATE` carries *"Equipment is
authorable but not read in play — `strike()` still uses a hardcoded fist"*: a
value that is read wrongly. **A power is not read wrongly. There is no verb to
read it into**, and the two ends that would need it are both already written.

### What it looks like from the chair

`Ilyana Sorr` — Jedi Guardian, `Padawan Robe`, `Training Lightsaber  blue`,
`Force Push`, `Beast Control` — swung at the trooper and the line read:

    unarmed · rolled 17 — d20 16 + attack 1 · needed 10 — hit · 1 damage · 17 left
    sith-trooper.command-deck.39: Blaster Rifle · … 6 damage · 1 left

**A Jedi with a lightsaber and two Force powers punches for 1 and is one hit
from dead.** ⚠ **Not re-filing the unarmed half** — `PT-1475`'s diagnostic has
landed and now says so on screen: *"unarmed — your record carries no
[equipment]: chargen records THAT you took the grant, not WHICH item."*

---

## ⚠ 2 · What would break the `PT-1415` acceptance — and it is not the missing event

**You were right that the code half is not mine, and right that the shapes are.
I read the acceptance** — `KOTOR-RPG-APP/test/ledger_test.dart` — **and it is
stronger than I assumed and narrower than it looks.**

    void mustMatch(String who) {
      final replayed = replay(log!).asMap;
      final direct   = fromChoices!.asMap;
      expect(replayed.keys.toSet(), direct.keys.toSet());
      for (final k in direct.keys) expect(replayed[k], direct[k]);
    }

**Field by field over the whole record, nothing skipped.** It runs on exactly
two characters:

| case | shape |
|---|---|
| **the organic** | `sp('Human')`, **`variant: human.own`**, `model: null`, `jedi_sentinel` |
| **the droid** | `Droid`, **`variant: Astromech`**, **`model: null`**, `scout` |

### ⚠ The missing-event shape is the one it DOES cover

You asked which shape I would expect it to handle worst, and flagged
`HK-Nine`'s absent `origin-set`. **That is the case the droid test was written
for.** Its own comment says so:

> *"⚠ A REPLAY ASSUMING NINE EVENTS IN ORDER PASSES ABOVE AND FAILS HERE. No
> Origin, no Gender, no Powers — and origin must be ABSENT, not empty."*

and it asserts `r.origin, isNull, reason: '⚠ absent, not zeroed — §2'`.
**A fold over a log with an event missing entirely is the acceptance's whole
reason for having a second case.** My instinct there was wrong.

### ⚠⚠ What it has never seen is a field that is PRESENT and unusual

**`HK-Nine` is the one I would expect it to handle worst, and not because of an
absence — because of two presences the droid case pins to null:**

    expect(shape.steps.length, 6);
    expect(shape.steps, isNot(contains(HubStep.gender)));
    expect(r.gender, isNull);
    ...  model: null

- **`HK-Nine` is a `Battle` droid: SEVEN steps, with a Voice**, and its log
  carries `character.gender-set {value: "Masculine"}`. ⚠ **The acceptance
  encodes "a droid has no gender" as a droid invariant, and it is a per-chassis
  fact** — true for `Astromech` and `Remote`, false for `Battle`. A droid whose
  `gender` is non-null has never been through `mustMatch`.
- **`model` is `null` on both existing cases.** `HK-Nine` carries
  `model-set {model: "Assault Droid Mark II"}` — **so the `model` field has
  never been compared with a value in it, on either path.**

**`Vekk Nal` is second**, for one reason: **`subrace` has never been non-null
on either side.** The organic case uses `human.own` — Human has no subraces —
and the droid case asserts `species['subrace'], isNull` with the reason
*"exactly one of the two"*. `Vekk Nal` carries `subrace: "nikto-pale"` with
`chassis: null`, which is the other half of that either/or **and has never been
run**.

**`Ilyana Sorr` I would expect it to handle best** — Human, no subrace, no
model, a Force class with two powers. **That is the covered organic case with a
different class.** It is the only one of my three I would not expect to teach
the acceptance anything.

⚠ **I am not claiming any of them fails** — I have not run it, and running it
against these three needs code I am not writing. **What I can say is which
fields have never had a value on either path**: `subrace`, `model`, and a
droid's `gender`. All three exist in my saves.

---

## ⚠ Scoped negatives

**Checked:** `ledger_test.dart` in full · `pools.dart` · `play_state.dart`'s
signature · all three `projectPlayState` call sites in the app ·
`combat.dart`'s `CheckType` and every "power" mention · every `power` mention
under `KOTOR-RPG-APP/lib/play/` · nine keys in a live fight.

**NOT done, and one is a direct miss against what you asked:**

- ⚠ **I did NOT build another Nikto subrace or another Battle model.** You said
  *"take one of the others, and take it to a FIGHT"*. **I took `Ilyana Sorr` to
  a fight instead** — she was one of the three that had never swung, and she was
  the only one who could answer the powers question. **So "no fights" is closed
  for one of the three, and four of five Nikto subraces and six of seven Battle
  models remain unbuilt, exactly as before.**
- **Whether the acceptance actually fails** on any of the three — see above
- **Whether `forceCapacity` would work if passed.** I read the projection's
  signature and its `forceCurrent`/`forceCeiling` locals; **I did not trace
  whether the fold has cases that would decrement them**
- **Whether `items: []` is fixed.** `PT-1475`'s diagnostic is on screen and I
  did not re-check the payload — **not re-filing either way, per your note**
- **Any window size but 1280×720**

**Not re-filed, all seen again:** `items: []`, the power citations, `D3`, the
hardcoded `Battle` example.

**No exception, no overflow, nothing red.**

---

## Data

**No new saves.** `Ilyana Sorr` now carries a fight in her log — she was at
`1 of 11` when I closed the app, so **that save is one blow from a death** if
anyone wants to reload into it. The other nine are as `010` left them.

**I deleted nothing and fixed nothing.**
