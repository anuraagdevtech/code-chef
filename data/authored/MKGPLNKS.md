---
topic: Strings
subtopic: Counting runs
time: $O(N)$ per test case
space: $O(1)$
---
The spreading rule means painting a plank repaints its **entire maximal run** of equal colour — the change propagates to any neighbour sharing the old colour, and onward from there. So the plank's identity hardly matters; what matters is the run it currently sits in.

Collapse the string into runs. If there are $k$ runs, then painting a plank in a run that has neighbours on *both* sides flips that run to the other colour, merging it with both neighbours and turning three runs into one — **$k$ drops by $2$** per operation. Repeating from a well-chosen interior position drives $k$ down to $1$, and the answer is

$$\left\lfloor \frac{k}{2} \right\rfloor$$

Both parities land correctly: an odd $k$ reaches $1$ after $(k-1)/2$ merges, and an even $k$ reaches $2$ and then needs one final paint to merge the last pair — which is $k/2$ in total. The floor expresses both.

Ryan is restricted to **one** plank, repainted repeatedly, and that is fine: after each merge the chosen plank still sits inside the new combined run, which keeps absorbing its neighbours.

The samples walk the cases. `BBWWWB` has runs `BB | WWW | B`, so $k=3$ and one paint of the middle run turns everything black. `WWBWB` has $k=4$ and needs two. `BB` is already uniform at $k=1$. `WWBBBBBWW` has $k=3$ again, needing one.

Counting runs is a single pass comparing each character with its predecessor, which keeps this $O(N)$ at $\sum N = 10^5$.

## Edge cases

- **One operation removes two runs, not one.** Painting a plank repaints its whole run and the propagation merges it with the runs on both sides, turning three runs into one — so the answer is $\lceil (\text{runs} - 1)/2 \rceil$, which equals $\lfloor \text{runs}/2 \rfloor$.
- **The chosen run must be interior to get the full benefit.** Painting the first or last run merges only two runs into one, so $4$ runs would take three operations instead of two; always picking an interior run is what achieves the bound.
- **Already uniform** (the third row, `BB`) → one run and $0$ operations.
- **Even and odd run counts behave differently**: $3$ runs need $1$ operation and $4$ need $2$, which the floor division captures.
- **Only two colours exist**, so runs strictly alternate and the run count is one more than the number of adjacent mismatches.
- **Sum of $N \leq 10^5$**: a single pass counting mismatches, with the length token skipped.

## Dry run

| $S$ | runs | $\lfloor \text{runs}/2 \rfloor$ |
|---|---|---:|
| `BBWWWB` | `BB`, `WWW`, `B` → 3 | `1` |
| `WWBWB` | `WW`, `B`, `W`, `B` → 4 | `2` |
| `BB` | `BB` → 1 | `0` |
| `WWBBBBBWW` | `WW`, `BBBBB`, `WW` → 3 | `1` |

In the last row, painting any of the five `B`s white turns the whole string white in one move.
