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
