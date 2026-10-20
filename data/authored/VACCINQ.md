---
topic: Arrays
subtopic: Prefix sum with a per-element lookup
time: $O(P)$ per test case
space: $O(1)$
---
Chef is $P$-th in the queue and nobody is served out of order, so his vaccination finishes once everyone from position $1$ to position $P$ — **including himself** — has been done. Each person costs $Y$ minutes if elderly ($A_i = 1$) or $X$ if a child ($A_i = 0$):

$$\sum_{i=1}^{P} \begin{cases} Y & A_i = 1 \\ X & A_i = 0 \end{cases}$$

Two off-by-one risks sit here. The sum must run **through** $P$, not stop before it — the question asks when Chef's own vaccination completes, not when it starts. And the array is one-indexed in the statement but zero-indexed in code, so the slice is `a[:p]`.

The guarantee $A_P = 1$ confirms Chef is elderly, as the statement says, so his own cost is $Y$. It is a consistency check rather than something the code must enforce.

The people **behind** Chef are irrelevant — the array may be longer than $P$, and everything past position $P$ is ignored. Sample case 1 has a fourth person who never enters the calculation.

Working through case 1: positions $1$ and $2$ hold a child and an elder, costing $X + Y = 3 + 2 = 5$. Case 3 has three elders at $2$ minutes each for $6$.

Since only the first $P$ entries matter, the scan is $O(P)$ rather than $O(N)$ — immaterial at these bounds, but the right shape.
