---
topic: Binary Search
subtopic: Searching the answer on a monotonic predicate
time: $O(N \log \max A)$ per test case
space: $O(1)$
---
At speed $K$, a pile of $A_i$ bananas takes $\lceil A_i / K \rceil$ hours, because Chef commits a whole hour to one pile even when the remainder is small. So the total time is

$$f(K) = \sum_{i} \left\lceil \frac{A_i}{K} \right\rceil$$

The key structural fact is that $f$ is **non-increasing** in $K$: eating faster never takes longer. So the predicate "$f(K) \leq H$" is false for small $K$ and true for all $K$ beyond some threshold — exactly the monotone shape that **binary search on the answer** needs.

Search $K$ over $[1, \max A]$; the upper end suffices because at that speed every pile falls in one hour, needing $N \leq H$ hours, which the constraints guarantee.

Each evaluation of $f$ costs one pass, so the whole thing is $O(N \log \max A)$ — about $30$ passes rather than the $10^9$ a linear scan over $K$ would need.

The ceiling must be computed in integers as `(a + k - 1) // k`; a float division would drift at $A_i$ up to $10^9$.

The samples show the threshold moving with the budget. With piles $[1,2,3]$ and $H = 3$ — exactly the number of piles — Chef has one hour per pile, so $K$ must cover the largest pile outright: $K = 3$. Give her one extra hour ($H = 4$) and $K = 2$ suffices, since the $3$-pile may then take two hours.

Sample case 3 lands exactly on the budget: $K = 4$ costs $1+1+1+2 = 5 = H$, and $K = 3$ costs $7$.

## Edge cases

- **Hours needed is non-increasing in the speed $K$**, so the predicate "finishes within $H$ hours" is monotone and the smallest feasible $K$ can be binary searched.
- **A pile takes $\lceil A_i / K \rceil$ hours**, since only one pile may be touched per hour and a partial pile still costs a whole hour — the ceiling is where the problem lives.
- **The search upper bound is $\max A$**, at which every pile takes exactly one hour and the total is $N$ — and $H \geq N$ is guaranteed, so that speed always works and the search never runs off the top.
- **The lower bound is $1$**, not $0$, since a speed of zero finishes nothing.
- **$H = N$ forces $K = \max A$** (the first sample), the tightest case.
- **The ceiling must be integer**, computed as `(a + k - 1) // k`; a float division would misjudge exact multiples.
- **Sums reach $10^5 \times 10^9$** in intermediate totals, so exact integers are needed throughout.

## Dry run

Third sample: piles $4, 3, 2, 7$ with $H = 5$ hours.

| $K$ | hours per pile | total | within $5$? |
|---:|---|---:|:---:|
| 3 | $2, 1, 1, 3$ | 7 | no |
| 4 | $1, 1, 1, 2$ | 5 | **yes** |

So $4$ is the smallest workable speed. Output `4`.
