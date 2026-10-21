---
topic: Bit Manipulation
subtopic: One power of two dominates all the lower ones
time: $O(N)$ per test case
space: $O(1)$
---
Since $2^{k} > 2^{k-1} + 2^{k-2} + \cdots + 1$, the **largest-index term dominates** any subarray: in $C[l..r]$ the term $\pm 2^{r-1}$ outweighs everything before it combined. So

$$\mathrm{sign}\bigl(\textstyle\sum_{i=l}^{r} C_i\bigr) = B_r$$

The left endpoint is irrelevant, and no subarray sums to zero.

So every subarray ending at $r$ is positive when $B_r = +1$ and negative when $B_r = -1$ — and there are exactly $r$ such subarrays, one for each $l \in \{1, \ldots, r\}$. Therefore

$$P - Q = \sum_{r=1}^{N} B_r \cdot r$$

and the answer is its absolute value. One pass, no subarray enumeration — which matters, since there are $\binom{N+1}{2}$ of them.

Sample case 1, $B = [1,-1,1,1]$, gives $1 - 2 + 3 + 4 = 6$. Sample case 3, $B = [1,-1]$, gives $1 - 2 = -1$, so the answer is $1$ — the absolute value is what makes $P < Q$ harmless.

The dominance argument is the whole problem; recognising that the sign depends only on the *last* element is what collapses a quadratic count into a linear sum.

With $N$ up to $10^5$ the weighted sum reaches about $5 \times 10^9$, which **exceeds 32 bits** — worth noting outside Python.

## Edge cases

- **The last term dominates the whole subarray.** Since $2^{r-1} > 2^{r-2} + \dots + 2^{l-1}$, the sign of $C_l + \dots + C_r$ is exactly the sign of $B_r$ — so only the right endpoint matters.
- **No subarray sums to zero**, which is why $P + Q$ covers every subarray and the signed count telescopes cleanly into $\sum_r B_r \cdot r$.
- **There are $r$ subarrays ending at position $r$**, so each $B_r$ is weighted by its own index — not by $1$, and not by the count of subarrays containing it.
- **All signs the same** (the second row, every $B_i = -1$) gives the full triangular total, $1 + 2 + 3 = 6$ in magnitude.
- **The answer is an absolute value**, so a $Q$ larger than $P$ is fine; the second and first rows both give $6$ with opposite signs inside.
- **Cancellation is possible**: $[1, -1]$ gives $1 - 2 = -1$, so the answer can be small even on a short array.
- **Sum of $N \leq 3 \cdot 10^5$** with totals near $5 \times 10^9$ at $N = 10^5$ — past 32-bit.

## Dry run

First sample: $B = +1, -1, +1, +1$, so $C = 1, -2, 4, 8$.

| $r$ | $B_r$ | subarrays ending at $r$ | contribution |
|---:|---:|---:|---:|
| 1 | $+1$ | 1 | $+1$ |
| 2 | $-1$ | 2 | $-2$ |
| 3 | $+1$ | 3 | $+3$ |
| 4 | $+1$ | 4 | $+4$ |

$P - Q = 6$, so the output is `6`. For instance $C_1 + C_2 = -1 < 0$, matching $B_2 = -1$.
