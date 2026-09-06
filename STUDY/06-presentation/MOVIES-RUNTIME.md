# STUDY 06 — MOVIE PLAYBACK, THE RUNTIME MECHANISM

*The other half of batch 6's `BIK` record, which covered movies as files. This
is how one gets played.*

---

## 0 · Method, and one correction to my own first attempt

**Reliable source:** shipped NSS script source. Batch 7 established that KOTOR
ships source for BIF-layer scripts — **1,774 files in K1 and 638 in K2** — so
every call site in that layer can be read directly.

**⚠ A method I tried and discarded.** I first searched compiled NCS bytecode for
shipped movie filenames as string literals. It produced **862 "creature spawn"
call sites in K2** and other implausible figures. The cause: K2's movie files
include `credits`, `legal`, `aspyr` and `trailer` — ordinary English words that
appear in unrelated bytecode. Verified on `k_def_spawn01`, which matched only
because of the movie named `credits` and whose shipped source contains no movie
call at all. **Those numbers are discarded and appear nowhere below.**

**⚠ The consequence is a real limit, stated once and applying throughout.**
Module scripts are **compiled-only** (batch 5: 10,861 K1 and 4,508 K2 NCS files,
zero NSS). A module script can call `PlayMovie` and I cannot detect it without
decoding the NCS opcode set, which batch 5 left undecoded. **Every call-site
count below is a floor, not a total** — and the gap is visibly large, because
K1 ships 61 movie files and 63 source call sites naming only 14 distinct movies.

**Not run.** Neither game was executed. Nothing here is observed behaviour.

---

## 1 · ⚠ The call

Full declarations from `nwscript.nss`.

```
K1   void PlayMovie(string sMovie);
     void QueueMovie(string sMovie, int bSkippable);
     void PlayMovieQueue(int bAllowSeparateSkips);
     int  IsMoviePlaying();

K2   void PlayMovie(string sMovie, int nStreamingMusic = FALSE);
     void QueueMovie(string sMovie, int nSkippable = TRUE);
     void PlayMovieQueue(int nAllowSkips = TRUE);
     int  IsMoviePlaying();
```

**A movie is named by a plain `string`.** Not a `ResRef` (GFF has that type —
batch 3), not an index into `movies.2da`, not a filename with an extension. Just
a string matched against the `movies/` directory. This confirms batch 6's
finding from the other direction: `movies.2da` is a gallery listing and plays no
part in resolution.

**Three K1→K2 signature changes, all meaningful:**

- `PlayMovie` **gains `nStreamingMusic`**, defaulting to `FALSE`.
- `QueueMovie`'s skippable flag **becomes optional and defaults to `TRUE`**. In
  K1 the author had to decide; in K2 the default is that the player may skip.
- `PlayMovieQueue`'s flag likewise defaults to `TRUE`, and is renamed from
  `bAllowSeparateSkips` to `nAllowSkips`.

**⚠ And `IsMoviePlaying` is a stub in K2.** Its comment reads
*"PC CODE MERGER … dummy func so we can compile."* K1's is documented as a real
check. So the one function that would let a script *wait* for a movie is
non-functional in the sequel.

**K1's documentation is substantially fuller.** K1 comments explain the skip
semantics in four lines; K2's are reduced to bare function numbers.

---

## 2 · ⚠ What happens to the game

**Three of the four sub-questions have partial data answers; one does not. I am
separating them rather than filling the gap.**

### Can the player skip — ✅ answered, from BioWare's own documentation

K1's `nwscript.nss` comments, verbatim in substance:

- `bSkippable` **TRUE** — *"the player can cancel the movie by hitting escape."*
- `bSkippable` **FALSE** — *"the player cannot cancel the movie and must wait
  for it to finish playing."*
- `bAllowSeparateSkips` **TRUE** — escape *"only cancels out of the currently
  playing movie rather than the entire queue."*
- `bAllowSeparateSkips` **FALSE** — *"the entire movie queue will be cancelled."*

So skip is per-movie, and queue-skip granularity is a separate flag. **This is
documentation, not observation** — but it is the engine author's own, shipped
with the engine.

**What the engine does on a skip is not stated** beyond cancelling. Whether it
runs any completion path is unknown.

### Where does control return — ⚠ partially answered, and the answer is "it depends"

**Both cases occur in shipped data.**

*Into a new module.* `k_sup_galaxymap` contains, on consecutive lines:

```
PlayMovieQueue();
StartNewModule("003EBO", "WP_PC_WALK_MAP");
```

That script has **31 movie calls, 15 of them within three lines of a transition
or global write, and 5 `StartNewModule` calls**. The galaxy-map case plays a
travel sequence and lands the player somewhere else.

*Back into the conversation.* Of the dialogue nodes that call a movie script,
**K2 has 3 speaker nodes and 1 player reply that carry onward links** — the tree
continues after the movie. See §3.

### Is the calling script suspended — ⚠ inference, not read

**Most likely it runs on to completion.** The warrant is a batch-5 structural
finding, not a movie-specific one: **exactly three functions in either game take
an `action` parameter** — `DelayCommand`, `AssignCommand`, `ActionDoCommand` —
and those are the entire deferral surface. Scripts otherwise run to completion.
`PlayMovie` is not an `Action*` function and takes no `action` argument, so
there is no mechanism by which it could suspend its caller.

The `PlayMovieQueue(); StartNewModule();` adjacency is consistent with that and
does not prove it — it reads equally well as "the call blocks" or "both are
handed to the engine and sequenced."

**⚠ Needs the running game to settle.**

### Does the module stay loaded — ❌ not answerable from data

Nothing in the script API, the module manifest or the save format indicates
whether a module unloads during playback. **Needs the running game.**

*(Batch 4's three-tier module-state model says a module snapshot is written on
leaving. Whether a movie counts as leaving is exactly the unknown.)*

---

## 3 · ⚠ Where it is actually called from

**Scripts whose shipped source calls a movie function:**

```
K1   8 scripts, 63 calls — ALL PlayMovie, ZERO QueueMovie
     k_hbas_playkash · k_hbas_playkorr · k_hbas_playman · k_hbas_playtat
     k_inc_ebonhawk · k_pman_28d_cmp01 · k_pman_28d_cmp02 · k_qa

K2   4 scripts, 43 calls — 10 PlayMovie · 26 QueueMovie · 7 PlayMovieQueue
     a_playkremov01 · a_playpermov · k_align_movie · k_sup_galaxymap
```

### What binds them

```
                                   K1        K2
object / area / module hooks      NONE      NONE
dialogue nodes                       5        11
Mod_StartMovie (IFO field)           0         0
```

**No creature, placeable, door, trigger, area or module hook is bound to any of
these scripts.** Searched every one of those hook fields across every module in
both games.

**⚠ `Mod_StartMovie` is set on zero modules in either game.** Batch 4 recorded
the field as present on all 239 module manifests; it is populated on none of
them. A declared "play this on module entry" mechanism, never used.

### ⚠ Is it ever called mid-conversation — YES, and K2 does it deliberately

```
K1   player reply, TERMINAL        5      ← the conversation ends
     player reply, continues       0
     speaker node                  0

K2   player reply, TERMINAL        7
     speaker node, CONTINUES       3      ← ⚠ the tree carries on
     player reply, CONTINUES       1
```

**In K1 every movie-calling dialogue node is a terminal player reply.** The
movie is the last thing the conversation does.

**In K2, four nodes play a movie and then continue the tree** — three speaker
nodes and one player reply, all in `003atton` and `3cfd`, all calling
`a_playpermov`. That script reads `GetScriptParameter(1)` and switches on it to
pick one of seven `permov0*` files — the K2 parameterised-primitive pattern from
batch 5, applied to movie selection. **The movie is a beat inside the scene, not
the end of it.**

*The K1 sample is 5 nodes and the K2 sample 11, both floors — see §0.*

### One oddity

**`k_qa` carries 43 `PlayMovie` calls and 50 `DelayCommand` calls** — a QA
harness for stepping through every movie, shipped in K1's BIF layer. It is the
single largest concentration of movie calls in either game and is not content.

---

## 4 · Transition shape

**No fade is authored around a movie at the dialogue layer.**

`FadeType` is **0 on all 16 movie-calling dialogue nodes** — 5 in K1, 11 in K2,
without exception. Batch 6 found `FadeType` set on only 0.2% of nodes overall;
on movie nodes it is set on none.

So from the conversation's point of view the cut is hard, and any fade must come
from the engine or from the script. **`k_sup_galaxymap` does call
`SetGlobalFadeOut` twice** — so the galaxy-map travel sequence fades
deliberately, in the script, not on the node. That is the only fade evidence
found in either game around a movie.

**No `Delay` is set on any movie-calling node either.**

---

## 5 · K1 vs K2 — the calling pattern changed as much as the budget

Batch 6 found K2 spending 607 MB → 1,600 MB on video for 10% more files. **The
calling pattern changed too, and in a direction the asset budget explains.**

| | K1 | K2 |
|---|---|---|
| `PlayMovie` calls in source | **63** | 10 |
| `QueueMovie` calls | **0** | **26** |
| `PlayMovieQueue` calls | **0** | **7** |
| skippable default | author must decide | **defaults TRUE** |
| `IsMoviePlaying` | documented, real | **stub** |
| mid-conversation, continuing | **0** | **4** |
| beside a module transition | 0 of 63 | **15 of 31** in the galaxy map |

**K1 plays one movie and forgets it.** Every call is `PlayMovie`, fire and
forget, and every dialogue binding is terminal.

**K2 builds sequences.** `k_sup_galaxymap` queues a departure and a hyperspace
shot together — `QueueMovie("TelMov02"); QueueMovie("HypMov01"); …
PlayMovieQueue(); StartNewModule(…)` — so a single journey is composed from
reusable pieces rather than one bespoke file. That is what 1,600 MB across 67
files buys: **not longer movies, but movies that combine.**

**And the migration is visible in the source.** `k_align_movie` carries a
commented-out `PlayMovie("ScnMov01")` immediately above the two `QueueMovie`
calls that replaced it.

---

## 6 · What was not checked

- **Neither game run.** Every §2 claim is documentation or inference, labelled
  as such.
- **Module-script call sites.** Compiled-only, opcode set undecoded (batch 5).
  All counts are floors. The size of the gap is visible: 61 K1 movie files
  against 14 distinct movies named in readable source.
- **What the engine does on a skip** beyond cancelling.
- **Whether a module unloads** during playback.
- **Whether `PlayMovie` blocks** its caller.
- **`nStreamingMusic`** — K2's added parameter. Its effect was not traced; it is
  `FALSE` at every K2 call site read.
- **Bink playback itself** — third-party codec, deliberately untouched in
  batch 6 and here.
