---
topic: Dynamic Programming
subtopic: Bounded compositions via a prefix-sum convolution
time: $O(nm)$ per test case
space: $O(n)$
---
The dishes are indistinguishable, so a distribution is a tuple $(d_1, \ldots, d_m)$ with $x_i \leq d_i \leq y_i$ and $\sum d_i = n$ — a **bounded composition** of $n$. Processing cooks one at a time gives

$$\mathrm{dp}_i[j] = \sum_{d = x_i}^{\min(y_i,\, j)} \mathrm{dp}_{i-1}[j - d]$$

with $\mathrm{dp}_0[0] = 1$. Done literally this is $O(nm \cdot 101)$ per test, and with $T = 50$ that is tens of millions of operations for no reason.

The inner sum is a **contiguous window** of the previous row, so one prefix-sum array $P[j] = \sum_{u \leq j} \mathrm{dp}_{i-1}[u]$ collapses it to a subtraction:

$$\mathrm{dp}_i[j] = P[j - x_i] - P[j - y_i - 1]$$

treating out-of-range indices as $0$. Each cook is then $O(n)$ and the whole test $O(nm)$. Doing the subtraction under the modulus can go negative, so add $\mathrm{MOD}$ before reducing.

One edge case the bounds permit: $x_i$ and $y_i$ are independent, so a cook may have $x_i > y_i$ — an empty range, making the answer $0$ outright. Also $x_i$ may be $0$, so a cook can be given nothing.

The sample has $n = 3$ with ranges $[0,3]$ and $[1,3]$. The three distributions are $(0,3)$, $(1,2)$ and $(2,1)$; $(3,0)$ is excluded because the second cook must receive at least one dish. Note that *every* dish must be handed out — the count is of distributions summing to exactly $n$, not at most $n$.

## Edge cases

- **A prefix sum turns the inner loop from $O(n)$ into $O(1)$.** The transition sums the previous row over the window $[j - y_i,\, j - x_i]$, and without the prefix array the DP would be $O(nm \cdot n)$.
- **The window must be clipped at zero**, since $j - y_i$ can be negative — and skipped entirely when $j - x_i < 0$, which means cook $i$ cannot even meet their minimum.
- **An empty range ($x_i > y_i$) admits nothing**, so the whole count collapses to $0$; the explicit check avoids relying on the window arithmetic to produce it.
- **$x_i$ may be $0$**, letting a cook take nothing — the sample's first cook has a minimum of $0$.
- **Only $dp[n]$ is read at the end**, so distributions that use fewer than $n$ dishes are correctly excluded.
- **The modular subtraction needs a final `%`**, because `pref[top+1] - pref[bottom]` can be negative after reduction.
- **$n, m \leq 100$** keeps the table at $10^4$ transitions per case, trivial at $T \leq 50$.

## Dry run

Sample: $n = 3$ dishes, cooks with ranges $[0,3]$ and $[1,3]$.

| cook 1 takes | cook 2 takes | valid? |
|---:|---:|:---:|
| 0 | 3 | yes |
| 1 | 2 | yes |
| 2 | 1 | yes |
| 3 | 0 | **no** (below cook 2's minimum of 1) |

Output `3`.
