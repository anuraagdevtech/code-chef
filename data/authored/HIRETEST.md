---
topic: Strings
subtopic: Counting characters, then a two-branch rule
time: $O(N \cdot M)$ per test case
space: $O(N)$
---
For each candidate, count the full solves $F$ and the partial solves $P$ in their result string. The pass rule has two independent routes:

$$F \geq X \quad\text{or}\quad \bigl(F = X - 1 \text{ and } P \geq Y\bigr)$$

The second branch is narrow and precise: it applies at **exactly** $X-1$ full solves, not at "fewer than $X$". A candidate with $X-2$ full solves cannot compensate with any number of partials. Sample case 3 is built on this — one candidate with $X = 2$, zero full solves and three partials fails, because $0 \neq X - 1 = 1$.

Within the first test case, candidates 2 and 3 both have $F = 2 = X - 1$ and differ only in partials: $P = 2$ passes against $Y = 2$, while $P = 1$ does not. Those two rows isolate the second branch exactly.

The `U` characters never enter the rule, so they can be ignored entirely rather than counted.

Output formatting is the other thing to get right: the $N$ results are printed as a single line of digits with **no separators** — `1100`, not `1 1 0 0`. Joining the per-candidate characters and emitting one line per test case does it.

The constraint $1 \leq (X-1) + Y \leq M$ guarantees the second route is always attainable in principle, so neither branch is vacuous.
