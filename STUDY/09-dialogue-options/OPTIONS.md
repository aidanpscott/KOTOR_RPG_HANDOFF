# STUDY 09 — PRESENTING CONVERSATIONAL OPTIONS

*KOTOR's player replies against Daggerfall's topic system. Narrower than batch 5
and about the **player's side** only.*

---

## 0 · Method and scope

**KOTOR.** Every DLG in both games — 1,167 K1 and 1,159 K2 — with every player
reply's text resolved through that game's TLK. `.mod` files excluded (batch 4:
runtime artifacts).

**Daggerfall.** The classic install's `ARENA2` data, and `TalkManager.cs` (3,736
lines) and `DaggerfallTalkWindow.cs` (1,617 lines) from the Daggerfall Unity
reimplementation, which is **MIT-licensed** — read and described, not
reproduced.

**⚠ The Daggerfall claims are of two kinds and are marked as such.** Data facts
come from the shipped install. **Mechanism** facts come from the
reimplementation, which is a faithful re-creation and not the original binary —
where DFU annotates a difference from classic, that annotation is quoted.

**Not checked:** neither game was run. Nothing here is observed behaviour.

---

## 1 · ⚠ KOTOR's reply structure

Batch 5 covered nodes and gated links. The reply itself:

**A player reply carries 26 fields in K1 and 46 in K2** — the same set as a
speaker node minus `Speaker`, plus `EntriesList`. Text, voice, a script,
animation, camera, fade, a quest update. **A reply is not a choice with text
attached; it is a full authored beat that happens to be selectable.**

### The bracket convention is authored into the string

**There is no field that produces a bracket.** The `[Persuade]` marker is
literal text at the start of the TLK entry. Searched every reply field in both
games: no prefix, tag, marker, skill-id or gate-label field exists.

```
                                    K1              K2
player replies                   27,465          28,509
  with resolvable text           11,284          14,815
  ⚠ carrying a [bracket]          1,133 (10.0%)   1,033 (7.0%)
  distinct prefix strings           119              93
```

### ⚠ The bracket and the gate are independent

```
                              K1        K2
gated AND bracketed          425       571
bracketed but NOT gated      708       462
gated but NOT bracketed    1,528     2,249
```

**In K1, 62% of bracketed replies have no gate on them at all**, and **1,528
gated replies carry no bracket**. The marker is a writing convention applied by
hand, and it agrees with the mechanic less than half the time in either
direction.

### The full prefix vocabulary

**K1 — 119 distinct, used more than once:**

```
540  [Computer]              6  [Abort.]                3  [Attack the tach.]
198  [Persuade]              6  [Proceed.]              3  [Leave.]
114  [Force Persuade]        4  [Play Pazaak Tutorial]  3  [Use the ICE breaker]
 73  [Lie]                   4  [Interrupt.]            2  [Force Choke]
 36  [Persuade/Lie]          4  [Allow him to continue.] 2  [more]
 12  [Computer Skill]        3  [Don't speak to her.]   2  [Leave quietly]
  6  [Leave it alone.]       3  [Don't speak to him.]   2  [Leave]
                             3  [Leave the tach alone.]
   + 8 more scenery-specific pairs, + 90 prefixes used EXACTLY ONCE
```

**K2 — 93 distinct, used more than once:**

```
243  [Computer]             25  [Demolitions]           6  [Security]
224  [Persuade]             23  [Wisdom]                5  [Sonic Sensor]
 89  [Awareness]            22  [Persuade/Lie]          5  [Intimidate]
 83  [Repair]               13  [Treat Injury]          4  [Influence]
 70  [Force Persuade]        9  [Persuade/Intimidate]   4  [Stay here.]
 53  [Lie]                   6  [Learn about…] ×2       4  [Ask quay]
 32  [Intelligence]          4  [Leave the workbench…]  4  [Give 5 credits]
```

**Three different things share one visual channel.** Genuine skill gates
(`[Persuade]`, `[Repair]`, `[Demolitions]`); stage directions with no mechanic
at all (`[Leave.]`, `[Proceed.]`, `[Don't speak to her.]`); and outright
notifications (`[T3-M4 has joined your party.]`). A player cannot tell from the
bracket which they are looking at.

**K2 tightened it substantially.** K1's list is 540 `[Computer]` and little
else systematic; K2 adds `[Awareness]`, `[Repair]`, `[Demolitions]`,
`[Treat Injury]`, `[Security]`, `[Intelligence]`, `[Wisdom]` — attribute and
skill names used consistently. **The convention got closer to a system without
ever becoming one.**

### `[Success]` / `[Failure]` is not a reply convention

Searched both entire string tables: `[success]`/`[failure]` variants appear
**1,264 times in K1 and 831 in K2** — but **zero of them as a reply prefix**.
They belong to the computer-terminal and system-feedback channel
(`[SUCCESS] ELEVATOR OPEN`), which `LIVE-STATE.md` found in the save's dialogue
log. **Skill-check outcome is not surfaced on the player's option at all.**

### Most replies are not options

```
                            K1              K2
has text                 11,284 (41%)   15,137 (53%)
NO strref at all         16,179 (59%)   13,257 (46%)
   of which terminal      3,565          2,756
```

**Over half of K1's `ReplyList` entries have no text.** They are silent
transitions — continue-nodes and end-nodes that exist to route the graph. The
"player reply" list is mostly plumbing.

---

## 2 · Ordering

**There is no ordering field.** Searched every reply field and every link field
in both games. The only index-shaped fields are `Index` (the link's target
pointer) and `PlotIndex` (a quest reference). K2 adds eighteen gate fields and
**no** position, priority, weight or sort field.

**So presentation order is the array order of `RepliesList` on the speaker
node** — the order the writer typed them.

**Do hidden replies hold a slot?** **They cannot.** There is no position field
to hold, so a filtered list has no way to leave a gap — the list must close up.
*This is inference from the absence of a mechanism rather than observed
behaviour; I did not run either game.*

---

## 3 · ⚠ Daggerfall's topic system

**There is no dialogue tree, and there is no authored topic list either.**
**Topics are assembled at runtime from world state.**

The assembly entry points are explicit: `AssembleTopicLists`, and one builder
per list — `AssembleTopiclistTellMeAbout`, `AssembleTopicListLocation`,
`AssembleTopicListPerson`, `AssembleTopicListThing`.

### The shape

**Two things the player picks, then a category, then a subject.**

```
TalkOption      TellMeAbout · WhereIs                        (2)
TalkCategory    Location · People · Things · Work            (4, under WhereIs)
four lists      listTopicTellMeAbout · listTopicLocation
                listTopicPerson · listTopicThing
```

**It nests, and the nesting is explicit in the data model.** `ListItemType` has
three values: `Item`, `ItemGroup` (a group containing other items), and
`NavigationBack` — described in the source as *"A special item to navigate out
of group items ('Previous list')"*. So the list is a **two-level tree with a
back entry rendered as a list row**.

`QuestionType` enumerates twelve kinds of question — `News`, `WhereAmI`,
`OrganizationInfo`, `Work`, `LocalBuilding`, `Regional`, `Person`, `Thing`,
`QuestLocation`, `QuestPerson`, `QuestItem`, `NoQuestion`.

`KeySubjectType` says what a topic can be *about* — `Building`, `Person`,
`Thing`, `Work`, `QuestTopic`, `Organization`.

### ⚠ Global pool, per-NPC filter — not per-NPC assembly

`NPCKnowledgeAboutItem` is **tri-state**: `NotSet`, `DoesNotKnowAboutItem`,
`KnowsAboutItem`.

That is the answer to the brief's question. The topic *pool* is assembled from
the world — the buildings in this location, the people known, the factions, the
active quest resources. **Whether a given NPC can answer is a per-NPC flag on a
shared pool**, and "does not know" is a distinct state from "not yet
determined".

### ⚠ Asking changes what is available

Three mechanisms, all in the data model:

- **Quests inject topics.** `AddQuestTopicWithInfoAndRumors` adds a quest's
  locations, persons and items to `Tell me about` as the quest runs.
- **Topics can be hidden.** Quest resources carry `hasEntryInTellMeAbout`,
  described in the source as controlling whether a topic is *"hidden by dialog
  link command"*.
- **Topics can reveal topics.** A quest resource carries
  `dialogLinkedLocations` — *"list of location quest resources dialog-linked to
  this quest resource"*. Asking about one thing exposes another.

Separately, `RumorType` distinguishes `CommonRumor`, `QuestProgressRumor` and
`QuestRumorMill` — a second channel that is not topic-driven at all.

### How many topics

**There is no fixed number, and that is the design.** The list is a function of
where you are and what you are doing. Bounds from shipped data:

- **`FACTION.TXT` carries 366 named factions**, the pool for
  `OrganizationInfo`.
- **`Where is → Location`** draws from the buildings present in the current
  location, and Daggerfall's building type enum runs to ~20 kinds across
  thousands of generated settlements.
- **`Tell me about`** has exactly **two fixed entries** — *Any news* and *Where
  am I* — and everything else is quest- or faction-derived.

### ⚠ One whole category has never worked

`Where is → Things` is annotated in the reimplementation as *"Not used … Not
implemented in classic either"* and *"Never reached since there are no 'where
is'-type questions for things in classic."* **A category button that has shipped
non-functional in the original and in its faithful re-creation.**

---

## 4 · What the player sees

From the UI layer.

**A scrolling list box, browsed.** `listboxTopic` with a `VerticalScrollBar`.
The source's own constants: **~13 topics visible at once**, and
**`maxNumCharactersOfTopicShown = 20`** — twenty characters per label.

**No search. No filter. No typing.** Searched the whole talk window for a text
input, filter or search field: nothing. (The only `filter` hits are texture
filter modes.)

**Unavailable categories are greyed, not hidden.** There are dedicated
`GrayedOut` and `Highlighted` textures for both `TellMeAbout` and `WhereIs`, so
the player sees a category exists and is currently closed to them.

**A tone axis, orthogonal to the topic.** `TalkTone` is `Polite` / `Normal` /
`Blunt` — chosen separately from what you ask, and feeding a per-session
reaction score with thresholds at 0 (neutral), 10 (like) and 30 (very like).
*DFU notes its Etiquette-skill modifier as an "improvement over classic"; the
three-tone selector itself is classic.*

**No evidence of recency or grouping in presentation** beyond the category tree
itself. Ordering within a list was not established — I did not trace the sort.

---

## 5 · ⚠ The comparison

Neither is a good model for what we are building. Both are instructive about
*why*.

### What KOTOR got right

**Every option is prose in the player's voice.** You read the sentence you are
about to say. That is the single strongest thing either game does, and it is why
KOTOR conversations are remembered and Daggerfall's are not.

**A gated option is invisible, so the list is always plausible.** You never see
a locked door you cannot open. The cost is that you never learn what you missed
— which is a design position, not an oversight.

**The option carries its own consequence.** Script, quest update, camera, XP —
all on the reply. One place to look.

### What KOTOR got wrong

**The bracket is a lie in both directions.** 708 K1 replies are marked and
ungated; 1,528 are gated and unmarked. **The player learns a visual tell that is
wrong more often than right.** And because the bracket is typed into a
translatable string, it cannot be checked, cannot be restyled, and cannot be
localised without a translator understanding the convention.

**One channel, three meanings.** Skill gates, stage directions and party
notifications all wear the same brackets. 119 distinct prefixes in K1, 90 of
them used once.

**Nothing about the check reaches the player.** No difficulty, no odds, no
outcome marker. `[Persuade]` tells you a skill is involved and nothing else.

**Order is whatever the writer typed**, with no field to reason about it.

### What Daggerfall got right

**Topics are assembled from world state, so an NPC can be asked about anything
the world knows without anyone authoring that NPC.** This is the correct model
for unauthored NPCs and it is exactly our problem.

**Per-entity knowledge is a real, tri-state filter.** "This person does not know"
is a distinct answer from "there is nothing to know", and the distinction is in
the data. **That is the mechanism KOTOR's bracket should have been.**

**The topic set grows with the fiction.** Quests inject subjects, and asking
about one thing can expose another.

**Tone is a separate axis from subject.** One control for *what*, one for
*how* — cheap, and it makes the same topic list carry characterisation.

### What Daggerfall got wrong

**Twenty characters and thirteen rows for a list that grows without bound.** The
interface is sized for a menu and the content is sized for a world. There is no
search, no filter, and no typing.

**You never say anything.** Selecting a topic is a database query, not an
utterance. Nothing is in the player's voice, which is why the system reads as an
index rather than a conversation.

**A category has shipped broken since 1996** — `Where is → Things`, non-functional
in the original and in the re-creation, still occupying a button.

### For a typed-primary interface with topics as prompts

Three things follow directly.

**Daggerfall's assembly model is the right spine and its interface is the
warning.** Assembling subjects from world state is what makes an unauthored NPC
answerable at all. But the moment that list is the *only* way in, it has to be
complete, and a complete list is unusable — twenty characters, thirteen rows.
**Typed input is what makes the list allowed to be incomplete**, which is the
argument for our shape. The list stops being a constraint and becomes a hint,
and a hint may be short.

**KOTOR's bracket is the exact failure mode a prompt list would reproduce.** If
a prompt is shown and the NPC turns out not to know, we have built the
`[Persuade]`-on-an-ungated-line problem with a bigger surface. **Daggerfall's
tri-state knowledge flag is the fix, and it is cheap** — a prompt should only
appear if the entity can actually answer it.

**And keep the player's voice.** KOTOR's authored replies are the one thing here
worth preserving wholesale. For authored beats, write the sentence. For
unauthored ones, the typed input *is* the player's voice — which means the
prompt list should read as **subjects**, not as sentences, so it never competes
with what the player typed for being "the real line".

---

## 6 · What I did not check

- **Neither game was run.** No observed behaviour. The claim that a hidden reply
  cannot hold a slot is inferred from the absence of a position field.
- **Ordering within a Daggerfall topic list** — I found no sort, but did not
  trace the list-building code far enough to say there is none.
- **Whether classic Daggerfall's binary matches the reimplementation** on any
  mechanism claim. Where DFU annotates a divergence I quoted it; elsewhere I am
  trusting a faithful re-creation and saying so.
- **KOTOR's `[Computer]` prefix against the terminal system** — 540 K1 uses is
  by far the largest group, and whether those replies are gated by the Computer
  Use skill or by spike inventory was not traced.
- **The 90 K1 single-use prefixes** were counted, not read individually.
- **Daggerfall's answer text** — how a topic resolves to a reply, and the
  `%`-macro layer that fills it. That is the earlier free-text study's territory.

---
---

# ⚠ ADDENDUM — MARKING A LINE AT THE MOMENT IT FIRES

*Added after a ruling that typed text meaning an authored reply **counts as
picking it** — the branch fires, the check runs, the player's words are shown.
So the question sharpened: **when the player typed the line, what is there to
mark?** In both source games the reply was on screen before it was chosen; a
typed line has no such object until after it resolves.*

**Short answer: three commit-time mechanisms exist across the two games, and one
of them is exactly the shape a typed line needs — because it never needed an
object.**

---

## 1 · ⚠ K2 plays a stinger when a morally-weighted reply commits

`guisounds.2da` — the **UI sound** table — carries 17 rows in K1 and **19 in
K2**. The two K2 additions:

```
DarkSide     mus_s_darkshort
LightSide    mus_s_lightshort
```

**The assets exist in K2's BIF *and* on the filesystem, and do not exist in K1
in either place.** So K2 added the sounds and the table rows together; this is a
sequel addition, not an inherited row.

**And alignment shifts fire overwhelmingly from the player's own line:**

```
alignment-script firings on dialogue nodes
             total    on PLAYER replies    on speaker lines
   K1          365          275 (75%)           90
   K2          631          525 (83%)          106

K2's top scripts: a_givedark 201 · a_givelight 155 · a_darksml 121 ·
                  a_lightsml 81 · a_lightmed 38 · a_darkmed 35
```

So the sequence is: the player's reply commits → its `Script` fires
`a_givedark` → the engine adjusts alignment (`adddarkside` / `addlightside`,
literals present in both binaries) → **K2 plays a short musical cue.**

**⚠ Note where those rows live.** Not in `ambientmusic.2da`, where the stingers
of batch 6 live. In `guisounds.2da`, beside `Quest_New_Notify`,
`Quest_Complete_Notify` and `Level_Up_Notify`. **K2 classified an alignment
shift as a UI notification** — the same category as gaining a level.

**⚠ And this is the mechanism that transfers, for one specific reason: it is
temporal, not spatial.** A sound needs no object on screen to attach to. It
marks *the moment*, which is precisely what a typed line has and a pre-rendered
option does not. Everything else either game does needs a row to hang on.

---

## 2 · Both games log the player's line, attributed by name

`PARTYTABLE.res` carries `PT_DLG_MSG_LIST` — 64 entries of
`{PT_DLG_MSG_SPKR, PT_DLG_MSG_MSG}`. Speakers in the save read:

```
(blank) x12 · Canderous Ordo x10 · Gail Dakari x9 · Security Terminal x7
Zax x7 · Darth Malak x6 · T3-M4 x4 · Sith Governor x4 · Admiral Saul Kar x4
```

**`Gail Dakari` is the player character.** Their chosen line enters the
transcript under their own name, alongside everyone else's.

That is commit-time, and it is a *record* rather than a *marker* — nothing in
the data distinguishes the player's entries from an NPC's beyond the speaker
name. But it is the mechanism by which a chosen line becomes **a thing that was
said**, which is the half of the problem a typed line already solves for itself.

---

## 3 · Daggerfall commits the question to a colour-differentiated transcript

`SetQuestionAnswerPairInConversationListbox` runs on selection and does three
things in order:

1. **plays a click** — `PlayOneShot(SoundClips.ButtonClick)`
2. **appends the question** to `listboxConversation`, coloured
   `DaggerfallQuestionTextColor` and right-aligned
3. **appends the answer** beneath it

So the topic you picked becomes a line in a running exchange, visually distinct
from the reply it drew.

**⚠ Scope on this one.** Only **three** things in that window are guarded by
`EnableModernConversationStyleInTalkWindow` — the background-colour treatment at
lines 646, 1262 and 1273. **The transcript itself, the question colour and the
click sound are unguarded**, so the reimplementation treats them as base
behaviour. I cannot verify that against the original binary; I did not
disassemble classic Daggerfall.

*Separately, `textlabelPlayerSays` is a dedicated on-screen label showing the
question the player is **about to** ask, live, as they browse the list. That is
**pre**-commit and does not answer this question — but it is the closest either
game comes to showing a line in the player's voice before it exists.*

---

## 4 · ⚠ What neither game has

**Nothing in either game marks a reply with the outcome of its check.**

Searched both entire string tables: `[success]` / `[failure]` variants appear
**1,264 times in K1 and 831 in K2**, and **zero of them are attached to a player
reply**. They belong to the computer-terminal and system-feedback channel.

There is no field, no sound, no colour and no transcript treatment that says
*"that was a Persuade, and it worked."* The `[Persuade]` bracket announces a
skill is involved **before** the line, unreliably (§1), and then nothing follows
it. **The check resolves silently.**

Nor is there any per-reply commit treatment that is *systematic* rather than
authored. The presentation fields that fire when a reply plays are hand-placed:

```
                    K1 of 27,465 replies      K2 of 28,509
Script                 2,486  (9.1%)          3,563 (12.5%)
AnimList                 277  (1.0%)            297  (1.0%)
FadeType                  68  (0.2%)             40  (0.1%)
CamVidEffect               —                       4  (0.0%)
Emotion                    —                  28,509 (100%, K2 field)
```

A writer chose each of those. **None is generated from what the reply *did*.**

---

## 5 · So: borrowing or inventing?

**Borrowing, for two of the three parts.**

**Sound at the moment of commit — borrow it, and it is the important one.**
K2's alignment stinger is a working precedent for marking a line that has no
on-screen object, because a cue in time needs no row to attach to. The
classification is worth borrowing too: K2 filed it as a **UI notification**
beside level-up and quest-complete, not as music. That is the right register —
it says *something just happened to you*, not *the scene changed*.

**Attribution in a transcript — borrow it.** Both games make the chosen line a
thing that was said, under the speaker's name; Daggerfall additionally colours
the player's half differently from the reply. For typed text this is nearly
free, and it is what converts *"I wrote something"* into *"I said something."*

**Marking the check — inventing.** Neither game does it, in either direction,
and the one convention that gestures at it (`[Persuade]`) is pre-commit,
unenforced, and wrong more often than right. **There is no precedent to borrow
and no bad precedent to avoid — the space is empty.**

**One inherited warning that now applies differently.** §5 argued that a prompt
shown for something an NPC cannot answer would rebuild KOTOR's bracket problem.
Under the new ruling that risk moves: the failure is no longer a misleading
*label*, it is a typed line that **looks** as if it matched an authored reply
and did not. **The commit-time signal is what distinguishes the two cases**, and
that is the argument for having one at all — not decoration, but the only way
the player can tell which of the two things just happened to their sentence.

---

## 6 · Added to what was not checked

- **Neither game run.** The stinger is established from `guisounds.2da`, the
  presence of the assets in K2 and their absence in K1, and the script counts —
  **not from hearing it fire.**
- **Which K2 script actually triggers the stinger** — `a_givedark` calls an
  engine alignment function; whether the engine plays the cue on every alignment
  change or only above a threshold was not traced.
- **Daggerfall's classic binary** — §3's transcript claims come from the
  reimplementation, with the guarded/unguarded split reported as the evidence.
- **K1's reply `VO_ResRef`**, present on 19,640 of 27,465 replies against K2's
  32. A large divergence, noticed and not explained. It may mean K1 replies
  carry timing data rather than audio; I did not check whether those resrefs
  resolve to shipped files.
