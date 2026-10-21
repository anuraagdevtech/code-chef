---
topic: Basic Math
subtopic: Choosing the cheaper of two targets
time: $O(1)$ per test case
space: $O(1)$
---
There are $X$ face-up cards and $N - X$ face-down ones, and only two possible end states.

- To make everything **face-up**, flip the $N - X$ cards that are currently down.
- To make everything **face-down**, flip the $X$ cards that are currently up.

Each flip changes exactly one card, so each target costs precisely the number of cards not already in that state. The minimum is therefore

$$\min(X,\; N - X)$$

The insight is that both targets are always reachable and their costs are complements summing to $N$, so no search is needed — just take the cheaper. Note the problem does not insist on a particular final direction, only that all cards agree; if it had demanded "all face-up", the answer would be the single value $N - X$.

The extremes confirm the formula. When every card already points the same way the cost is zero, as in sample cases 1 ($X = 0$) and 3 ($X = N$). When the split is exactly even, as in case 2 with $N = 4, X = 2$, both targets cost the same $2$ and the `min` is indifferent.

The identity $\min(X, N - X)$ also says the answer never exceeds $\lfloor N/2 \rfloor$ — you are never worse off than flipping the smaller half.

## Edge cases

- **Already uniform**: $X = 0$ needs no flips (sample row 1), and $X = N$ also needs none, because making them *all* face the other way is equally acceptable. A solution that always flips the $X$ face-up cards returns $3$ instead of $0$ on the sample's third row.
- **An even split** ($N = 4$, $X = 2$): both targets cost $2$, so the tie is harmless.
- **Smallest input** ($N = 2$): $X \in \{0, 1, 2\}$ gives $0$, $1$, $0$.
- The goal is uniformity in *either* direction, which is exactly why the answer is a minimum over two options rather than a single count.

## Dry run

| $N$ | $X$ (face up) | flip the up ones | flip the down ones | output |
|---:|---:|---:|---:|---|
| 5 | 0 | 0 | 5 | `0` |
| 4 | 2 | 2 | 2 | `2` |
| 3 | 3 | 3 | 0 | `0` |
| 10 | 2 | 2 | 8 | `2` |

Rows 1 and 3 are the two already-uniform cases, reached from opposite directions.
