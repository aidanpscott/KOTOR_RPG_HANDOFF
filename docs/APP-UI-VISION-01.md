# APP-UI-VISION-01 — foundational outline, first pass

**Status: working draft. Not a ruling. Written to be handed to a Claude Code exploration pass next, and possibly Claude Design for mockups after that.**

Scope: the player-facing app only. The builder (the authoring tool, `BUILDER-VISION-01`) is a separate document — corrected at `PT-1130`, since this line had gone stale claiming the builder was still deferred when it's been running in parallel for a while. Concretely: the palette UI and freeform mode, both author-only tools for building rooms, live entirely in the builder document and have no counterpart here — checked directly at `PT-1131`, confirming neither ever appeared here. `PT-1023` makes both call the same engine, so decisions made here about what the engine needs to expose will shape the builder too, but the builder's *own* UI is out of scope for this document.

---

## 0. Two layers, not one

The console-home-screen and the per-campaign-main-menu are different screens with different jobs, and should stay structurally separate rather than collapsing into one flat "pick a game" screen.

**Console Home** — before any package is running.
- Your library of campaign packages (the "games" on the console)
- Characters, across all campaigns — a player may have four characters in four different packages
- Friends / party status, for connecting with other players
- Global settings (not campaign-specific — audio device, account, etc.)
- **A path to content beyond what's installed** — moved here from the package main menu at `PT-1101`, matching where NWN's own equivalent actually sits: at the level of picking which package, not inside one already chosen. Not designed yet.

**Full layout locked at `PT-1146`, confirmed through real mockups rather than the bullet list above alone.** Three small icons sit in the corner, deliberately kept light rather than competing for the main space: Characters, Profile, and Settings — Characters lives here specifically because it's a utility a player reaches for occasionally, jumping to a specific character across campaigns, not a first-priority choice the way Friends and the Library are.

The **friends strip** sits prominently below that, avatars with online status shown by dimming rather than a separate label, plus an add affordance matching the same visual language as adding a new package. This strip is itself the entry point into a fuller **Friends / Connect screen**, which carries two tabs rather than needing its own top-level icon: **Friends**, and **Public Games** — the public browser this whole system needed once `PT-1144` made hosting and public listing one toggle rather than two systems. Real detail drawn from NWN's own confirmed browser rather than invented: a listed game shows the package name, host, and seat count, stays visible even when full rather than disappearing, and can be password-locked while still publicly listed — a real combination the source supported that's worth keeping rather than simplifying away.

The **library** sits below the friends strip as its own scrollable row, packages as tiles with a matching add-affordance for reaching more content, per the path already relocated here at `PT-1101`.

**⚠ WHAT A TILE SHOWS, added at `PT-1358`** — the gap being that **`§0` specified the fields for the Public Games list and not for the library**, which is the app's main content. **Name · summary · authors · version**, with a **cover image if the package supplies one**. Fields defined at `PACKAGE-FORMAT-01 §4.1`.

**⚠ Sort order is the app's, not the package's.** The manifest carries nothing temporal — an author writing a date is **writing a claim, not a fact** — so the app sorts by filesystem time or by name. **Which tile comes first is not a fact about the package.**

**Package Main Menu — locked at `PT-1101`** (`TRACE-09`), after picking a package, before or between sessions inside it. Two assumptions here turned out wrong and one turned out right by accident, worth recording plainly:

- **Confirmed against source, all three games:** KOTOR 1 is New Game, Load Game, Movies, Options, Exit — nothing more, nothing hidden the manual wouldn't mention except a developer module-jump list and a warp button, both hidden by convention rather than removed. KOTOR 2 reuses that same panel wholesale. NWN's outer menu is New Game, Load, Multiplayer, Movies, Options, Exit.
- **Continue doesn't exist anywhere**, checked across all three games' full panel sets. Not an oversight we're fixing — NWN's own "you picked a package, now what" screen would have been the natural place for it and doesn't have one either. We're adding it anyway, and it's ours, not a borrowing.
- **Music was a wrong guess that turned out half right.** No jukebox in KOTOR 1 or NWN. KOTOR 2 has a genuinely complete one — track list, play/stop/next/loop, its own volume slider, and tracks that unlock as the player progresses rather than all being available from the start. Worth keeping the unlock pattern specifically, not just the player. One methods note attached to this finding: reading K2's base menu panel alone says no music button exists — it only appears in the resolution-specific panels actually used on screen. The file that looks authoritative isn't always the one running.
- **"Other content" — browsing beyond installed packages — moved out of this screen.** NWN's equivalent button lives at the level of picking *which* package, not on the menu of one already chosen. That's Console Home's job; noted there instead, not here.

Final structure, in order: **Continue** (highlighted by default, not New Game — the thing a returning player actually wants), New Game, Load Game, Movies, Music, Options, **Exit to Library** (not "Exit" or "Quit" — leaving this screen returns to Console Home, not the desktop, and the label should say so).

Layout, confirmed against an actual K2 screenshot rather than assumed: a centered vertical stack of bordered buttons, not a left-aligned list — package title and status sit in the top-left corner, separate from the button stack — and background art fills the entire screen behind everything, not a side panel. Real artwork is a separate question entirely; nothing here reproduces KOTOR's own art, which is copyrighted, and any placeholder in a mockup is marked as exactly that.

**Full visual specification checked against K2 directly (`TRACE-24`), with two deliberate departures — locked at `PT-1116`.** The obvious source file for K2's menu understates it the same way `TRACE-09` found for the music button, worse this time: it's not just missing an item, it's authored in an entirely different coordinate space than what actually renders. K2's real buttons are pure outlines with no fill at all — the game's own 3D character view shows straight through the middle of every one, since that empty space is deliberately reserved for a live character render standing behind the menu. Two departures from that, both deliberate: **our buttons stay filled, not outlined**, since every campaign package can supply its own background art we don't control the way K2 controlled its own character model, and a filled button stays legible regardless of what happens to be behind it — copying pure outlines would mean copying a solution to a problem specific to K2's fixed art, not one we share. **Our layout stays centered, not right-aligned with a reserved gap**, for the same reason — that empty space only makes sense once there's something specific meant to occupy it, and live character art on this screen is a decision explicitly deferred, not one we've made.

Everything else matches directly: button text centered on both axes, confirmed against K2's own alignment code rather than assumed — corrected into our own mockups after being caught sitting left-aligned. No dividing elements anywhere on the screen, buttons floating directly over the background with nothing separating them. Motion, source-accurate part: `TRACE-24` checked every main-menu panel specifically and confirmed zero pulsing anywhere in K2's actual screen, hover a pure border color shift with no fill or press treatment, matching the format's total absence of a pressed state.

**One deliberate departure on top of that, locked at `PT-1118`: Continue pulses.** Nothing else does. Applies `PT-1113`'s existing rule exactly — pulse means waiting for input, hovering cancels it instantly — rather than inventing new motion language, and keeps that rule meaningful by not diluting it across all six buttons at once. Stated plainly as ours, not sourced: `TRACE-24` found the real K2 main menu is fully static, so this is a genuine choice, not a restoration.

**A persistent focus ring, real and genuinely sourced this time — locked at `PT-1119`.** `TRACE-25` corrected `TRACE-24`'s original negative under a harder look: there's no separate "remembers what I clicked" state anywhere in the source, but one button is always focused, defaulting to New Game the moment the screen opens and never persisted to disk. What made this look like memory is a specific, deliberate choice worth keeping exactly: **focus uses the identical color hover uses**, bone border, no separate treatment. Confirmed against a side-by-side comparison before locking — a version giving focus its own distinct marker was shown and rejected in favor of matching K2's ambiguity exactly, since that shared color is precisely what produced the effect that prompted this whole check in the first place. Navigation order, for whenever keyboard or gamepad input matters: New Game through Exit to Library in sequence, wrapping at both ends, with no left/right movement authored.

**Colors, stated explicitly rather than only cross-referenced:** button text `#1AB28C`, resting border `#0D5945`, hover border `#CCCCB2` — the exact same three values as the established K2 theme (`§0b`), confirmed by `TRACE-24` as an identical match with no screen-specific variation. Nothing new to source for this screen; it uses the house palette already in place.

One technical ceiling worth naming rather than glossing over: K2's actual typeface isn't a font in the normal sense at all — it's a fixed, pre-built image containing every character already drawn, with letter spacing coming from that image rather than any adjustable setting. Genuinely exact text reproduction would mean building our own equivalent asset, not just picking a visually similar web font; a close font is the practical ceiling without that additional work.

The label reading "Quit" in the source, rather than "Exit," confirms rather than overturns our own choice: we deliberately use "Exit to Library" instead, since leaving this screen returns to Console Home rather than closing the app the way K2's Quit does.

**Party rail, added at `PT-1102`, position corrected at `PT-1111`.** The same roster panel from the multiplayer lobby (`§6`), docked to the **left** edge of this screen — corrected from an earlier right-edge placement that drifted away from our own `UI-REFERENCE-ABACUS-DEMO-01` finding that Del Arroz's app keeps its persistent character card on the left, matching Baldur's Gate 3's own portrait placement too. A player sees their party forming the moment they land on the menu, before clicking anything. Collapsible: a thin tab sits permanently at the panel's edge and stays visible in both states, so pulling the rail back out is never more than one click even when it's fully collapsed. Same rules govern it as the full lobby screen — filled seats and open invite slots, a live subtitle reflecting whether the current headcount is solo or multiplayer, and Play never blocked by an empty seat.

**A real requirement surfaced here, not designed yet:** friends, invites, and in-game messaging all need a genuine account system underneath them, not just a locally-typed display name. Infrastructure, not a screen — flagged so it isn't lost, picked up separately from the screen-by-screen pass.

---

## 0c · ⚠ Inspecting a check — an option, not the default, `PT-1326`

**`PT-1307` cut every number from a dialogue option: `[Persuade]`, and you roll.** That stands as the **default**.

**⚠ This adds an opt-in under `Rolls & Feedback`, default OFF.** With it on, tapping the **skill tag** expands the option row in place:

```
[Persuade] You need us more than we need you.
  ─────────────────────────────────
  needs            14
  your Persuade    +6   rank 4 · aptitude 2
  you roll d20 and add 6
```

**Tapping the tag inspects. Tapping the LINE still says it.** So a player with the option off never sees a number and never pays a click.

### ⚠ Two moments, and they must never share a format

**This corrects a real error in the drafts.** `16 vs 14` was shown at both moments, meaning two different things.

| | What exists | Shown as |
|---|---|---|
| **Before the pick** | **no roll has happened** — only what it needs and what you add | `needs 14` · `your Persuade +6` |
| **After the pick** | **the roll exists** | `rolled 17 — d20 11 + rank 4 + aptitude 2 · needed 14` |

**⚠ There is no total before you commit**, and showing one implies you can see whether you will succeed. **You cannot — that is the whole reason `PT-1307` cut the numbers.**

### Why in-place rather than a panel

**The row grows.** Nothing appears over anything, nothing must be dismissed, and **the working sits where the line is.** The earlier panel design put a component between the player and the choice, costing two extra clicks for everyone.

**And the result renders inline under the player's own line in the transcript**, indented against a rule — so it persists with the conversation rather than vanishing with an overlay.

---

## 0b. ⚠ THE PRESENTATION LAYER — a character never moves, `PT-1319`

**Stated as one ruling because it was already decided in pieces, and scattered decisions are how `PT-1292`'s stale count and `TRACE-86`'s `.mod` retraction happened.**

> **A character on screen is a portrait. Nothing animates. There is no model.**

**The three decisions that already made this true:**

- **`PT-1137`** — a grid token is **the same portrait as the sidebar entry**, so a token on the board and its row in the rail are visibly one character rather than two representations.
- **`PT-1179`/`PT-1180`/`PT-1182`** — the Species screen uses a **holotable figure**, chosen over *"a portrait or a reused 3D viewport"*, explicitly because **it sidesteps the model-asset dependency.**
- **`PT-1113`** — menu transitions are **hard cuts**, and the pulse rule is the only motion in the house style.

### ⚠ What this closes

**`UI-ASSETS-01` flags the character model as the project's largest asset commitment. It is not needed and should be struck from the plan** — no rigged model per species, no equipment rendering on a body, no animation set.

**And `TRACE-88`'s deferred questions never arise.** The **16-viseme LIP timeline** and the **three competing animation numbering schemes** are model-layer concerns. **Nothing here needs them.**

**`EMBODIMENT-01`'s `appearance` field stands and its meaning narrows:** a handle the presentation layer resolves — **to a portrait, and to nothing else for now.**

### ⚠ What it costs, stated rather than hidden

**Equipment does not show on a character's PORTRAIT.** Change armour and the portrait does not change. `EMBODIMENT-01` lists `overlay` as derived, and **derived-to-nothing is the current answer for rendering.**

**⚠ THIS IS A RENDERING LIMIT, NOT A FICTIONAL ONE — `PT-1320`.** What someone wears **is a fact about them**, held in `EMBODIMENT-01`'s eleven slots, and it stays reachable:

> **A player asks what someone is wearing. That is an `Awareness` check against the equipment slots, and it answers.**

**The data exists whether or not it is drawn.** So *"is he armed?"*, *"is that Echani work?"*, *"what's under the robe?"* are all askable — and they route through the character brain like any other fact, with the same locality and tier rules.

**⚠ And the check is the point.** A trained eye sees the maker's mark; an untrained one sees a sword. **A rendered figure would have told everyone the same thing at a glance** — so the portrait limit converts a free visual into an earned one, which is arguably better for a tabletop system than the render would have been.

**⚠ That is a real loss and it is accepted**, because the alternative is the largest asset commitment in the project **for a game whose play surface is a 2D grid.**

**⚠ And it is reversible in one direction only.** A portrait system can gain richer depiction later. **A design that assumed animation cannot cheaply lose it** — so the conservative choice is the recoverable one.

---

## 0a. Motion and animation, locked at `PT-1113`

Applies across every screen already locked, not just one — checked with `TRACE-23`, since no prior pass had specifically looked for animation and one earlier reading (`PULSING` as mostly unused) turned out to be true of the specific screens read but not of the game as a whole.

**Menu-level transitions are hard cuts, not fades.** K2's own panel format has no field capable of describing a fade, slide, or any timed transition at all — screens are added and removed instantly, and the *transition* is entirely a dedicated pair of sounds, the two longest in the whole audio bank, playing on open and close. Match this exactly for the package main menu and anywhere else a full-screen panel swaps for another: instant cut, paired with the open/close sound, no fade added. Adding one would be a deviation from the source, not a restoration of something it always had.

**The pulse rule, adopted as a house-wide principle, not a menu-specific detail.** Where K2 does animate, it follows one clean, consistent rule: a pulsing element means "this is waiting for your input," and hovering over it instantly cancels the pulse — every pulsing element on a screen breathes in sync, on one shared clock, never out of phase with anything else. Applied to us: the party rail's open invite slots (`PT-1102`) and any idle, unfilled action-economy budget slot (`PT-1105`) should pulse using this exact rule — cheap to build, directly borrowed rather than invented, and it gives an unfilled state a way to say "you haven't touched this yet" without adding a new visual language for it.

**One deliberate addition beyond the source: a real press state.** K2 has no pressed/down visual at all — clicking something just keeps showing whatever hover look it already had, plus a click sound, so the entire feeling of a press lives in audio alone. A muted player gets less feedback than everyone else, which is a real gap rather than a style choice. Worth adding a small, genuine press state as a marked improvement, not something pretended to be faithful reproduction.

**The main menu's drifting mist, confirmed original rather than a remaster addition, and confirming where motion actually lives.** `TRACE-25` traced it fully: not a particle system, not an animated texture — hand-keyframed geometry, textured planes drifting on a loop, built directly into the same 3D model rendered behind the menu, present in both games' original files independently. This is the answer to something already established here: the UI panel format itself has exactly one animation primitive and the main menu uses none of it — all motion on that screen, then and now, lives in the background scene layer, never in a button or a panel. Any future animated background follows this same model: scene-layer motion, UI layer stays exactly as static as `PT-1113` already locked.

**Confirmed already correct, no changes needed:** character creation, dialogue, journal, message log, and the target sidebar all have zero authored motion in the source, and nothing about how we've already built any of them needs correcting as a result.

---

## 0b. Color theme system, locked at `PT-1117`

Never previously written into this document despite being fully worked out — `TRACE-18` through `TRACE-20` and an extended conversation produced two complete themes and a working interactive demonstration, but no ruling number and no section here. Found and fixed while adding an unrelated color cross-reference to the main menu.

**Colors are named roles, not values hardcoded per screen.** Background, body/accent text, heading/emphasis, border, dimmed, and alert — every screen reads from these roles, and a theme is just a set of values plugged into them. This is the architecture, independent of which theme is active.

**Confirmed at the implementation level, locked at `PT-1147`: this architecture isn't just how we're choosing to build it — it's how the source actually works underneath.** `specs/SPEC-01` decoded every border and fill primitive surveyed so far and found they're all flat greyscale alpha masks, tinted at runtime — the same six tiny shapes reused and retinted across every screen this whole session has touched, main menu to journal to target plate. Confirms directly that the entire visual chrome of this interface needs no original art at all; it can be generated from geometry alone. **One deliberate departure from source, worth stating plainly:** the terminal font's outline color is baked directly into the source's own glyph sheet, which breaks tintability — the one rule this whole system depends on. Ours authors the font white-on-transparent instead, with the outline rendered as a separate pass, keeping it tintable like every other primitive rather than locked to one color the way the source shipped it.

**A new `specs/` folder, distinct from `research/`, established at `PT-1147`.** Research traces are evidence about what the source actually does. Specs are build documents meant to be handed directly to an artist or a builder — a genuinely different kind of artifact, worth keeping structurally separate going forward rather than mixed with the trace files.

**Two starter themes, checked directly against each game rather than invented (`TRACE-18`):**

    ⚠ K2 (default)  background black · accent `#1AB28C` · heading/hilight
                     `#CCCCB2` bone · border `#0D5945` · dimmed `#B2B299`
    ⚠ K1 (alternate) background black · accent `#00A8FA` cyan · heading
                     white · border white (K1 never had its own border
                     color — honest fill, not an invented shade) ·
                     dimmed: none (K1 never had this tier either)

The two themes aren't the same shape. K1 has no border color and no dimmed tier at all — filling those gaps with white and "not present" respectively is the honest answer, not inventing values the source never had.

**Hilight is the one invariant, kept as a rule rather than a value.** Whichever theme is active, one color always means "you are touching this," and it never changes job — confirmed as the pattern holding across K2's house theme and all three of its contextual sub-themes (crafting, commerce, terminals).

**Alert is red, universal across both themes, not theme-specific.** The one color both source games independently agree on — used for nothing else in either game's entire interface. Both starter themes share this value rather than each defining their own.

**First real extension beyond source, locked at `PT-1177`:** the camp-vote decline state is the first thing besides Alert itself ever drawn in this color, in either game's own interface or ours. Deliberate, not a silent violation of "used for nothing else" — a declined vote is treated as a legitimate use of Alert's role, not a new color assignment.

**Notification is its own role, and a theme may either separate it from the base palette or fold it in — both shipped, neither is more correct.** K1 breaks from its own palette for notifications (green for journal updates, violet for items and XP); K2 folds everything into its own house teal. A theme declares which way it goes rather than the system forcing one.

**Switchable in settings, K2 as default.** Confirmed working as an actual live toggle before locking — the same screen, same layout, same interaction logic, only the values plugged into each role change. K1 as the alternate is a genuine second theme built to match the source, not a cosmetic recolor of K2's.

**A third option, locked at `PT-1140`: fully custom, via a color wheel.** Beyond K1 and K2 as fixed presets, a player can define their own values directly rather than choosing between only two authored themes. Since colors are already architected as named roles rather than hardcoded per screen (`§0b`), this costs nothing structurally — a custom theme is just a third set of values plugged into the same roles, no new system required.

---

## 0c. K2 as the default tie-breaker, locked at `PT-1151`

**Made explicit rather than left as an unstated habit.** Checked against everything already decided before locking, since a blanket rule risked quietly overriding real, reasoned exceptions already made — the terminal backdrop deliberately keeps K1's tonal warmth (`PT-1150`), and the button styling departed from both games entirely (`PT-1116`). Neither of those is overturned by this.

**The actual rule: when K1 and K2 differ and nothing else specifically argues otherwise, K2 wins by default.** This isn't new so much as it's naming a pattern already followed throughout this whole thread without ever being written down — K2 as the default color theme, K2's portrait wing proportions over K1's thin strips, K2's chevron buff icon over K1's arrow, K2's inventory filter bar called out directly as the clearer design. A specific, reasoned exception still wins when one genuinely applies; this only settles the default when there isn't one.

---

## 1. New Game — character creation

**Consumable resource sharing, locked at `PT-1148`, closing the terminal pricing bug found while researching Computer Use and Repair.** The source's own bug — pricing a terminal action off a fixed "party leader" while spending from whichever character is currently controlled — is fixed cleanly for single-player by pricing and spending against whoever's actually using the screen, never ambiguous since only one character is ever controlled at a time. Multiplayer genuinely needed its own decision, since several real players can be controlling different characters simultaneously, so **this becomes a real setting chosen before a campaign begins**, not something we pick for every group: fully shared party inventory (the default), fully separate per-player ownership, or a middle path where only specific consumables like spikes and repair parts are called out as shared while everything else stays personal. Separate and middle-path modes lean on the Trade/give item verb already built into the exploration catalog at `PT-1123` — no new mechanic required to move a shared-mode item between players. Single-player never sees this choice at all, since there's only one real owner of everything regardless of mode.

**This is the first confirmed occupant of a broader "pregame settings" category, flagged at `PT-1148` and deliberately not fully scoped yet.** The owner's own framing: some settings will end up universal to single-player and multiplayer alike, others will only make sense for one or the other, and which is which isn't fully known yet — this gets scoped out incrementally as more of these surface naturally, the same way the actual Settings screen (`PT-1140`) is growing its own occupant list rather than being designed all at once from a guess.

**Structure, confirmed against source at `PT-1100`** (`TRACE-08`), correcting an earlier assumption: it is not an NWN-style wizard with Back/Next. NWN's own chargen has no Back or Next anywhere in it — it's a hub screen with eight category buttons, and ordering is enforced by disabling buttons rather than by navigation: finishing one step unlocks the next and re-locks everything after it. KOTOR's creation screen isn't tabs either — it's a numbered sidebar next to a full-size content panel, structurally a hub in its own visual language, not far from NWN's shape at all.

The synthesis, drawn from what both games actually do rather than from memory: **KOTOR's numbered sidebar as the visual and structural shape** (it's already a hub), **NWN's progressive-unlock discipline for ordering** (a step stays locked until the one before it is confirmed, and confirming an earlier step re-locks everything after it — matching our own strict dependency order better than free navigation would), **hiding reserved for genuinely inapplicable steps** rather than used for ordering (Force Powers, Lifestyle and Upbringing for a droid), and **KOTOR's own live before/after preview** — its creation screen already showed old-value-arrow-new-value for every save and every attribute, reacting live as choices were made, in 2003 — as the model anywhere a choice changes a derived number.

Order: ours, already ruled — `CHARACTER-CREATION-01`.

The order is fixed and dependency-driven, not arbitrary:

1. **Species** — fixes origin world, species skill bonuses, age bands, cardinality band
2. **Homeworld** — constrained by the cardinality band (a droid takes a **model** instead, per `PT-958`, and derives its manufacturer from that)
3. **Gender** — narrative (for a droid, this is its voice)
4. **Class** — grants the class skill list. Moved ahead of Ability Scores at `PT-1098` so the class's priority abilities can be shown on screen before the player assigns scores, not after.
5. **Ability Scores**
6. **Skill Points** — spent against a cap that already includes steps 1–2
7. **Feats**
8. **Force Powers** — conditional, `PT-1099`. Exists only for a class that grants Force Powers. For a class that does not, this step does not render — not shown, not greyed out.
9. **Profession**
10. **Lifestyle** (droids skip this by owner ruling)
11. **Upbringing** — flavor only, no mechanical grant, organic-only
12. **Equipment**
13. **Name, Appearance, Backstory** — the text layer, last

Steps 9–11 sit after Feats and Force Powers for a specific reason: none of them feed the skill-point cap, so they can't invalidate an earlier choice. That maps directly onto the NWN-style lock behavior now — a player can't back up past step 6 and have step 9–11 choices silently break, because step 6 stays locked until steps 1–5 are confirmed in the first place.

First screen of the flow, matching Del Arroz's app and KOTOR's own party system: **use an existing character, or create new.** An existing character keeps XP, level, and story — no re-rolling, matching the language his app already uses for exactly this.

### The governing rule: a locked-out option does not appear

Not greyed out, not skipped with a note — simply not there. This project was already doing this three times before it got named: Gender becomes Voice for a droid, droids skip Lifestyle entirely, droids skip Upbringing entirely because it's organic-only. Force Powers not rendering for a non-Force class is the fourth instance, and the one that finally got the rule stated out loud.

The precedent is KOTOR itself, and `TRACE-08` confirms it generalizes rather than being a one-off. Across the source, hiding outnumbers disabling by more than 50 to 1 — it's the house style, not an exception for one screen. And it isn't limited to menus: the in-game overlay hides the Force bar itself, per party slot, for any character who isn't Force-sensitive. Not an empty bar — no bar. NWN does the opposite on purpose, greying out unavailable categories so its hub still shows the shape of what remains — the two conventions are saying different things (disable means "not yet," hide means "not applicable"), and ours is squarely the second one: **if a prior choice makes a later option meaningless, that option does not render, anywhere in the UI.**

---

## 2. In-session dashboard (the persistent HUD)

A player card, always visible, similar to Del Arroz's sidebar — but ours needs an extra bar his can't have.

- **Vitality** — one bar, standard
- **Force** — not one bar. `PT-1059` gives the Force pool three values: current, a degrading working ceiling, and true max. The bar needs to show current *and* how far the ceiling has slipped — a Force user who's been casting all day should visibly look different from one who slept. A flat single bar hides the exact mechanic that makes several of our own rulings (`Moderation`'s `+1` ladder, Soresu's DR steps) mean anything on screen.

  **Decided:** the bar's frame stays a fixed length representing the true maximum. The degraded portion (true max minus working ceiling) shows as a dimmed or hatched zone within that frame. Current Force fills the bright portion up to the ceiling. The true max never disappears from view — the player always sees both what they have right now and what they're missing.

  Researched against Dark Souls 2's hollowing mechanic first, since the shapes are close: death there reduces max HP by 5% per hit, capping at a 50% loss, and only an active choice (using a Human Effigy) restores it — sleep or ordinary rest does nothing. `FORCE-POOL-01-v3` already has the same shape independently: the floor is half the true maximum, and only meditation restores the ceiling (one hour for 75%, eight hours for full) — sleep refills current but leaves the ceiling degraded. Dark Souls 2 draws this by shrinking the bar's visible length, hiding the true max entirely once degraded. We're not doing that — it works against `RULES-01 §2.1`'s "show the dice" principle, where nothing about a resolution is ever hidden by default. Keeping the true max visible is the better fit for a game built around a party managing a shared resource across a whole session, rather than one built around dying and restarting.

  And `TRACE-08` confirms the *absence* half of this independently: KOTOR's own in-game overlay hides the Force bar entirely, per party slot, for any character who isn't Force-sensitive — not an empty bar, no bar at all. Direct precedent for the governing rule in `§1` applied to the HUD itself.
- ~~Party connection / other players — open question~~ **Closed at `PT-1124`, see `§3`: the combat sidebar now runs during exploration too, showing party members at all times.**

Clicking into the player card opens the full character screen, KOTOR-style: Inventory, Equipment, Character Sheet, Skills/Feats/Powers, Journal, Message Log. Structurally these map cleanly onto things we've already built — the sheet is `RULES-01 §1.2`'s derived values, the journal is the quest ledger, the message log is dialogue history.

**Equipment, Inventory, Character Sheet, the alignment meter, and Skills/Feats/Powers, locked at `PT-1154`, closing a real gap where `TRACE-42` was researched but never actually written in.** All checked against real source rather than assumed.

**Equipment, full lattice locked at `PT-1156`, correcting an earlier "frameless" claim.** `TRACE-46` found K2's slots aren't frameless at all — each is a Button drawn from the exact same tinted nine-slice primitives `SPEC-01` already specifies, house chrome at rest and bone on hover, just with no fill inside, which is what made it read as frameless in an earlier pass. Corrected in place. Both frame treatments adopted together rather than picking one: **K2's tinted-primitive border**, genuinely free since it's already-specified shared assets, plus **K1's placeholder silhouette** sitting inside an empty slot, since an outlined box alone tells a first-time player a slot exists but never what belongs in it — K2 lost that legibility, K1 had it, we keep both. **Confirmed at `PT-1157`: any mockup currently using the real game's own slot-type icons is doing so purely as a temporary testing stand-in, the same treatment already applied to portraits, tiles, and backdrops throughout this project.** Real, non-copyrighted icon art gets built or licensed properly before anything ships; nothing here assumes the source's actual assets are the final answer.

**Upgrading, locked at `PT-1171`, split from Crafting into its own system.** `TRACE-58` found `upgrade`/`upgradesel`/`upgradeitems` and the new `chemical`/`component` crafting screens sitting together in the source as one loosely related family, but checking our own rules found only `CRAFTING-01` actually has a real process ruling — `UPGRADES-01` is genuinely just the item catalog, silent on where or when an upgrade actually happens. **Resolved as a new ruling, not something already decided:** Upgrading is instant, triggered by interacting directly with an item already owned, no rest requirement and no location object involved — matching how it already felt in the source games, and preserving a real, felt difference from Crafting rather than the two systems quietly merging back into one under different names. Crafting makes something new and costs a real rest period per `CRAFTING-01`; Upgrading changes something already held and costs nothing but the moment itself, closer in spirit to swapping equipped gear than to producing an item from raw components.

**Crafting itself is ONE screen, not two, locked at `PT-1195`.** The source split Lab Station from Workbench because it had two pieces of furniture on its maps; `CRAFTING-01` had already ruled that away — *"the gate is what the thing IS, not what bench you stood at"* — before either screen was designed. Built to `component_p.gui`'s real two-column proportions: item list occupying the left 40% at full height, with the skill line, description and three paired readout rows stacked in the right column. The merged category row spans both benches — Armor, Ranged, Melee, Saber, Medical, Misc. **Break down is promoted to a real visible mode**, which `TRACE-64` showed it always was: the create and break rows share four of five x positions and swap in place rather than stacking, so surfacing the mode restores authored intent rather than adding a feature. **One row is genuinely ours rather than the source's:** Downtime, since a crafting session costs a full downtime period per `PT-1172` and the source had no such cost to display. **Palette stays cyan**, per `TRACE-58`'s exception rather than the K2-default rule — the whole crafting and upgrade family keeps K1's cyan inside K2's own build, confirmed four times now.

Base lattice: a 3×5 grid with genuine empty cells, confirmed unchanged in adjacency across rows one and two between K1 and K2 despite K2 rebuilding everything else on this screen — Implant/Head/Hands, then Left Arm/Body/Right Arm. **Rearranged from there, by owner choice:** primary weapon configuration flanks Belt in its own row, matching K1's original meaning of belt-as-worn-item rather than K2's version, which pulled belt out alone specifically to avoid it blurring into the weapon group — our arrangement keeps that same reasoning while still flanking it, since a single row of three reads clearly either way. **Boots — genuinely new, no source precedent at all** (`ITEMS-08`, `PT-690`: KOTOR's own data has no foot slot whatsoever) — sits alone in its own row directly beneath Belt, grouped with the other worn-on-the-body items rather than wedged into the weapon block. Secondary weapon configuration keeps its own row below that. The configuration switch spans the full width beneath the whole grid, wider than any single column, exactly matching K2's own placement. Confirmed unchanged from the original finding, count corrected at `PT-2503`: twelve slots total including the second weapon pair for our already-locked dual-wield system, and swapping gear has a real commit step, unlike the terminal — click a slot, the list narrows to only what fits, pick, confirm.

**Inventory, full detail locked at `PT-1155`, correcting an earlier mockup's wording and order.** K2's filter bar adopted directly — seven category buttons, folding quest items in as one of them rather than K1's separate dedicated screen for the same content. Already called out as the single clearest improvement either game made anywhere in this research. `TRACE-45` gave the real, exact order and wording rather than the assumed version an earlier mockup used incorrectly: **All, Datapads, Weapons, Armor, Useable, Quests, Misc** — the seven-letter "Useable" spelling specifically, not the more common six-letter form, and the bare plural "Quests," neither "Quest" nor "Quest Items." Worth knowing plainly: Quests was added after the other six were authored as one batch and inserted into the middle of the bar rather than appended, which is the actual mechanism behind K2 folding K1's separate quest screen into this filter at all. Full control set confirmed: a credit balance and Close read from the exact same source text `Store` uses, plus a Use Item button — and confirmed genuinely absent in both games: no weight or encumbrance, no sort, no search, no stack-splitting, no capacity or count display. The category filter was the screen's only organizing tool in the source. The same missing-active-state defect already fixed for Store applies here too, worse in consequence since seven ambiguous filters is a harder guess than four on a screen a player returns to constantly — same fix, a real visible active state from the `SPEC-01` primitives. **One deliberate addition beyond source:** a real sort control, since neither game ever built one and we have no weight cap of our own to help constrain a growing, unordered list the way a limit implicitly would.

**Character Sheet.** Both games pair every attribute's score and modifier as separate adjacent fields, never one formatted string — adopted directly, consistent with every other readout in this project. **One real finding kept as an open question, not asserted as fact:** K1 places ten small markers in an arc beside the character view that plausibly mark alignment steps, but neither the panel data nor the reimplementation actually confirms what they do — not adopted, since we have nothing to build from beyond a guess.

**The right column, locked at `PT-1163`, corrected and finalized at `PT-1164`.** `TRACE-56` overturned the original framing here — the twelve rows are not one continuous list, and reproducing them that way would have preserved a real flaw rather than fixing it. Vitality and Force are genuine resource pools, showing current over maximum, structurally different from Defense, Fortitude, Reflex, and Will, which are flat single-number ratings — K2 merged all six into one undifferentiated block, burying that distinction; K1 happened to keep them six rows apart, better by accident. **Adopted deliberately, not accidentally:** three real groups in order — pools first, the six ability scores in the middle, the four ratings last. **Sizing corrected rather than copied:** K2's own field widths were inconsistent authoring drift, not deliberate design — Defense sat 34 pixels wider than the other three ratings for no content reason. Fixed: one consistent field geometry per content format, pools sized once from their real maximum range rather than widened piecemeal the way K2's own were. **One deliberate addition beyond either source:** an icon on every ability score and every rating row, since neither game did this for these specific rows — first-pass placeholder icons, easy to swap once real art is chosen. The experience block stays exactly as already confirmed, a matched pair directly beneath, unaffected by this reorganization.

**The full structure, resolved and locked at `PT-1166`, closing what was left open above.** The alignment cluster and both level-up buttons — never actually positioned relative to the screen at all in the source, only relative to the 3D model inside the viewport (`TRACE-55`) — get a real, deliberate new home rather than an afterthought: the alignment slider becomes its own persistent left wing, running the full height of the screen, visible no matter which page is active. Portrait, identity, and both level-up buttons sit together in a header to its right, also persistent across every page. This is genuinely closer to NWN's real contribution than K2's — NWN is the one that actually has a persistent header sitting above switchable pages; K2 never had tabs to persist across at all, having built everything onto one single screen instead. A real alternative, kept everything scoped to one page rather than a persistent header, was built and shown before this one was chosen — closer to K2's own single-screen instinct, but rejected in favor of the version below.

**Skills, Feats, and Powers are not pages here at all — corrected from an earlier draft that mistakenly folded them in.** They remain their own separate screen, exactly as already locked at `PT-1154`; nothing about that changes.

**Three pages, in this order: Stats, Character Info, Backstory.** Stats is the default, carrying the right column already locked at `PT-1164`. **Character Info, locked at `PT-1166`, sourced directly from `CHARACTER-CREATION-01`'s real steps rather than invented:** Species, Gender, Homeworld, Profession, Lifestyle, and Upbringing — Upbringing specifically fits here since it's already established as pure flavor with no mechanical grant at all, the same character. **Backstory is its own dedicated third page, not folded into Character Info** — a genuinely large, scrollable text area, since a backstory can run long and deserves real room rather than being squeezed beside shorter fields.

**Player-only, with Known Languages resolved as the one field both share.** The Character Info and Backstory pages exist for player characters only. Companions get Stats alone — which is exactly where Known Languages now lives too, per `PT-1169`, so nothing about a companion's page is actually missing anything it needs.

**Known Languages, resolved and closed at `PT-1169`.** Confirmed real and mechanically grounded — `SPECIES-MASTER §3` gives every species its actual known languages directly, not something chosen separately during character creation. Since it's species-derived, every character has it, player or companion alike, which settles the placement question cleanly: **moved off Character Info entirely, onto Stats**, the one page both types of character genuinely have. No special-cased exception required — one simple rule covers both cases, since companions already don't get Character Info or Backstory at all.

**Alignment slider, fully corrected and locked at `PT-1162`.** `TRACE-54` overturned a standing error repeated across two earlier passes: this is not the Force bar's texture reused — it's genuinely bespoke art referenced nowhere else in the game, on a completely different asset with a different color model. Corrected in place. The real design: a true two-pole color gradient track, blue through purple to red, always fully drawn regardless of value — nothing about the track itself changes, only the thumb moves. The thumb is a bracket, not a pointer or filled block — two lines straddling the current value rather than indicating it with an arrow. **One deliberate addition beyond source:** a center tick mark, since K2's own version has no way to show true neutral at all — a character dead-center and one a step off a pole differ only by a few pixels of bracket on an unmarked gradient, confirmed as the control's real, genuine weakness rather than a stylistic choice worth preserving. **Placeholder status confirmed per `PT-1157`:** real game assets are fine to build and test against now, with proper original or licensed art replacing them before anything ships — same standing rule as everywhere else in this project, not a new exception for this one element.

**The gradient's middle, further corrected and finalized at `PT-1165`.** `TRACE-57` resolved a direct conflict between the owner's memory (a grey center) and the earlier reading (a smooth blue-to-purple-to-red blend) — both were partly right. The center is measurably a genuine desaturated purple, not true grey, but simultaneous contrast against two vivid, saturated poles pushes it toward reading as neutral, which is exactly what the owner was describing. The real structural correction: it isn't a smooth blend at all — a real, roughly eight-point-wide plateau sits in the middle where the color barely changes, dropping steeply into it from both sides. **Adopted deliberately, tuned toward grey beyond the raw measurement** — the plateau color pulled further toward neutral than the source's own numbers, since that's the actual feel being aimed for, while staying rooted in the confirmed purple rather than inventing a value with no basis. **The center tick repositioned with precision as a direct consequence:** `TRACE-57` found the gradient's true red-blue crossover sits almost exactly on the authored neutral value, but the plateau completely buries it — roughly eight points around center all look identical. The tick marks that exact calibrated point specifically, not just "the visual middle," recovering the one precise thing the plateau otherwise hides. **A methodology note worth carrying forward:** this exact correction happened because an earlier pass sampled the gradient too coarsely to catch something this narrow — worth remembering that any other trace in this project claiming a smooth gradient or profile is only as reliable as how finely it was actually sampled.

**Final exact values, locked at `PT-1167` after live iteration against the mockup.** Plateau spans the confirmed real width, 42.6% to 50.8% of the scale, not a rounded approximation. Color settled at `#7c7986` through the flat zone, `#6c6884` and `#806e76` easing in and out on either side — deliberately pulled toward neutral from the raw measured `#624968`, tested directly against a too-white version and rejected before landing here. This is the one true color for this element; nothing further to adjust.

**Full assembly confirmed at `PT-1168`.** Every piece of the Character Sheet locked across `PT-1162` through `PT-1167` was rendered together in one complete mockup — the left-wing slider with its final colors, the persistent header, all three pages with Stats open by default — and confirmed working as one coherent whole rather than staying a set of separately-verified pieces. No new content here, just the integration itself checked and signed off.

**The companion rendering confirmed at `PT-1170`, completing the pair.** Same header, same left-wing slider, but only Stats exists — no Character Info, no Backstory tab at all — with the full six-ability, four-rating stat block rendered exactly as it appears for a player, and Known Languages sitting as the final row per `PT-1169`. Confirmed as a real, complete rendering rather than left as an implication of the rule.

**Skills, Feats, and Powers.** Structurally identical in both games, so no K1/K2 choice to make: one screen, three tabs, a single three-row stat block whose labels change per tab rather than three separate layouts. View-only — actually acquiring a skill, feat, or power happens on the separate level-up screens, not here.

**Portrait click behavior, locked at `PT-1134`, applied uniformly to the player and every party member — no special case for "yours."** `TRACE-34` found the source's "switches which character you're controlling" behavior doesn't apply to *combat* — corrected at `PT-1142`, since the original wording claimed this too broadly. It exists specifically to solve a real-time problem — handing the mouse between characters while everyone else acts simultaneously — that turn-based combat never creates; whoever's turn it is already has the player's attention, no handoff needed. What we adopt for that context: clicking a portrait opens that specific character's own screen — Equipment by default, or Character Sheet specifically if that character has a level-up pending. This was the source's own reconstructed (not confirmed) guess for the player's portrait specifically; we extend it deliberately to be the universal answer for every portrait, in this context, rather than leaving the player's own case as a special, undefined one.

**Exploration is genuinely different, confirmed real rather than assumed — locked at `PT-1142`.** `TRACE-38` confirmed the exploration HUD's portrait cluster is a separate control from the menu-screen one, live only during exploration, and control-switching there is real and deliberate — K1's own companions ask to be switched to, mid-adventure, specifically so their skill can be used on something in the world. Adopted directly, and it resolves cleanly against the screen-opening rule above rather than competing with it: **tapping a companion who isn't currently active switches control to them; tapping the character who's already active opens their screen instead.** This isn't two separate rules bolted together — `TRACE-38` found the currently-active portrait's own button can't switch control, since you're already that character, which is exactly why that tap is free to mean "open my screen" instead. Practically: switching to a companion and then opening their screen is two taps on the same portrait, one to activate them, one more now that they're active — never ambiguous, since which behavior applies is just a question of whether that portrait is already the active one.

**Modal targeting, extending `PT-1110`'s existing enemy-click behavior to allies too.** Outside of active targeting, a portrait click does the above. The instant an item or power that needs a target is active, that same click instead applies it directly to whoever was clicked — ally or enemy, same mechanism already built, now covering both. Confirmed real in the source rather than assumed, and genuinely free to add: no new control, just a second meaning for the click that already exists.

**Companion control cycle button, locked at `PT-1141`, deliberately its own control rather than a third meaning stacked onto the portrait tap.** Sits beside each sidebar entry's info block, cycling between manual, hands-off, and auto-battling. Given the portrait tap already carries two context-dependent meanings, a third one layered on top would be genuinely ambiguous with no visual cue distinguishing which was about to trigger — this avoids that entirely by being its own clearly-scoped tap. One press flips the mode; the same button doubles as the "step in for one turn" override, since flipping a companion to manual right before their turn and back afterward costs exactly one tap either way, no separate mechanic needed. Styled in the established house palette rather than copied from either source game — neither actually shipped a cycling control like this: K1's real script system opened a full separate screen, K2 never shipped this control anywhere in its interface at all.

**Combat-side party control, locked at `PT-1143`, closing the item flagged since `PT-1136`.** Full manual is the default for every character, matching what our action-economy system already implies about player-initiated decisions. A companion can be switched to hands-off (the AI decides everything, no player input reaches it, ever) or auto-battling (the AI acts by default, but a player can grab any individual turn back at will via the same cycle button, then let it return to auto afterward). **Auto-battling's actual behavior is chosen from K2's five presets** — Aggressive, Defensive, Ranged, Stationary, Jedi Support — confirmed by `TRACE-37` as the source's own better-designed set, adopted directly as our starting list rather than K1's thinner three or NWN's fuller but more complex system. Preset selection lives on the Character Sheet, reusing K1's own smart placement logic rather than building new screen space: that screen already knows whose data is being viewed, so per-companion scoping comes free, exactly the property `TRACE-37` flagged as worth keeping. The flat-list-with-live-description pattern the source used for this picker is adopted directly too — genuinely good UX on its own, separate from the single-enum limitation the research found underneath it.

**Single click only — no distinct double-click behavior anywhere.** Confirmed absent in both games' actual interaction layer, not merely undocumented.

**In-screen party switching, locked at `PT-1135`, costing us nothing new to build.** `TRACE-35` confirmed both games let a player switch which party member's data a character-suite screen shows without backing out first — K2 broader than K1, built once into shared chrome rather than authored per screen, and the research explicitly names that architecture as the thing worth copying. We already have exactly that shared chrome: the always-visible sidebar (`§3`, running through both exploration and combat) already shows every party member and already opens a character's own screen on click (`PT-1134`). The only rule genuinely new here: **switching this way preserves the current screen type** — clicking a different portrait while already viewing Equipment shows that character's Equipment, not a reset to some default. No new control surface required, only this one behavioral rule.

**The context-flagged keybind pattern, adopted as a standing principle for `PT-1135`.** `TRACE-35` found the source drives this with a data table where every action carries per-context activity flags — active in a menu, active in gameplay, active in dialogue, and so on — so the same physical key means different things in different contexts with no special-casing required in any individual screen. Genuinely worth stealing outright as our own architecture for keyboard and gamepad input generally, not just for this one feature: one data-driven table an author can read and edit, rather than scattered conditionals. The specific key itself (Tab, in source) is a detail to confirm later against our own control scheme; the pattern is what's locked here.

**Navigation between these screens, locked at `PT-1129`, checked directly against K1 rather than assumed.** `TRACE-29` found K1 has no shortcut at all between journal and message log, one-way or otherwise — instead, every character-adjacent screen sits as an equal peer on one persistent eight-button bar, always visible, always one click away, with no hierarchy between any of them. Adopted directly: **Equipment, Inventory, Character, Abilities, Messages, Journal, Map, Options**, matching K1's exact set. Map and Options aren't new — Map is a direct path to the full-area-map zoom level already locked in `§3`, Options is quick access to settings. This makes the K2-style journal-to-log shortcut genuinely optional rather than load-bearing — Message and Journal are already equally one click away from anywhere, so adding that shortcut later is a pure convenience, never a fix for something missing.

**Store and Container, locked at `PT-1152`, deliberately excluded from that shared bar rather than added to it.** `TRACE-43` confirmed this exclusion is real and intentional in both games — Store and Container fail every structural test that marks a screen as part of the shared-frame family, and `TRACE-42`'s completeness audit sharpened by the same check: the family is exactly those eight and nothing else, no exceptions found anywhere in either game. **The boundary is drawn around the transaction, not the screen** — the eight character-suite screens are a player looking at their own things; Store and Container both involve someone or something else, money or items changing hands. Adopted directly as our own architecture: both are fully sealed modals, reached only by clicking something specific in the world (a merchant, a container), with no path to any other screen while inside and no accidental route through a shared frame drawn underneath, since neither composites with one. Exit is a single Close, back to the world, never to a menu.

**The gap this creates, closed rather than reproduced.** A sealed screen only works if it doesn't leave a player needing information they can't see. `TRACE-43` found K1's store shows nothing about what a player already owns; K2 partially fixes this with a simple on-hand count. Adopted as the floor, then extended: since our own Equipment slot data is already fully known, the purchase screen also shows **what an item would actually replace**, right there in the sealed moment — closing the gap structurally rather than leaving a player to guess or step outside to check.

**Color, per `PT-1151`'s K2-default rule.** Both games treat commerce as a real chromatic exception, joining the target plate and the terminal on that list — K2 themes its store in gold and bronze, found nowhere else in its interface; K1 uses its own off-palette yellow. K2's gold/bronze adopted as the default, a deliberate, legible break from house palette specifically for a screen about money, consistent with how every other special-case color in this project has been handled.

**A second, distinct color exception, now confirmed recurring rather than a one-off — `TRACE-58` and `TRACE-59`.** K2's own upgrade/crafting family and K2's own galaxy map both render functional text in `#00A8FA`, K1's cyan, not K2's own house teal, in K2's own build of both screens. Two independent confirmations of the same real pattern: some of K2's own functional/informational text stays in K1's inherited cyan rather than adopting K2's own house color, even inside screens K2 itself designed. Worth treating as a real, generalizable house exception going forward — any screen carrying over this specific K2 functional-text role should be checked for the same cyan carry-over before assuming house teal applies.

**Full store layout and text structure, locked at `PT-1153`, with two real defects fixed rather than copied.** `TRACE-44` found the filter buttons carry no active/selected state at all in either game — a row of identical-looking text with one silently in effect — even though the primitive already exists and the engine's own HUD toggles prove it supports the extra state. Fixed: filters get a real, visible active state. Second: the mode heading and the confirm button read from the exact same value in the source, meaning they can never disagree — adopted directly rather than treated as a coincidence, so switching Buy/Sell flips both together from one bound value. Filter categories: **All, Weapons, Armor, Misc**, a real subset of Inventory's own seven — flagged as worth unifying rather than leaving as two different taxonomies moving the same goods. The readout folds the credit balance into one four-row block on K2's pattern, confirmed the better arrangement over K1's separately-floating balance — price, credits, then two counts worded as a genuine parallel pair, **`In Stock` / `In Inventory`**, the same preposition-led shape asking one question of two different places. Label and value stay separate fields throughout, matching every other readout in this project.

**Item icons, added to both Store and Container.** Neither screen's spec explicitly called these out, but every item row in both sealed-modal screens carries a small icon alongside its name — consistent with how items are represented everywhere else a player sees them.

**Build note, stated plainly for whenever real development starts:** this bar should be built to match K1's actual design exactly, using icons rather than text labels — confirmed as the intended implementation, not an open style question.

**Icon system, locked at `PT-1158`, K2's technique adopted per `PT-1151`.** `specs/SPEC-03` found K1's icons are sixteen pre-colored, unretintable textures, while K2 draws eight white shapes on transparency and tints them at runtime — the identical primitive discipline `SPEC-01` already established for every other border and frame in this project. Adopted directly: one authored asset per icon, tinted house teal at rest and bone on hover, using the shared nine-slice frame already specified rather than baked art. Confirmed real game icons in current mockups are temporary prototypes only, per `PT-1157` — same standard, applied here too.

**The fifth slot, locked at `PT-1158`: Party Selection, not Messages.** `SPEC-03` found K2's fifth icon depicts something genuinely different from K1's — several figures rather than a page of text — and it isn't a cosmetic swap, since `TRACE-37`'s keybind research independently found the same slot behaves as party selection in K2. The redundancy this creates is what makes the swap free rather than a loss: Messages stays fully reachable through Journal, per the shortcut already found and locked at `PT-1129`, so nothing becomes harder to reach by giving this slot to something new. **The multiplayer contest this creates — two players wanting the same companion — reuses the yield-first-then-roll resolution already locked for dialogue** (`§3`), rather than inventing a separate rule: whoever yields defers, a genuine contest is settled by roll rather than by connection speed, keeping the whole multiplayer system consistent rather than a pile of one-off mechanics.

---

## 3. Core play view

Three things share this space now, and all three have real design behind them: dialogue, the grid, and the shared narration space that carries everything else.

**Dialogue with the DM — locked at `PT-1104`.** `ENGINE-SPEC-03 §4c`/`§4d` carries the full design now; this is the summary. Reply options render as plain inline text with only the bracketed tag colored — no pill, no badge — confirmed against `TRACE-13` reading KOTOR's actual dialogue panel directly: it had exactly one styling slot for the whole reply list, not per-item, so KOTOR's plainness was a tooling limit rather than a choice, and coloring the tag is something it never had the capability to do at all. Three colors carry three genuinely different meanings: amber for a real skill check, which shows no number until clicked and then reveals a separate panel with the DC as the headline figure; muted gray for a manner tag like `Lie`, which never rolls anything; teal for a background-gated option, available because of who the character is rather than a roll. Confirmed provisional rather than final — revisit once there's a real build to sit in front of, not before.

Multiplayer dialogue is fully specified: one shared, synchronized screen for everyone present, only one player picking a reply at a time, anyone nearby free to join an in-progress conversation, the initiator choosing whether to wait for others or start immediately, a yield-first-then-roll resolution when more than one player wants the same pick, and the initiator controlling advancement through plain NPC lines. Whoever wins a pick uses their own character's stats for whatever follows.

**2D grid movement** — a tabletop-mat equivalent, digital, 2D rather than NWN's 3D. This is not just an art decision — **it resolves an open engine question.** `ENGINE-SPEC-06 §4` left relational-vs-absolute positioning open specifically pending a UI answer. A visible grid with tokens on squares means every combatant needs real coordinates — the answer is absolute, not relational. Worth ruling that formally once this is settled, since it unblocks `§4` and, downstream, `SW-7`'s cover query.

`TRACE-11` gives the grid a real structural precedent, and rules out the obvious alternative: NWN's areas are a genuine tile grid with real coordinates per tile — the right foundation for a system that needs to answer "who's adjacent to whom" or "what's inside this radius." KOTOR's own map has no coordinate system underneath it at all — it's a flat picture with a transparency mask painted over it, nothing to build a grid from. Same split as character creation: structure from NWN, visual skin from KOTOR.

**Grid token design, locked at `PT-1137`, replacing the flat colored dots used in every mockup so far.** Each occupied tile shows the same portrait already designed for the sidebar — party or enemy, whichever applies, per `PT-1132`/`PT-1133` — rather than a plain marker, so a token on the board and its entry in the sidebar are visibly the same character rather than two disconnected representations. A decorative ring surrounds the portrait, distinct from the sidebar's own selection border, purely a framing device for how a token reads sitting on the grid rather than carrying state on its own. One tile, one occupant, always — `ENGINE-SPEC-06 §4` locks this as a direct consequence of absolute positions being real: two combatants cannot share one position, the same way a chess piece owns its square outright.

**Live visibility, locked at `PT-1103`.** One screen, not a separate map you check on purpose — the tactical view you're actually playing on renders in three states at once: what's directly in front of you now, fully lit; somewhere you've been but aren't currently standing in, dimmed and drawn from memory; somewhere never visited, blank. Visibility is **geometry-aware, not distance-aware** — blocked by walls and closed doors specifically, not revealed by a radius around the player regardless of what's in the way. A room switches from blank to lit only once actually entered, and stays at least dimmed from then on.

Corrected against source before locking: this three-state pattern — lit, remembered-and-dimmed, unknown — is not from either game. KOTOR's own map is binary, seen or not, and once revealed it stays fully clear forever with no dimming and no memory decay. NWN's actual play view has no fog of war at all. Ours is new, the way Continue and the account system are new — worth marking as ours rather than assumed borrowed.

And the memory stays a display concern only, not a rules one. `CANON-01 v2`'s local layer is already a *projection*, narrow to what's currently relevant, not a standing authority — the dimmed-room memory is a convenience for the player's eyes sitting on top of that, not something the rules engine itself tracks or depends on. The engine's live context stays exactly as narrow as already decided; the map just being kinder to look at doesn't change that.

**The scroll window, locked at `PT-1105`.** Narration, party exchanges, and non-dialogue rolls (Awareness on entering a room, an attack in combat) live in one continuously accumulating log, distinct from dialogue's replace-based window — dialogue takes over the screen when a conversation starts; this is what's underneath the rest of the time. Rolls in this space are **player-initiated, not automatic-with-opt-out** — owner overrode my recommendation deliberately: an active turn, where the player is already choosing what to spend each of their five action-economy budgets on, should have them roll too, not have it happen to them. Matches the two-stage check reveal already built for dialogue at `PT-1104` — a "roll" button, not an automatic result.

Multiplayer follows the same rule as dialogue: one shared, synchronized view for everyone present, with every line clearly tagged as a specific player, an NPC, or the DM.

**Layout shifts between two states rather than picking one fixed arrangement.** `TRACE-14` found KOTOR lets players choose their own auto-pause moments — enemy sighted, party member down, round ended — rather than forcing real-time or turn-based on anyone, and names the reason whenever it stops. Ours works the same way conceptually: while the game is resolving on its own, grid and scroll sit together, both compact, narration flowing. The moment something genuinely needs the player's decision, the layout shifts — the grid grows to take the room it needs, the scroll dims back rather than disappearing, and a label states plainly why the game is waiting. Confirmed working as an actual interactive toggle before being written in here, not just described.

**Zoom is one continuous range, not separate screens — extending `PT-1103`'s "one screen, not a map you check" further than originally scoped.** Three points on it: tactical, local, and full area map, the last of these being what a traditional overview map would have been as its own screen. Outside combat, all three are freely selectable. **Combat locks the zoom to tactical automatically** the instant a fight starts, regardless of where the player had it — the player doesn't have to remember to zoom in themselves.

**Action economy gets its own on-screen slots, one per budget** — Move, Action, Bonus, Gear, Reaction, the five from `ACTION-ECONOMY-01` — appearing only once the layout has shifted into its paused, decision-focused state. `TRACE-14` found the combat math itself doesn't transfer from KOTOR's single-queued-action model, but one piece of the interface does directly: a compact resting slot per category with the full option list one click away, rather than changing the whole screen to show it. Confirmed working as an actual click-to-expand interaction, not just described.

**The three fog-of-war states from `PT-1103`, shown concretely for the first time**: lit for the party's current position, dimmed for a remembered but unoccupied room, nothing drawn at all for anywhere unexplored — visible directly in the grid rather than only described in the spec.

**Targeting is contextual, locked at `PT-1108`.** No standing "who am I targeting" axis sitting permanently on screen. A player picks an action first — Attack, a Force power, whatever's relevant — and only if that specific choice actually needs a target does the game ask who. This is a deliberate departure from `TRACE-21`'s finding that KOTOR runs two always-visible axes, target and action, cycled identically: that shape exists to solve a real-time problem neither of us has, since our five action-economy budgets don't all need a target the way KOTOR's single action slot always did (Move doesn't; an attack does). Justified by having more structure than the source, not less care.

**Two combat interaction systems, one default, one a genuine alternative — locked at `PT-1108`.** Our own compact-slot-with-full-menu-on-click system (already specified above) stays what every player gets by default. A separate settings option, off by default, switches to spinner-cycling faithful to `TRACE-14`/`TRACE-21`'s actual findings, for anyone who wants the original games' specific feel. This means building two real interaction systems, not a single system with a different skin — accepted deliberately as worthwhile rather than scope creep, since it preserves something already carefully researched rather than inventing something new.

**Stealth presentation, locked at `PT-1108` — mechanics untouched, only how it's shown.** `SKILL-RESOLUTION-01 §4` and `ACTION-ECONOMY-01`'s Hide action stay exactly as already specified: Hide is an action, opposed against the better of the enemy's Awareness or Alertness, granting the Hidden condition on success. Two things borrowed from `TRACE-21` on top of that, deliberately: a **real, clearly visible indicator** while Hidden is active — not the small easy-to-miss checkbox the source games actually used, matching the same "nothing hidden from the player by default" rule held everywhere else — and **Hidden disables running**, restoring a real cost the source had that a bare opposed roll doesn't otherwise carry. Neither change touches the roll or the condition itself.

**Friend/enemy/low-health color rule, locked at `PT-1109`, marked explicitly reversible.** Allies and anything friendly use whichever of our two starter themes is active — the same colors the rest of the app already uses. Enemies and combat-hostile things are fixed red, regardless of which theme is active, since `TRACE-18`/`TRACE-22` confirmed red is the one color both source games treat as universal rather than theme-specific. Low health, for anyone, is carried by the health bar itself flashing between red and white — deliberately not a static color, since a static red would be indistinguishable from an enemy's already-red baseline identity. This corrects a real gap `TRACE-22` found in the source: neither game gave a shrinking bar any additional signal for urgency, leaving a sliver of health looking identical to a large loss at a glance. Locked as a genuine design decision, not a placeholder, but explicitly kept reversible to the simpler shrinking-bar-only version if it doesn't hold up once actually built and played.

**No separate target plate — the combat sidebar carries that job instead, locked at `PT-1110`, position corrected at `PT-1111`.** The source games' floating target cluster is not being built. Once combat's sidebar exists — showing every combatant, ally and enemy, name and health — that sidebar *is* the target display, replacing what a floating plate would have done. Docked to the **left** edge, matching Del Arroz's app and Baldur's Gate 3, correcting the right-edge placement the party rail also mistakenly drifted into. Part of the original reasoning for using the sidebar at all was that it avoids `TRACE-22`'s minimap collision, but that collision was specifically the source games' top-left corner — we haven't actually located a minimap in our own design yet, so whether the left-edge sidebar creates a new version of that same problem once one exists is worth checking rather than assuming solved.

**The sidebar now runs during exploration too, not just combat — locked at `PT-1124`, closing the party-visibility gap flagged in `§2`.** Party members are always visible there; enemies are not shown at all until they're actually fighting you specifically.

**The portrait design itself, locked at `PT-1132`, closing the open information-content question honestly rather than guessing.** `TRACE-30` confirmed the source carries seven real signals per portrait — identity, vitality, Force, and four condition markers (disabled, debilitated, level-up pending, plus separate buff and debuff corner icons) — and drew one clean, deliberate line worth adopting directly as a rule: **the portrait shows condition, never statistics.** No name, class, or level in the source; those live on the character sheet.

We depart from that boundary on purpose, pulling from `UI-REFERENCE-ABACUS-DEMO-01`'s Del Arroz findings: **name, class and level, and a numeric experience readout now sit in a text block beside the portrait**, since a sidebar a player looks at constantly benefits from that at a glance in a way K2's occasional HUD glance didn't need to justify. Structurally, K2's own wing-bar language is kept and extended rather than replaced: vitality as the left wing, Force as the right wing — both full-height vertical bars flanking the portrait, matching K2's real proportions, not K1's thin strips — and **experience added as a third, thin wing wrapping the bottom edge**, connecting all three into one wraparound frame rather than bolting XP on as a separate stacked element. The numeric readout (current/total) sits directly under class and level in the text block, giving both an at-a-glance bar and an exact number without requiring a click.

Buff and debuff icons, and the disabled/debilitated/level-up overlays, all carry over unchanged from `TRACE-30`. The low-health flash from `PT-1109` applies here too, on the vitality wing specifically, for consistency with the target sidebar rather than inventing a second rule.

**Confirmed identical for the player's own entry and every party member — no special "you" treatment beyond the same selection border already used everywhere else.**

**Enemy portraits, locked at `PT-1133`, closing what `PT-1132` left open.** Structurally an inversion of the party design rather than a stripped copy — `TRACE-31` confirmed the source itself never gives an enemy a real portrait, only a name; ours keeps a portrait anyway as our own substitute for something the source got for free that we don't: actually seeing the enemy's live model in a 3D scene. Layout: health bar sits above the portrait, name in its own info block beside it matching the party's block position — but enemy-only, since there's no class, level, or XP to show. Fixed red throughout, per `PT-1109`. Buff and debuff icons carry over from the party design, unchanged.

**Correcting two real mistakes from earlier passes, found only once the actual mechanism was checked directly.** First, `TRACE-22`'s inference that the target cluster's small icon slot was a per-enemy portrait was wrong — `TRACE-32` confirmed it's an action icon, showing what *you* can do to the target, built from your own skills and inventory, never anything about the enemy's identity. Second, `TRACE-22`'s minimap collision finding was itself wrong — the coordinates behind it turned out to be an engine placeholder overwritten every frame, nothing ever actually drawn there. Both corrected in the record rather than left standing.

**And the real mechanism, corrected from `TRACE-21`'s original "two axes" framing:** there is no separate "who" selector at all. Targeting happens by clicking the creature directly in the world; the name and health plate float attached to that creature's own screen position, tracking it as it moves, and friend versus foe is shown by a colored reticle rendered on the model itself — violet or teal for friendly following the same K1/K2 divergence found everywhere else, red for hostile, the one value neither game ever re-themed.

**Buff and debuff icon artwork, locked at `PT-1133`.** `TRACE-33` found K2 genuinely redrew these from scratch rather than retinting K1's version — a real, rare exception to the pattern held everywhere else in the source. Adopted: K2's hollow chevron shape, for consistency with everything else already built around K2's style, kept as a true mirror image between the two states exactly as the source does it, so buff and debuff can never visually drift apart from each other. One deliberate addition beyond the source: a small effect-count badge next to the icon. Both games only ever showed one bit of information — something helping or hurting is present — with no way to tell one effect from several stacked together; given informed decisions are the whole point of a deterministic system, that gap was worth closing, and the badge costs nothing structurally since the icon slot already exists.

**Sidebar ordering, locked at `PT-1133`, closing the turn-order idea logged back at `PT-1110` and never designed until now.** Outside combat, the sidebar is personalized per viewer rather than one shared list — whichever player is looking at their own device sees their own character pinned at the top, party below. The moment initiative is rolled, this becomes one shared, objective order instead — first to act at the top, last at the bottom, identical on every player's screen, since initiative is a fact of the fight rather than a personal preference. Once the fight ends, it reverts to each player seeing their own character on top again.

**Motion for these transitions, confirmed as an actual working interaction before locking, not just described.** Every order-changing transition — rolling initiative, manually ending combat, or the fight ending because the last enemy fell — uses the same curved shuffle: each card sweeps along its own individually varied curve from old position to new, continuously eased rather than moving in a straight line, so several cards moving at once don't read as one identical motion repeated. A regular mid-fight defeat, with enemies still remaining, is treated differently on purpose: the remaining cards simply slide straight up to close the gap, a quicker and quieter motion reflecting that it's a small removal, not a full reorder. A defeated enemy disappears from the list entirely rather than sitting at zero health.

**What "actually fighting you" means, built entirely from pieces already locked rather than invented:** one new state per NPC, plainly on or off — *currently engaged in combat.* It turns on the instant either an attack targets them, or they successfully notice a Hostile-disposed party member (the five-point attitude scale already in `RULES-02` — Hostile, Unfriendly, Indifferent, Friendly, Helpful) via the opposed detection roll already built for Stealth. It turns off once they're defeated, or once they lose track of every party member for a full round with nobody reacquiring by the start of the next one — reading directly off the round structure combat already has, not a new timer system. The sidebar's rule is exactly this simple as a result: show anyone whose engaged state is currently true, nothing else.

**Grid and sidebar selection are one shared state, not two separate things kept in sync.** Tapping a token on the grid or an entry in the sidebar selects the same target either way — there is exactly one piece of truth about who's currently targeted, read from two places, never two independently-tracked answers that could disagree. This directly closes `TRACE-22`'s finding that the source games' own files couldn't confirm which of their three target slots was actually current; that ambiguity has no way to exist here by construction. Selected state shows on both: the grid token gets a highlight ring, the sidebar entry shifts slightly and gains a border. Confirmed as an actual working interaction, both directions, before being written in here.

**Two items surfaced by this conversation, logged for later rather than built now.** First: fold turn order into the same combat sidebar once it's built — every combatant shown in the order they act, prompted directly by the owner's own instinct toward Baldur's Gate 3's top-of-screen portrait row, which turned out to answer a different question ("whose turn is it") than targeting does ("who am I aiming at") and is worth having on its own merits rather than being forced into solving the target-plate question it was originally raised for. Second: initiative rolls automatically, no player prompt — nothing being taken from the player, since nobody is making an active choice about how well they roll to go first, consistent with rolls staying player-initiated specifically where a real choice is involved.

**One item resolved into a real architecture, not fully open anymore:** Solo Mode is no longer its own system waiting on a separate conversation — it's one entry in the exploration action catalog below (`§3a`), specifically a party-directed verb rather than a special mode. The verb list itself and where each category physically appears on screen remain open, tracked there.

**Tile art, direction set, not yet built. Corrected at `PT-1136`: this paragraph and the next were misplaced under `§3a` in an earlier edit and are restored here, where they actually belong.** Real per-tile art is the plan, not flat color — modeled on how NWN's own toolset preview window shows real tile art while an author places pieces, which lines up with `TRACE-11`'s finding that NWN's areas are already a grid of real, textured tiles under the hood. The obvious source — KOTOR's actual textures — is real, copyrighted art, the same issue already flagged for portraits. Treated the same way: placeholder now, clearly marked as temporary, real art built or licensed properly before anything ships.

Loading screens with concept art between areas — deferred, noted for later.

---

## 3a. The exploration action catalog, locked at `PT-1122`

**The real split, confirmed rather than assumed:** combat needs a defined, closed set of options because it's turn-based and fairness depends on everyone having the same defined choices — which is exactly why `ACTION-ECONOMY-01`'s five budgets exist. Exploration doesn't have that pressure, and checking D&D 5e's own actual rules confirms this isn't an oversight to fix — 5e itself defines a closed list of combat actions and *deliberately* leaves exploration open, reasoning that nothing forces a turn structure outside a fight. Digital 5e tools (D&D Beyond, Roll20, Foundry) confirmed to build nothing resembling a formal exploration-action catalog either — nobody has solved this the way we're about to.

**Architecture, modeled on `TRACE-26`'s finding for NWN's right-click system, not its separate 12-slot quickbar, which is a distinct system flagged as its own open question below.** One flat table of possible verbs, each filtered in or out by context — shown only when genuinely relevant to whatever's currently clicked or nearby, never a fixed menu everyone sees regardless of situation.

**Three categories, sourced from what's already built rather than invented:**

    ⚠ Object-directed  — search, open, repair, hack, disarm — mapping
      directly onto skills already defined in `SKILL-RESOLUTION-01`,
      several of which explicitly don't roll dice at all
    ⚠ Self-directed    — rest, meditate (`REST-AND-MEDITATION-01`,
      already built), consumables, non-combat Force powers
    ⚠ Party-directed    — **Solo Mode lives here now**, as one verb
      aimed at your own companions ("wait here") rather than a
      separate mode with its own rules

**Verb list, first pass drafted from what's already built rather than invented — locked at `PT-1123`:**

    ⚠ Object-directed  Search (Awareness) · Open Lock (Security) ·
                       Disarm (Demolitions) · Repair · Slice ·
                       Pick Pocket (Sleight of Hand) · Track (Survival) ·
                       Examine — auto-picks Xenology, Archaeology,
                       Mysticism, or Science by what's actually clicked,
                       one verb rather than four separate buttons
    ⚠ Self-directed    Rest · Meditate · Use item · Force power
                       (`REST-AND-MEDITATION-01`, already built)
    ⚠ Party-directed    Wait here (Solo Mode, `PT-1122`) · Follow/
                       regroup · Trade/give item

**Confirmed gaps rather than oversights:** Alertness stays passive, triggered automatically rather than chosen. Beast Handling and Pilot surface only when a beast or vehicle is actually present, not as permanent list entries. Acrobatics/Athletics/Swim stay folded into movement itself on the grid, not separate deliberate actions.

**The governing rule, locked at `PT-1123`, settling more than the two skills that raised it:** Persuade and Intimidate live exclusively in dialogue — no separate object-click shortcut into either, ever. Reasoning generalized into a standing principle for every future skill shaped like this: **if using a skill on a person requires communicating with them, it belongs to dialogue alone; if it's something physical done to a person or their things without requiring exchange — Pick Pocket, for instance — it's a normal exploration-catalog verb.** Chosen specifically to avoid the same skill existing in two places that could quietly drift apart from each other over time, rather than because dialogue's existing fallback-generation system already covers the ground a second path would only duplicate.

**Screen placement, shape chosen at `PT-1124`, not yet mocked up:** object-directed verbs surface as a context menu at the point of contact, tapping something on the grid directly — NWN's model. Self-directed verbs live on the player's own card, already locked in `§2`. Party-directed verbs live on the sidebar, extended to exploration above. Every category now has a confirmed home built from pieces already locked, rather than new screen space invented for this.

**Deferred at `PT-1264`, leaning no:** whether we want our own version of NWN's player-filled quickbar at all, and if so, typed like our combat budgets or untyped like NWN's. **Not settled here because the normal in-game UI is still developing** — a quickbar answers a question about a surface that is not finished.

---

## 3b. Exploration party control and following, locked at `PT-1136`

**The control model itself, confirmed rather than invented — matches K2 and BG3 independently.** One character is actively controlled at a time — the player's own character solo, or in multiplayer, whichever of the player's own character or their one bound companion they're currently focused on, cycled between via the exploration-HUD portrait mechanism locked at `PT-1142`. Everyone else auto-follows the active character. This is genuinely the exploration half of the larger party-control question flagged since `PT-1110` — settled here on its own terms rather than as a side effect of anything else. The combat half remains a real, separate, still-open question.

**The follow mechanism, adopted directly from source.** `TRACE-36` confirmed following in both games is a persistent, native engine action using real pathfinding, re-armed by a script only when it lapses — never a simple "stay within some distance" rule. Adopted as-is; there was nothing broken in the core mechanism.

**The one genuine gap, answered rather than reproduced.** Both source games leave a follower who's completely blocked with no path at all unhandled — the developers' own shipped code for that exact case is empty, with a comment asking themselves what should happen there, never resolved, identical in both games. Our grid makes this cheap to actually answer: whether a tile is reachable at all is a clean, fast yes-or-no question on a grid, not the harder problem it was in the source's continuous space. When a follower is genuinely stuck, they say so and hold position rather than silently failing; they resume automatically the instant a path opens.

**Formation, adopting a system the source built but never switched on.** `TRACE-36` found both games ship a complete, working formation system — real positions for where followers should stand — that no script in either game ever actually activates. Adopted and turned on, extended slightly for our own party sizes: a close ring at one tile as the target distance, with a second, farther ring for anyone who doesn't fit in the first, rather than one ring that can't hold a larger party. Explicitly a target, not an absolute rule — a follower heads toward their formation slot when there's room to, rather than being locked to exactly one tile in a corridor too narrow to allow it, which keeps this from conflicting with the stuck-follower fix above; that one covers a genuinely blocked path, a different and rarer problem than simply not having room to stand in the ideal spot for a moment.

---

## 4. Nostalgia UI — terminals, droid repair, minigames

The instinct is right: lift these as close to verbatim as the source allows, for the "this looks like the game" effect specifically. `TRACE-08` closed the gap flagged here — both games ship their GUI as data, and the two formats are not equally liftable.

KOTOR's is the one to lean on. It's typed controls with absolute rectangles in a fixed 640×480 space, a plain enum for control type (panel, label, button, checkbox, slider, scrollbar, progress, listbox), textures referenced by name, and text resolved through the same string table dialogue uses. Even the tab order between controls is authored data, not computed. Everything a faithful terminal or droid-repair screen needs — including that the terminal and droid-upgrade panels already exist by name in the source — is sitting in the file, plainly readable.

NWN's is not a good target for lifting. Its panels are a scene graph of relative offsets, and a panel on its own means little until its shared visual template is resolved through a whole reference chain. Fine for building our own new screens in NWN's spirit; not something to extract wholesale.

So: KOTOR for anything meant to look exactly like the game. NWN's actual contribution turned out to be structural, not visual — see `§1`.

**Next concrete step, logged at `PT-1145`, not yet started.** The principle above was stated in the abstract; the actual screens were never researched or mocked up. Owner wants Computer Use and Repair specifically checked and lifted as close to verbatim as the source allows — real layout, real interaction pattern, changing almost nothing — with room to extend the same pattern to other skills once those two are settled. A dedicated Claude Code pass against the real panel data, the same standard every other screen in this document has already gotten.

**Option text convention, locked at `PT-1149`, `TRACE-40`/`TRACE-41` confirmed.** Computer Use and Repair are one shared screen in the source, not two — the only real difference is which resource an option consumes, spikes or parts. The row height itself dictated the writing convention: a hard, one-line limit forced every option into skill tag, complete sentence, cost, all on a single row, no subtitle possible. Adopted exactly: **`[Skill] Complete sentence. (cost)`** — the tag prefixed in brackets rather than a subtitle, a real full sentence rather than a fragment, cost as a parenthetical suffix in parentheses specifically (K1 was consistent here; K2's mix of brackets and parentheses is a defect, not a second valid style). One deliberate fix over source: proper pluralization computed live, rather than the literal "(s)" both games typed onto every string regardless of quantity. And since our cost is skill-scaled rather than fixed, the number shown has to be calculated at display time — K1 already had a handful of options straining toward exactly this with token substitution; ours does it properly. The readout stays a separate channel from inline cost, both kept: label and value as distinct fields, four fixed rows, no "remaining," no fraction, no color coding, matching the source's plain structure exactly.

**Backdrop art direction, locked at `PT-1150`, a real synthesis rather than a straight lift from either game.** `specs/SPEC-02` found the two games' approaches aren't a retheme of each other — they're conceptually opposite, and the difference traces back to a structural cause rather than pure taste: K2 added real bordered text panels K1 never had, and a frame needs something dark and quiet behind it to read clearly, so K2's backdrop became a flat, symmetric bezel where K1's was a lit, atmospheric space. Adopted brief: **K2's structure, K1's tonal warmth** — one real asset built to modern practice (no resolution-tiered variants the way K1 shipped eight of), composed with K1's softer, more atmospheric feel rather than K2's colder symmetry, since nothing about that warmth was actually tied to K1's outdated technical approach. Confirmed the same backdrop serves both Computer Use and Repair, consistent with `PT-1149`'s one-shared-screen finding — neither game gave Repair its own art, and neither do we. Two lighting states of one composition, not two separate images, matching the source's own Standard/Rakata approach. The additive speckle animation already found stays exactly as locked, layered behind the text rather than over it — this brief only covers the static backdrop beneath that layer. Real final art remains deferred, same as every other visual asset in this project; this is the brief it gets built to, not the art itself.

---

## 5. Audio

Three separate things, worth keeping separate in scope:

- **Music, with triggers** — area music vs. combat music, transitions, stingers. By `PT-1056`'s test this is cleanly engine-*adjacent*, not engine-*owned*: no GM rolls a die for what music plays. The ledger only needs to expose state that already exists for other reasons — `combat: true/false`, location, alert state — and the app layer decides what to play off that. This is good news; it means audio doesn't create a new dependency on the rules engine, only a *reader* of state the engine already tracks. Worth a Claude Code pass specifically on how the original games wire trigger scripts to music state changes, since that pattern (not the actual tracks) is what gets reused.
- **Cutscenes and character dialogue audio** — separate system, likely ties into the dialogue tree work (`ENGINE-SPEC-03`) for playback triggers.
- **Sound effects** — smallest scope, probably follows whatever pattern the music trigger research turns up.

---

## 6. Multiplayer — party composition and the lobby

Party math corrects an early assumption of mine, checked against `PARTY-01` rather than invented: it is not a fixed total that empty seats fill in with companions. Solo — one human — fields three companions, four bodies total. Multiplayer — two or more humans — is one companion each, scaling up with headcount rather than filling toward a cap: two players is four bodies, four players is eight. The reason is concrete: companions already take their own turn in combat, which is fine solo, but would mean sixteen turns a round at a real table of four humans, most of them nobody's. One each keeps the companion system alive without the table stalling. **The moment a second real person joins, party math flips formulas entirely** — the lobby's job is to show that flip live, not to show companion slots as something a player fills.

A package declares its own player cap — not a total body count, a cap on human seats specifically. The lobby is a roster built from that cap: filled seats show a name, chosen character, and ready state; open seats show an invite affordance, up to the package's max. **Play only cares about filled seats being ready — open seats never block it.** A subtitle above the roster states the current formula in plain terms and updates the moment headcount changes, so a host watching people join sees the party math shift in real time rather than having to work it out themselves.

Friends are invited directly into open seats, not found the way `TRACE-10` found NWN does it — their buddy list only tells you which server a friend is already on, so you go join them there. Ours skips that step entirely.

`PT-1102` locked all of this, plus one addition: the same roster, docked as a compact rail on the package main menu itself rather than confined to a separate lobby step, so a player sees their party forming the moment they land on the menu. Collapsible — a thin tab stays visible at the panel's edge in both states, so pulling it back out or tucking it away is always one click.

**Connection architecture, locked at `PT-1144`, closing the "player connections around the world" item flagged since the very first pass.** `TRACE-39` checked NWN's real, two-decade-old multiplayer system rather than inventing ours from nothing, and it resolves the open matchmaking question directly: hosting and public listing aren't two systems, they're one — a single toggle on the same session deciding whether it's visible to a public browser or stays private. Adopted directly, closing what the owner had flagged as possibly needing its own separate system.

**The host's own device is the server — no separate server software required, ever.** Confirmed as NWN's real, proven architecture: the client secretly contains a complete server, and hosting simply means running it locally. Exactly the shape a mobile-first game needs.

**Everything a player owns lives on their own device first; any central listing we run is a convenience layer, never the source of truth.** The one real cautionary tale in the research: NWN's public browser depended entirely on an external listing service, and when that service shut down permanently in 2012, the browser died with it — what kept the game alive afterward was purely local history and favorites, untouched by the outage. Taken as a hard requirement, not just a preference: friends and session history are stored locally, so losing any service we run never breaks a player's ability to reach someone they already know.

**Friends are captured automatically after a shared session, never typed by hand.** Corrects a real, well-documented failure in NWN's own system — its name-typed buddy list broke often enough that the game's own error messages told players to fix it on an external website. We avoid the entire failure class by never asking for a typed name in the first place.

**A real invite code, genuinely new rather than adopted from source.** `TRACE-39` confirmed NWN never had one at all — its only answer to "play with this specific person" was sharing a raw IP address, a gap it openly needed and never closed. Ours gives that a real, friendly answer instead.

---

## 7. Journal and message log — locked at `PT-1107`

Checked directly against K2's actual panel data (`TRACE-17`), not K1's — a real trap avoided here: K1's message log has 5 controls, K2's has 20, and it is a genuinely different screen, not a light reskin of the same one. Two panels, built to be pixel-identical in their chrome, with a button at the top keeping both always one click away from each other.

**Journal.** Two columns — a quest list on the left, a scrolling description of whichever quest is selected on the right. Planet is a sort key here, not a folder to dig into — one flat list, four ways to arrange it. Quest entries are framed, clickable boxes; the description text underneath them is plain, unframed, and scrolls independently.

**The filter row, corrected and fully locked at `PT-1160`.** `TRACE-52` reframed what `TRACE-49` had already found: this isn't five buttons, it's one continuous sentence. The active/completed toggle is the opening clause — "Active Quests By" — and the four sort words complete it, not four independent options sitting beside an unrelated switch. Confirmed genuinely textureless: no fill, no edge, no frame anywhere on any of the five, pure text hit-targets, colored to carry the grammar — the toggle in bone as the statement, the four sort words in teal as its choices. And a real correction to `TRACE-49`'s own numbers: those figures were origin-to-origin pitches, not gaps — the true visual spacing tightens to just 3px between the toggle and the first word, then widens progressively across the remaining three, a deliberate progressive spread rather than an even grid. The row stops well short of the right-hand rule rather than stretching to fill it, reading as left-weighted prose, not a justified toolbar. **One deliberate addition, more necessary here than anywhere else in the project:** an active-word marker neither game built — a sentence naming four equally-weighted words with none distinguished is actively misleading about which is actually in effect, so the currently active word shifts to the same bone the toggle already uses, reusing a meaning the source's own hover behavior already established rather than inventing a new one.

**Personal Notes, locked at `PT-1160`, a genuinely new system with no direct source precedent as a whole.** A second footer shortcut alongside the existing message-log one, both pushing onto the same navigation stack from `PT-1159`. Two distinct pieces, deliberately built from different precedent: **reading** someone else's looted notes reuses K2's real datapad popup (`TRACE-50`) — a small, compact modal rather than a full screen, kept in context rather than pulling the player away from wherever they were — but reframed from K2's confirm-shaped OK/Cancel into a single plain Close, since reading isn't a decision the way K2's original use of that shape implied. **Writing** your own notes uses NWN's real precedent instead (`TRACE-51`) — a genuinely wrapping, chrome-free scrolling text box, sized to match the Message Log screen rather than K2's small popup, since composing your own notes is a deliberate, sit-down moment rather than a quick glance. Explicitly not inheriting K2's fixed-authored-line text model, which only worked for short, hand-written quest text and breaks completely for something a player types freely. **Privacy, decided deliberately rather than inherited by default:** notes stay fully private, unreadable by any scripted content, matching NWN's own choice — chosen specifically because the feature is meant to be a small, personal, low-stakes moment for a player, and making campaign content aware of freely-typed text would require reliable text understanding neither game nor we have any real foundation for. **Naming, locked at `PT-1161`:** the item itself is titled "[Player Name]'s Datapad" — real identity attached to the object, since it's the exact thing that makes finding one on a fallen character mean something.

**Message log.** Four filters: Dialog, Feedback, and Combat all share one identical full-width list, one visible at a time — a filtered view of the same kind of content, not three different screens. Effects is structurally different from the other three, the only one that splits the content area into two columns, good effects on one side and bad on the other. Every row in the shared list is plain text, no icon, no timestamp, no visual distinction between a line of dialogue and a line of combat feedback in the source. **Active-state fix confirmed here too, locked at `PT-1159`.** `TRACE-47` found this same missing-selected-state defect on all four of these filters, completing the pattern already fixed for Store and Inventory — fifteen buttons across three screens, one systemic gap in how K2 built every filter bar it ever shipped, not three separate coincidences. Same fix applied: a real, visible active state from the `SPEC-01` primitives, confirmed working in an actual interactive build before locking.

**Real navigation stack, locked at `PT-1159`, replacing what had drifted into a stale "unresolved" note here.** `TRACE-48` corrected the earlier read: K2's message log has only one entry point at all, since `PT-1158` moved the fifth nav-bar slot to Party Selection — the Journal shortcut isn't one option among several anymore, it's the only door. Checked directly rather than assumed: Close always exits fully to gameplay, never back to Journal, confirmed by two independent shipped-data findings — the button is structurally identical to every other screen's generic Close, and the engine itself has no concept of a previous screen to return to at all. Built as real infrastructure rather than a one-off patch: a genuine navigation stack, so opening the log from Journal pushes it on top instead of replacing Journal, and Close reveals whatever's underneath rather than exiting outright. This also directly fixes Options' identical problem, where every sub-panel currently needs its own separate Close because the source never built real back-navigation either — one system serving both rather than two special cases.

**A standing principle, worth keeping for its own sake:** when the owner's memory of actual play and this project's source research disagree specifically about navigation or convenience, check whether a modern remaster explains the gap before treating either side as simply wrong. This exact case started as exactly that kind of disagreement, and checking rather than dismissing either side led directly to a real, worthwhile fix.

**Readability, deliberately improved over K2's own version, not copied faithfully.** Owner flagged directly that K2's actual log reads as a wall of identical, clashing lines nobody really wanted to read — confirming that the source data's total blindness to line type (a roll and a line of dialogue rendered identically) was a real usability problem, not just a curiosity. The fix uses only the palette already established below, nothing new introduced: bone, otherwise reserved for titles and selection, does double duty as the color for a speaker's name specifically, so `jimaya:` stands out from the rest of its own line the way a title already stands out elsewhere on the same screen. Combat lines, which have no speaker, stay as they were. Paired with more breathing room between distinct exchanges rather than uniform single-spacing throughout.

**Visual specification, texture-pass-ready.** Three colors and two fonts do nearly everything: `#1AB28C` teal-green for interactive text, `#CCCCB2` bone for titles and every highlight, `#0D5945` dark teal for every border, black background. Selection and hover are a pure color shift, not a texture swap — every highlighted state reuses the identical frame art and only changes which of the three colors it's drawn in, which means a texture pass genuinely cannot break how selection reads no matter how the surface art changes. One thing worth flagging before anyone touches the art: the horizontal divider rules on both screens aren't their own asset at all — they're a button's edge texture stretched flat, so redrawing that edge changes every divider on both screens along with it, whether intended or not. No icons anywhere in either screen — everything is text, a frame, or a stretched bar.

---

## 7a. Character creation — eleven screens, locked across `PT-1179`–`PT-1210`

**⚠⚠⚠ THE CURRENT ORDER — `PT-2752` (2026-10-15), chargen rebuilt 1:1 with K2. It supersedes every order below, and the older `PT-2470`/`PT-2471` stale notice it replaces.**

    BEFORE THE HUB   Entry (Quick / Custom / Premade) → Species → [Model, droids] → Class
    IN THE HUB       Gender/Voice → Portrait → Origin → Background → Attributes → Skills → Feats → [Powers, Force classes]
                     → Equipment → Name (with Story, in K2's name_p popup) → Play

- **No screen between Class and the hub** (`R-d`): the "SPECIES AND CLASS" confirmation is gone; Back from the hub returns to Class with the species kept.
- **Gender/Voice is the first hub step, before Portrait** (owner, `R-b`), so the portrait filter has the gender; the class screen shows the class only.
- **Portrait is its own step** (`PT-2751`), K2's `portcust_p`; it is no longer a stage of Identity.
- **Name is K2's `name_p` popup over the hub, with Random Name; Story is a second panel inside it** (`R-c`, `R-h`) — this supersedes `PT-1732`'s full-screen Name.
- **Quick Character** (`R-a`) runs Gender, Portrait, Name, Play, the rest filled from Recommended — built after Recommended works (`Y5`).
- **K2's own words wherever K2 has one** (`PT-2752`): OK (1580) for every affirmative button, Attributes (209), Remaining Points / Feats / Powers (210 / 32062 / 1074), Description (217), Choose your class (32160), Quick / Custom Character (239 / 240), Yes / No (128498 / 128497) on the re-open warning.
- **Lifestyle no longer exists** (`PT-1401`): it folded into the profession row. **"Backstory" is the internal key only** (`PT-1848`); the step reads Background.

**Select Premade Character, locked at `PT-1223`.** A single split screen: scrolling roster on the left with the highlighted character's description beneath it, full sheet on the right. **No View Sheet and no navigation** — choosing between premades is a comparison task, and comparing means watching the sheet change as you move between them.

**Senses render on the sheet too, per `PT-1238`** — a sense is a rollable ability with a range and often a DC, so a player who cannot see it on their own sheet cannot use it, and a GM reading a premade's sheet cannot adjudicate it. Present when the species has one, absent when it does not.

**The sheet runs in creation order** — identity, homeworld with its aptitude, upbringing, profession with its grant, lifestyle, languages, then abilities, then vitality/Force points/defence/saves, then the section panes. That ordering is not arbitrary: it reads as the account of how the character was assembled, so the sheet and the eleven steps can never disagree about what matters. **Every background field carries its label** — `Homeworld`, `Upbringing`, `Profession`, `Lifestyle` — since "Coruscant · Persuade" alone does not say what it is.

**Section buttons below the stats: Skills, Feats, Powers, Gear.** Powers appears only for a Force user; background is *not* a button, since it belongs with the always-relevant material. **The panes match their creation screens exactly, at smaller scale** — skills as the alphabetical aptitude-marked list, feats and powers as identical chain grids with arrows between tiers and rows stopping at their real depth. `PT-1224` corrects the feat grid to carry arrows, matching powers.

**All 25 character skills render, including untrained ones at 0** (`PT-1292`), in three states: amber with a diamond for aptitude, pale for a rank without it, dimmed for zero. What a character *left empty* is real information when comparing premades. **Force Points appear only for Force users**, absent rather than zeroed.

**Every region scrolls independently** — roster, description, stat block, section pane — so a package with thirty premades works without redesign.

**The entry screen, locked at `PT-1221`.** New Game opens a choice built on `qorcpnl_p`'s exact structure — two stacked option buttons with a description panel beneath that updates as each is highlighted, and a **single full-width Back** at the foot. **No Continue:** the source has only `BTN_BACK` here, because the option buttons *are* the commit and a separate confirm would add a click to a decision already made. The footer stays uniform in treatment — same height, border, radius and position as every other footer in the flow — while carrying one button rather than two.

Two additions the source had no need for: **the campaign package is named at the top**, since premade characters belong to a package and which one you are in determines what is on offer; and the premade option **states how many exist**, so the player knows whether that path is worth opening.

**Species and Class come BEFORE the hub, locked at `PT-1220`.** New Game offers **create a new character** or **play an existing one**; choosing to create opens the **Species screen with no strip at all**, then **Class**, and only then does the hub appear. This is KOTOR's own architecture restored rather than a departure — `custpnl_p`'s six steps are Portrait, Attributes, Skills, Feats, Name, Play, and **Class is not among them**, because `classsel_p` resolved it before the hub was ever drawn.

**The reason is structural, not cosmetic.** The strip cannot render honestly until it knows two things: whether this character is a droid, which changes Origin, Gender and Backstory into substituted or partial steps; and whether the class grants Force Powers, which decides whether step 9 exists at all. Choosing those two first means **the strip is correct the first time it draws** rather than reshaping itself under the player.

**⚠ SUPERSEDED BY `PT-2752`'s ORDER ABOVE.** ~~Nine steps in the hub, plus Play: Origin, Gender, Backstory, Abilities, Skills, Feats, Powers, Equipment, Identity.~~ For a droid, Powers is absent and the strip renumbers.

**A droid takes a fourth pre-hub screen, MODEL, locked at `PT-1222`** — between Species and Class, because chassis chosen at Species constrains which models are offered, and `DROID-MODELS-01` is organised by chassis. **Consequence: a droid has no Origin step at all.** Origin is Homeworld plus Upbringing; the model replaced homeworld and now resolves before the hub, and upbringing does not apply to a droid under `PT-962`. Nothing is left in the step, so it does not render — an improvement on `PT-1209`, which had it rendering half.

**The hub carries a header of checked chips** naming every pre-hub choice: species with its subrace or chassis, the model where there is one, and class. Three chips for a droid, two for an organic. The player can see what the strip was shaped by.

**On the Species screen, a droid's second-level pick reads "choose a chassis"**, not "choose a subrace" — the mechanism is `PT-1182`'s, the vocabulary is the droid's own. And the affirmative button reads **OK** (K2's 1580, `PT-2752`; it read Accept until then) on the pre-hub screens rather than naming the next one, since these are discrete screens rather than stages inside a step.

**⚠ HISTORY — the order in this paragraph is superseded by `PT-2752`'s above.** **Eleven steps, not thirteen** — `PT-1205` merged Homeworld with Upbringing into **Origin** and Profession with Lifestyle into **Backstory**, and `PT-1199` dropped Backstory from the old step 13. Order: Species, Origin, Gender, Backstory, Class, Ability Scores, Skill Points, Feats, Force Powers, Equipment, Name/Appearance.

**Every screen shares one shape** — a numbered step strip on the left, content panel to its right. No screen invents its own frame.

**And every screen wears the game's own frame, locked at `PT-1226`.** The owner's screenshots settled a styling question the `.gui` files could never answer. The house treatment across all creation and level-up screens: **two stacked bordered header bars** (`CHARACTER GENERATION` over the step name), **bordered rows rather than bare text**, **paired label-and-value readout bars** with the label left and value right, and a **three-button footer** — `CANCEL` / `OK` / `RECOMMENDED`. Everything sits inside a border; nothing floats.

**Amber marks the privileged member of a set**, teal marks the ordinary one — class skills against cross-class, priority attributes against standard. Confirmed at `TRACE-78` from a mixed level-up skills list where the header read `CROSS-CLASS SKILL` for a teal row.

**Spend controls appear and disappear by state, locked at `PT-1227`.** The **minus renders only above the floor** — nothing to sell back at zero, so nothing is drawn — and the **plus disappears at the cap** rather than greying out. Space for each is reserved so rows never shift. Confirmed from the owner's screenshots: an all-floor attribute screen shows plus only, a spent one shows both.

**A zero modifier renders as `-`, not `+0`** — source detail, easy to get wrong.

**Caps are real and stated in the panel.** Abilities cap at **18 at level 1**. Skills use `SKILLS-01`'s own rule: **aptitude gives level+3, without it half that** — so at level 1 an aptitude skill reaches 4 and a cross-class one reaches 2. Aptitude therefore does two things at once, halving the cost *and* doubling the ceiling, and the description panel names the cap and says when a skill is at it.

⚠ **`RECOMMENDED` is under review.** It exists in KOTOR because chargen is a one-shot commitment; ours is a revisitable hub with progressive unlock (`PT-1215`), so it may be redundant. Not yet decided.

**The strip carries four states, locked at `PT-1215`.** `PT-1100` established the hub-with-progressive-unlock structure but left the visual treatment open; this closes it.

    ✓  GREY disc     COMPLETED — revisitable
    n  teal disc      ENCOURAGED — the next step, and it pulses
    n  bone disc      CURRENT — the step being viewed
    🔒 dimmed disc    LOCKED — name still readable beside it
    12 amber disc     PLAY — the only non-teal entry, pulses when ready

**Named buttons with a separate circular numeral, at NWN's width.** An owner screenshot of `custpnl_p` rendered settled three things the files could not. **The numeral is a filled circle** beside the button, not inside it — so the padlock replaces the *numeral* and the step name stays readable even when locked. **Completed renders grey, not highlighted** — the finished step dims while unfinished ones stay teal, which is the opposite of what this doc first assumed. And **`Play` is a numbered step**, step 6 of 6 there, confirming `PT-1214` visually where `strref` 235 had only implied it.

**Width comes from NWN, not KOTOR, locked at `PT-1216`.** KOTOR's step buttons are 268px against a 800px screen — a third of the width, which crowds out the content panel. NWN's template names encode their own widths: `ctl_btn_pre_176` for step buttons and `ctl_btn_pre_118` for actions, so ~22% of screen. Ours follows NWN, since the ordering discipline is NWN's already.

**The padlock is deliberate over a dimmed number:** it states *why* a step can't be clicked rather than only that it can't. `TRACE-73` confirms NWN has no disabled animation at all, so nothing is being restored here — this is ours.

**The pulsing encouraged state is stolen directly from NWN**, which carries `SetEncouraged`, a `Gui_Anim_Button_Encouraged` animation, and `SetNextEncouragedButton` on the chargen panel — a third affordance beyond locked/unlocked where the hub *points at the next step* rather than only greying out the rest. It needs no new mechanism from us: the house pulse rule already means "this is waiting for your input," which is exactly what encouraged means, and hovering already cancels it.

**Re-lock warns, and this is a deliberate departure.** `TRACE-73` searched ~90,000 string-table entries and found no confirmation text, and the chargen panel carries no confirmation method — evidence NWN silently discards later choices when an earlier step changes. Ours does not. Changing Class at step 5 invalidates skill points already spent at step 7, and silently destroying a player's allocation is a worse failure than an extra dialog. The confirmation names what will be lost, not merely that something will be.

**Species, restyled and locked at `PT-1233`.** The first **hybrid** rather than a full reframe, and the pattern for the remaining browse screens. From the game: the **two stacked header bars** and the **`CANCEL` / `OK` footer**. From ours: the **holo at full size with its cycling arrows** — boxing it would have crowded the thing the screen exists to show — and the **subrace block** with its own label. The information panel is **boxed as the game does it, in our palette rather than the game's mint**.

**Three-tier colour hierarchy inside the panel:** dim olive lowercase section labels (`ability adjustments`, `skills`, `senses`, `trait`, `size / speed`, `about`), tan abbreviations, bone values — **all left-aligned inline**, nothing pushed to the right edge. **Ability adjustments render as plain signed modifiers** (`Int +2`, `Con −2`), corrected at `PT-1260`. An earlier arrow notation (`Str 10 → 12`) implied a base of 10 that does not exist — the base is **8** — and, worse, implied a sequence that does not happen: adjustments apply **after** generation, so a species modifier attaches to whatever the player bought, not to a starting value.

**The panel re-resolves entirely on a subrace or chassis pick.** Verified against real data across all seven: the three Aqualish subraces differ in ability, skills *and* trait — `Aquala` gains Constitution and **+4 Swim** but takes **−4 on anything built for fingers**, `Quara` gains Strength and Tusked Charge, `Ualaq` gains Dexterity and Stealth with no trait at all. The four droid chassis differ as sharply — `Battle` is the only one with **four** adjustments, `Remote` the only one at **Tiny** size with no hands. **The `trait` and `senses` sections render only when there is one.** **Senses added at `PT-1237`** after the owner caught their omission — they are rollable abilities with ranges and DCs, not flavour: `Bith` identify by scent at 10m on a DC 15 Wisdom check, `Aquala` have Low-Light Vision, `Miraluka` have no eyes at all and perceive through the Force. ⚠ **Open:** whether all 47 species records carry a senses line is unestablished.

**Species, `PT-1179`/`PT-1180`/`PT-1182`.** Holotable figure in house accent teal rather than a portrait or a reused 3D viewport — chosen over four alternatives because KOTOR already uses holo language and it sidesteps the model-asset dependency. Real stat panel from `SPECIES-CHAPTER-v2`, scrollable lore prose (**not** expand-on-tap — corrected at `PT-1180` against `PT-1166`'s Backstory-page precedent). **Subrace picker required for the seven multi-record species**: the screen does not resolve until the second-level pick is made, and switching subraces re-resolves every field. Portraits explicitly **not** here — they belong at step 11.

**Origin, `PT-1184`/`PT-1205`/`PT-1210`.** Galaxy-map presentation, since `TRACE-59` established the source's own map is a live model viewport with a summary panel. Confirmed worlds as quick-picks plus a genuine **open "other"** option for Regional and Diaspora bands — the Atlas's own notes say absence means *unknown, not absent*, so a closed list would misrepresent the data. World grants aptitude from a real four-skill menu ⚠ `PT-1396` (**+2 and aptitude**, per `WORLDS-MENUS-01`). **The two halves are asymmetric and the screen says so:** upbringing grants nothing at all, labelled as flavour only.

**Restyled at `PT-1234`, on `PT-1233`'s hybrid pattern.** Header bars and `CANCEL`/`OK` from the game; star field, planet viewport and upbringing list ours. **The world panel and the upbringing block are both boxed**, with dim olive lowercase section labels.

**World switching gained `‹ ›` arrows** beside the viewport, matching Species. The map still shows *where* a world sits, but the arrows do the moving — hunting small dots on a star field was the wrong interaction for a list of three.

**The skill row says what it is for.** It reads *"this world taught you one skill — you keep an aptitude in it"*, and names the consequence beneath the buttons: one point per rank instead of two, and a higher cap. Previously it read only `grants — choose one`, which stated the mechanic without saying what it bought.

**The open "other" option is a real third entry** with a dashed marker, per `PT-1183`. Selecting it correctly kills the skill row — you cannot take a skill from a world you have not named.

**Two stages inside one step, locked at `PT-1212`.** The world is chosen first on the map with its skill menu; confirming it **transitions the panel in place** into the upbringing menu rather than moving to a new screen. The chosen world and skill carry into the upbringing header, with a `◂ change` returning to stage one without leaving the step. A stage indicator sits top-right. This is the honest shape for a merged step — two decisions with a real dependency between them (the skill menu belongs to the world) presented in sequence, rather than two unrelated panels competing for one screen.

**Stage one is the locked galaxy-map screen unchanged, confirmed at `PT-1213`** — star field, planet model viewport, description in the terminal font, three-skill aptitude menu. The only alteration is its affirmative button, which reads **`Upbringing ▸`** rather than `Select`: the step is not finished when a world is chosen, and the button says where it goes rather than implying completion. Cancel keeps its position and weighting. Stage two returns via **`◂ change world`** in its header, and the world and skill chosen in stage one render there as a single confirmed line.

**Gender, restyled at `PT-1236` — header bars only.** The one screen that takes the header pair and **nothing else** from the frame. Gender is the smallest screen in the flow, two or three buttons and a sentence; two header bars plus a boxed description plus a footer would be more chrome than content, and boxing shrank the buttons from comfortable targets to small ones. **Ours keeps large buttons and an unboxed description.** The subtitle bar carries real state — `GENDER`, `VOICE`, or `STEP ABSENT`. **No entry popup:** owner ruling, and consistent with `PT-1235`'s rule that a popup earns its place by stating something non-obvious. Nothing here is non-obvious.

**Gender, `PT-1189`/`PT-1190`.** Four real branches: organic shows Gender; Assassin and Battle droids show **Voice** (masculine/feminine/neither); Astromech and Remote **have no step 3 at all** and the sidebar renumbers rather than showing a gap. `Neither` was kept over `No voice` deliberately — a fitted vocabulator that reads as neither is not silence, and silence is the state that never appears here.

**Backstory, restyled at `PT-1239` — and the strongest result of the pass.** Header bars from the game; everything else ours, with **every list entry as its own rounded box**. That is the change that made it work: tabs, list entries, offer boxes and footer all wear the same rounded treatment, so the screen speaks one visual language instead of mixing bordered rows with unbordered text.

**The two offers are rounded boxes too**, with the aptitude one in **amber** — the colour that marks a grant everywhere else in the flow. Beneath them, the note says *why* neither can be picked here: the choice resolves at Equipment, once the item's worth is visible beside the rest of your gear. Without that line, two options you cannot click reads as broken.

**Lifestyle's note states both facts** — it touches starting credits rather than aptitude, and a droid does not take one.

**Backstory, `PT-1198`/`PT-1205`/`PT-1206`.** Profession and Lifestyle as two tabs. Profession offers **item or aptitude** per `PT-695`, chosen here, with `PT-1200`'s forward-looking warning stated inline. Droids take a **Programming** instead (seventeen, `PROGRAMMINGS-01`) and no Lifestyle, so the step renders half.

**Equipment, restyled at `PT-1241` — the full hybrid, and the frame earns its place here more than anywhere.** Header bars, every region boxed, `CANCEL`/`OK` footer, stock and cart as **rounded option boxes**. The screen carries **three distinct regions** — the route toggle, the gear content, and the profession trade — and unboxed they ran together into one column of text. **The trade at the foot is a different decision from the gear above it** and must not read as part of the same block; boxing is what separates them.

**Equipment, `PT-1217`.** Step 10. The screen is a **fork, not a shopping list**: `STARTING-EQUIPMENT-01 §1` gives two player routes — take **Standard Gear** (the class array), or **Purchase Gear** — its value in credits, spent freely, keeping the change. Route 3, a campaign package imposing equipment, overrides both and replaces the screen rather than appearing on it. **Both routes renamed at owner ruling, `PT-1218`:** the rules document calls them *"The Assortment"* and *"The Purse"*, which are this project's own coinage and read as neither. The screen labels say what each route *does* — one is what you are issued, one is what you buy — and pair on a shared noun so the fork reads at a glance.

**Both routes state `PT-728`'s reasoning on screen:** standard gear is worth *more* than the credits, because it can hold items a purse would never prioritise — an Engineer's two Computer Spikes are 500cr of consumables alone. Credits buy freedom; the array buys value. Neither is strictly better, which is what makes it a choice rather than a calculation. The array itemises with its slot mapping, and names the five slots (`Implant`, `Head`, `Hands`, `Arms`, `Belt`) that **deliberately start empty** so profession grants and first-level buys have somewhere to go.

**Purchase Gear is the Store screen reduced to fit the step, locked at `PT-1219`** — same filter row (`All / Weapons / Armor / Misc`), same two-column shape, same `PT-1153` four-row readout repurposed as Credits / Spent / Remaining / Slots empty. Available on the left scrolls; chosen on the right is the cart. **Items you cannot afford render red and are unclickable** rather than permitting an overspend. **The catalogue is tier-1 only** — `STARTING-EQUIPMENT-01` is explicit that a starting array takes the entry-level item by definition, and the `Vibro Double-Blade` is tier 1 at 200cr against tier 2 at 3,585cr, so the gate is real rather than cosmetic.

**⚠ The commerce palette is deliberately NOT inherited here.** `PT-1152` made gold and bronze a real chromatic exception for the *world* store. This is a creation step, and every other step in the strip is teal — consistency within the flow beats inheriting an exception from a screen reached a different way. The exception stays with the world store, where it was earned.

**`Slots empty` is ours, not the source's**, and it exists to stop a player spending 325 credits and arriving at Identity with no boots.

**The profession's item-or-aptitude trade resolves here**, and this is where `PT-1200`'s obligation is discharged: choosing the aptitude shows *"Applies from level 2. Your skill points at step 7 are already spent at the old price."* **Backstory shows the offer; Equipment resolves it** — the same choice must not be live on two screens.

**Class, restyled at `PT-1240` — the full hybrid.** Header bars, both columns boxed, `CANCEL`/`OK` footer, and the list entries as **rounded option boxes** per `PT-1239`. The frame fits without argument here because the screen is already list-plus-detail, the shape it was built for. Boxing gives the six-item list a visible edge, which a bare column lacked.

**All six fields render**, which is `PT-1191`'s whole point: vitality die, skill points, feat rate, class-skill count, key abilities, Force status. `TRACE-60` found KOTOR authored a **fifteen-line stat block per class and displayed it in a two-line label** — the mechanics were written in full and the UI hid them. Sizing the container was the fix, not adding fields.

**Class, `PT-1192`.** NWN's shape sized properly — `TRACE-60` found KOTOR authored a full 15-line stat block per class and gave it a two-line label, so the fix is sizing the container, not adding fields. Alphabetical, never grouped by tier or Force access, so the ordering smuggles in no recommendation.

**Ability Scores, `PT-1197`, generation ruled at `PT-1260`** — all six start at **8**, a **30-point** budget, ladder of 1/2/3 per step, ceiling **18** at level 1. Droids excluded. Built on `abchrgen_p`'s real structure, the best-built panel in the source: separate bonus readout per row, minus/value/plus, live cost and remaining readouts. Priority abilities shown — the payoff for `PT-1098` moving Class ahead of this step. ⚠ **Assumes point buy; the generation mechanic is still unruled.**

**Every screen opens with a one-time explanatory popup, locked at `PT-1235`** — the browse screens too, not only the spend ones. Each carries its own glyph: a **question-mark figure** for attributes, a **hand** for skills, a **globe** for origin, a **standing figure** for species. Extended from spend screens at `PT-1230` — first entry only, never again. Each carries its own glyph: a **question-mark figure** for attributes, a **hand** for skills. These explain the mechanic rather than announcing anything, which is why they differ from the feat grant popup.

**And `RECOMMENDED` splits two ways.** Attributes and skills apply **silently**; feats and powers **announce with a popup**. Not arbitrary — `TRACE-79` found the two recommendation strings exist for feats and powers only. **The rule: a popup announces what you might not otherwise notice.** A feat is a named entry buried in an icon grid; an attribute number changes on the row you are already looking at.

**Skill Points, `PT-1201`.** Alphabetical scrolling list of all twenty-five — the source's eight-row template cannot hold them (`TRACE-66`). Aptitude marked per skill **with its sources named**, since several can grant it at once.

**Feats, `PT-1202`, restyled and sequenced at `PT-1228`.** A **three-column icon grid**, one chain per row, one tier per column, no text in the list at all. Red box means unselectable; a **held feat renders dimmed** and its chain arrow opens the next tier.

**The entry sequence is fixed:** arriving fires **"You have been granted the following feat(s) this level"**, listing each automatic grant with its icon. Dismissing it shows the plain screen. `RECOMMENDED` then does two things at once — **auto-selects and announces**, via **"The following feat(s) have been recommended."** Both popups are real source strings, not our invention.

**The action button toggles** `ADD FEAT` / `REMOVE FEAT`, with `REMAINING FEATS` dropping to 0 and every other feat's button greying while one is held. A selection is reversible in place. ⚠ **Open accuracy debt: cells are 85.7×56 in a 257×56 row with 4px padding, and the mockup does not match.**

**Force Powers, `PT-1204`, corrected at `PT-1231`.** Same three-column grid, same cell geometry — but **no arrows.** Feats have them; powers do not, confirmed from three owner screenshots. The reason is structural: a feat chain is a strict upgrade ladder where an arrow correctly says *this becomes that*, while powers **branch** — one power can gate two others, 25 carry two prerequisites at once, and depths run 1 to 4 unevenly. An arrow would misdescribe the data.

**`ADD POWER` reflects eligibility, not budget** — it stays greyed with a pick remaining if the highlighted power's prerequisite is unmet. ⚠ **Two independent colour channels:** icon artwork by alignment (`goodevil`), box border by selectability. Same accuracy debt as feats.

**Identity, restyled at `PT-1242` — the frame with generous space.** Header bars, one boxed region per stage, `CANCEL` footer. **The lesson here was padding, not structure.** Identity has the least content of any framed screen — a portrait or a name field — and the first attempt crowded both against their borders. Both stages now share one shape: **a prompt line, the thing itself with real room around it, and a note at the foot.** The portrait viewport is **84px** with the arrows spaced well clear; the name field is centered in an 18×22 padded box at larger type.

**Subtitle names the step, not the flow** — `PORTRAIT`, `NAME`, `YOUR STORY`, no `IDENTITY` prefix and no stage count.

**Identity gained a third stage at `PT-1243`: YOUR STORY.** It closes the question `PT-1199` left open — the prose backstory had no home once step 13 lost the name, and this is it. **A full rundown** sits above: portrait, name, species, class, all six abilities, then every flavour choice as a rounded chip. **Below it, a generated story assembled from exactly those choices** — `Coruscant` supplies the towers, `Orphan` supplies *"nobody came for him"*, `Acolyte` supplies the temple, `Sentinel` explains why he reads people before reaching for the blade.

**It is a real text field**, not a display — type, erase, select, scroll. **`Try another`** regenerates from the same inputs; **`Clear`** empties it and focuses the cursor. The status line tracks three states — *assembled from your choices*, *edited by you*, *empty* — so a blank field reads as deliberate rather than broken.

**⚠ Amended at `PT-1266`: the campaign reads the CHOICES, not the prose.** The story is assembled from Origin, upbringing, profession and lifestyle — all closed sets — so the hookable content is upstream of the sentences. **A player's edits change what they read, not what the campaign can hook**, and the screen should say so rather than imply otherwise. No source game parses player prose; a **named slot** (a mentor, an invented homeworld) is the safe way to get a player's own proper noun into generated text.

**Two stages** — now three. The `NAME ▸` button already says another stage follows.

**Two notes that earn their place:** *"Presets follow your species. The last slot takes an image of your own"*, and *"You can change this later. Nothing else on the sheet can"* — true, and worth saying to a player hesitating over a name at the final step.

**⚠ SUPERSEDED BY `PT-2751`/`PT-2752`:** Portrait is its own hub step (`portcust_p`), the portrait is chosen once and never changed later (`PT-2751` R4), and Name is `name_p`'s popup over the hub with Story as its second panel. Kept below as history. **Identity, `PT-1214`.** Step 11, renamed from Name/Appearance. **Two stages in one step**, the same pattern as Origin: the portrait is chosen first — cycling arrows either side of the portrait, matching `portcust_p`'s own `BTN_ARRL`/`BTN_ARRR` at 25×50 flanking a 90×90 portrait — with a preset strip and a **custom upload slot** per `PT-1180`'s NWN precedent. Accept moves to the name box, built to `name_p`'s real proportions: a small centred panel, 340×150, with a **full-width Random button** (`BTN_RANDOM`, real source behaviour) above equal-width footer buttons.

**The final button is not on this screen.** `custpnl_p` — KOTOR's real chargen hub — carries **six numbered steps**, and `BTN_STEPNAME6` uses `strref` 235, a string appearing nowhere else in the chargen suite, in its own half-width slot beside step 5. Every other footer reuses 1580/1581. So the source genuinely gives its final step a distinct label rather than another Accept. **Ours ends the Name popup with OK (1580, `PT-2752`) and puts Play on the hub**, matching that structure.

**A standing caution, `TRACE-69`/`TRACE-70`:** authored `.gui` colour is **intent, not output** — the engine repaints text at runtime, and the render condition is `pulsing OR hover OR selected`, so authored `PULSING: 0` does not mean nothing pulses. Treat every authored visual field as a default the engine may replace.

## 7b. Level-up — locked at `PT-1225`

> **⚠ CHANGED → `PT-2752` (owner, 2026-10-22, the latest decision): CLASS FIRST, ON ITS OWN PAGE.** The class is picked on the approved Class page titled "Level Up", before the hub; the hub (`maincg_p` with `leveluppnl_p`'s rows) carries six fixed rows: Attributes, Skills, Feats, Powers, Forms, Accept, with a row left empty when the level grants nothing, as K2 does. K2's grant popups (42258, 111635) replace the amber grant summary below. "A Class step at position 1" on the hub, below, is superseded.

**No new screens.** `TRACE-77` found there are no level-up variants of the ability, skill or feat panels — only `pwrlvlup_p` exists as level-up-specific. Attributes, Skills and Feats reuse `abchrgen_p`, `skchrgen_p` and `ftchrgen_p` **exactly**, which is why `leveluppnl_p`'s steps 1–3 carry chargen's own strrefs (209, 233, 232) while step 4 gets a new one. The strref reuse and the panel reuse are the same fact.

**And the asymmetry has a cause:** KOTOR has no Force class at level 1 — you begin a Soldier, Scout or Scoundrel and become a Jedi later — so Powers never appears in chargen and `pwrlvlup_p` is the game's only powers screen. **Ours differs**: Jedi Guardian and Consular are base classes, so our chargen needed a powers screen where KOTOR's did not. `PT-1204` built one from `pwrlvlup_p`, and this explains rather than merely justifies that call.

**So level-up reuses our four locked screens** — `PT-1197` Abilities, `PT-1201` Skills, `PT-1202` Feats, `PT-1204` Powers — with level-up budgets rather than creation budgets.

**Structure, from `TRACE-75`.** Level-up drops **two** steps from chargen's ends, Portrait and Name, and inserts Powers before the commit. The commit reads **Accept** (strref 1073) and is **not** visually distinguished — chargen gives `Play` a fill and level-up withholds one. **Back only, no cancel path.**

**Two additions, both marked as ours.** A **Class step at position 1**, because `MULTICLASS-01 §3` allows taking a level in any class at any level-up while K2 grants prestige class through a dialogue script (`a_pc_jedi.nss`) and has no class step in any of its 159 panels. Class must be first: it decides hit die, skill points, whether Feats renders and whether Powers exists. And a **grant summary on commit**, since `TRACE-76` established K2 announces nothing at all.

**Steps render only when the level grants them** — Attributes every fourth level, Feats on the class's own `featgain.2da` schedule (a Soldier nearly every level, a Consular roughly every third), Powers only for a Force class. **Accept stays locked until every step above is done**, the level-up equivalent of the strip's progressive unlock.

**Automatic grants are announced**, in an amber block kept separate from what the player chose. `_granted` columns carry the class level of each grant; `-1` is a sentinel meaning never, and is the dominant value.

## 7c. The in-game screens — restyled against real screenshots, from `PT-1249`

**All eight were locked at `PT-1152`–`PT-1168` before any screenshot existed**, from parsed geometry and `TRACE-42`'s audit alone. They largely held. `TRACE-80` supplied what the files could not.

**Three pieces of persistent furniture appear on every in-game screen**, and this is the change that matters most:

- **The shared navigation bar** — eight icons top right, identical position throughout, with the **active screen's icon rendering white** against teal. That active state is engine-applied; it does not exist in the panel files, which is why this project logged its absence across 42 buttons as a defect.
- **A title bar top left**, in its own box, naming the screen.
- **A persistent footer** — `CLOSE` bottom left, and bottom right the **portrait with name, class and level**, carrying a **red vitality edge** and the **level-up arrow badge** when a level is available.

**Character Sheet, locked at `PT-1249`. ⚠⚠⚠ "3D model" here is stale in its first two words, per the later `PT-1319`/`UI-ASSETS-01 §7`/`§0b` (no model, ever — see §0b) — confirmed by the actual build (`PT-2472`).** Portrait placeholder in a rounded viewport with the **curved light–dark alignment arc** beside it and **`Auto Level Up` / `Level Up` overlaid on the viewport itself**. Right column is a bordered stat table with **value and modifier in separate columns**, then `Vitality` and `Force` as current/max, `Defense` single, three saves, and `Experience` / `Needed` as a paired block at the foot.

**⚠ One deliberate departure:** ours shows `Force 24/24` where the source shows `0/0`. KOTOR's Jedi arrive later in the story, so a level-1 character has no Force pool. **Ours are base classes** — the row is live from level 1.

**Abilities, locked at `PT-1250`.** Nav bar, title bar and footer per `PT-1249`. A **tab strip** rather than buttons — `FILTER` in its own filled block at the left, then `SKILLS` / `POWERS` / `FEATS` sharing the rest, all sitting on a rule.

**⚠ All three tabs have DIFFERENT list layouts, and a different readout — or none:**

| Tab | List | Readout |
|---|---|---|
| **Skills** | icon in its own box **beside** a name box | `SKILL RANK` / `BONUS` / `TOTAL RANK`, **bonus in amber** |
| **Powers** | an **icon column with no names at all** | `BASE COST` / `ADJUSTMENT` / `COST PER USE`, **adjustment in amber** |
| **Feats** | the **chain grid with arrows**, held tiers teal and unheld red | **none** |

**Unlearned powers render as `?`** in dimmed teal, read `UNKNOWN FORCE POWER`, and show `--` in every readout row. The source's own line: *"Some Force Powers cannot be learned through normal means…"*

**This resolves what `TRACE-60` half-answered.** The three-row block is not one block relabelled across all three tabs — it is relabelled across **two**, and feats have none, because a feat has no numbers to report.

**Inventory, locked at `PT-1251`.** Nav bar, title bar and footer per `PT-1249`. A **seven-category filter strip** — `ALL / DATAPADS / WEAPONS / ARMOR / USEABLE / QUESTS / MISC` — as a tab strip on a rule, not wrapped buttons. Icon in its own box beside a name box, matching the Abilities skills tab.

**Two details taken from the source rather than invented:** `(Equipped)` is a **suffix on the item name**, not a separate badge or column; and **`CREDITS` is a label-value row in the lower right**, beneath the description, rather than a header stat.

**`USE ITEM` greys unless the selection is usable** — eligibility, not budget, the same rule as `ADD POWER` at `PT-1231`.

⚠ **`PT-1155`'s sort control is not visible in the source screenshot** and has been left out pending confirmation. It may sit off-screen, or it may be ours.

**Equip, locked at `PT-1252`.** Nav bar, title bar and footer per `PT-1249`. **Two states, and the footer tells you which one you are in.**

**Slot view** — the item list for the current slot on the left, the **lattice** on the right with `DEF`, the attack and damage bars, and `SWITCH WEAPONS` spanning beneath. Subtitle names the slot. Footer reads `CLOSE`.

**Clicking a slot** replaces the lattice with the highlighted item's **full description**, drops the subtitle, and swaps the footer to `CANCEL` / `OK`. Moving between items updates the description without leaving the state. `OK` commits; `CANCEL` returns unchanged.

**The lattice uses `PT-1156`'s arrangement**, which is a real **3×5 grid with empty cells** rather than a packed block:

```
implant   head    hands
right arm body    left arm
weapon R  BELT    weapon L     ← primary config flanks Belt
   ·      BOOTS      ·         ← alone beneath, with worn items
weapon R  ·       weapon L     ← secondary config, own row
```

**⚠⚠⚠ CORRECTED AT `PT-2503` — twelve slots, not eleven; the diagram above was always right and this line was stale.** Boots has **no source precedent at all** — KOTOR's data has no foot slot (`ITEMS-08`, `PT-690`) — which is why it sits with Belt rather than in the weapon block, and is exactly why the count runs one higher than the source's own layout ever needed.

**An equipped slot shows the item's own icon; an empty one shows a dimmed placeholder** of what belongs there. `PT-1156`'s reasoning: an outlined box alone never tells a first-time player what a slot is for.

**Journal, Messages and Personal Notes, locked at `PT-1253`.** One family reached from one screen: the journal footer carries `MESSAGES LOG` and `NOTES`, each returning by `◂ JOURNAL`. Nav bar, title bar and footer per `PT-1249`.

**The sort row is one grammatical sentence**, not five buttons — *"Active quests by time / name / planet"* — with the active word in bone. Confirmed against the source screenshot at `TRACE-80`, vindicating a correction `PT-1160` made from file evidence alone. **`Planet` is a sort key, not a folder.**

**Messages** carries the five-part filter strip (`FILTER / DIALOG / FEEDBACK / COMBAT / EFFECTS`), one scrolling speaker-prefixed pane, with **system lines dimmed** against dialogue.

**Personal Notes** is `PT-1160`'s new system: a **chrome-free wrapping text box** on NWN's precedent, explicitly not KOTOR's fixed-authored-line datapad model, which only ever worked for short quest text. **Notes are fully private — no scripted content can read them**, chosen because the feature is a small personal moment and because reliable reaction to freely typed text has no foundation in either source game.

**Party Selection, locked at `PT-1254` — and the first screen where the source's shape was rejected.** KOTOR arranges **eight slots in a ring** with a character preview inside it. Ours is a **roster list**, in the game's frame.

**Two reasons the ring loses.** Position in it **carries no meaning** — slot 3 is not better than slot 7, they are eight places for eight companions. And it works *only because* KOTOR's roster caps at exactly eight; a campaign package shipping nine has nowhere to put the ninth.

**The list shows who is available alongside who is in**, with an `IN FIELD` marker, and scales to whatever a package supplies. The action button toggles membership and reads `PARTY IS FULL` when the cap is reached, with the count turning amber.

⚠ **The ring's real advantage is conceded rather than dismissed:** it makes a party feel like a formation instead of a checklist, which matters more than it sounds in a party-based game. Rejected on scaling, not on taste.

**Options, first pass at `PT-1255` — the screen that could not be copied.** KOTOR's list is a **video game's** options; ours is not a video game. Four entries replaced, two kept, two new, and two dropped entirely.

| Source | Ours | Why |
|---|---|---|
| `Gameplay` | **Table Rules** | difficulty, death handling, rest pacing — a **GM's calls, campaign-scoped**, not a difficulty slider |
| `Auto-Pause` | **Turn Pacing** | the concern is a **waiting table**, not a distracted player |
| `Graphics` | **Display** | theme, text size, motion — **nothing 3D to configure** |
| `Exit Game` | **Leave Session** | you leave a session, not a game |
| `Feedback` | **Rolls & Feedback** | kept — a tabletop app should be able to **show its working**. **⚠ Carries `inspect a check` (`PT-1326`), default OFF** |
| `Sound` | `Sound` | kept |
| — | **Session** | new — who is here, and whether it is publicly listed (`PT-1144`) |
| — | **Account** | new — sign-in, friends, sync |

**`Save Game` and `Load Game` stay**, at owner ruling — the question `PT-1255` raised is answered. Host-is-server does not remove the need for a player-visible save.

**This is a first pass, not a lock.** `PT-1140` has flagged a real Settings screen as undesigned since the first main menu mockup, and `PT-1148` deliberately left the broader pregame-settings category unscoped — which of these are universal, per-campaign or per-session is still unknown.

**Store, first pass at `PT-1256`.** Built to **K2's structure**, not K1's — the two differ substantially and an early screenshot was K1's. **Commerce palette in gold and bronze**, `PT-1152`'s chromatic exception, confirmed against the source.

**The title and the action button read one string** — both say `BUY ITEM`, or both `SELL ITEM`. In `store_p.gui`, `LBL_BUYSELL` and `BTN_Accept` share `strref` 32132, so they are physically incapable of disagreeing. `PT-1153` adopted this as a **bound relationship**; it survives here.

**Two lists stack at identical coordinates and swap** (`LB_INVITEMS` and `LB_SHOPITEMS`, both at 86,134) — the stack-and-swap pattern from the crafting family.

**⚠ One deliberate departure, reasoning corrected at `PT-2548`:** the source's third button is `EXAMINE`, which strref-resolves to "Show Sell List" — both K1 and K2 ship a real, labeled in-panel mode-switch toggle at that button (confirmed directly against `store_p.gui` in both games). Ours replaces "Examine" with the clearer `SHOW SELL LIST` / `SHOW BUY LIST` wording — not supplying a control the source lacked, since it already had one, but improving on the label. The two labels move together and stay opposite, so the mode is always readable from either button.

**Filter is spaced buttons between two rules**, `FILTER` as a label at the far left — not a contiguous tab strip. **Readout is four plain label-value lines**: `Cost`, `Credits`, `Stock`, `On Hand`.

**The shell is locked whole at `PT-1257`.** Seven screens on one shared navigation bar — `EQUIP`, `INVENTORY`, `CHARACTER`, `ABILITIES`, `PARTY`, `JOURNAL`, `OPTIONS` — with Journal branching to Messages and Personal Notes, and Equip carrying its two states.

**⚠ The map is NOT one of them.** Removed at owner ruling: **the grid carries the map**, so a separate map screen would duplicate it. The nav bar is seven icons, not eight.

**Store stays outside the bar**, per `PT-1152` — it is a **sealed modal**, reached from a merchant rather than from navigation, and a player in a shop cannot wander into their journal.

**State is shared, not per-screen.** Equipping body armour under `Equip` changes `Defense` on the `Character` sheet; party membership set in `Party` holds everywhere. The screens are views onto one character record (`CHARACTER-RECORD-01`), not seven independent panels.

## 7d. Deferred — real, scoped, and not being worked

**These are not open questions. They are decided-to-wait**, recorded here so they stop appearing on active lists (`PT-1261`).

- **⚠ THE PACKAGE SCHEMA** (`PT-1248`) — the contract where the Builder and the app meet. **Deferred at owner ruling: it belongs to a much larger project not yet started.** Eight locked screens reference a package; none is blocked from being built, because the schema is a serialisation question rather than a UI one.
- **⚠ SETTINGS SCOPE** (`PT-1140`, `PT-1148`) — which settings are universal, per-campaign or per-session. **Deferred at owner ruling.** Options is filed as a first pass at `PT-1255` and stays that way until this is answered; `SHELL-FLOW-MAP-01 §6` says so too.

- **THE QUICKBAR** (`PT-1264`) — NWN's separate player-filled quickbar, whether we want one at all. **Deferred at owner ruling, leaning no.** The reason it cannot be settled yet: the **normal in-game UI a player sees is still developing**, and a quickbar is an answer to a question about that surface. Decide it once the play view is further along, not before.
- **⚠ THE MINIMAP is CLOSED, not deferred** (`PT-1264`) — owner ruling: **the grid is a major view, so a minimap is not necessary for our product.** This also removes the sidebar left-edge collision that was carried as an open question, since there is nothing to collide with. **Do not re-open it as a UI question**; it would only return if the grid stopped being a primary view.

- **⚠ THE MAP AND GRID VIEW** (`PT-1257`) — the play surface itself. **Deferred at owner ruling.** The one screen a player would hit that is undesigned; everything else in the shell is locked.
- **CROSS-CAMPAIGN STATE CARRY** (`PT-1267`) — **⚠ four decisions now locked at `PT-1276`**, so this is no longer a blank design question. See that ruling before starting.
- ~~**CROSS-CAMPAIGN STATE CARRY**~~ *(original entry, superseded above)* (`PT-1267`) — **queued as the next major piece, not deferred.** Saves record quest conclusions and decisions so a later campaign can determine the state of things at that point *because of them* — Mass Effect's model, more ambitiously. **Substantial prior thinking already exists in `rules/CANON-01-v2`**: three canon layers, per-fact package policy, `requires` as a predicate, invalidation, load-time validation, one ledger per save-chain, and a multi-save conflict rule at `§4.2`. **Start there, not from scratch.**

**Anything moved here must name who deferred it and why.** A deferred item with no reason is an open question wearing a disguise.

## 8. Open questions carried forward

- **⚠ THE PACKAGE SCHEMA — what a campaign package *is* as data.** Not written, and it is **the contract where the Builder and the app meet**: the Builder's entire output and the app's entire input are the same artefact, and nothing specifies it. Everything downstream depends on it — Console Home lists packages (`PT-1146`), the Package Main Menu opens one (`PT-1101`), premade characters live inside one (`PT-1223`), `CHARACTER-RECORD-01` carries a `package` field pointing at one, and `PT-1203`'s author-created feats and powers would be stored in one. **Larger and more load-bearing than `CHARACTER-RECORD-01` was.** Flagged at `PT-1248`.


- ~~How do players connect with others "around the world"~~ **Closed at `PT-1144`, see `§6`: host-is-server architecture, local-first friends and history, automatic friend capture, one toggle unifying private and public listing, and a genuine invite code.**
- Loading-screen and concept-art triggers — deferred specifically pending owner-provided modded reference files, not just K2's base implementation, so the full picture can be checked at once rather than designing against the base game and redoing it once the mod material is available.
- ~~The journal-to-log shortcut's one-way asymmetry — keep or fix, not decided~~ **Closed at `PT-1129`: no longer load-bearing. The persistent navigation bar in `§2` already gives equal one-click access to both, so the shortcut is a pure convenience either way, never a fix for something missing.**
- ~~What information actually belongs on a sidebar portrait beyond vitality and Force pools~~ **Closed at `PT-1132`, see `§3`: seven signals confirmed from source plus name, class, level, and XP added deliberately from Del Arroz's reference. Enemy portraits remain a separate open question, not yet designed.**
- Whether to build a real animated background scene layer at all, of which K2's confirmed-original mist (`PT-1119`) would be one instance — genuinely bigger than the effect itself, since it means committing to live scene art rather than the current flat placeholder. Deliberately parked behind Solo Mode and the rest of the current agenda.
- **A full combat-code audit, logged at `PT-1121`, deliberately not started now.** Every prior combat pass answered a specific question asked in advance; nobody has read the source games' combat code exhaustively looking for gaps nobody thought to ask about. One confirmed while logging this: `PT-1108` locked action-first-then-target as the flow, `PT-1110` separately lets a player select a grid token directly, and nothing says what tapping an enemy *before* picking an action actually does — found by cross-checking two already-locked rulings against each other, not by asking about it directly, which is exactly the method this future audit would apply systematically rather than by accident.
- ~~Combat-side party control, flagged in `PT-1136` but never formally tracked until now~~ **Closed at `PT-1143`, see `§3`: full manual default, with hands-off and auto-battling available via the sidebar cycle button, K2's five presets as the auto-battling behavior set, chosen from the Character Sheet.**
- **A real Settings screen, never actually designed — flagged at `PT-1140`.** We've referenced an Options button since the very first main menu pass, but nothing has ever specified what's actually inside it as a real, laid-out screen. **⚠⚠⚠ CORRECTED AT `PT-2523` — the companion AI control preset picker is NOT a Settings occupant.** `PT-1143` itself places it on the Character Sheet specifically because per-companion scoping comes free from that screen's own existing context — this line previously, incorrectly, restated it as belonging here too, contradicting the very ruling it cited. Confirmed occupants: the colour theme toggle (`§0b`, currently deferred pending a real rearchitecture — `PT-2523`), and whatever else naturally belongs here. Worth its own real design pass rather than continuing to add occupants to a screen that doesn't formally exist yet.
- **A broader "pregame settings" category, flagged at `PT-1148`, deliberately not fully scoped.** The consumable resource-sharing setting (`§1`) is its first confirmed occupant — a choice made once before a campaign begins rather than fixed globally. Which future settings end up universal to single-player and multiplayer versus specific to one isn't known yet; scoped out incrementally as more surface naturally, the same growing-occupant-list approach already used for the Settings screen above.

---

## 9. Process, as agreed

1. This document — the outline, built by us, first pass.
2. A Claude Code exploration pass — what actually exists in the reference engines for GUI assets and music trigger systems, and what's extractable versus what needs rebuilding from scratch.
3. Possibly Claude Design, for early visual mockups of the console home and package main menu, once the exploration pass says what's feasible to lift directly versus what needs original design.
