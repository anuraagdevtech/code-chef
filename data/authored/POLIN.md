---
topic: Sets
subtopic: Counting distinct coordinates independently
time: $O(N)$ per test case
space: $O(N)$
---
Each point contributes one vertical line at $x = x_i$ and one horizontal line at $y = y_i$. The statement defines distinctness per axis: two vertical lines coincide exactly when their $x$ values match, and likewise for horizontal and $y$.

So the two families never interfere, and the answer is simply

$$|\{x_1, \ldots, x_N\}| + |\{y_1, \ldots, y_N\}|$$

— two independent distinct-counts, added.

The trap is treating the lines as a single collection and deduplicating across axes. A vertical line at $x = 5$ and a horizontal line at $y = 5$ share a number but are different lines, so they must be counted separately. Keeping two sets rather than one avoids the question entirely.

Sample case 2 shows heavy overlap on one axis: five points all share $x = 0$, collapsing to a single vertical line, while their five distinct $y$ values give five horizontal lines — $6$ in total, not $10$.

Sample case 1 has four points forming a unit square, with two distinct $x$ and two distinct $y$, so $4$ lines. Sample case 3 is a single point contributing one of each.

Coordinates reach $10^9$, so hashing into a Python `set` is the right structure — an array indexed by coordinate is out of the question. With the sum of $N$ at $10^5$, two sets per test case are comfortable.

## Edge cases

- **The two axes are counted independently**, so a shared numeric value does not merge anything: the third row's single point at $(10, 10)$ contributes one vertical and one horizontal line, for $2$.
- **All points on one vertical line** (the second row): one vertical line plus $N$ distinct horizontal ones, giving $6$ for $N = 5$.
- **Duplicate points** would collapse on both axes at once, which the sets handle with no extra logic.
- **Coordinate $0$ is allowed**, so the origin is an ordinary point and the tokens include `0`.
- **Comparing raw byte tokens is safe** here, since the input has no leading zeros or negative numbers and each value therefore has exactly one spelling.
- **The strided slices read the $x$ and $y$ columns in one pass** without materialising a list of points, which matters at $\sum N = 10^5$.

## Dry run

| points | distinct $x$ | distinct $y$ | output |
|---|---|---|---:|
| $(1,1), (1,0), (0,1), (0,0)$ | $\{0, 1\}$ → 2 | $\{0, 1\}$ → 2 | `4` |
| $(0,0) \dots (0,4)$ | $\{0\}$ → 1 | $\{0,1,2,3,4\}$ → 5 | `6` |
| $(10, 10)$ | $\{10\}$ → 1 | $\{10\}$ → 1 | `2` |
