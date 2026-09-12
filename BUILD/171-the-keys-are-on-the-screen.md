# BUILD 171 — the keys are on the screen

---

## 1 · ⚠ `PT-1852` — FOUR ACTION KEYS, NAMED

    f powers · d disengage · s hide · h hurry · space to end your turn

**All four on the combat line, and the exploration line took none — because it
could not.** It sits in a `Row` beside an `Expanded`, so its width is whatever
is left over, and **one more entry wrapped it and overflowed the screen's
column by 57px.**

The comment beside that line has warned since the day a second **line** cost
9px and broke seventeen tests. **A second line's worth of height is the same
whether it comes from a new widget or from this one wrapping** — which is the
part the warning did not say and now does.

## 2 · ⚠⚠ I GUESSED WRONG ABOUT WHICH LINE, AND THE GUESS WAS THE MISTAKE

I changed **both** lines at once, saw the overflow, and assumed the longer
combat line was the cause. It is not — it takes four entries comfortably.

Found by changing **one line at a time** and running the same fast test against
each:

    exploration change only   →  2 overflows
    combat change only        →  0

**Guessing which of two changes caused a failure is not a diagnosis.** Third
time this session a bad attribution has cost a step — the invalid indicator
control, the `whole_loop` flake, and now this — and every one was settled the
same way: isolate one variable and measure.

## 3 · ⚠ AND THE COMBAT LINE IS WHERE THEY MEAN SOMETHING

Every one of the four costs the Action, so all four answer *there is nothing
to…* until a round is running — `f` opens its menu anywhere and `PT-1488`
refuses the aim outside a fight.

**⚠ THEY VANISH WHEN THERE IS NOTHING LEFT TO SPEND**, which is the rule the
colour one line below already follows (`PT-1517`). Naming three keys to somebody
who has already acted would name three keys that can only refuse.

## 4 · ⚠ ELEVEN ASSERTIONS READ THE OLD STRING EXACTLY

`find.text('space to end your turn')` across three files. The string is now part
of a longer line, so they read `textContaining`. The intent is unchanged: the
end-turn affordance is on screen.

---

## Tests

    App  595 pass · zero overflows

## Still open

- **A real target picker**, before power effects resolve — `PT-1847`.
- `§2`'s character screen (the click, `PT-1443`'s) · `Scan`, `Slice`, `Treat`,
  `Repair` unblocked and unbuilt · the stealth field generator has no item.
- **22 unresolved rows** in `Armory` Chapter Seven.
- ⚠ The suite is flaky under load — `BUILD 167`.
- ⚠ **The exploration legend is full.** The next key that belongs there has
  nowhere to go without shortening an existing entry.
