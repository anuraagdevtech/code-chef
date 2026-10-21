---
topic: Greedy
subtopic: Keeping the heaviest elements apart
time: $O(N)$ per test case
space: $O(1)$
---
$Z$ is the largest sum any pair can make, so adjacent sums are automatically $\leq Z$ and the question is purely whether the pairs achieving **exactly** $Z$ can be kept non-adjacent. Writing $b_1 \geq b_2$ for the two largest values, a pair sums to $Z = b_1 + b_2$ only if its values are precisely $b_1$ and $b_2$.

That splits into two cases.

**The maximum is repeated** ($b_1 = b_2 = m$, occurring $p$ times). The bad pairs are two copies of $m$ side by side, so the $p$ copies must be mutually non-adjacent. Separating $p$ items among $N$ positions is possible exactly when

$$p \leq \left\lceil \frac{N}{2} \right\rceil$$

Sample case 1, $[3,4,4]$, has $p = 2$ against $\lceil 3/2 \rceil = 2$ — just enough, via $4\;3\;4$. Sample case 3, $[2,2]$, has $p = 2$ against $\lceil 2/2 \rceil = 1$, so `NO`.

**The maximum is unique.** Then $b_1$ occurs once and the bad pairs are $b_1$ beside any copy of $b_2$. Placing $b_1$ at an **end** leaves it a single neighbour, which only needs to be some element strictly below $b_2$. So the answer is `YES` exactly when such an element exists — that is, when the count $q$ of $b_2$-valued elements satisfies $N \geq q + 2$.

Sample case 4, $[1,2]$, has $q = 1$ and $N = 2 < 3$, so the $2$ is forced beside the $1$ — `NO`. Sample case 2, $[1,2,3,4]$, has $q = 1$ and $N = 4$, so $4\;1\;3\;2$ works.

Note $N = 2$ always fails under either branch, since the only arrangement puts the top two together.

## Edge cases

- **Two different cases, and $Z$ means different things in each.** When the two largest elements are equal, $Z = 2M$ and only an $M$-beside-$M$ adjacency is forbidden. When the maximum is unique, $Z = M + S$ with $S < M$, and $M$ must simply avoid sitting next to any copy of $S$.
- **Equal maxima**: $p$ copies of $M$ must be mutually non-adjacent, which needs $p \leq \lceil N/2 \rceil$. The third row has two $2$s in an array of two — impossible.
- **Unique maximum**: $M$ goes at an end, so it needs one neighbour strictly below $S$ — requiring at least $q + 2$ elements where $q$ counts the copies of $S$. The last row has $N = 2$ against $q + 2 = 3$, so `NO`.
- **No other adjacency can fail.** Any two non-maximum values sum to at most $2S < M + S = Z$, and $M$ with anything below $S$ is also under $Z$ — so the analysis really does reduce to these two cases.
- **$N = 2$ is always `NO`**, since the single adjacency is exactly $B_N + B_{N-1} = Z$.
- **Sorting descending makes both counts a prefix scan**, and only the top two distinct values are ever inspected.

## Dry run

| array | sorted descending | $Z$ | case | test | output |
|---|---|---:|---|---|---|
| $3,4,4$ | $4,4,3$ | 8 | equal maxima, $p = 2$ | $2 \leq \lceil 3/2 \rceil = 2$ ✓ | `YES` |
| $1,2,3,4$ | $4,3,2,1$ | 7 | unique max, $q = 1$ | $4 \geq 3$ ✓ | `YES` |
| $2,2$ | $2,2$ | 4 | equal maxima, $p = 2$ | $2 \leq 1$ ✗ | `NO` |
| $1,2$ | $2,1$ | 3 | unique max, $q = 1$ | $2 \geq 3$ ✗ | `NO` |

Row 1 works as $4, 3, 4$: sums $7$ and $7$, both under $8$.
