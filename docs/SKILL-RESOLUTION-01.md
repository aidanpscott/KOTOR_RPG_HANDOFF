# SKILL-RESOLUTION-01 — How Skills Resolve

**Status: SETTLED.**
**Decision ID: D-AO.**
**Depends on:** `SKILLS-01` (D-AN) for the 23-skill list.
**Sources:** `traps.2da` (`source_system: kotor_game`); KOTOR mechanics reported by StrategyWiki, community guides, and a K2 bug report quoting exact DCs — **all secondary and marked as such.**

---

## 1. Not every skill rolls against a difficulty

**The single most useful finding from the source: KOTOR's eight skills resolve five different ways.**

| Mode | What happens |
|---|---|
| **Fixed DC** | The world has a difficulty. A commercial lock is DC 15 whoever you are. |
| **Scaling DC** | *Character level + N.* **Reserved for the exceptional.** |
| **Opposed** | Against another character's number. Both sides scale. |
| **Resource** | **No roll.** Skill reduces the consumables spent. |
| **Effect** | **No roll.** Skill changes how much the action accomplishes. |

> **Three of KOTOR's eight skills do not roll against anything.** Repair and Treat Injury are formulas; Stealth and Awareness are a contested pair. **A system that assumed every skill has a DC would have got three of eight wrong.**

---

## 2. The difficulty ladder

**Seven tiers. The middle five are `traps.2da`'s own values.**

| Tier | DC | Auto-succeeds at | Example — a locked door |
|---|---|---|---|
| **Trivial** | 5 | −5 | Latched panel, no lock |
| **Easy** | 10 | +0 | Civilian door, standard lock |
| **Moderate** | 15 | +5 | Commercial security lock |
| **Hard** | 20 | +10 | Military blast door |
| **Formidable** | 25 | +15 | Sith vault seal |
| **Heroic** | 30 | +20 | Rakatan lock |
| **Legendary** | 35 | +25 | Built never to open |

**"Auto-succeeds at" is the total bonus that beats the DC by taking 10.** That is the number that matters at a table, because most skill use is not under pressure.

**Modifiers: ±2 minor, ±5 major, ±10 extreme.** One set, used for both DCs and social contests.

### 2.1 Demolitions carries its own spread

**Setting a mine uses the tier DC. Disabling adds +2. Recovering adds +5.**

> **KOTOR uses +5 and +10 — steeper — but it was tuned for *take twenty*.** Out of combat the games roll an automatic 20, so a gap of +10 costs nothing when unhurried. **Under take 10 the same gap would put recovery out of reach at low level**, and recovering mines is most of what makes Demolitions worth taking.

### 2.2 The scaling band, and what it is for

**KOTOR's hardest Security checks are *character level + 28*.** At level 30 that is DC 58.

> **That is why a KOTOR specialist never trivialises the game — the top of the range moves with them.**

**Adopted, but narrowly.** **Fixed tiers describe the world; the scaling band describes the story.** A commercial lock never gets harder. **The Rakatan vault at the end of the campaign is defined relative to whoever reaches it.**

**Two or three per adventure, not a general rule.** A world that levels with the player is a treadmill, and players notice.

---

## 3. Social skills are opposed, and they resist differently

> **This is a deliberate departure from KOTOR, which scales Persuade DCs *relative to player level*.**
>
> **Under that rule, the same guard refusing the same request gets harder because you levelled.** Your Persuade climbs from +10 to +20 and his resistance climbs to match. **You never actually get better at talking to guards — you run to stay in place.**

**Persuade rolls against the target's Alertness.** *Can they see through you?*

**Intimidate rolls against the target's Will save.** *Do they hold their nerve?*

**Streetwise's disguise use rolls against Alertness.**

### 3.1 Why two different resistances

**One social number cannot express an NPC.** Two existing mechanics can, at no added cost — **saves already exist.**

> **A Wookiee thug is easy to fool and impossible to frighten. A nervous slicer catches your lie and folds the moment you lean on him. A Jedi Master is hard both ways.**

### 3.2 NPC resistance

| Who | Alertness |
|---|---|
| Distracted, drunk, desperate | **+0** |
| Ordinary guard, shopkeeper, spacer | **+5** |
| Officer, professional, cautious merchant | **+10** |
| Jedi Knight, senator, crime boss | **+15** |
| Jedi Master, Sith Lord, Hutt | **+20** |
| Named exceptions | **+25 and up** |

**Nothing on this list moves when the player levels.** A Taris warehouse guard is +5 forever — **rolled against at level 5, walked past at level 15.** That is correct.

### 3.3 Some things are not a roll

**A request contradicting the target's core loyalty is refused regardless of the result.**

**RCR supplies the shape.** Its Reputation section rules that a favour which would let a character circumvent an adventure *"should always be unavailable regardless of the check."* **Same principle, stated for social skills.**

---

## 4. Stealth, and the stealth field generator

**The defender rolls the better of Awareness or Alertness.**

**A stealth field generator imposes −10 on Awareness only. Alertness is unaffected.**

### 4.1 Why this is better than one detection skill

**Two skills that fail differently is worth more than one that is simply better.**

**Without a field**, Awareness is the stronger roll — you are looking for someone hiding, and sight is primary. **With a field, sight is defeated and hearing is not.**

> **So a stealth field is not a flat upgrade. It is excellent against a watchful guard and useless against a Selkath.** The sneaker has to consider *who is on duty*, which turns a stat check into a tactical read.

**It also gives Alertness a job it needed.** Without this, Alertness was the social-reading skill with a vestigial hearing clause. **It is now the counter to the most powerful stealth item in the setting.**

**Falling out of the mechanic:** five species carry Alertness bonuses — **Selkath +4, Nautolan +4, Echani +2, Sullustan +2, Rodian +2.** A Selkath guard is the worst possible person to sneak past with a field running.

---

## 5. Resource mode — six skills

**The test: does a consumable already exist in the fiction?** **Inventing one to justify a mechanic is how a system acquires bookkeeping nobody asked for.**

### 5.1 The reduction curve

**Thresholds at 4, 9, 16, and 25. One fewer consumable at each. Minimum one.**

| Skill total | Reduction | A 5-part job costs |
|---|---|---|
| 0–3 | — | 5 |
| 4–8 | −1 | 4 |
| 9–15 | −2 | 3 |
| 16–24 | −3 | 2 |
| 25+ | −4 | **1** |

> **The bands widen on their own — 5 points, then 7, then 9.** Diminishing returns without anyone doing arithmetic, **and the four numbers are memorable because they are the perfect squares.**

**A first-level specialist already saves one.** They reach the floor on a five-part job around level 20 — **the whole campaign, and never wasted.**

**Hard jobs stay expensive.** An eight-part job still costs 3 at level 30. **The lever for keeping high-level characters spending is raising the base cost, not the rate.**

### 5.2 The six

| Skill | Consumable | Notes |
|---|---|---|
| **Slicing** | Computer spikes | Base cost by terminal grade |
| **Security** | Security spikes | **Optional.** Spikes grant a bonus, not access — the one skill where the consumable is insurance rather than a cost. |
| **Repair** | Repair parts | Base cost by damage |
| **Demolitions** | Mines | One per placement; the skill governs grade and radius |
| **Streetwise** | **Credits** | **Higher skill means cheaper informants.** No new item — credits are already tracked. |
| **Scavenging** | Rations | **See §5.4.** |

### 5.3 Effect mode — two

**Medicine** — one medpac, **more vitality restored.** The roll answers *how much did that heal*, which matters mid-fight where counting supplies does not.

**Repair** — a **second** mode alongside its resource use: **more vitality restored when a droid uses a repair kit on itself.** The droid equivalent of a medpac, and the same shape as Medicine.

### 5.4 Scavenging and rations are difficulty-gated

> **Ration tracking is real in the fiction and abandoned by most tables within two sessions.**

**It is therefore optional, controlled by the campaign difficulty setting** — the same knob that scales alignment drift and, in KOTOR, added +5 to skill DCs.

**Where rations are not in play, Scavenging is a pure fixed-DC skill.** **Where they are, Scavenging reduces consumption on the curve in §5.1.**

**A campaign package declares whether rations are tracked.** It is not a per-session GM choice.

### 5.5 Seventeen skills have no resource dimension

Acrobatics · Alertness · Appraise · Archaeology · Athletics · Awareness · Beast Handling · Botany · Intimidate · Mysticism · Persuade · Pilot · Sleight of Hand · Stealth · Swim · Xenology

**And that is correct.** **The mechanic's value is that it makes a skill matter at high level without the world scaling.** Applied to six skills that genuinely have consumables it is elegant; applied to twenty it is a spreadsheet.

**One thing worth noticing about the six:** they are the technical and legwork skills — **exactly what a Machinist and a Smuggler live on.** Resource mode disproportionately rewards the two classes with the deepest skill pools, **which is coherent rather than accidental.**

---

## 6. Every skill, assigned

| Mode | Skills |
|---|---|
| **Fixed DC** | Acrobatics, Appraise, Archaeology, Athletics, Botany, Demolitions, Mysticism, Pilot, Security, Scavenging, Swim, Xenology |
| **Opposed** | Stealth ↔ Awareness/Alertness · Sleight of Hand ↔ Awareness · Persuade ↔ Alertness · Intimidate ↔ Will save · Beast Handling ↔ the creature |
| **Resource** | Slicing, Security, Repair, Demolitions, Streetwise, Scavenging |
| **Effect** | Medicine, Repair |
| **Scaling DC** | **Any skill, sparingly** — the two or three obstacles an adventure is about |

**Several skills carry two modes.** Security has a DC *and* optional spikes. Repair has resource *and* effect. Demolitions has a DC *and* consumes a mine. **That is the source's own shape, not an elaboration.**

---

## 7. Open

| Item | Status |
|---|---|
| **Base consumable costs** | The reduction curve is settled; **what a terminal or a droid repair costs before reduction is not.** |
| **K1 versus K2 mine tiers** | Sources conflict — **three grades (15/20/25) or five (10/15/20/25/30).** The five-grade version matches `traps.2da`, which we hold for K2. **One question to the 2DA holder settles it.** |
| **The scaling band's constant** | KOTOR uses level + 28. **Ours is unset.** |
| **Knowledge-skill DCs** | Archaeology, Xenology, Mysticism, and Botany need a DC-by-obscurity ladder — common 10, specialist 20, lost 30 is a starting shape, not a decision. |

---

## Who may use a skill against whom

**`skills.2da` carries an `npccanuse` column. Exactly one skill is flagged zero: Persuade.** **Seven of KOTOR's eight work identically for NPCs.**

> **The principle: a mundane skill may not override the decision of a character under player control, or take their property.**
>
> **The restriction protects the player, not the skill.** **Between NPCs, every skill works in every direction.**

| Skill | Against a player-controlled character | Between NPCs |
|---|---|---|
| **Persuade** | **No.** *Source: `npccanuse` = 0.* | **Yes** |
| **Intimidate** | **No** | **Yes** |
| **Sleight of Hand** | **No** | **Yes** |
| **Slicing** *(on a droid)* | **No** | **Yes** |
| **All others** | **Yes** | **Yes** |

**So a Sith officer intimidates a subordinate into talking, a bounty hunter lifts a datapad off a rival, and a slicer takes control of an enemy droid mid-fight.** **All of it runs.**

### Companions are player-side

> **A companion under player control is a player-controlled character for this rule.** **A companion the GM is running is an NPC.**

**Which means the protection follows control, not the character sheet.** **Nobody intimidates Bastila while you are playing her. If she is off doing something on her own, she is fair game.**

**And companions may use these skills freely on NPCs** — **which is the point.** **Handing a player control of Canderous specifically so they can intimidate someone is good play, and it is one of the few things a companion offers that the player character may not.**

### Force powers are the exception

**Force Persuade and the domination powers work on players.** **They are explicitly supernatural, they carry a saving throw, and mind-tricking a guard is core to the setting.**

> **A Sith who wants a player to kneel uses the Force, not rhetoric.**

### An NPC may still say anything

**A Sith Lord telling a player to surrender is a scene, and the player answers it.** **What the NPC may not do is roll for the answer.**

### Note on §5.2

**The NPC resistance ladder — +0 to +25 for social checks — applies whenever a player-controlled character rolls a social skill.** **There is no reverse table against a player, and there should not be one.**
