# TEST 223: the stealth opener (as K2), save lines that name their source

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and my beds are in `KOTOR_RPG_MAIN_WORK/media/screens/test-223/` (MAIN_WORK `e2b56de1`).

## Build

- **App**: main `d0c9c3e`, a worktree beside my clone. `gate.py --at d0c9c3e`: "SENDABLE — 6 warning(s)"; "FOR TESTER — CORE at d0c9c3e, 5476 tests, 0 failed"; ARCHIVE last green at d0c9c3e. Lodestar `4f97619` = lock = compiled; built through the lock in 10.1 s; git status clean.
- **Settings**: defaults (no settings.json). **Shelf** `194cc43`, synced; check_shelf clean (33 rules files, 128 blueprints).
- **Beds**: `author_tester_test221_saves.dart` rerun (Sneak Strike, Shot Strike), with pristine copies kept so each replay starts clean. My own, each with Sneak Strike's build (Scoundrel 5, Dex 18, Stealth 8, Sneak Attack, Vibroblade): **Stranger Sneak** (tester-220's Stranger Yard, the Stranger 6 squares off, not fighting on sight) and **Market Sneak** (tester-talk's Market, Dressa the merchant). **Aura Saver** (Jedi Consular 4 knowing Force Aura) in tester-powers' Power Yard, facing Power One's Sith Apprentice.

## Summary: all pass

| # | Check | Result |
|---|---|---|
| 1 | Stealth opener | **PASS**. Sneak Strike: s → "hidden"; one step right → "hidden — d20 13 + Stealth 8 + Dexterity 4 = 25 beat 9"; nine more steps; x → "Sneak Attack"; the walk into the sentry: the box heads "Stealth Mode Deactivated (Run Enabled)", then "Sneak Attack · Vibroblade · rolled 20 — d20 16 + attack 3 + Strength 1 · needed 10 — hit · damage 14 — 1d10 4 + Strength 1 +2d6 Sneak Attack 6+3 · 386 left", then "Sith Sentry: unarmed · rolled 4 … needed 16 — miss", and it is her turn. Combat log: "Round 1 / Sneak Strike attacks Sith Sentry : *hit* … 14 damage / Sith Sentry attacks Sneak Strike : *miss* / Sneak Strike attacks Sith Sentry : *hit* … 6 damage": her own round-1 turn comes after the opener. Shot Strike: the same walk; x → "Stealthy Shot"; "Stealth Mode Deactivated (Run Enabled)", then "Stealthy Shot · Blaster Pistol · rolled 19 … hit · damage 21 — 1d8 8 + Dexterity 4 +2d6 Stealthy Shot 6+3 · 379 left", the sentry misses, and her next shot is again in Round 1. **Controls**: seen, the walk into the Stranger → "initiative — Stranger Sneak 21 · Stranger 18", log "A fight begins.", no strike. A seen Sneak Attack (x → "Sneak Attack", round 2): "Sneak Attack · Vibroblade · … hit · damage 6 — 1d10 5 + Strength 1", no 2d6. Hidden, the walk into Dressa: "Dressa: Looking to trade? …" with the replies; after [Leave.] the stealth icon is dim and Messages reads "Stealth Mode Deactivated (Run Enabled)". x outside a fight: hidden → "Sneak Attack" (declared); not hidden → "nothing is threatening you" |
| 2 | Save lines | **PASS**. Aura Saver: before the aura, "Horror at Aura Saver · Aura Saver — d20 18 + will 4 + Wisdom 1 = 23 vs 7 · shaken". Force Aura → "+2 defense · +2 saves". Then "Horror … d20 3 + will 4 + Wisdom 1 + Force Aura 2 − shaken — Horror 2 = 8 vs 7 · shaken" and "Force Slow … d20 12 + will 4 + Wisdom 1 + Force Aura 2 − shaken — Horror 2 = 17 vs 7 · resists". Each adds up. The apprentice's swing: "needed 15 (+2 Force Aura)". No "power" in the box or in the Combat log |
| 3 | Dice, regression | **PASS**. All 17 lines match the 206 baseline. Regression: Save to slot 60 ("reg223"), Escape then F4 (one quick save), Load, and a fight won (Icon Nine 94 of 196) |

Seen, not filed:
- In Sneak Strike's own round-1 turn, my x press cycled the declaration off (its strike read plain "Vibroblade"), since it was still set from before the walk-in. Pressing x again in round 2 showed "Sneak Attack". This is the cycle doing its job.
- Seen, Sneak Strike is spotted by the Sneak Hall sentry six squares out and the fight starts on sight ("A fight begins.", no strike), so it can't take a seen bump; I used the Stranger for that.

KNOWN, not filed: the Flurry and Rapid Fire count (now ruled at three); ranged attacks outside a fight; the stale "is hidden" Combat log line (TEST 222 small item 1, with Coder).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
