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

## Edge cases

- **The snap is what makes the timing exact.** Once the temperature is within one degree of $K$, the next minute lands it precisely on $K$ — so a can starting $g$ degrees away reaches ambient after exactly $g$ minutes, never $g-1$ or $g+1$.
- **A can already at ambient stays there** for any walk length, which the $m \geq g$ branch covers with $g = 0$.
- **Cheapest, not coldest.** The first sample has two qualifying cans; the one at price $8$ wins over the one at price $10$ even though both land inside $[L, R]$.
- **No qualifying can** → $-1$ (the second sample, where every can cools to $16$–$18$ against a window of $[20, 30]$).
- **Temperatures and the window may be negative** ($|C_i|, |K| \leq 50$ and $-50 \leq L$), so the drift direction must be chosen by comparison rather than assumed.
- **Both endpoints are inclusive**, and the first sample's winner lands exactly on $L = 4$.
- **$M \geq 1$** by the constraints, so the zero-walk case never arises in practice though the formula handles it.

## Dry run

First sample: $M = 2$ minutes, ambient $K = 5$, window $[4, 6]$.

| can | start $C$ | gap $|C - K|$ | $M \geq$ gap? | temperature on arrival | in $[4,6]$? | price |
|---:|---:|---:|:---:|---:|:---:|---:|
| 1 | 1 | 4 | no | $1 + 2 = 3$ | no | — |
| 2 | 2 | 3 | no | $2 + 2 = 4$ | yes | **8** |
| 3 | 8 | 3 | no | $8 - 2 = 6$ | yes | 10 |

Output `8`.
