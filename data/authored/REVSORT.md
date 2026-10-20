---
topic: Arrays
subtopic: Constraining which inversions may be undone
time: $O(N)$ per test case
space: $O(N)$
---
Reversing a subarray of length $2$ is just swapping an adjacent pair, so the pair $(x, y)$ can be swapped only when $x + y \leq X$. That single observation drives everything.

**Necessity.** If two elements $x$ and $y$ satisfy $x + y > X$, they can never cross each other — not directly, and not by any sequence of moves, since any reversal that reorders them relative to one another would have to contain both and therefore have sum exceeding $X$. So every pair that is **out of order** in the input must be cheap enough to swap:

$$\text{for all } i < j \text{ with } A_i > A_j: \quad A_i + A_j \leq X$$

**Sufficiency.** If that holds, bubble sort works: it only ever swaps adjacent pairs that are currently inverted, and any pair inverted now was inverted in the original array, so its sum is within budget.

Checking all pairs is $O(N^2)$, but only the **worst** inversion matters. Sweeping left to right with a running prefix maximum, each position $j$ contributes the candidate $\max(A_1 \ldots A_{j-1}) + A_j$ whenever that maximum exceeds $A_j$. The answer is `YES` exactly when the largest such candidate is at most $X$ — or when no inversion exists at all.

The already-sorted case is where this matters most. Sample case 1 is $[1,2,3,4]$ with $X = 1$: nothing can be swapped, but nothing needs to be, so `YES`. Sample case 2 is the same tiny budget with one inversion, $2$ before $1$, costing $3 > 1$ — `NO`. Sample case 3 has inversions costing at most $5$, inside the budget of $7$.
