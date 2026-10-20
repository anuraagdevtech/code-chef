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
