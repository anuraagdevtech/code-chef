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
