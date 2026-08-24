# FINDINGS-49 — ⚠ Retraction: `FORMS-01` exists. And a name collision it exposes.

**`REPLY-45`'s three fixes are `§4`. `§1` to `§3` are the damage from the retraction and one of them is not small.**

---

# 0 — What I claimed and why it was wrong

**`FINDINGS-47 §3`:** *"There is no Force-form system anywhere in the corpus — **not a document, not a feat row, not a mention**."*

**`docs/FORMS-01.md` is 18 kilobytes, is titled *Lightsaber and Force Forms*, carries all four Force forms with effects, and is cited three times by `FORCE-POOL-01-v3` as a live warrant.**

**⚠ I searched `feat.2da` and `ATTACKS-06` and made an absolute claim about the whole corpus from two files.**

> **`FORMS-01 §1` is titled *"`formmask` is not a form pointer."*** **The document exists **because** the feat table does not carry forms. The absence I found is that document's own opening finding.**

**⚠ Fourth instance of this shape from me, after the range rules in `FINDINGS-38`.** **The countermeasure I wrote there — *a negative about a document has to be confirmed by opening it* — was the right rule and I did not apply it to `docs/` as a whole.**

**Concretely: `ls docs/` costs one call and I did not make it.**

---

# 1 — ⚠ `FINDINGS-32`'s acquisition rules rest on a premise `FORMS-01` rejects

**I built form acquisition on `ATTACKS-06`'s *"Forms are feats."*** **`FORMS-01 §2` is titled *"Forms are conditions, not feats"* and `§4` lists it under **Settled**.**

**Three things in `FINDINGS-32` are wrong as a result:**

**The feat cost.** **I ruled *a form learned after 5th level costs one feat*. `FORMS-01 §4`: *"No cost, no duration."*** **⚠ The price I invented does not exist.**

**One group, not two.** **I treated all forms as a single exclusion group. `FORMS-01 §2.1`: **two** groups, and a character holds one of each simultaneously.** **⚠ So a Jedi has a lightsaber form *and* a Force form at all times, and my grants only ever gave one.**

**The Battlemaster's tier 1.** **`Master of Forms` grants *switch once per encounter as a free action*. `FORMS-01 §4`: switching already *"costs an action."*** **⚠ The tier converts an action to a free action once per encounter, which is far less than I priced it at.**

## 1.1 What survives

**The class-to-form assignments in `FINDINGS-32 §3.1` hold, and one is confirmed by `FORMS-01` independently.**

**`FORMS-01 §6.1` on Moderation:** *"the diplomat's form… favoured by **Jedi Consulars**… the only lightsaber form that touches Force powers at all, which makes it the Consular's saber form."*

> **✓ I assigned Moderation to the Consular from the form's mechanical description. `FORMS-01` reaches the same place from Wookieepedia and a Kavar quote.**

**And the owner's prestige-entry ruling now applies as given — `§2`.**

---

# 2 — ⚠ `Force Channel` is two different things

**`PT-103` renamed the Jedi Consular's class chain `Force Focus` → **`Force Channel`**.**

**`FORMS-01 §6.2` names Force form I **`Force Channel`**.**

    feat.2da     FORCE_FOCUS · FORCE_FOCUS_ADVANCED · FORCE_FOCUS_MASTERY
                 -> jcn_granted at 1 / 6 / 12 -> our "Force Channel", PT-103
    FORMS-01     FORM_FORCE_I_FOCUS -> "Force Channel", from Force_Forms_Table.docx

> **⚠ Two distinct source rows, both renamed to the same string, by two workstreams, from the same underlying word.**

**They are not the same object.** **One is a granted class chain that extends buff duration; the other is a persistent condition giving `+50%` out-of-combat regeneration, `+3` power damage and `+2` saves.**

**⚠ And under the owner's ruling a `Jedi Master` could hold both at once — the class chain from being a Consular, and the form from prestige entry — and a player would have no way to tell which one a rule meant.**

**One has to be renamed. `PT-103` is mine and the later collision is not, so I would rename the class chain rather than the form** — **the form's name comes from a source document and mine came from me.**

---

# 3 — The prestige-entry ruling, applied

**Owner: a lightsaber form on entry; a Force form for `Jedi Master` and `Sith Lord`; a choice for `Watchman` and `Marauder`.**

| Class | Grants on entry |
|---|---|
| **Jedi Weaponmaster** · **Sith Battlemaster** | one **lightsaber** form |
| **Jedi Master** · **Sith Lord** | one **Force** form |
| **Jedi Watchman** · **Sith Marauder** | **choice of either** |
| **Jedi Sage** · **Sith Sorcerer** | ⚠ not named in the ruling — they are the caster pair, so **Force form** by symmetry with Master and Lord. Confirm. |

**⚠ And `FORMS-01 §2.1` means this is additive rather than exclusive.** **A Jedi Master entering with a Force form still holds whatever lightsaber form the base class gave them — the groups do not interact.**

---

# 4 — `REPLY-45`'s three fixes

**`Read the Ruin` — Explorer. Tiers 2 and 3 cut. Replacements scale the one idea:**

| Tier | | Effect |
|---|---|---|
| **`Read the Ruin`** | 1 | A failed knowledge, `Security` or `Awareness` check **tells you why it failed**. |
| › **`Second Look`** | 4 | It also tells you **what would succeed** — a tool, a skill, a piece of knowledge you lack. |
| ›› **`Nothing Is Sealed`** | 8 | It tells you **whether anything would**, so the party knows to stop trying. |

**⚠ Each tier is more of *knowing why*, not a new verb.** **The capstone is the one that saves a session: it ends the search rather than extending it.**

**`Dominion` — Sith Inquisitor. Partial-success clause cut.** **Capstone becomes `+3` and nothing else. One idea: harder to resist.**

**`Quarry` — Bounty Hunter. Combat bonuses cut.** **Capstone becomes: **you always know where your quarry is**, at any distance, while it lives. Information and capture, which are the same idea.**

---

# The question

> **⚠ `§2` — `Force Channel` names two objects. Rename the class chain, or the form?**

**And `§1` — `FINDINGS-32`'s acquisition rules need reworking against `FORMS-01`. That is mine and I will take it next unless it belongs with whoever holds `FORMS-01`.**
