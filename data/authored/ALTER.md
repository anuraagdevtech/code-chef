---
topic: Number Theory
subtopic: Divisibility plus an alternation constraint
time: $O(1)$ per test case
space: $O(1)$
---
Alice gains $A$ on each of her work days and Bob gains $B$ on each of his, so reaching exactly $P$ and $Q$ requires

$$a = \frac{P}{A}, \qquad b = \frac{Q}{B}$$

to both be **whole numbers** — otherwise the targets are simply unreachable.

But divisibility alone is not enough, and this is where the problem has its teeth. Because they work on **alternating** days, after $d$ days one of them has worked $\lceil d/2 \rceil$ times and the other $\lfloor d/2 \rfloor$. So the two work counts can never differ by more than one:

$$|a - b| \leq 1$$

That covers all three legal shapes — equal counts after an even number of days, or one ahead after an odd number — and it does not matter which of them takes the odd days, since both orderings are allowed.

Sample case 2 shows divisibility passing while the alternation fails: $P = 3$ with $A = 1$ needs three Alice-days, but $Q = 2$ with $B = 2$ needs only one Bob-day, and a gap of $2$ is impossible. Sample case 4 is the same failure with a gap of $2$ between three and five.

Sample case 3 is the off-by-one case that must be **accepted**: $a = 1$ and $b = 2$ differ by exactly one, which happens naturally after three days with Bob starting.

A strict equality check would reject it, and a check omitting the gap entirely would accept cases 2 and 4 — both halves are load-bearing.
