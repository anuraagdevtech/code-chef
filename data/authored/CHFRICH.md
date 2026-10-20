---
topic: Basic Math
subtopic: Exact division from a guaranteed divisor
time: $O(1)$ per test case
space: $O(1)$
---
Chef starts at $A$ billion and gains $X$ billion per year, needing to reach $B$. The shortfall is $B - A$, so the time required is

$$\frac{B - A}{X}$$

The constraints do two kind things here. $A < B$ guarantees the gap is strictly positive, so no clamping is needed and the answer is at least $1$. And **$X$ divides $B - A$**, which makes the division exact — no ceiling, no rounding rule.

That second guarantee is worth noticing rather than assuming. Without it the answer would be $\lceil (B-A)/X \rceil$, since a partial year still counts as a year in which the target is reached. Problems in this set go both ways, and the constraint block is where the setter tells you which.

The statement's remark that the current richest are not growing is there to rule out a moving target — Chef's goal $B$ is fixed, so this is a simple division rather than a pursuit problem.

Sample case 2 is the one that exercises the division: a gap of $88$ at $11$ per year gives exactly $8$. Case 3 is the one-year case, and case 1 the round $100/10$.

With $T$ up to $21{,}000$, reading the whole input at once and writing one joined block matters more than the arithmetic.
