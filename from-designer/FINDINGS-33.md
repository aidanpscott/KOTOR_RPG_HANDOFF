# FINDINGS-33 — ⚠ Retraction. `Superior Two-Weapon Fighting` is a penalty reduction and I said it was not.

**Owner asked whether we are using KOTOR 2's version or an invented one. The answer is: ours is a faithful port and my reading of it was wrong.**

---

# 0 — What I said, and why it was wrong

**`FINDINGS-32` and the conversation before it argued that `SUPER_WEAPON_FOCUS_2_WEAPON` is an *attack bonus*, on the grounds that its row name sits in the `SUPER_WEAPON_FOCUS_*` family alongside the lightsaber version, which our library prints as `+1 / +2 / +3` attack.**

> **⚠ That was an inference from a row label. It is wrong.**

**StrategyWiki, on KOTOR 2 combat — *secondary source, marked as such*:**

> *"Once Two-Weapon Fighting has been mastered, the Jedi Weapon Master and Sith Marauder Prestige classes can then select Superior Two-Weapon Fighting to **reduce this attack penalty even further**."*

**It reduces the penalty. `FEATS-LIBRARY-01`'s presentation is correct in kind and I called it invented.**

**⚠ The failure is the one this project names most often.** **I had the row label and the prerequisite chain and I built a conclusion on the naming convention without a source that says what the feat does.** **`FINDINGS-32 §1` should be read as withdrawn on this point.**

---

# 1 — What the source actually says, and it answers the owner's ruling exactly

**Three facts, all from the same secondary source and all consistent with `feat.2da`'s prerequisite rows:**

**One — it is restricted to two classes.** > *"only a Jedi Weapon Master or Sith Marauder can then select Superior Weapon Focus: Lightsaber,"* **and the same two for `Superior Two-Weapon Fighting`.**

> **⚠ The owner's instinct — *"only 1 or 2 classes can use it"* — is the source's own rule. Two classes, and they are named.**

**Two — `FEATS-LIBRARY-01` files both chains under **Any prestige class**. That is the departure, and it was ours.**

**Three — the `+2` is not the feat.** **StrategyWiki:** *"a balanced weapon… adds Small Offhand Bonus 2 to the attack(s) of the main hand: **All blaster pistols**, Double-Bladed Lightsabers and double-handed melee weapons are balanced."*

    Superior TWF, top tier      0 main / −1 off      the feat
    balanced weapon            +2 main               a property of the weapon
    printed in our library     +2 main / −1 off      the two, folded together

**So our library's line is arithmetically right and presentationally misleading.** **The feat reaches zero; the weapon supplies the plus.**

---

# 2 — Which means the contradiction is real, and it is ours

**`ACTION-ECONOMY-01 §7.2`:** *"Never zero — the principle every attack chain follows."*

> **⚠ That principle is authored. KOTOR 2's penalty does reach zero, for two prestige classes, and our port of the feat is faithful.**

**So the conflict is not a bad port. It is a house rule colliding with a correct one.**

**Three ways to close it, and the second is now clearly best:**

**Amend `§7.2`.** *"Never zero, except through `Superior Two-Weapon Fighting`."* **⚠ Honest, and it makes the exception visible where a reader will look for it.**

**Restrict as the source does — `Jedi Weaponmaster` and `Sith Marauder` only.** **⚠ This is the owner's ruling and the source's, arrived at independently.** **`§7.2` still needs the exception clause, but it now applies to two Force prestige classes rather than to anyone who prestiges.**

**Re-point the chain at the off hand.** **⚠ Withdrawn. `FINDINGS-32 §1` proposed it to preserve a principle that the source does not share, on the strength of a reading that was wrong.**

---

# 3 — ⚠ Two consequences worth catching now

**`PT-150` opened `Superior Weapon Focus` from lightsaber-only to all six weapon families, for the `Commando`.**

**The source restricts it to `Jedi Weaponmaster` and `Sith Marauder`.** **So `PT-150` departed further than the record shows: it did not open a *lightsaber* feat to other weapons, it opened a *two-class* feat to any prestige class and then to six families.**

> **The Commando still needs it and the departure is still right — `FINDINGS-29 §4.1`'s argument stands, that a prestige Soldier could reach nothing where a prestige Jedi reached `+3`. But the ruling should record what it departed from.**

**And giving `Superior Two-Weapon Fighting` to the `Gunslinger` is a departure too.** **The source's version is for Jedi and Sith dual-wielding lightsabers.**

**⚠ It is a departure I would still make, and for the same reason as the Commando's:** **all blaster pistols are balanced weapons, so a two-pistol build is the one the `+2` was written for, and no Force class in our roster is built on pistols.** **But it should be marked as authored rather than ported.**

---

# The question

> **⚠ Restrict to `Jedi Weaponmaster` and `Sith Marauder` as the source does, or extend to the `Gunslinger` as a marked departure?**

**Either way `ACTION-ECONOMY-01 §7.2` needs an exception clause, because the penalty does reach zero and our rule says it never does.**
