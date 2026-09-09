# DEATH-AND-DIFFICULTY-01 — three modes, and what dying means in each

**Owner ruling. `PT-152`.**

**⚠ This began as a Beast Master question — *what happens when a permanent companion dies* — and the answer turned out not to be a class rule.** **It is a campaign setting that touches every character at the table.**

---

## 1. What already exists

**`ACTION-ECONOMY-01 §6.3` and `E-2` give the thresholds:**

    ⚠ 0 vitality              Disabled
    ⚠ −1 to −(Con − 1)        dying — loses 1 per round, Medicine stabilises
    ⚠ −Constitution           dead

**⚠ ONE POOL — `PT-559`. `wound points` no longer exist.** **Damage runs into the negative and the killing blow's EXCESS CARRIES THROUGH.**

**⚠ Nothing said what *dead* means for a player character, and nothing distinguished a player from a companion.**

---

## 2. The three modes

**A campaign package or a GM picks one at the start and it applies to everyone.**

### Easy — the KOTOR rule

> **Nobody dies permanently unless the whole party dies.**

**⚠ THE NEGATIVE BAND DOES NOT EXIST ON EASY — `PT-559`.** **A character reduced to 0 is DOWN: out of the fight until an ally helps them up, or until combat ends, when everyone who was down stands at 1 vitality.**

**⚠ There is no dying, no bleed-out and no death threshold. Damage below 0 is not tracked at all.**

**⚠ This is what the games actually do.** **A downed party member in KOTOR stands up when the fight ends; the only true loss is a total party defeat.**

> **⚠⚠ THE WHOLE BAND IS THE PARTY'S, NOT JUST THE STANDING UP — `PT-1524`.** `PT-1515` made the stand-at-1 rule party-only and left a **dying enemy nothing ticks out of combat.** `STUDY 23` settles it from the source.
>
> **⚠ KOTOR HAS NO DYING BAND AT ALL.** `DYING` and `BLEED` appear **zero times** in the whole 216,650-byte API; `GetIsDead` is binary and there is no `GetIsDying`. **And it is a deletion rather than an absence — NWN keeps `EVENT_SCRIPT_MODULE_ON_PLAYER_DYING` and KOTOR dropped it.**
>
> **⚠ What KOTOR used instead is a FLAG ON NINE CHARACTERS.** `NoPermDeath=1` on **17 of 205 K1 blueprints — all nine recruitable party members plus eight plot NPCs. NO ENEMY CARRIES IT.**
>
> **RULED: AN ENEMY DIES AT 0. There is no dying enemy, so nothing needs to tick one out.** The band — dying, the bleed, the threshold at −Constitution — **is the party's, entire.**
>
> **⚠ And `STUDY 23`'s line is why this is not a loss: KOTOR PROVES A BAND IS NOT REQUIRED TO FEEL LIKE KOTOR.** Ours was a **universal** band where theirs was **a flag on nine characters.**

> **⚠⚠ THAT IS A PARTY RULE AND THE CODE APPLIES IT TO EVERYTHING — `PT-1515`.** The sentence above says it outright: **a downed PARTY MEMBER stands up when the fight ends.** `TEST 020` found an enemy doing the same thing, **and persisting it.**
>
> **⚠ SO NOTHING DIES.** Tester struck a sentinel to **−2** and it **stood again at 1 the moment combat ended**, with `character.revived` written into the log. After a full quit and Continue it is **still at 1.**
>
> **⚠⚠ AND THE CONSEQUENCE IS A GAME NOBODY DESIGNED: EVERY CREATURE ANYONE HAS EVER BEATEN STANDS AT 1 VITALITY, PERMANENTLY.** Tester's line is the one to keep — **a second visit is never a second fight. It is one hit.**
>
> **RULED: the stand-at-1 rule is the PARTY's.** An enemy reduced past its threshold **dies**, on every difficulty. **`Easy` protects the player from loss; it was never a promise that the galaxy is unkillable.**
>
> **⚠ And that makes `PT-1511`'s vacated square reachable for the first time.** Tester could not construct it *because nothing dies* — it will exist the moment this lands, and the wall-under-a-creature question stops being hypothetical.

### Normal

> **Players can die. ⚠ So do BEAST and DROID companions. Henchmen get up.**

**⚠ With exceptions chosen by the GM.**

**A player character reduced to `−Constitution` is dead. ⚠ SO IS A BEAST COMPANION AND SO IS A DROID COMPANION — `PT-558`.** **⚠ A HENCHMAN USES THE `Easy` RULE: down at 0, up after combat at 1 vitality — `PT-571`.** **⚠ A hired NPC or a temporarily overridden droid is not the player's to lose permanently.**

**⚠ AMENDED. This section previously read *"a henchman, a beast companion, or a droid is not [dead] — it is out for the encounter and recovers."*** **That made the two companion classes the only ones playing without a stake at the default difficulty.**

> **⚠ BUT A DROID CAN BE REBUILT AND A BEAST CANNOT.**

**A destroyed droid companion may be REPAIRED AND REBUILT TO NEW.** **⚠ `§5` already says a Droid Master's droids are *"built, commanded, permanent until destroyed, and REPLACEABLE."*** **A Droid Master who loses one loses TIME AND PARTS.**

**⚠ A BEAST MASTER WHO LOSES ONE LOSES THE BEAST.** **It must be acquired again — `BEASTS-01`'s bond DC and price — and the new one is a NEW ANIMAL at the master's current level.**

**⚠ It does not keep the dead beast's name, its skill ranks, or anything a Beast Master chose for it.** **Everything else about a beast is fixed by species — `BEASTS-LEVELS-01 §1` — so a replacement is mechanically identical and is not the same creature.**

### ⚠ Why the difference is the point — `PT-558`

**`PT-151`'s constraint: *"either a devastating loss or a shrug, and both are bad."***

> **⚠ THE DROID IS THE SHRUG AND THE BEAST IS THE LOSS, AND THAT IS NOW DELIBERATE.** **`§5` already said *"the Beast Master has one companion and it matters. The Droid Master has several and they are materiel."*** **This makes that sentence mechanical instead of descriptive.**

**⚠ A Beast Master pays the acquisition price twice. A Droid Master pays for parts.**

### Hard

> **Anyone can die permanently.** **⚠ Henchmen included — the `Easy` rule does not apply here.**

**⚠ With exceptions determined by the GM.**

**No distinction between player, companion and henchman. −10 is −10.**

> **⚠ `PT-1421` — *"−10 is −10"* IS ABOUT ROLE, NOT ARITHMETIC.** The sentence it follows is *no distinction between player, companion and henchman* — **Hard's point is that the SAME band applies to everyone**, not that the number is ten. **⚠ `§5b` supersedes the figure: `E-2`'s flat `−10` is gone and the threshold SCALES with Constitution.** So on Hard a `Con 18` character dies at **−18**, and a henchman dies on the same band as a player. **Both sentences are true and they answer different questions.**

#### ⚠ DEFERRED TO HARD — the rakghoul plague

**Owner ruling, `PT-458`. NOT built now. Recorded so it is not rediscovered as a gap.**

**⚠ The rakghoul disease has NO mechanical implementation in either game.** **Swept exhaustively: 39 creature weapons, 14 rakghoul and kinrath blueprints, every `.uti` matching `rakg`, and seven property tables.** **`c_rakghoul`'s `FeatList` and `SpecAbilityList` are EMPTY and its weapon `g_w_crslash001` — a generic `1d4` shared with the Iriaz and the Brith — carries no on-hit property.**

> **⚠ And BioWare's own internal comment on `ptar_rakghoulser.uti` reads: *"This is the serum required to complete the various rakghoul disease plots on tar[is]."*** **The Rakghoul Serum has ZERO item properties. It is a quest token.**

**In KOTOR the plague is narrative. A rakghoul that hits you deals `1d4` and nothing else.**

**⚠ It belongs HERE, on Hard, because it is a permanence mechanic rather than a combat one** — an infection that gets worse between encounters and ends a character if untreated is the same shape as `Hard`'s permanent death, not the same shape as a poison.

**When it is built it should NOT reuse the poison chassis — `PT-457`.** **Poison is two saves and ability damage; a plague is a clock.**

**⚠ `iprp_immunity` row 4 is `Disease` — the engine has the category and nothing in the data uses it.** **`disease.2da` is NOT in holdings.**

---

## 3. ⚠ Exceptions are the GM's, and a package may set them

**Every mode above `Easy` allows named exceptions.** **A campaign package may name characters who cannot truly die, and say what happens instead.**

### The worked example — a KOTOR 1 package

> **Revan cannot truly die unless the whole party dies.** **And the encounter is rigged so that he is always the last one standing — he can only lose everything if he is the last one alive.**

**⚠ That is a *structural* exception, not a save-or-die reroll.** **It is not that Revan survives a killing blow; it is that the order of events is arranged so the killing blow reaches him last.**

**Which is the right shape for a story character in a package built on a known story, and it costs no new mechanic.**

---

## 4. What this settles

**⚠ The companion-death question, for every class that has one.**

    Engineer       a turned droid is the enemy's; it was never yours to lose
    Droid Master   §5
    Beast Master   the beast follows the mode, like any other companion

**A permanent companion is neither a devastating loss nor a shrug.** **It is whatever the table chose when it picked a mode**, which is where that decision belongs.

---

## 5. ⚠ Droid Master droids are the necromancer's undead

**Owner ruling. They do not follow `§4`.**

> **A Droid Master's droids are built, commanded, permanent until destroyed, and replaceable.**

**A destroyed droid is not a loss the way a beast companion is. It is a rebuild.**

**⚠ Which resolves the constraint `PT-151` raised** — *"either a devastating loss or a shrug, and both are bad"* — **by making the Droid Master's case genuinely different from the Beast Master's.**

**The Beast Master has one companion and it matters. The Droid Master has several and they are materiel.**

### And a Machinist may build one

**Owner ruling.** **A Machinist who chooses to can build a droid of their own.**

**⚠ The precedent is Bao-Dur and his remote — a technician who made himself a companion rather than being given one.**

    Machinist       may build one, if the player chooses to
    Droid Master    gets one automatically and chooses its chassis

**⚠ Which is the distinction between the two: the Machinist *can*, the Droid Master *is*.**

---

## 5b · ⚠⚠ A DROID **PLAYER CHARACTER** REBUILDS ON HARD, AND PAYS ITS BAYS. `PT-953`

> **⚠ OWNER RULING. ⚠⚠ `§5` ALREADY GIVES THE **COMPANION** REBUILD: ⚠ *"a destroyed droid companion may be repaired and rebuilt **to new**."* ⚠ THIS IS THE **PLAYER CHARACTER** CASE, WHICH WAS OPEN AT `DROID-CONSTRUCTION-01 §7`.**

    ⚠ EASY    ⚠⚠ NOBODY DIES — ⚠ THE QUESTION DOES NOT ARISE
    ⚠ NORMAL  ⚠ REBUILT ⚠⚠ TO NEW — ⚠ AS COMPANIONS ALREADY ARE
    ⚠⚠ HARD   ⚠ REBUILT, ⚠⚠ **AND `Constitution` DROPS BY 2**
              ⚠ ⚠⚠ **FLOOR OF 10** — ⚠ IT CANNOT GO LOWER

> **⚠⚠ AMENDED TWICE — `PT-953` TOOK THE BAY CONTENTS; `PT-968` SET `Con` TO 10; ⚠ `PT-969` MAKES IT ⚠⚠ **`−2` PER REBUILD, FLOOR 10**.**

### ⚠⚠⚠ WHY A **SUBTRACTION** AND NOT A **SET**

**⚠ A FLAT SET TO 10 IS ⚠⚠ WILDLY UNEVEN, BECAUSE DROID `Con` IS NOT UNIFORM:**

    ⚠ `Astromech`             ⚠ `Con` ~10 — ⚠⚠ **LOSES NOTHING**
    ⚠ `Assassin Droid MK VI`  ⚠ `Con` 19 — ⚠ LOSES **9**
    ⚠⚠ `Construction Mk II`   ⚠ `Con` 22 — ⚠⚠ LOSES **12**

> **⚠ THE TOUGHER THE DROID, THE HARDER IT IS HIT — ⚠⚠ AND AN ASTROMECH PAYS **NOTHING AT ALL**. ⚠ DEATH WAS FREE FOR THE CHASSIS THAT IS ALREADY FRAGILE.**

**⚠ AND A `Con 22` CONSTRUCTION DROID REBUILT AT 10 ⚠⚠ STOPS BEING THE THING IT IS. ⚠ THAT IS NOT A SETBACK — ⚠⚠ IT IS A DIFFERENT CHARACTER.**

### ✓ `−2` WITH A FLOOR DOES ALL THREE JOBS

    ⚠ EVERYONE PAYS ⚠⚠ THE SAME
    ⚠ NOBODY PAYS ⚠⚠ NOTHING
    ⚠⚠ AND IT STILL **CANNOT SPIRAL** — ⚠ 22 → 20 → 18 … ⚠⚠ **STOPS AT 10**

> **⚠ A DROID ALREADY AT ⚠ 10 PAYS IN ⚠⚠ **TIME AND PARTS** — ⚠ `DROID-CONSTRUCTION-01 §5a`'s SALVAGE ROUTE — ⚠⚠ NOT IN STATS IT DOES NOT HAVE.**

**⚠ AND EACH DEATH BECOMES ⚠⚠ A SETBACK YOU CAN **OUTRUN**, ⚠ WHICH IS WHAT LEVELLING IS FOR.**

### ⚠⚠ AND THE BAYS ARE NO LONGER EMPTIED

**⚠ ONE COST, NOT TWO. ⚠⚠ THE UPGRADES SURVIVE — ⚠ AND SINCE **UPGRADES ARE ONE ROUTE BACK TO `Constitution`**, ⚠⚠ EMPTYING THEM WOULD HAVE REMOVED THE REPAIR PATH ALONG WITH THE DAMAGE.**

### ⚠ WHY THE **BAY CONTENTS** AND NOT STATS OR LEVELS

**⚠ `DROIDS-UPGRADE-01 §1`: ⚠ THE **BAYS** ARE GRANTED BY ⚠⚠ CLASS AND LEVEL — ⚠ 3 / 6 / 9. ⚠⚠ WHAT SITS IN THEM WAS **BOUGHT AND INSTALLED**.**

    ⚠ THE BAYS ARE ⚠⚠ EARNED — ⚠ THEY SURVIVE
    ⚠⚠ THE CONTENTS WERE **PURCHASED** — ⚠ THEY DO NOT

> **⚠ SO THE COST IS ⚠⚠ **MATERIAL**, NOT CHARACTER. ⚠ IT DOES NOT COMPOUND, IT DOES NOT DEATH-SPIRAL, AND ⚠⚠ THE PLAYER CAN BUY THEM BACK.**

**⚠ A STAT LOSS ⚠⚠ COMPOUNDS — ⚠ REBUILD TWICE AND THE CHARACTER IS UNPLAYABLE. ⚠ A LEVEL LOSS PUNISHES ⚠⚠ THE PARTY, NOT THE DROID, BY OPENING A GAP THE GM MANAGES FOREVER.**

### ⚠⚠ AND MEMORY IS THE STORY, NOT THE BILL

**⚠ THE DROID COMES BACK ⚠ MISSING TIME. ⚠⚠ THAT IS WHAT KOTOR DOES — ⚠ HK-47 IS FOUND IN PIECES, T3 IS REPAIRED REPEATEDLY.**

> **⚠ IT COSTS THE PLAYER ⚠⚠ NOTHING MECHANICALLY, AND IT IS THE REASON THE BAYS ARE EMPTY: ⚠ THE CHASSIS SURVIVED THE SALVAGE, ⚠⚠ THE DELICATE EXPENSIVE THINGS BOLTED INTO IT DID NOT.**

### ⚠ AND THE REBUILD ITSELF USES `DROID-CONSTRUCTION-01 §6`

**⚠ NO NEW PROCEDURE. ⚠⚠ THE SAME `Repair` CHECK, THE SAME PARTS, THE SAME **FAILURE COSTS A DAY, NOT THE PARTS**.**

---

## 6. Open

**✓ ⚠ CLOSED — `PT-572`, recorded here at `PT-653`.** **⚠ PARTS AND TIME, NOT A LEVEL: the CHASSIS FRAME SURVIVES and the motivator, processor and cell are replaced — `DROID-CONSTRUCTION-01`.** **⚠ `PT-608` tiered the part prices: 700 / 1,400 / 2,800 by chassis tier.**

**✓ ⚠ CLOSED — `PT-559`, recorded here at `PT-653`.** **⚠ A COMPANION DIES AT `−Constitution`, LIKE EVERYTHING ELSE.**

> **⚠ `PT-559` REPLACED THE TWO-POOL SYSTEM AND MADE ONE THRESHOLD SERVE EVERY CREATURE.** **`BEASTS-LEVELS-01` states it; this paragraph never moved.**

**⚠ `E-2`'s flat `−10` is superseded. The threshold SCALES with Constitution, so a beast with `Con 18` and a character with `Con 10` are handled by ONE RULE at their own scales — which is exactly what this item worried could not be done.**

**✓ CLOSED — `PT-572`. `2,800` credits and one day: the MOTIVATOR, PROCESSOR CORE and POWER CELL.** **⚠ THE CHASSIS FRAME SURVIVES — wreckage is repairable — so a destroyed Assassin droid costs `2,800` rather than `6,900`.** **⚠ EVERY BAY INSTALLATION IS LOST, and that is the real cost.**

**⚠ Whether `Easy` mode's *"whole party dies"* means simultaneously or cumulatively.** **In KOTOR it is simultaneous — a wipe. Stated here so it is not read as attrition.**
