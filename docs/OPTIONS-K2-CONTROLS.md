# OPTIONS-K2-CONTROLS — every control on K2's Options screens, and whether ours can have it

**For the owner (sent early, before building).** Source: K2 itself, read-only, captured live 2026-10-05 (`BUILD/screens/options-k2/`); the in-game Options menu, its five sub-screens, Mouse Settings, the main-menu Options, and the Exit Game prompt. Gameplay's Key Mapping was captured earlier (`pt2729-saveload/k2/33`).
**Why this list exists:** our Options were built as a *tabletop* list at `PT-1255`/`PT-2522` (Table Rules, Turn Pacing, Display, Rolls & Feedback, Sound, Session, Account, Keyboard Shortcuts, Leave Session) because "ours is not a video game". The order is now 1:1 with K2. Where K2 has an option our product cannot honour, that is named here for a ruling, as the Autosave checkbox was. **Recommendation** is mine; nothing is built until the owner rules.

Legend: **YES** we can build it as K2 has it · **MEANS** we can build it, with a stated meaning that differs · **CANNOT** the thing it controls does not exist · **RULE** the owner decides.

## The Options menu (in game) — `optionsingame`
| K2 control | Ours | Status / recommendation |
|---|---|---|
| Save Game · Load Game | K2's screens, built (`PT-2732`) | YES |
| Gameplay · Feedback · Auto-Pause · Graphics · Sound | the five sub-screens below | YES (the screens), see rows |
| Exit Game → "Do you really want to quit? Your progress will not be saved." OK / Cancel | ours is "Leave session" (`PT-1255`: "you leave a session, not a game") with a confirm | **RULE:** keep our label and a K2-style confirm with K2's sentence? Recommend yes: label "Exit Game" per 1:1, sentence word for word |
| Close | Close | YES |
| Hover help pane ("Save the current game") | none yet | YES, K2's own strings |
| Main-menu Options (before play): Gameplay, Feedback, Auto-Pause, Graphics, Sound only | our package menu has an Options row | YES |

## Gameplay
| K2 control | What it is in K2 | Ours |
|---|---|---|
| Combat Difficulty (◄ Normal ►) | Easy / Normal / Hard scaling of enemy strength | **CANNOT as K2 has it** — the ruleset has no difficulty dial; difficulty is the encounter's authored numbers (`PT-1255` kept "difficulty" under Table Rules as a GM call). **RULE:** show it disabled? hide it? or MEANS: a campaign-scoped Table Rule |
| Auto Level Up | levels spend themselves on a recommended build | **RULE / later:** needs the recommendations system already queued ("recommendations + Auto Level Up"). Show it dimmed with "not available yet", or omit until built |
| Mouse Look | the mouse always turns the 3D camera | **CANNOT** — a 2D board with no camera |
| Autosave | tick = the game autosaves on area changes | **Ruled at PT-2732: no checkbox** (ours writes continuously). Recorded as excused. |
| Reverse Mouse Y Axis | invert camera pitch | **CANNOT** — no camera |
| Reverse Mini-Game Y Axis | invert the swoop-bike / turret minigames | **CANNOT** — no mini-games |
| Combat Movement | movement during combat is allowed / locked while a target is selected | **CANNOT as K2 has it** — K2's combat is real-time with pause; ours is a turn with a movement budget |
| Mouse Settings (button) | Mouse Sensitivity slider · Reverse Mouse Buttons tick | Sensitivity **CANNOT** (no look speed). Reverse Mouse Buttons **MEANS** swapping primary and secondary click (we use the secondary click for portraits and the action menu): feasible, **RULE** |
| Key Mapping (button) → Movement · Game · Mini Games tabs, OK / Cancel / Default | rebind every key | **MEANS:** rebind OUR keys (the board's real key grammar, `PT-2544`'s Keyboard Shortcuts list becomes the Game tab). Mini Games tab **CANNOT**. **RULE:** build the rebinding (a real feature) or show K2's list read-only with our keys? Recommend read-only first, rebinding later |
| Close · Default | close; reset this screen's values | YES |

## Feedback
| K2 control | Meaning in K2 | Ours |
|---|---|---|
| Hide Unequippable | hide items the character cannot use in lists | **YES** (we know what a character can equip: `EQUIPMENT-01 §17`) |
| Tutorial Popups | the boxes like "Immersion in kolto tanks…" | **CANNOT yet** — we have no tutorial popups. Show dimmed, or omit until we write some |
| Subtitles | show spoken dialogue as text | **CANNOT** — no voiced dialogue; text is always shown. Omit, or tick-locked-on |
| Mini Map | the corner mini-map | **RULE:** our board is the map; a mini-map overlay does not exist. Omit |
| Floating Numbers | XP, Vitality and Missed-Attack text floats over heads | **MEANS** a floating figure over the board square on a hit/miss: not built; the combat log says it today. **RULE** |
| Status Summary | party status text/summary on screen | **RULE:** needs the K2 meaning read (tool-tip text not captured). Not captured: help pane empty when I hovered |
| Hide Quick Menu Buttons | hide the corner quick-action icons | **MEANS** hide our quick-action buttons if we draw some; **RULE** |
| Enable Tool Tips | hover tool-tips | **YES** if we have tool-tips (check); else CANNOT yet |

## Auto-Pause (K2 is real-time; these decide when it pauses)
End of Combat Round · Enemy Sighted · Mine Sighted · Party Member Down · Action Menu Used · New Target Selected.
**All six CANNOT:** ours is turn-based and always waits; there is nothing to pause. (Mine Sighted: no mines.) **RULE:** omit the screen, or keep it as a read-only page saying "the table waits for you"? Recommend omit… but 1:1 says keep the row, so **show the screen with its six ticks fixed on**, each help line saying so. Needs a ruling.

## Graphics
| K2 control | Ours |
|---|---|
| Brightness (slider) | **YES** (a dimming overlay on our own screens) |
| Shadows · Grass · Force Speed Effects | **CANNOT** — 3D renderer features |
| Screen Resolution | **MEANS** window / full-screen size on desktop; **RULE** (the app is windowed on a desktop and may be a browser later) |
| Advanced Options | **CANNOT** (anti-aliasing, texture quality, vsync of a 3D engine) |

## Sound
Music · Voice-over · Sound Effects · Movie Volume sliders. We have **no audio at all yet** (and Movies are a package-menu row). **MEANS:** the four sliders exist and are stored; they do nothing until audio exists, **or** omit. **RULE.** Voice-over **CANNOT** (no voice).

## Summary of what the owner must rule (the short list)
1. Combat Difficulty: omit, dim, or a campaign Table Rule.
2. Auto Level Up: dim until the recommendations system exists?
3. Mouse Look, Reverse Y (both), Mouse Sensitivity, Mini Map, Subtitles, Shadows, Grass, Force Speed Effects, Advanced Options, Mini Games keys: **cannot exist** — omit them (recommended), or show them dimmed with the reason?
4. The whole Auto-Pause screen: omit, or six fixed-on ticks?
5. Key Mapping: read-only list now, rebinding later?
6. Sound: sliders that store a value now and act when audio exists?
7. Floating Numbers, Hide Quick Menu Buttons, Status Summary: build, or omit?
8. Exit Game label and K2's confirm sentence.

**Rule of thumb I will follow unless told otherwise:** an option whose thing does not exist is **left out, not faked**; a control that stores a value nothing reads would be the "mechanism that only reports success" (`PT-2423`). Everything marked YES is built 1:1 (layout from `optionsingame_p.gui` and its sub-panels, K2's own strings from `dialog.tlk`, K2's help text on hover).
