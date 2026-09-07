# DROID-SKILLS-01 — What Droids Can and Cannot Do

**Status: ⚠ SETTLED — `PT-642`.** **The dependency named here is BUILT: `DROIDS-UPGRADE-01` and `DROID-CONSTRUCTION-01` both exist, and `PT-615`/`PT-616` gave the ladder its level floor and class grants.** **⚠ Three chassis carve-outs since: `Stealth` to `Assassin`, `Intimidate` to `Assassin` and `Battle`, `Persuade` to `Protocol` — `PT-621`.**

**Source: `skills.2da`'s `droidcanuse` column, both games.** `source_system: kotor_game`.

---

## 1. The source closes three skills to droids

**`skills.2da` carries a `droidcanuse` flag. Three of KOTOR's eight are zero.**

| Skill | Droids | Note |
|---|---|---|
| Slicing · Demolitions · Repair · Security · Awareness | **yes** | |
| **Stealth** | **no** | **G0-T0 overrides it** with Personal Cloaking Shield — *"allows him to use his Stealth skill without a Stealth Field Generator."* |

> **⚠ Opened to the Assassin chassis by owner decision.** **A droid built to kill organics stalks them.** **The same argument that gave it `Sleight of Hand` — *"precision is its function"* — and `Intimidate` — *"a droid built to kill organics is frightening in a way a protocol droid is not."***
>
> **⚠ Eligibility only.** **The Assassin droid has no Stealth *bonus*, so it can never hold Stealth as its racial skill** — `PT-60`, and the three tiers are eligibility, bonus, aptitude. **This is the cleanest illustration of that chain in the chapter: a skill it may buy, will pay full price for, and can never master cheaply.**
| **Persuade** | ⚠ **PROTOCOL chassis only — `PT-621`** | **The only skill in the table with `npccanuse` = 0 as well.** Flagged twice. ⚠ **Opened to the `Protocol` chassis by owner decision.** |
| **Medicine** | **no** | Droids repair. They do not heal. |

> **So the exclusion is real, stated in data, and already has one documented exception.** A unique feat can override it — which is the pattern any species-level prohibition should follow.

---

## 2. The 23, ruled

### 2.1 Universal droid skills — every chassis

**Nine skills. All four droid species can use these.**

| Skill | Why a droid can |
|---|---|
| **Slicing** | **Slicing is what a droid is for.** Source: `droidcanuse` = 1. |
| **Repair** | Self-repair and repairing other droids. Source: 1. |
| **Security** | Spike mounts are droid equipment — `baseitems.2da` has **Droid Computer Spike Mount** and **Droid Security Spike Mount**. Source: 1. |
| **Demolitions** | Source: 1. HK-47 and T3-M4 both use it. |
| **Awareness** | Sensors. `baseitems.2da` has **Droid Search Scope**, **Motion Sensors**, **Sonic Sensors**, **Targeting Computers**. Source: 1. |
| **Alertness** | **Awareness split in two on our side.** Sonic Sensors are the hearing half — the equipment exists. |
| **Appraise** | Assessing value is computation. **Authored.** |
| **Archaeology** | Knowledge, not intuition. **Authored.** |
| **Xenology** | Knowledge. **Authored** — and a droid that catalogues species is unremarkable. |

### 2.2 Closed to all droids

**Six skills. No chassis, no exception.**

| Skill | Why not |
|---|---|
| **Mysticism** | **No Force connection.** `GAP-002` gates Force powers behind class levels with species exceptions; **this is the first exception that runs as a prohibition rather than a permission.** |
| **Persuade** | **Source: `droidcanuse` = 0, `npccanuse` = 0.** Flagged twice — the only skill so marked. ⚠ **OPENED TO THE `Protocol` CHASSIS — `PT-621`.** |

> **⚠⚠ `PT-621`: THE THIRD CHASSIS CARVE-OUT, AND THE SAME SHAPE AS THE OTHER TWO.**

    ⚠ Stealth     opened to `Assassin`            *"a droid built to kill
                                                  organics stalks them"*
    ⚠ Intimidate  opened to `Assassin` · `Battle` *"frightening in a way a
                                                  protocol droid is not"*
    ⚠ Persuade    opened to `Protocol`            ⚠ *"a diplomatic aide is what
                                                  a protocol droid IS"*

**⚠ *"A DROID DOES NOT WORK A CANTINA"* IS THE ARGUMENT AGAINST A SMUGGLER DROID. IT IS NOT AN ARGUMENT AGAINST A DIPLOMAT.**

**⚠ AND IT RESOLVES A LIVE TENSION.** **`PT-567` gave the `Protocol` chassis a chassis action of *"one `Persuade`, `Appraise` or `Xenology` check"* — ⚠ NAMING A SKILL THE CHASSIS COULD NOT HOLD.** **`PT-602`'s `GE3` list — *"receptionist, secretary, errand-runner, DIPLOMATIC AIDE"* — pointed the same way.**

**⚠ `Streetwise` STAYS CLOSED TO EVERY CHASSIS. It is the cantina half of the cluster and the argument against it survives intact.**
| **Streetwise** | Part of the Persuade cluster. **A droid does not work a cantina.** |
| **Swim** | **Droids sink.** Nothing in the equipment tables floats. |
| **Beast Handling** | **Animals do not read a droid.** No scent, no body language, no fear response to work with. |

### 2.3 Chassis-dependent — eight skills

**Four droid species. These depend on the body, not on being a droid.**

| Skill | Astromech | Assassin | Battle | Remote |
|---|---|---|---|---|
| **Pilot** | **yes** | no | no | no |
| **Botany** | **yes** | no | no | no |
| **Medicine** | **yes** | no | no | **yes** |
| **Sleight of Hand** | **yes** | **yes** | no | no |
| **Intimidate** | no | **yes** | **yes** | no |
| **Acrobatics** | no | **yes** | **yes** | **yes** |
| **Athletics** | no | **yes** | **yes** | no |
| **Scavenging** | no | **yes** | **yes** | no |
| **Stealth** | no | **yes** | no | **yes** |

**Pilot** — **the astromech's defining function.** *"A backup or replacement for a nav computer."* No other chassis is built for it.

**Botany** — analysis rather than affinity. **An astromech runs soil samples.**

> **Treat Injury departs from the source, deliberately.** `droidcanuse` is 0. **Overruled for the Astromech and Remote — on organics other than themselves.** Both are support chassis, **medical droids are unremarkable in this setting**, and **Bao-Dur's Remote carries a laser that repairs.** The combat chassis keep the exclusion.

**Sleight of Hand** — **requires fine manipulators.** The Astromech has them; **the Assassin droid has them because precision is its function.** The Battle droid is mass-produced and does not. **The Remote has no hands at all.**

> **Intimidate reverses the earlier ruling, and HK-47 is the reason.** It sits in the Persuade cluster, which is closed — **but a droid built to kill organics is frightening in a way a protocol droid is not.** Assassin and Battle droids only.

**Acrobatics** — hovering frames and humanoid combat frames. **Not a wheeled astromech.**

**Athletics** — ⚠ **`PT-319`. Assassin and battle frames only.** **Climbing and jumping need arms and legs.**

> **⚠ This was previously banned to EVERY droid on the reasoning *"a wheeled or hovering frame does neither."*** **True of an astromech and a remote; false of a humanoid combat chassis, which has both.**

**The ban was written from the astromech outward and never checked against the other three.**

**Scavenging** — **wilderness endurance for something that does not eat.** Only the combat chassis, and only because it is built to operate unsupported.

**Stealth** — **the source says no and G0-T0 is the documented exception.** He is a Remote with a cloaking shield. **Repulsorlift frames make no footfalls; wheels and servos do.**

### 2.4 What each chassis ends up with

| Species | Skills | Character |
|---|---|---|
| **Astromech** | 9 universal + **Pilot, Botany, Medicine, Sleight of Hand** = **13** | The utility droid. T3-M4. |
| **Assassin droid** | 9 + **Sleight of Hand, Intimidate, Acrobatics, Scavenging, Stealth** = **14** | The hunter. HK-47. |
| **Battle droid** | 9 + **Intimidate, Acrobatics, Scavenging** = **12** | Mass-produced infantry. |
| **Remote droid** | 9 + **Medicine, Acrobatics, Stealth** = **12** | Support and infiltration. G0-T0, Bao-Dur's Remote. |

> **Twelve to fourteen against an organic's twenty-three.** Roughly half — **and the upgrade system in §3 is what closes it.**

## 3. The reason droids look thin, and the system that fixes it

> **Organics have ten skill-bonus feat chains. Droids have none.**

**That is not an oversight — it is the wrong mechanism for a droid.** A droid does not practise. **It gets better hardware.**

### 3.1 The upgrade system — unbuilt, and this depends on it

**KOTOR 2 lets you install permanent upgrades on droid companions, including attribute bonuses.** The tables are held:

**`baseitems.2da`** carries eleven droid-specific item types — Light, Medium, and Heavy Plating; Search Scope; Motion Sensors; Sonic Sensors; Targeting Computers; Computer Spike Mount; Security Spike Mount; Shield; Utility Device.

**`upgrade.2da`** grew from **25 rows in K1 to 369 in K2** — the single largest expansion between the games.

**`Droid Upgrade 1/2/3` gates which tier a chassis accepts**, at levels 1, 7, and 13.

> **So the parts exist and the system does not.** **Skill upgrades should be part of it** — a sensor package that grants Awareness, a vocabulator that grants languages, a manipulator array that grants Sleight of Hand.
>
> **Which means some of §2.3's chassis restrictions are not permanent.** A Remote with a manipulator arm gains Sleight of Hand. **The chassis sets what you start with; upgrades change it.**

**That is the design and it is not written. On the agenda.**

---

## 4. Open

**Whether the upgrade system replaces skill feats for droids, or supplements them.** If upgrades grant skill bonuses, **droids may not need feat chains at all** — which would make the current asymmetry correct rather than a gap.

**Alertness for droids with no audio sensors.** Sonic Sensors are an *upgrade*, not standard. **A droid without them arguably cannot hear** — which would make Alertness chassis-dependent rather than universal.

---

## 5. Spheroid is cut. Remote absorbs it.

**`FEATS-CUT-AND-DROIDS-01 §3` listed five droid species, separating Spheroid from Remote by size** — G0-T0 at Medium, Bao-Dur's Remote at Tiny.

> **They are one chassis. Remote is the name.** Repulsorlift, no limbs, spheroid body. **Wookieepedia calls both *spheroid droids* in the same sentence**, and *droid remote* is the documented category.

**Four droid species: Astromech, Assassin droid, Battle droid, Remote droid.**

**Size becomes a property within the species rather than a species boundary.** G0-T0 is Medium; Bao-Dur's Remote is Tiny. **`creaturesize.2da` gives Tiny a +2 attack-and-defence modifier**, so the difference is mechanically real — **it just is not a different kind of droid.**
