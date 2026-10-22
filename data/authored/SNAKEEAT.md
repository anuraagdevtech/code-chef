---
topic: Binary Search
subtopic: Feasibility check with prefix sums
time: $O((N + Q) \log N)$ per test case
space: $O(N)$
---
Suppose we aim to end with $m$ snakes of length at least $K$. Two greedy choices are forced.

**Keep the $m$ longest.** They start closest to the target, so any other choice needs at least as much feeding.

**Feed them the $N - m$ shortest.** Each snake eaten adds exactly $1$ to its eater, so the sacrifices are interchangeable — only their *count* matters.

So after sorting, the kept snakes are the suffix $L[N-m \ldots N-1]$, and the total feeding needed is the sum of their shortfalls:

$$\text{deficit}(m) = \sum_{i=N-m}^{N-1} \max(0,\ K - L_i)$$

which must not exceed the $N - m$ available meals.

As $m$ grows the deficit rises while the supply falls, so feasibility is **monotone** — binary search on $m$ answers each query in $O(\log N)$.

The deficit itself is computed in $O(\log N)$ rather than $O(m)$: binary search for the first index whose length already reaches $K$, then take a prefix-sum slice of everything below it. Without that, the queries would be $O(NQ)$ overall.

The eating rule $L_i \geq L_j$ is automatically respected, since every kept snake is at least as long as every sacrificed one.

Sample case 1 with $K = 10$ keeps $[9,10,21]$: only the $9$ falls short, by $1$, and two meals are available — so $3$ snakes. Pushing to $m = 4$ would need $3$ meals with only $1$ left. At $K = 15$ even $m = 2$ needs $5$ meals against $3$, so the answer drops to $1$.

Sample case 2 asks for length $100$ from snakes topping out at $5$, needing $95$ meals from four — so $0$.

## Edge cases

- **Keeping the longest snakes is optimal**, so for a target count $m$ the survivors are the top $m$ after sorting — and everything else becomes food.
- **The feasibility check is a prefix sum.** Among the survivors, those still below $K$ need $K - L_i$ feeds each, and the total must not exceed the $n - m$ snakes available as food.
- **The predicate is monotone in $m$** — fewer survivors means more food and less demand — so the answer is binary searched.
- **Survivors already at or above $K$ need nothing**, which is why the demand is summed only over the prefix below $K$, found by one `bisect_left`.
- **An unreachable $K$ gives $0$.** The second sample asks for length $100$ from snakes of length at most $5$; even one survivor would need $95$ feeds against four available, so no snake qualifies.
- **A feed gives exactly $+1$**, so the demand is linear in the shortfall and no scheduling subtlety arises.
- **$L_i$ and $K$ reach $10^9$ with $n$ at $10^5$**, so the demand can reach $10^{14}$ — past 32-bit.

## Dry run

First query of the first sample: lengths sorted to $5, 8, 9, 10, 21$ with $K = 10$.

| survivors $m$ | kept snakes | those below $10$ | feeds needed | food available | feasible? |
|---:|---|---|---:|---:|:---:|
| 3 | $9, 10, 21$ | just the $9$ | 1 | 2 | yes |
| 4 | $8, 9, 10, 21$ | $8$ and $9$ | $2 + 1 = 3$ | 1 | no |

So `3` snakes can reach length $10$.
