---
topic: Basic Math
subtopic: Net progress per cycle, with an odd remainder
time: $O(1)$ per test case
space: $O(1)$
---
The walk repeats a two-second cycle: $+3$ forward, then $-1$ back, for a net gain of $2$ steps every $2$ seconds. So over complete cycles the position simply equals the elapsed time.

**$k$ even.** There are $k/2$ complete cycles, each worth $+2$:

$$\text{position} = \frac{k}{2} \cdot 2 = k$$

**$k$ odd.** There are $(k-1)/2$ complete cycles plus one final forward second:

$$(k - 1) + 3 = k + 2$$

So the answer is $k$ for even $k$ and $k + 2$ for odd $k$ — a pleasingly compact result that is easy to miss if one simulates without looking for the pattern.

The odd case is where the intuition slips. After an odd number of seconds Faizal has just taken a forward step and has not yet staggered back, so he is momentarily *ahead* of his steady-state position by $2$. Sample case 1 shows it: after $5$ seconds he is at $7$, not $5$.

The case $k = 0$ is inside the constraints and gives $0$ — even, so the formula handles it with no special guard.

The constraints are worth reading as a hint: $T$ reaches $10^5$ while the sum of $k$ is bounded by $10^6$, which is the setter signalling that per-test simulation would be acceptable but a closed form is better. Since the closed form is two lines, there is no reason to loop.

## Edge cases

- **$k = 0$**: the answer is $0$, and the constraints do allow it.
- **$k$ even**: exactly $k$, since each two-second cycle of $+3$ then $-1$ nets $+2$ — the position equals the elapsed time.
- **$k$ odd**: $k + 2$. The final second is a $+3$ with no matching $-1$ yet, so the walker is caught mid-stagger two units ahead of the steady rate. For $k = 1$ that is $3$, and for $k = 3$ it is $+3, -1, +3 = 5$.
- **Largest input** ($k = 10^5$, with the sum of $k$ bounded at $10^6$): the closed form means the bound never bites, where simulating second by second would.

## Dry run

| $k$ | parity | steps | position | output |
|---:|---|---|---:|---|
| 5 | odd | $+3, -1, +3, -1, +3$ | 7 | `7` |
| 11 | odd | five full cycles then $+3$ | 13 | `13` |
| 23 | odd | eleven full cycles then $+3$ | 25 | `25` |

All three samples are odd; an even $k$ such as $4$ would give $+3,-1,+3,-1 = 4$.
