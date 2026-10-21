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
