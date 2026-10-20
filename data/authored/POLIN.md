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
