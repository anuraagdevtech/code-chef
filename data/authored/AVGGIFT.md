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

## Edge cases

- **The array may be any finite length with repeats**, so the reachable means are exactly the weighted averages of elements of $S$ — which fill the whole closed interval $[\min S, \max S]$ at every integer point.
- **So the test is just $\min S \leq X \leq \max S$**, and nothing between the extremes matters. The second row fails because $X = 5$ sits above the only element, $3$.
- **The construction is explicit**: taking $\max S - X$ copies of $\min S$ and $X - \min S$ copies of $\max S$ gives a mean of exactly $X$, with both counts non-negative integers.
- **$X$ itself being in $S$** makes a one-element array work (the fourth row).
- **$N = 1$** forces $X$ to equal that single element, which both bounds then demand.
- **Both ends are inclusive**, so $X = \min S$ or $X = \max S$ succeeds.
- **The elements are distinct and positive**, so the interval is non-degenerate whenever $N \geq 2$.

## Dry run

| $N$ | $X$ | $S$ | $\min$ | $\max$ | in range? | output |
|---:|---:|---|---:|---:|:---:|---|
| 3 | 2 | $1,2,3$ | 1 | 3 | yes | `YES` |
| 1 | 5 | $3$ | 3 | 3 | no | `NO` |
| 2 | 5 | $4,6$ | 4 | 6 | yes | `YES` |
| 1 | 5 | $5$ | 5 | 5 | yes | `YES` |

Row 3 is realised by $[4, 6]$: one of each, mean $5$.
