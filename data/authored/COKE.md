---
topic: Basic Math
subtopic: Closed form for a drift-to-target process
time: $O(N)$ per test case
space: $O(1)$
---
Each can drifts one degree per minute toward the ambient temperature $K$, and snaps exactly onto $K$ once it is within one degree. So from a starting gap $d = |C - K|$, the can reaches $K$ after exactly $d$ minutes — $d-1$ minutes of drifting down to a gap of $1$, then one more to snap.

That gives a closed form after $M$ minutes, with no simulation:

$$\text{final} = \begin{cases} K & M \geq d \\ C - M & C > K \\ C + M & C < K \end{cases}$$

Then keep the cheapest can whose final temperature lands in $[L, R]$, or report $-1$.

The snapping rule is what makes this exact rather than asymptotic — without it, a can would approach $K$ but the last step would need care. With it, once the gap is at most $1$ the next minute closes it entirely.

Sample case 1 has ambient $5$ and $M = 2$. The can at $1$ reaches $3$ (gap $4$, only two minutes of drift) — outside $[4,6]$. The can at $2$ reaches $4$, and the can at $8$ reaches $6$; both qualify, so the cheaper one at price $8$ wins. Note the **cheapest valid** can is wanted, not the coldest or the closest.

Sample case 2 has all cans far above a cold ambient with only five minutes to cool, so none reaches the required range.

Temperatures may be negative — the constraints allow $|C_i|, |K| \leq 50$ and $L$ down to $-50$ — so no positivity may be assumed anywhere.
