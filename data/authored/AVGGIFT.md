---
topic: Basic Math
subtopic: Mean reachability as a sign condition
time: $O(N)$ per test case
space: $O(1)$
---
An array with elements $S_i$ repeated $c_i \geq 0$ times has mean $X$ exactly when

$$\sum_i c_i S_i = X \sum_i c_i \quad\Longleftrightarrow\quad \sum_i c_i\,(S_i - X) = 0$$

with the $c_i$ not all zero. So the problem is whether the shifted values $S_i - X$ admit a non-trivial non-negative integer combination summing to zero.

That is possible in exactly two ways:

- some $S_i - X$ is **zero** — then the one-element array $[X]$ works;
- some value is **positive** and another **negative** — if $p > 0$ and $-q < 0$ are available, take $q$ copies of the first and $p$ copies of the second, giving $qp - pq = 0$.

If every shifted value has the same strict sign, every non-trivial sum inherits that sign and can never vanish. Combining the cases, the condition collapses to a range test:

$$\text{answer} = \text{YES} \iff \min S \leq X \leq \max S$$

The array may be as long as needed, so there is no size constraint to worry about — the integer multiples above are always allowed.

The samples cover the three shapes. $S = \{1,2,3\}$ with $X = 2$ contains $X$ outright. $S = \{4,6\}$ with $X = 5$ has values on both sides, so $[4,6]$ has mean $5$ even though $5 \notin S$. $S = \{5\}$ with $X = 5$ is the degenerate single-element case, `YES`. And $S = \{3\}$ with $X = 5$ is out of range — every element is $3$, so every mean is $3$.
