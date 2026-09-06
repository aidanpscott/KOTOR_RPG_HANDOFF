# STUDY 05 — BEHAVIOUR LAYER — RECORDS

Four records — DLG, NSS, NCS, LIP — on the template from `STUDY/README.md`.

Coverage: **every DLG in both games** (1,167 K1 / 1,159 K2 — 48,776 speaker
nodes, 55,974 player nodes, 150,344 links), every NSS and NCS in the BIF layer,
every LIP in `lips/`, and both `nwscript.nss` files. `.mod` files are excluded
throughout — batch 4 established they are runtime artifacts.

**Sits on:** batch 2 (globalcat, two string globals), batch 3 (blueprint script
hooks), batch 4 (IFO/ARE/GIT event bindings, the journal) and `LIVE-STATE.md`
(the persisted `ActionList`).

---

## DLG — the conversation

**WHAT IT IS** A conversation as a directed graph: things a character says,
things the player may say back, and the conditions on each link between them.

**CONTAINER** BIF, and per-module — `<mod>_s.rim` in K1, `<mod>_dlg.erf` in K2
(batch 1).

**STRUCTURE** GFF, tag `DLG `, V3.2. **Three node pools and one entry point.**

```
StartingList[]   which speaker node opens the conversation  (gated)
EntryList[]      what a character says          each has RepliesList[]
ReplyList[]      what the player may say        each has EntriesList[]
```

`EntryList` and `ReplyList` are **flat pools indexed by position**; the tree is
made entirely of links holding an `Index` into the other pool. A node is never
nested inside another node.

**A node carries far more than text.** Present on 100% of nodes in both games:

*Content:* `Text` (StrRef), `Speaker`, `Listener`, `Comment` (author notes,
shipped).
*Voice:* `VO_ResRef`, `Sound`, `SoundExists`.
*Script:* `Script`; **K2 adds `Script2` and seventeen parameter fields.**
*Animation:* `AnimList`, `WaitFlags`, `Delay`; **K2 adds `Emotion` and
`FacialAnim`.**
*Camera:* `CameraAngle`, `CamVidEffect`, and optionally `CameraID`,
`CamHeightOffset`, `TarHeightOffset`, `CamFieldOfView`, `CameraAnimation`.
*Fade:* `FadeType`, and optionally `FadeColor`, `FadeDelay`, `FadeLength`.
*Quest:* `Quest`, `PlotIndex`, `PlotXPPercentage`, and optionally `QuestEntry`.

So the answer to "can a node carry a script, a sound, an animation, a camera?"
is **yes to all four, plus a quest update and a screen fade, on every node.**

**⚠ The link is where the gate lives, and this is where K1 and K2 diverge most.**

```
K1 link   { Index, Active, IsChild, LinkComment }

K2 link   { Index, Active, Active2, Not, Not2, Logic,
            Param1..Param5, Param1b..Param5b, ParamStrA, ParamStrB,
            IsChild, LinkComment }
```

K1's gate is **one script resref and nothing else**. K2's is a **two-term
boolean expression**: two script slots, each negatable, combined by `Logic`,
each parameterised with five integers, five more integers, and two strings.

`StartingList` entries carry the same gate fields — so which line opens a
conversation is decided by the same mechanism.

**REFERENCES OUT** TLK **by StrRef** (`Text`); scripts **by resref** (`Active`,
`Active2`, `Script`, `Script2`); voice and lip assets **by resref**
(`VO_ResRef`); quests **by index**; 2DA rows **by index** (`CameraAngle`,
`Emotion`, `FacialAnim`, `CamVidEffect`); other nodes **by list position**.

**REFERENCED BY** `UTC.Conversation`, `UTP.Conversation`, `UTD.Conversation`
(batch 3), and `ActionStartConversation` — all **by resref**.

**SCOPE** Module-local when in a module archive; game-global in the BIF.
Companion dialogue lives in the BIF, so it follows the player between modules.

**AUTHORED BY** A human in a conversation editor. K2 ships `EditorInfo` on 5
files and `NodeID`/`NextNodeID` on every node — editor bookkeeping in the
product.

**READ WHEN** Conversation start; each link's gate is evaluated when the node is
reached.

**K1 vs K2**
- **K2 replaces bespoke gates with a parameterised library** — see `README.md` §2.
- K2 adds `Script2` + `ActionParam1..5`, `1b..5b`, `StrA`, `StrB` to every node.
- K2 adds `Emotion` and `FacialAnim` (indexing the K2-only `emotion.2da`, 35
  rows, and `facialanim.2da`, 17 rows, found in batch 2).
- K2 adds VO pipeline fields to every node: `RecordVO`, `RecordNoVOOverri`,
  `VOTextChanged`, `Changed`, `AlienRaceNode`, `PostProcNode`; and at file level
  `DeletedVOFiles`, `RecordNoVO`, `AlienRaceOwner`, `PostProcOwner`.
- K2 makes `ConversationType`, `ComputerType`, `OldHitCheck`, `AmbientTrack`,
  `UnequipItems`, `AnimatedCut`, `UnequipHItem` universal (partial in K1).
- **K2 abandons the `Sound` field entirely** — see the LIP record.

**SAMPLES**
| # | file | source | shape | why |
|---|---|---|---|---|
| 1 | `dan14aa_door` | K1 `danm14aa_s.rim` | 1 entry, 0 replies, 1 start, 1,348 b | trivial — a single barked line |
| 2 | `k_hjuh_dialog` | K1 BIF | 540 entries, 732 replies, 23 starts, **583 KB** | the large one — a companion's whole conversation tree |
| 3 | `kreia` | K2 BIF | 627 entries, 738 replies, 18 starts, **1.64 MB** | K2's largest; the biggest single content file in the study |
| 4 | `man26_swoop1` | K1 `manm26ab_s.rim` | 28 entries, **0 replies**, 28 starts | oddity — 28 gated openings and no player choice at all; a conditional barks table wearing a conversation's clothes |
| 5 | `listen1` | K2 `303nar_dlg.erf` | **0 entries, 0 replies, 0 starts**, 864 b | oddity — a completely empty conversation that still ships |

**UNKNOWN** What `IsChild` selects on a link (present on all 150,344, values not
tabulated). What `OldHitCheck` and `ConversationType` control. Not resolved.

---

## NSS — script source

**WHAT IT IS** The C-like source a designer writes.

**CONTAINER** BIF only.

**STRUCTURE** Plain text. Two entry-point conventions, and the distinction is
the whole type system of the behaviour layer:

```
void main()                 an ACTION — runs for effect, returns nothing
int  StartingConditional()  a CONDITION — returns non-zero to open a gate
```

**Source ships, and that is worth stating plainly.** K1 ships **1,774 NSS**
files against 1,784 NCS in the BIF; K2 ships **638 NSS** against 612 NCS. So
nearly every engine-level script ships with its source beside the compiled form.

**Module scripts do not.** All 10,861 K1 and 4,508 K2 module scripts are NCS
only — searched every `_s.rim` in both games for type 2009 and found none.

**REFERENCES OUT** `nwscript.nss` — the function library, `#include`d
implicitly. Engine functions by name; other scripts by resref via
`ExecuteScript`.

**REFERENCED BY** Nothing at runtime. Source is documentation that happens to
ship.

**SCOPE** Game-global (BIF).

**AUTHORED BY** A human.

**READ WHEN** Never by the engine — the NCS is what runs.

**K1 vs K2** K1 ships nearly three times as much source. K2's is dominated by
the `a_*` / `c_*` primitive library described in `README.md` §2.

**SAMPLES**
| # | file | game | why |
|---|---|---|---|
| 1 | `c_ismale` | K2 | trivial — 240 bytes, one engine call |
| 2 | `c_global_eq` | K2 | the pattern — 470 bytes, reads its own parameters |
| 3 | `c_quest_status` | K2 | the large primitive — 2,795 bytes |
| 4 | `nwscript` | both | the library itself; 217 KB in K1, 266 KB in K2 |

**UNKNOWN** Whether the shipped NSS matches the shipped NCS byte-for-byte after
recompilation. Not tested — would need a compiler run and is out of scope.

---

## NCS — compiled script

**WHAT IT IS** The bytecode the engine actually runs.

**CONTAINER** BIF and every module archive. **The most numerous resource type in
the game** — 12,645 in K1, 5,120 in K2.

**STRUCTURE** Binary. Magic `NCS V1.0` (8 bytes), then a byte and a **big-endian
uint32 giving the total file length**, then the instruction stream. Verified: the
declared length equals the resource size on every file sampled.

Note the endianness: **the length is big-endian while every other binary format
in the study is little-endian.** GFF, 2DA, TLK, ERF, RIM and KEY are all
little-endian.

Sizes run from under 100 bytes to over 100 KB — `LIVE-STATE.md` found a 106 KB
script captured mid-execution in a save.

**REFERENCES OUT** Engine functions **by numeric opcode**, not by name — the
name-to-number binding is fixed by `nwscript.nss`'s declaration order and
compiled away. Other scripts and objects by string constants in the stream.

**REFERENCED BY** Every script hook on every object (see `README.md` §5), every
DLG gate and node action, and `ExecuteScript`.

**SCOPE** Module-local or game-global by container.

**AUTHORED BY** Generated by the compiler.

**READ WHEN** On the event that binds it. Can be **captured mid-execution and
persisted** — see `README.md` §4.

**K1 vs K2** Same format, same magic, same header. K1 has 2.5× as many.

**SAMPLES**
| # | file | game | size | why |
|---|---|---|---|---|
| 1 | `a_global_set` | K2 BIF | 98 b | minimal — read two parameters, one engine call |
| 2 | `c_local_set` | K2 BIF | 895 b | typical primitive |
| 3 | `k_con_talkedto` | K1 BIF | 929 b | K1's bespoke equivalent |
| 4 | `k_ai_master` | K1 | ~106 KB | oddity — the AI script found suspended in a save with an instruction pointer |

**UNKNOWN** The opcode set. Not decoded — this batch establishes the container
and the calling convention, not the instruction semantics.

---

## LIP — lip-sync animation

**WHAT IT IS** A timeline telling a face which mouth shape to hold, so speech
looks spoken.

**CONTAINER** `lips/<module>_loc.mod` — one archive per module, named by format
string (`LIPS:%s_loc`, batch 1). **123 archives in K1, 77 in K2.**

**STRUCTURE** Binary, magic `LIP V1.0`.

```
"LIP V1.0"            8 bytes
duration              float32, seconds
entryCount            uint32
entries               entryCount x 5 bytes
```

Entry stride is **exactly 5 bytes**, verified arithmetically on files of
different sizes: a 351-byte file declares 67 entries ((351−16)/67 = 5.0) and a
111-byte file declares 19 ((111−16)/19 = 5.0). The natural reading is a float32
timestamp plus a one-byte mouth-shape id, but **the field split was not
confirmed by decoding values** — it is inference from the stride.

Counts: **18,209 LIP resources in K1, 26,218 in K2.** Sizes 26 bytes (2 entries)
to 926.

**REFERENCES OUT** Nothing.

**REFERENCED BY** A dialogue node, **implicitly** — the LIP shares its resref
with the voice line. `VO_ResRef` names one string, and that one string locates
the WAV *and* the LIP. Confirmed: dialogue node resrefs match a shipped LIP name
15,126 times in K1 and 15,377 in K2.

**SCOPE** Module-local, by archive.

**AUTHORED BY** Generated from the audio by a tool.

**READ WHEN** When the line plays.

**K1 vs K2** Same format. K2 ships 44% more LIP files across 37% fewer archives.
The routing changed — see `README.md` §6.

**SAMPLES**
| # | resref | archive | why |
|---|---|---|---|
| 1 | `nm13aac86906000_` | K1 `danm13_loc.mod`, 26 b | minimal — 2 entries |
| 2 | `nstn57c01001009_` | K1 `STUNT_57_loc.mod`, 926 b | the large one |
| 3 | `nglobebant00102_` | K1 `global.mod`, 351 b, 7.988 s, 67 entries | a typical line |
| 4 | `avo_quarquess1` | K2 `001ebo_loc.mod`, 111 b, 3.984 s, 19 entries | K2's naming convention differs — no trailing underscore |
| 5 | 14 K1 `lips/*.mod` archives | — | oddity — empty, carrying no LIP at all (batch 1) |

**UNKNOWN** The mouth-shape vocabulary — how many shapes exist and what they
map to. Would need the model layer (batch 6) or the running game.
