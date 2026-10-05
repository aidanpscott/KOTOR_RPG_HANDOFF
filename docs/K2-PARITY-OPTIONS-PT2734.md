# K2-PARITY-OPTIONS-PT2734 — K2's Options screens against ours

K2: `optionsingame_p.gui`, `optionsmain_p.gui`, `optfeedback_p.gui`, `optgraphics_p.gui` (extents read from the GFF) and live captures in `HANDOFF/BUILD/screens/options-k2/`; ours: side-by-sides in `.../sbs/`, K2 left, ours right. Owner rulings: `PT-2734` B. Rule: **what does not exist is left out, not faked.** Where a row is absent the list **closes up** (K2's own `optionsmain_p.gui` starts its first row at the same top as the in-game menu, so a missing row leaves no gap).

| Element | K2 | Ours | Status |
|---|---|---|---|
| Menu rows (318×32 on a 36 pitch from 134), hover white, selected pulses | Save, Load, Gameplay, Feedback, Auto-Pause, Graphics, Sound, Exit Game | Save Game, Load Game, Feedback, Graphics, Keyboard Shortcuts, Exit Game | = layout; rows omitted per ruling; **Keyboard Shortcuts is ours** (kept by the owner) |
| Hover help pane (`LB_DESC`, K2's strings 42301/42300/42278/48687/42302) | yes | yes, K2's words | = |
| Exit Game confirm | "Do you really want to quit? Your progress will not be saved." OK / Cancel | "Do you really want to quit?" OK / Cancel (ours saves as you go) | X owner ruling |
| Feedback | 8 rows | Hide Unequippable, Floating Numbers; check boxes `uibit_checkbxon/off`, K2's help (42286, 42291), Default = K2's defaults | = for the rows kept |
| Graphics | Brightness slider, Shadows, Grass, Force Speed, Screen Resolution, Advanced | Brightness only (`uibit_slider_p`, thumb native 8×32); washes the whole app | = for the row kept |
| Main-menu Options | Gameplay, Feedback, Auto-Pause, Graphics, Sound | Feedback, Graphics, Keyboard Shortcuts; no Save/Load/Exit/icon row, as `optionsmain_p.gui` | = |
| Quick-menu icon row on the in-game menu | yes | yes (shared chrome) | = |
| Window frame | K2 ornate frame | ours | X (PT-1309) |
| Footer: portrait, name, class line, bars, other members (in-game menu only) | drawn under the pane | drawn, the same widget as Equip's; default art for a companion with none | = |
| List scroll bars | 14-wide extent, thumb fills the track | thin strip (measured ~12 px), arrows + thumb | = (approx.) |

## Left out, per ruling ("not yet" / does not exist)
Combat Difficulty, Auto Level Up, Mouse Look, Reverse Mouse Y, Mouse Sensitivity, Mini Map, Subtitles, Tutorial Popups, Advanced Options, Shadows, Grass, Force Speed Effects, Reverse Mini-Game Y, the Mini Games key tab, the whole Auto-Pause screen, Key Mapping (the owner will set our map), Sound sliders (no audio yet), Gameplay screen. **Defaults I set, owner may override:** Screen Resolution, Reverse Mouse Buttons, Status Summary, Hide Quick Menu Buttons, Enable Tool Tips (we have no tool-tips).

## Floating Numbers (built)
Vitality changes float as the signed number, a miss floats "Miss", experience floats "+N XP"; ON by default, switched by the Feedback tick; they rise and fade over 1.4 s. **Colours, rise and timing are provisional** — not yet read off a K2 fight (none reachable without a save at a fight); one place, `_FloatStyle`. **GAP until read from K2.**

Proof: `options_screens_test`, `options_through_the_app_test`, `floating_numbers_test`, `app_settings_test`, `onjo_implant_refusal_fixture_test` (Hide Unequippable), all mutation-checked.
