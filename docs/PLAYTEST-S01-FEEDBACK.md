# FIRST PLAYTEST — what to try, and where to write what you think

**Everything here works today. Nothing here has been designed.** Sizes are correct now but nobody has decided what any of it should *look* like, so the useful feedback is about **what confused you, what you expected and didn't get, and what felt wrong** — not about it being plain.

**Fill in the boxes as you go.** Skip anything that doesn't provoke a reaction. An empty box is a fine answer.

---

## Before you start

```
cd ~/kotor-repos
. ./env.sh
```

Then from `KOTOR-RPG-APP/` or `Loom/`:

```
flutter run -d linux
```

**Your packages are at `~/.local/share/kotor-rpg/packages/`** — open that folder alongside, because a lot of what you're testing is *"did clicking this write the right thing to disk."*

**Known scaffold — don't report these as bugs:**

- The weapon is **a fist**. Nothing resolves equipment yet.
- The portrait is **a placeholder circle**. No portrait art exists.
- The board is **drawn, not textured**. No tileset has ever been imported.
- Nothing is designed. Colours carry meaning; they aren't a look.

---

# PART ONE — THE APP

## 1 · Console Home

**The first screen.** Your library of packages, a friends strip, three small icons in a corner.

**Try:** does the library show `Endar Spire`, `Taris Undercity` and `base-rules`? Do the tiles tell you what each package *is*? Is `base-rules` offered as something you could play, and should it be?

**Feedback**

```



```

---

## 2 · Package selection and the main menu

**Pick a package.** You should reach a seven-button screen: Continue, New Game, Load Game, Movies, Music, Options, Exit to Library.

**Try:** does `Exit to Library` go where its name says? Are `Continue` and `Load Game` lit or dark, and does that match whether you have a save?

**Feedback**

```



```

---

## 3 · Character creation — the pre-hub

**Species, then Model if you picked a droid, then Class.** No step strip yet — that's deliberate.

**Try:** pick a species with subraces (**Aqualish**, **Zabrak**). Does the second-level picker make sense? Then try a **Droid** — you should get chassis instead of subraces, and a Model step organics never see.

**Try a Rakata or a droid and then look for Force classes.** They should be barred, and it should tell you which rule is barring you.

**Feedback**

```



```

---

## 4 · The step strip

**After Class, the strip appears.** An organic Jedi gets nine steps; an Astromech gets six.

**Try:** count the steps for an organic and for a droid. Does the numbering make sense when steps are missing? Is it obvious what's locked and why?

**Try re-opening a completed step.** It should warn you and name what you'll lose.

**Feedback**

```



```

---

## 5 · Origin

**Two stages — homeworld, then upbringing.** 271 worlds. Each world teaches four skills; you pick one.

**Try:** read a world description. Does it read like something written for a player, or like a research note? Does the four-skill menu make the choice feel meaningful?

**Feedback**

```



```

---

## 6 · Abilities

**Six rows at 8, thirty points to spend.** Your class's priority abilities are marked in amber.

**Try:** spend everything. Can you tell what a point costs before you spend it? Is the amber marking useful or noise?

**Try a droid.** It doesn't buy — it gets its chassis's production spread. Does that read as intentional or as broken?

**Feedback**

```



```

---

## 7 · Skills

**25 skills. Ones you have an aptitude for cost half and cap twice as high.**

**Try:** find a skill marked `class`, one marked `homeworld`, one marked `profession`. Does knowing *why* something is cheap matter to you, or would a tick have been enough?

**Feedback**

```



```

---

## 8 · Feats, Powers, Equipment, Identity

**Powers only appears if your class grants them** — six of nineteen classes.

**Try:** at Equipment, the profession offer — an item or an aptitude. Neither is pre-picked. Is the choice clear?

**At Identity:** portrait, name, story. The story is assembled from your choices and you can edit it. **Does the generated story read like something a person would write?**

**Feedback**

```



```

---

## 9 · Play — walking

**Two areas, a door between them.**

**Try:** walk around. Walk through the door and back. Does the room read? Is the grid too loud, too faint, about right?

**Feedback**

```



```

---

## 10 · The conversation

**Walk into the trooper.** A panel opens below the board.

**Try:** read the options. **The colours mean things** — amber rolls, grey is manner, teal is who you are, plain is plain. Can you tell them apart without being told?

**Type something in the box** that matches an option's meaning. Does it fire?

**Try the option that starts a fight.**

**Feedback**

```



```

---

## 11 · The fight

**Initiative, then turns.** The trooper acts under a doctrine.

**Try:** attack, get attacked. Does the line explaining the roll help or clutter? Can you tell whose turn it is?

**Try walking out mid-fight and coming back.** The trooper should still be hurt.

**Feedback**

```



```

---

## 12 · Saving

**Play writes a save.** Quit the app entirely and reopen it.

**Try:** does `Continue` bring back the same character in the same place, still hurt if they were hurt?

**Feedback**

```



```

---

# PART TWO — LOOM

## 13 · Making a package

**New Package.** It asks two things — a name, and an id it fills in for you.

**Try:** type a name with a number or a stat in it — `Armor Class 8`. It should refuse and say why. **Then open `~/.local/share/kotor-rpg/packages/` and look at what it wrote.**

**Feedback**

```



```

---

## 14 · Areas and painting

**New Area, then paint.** Drag a box — it fills. Five tile types.

**Try:** paint a room with walls. **Then open the area's `.toml` and look at the map** — it's drawn as characters, so you should be able to see your room in the file.

**Feedback**

```



```

---

## 15 · Creatures, doors and conversations

**Try:** make a creature, place it. Make a doorway between two areas. Make a conversation with a node, a reply and a gate.

**Does the tree make sense? Can you tell what a gate does from looking at it?**

**Feedback**

```



```

---

# PART THREE — THE BIG QUESTION

## 16 · The side panel

**Right now the dialogue panel runs the full width along the bottom, and the board sits above it.**

**The measurement:** with the panel open, the room's size is governed by height alone, so **about 70% of the width is black.** A panel **down one side instead** would give the room a squarer space — **a 66px tile instead of 29px. More than double.**

**Try a conversation and look at how much room you can see.** Then imagine the panel on the right with the board filling the rest.

**Which do you want?**

```



```

---

# ANYTHING ELSE

**What surprised you. What you expected and didn't find. What you'd throw away.**

```




```
