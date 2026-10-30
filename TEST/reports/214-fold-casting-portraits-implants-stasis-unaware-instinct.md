# TEST 214: the one fold, a companion's powers outside a fight, the small portraits, implants, Stasis, unaware, Killer's Instinct

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-214/` (MAIN_WORK `249926fe`). The step-by-step log is `TEST/reports/214-running-log.md`.

## Build

- **App**: main `e7095dc` (includes `36c1d38`), a git worktree beside my own clone. `gate.py --at e7095dc`: "FOR TESTER — CORE at e7095dc, 5318 tests, 0 failed"; ARCHIVE last green at e7095dc. The gate's verdict line said "DO NOT SEND — 1 blocking failure": `check_shelf_repo.py`, one path under `base-rules/` uncommitted in the shared Shelf working tree, not in the build. Lodestar `279b521` = lock = compiled. The build (10.4 s) went through the lock, and git status was clean.
- **Settings**: defaults.
- **Shelf** `e612e14`, synced; check_shelf clean (33 rules files, 125 blueprints).

Local bed, package **tester-214**:

- **Stasis Yard**, with five enemies, all Soldier 3, Dex 16, 300 vitality:
  - Para Guard (Force Immunity: Paralysis);
  - Stun Guard (Force Immunity: Stun);
  - Target;
  - Seer (Precognition);
  - Saver (Con 30).
- **Blade Mate**, a companion without Killer's Instinct.
- **Players**:
  - Yard Jedi and Yard Flurry: Consular 16 with Killer's Instinct, Stealth 20, Stun, Stasis, Stasis Field, Blindness and Push. Yard Flurry carries Freedon Nadd's Short Lightsaber, for knockdown.
  - Implant Low and Implant None: Soldier 4, Constitution 6. Low has Cybernetic Implantation and None doesn't; both carry a Strength Package and a Mental Boost Package.
- **Reused**: tester-align (Plain Mate) and tester-kit (Weak Mate).

## Summary: all pass; two findings

| # | Check | Result |
|---|---|---|
| 1 | One fold | **PASS**. Plain Mate: Equip DEF 15 = sheet Defense 15. The player is 15 = 15; Blade Mate and Implant Low match too |
| 2 | Companion's powers outside a fight | **PASS**. Controlling Plain Mate, f reads "1 Heal 8f · 2 Force Affliction 12f · 3 Force Push 6f" with "force 105 of 105" (the player has 155). The cast: "Plain Mate: Heal · 8f — 105 → 97 … at Dark Mate" |
| 3 | Small portraits | **PASS**. In Equip, Character and Abilities the small portrait switches the page's member, both out of a fight and in one on my turn |
| 4 | Implants | **PASS, one finding**. With the feat at Constitution 6, the Strength Package equips and works: Strength 11, no refusal line. The pane reads "Feats Required: Cybernetic Implantation" with no Constitution, and Mental Boost's does too. Without the feat: "… it needs the Cybernetic Implantation, Advanced Cybernetic Implantation or Master Cybernetic Implantation feat." Chargen's Constitution text doesn't mention implants. Weak Mate's file implant shows no gate line. **Finding 1** is below |
| 5 | Stasis and Stasis Field | **PASS**. Neither the status line nor the Combat log ever says "is stunned"; failed saves read "paralysed". The Paralysis-immune guard "resists" both powers; the Stun-immune guard is "paralysed" by both. A made save gives "slowed", e.g. "d20 20 = 33 vs 21 · slowed" |
| 6 | Unaware | **PASS, one finding**. Against an aware target the line reads "needed 13". Paralysed: "needed 10 (-3 Dexterity: unaware)". Hidden ("hidden — 22 beat 3"): "needed 10 (-3 Dexterity: unaware)". Stunned: "needed 9 (-3 Dexterity: unaware)", which also carries slowed's −1 from an earlier save. Prone and Precognition read "needed 13", and slowed reads 12 (slowed's own −1); none of the three has an unaware term. **Finding 2** (blinded) is below |
| 7 | Killer's Instinct | **PASS**. Every hit on a paralysed, stunned, blinded or hidden target adds "+1d6 Killer's Instinct N". On a critical: "4d6 2+3+6+6 + 1d8 energy 1+5 + Strength 3×2 × 2 critical +1d6 Killer's Instinct 6". The weapon dice double; the rider is rolled once. Blade Mate, who lacks the feat, adds nothing on a hit or on a critical |
| 8 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 51 ("reg214"), Escape then F4 (one quick save), Load, and a fight won |

## Findings

1. **A companion's file implant doesn't show on her sheet.** Weak Mate has Constitution 10, Crado's Robe and the Bio-Antidote System (+1 Constitution) in her file. Her Stats read Constitution 10, not 11. The robe in the same file does count (Defense 13). Her Equip says "No equipment is recorded for Weak Mate", so I can't tell whether the implant is worn and not added, or not worn.
2. **A blinded target's line doesn't name the lost Dexterity.** After Force Blindness ("blinded" on all five), Blade Mate at Saver reads "needed 8 — miss" and mine at Target reads "needed 8 — hit"; both read 13 when aware. The line has no "(-3 Dexterity: unaware)" term, and the number drops by 5, not 3. Killer's Instinct does fire on the blinded target.

## Small

None.

Seen, not filed:
- Two of my hits in a row rolled the same damage dice ("2d8 8+1 … +1d6 Killer's Instinct 1") on different d20s.
- Four natural 20s came up in about a dozen saves in one fight.

Both are one sample each.

KNOWN, not filed: Stasis's description still says "instead of stunned"; the three 213 small items (in Kit Hall, with three companions, the menu's two small portraits reach Crado and Arca Mate but not Weak Mate; the HUD portrait reaches her); Sneak Attack.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
