# BUILD 60 — two stale extracts, and `§4a` pinned rather than fixed

**684 green** — Lodestar 303 · Lens 4 · Loom 120 · app 257.

---

## The stale extracts

`species` and `starting_equipment` were done at `BUILD 59`. `CHARGEN-DATA-01`
**moved a second time** after that, so `chassis` and `first_level_feats` went
stale again — **only line numbers changed**. `stale 1`, which is `event_kinds`
and is deliberate.

## ⚠ Which I would rather: **let the confirmation land first.**

Three reasons, and the third is the one that decides it.

**1 — `Tester`'s open question is already settled, in code.** It could not tell
whether the Guardian is a second path or a contradiction. **It is one path.**

    GrantRecord? grantFor(ProfessionRecord? p)   // ← the class is not a parameter

`grantFor` keys on the **profession alone and never looks at the class**, so an
Agent and a Guardian run identical code — and neither is named by any upgrade
grant. **There is no second path to find.** The run is now confirmation of
behaviour rather than of my reading, which is worth more, not less.

**2 — A fix landing mid-run destroys the pair.** `Tester`'s Guardian
observation would describe a build that no longer exists. `t3-k9.sav` was worth
having at `PT-1458` precisely because the before and the after were both
captured.

**3 — ⚠ The fix needs a ruling I do not have.** What *should* happen when an
upgrade names classes the character is not?

- **Do not offer the item half at all** — the profession then grants only its
  aptitude, and the choice disappears for those classes.
- **Offer it and apply nothing** — today, and the log now says so.
- **Apply it to whatever the class's array actually carries** — `Conscript`'s
  own shape, *"the best armour the character's Armour Proficiency allows"*.

Three different games. Not mine.

## What I did instead: pinned it

`grant_reaches_class_test.dart` **changes nothing.** It records the current
behaviour so the ruling's effect is visible rather than silent, and names in
its own body which assertion turns red when the fix lands.

### The measurement, for whoever rules it

| profession | kind | classes its text names |
|---|---|---|
| **Hunter** | upgrade | Soldier · Scout · Duelist — ⚠ **3 of 19** |
| **Veteran** | upgrade | Smuggler · Bounty Hunter — **2 of 19** |
| Conscript | upgrade | ⚠ none, and that is correct — *"the best armour the character's Armour Proficiency allows"* applies to any class |
| Acolyte | upgrade | none named; a Padawan Robe implies a Force class without saying so |

⚠ **So it is two grants, not four.** `Conscript` and `Acolyte` are a different
shape and should not be swept in with them — which is the same distinction the
seven needed, one layer over.

## Still open

- ⚠ `§4a` — **needs a ruling**, then one slice. Sixteen of nineteen classes are
  offered `Hunter`'s upgrade.
- 45 annotation cells; `targets` under-populated by 21; conditional damage.
- ⚠ A citation assembled at runtime falls between the two checks.
