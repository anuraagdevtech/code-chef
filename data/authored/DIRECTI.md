---
topic: Strings
subtopic: Parsing and reversing a route
time: $O(N)$ per test case
space: $O(N)$
---
Separate each instruction into its **turn** and its **road**. The first line is `Begin on <road>`; every later line is `Left on <road>` or `Right on <road>`. Splitting on the first occurrence of `" on "` is the safe way to do it, since road names contain spaces — `Old Madras Road` would break a naive `split()`.

Reversing the route pairs each road with a *different* turn. Driving out, the turn listed with road $i$ is the one taken to **enter** road $i$. Driving back, that same junction is taken in the opposite sense and now leads onto road $i-1$. So:

- the new `Begin on` road is the **last** road of the original;
- for $i$ from $N-1$ down to $1$, emit the **flip** of turn $i$ together with road $i-1$.

Each `Left` becomes `Right` and vice versa.

That index shift is where this problem is usually lost. Reversing the list and keeping each turn attached to its own road produces a route of the right length that turns the wrong way at every junction. Sample case 1 shows the offset clearly: the outbound route ends `Left on Road D`, and the return route starts `Begin on Road D` and immediately turns **Right** onto Road C — the flipped version of the turn that *entered* Road C, not the one that entered Road D.

The output format needs a **blank line after each test case**, including the last. Omitting it is a common presentation error.

With $N \leq 40$ the cost is irrelevant; the whole difficulty is the pairing and the parsing.

## Edge cases

- **Road names contain spaces and digits**, so the split must be on the *first* `" on "` only. `100 Feet Road` and `Ganapathi Temple Road` both break a naive split on whitespace, and a split without `maxsplit=1` would also mangle any name containing the word `on`.
- **The turn and the road are offset by one on the way back.** Turn $i$ was what took you *onto* road $i$; returning, that same junction leads you onto road $i-1$. Pairing turn $i$ with road $i$ is the natural mistake and shifts the whole output.
- **`Begin` is never flipped.** It is dropped entirely and replaced by a fresh `Begin on <last road>`.
- **A blank line follows every test case**, including the last one.
- **$N \geq 2$ is guaranteed**, so there is always at least one turn to reverse.
- **Only `Left` and `Right` occur** as turns after the first, so a two-entry lookup table covers every flip.

## Dry run

First sample.

| outward | | return |
|---|---|---|
| Begin on Road A | | Begin on Road D |
| Right on Road B | turn 4 was `Left`, previous road is C | Right on Road C |
| Right on Road C | turn 3 was `Right`, previous road is B | Left on Road B |
| Left on Road D | turn 2 was `Right`, previous road is A | Left on Road A |

Each returned turn is the flip of the turn that *followed* the road being entered.
