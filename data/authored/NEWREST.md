---
topic: Combinatorics
subtopic: Stirling numbers of the second kind times a falling factorial
time: $O(N_{\max}^2 + \sum \min(N, M, K))$
space: $O(N_{\max} + T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Count the schedules that use exactly $j$ distinct dishes and sum over $j \le K$.

Using exactly $j$ dishes means splitting the $N$ days into $j$ non-empty groups (days with the same dish) and giving the groups distinct dishes. The number of splittings is the Stirling number of the second kind $S(N, j)$, and the dishes can be assigned in $M (M-1) \cdots (M-j+1)$ ways, so

$$\text{answer} = \sum_{j=1}^{\min(N, M, K)} S(N, j) \cdot M^{\underline{j}}.$$

The Stirling row is advanced in place with $S(n, j) = j \cdot S(n-1, j) + S(n-1, j-1)$; test cases are grouped by $N$ and answered when their row is reached. $M$ can be a million but only the first $\min(N, K)$ factors of the falling factorial are needed.

## Edge cases

- $j$ cannot exceed $N$ (days), $M$ (dishes) or $K$ (limit).
- $K \ge N$ and $M \ge N$ gives all $M^N$ schedules.
- The in-place row update must run from high $j$ to low $j$.
- Everything is modulo $10^9 + 7$.

## Dry run

`N = 4, M = 3, K = 2`. $S(4, 1) = 1$, $S(4, 2) = 7$.

- one dish: $1 \cdot 3 = 3$
- two dishes: $7 \cdot (3 \cdot 2) = 42$

Answer 45.
