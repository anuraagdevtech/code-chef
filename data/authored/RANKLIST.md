---
topic: Greedy
subtopic: How much deficit a given number of edits can absorb
time: $O(\sqrt{S})$ per test case
space: $O(1)$
---
An ideal rank list is exactly $\{1, 2, \ldots, n\}$ with total $T = \frac{n(n+1)}{2}$. Any valid rank list has sum at most $T$, since sorted it satisfies $a_1 = 1$ and $a_{i+1} \leq a_i + 1$, forcing $a_i \leq i$. So the given list runs a **deficit**

$$D = T - s \geq 0$$

Now ask: with $k$ elements free to change, what is the largest deficit the *rest* of the list can carry while staying a valid rank list? Keeping the smallest $n-k$ values as $1, 2, \ldots, n-k$ and pushing the remaining $k$ as low as the rank-list rule allows — all equal to $n-k$ — gives a shortfall of

$$\sum_{j=n-k+1}^{n} j \;-\; k(n-k) \;=\; \frac{k(k+1)}{2}$$

Neatly, the $n$ cancels: **$k$ edits can absorb at most $\frac{k(k+1)}{2}$ of deficit**, whatever the list length. So the answer is the smallest $k$ with

$$\frac{k(k+1)}{2} \geq D$$

found by walking $k$ upward (or by inverting the triangular number).

Sample case 4, $n=3, s=3$, has $T = 6$ and $D = 3$: one edit absorbs only $1$, two absorb $3$, so the answer is $2$ — the list must have been $\{1,1,1\}$. Sample case 3, $D = 1$, needs a single edit. Sample cases 1 and 2 have $D = 0$ and need none.

With $s$ up to $10^{10}$, $T$ reaches about $5 \times 10^9$, so this is **64-bit** arithmetic outside Python; $k$ never exceeds about $10^5$.

## Edge cases

- **The deficit is $n(n+1)/2 - s$**, and it is never negative: the ideal list has the largest possible sum for a rank list of size $n$, so $s$ can only fall short.
- **$k$ edits can raise the sum by at most $k(k+1)/2$**, independent of $n$ — the best possible is to lift $k$ chosen elements onto the $k$ largest missing ranks. So the answer is the smallest $k$ meeting the deficit.
- **Zero deficit** → $0$ edits, which the first two rows show ($n = 1, s = 1$ and $n = 3, s = 6$ are already ideal).
- **The bound is independent of which rank list the input came from**, which is why only $n$ and $s$ are given and no array is read.
- **Validity is guaranteed**, so the deficit always corresponds to a real rank list and no infeasible case arises.
- **The loop runs $O(\sqrt{S})$ times** at most, around $1.4 \times 10^5$ for $s$ near $10^{10}$ — cheap at $T \leq 10$, though the quadratic formula would also serve.

## Dry run

| $n$ | $s$ | ideal sum | deficit | smallest $k$ with $k(k+1)/2 \geq$ deficit | output |
|---:|---:|---:|---:|---|---:|
| 1 | 1 | 1 | 0 | $k = 0$ | `0` |
| 3 | 6 | 6 | 0 | $k = 0$ | `0` |
| 3 | 5 | 6 | 1 | $k = 1$ (gain 1) | `1` |
| 3 | 3 | 6 | 3 | $k = 2$ (gain 3) | `2` |

The last row starts from $\{1,1,1\}$; changing two elements to $2$ and $3$ gives the ideal list.
