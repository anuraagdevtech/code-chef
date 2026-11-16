---
topic: Dynamic Programming
subtopic: Requirements propagated outwards from the first support that breaks
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Suppose weight is added to support $i$ until it collapses. Its load is then split between its neighbours in some way, and since we only need a non-zero chance, we may pick the most favourable split at every collapse. After support $i$ is gone, the supports to its left and to its right no longer interact: anything a collapsing support sends towards an already destroyed neighbour is lost.

So define `left_need[j]` as the weight that has to arrive, from the right, on support $j - 1$ in order to destroy all of the supports $0 \dots j - 1$. Support $j - 1$ must reach its limit, and it must also hold at least what the supports further left need, because it passes that on when it collapses:

$$\text{left\_need}[j + 1] = \max(A_j,\; \text{left\_need}[j]) - W_j .$$

`right_need` is defined symmetrically from the other end.

If the added weight goes to support $i$, its final load must be at least its own limit and at least the sum of what the two sides need, so the answer for $i$ is

$$\max\bigl(A_i,\; \text{left\_need}[i] + \text{right\_need}[i + 1]\bigr) - W_i .$$

## Edge cases

- A single support just needs $A_1 - W_1$.
- The end supports have an empty side whose need is 0.
- The needs are never negative, since $W_j < A_j$ makes every term at least 1.
- Values reach about $N \cdot 10^9$.

## Dry run

`W = [1, 1234]`, `A = [2, 5678]`.

`left_need`: `[0, 1, 4444]`, from $\max(2, 0) - 1 = 1$ and $\max(5678, 1) - 1234 = 4444$. `right_need`: `[4443, 4444, 0]`, from $\max(5678, 0) - 1234 = 4444$ and $\max(2, 4444) - 1 = 4443$.

- support 1: $\max(2,\; 0 + 4444) - 1 = 4443$
- support 2: $\max(5678,\; 1 + 0) - 1234 = 4444$

Output `4443 4444`.
