---
topic: Combinatorics
subtopic: Elementary symmetric polynomials by DP
time: $O(m \min(K, m))$ after an $O(N)$ tally, where $m$ is the number of distinct values
space: $O(m)$
---
A good subsequence never repeats a value, so it is built by **choosing a set of distinct values and then one occurrence of each**. If value $v$ appears $c_v$ times, a chosen set $S$ can be realised in $\prod_{v \in S} c_v$ ways, so the number of good subsequences of size exactly $j$ is the **elementary symmetric polynomial**

$$e_j(c_1, \ldots, c_m) = \sum_{|S| = j} \prod_{v \in S} c_v$$

and the answer is $\sum_{j=0}^{K} e_j$, with $e_0 = 1$ for the empty subsequence.

The $e_j$ come from the standard product expansion $\prod_v (1 + c_v x)$, evaluated as a DP over values: $\mathrm{dp}[j] \mathrel{+}= c_v \cdot \mathrm{dp}[j-1]$, sweeping $j$ downward so each value is used at most once.

The crucial bound is that the $A_i$ are **primes at most $8000$**, of which there are $1007$. So $m \leq 1007$ regardless of $N = 10^5$, and $e_j = 0$ for $j > m$ — you cannot pick more distinct values than exist. Capping $K$ at $m$ turns a nominal $O(NK) = 10^{10}$ into about $10^6$ operations.

For the sample $[2,2,3,3,5]$ with $K = 3$ the multiplicities are $2, 2, 1$, giving $e_0 = 1$, $e_1 = 5$, $e_2 = 2{\cdot}2 + 2{\cdot}1 + 2{\cdot}1 = 8$ and $e_3 = 4$, summing to $18$. Note $e_1 = 5 = N$: picking one element is always $N$ ways, since different occurrences of the same value are different subsequences.

That the values are prime is a red herring — only their distinctness matters — and the input has a single case with no leading $T$.

## Edge cases

- **A good subsequence picks at most one copy of each distinct value**, so the count of good subsequences of size $j$ is the $j$-th elementary symmetric polynomial in the multiplicities — and the answer sums those up to $K$.
- **$K$ can be clamped to the number of distinct values**, since no good subsequence is longer than that — which is what keeps the DP small when $K$ is large.
- **The empty subsequence counts**, which is the $j = 0$ term and the reason `dp[0]` starts at $1$.
- **The inner loop must run downward**, so each value contributes to at most one chosen slot — an upward loop would let a single value be picked twice.
- **The multiplicity is the weight**, not $1$: a value appearing $c$ times offers $c$ distinguishable choices for its slot, which is where the sample's $18$ comes from.
- **The values are primes**, which matters only in that they are distinct as values — the algorithm never uses primality.
- **$A_i \leq 8000$** bounds the distinct count, and the answer is taken modulo $10^9+7$.

## Dry run

Sample: $A = 2, 2, 3, 3, 5$ with $K = 3$, so the multiplicities are $2, 2, 1$ over three distinct values.

| after processing | $j=0$ | $j=1$ | $j=2$ | $j=3$ |
|---|---:|---:|---:|---:|
| start | 1 | 0 | 0 | 0 |
| the two $2$s | 1 | 2 | 0 | 0 |
| the two $3$s | 1 | 4 | 4 | 0 |
| the single $5$ | 1 | 5 | 8 | 4 |

Sum $1 + 5 + 8 + 4 = $ `18`.
