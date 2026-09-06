# STUDY 05 — ASKING THE SAME THING TWICE

*Narrower than batch 5's DLG record. What happens on the second ask.*

**Coverage.** Every DLG in both KOTOR games — 1,167 K1 and 1,159 K2, 48,776
speaker nodes and 55,974 player nodes — plus `globalcat.2da` in both, and
Daggerfall's `TalkManager.cs` (MIT, described not reproduced). Neither game run.

---

## 1 · ⚠ Is there a repeat mechanism? No — and the negative is clean

**Searched every field name at every level of the DLG format** — file, speaker
node, player reply, link, and starting-list entry — in both games:

```
distinct field names        K1  78      K2  159
matching  visit | once | seen | shown | repeat | count | used |
          been | prior | already | first | time
                            K1  NONE    K2  NONE
```

**There is no visited flag, no once-only marker, no counter, no
shown-before field, and nothing that tracks having been anywhere.**

This is not an oversight in one game corrected in the other. K2 more than
doubled the field count — adding eighteen gate fields, a second action script,
twelve parameter slots, `Emotion`, `FacialAnim` and a whole VO pipeline — and
added **nothing** here.

**The format has no concept of a second visit.**

---

## 2 · Loop-backs, counted

**Direct self-loops are rare.** A reply that returns to the very speaker node it
came from:

```
                    K1                      K2
reply transitions   48,659                  54,243
return to source       375  (0.8%)             276  (0.5%)
advance             44,536                  45,796
terminal             3,748                   8,171
```

Concentrated where you would expect: K2's `console01` (61) and `console01b`
(58) and `workbnch` (9); K1's `k_gen_comptest` (9). **Menus, not conversations.**

**But re-entrancy is common, and that is the real measure.** Counting how many
speaker nodes can be reached from more than one place:

```
                                    K1              K2
speaker nodes                   24,339          24,437
in-degree 1                     20,195          20,878
in-degree 2                      2,624           2,093
in-degree 3                        917             854
in-degree 4                        302             302
in-degree 5+                       321             310
⚠ reachable from >1 place        4,144 (17.0%)   3,559 (14.6%)
```

**One speaker node in six is a hub you can arrive at from several directions**,
and the concentration is exactly in the conversations players spend most time
in: `k_hjuh_dialog` 131, `k_hcar_dialog` 104, `k_hbas_dialog` 92 in K1;
`handmaiden` 123, `kreia` 111, `t3m4` 108, `disciple` 75 in K2. **The companion
conversations.**

**So asking twice is not an edge case.** The hub-and-spoke shape — return to a
topic menu, pick another subject, come back — is the normal structure of every
major character conversation in both games, and the format tracks none of it.

---

## 3 · ⚠ Did content work around it? Yes, by hand, and K2 twice as much

Globals whose names suggest asked / told / heard / met / first:

```
                    K1                      K2
globals declared    1,185                   999
matching              25  (2.1%)              45  (4.5%)

K1 by keyword   know 11 · ask 4 · told 4 · greet 2 · tell 1 · met 1 ·
                first 1 · spoke 1
K2 by keyword   first 20 · know 13 · intro 8 · talked 2 · met 1 · heard 1
```

**K1's shape is knowledge:** `KOR_KNOW_ACADEMY`, `KOR_KNOW_EXCAV`,
`KOR_KNOW_YUTHURA`, `KOR_KNOW_JORAK`, `kas_GuardTold`, `tat_AskAboutHunt`,
`End_TraskTalk`. Eleven of the twenty-five are Korriban `KNOW_*` flags — one
region's writers building a "has the player learned this" layer by hand.

**K2's shape is sequence:** twenty of forty-five contain `First`, and eight
contain `Intro`. The clearest case is a character introduction implemented as a
run of booleans:

```
101PER_Atton_Intro_1 · 101PER_Atton_Intro_2 · 101PER_Atton_Intro_3 ·
101PER_Atton_Intro_4
```

**Four global booleans standing in for a counter**, because there is no counter.
And each of those four occupies a row in a game-wide predeclaration table
(batch 2 F19), out of a 999-row budget.

**⚠ Scope on this count.** It matches on *names*, so it is a lower bound on
intent and an upper bound on certainty — a global called `KOR_KNOW_DRUG` is
probably a told-you-already flag but the name is the only evidence. Globals that
do this job under an unrevealing name are not counted.

---

## 4 · Daggerfall — and it does have answers

**Three real mechanisms, where KOTOR has none.**

**A per-conversation question counter.** `numQuestionsAsked` is incremented on
each question and reset per conversation. `GetPCGreetingOrFollowUpText()` reads
it: **zero questions asked → greeting phrasing; otherwise → follow-up
phrasing.** So the player's own question is worded differently the second time,
and it takes the current tone as well.

**⚠ A per-NPC answer budget.**
`maxNumAnswersNpcGivesTellMeAboutOrRumors = 1`. An ordinary NPC gives **one**
"tell me about" answer and then stops — the check refuses further answers unless
the NPC is *in the same building as the topic*, is the spymaster, or a debug
"NPCs know everything" mode is on. **Asking twice is explicitly handled by
declining.**

**⚠ And asking twice gives the same answer, deliberately.** The random pick is
seeded, not free:

```
DFRandom.Seed = hash(this NPC)
DFRandom.Seed += the topic key, the building key, the caption
rand = random_range_inclusive(1, 20)
```

**Seeded from who you are asking and what you are asking about.** So the same
NPC gives the same answer to the same question every time, while a *different*
NPC gives a different one. Variety across the population, consistency per
person. That is a design choice, and it is the opposite of the naive
"re-roll each time".

Rumors are the exception — `listRumorVariants` holds variants, and the rumor
mill is a separate channel from topics.

---

## 5 · ⚠ Does tone vary by context at all?

**Both games do this. Daggerfall does far more of it.**

### KOTOR — one player line, several gated answers

```
                                          K1              K2
replies with outgoing links           23,802          24,269
  exactly one target                  21,305          21,989
  several targets                      2,497           2,280
  ⚠ several AND gated                  2,379 (10.0%)   1,669 (6.9%)
fan-out 2 / 3 / 4 / 5 / 6+     1,870/328/110/75/114   1,757/282/115/45/81
```

**One reply in ten in K1 leads to a gated choice of answers** — the same player
line, a different NPC response depending on state. That is real context-varying
delivery and it is the mechanism KOTOR has.

The extreme case is K2's `000react`, a party-reaction file, where one reply
carries **51 gated targets, every one a `c_global_eq`** — a fifty-one-way
dispatch on a single global. Another in the same file switches three ways on
`c_npc_inprty` (*is this companion in the party*).

**But the gate vocabulary limits what can vary.** Batch 5 established K2's
conditions are dominated by `c_local_notset`, `c_global_eq`, `c_local_set` and
`c_quest_status` — **flags and quest stages**. Delivery varies by *what has
happened*, essentially never by *who the listener is* or *what state they are
in*. `c_ismale` (240 uses) is close to the only identity gate in the vocabulary.

### Daggerfall — the answer is computed from five inputs

Reaction to the player is assembled, not looked up:

```
reaction = faction reputation
         + player.BiographyReactionMod        ← the character-creation answers
         + reaction modifier for this social group
         + SGroupReputations[social group]
         + Personality / 5
         + the chosen tone (Polite / Normal / Blunt), cached per session
```

And the answer strings are **tables indexed by context, extracted from the
original executable**:

- `answersToDirections` and `answersToNonDirections` — **30 string ids each**,
  and the source comment names *"5 social groups"* and a *"dislike player +
  don't know answer"* combination. So the response to "where is X" is selected
  by **social group × whether they know × how they feel about you.**
- `knowledgeModifiers` — **40 values, documented as "8 question types and 5
  social groups"**.
- `greetings` — **27 string ids**.
- `etiquetteReactionMods` and `streetwiseReactionMods` — five values each,
  mirror images of one another.

**⚠ Note `BiographyReactionMod`.** That is the character-creation biography
questionnaire — the twelve multiple-choice questions whose answers carry
mechanical payloads — reaching into how strangers talk to you, years of play
later. It is the single most impressive thing either game does on this axis.

### The baseline, stated plainly

**KOTOR: one authored string per node, with branching used to choose between
whole authored alternatives.** A node's text never changes; the engine picks a
different node. Batch 5 found no template or substitution mechanism on node text
beyond the `<FullName>` token family, and batch 6 found `Emotion` and
`FacialAnim` vary *performance* but never *words*.

**Daggerfall: one template per situation, with the situation computed from
faction, social group, reputation, biography, Personality, tone and knowledge.**
Words are assembled; there is no authored line at all for the general case.

**Neither game varies delivery on being wounded, on time of day, or on
alignment.** Searched KOTOR's gate vocabulary (509 distinct K2 condition
scripts, batch 5) for health, time or alignment conditions: `c_ismale` and
quest/flag checks dominate, and no health or clock gate appears in the
frequently-used set. Daggerfall's reaction inputs are listed above in full and
contain none of the three.

---

## 6 · What was not checked

- **Neither game run.** No observed behaviour anywhere.
- **§3's global count matches on names only.** A told-you-already flag with an
  unrevealing name is not counted; the true figure is higher and unknowable
  from names.
- **Compiled module scripts.** A module script could implement a repeat guard
  invisibly — batch 5 left the NCS opcode set undecoded, so `SetLocalBoolean`
  calls inside compiled scripts are not searchable. **This is the largest gap
  in §1's negative:** the *format* has no repeat mechanism, which is proven;
  whether *scripts* hand-rolled one more often than the global names suggest is
  not.
- **Daggerfall's classic binary.** §4 and §5's Daggerfall claims come from the
  reimplementation. Where it annotates a divergence from classic — the
  social-group ordering fix, the Etiquette modifier as an *"improvement over
  classic"* — that annotation is reported.
- **The 51-way `000react` dispatch** was counted, not traced to what the fifty-one
  globals distinguish.
- **Whether KOTOR's gated alternatives are ever authored as tonal variants** of
  the same content rather than genuinely different content. That needs reading
  the strings in pairs, which I did not do.
