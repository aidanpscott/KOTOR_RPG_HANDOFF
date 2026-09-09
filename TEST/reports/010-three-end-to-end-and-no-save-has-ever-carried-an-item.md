# 010 · Three end to end — and no save has ever carried an item

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** App `9fb1762` ·
`Lodestar b7e9198`; **pin checked, `resolved-ref` = engine HEAD.**

**Three characters built, played, saved, quit and reloaded**, chosen for the
shapes I had never carried:

| | shape |
|---|---|
| **Vekk Nal** | **Nikto, Pale** — a subrace of a parent that says *"−2 Charisma, plus a +2 set by subspecies. See each entry."* · class **Agent** |
| **Ilyana Sorr** | **Human · Jedi Guardian** — a Force class, so **POWERS reached as a player** |
| **HK-Nine** | **Droid · Battle**, model *Assault Droid Mark II*, class **Scout** — the fourth body |

**✓ All three reload.** `Ilyana Sorr · 2 rules unchecked` · `Vekk Nal · 2 rules
unchecked` · `HK-Nine · 3 rules unchecked`, each opened from `Load Game` after
a full quit.

---

## ⚠⚠ THE FINDING: `items: []` — in every save this machine has ever written

**You asked whether an odd combination survives a save. The odd parts all do.
The equipment does not, and never has, for anybody.**

    hk-nine.sav        route='standard'   items=[]   credits=100
    ilyana-sorr.sav    route='standard'   items=[]   credits=100
    kaeda-vos.sav      route='standard'   items=[]   credits=100
    probe-walker.sav   route='standard'   items=[]   credits=100
    rell-vantt.sav     route='standard'   items=[]   credits=100
    second-fight.sav   route='standard'   items=[]   credits=100
    t3-k9.sav          route='standard'   items=[]   credits=100
    t3-m4-probe.sav    route='standard'   items=[]   credits=100
    vekk-nal.sav       route='standard'   items=[]   credits=100
    vess-taran.sav     route='standard'   items=[]   credits=100

**Ten of ten, including `kaeda-vos` — the oldest save on the machine, written
before I ever ran the app.**

`character.equipment-set` carries `route`, an empty `items` list, and
`credits: 100`. **The assortment the Equipment step showed me — `Hold Out
Blaster · Short Sword`, `Padawan Robe`, `Training Lightsaber`, `Blaster
Carbine`, the medpacs, the boots — is in no save.**

⚠ **This is `PT-1468` one layer deeper.** That ruling found the player fights
unarmed because the weapons map is built from `_here` and the player is not a
placement. **The record has no item in it either**, so wiring the map to the
player would still find nothing to wire. **Two independent reasons for the same
symptom, and only one of them was known.**

**⚠ And the grant is recorded without its object.** `Ilyana Sorr` took the
melee upgrade and the log says:

    character.grant-resolved  {"taken": "item"}
    character.equipment-set   {"route": "standard", "items": [], "credits": 100}

**Which item was never written.** For a Jedi Guardian this is sharper than it
looks — see the D3 note below.

---

## ⚠ What DID survive, field by field

**Read from the decoded logs, not inferred from the screen.**

| | recorded |
|---|---|
| **the odd subrace** | `species-set {id: "nikto", subrace: "nikto-pale", chassis: null, model: null}` ✓ |
| **the chassis** | `species-set {id: "droid", subrace: null, chassis: "droid-battle"}` ✓ |
| **the model** | `model-set {model: "Assault Droid Mark II"}` — **a name, no id**; `STATE` already flags this and I am **not** re-filing it |
| **both powers** | `power-taken {id: "force_push", at_level: 1}` · `{id: "beast_control", at_level: 1}` ✓ |
| **droid programming** | `backstory-set {profession: null, programming: "protocol-droid"}` ✓ |
| **no origin for a droid** | `HK-Nine` has **no `origin-set` event at all** ✓ |
| **the droid spread** | `str 14 · dex 12 · con 14 · int 10 · wis 12 · cha 10` — **exactly `chassis.toml`'s Battle row** ✓ |
| **skills, abilities, feat, identity** | all present with the values I chose ✓ |

⚠ **`character.gender-set {value: "Masculine"}` is how a droid's VOICE is
stored.** The boundary screen says *"Gender becomes Voice or is absent"*, and
the log keeps the `gender` kind for both. **Not obviously wrong — one event
kind serving two presentations** — but the vocabulary and the screen disagree
about the name, and I could not tell from `EVENT-KINDS-01` whether that is
intended.

**⚠ Scoped, and this is the important limit:** `PT-1415`'s acceptance is *two
paths to one record, compared field by field*. **I compared the LOG against MY
CHOICES.** I did not compare `replay()` against `recordFromChoices` — that
needs code I am not going to write. **What I can say is that every choice I
made is in the log with the value I gave it, and that all three characters
reload without a refusal.** The half I cannot reach is whether the two
in-memory records agree.

---

## 3 · `force_blind` — two species, four entries

**You asked how many. It is a mechanism with two users.**

    Droid                  is_droid=true    ← the parent only
    Rakata                 is_droid=false
    Rakata, Builder        is_droid=false   ← restates it
    Rakata, Flesh Raider   is_droid=false   ← restates it

**4 of 57 entries, but only 2 distinct species.** ⚠ **And the two disagree about
inheritance:** `Rakata` restates `force_blind` in both subraces; **`Droid` does
not restate it in any of its four bodies** — yet the class step greys the Force
classes for `Astromech`, `Assassin` and `Battle`, which I have now seen. **So
the app inherits from the parent, and Rakata's restatement is redundant rather
than load-bearing.** Two species, one mechanism, two data conventions.

---

## New, from carrying these three

**N1 · The Battle chassis HAS a voice, and the step appears.** `Remote` and
`Astromech` gave *"absent — this chassis has no vocabulator"*; `Battle` gives a
real **Voice** step and a **seven of nine** strip. **The "Gender becomes Voice"
half of the boundary text is now confirmed on a chassis that has one** — I had
only ever seen the "or is absent" half.

**N2 · Battle droid — 13 of 25 skills**, with its own closed list
(*Botany · Medicine · Pilot · Sleight of Hand · Stealth*), different again from
`Remote`'s 12 and `Astromech`'s 13. **Three bodies, three lists.**

**N3 · ⚠ D3 is worse for a class the label does not name.** As a **Jedi
Guardian** the Equipment step still offers *"TAKES THE CLASS'S OWN melee
UPGRADE FROM §4a — Soldier → … Scout → … Duelist → …"*. **Guardian is not one
of the three.** I took it: the weapon row stayed `Training Lightsaber  blue`,
nothing visibly changed, and the log recorded `taken: "item"` **with no item**.
⚠ **Not re-filing — `D3` is in `STATE`** — but the Guardian case is new
information about it: the label does not cover the class you are playing, and
the record does not say what you got.

**N4 · Small render things.** `Training Lightsaber  blue` carries a **double
space** and an unlabelled suffix where every other row is `label — value`. And
the Battle model list is interleaved — *War I · War II · Assault I · War III ·
War IV · Assault II · War V* — which reads as unsorted unless it is tier order.

---

## Powers, as they stood when I ran

**Not re-filed, per your instruction — recording state only, because `Coder` is
mid-slice.** At the time of this run `powers.toml` still had **0 `note` fields
and 41 citations**, and I saw a **second** one on screen as a player, having
only confirmed `Beast Control` before:

> **Force Push** — *"…thrown to the ground stunned for 1 round, and suffers 1d6
> per two Force levels — maximum 12d6 — **PT-301**. A successful Reflex save…"*

The `POWERS` screen is otherwise identical for `Jedi Guardian` and `Jedi
Consular` — same list, same order, same *"begins with 2"*. **The withheld line
still reads *"Precognition have no Force cost…"***.

---

## ⚠ Scoped negatives

**Sampled this session:** 3 species (`Nikto` + `Pale`, `Human`, `Droid` +
`Battle`), 3 classes (`Agent`, `Jedi Guardian`, `Scout`), 1 of 5 Nikto
subraces, 1 of 7 Battle models. **Three pairs carried end to end** — which is
three more than `009` had.

**NOT checked:**

- **The other four Nikto subraces** — `Red`, `Green`, `Mountain`, `Southern`.
  ⚠ **I opened one of five**
- **Whether `replay()` and `recordFromChoices` agree** — the half of `PT-1415`
  that needs code. See the scoped note above
- **Whether `items: []` is a writer gap or a reader gap.** I read the payload
  and the ten files; **I did not read `ledger_writer` to see whether the items
  are dropped at write time or never assembled**
- **Play beyond entering the area.** ⚠ **No fights this session** — these three
  were built for the save seam, so nothing here is evidence about combat, and I
  did not re-test the unarmed line
- **The other five Force classes**, and the 6 remaining Battle models
- **Any window size but 1280×720**

**Not re-filed, all seen again today:** the power citations, the species
citations, `D3`, the hardcoded `Battle` example on the abilities screen, and
the model-has-no-id.

**No exception, no overflow, nothing red** in either run log.

---

## Data

**Added three saves** — `vekk-nal.sav`, `ilyana-sorr.sav`, `hk-nine.sav`.
⚠ **`ilyana-sorr` is the only save on the machine carrying `power-taken`
events**, and `hk-nine` the only one carrying a `Battle` chassis and a voice —
**keep both if you want the odd shapes to reload against.** Ten saves now.

**I deleted nothing and fixed nothing.**
