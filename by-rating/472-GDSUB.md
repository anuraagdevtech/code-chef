# 472. Chef and Good Subsequences

> [`GDSUB`](https://www.codechef.com/problems/GDSUB) &middot; difficulty **1999** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Elementary symmetric polynomials by DP |
| **Complexity class** | Quadratic $O(n^2)$ (one-off precomputation) |
| **Time** | $O(m \min(K, m))$ after an $O(N)$ tally, where $m$ is the number of distinct values |
| **Space** | $O(m)$ |

## Question

Chef is given a sequence of prime numbers $A_1, A_2, \ldots, A_N$. This sequence has exactly $2^N$ subsequences. A subsequence of $A$ is *good* if it does not contain any two identical numbers; in particular, the empty sequence is good.

Chef has to find the number of good subsequences which contain at most $K$ numbers. Since he does not know much about subsequences, help him find the answer. This number could be very large, so compute it modulo $1,000,000,007$.

**Input**
- The first line of the input contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
Print a single line containing one integer ― the number of good subsequences with size at most $K$, modulo $1,000,000,007$.

**Constraints**
- $1 \le K \le N \le 10^5$
- $2 \le A_i \le 8,000$ for each valid $i$

**Subtasks**
**Subtask #1 (40 points):** $A_1, A_2, \ldots, A_N$ are pairwise distinct

**Subtask #2 (60 points):** original constraints

## Constraints

- $1 \le K \le N \le 10^5$
- $2 \le A_i \le 8,000$ for each valid $i$

## Sample

**Sample input**

```
5 3
2 2 3 3 5
```

**Sample output**

```
18
```

<details><summary>Explanation</summary>

There is $1$ good subsequence with length $0$, $5$ good subsequences with length $1$, $8$ good subsequences with length $2$ and $4$ good subsequences with length $3$.

</details>

## Approach

A good subsequence never repeats a value, so it is built by **choosing a set of distinct values and then one occurrence of each**. If value $v$ appears $c_v$ times, a chosen set $S$ can be realised in $\prod_{v \in S} c_v$ ways, so the number of good subsequences of size exactly $j$ is the **elementary symmetric polynomial**

$$e_j(c_1, \ldots, c_m) = \sum_{|S| = j} \prod_{v \in S} c_v$$

and the answer is $\sum_{j=0}^{K} e_j$, with $e_0 = 1$ for the empty subsequence.

The $e_j$ come from the standard product expansion $\prod_v (1 + c_v x)$, evaluated as a DP over values: $\mathrm{dp}[j] \mathrel{+}= c_v \cdot \mathrm{dp}[j-1]$, sweeping $j$ downward so each value is used at most once.

The crucial bound is that the $A_i$ are **primes at most $8000$**, of which there are $1007$. So $m \leq 1007$ regardless of $N = 10^5$, and $e_j = 0$ for $j > m$ — you cannot pick more distinct values than exist. Capping $K$ at $m$ turns a nominal $O(NK) = 10^{10}$ into about $10^6$ operations.

For the sample $[2,2,3,3,5]$ with $K = 3$ the multiplicities are $2, 2, 1$, giving $e_0 = 1$, $e_1 = 5$, $e_2 = 2{\cdot}2 + 2{\cdot}1 + 2{\cdot}1 = 8$ and $e_3 = 4$, summing to $18$. Note $e_1 = 5 = N$: picking one element is always $N$ ways, since different occurrences of the same value are different subsequences.

That the values are prime is a red herring — only their distinctness matters — and the input has a single case with no leading $T$.

## Solution

```python
import sys
from collections import Counter

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    counts = Counter(data[2:2 + n]).values()
    m = len(counts)
    # Only m distinct values exist, so no good subsequence is longer than m.
    k = min(k, m)
    dp = [0] * (k + 1)
    dp[0] = 1
    for c in counts:
        # Downward so each value contributes to at most one chosen slot.
        for j in range(min(k, m), 0, -1):
            dp[j] = (dp[j] + c * dp[j - 1]) % MOD
    sys.stdout.write(f"{sum(dp) % MOD}\n")


main()
```

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

---

Same problem grouped by topic: [../docs/combinatorics/GDSUB.md](../docs/combinatorics/GDSUB.md)
