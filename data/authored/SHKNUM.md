---
topic: Binary Search
subtopic: Precomputed candidate set with a bisect
time: $O(\log C)$ per test case after an $O(C \log C)$ precomputation
space: $O(C)$
---
The targets $M = 2^x + 2^y$ with $x \neq y$ are numbers with **exactly two set bits**, and there are very few of them below the bound: $N \leq 10^9 < 2^{30}$, so taking $x < y \leq 31$ covers every target that could be nearest, giving only $\binom{32}{2} = 496$ candidates.

Since the cost is $|N - M|$, the answer is the distance to the nearest candidate. With the candidates sorted once, each query is a binary search plus a comparison of the two neighbours:

$$\text{answer} = \min_{M \in \mathcal{C}} |N - M|$$

Both neighbours must be checked — the nearest candidate can lie on either side, and for $N = 22$ it is a tie: $20 = 16+4$ below and $24 = 16+8$ above, each $2$ away. The upper neighbour must exist, which is why the candidate list is generated past $10^9$ (up to $2^{31} + 2^{30}$) rather than stopping at it.

Generating candidates and bisecting is what makes $T = 10^5$ trivial; scanning all 496 per query would also pass, but the bisect makes the per-query cost logarithmic.

The samples show the three shapes. $N = 10 = 8 + 2$ is already a target, so $0$. $N = 4$ needs $1$ — note $4 = 2^2$ has a single set bit, so a *power of two* is never a target, and its nearest neighbours are $3 = 1+2$ and $5 = 1+4$. And $22 = 10110_2$ has three set bits, needing $2$.

## Edge cases

- **$2^x + 2^y$ with $x \neq y$ is exactly "two set bits"**, so the candidate set is just $\binom{32}{2} = 496$ numbers — small enough to build once and binary-search per query.
- **Both neighbours must be checked.** For $N = 4$ the nearest candidates are $3$ below and $5$ above, each one away; taking only the upper one still gives $1$ here, but $N = 2^{30}$ would be badly wrong.
- **$N$ may already qualify** → $0$, as in the first row where $10 = 1010_2$.
- **The lower neighbour may not exist.** The smallest candidate is $3$, so for $N \in \{1, 2\}$ the `if i:` guard is what stops an index of $-1$ silently wrapping to the largest candidate.
- **An upper neighbour always exists** for $N \leq 10^9$, since $2^{30} + 2^{29} \approx 1.6 \times 10^9$ is in the table — so `targets[i]` is always safe.
- **$32$ bits are enough** and $31$ would not be: the table must reach past $10^9$.
- **$T$ up to $10^5$** with one bisect each.

## Dry run

Candidates near the queries: $\dots, 3, 5, 6, 9, 10, 12, 17, 18, 20, 24, \dots$

| $N$ | binary | lower candidate | upper candidate | best distance |
|---:|---|---:|---:|---:|
| 10 | $1010$ | — ($N$ itself) | 10 | `0` |
| 22 | $10110$ | 20 | 24 | `2` |
| 4 | $100$ | 3 | 5 | `1` |

Row 2 is equidistant both ways; row 3 shows the lower side winning as readily as the upper.
