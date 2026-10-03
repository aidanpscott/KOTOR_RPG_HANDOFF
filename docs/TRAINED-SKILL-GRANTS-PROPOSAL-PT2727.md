# TRAINED-SKILL-GRANTS-PROPOSAL-PT2727 — which classes start trained in Demolitions, Stealth or Security

**RULED — owner, 2026-10-03 (via Main): the six proposed classes PLUS Bounty Hunter (Demolitions — "mines and traps fit a hunter"). BUILT: `classes.toml` `granted_skills`, a derived level-1 class grant (`classes_start_trained_test`).** *(Originally a proposal; the Bounty Hunter row below is now a grant, not "listed only".)* Owner ruling (via Main, 2026-10-03, under `PT-2727`): classes built around Demolitions, Stealth or Security start with a rank in that skill, granted at level 1, so they can use their identity on day one. This lists all **39** classes (`classes.toml`): which of the three each would start with, **1 rank** each unless a source says more (**none does**), and the basis.

**Columns.** *Ours* = the skill is on the class's own `class_skills` list (`classes.toml`, from `CLASS-TABLES-*` / `SKILLS-01 §9`). *K2* = the `skills.2da` column of the K2 class of the same name (`class`, and `reco` = K2's recommended order, 1 = first), only where K2 has that class. *Kit / identity* = the class's starting kit (`starting_items.toml`) or described role. **sourced** = ours AND (K2 agrees or the kit names it); **by identity** = the kit or role names it though no source list does; **listed only** = on our list, nothing else ties the class to it → **no grant proposed** (the owner may flip it).

| Class | Tier | Proposed start | Basis |
|---|---|---|---|
| **Saboteur** | base | **Demolitions 1** | **sourced + identity.** Ours: Demolitions, Stealth, Security. Kit: **Minor Frag Mine** + 2 frag grenades — the mine is a Demolitions action. (No K2 class.) *Stealth, Security: listed only.* |
| **Smuggler** (K2 *Scoundrel*) | base | **Stealth 1, Security 1** | **sourced.** Ours: all three. K2 `scd`: Stealth reco 1, Demolitions 2, Security 3. Kit: **Security Tunneler**. *Demolitions: K2 reco 2 but no kit → listed only (owner may add).* |
| **Engineer** | base | **Security 1** | **sourced + identity.** Ours: Security. Kit: **4 computer spikes** (Security's spike). |
| **Agent** | base | **Stealth 1, Security 1** | **by identity + ours.** Ours: Stealth, Security. `CLASS-ROSTER`: "rebuilt as the spy" (`PT-179`), class feats Field Position, Cover Identity. |
| **Jedi Sentinel** | force base | **Stealth 1, Security 1** | **sourced.** Ours: Stealth, Security; K2 `jsn`: Stealth reco 1, Security 5; role line "skills, stealth, versatility" (`CLASS-TABLES-JEDI`). |
| **Sith Assassin** | force base | **Stealth 1, Security 1** | **sourced.** Ours: Stealth, Security; K2 `sas`: Stealth reco 1, Demolitions 2, Security 5; "mirrors the Jedi Sentinel" (`CLASS-ATTACKS-01`). *Demolitions: K2 class skill, not ours → no.* |
| Soldier | base | none | listed only: Demolitions (ours; K2 `sol` reco 3). Kit is frag grenades, which are thrown, not Demolitions. |
| Scout | base | none | listed only: Demolitions (ours; K2 `sct` reco 2). |
| **Bounty Hunter** | base | **Demolitions 1** | **RULED, the owner's addition** — mines and traps fit a hunter. (On its list; no kit tie. Stealth stays *listed only*.) |
| Marksman | base | none | listed only: Demolitions. |
| Machinist | base | none | listed only: Demolitions. Kit: parts, repair kits, frag grenades — identity is repair, not mines. |
| Treasure Hunter | base | none | listed only: Demolitions. |
| Medic · Brawler · Duelist | base | none | no tie to any of the three. |
| Jedi Guardian · Jedi Consular · Sith Inquisitor · Sith Warrior | force base | none | no tie (K2 `jgd` lists Demolitions, ours does not). |
| **All 24 prestige classes** — Commando, Droid Master, Gunslinger, Officer, Shadow Hunter, Juggernaut, Beast Master, Scoundrel, Tech Specialist, Sharpshooter, Operative, Shock Trooper, Blademaster, Pirate, Jedi Weaponmaster, Jedi Watchman, Jedi Sage, Sith Marauder, Sith Battlemaster, Sith Sorcerer | prestige | **none** | **Entry already requires the training.** `CLASSES-STANDARD-PHB` prerequisites: Operative needs Stealth 8 + Slicing 8, Shadow Hunter Stealth 8, Scoundrel Stealth 8, Tech Specialist Engineer 6 *or* Machinist 6 (an Engineer has Security 1 under this proposal). No prestige row states a grant (`SKILLS-01 §11a` would be the place). |

**Total as ruled:** 7 base classes receive ranks (Saboteur 1; Smuggler 2; Engineer 1; Agent 2; Jedi Sentinel 2; Sith Assassin 2; Bounty Hunter 1); 32 receive none, **including all 24 prestige classes**.
**The owner's decisions:** (1) accept the six; (2) whether any *listed only* row should flip to a grant — the candidates are **Soldier/Scout/Marksman/Machinist/Treasure Hunter/Bounty Hunter: Demolitions**, **Smuggler: Demolitions**, **Bounty Hunter: Stealth**; (3) the Jedi Guardian/Watchman/Weaponmaster and Sith Marauder carry Demolitions in **K2's** class columns (reco 2) but not in ours — recorded, not proposed.
**How it would be built (after the ruling):** a level-1 class grant through the existing grant pipeline (`class` grants in `classes.toml` → the ledger's `skill-ranked` with `source: granted`), not from the player's skill points, shown as class-granted on the sheet; text in `SKILLS-01 §11a` and each affected class's table citing the ruling; tests that a new Saboteur sets its starting mine with no point spent and a class with no grant is still refused.
