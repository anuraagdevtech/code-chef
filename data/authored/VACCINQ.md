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

## Edge cases

- **Chef himself is included.** The slice runs over the first $P$ people, so position $P$ counts — and $A_P = 1$ is guaranteed, meaning Chef always takes the longer time $Y$.
- **Chef is first** ($P = 1$): only his own time, as in the second sample row.
- **Chef is last** ($P = N$): everyone ahead of him counts, as in the third row.
- **The people behind Chef are irrelevant**, so the array beyond $P$ is never read — the first row has a $1$ at position $4$ that contributes nothing.
- **Input order is $N$, $P$, $X$, $Y$** on one line, then the array.

## Dry run

First sample: $N=4$, $P=2$, $X=3$, $Y=2$, flags $0, 1, 0, 1$.

| position | flag | time | running total |
|---:|---:|---:|---:|
| 1 | 0 | $X = 3$ | 3 |
| 2 | 1 | $Y = 2$ | 5 |

Positions $3$ and $4$ are behind Chef and ignored, so the output is `5`.
