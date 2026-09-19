# FORCE-POWER-SKILL-01 — what a power adds to a skill, and for how long

**⚠⚠ THIS TABLE EXISTS BECAUSE A SKILL BONUS COULD ONLY BE WORN — `PT-2280`'s sweep, `PT-2294`'s ruling.** `mergedSkillBonuses` folds what a character is WEARING, off a `Map<String, int>` on a piece of kit. `Improved Force Camouflage` states *"an additional **+4** to their Stealth skill when this power is in effect"* and `Master Force Camouflage` states **+8**, and a worn map cannot hold either: it has no source and no clock, so two grants of the same size from different places are one number.

## What is *not* here

**⚠⚠⚠ THE BASE TIER GRANTS NO NUMBER AT ALL, AND HAS NO ROW.** `Force Camouflage` reads, in full: *"This power enables the Jedi character to use their Stealth skill without a Stealth Field Generator."* That is a **permission**, not a modifier — and the thing it gives permission for **does not exist in this build**. `hideCheck` takes a stealth-field argument and the caller passes `false`, with its own note saying why: *"`§4`'s stealth field generator is an ITEM, and no item in the catalogue declares itself one yet… Passing `false` is this build having no field, not a decision that the rule does not apply."* **There is nothing for the base tier to switch off.** A row here would be a rule with no reader; the gap is the item, and it is named rather than invented around.

**⚠ AND NO OTHER POWER IN THE CORPUS TOUCHES A SKILL.** Censused across all 104 — three name one, and all three are this chain.

## The columns

| column | meaning |
|---|---|
| `skill` | one of the **26** the ruleset carries, spelled as `SKILLS-01` spells it. ⚠ The reader keys by `skillKey`, so `Stealth` and `stealth` are one skill — but the table states the document's spelling, and a word outside the 26 is refused loudly here rather than silently never matching. |
| `points` | **POSITIVE, and ADDED by the reader** — the same statement `FORCE-POWER-ABILITY-BONUS-01` makes, for the same reason. |
| `rounds` | the power's own stated duration. ⚠⚠⚠ **BOTH ROWS WERE `—` AND ARE NOW `10` — `PT-2401`.** They transcribed the source's *"lasts until the character deactivates it"*, and this column's own note named the hole that left: ***nothing in the product can deactivate a power***, so the bonus ran for ever. `POWER-COSTS-01 §4.2` had already ruled the answer — *"In a real-time game an indefinite toggle costs attention. In a turn-based one it costs nothing, because a player would simply never turn it off. The correct translation is a bounded duration: 10 rounds."* — and it had never been carried into any table. A ruling that reaches no reader is not built. |

## The table

| Power | `id` | skill | points | rounds |
|---|---|---|---|---|
| **Improved Force Camouflage** | `improved_force_camouflage` | Stealth | 4 | 10 |
| **Master Force Camouflage** | `master_force_camouflage` | Stealth | 8 | 10 |
