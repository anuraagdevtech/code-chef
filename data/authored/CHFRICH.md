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

## Edge cases

- **$X$ is guaranteed to divide $B - A$**, so the division is exact and there is no rounding decision to make. Without that guarantee the problem would have to settle whether a partial step counts.
- **$A < B$ is guaranteed**, so the difference is always positive and no absolute value is needed.
- **The smallest qualifying gap** (the third row: a gap of $10$ with $X = 10$): one step.
- **$X = 1$**: the answer is the full difference $B - A$.
- **Largest gap** ($A = 100$, $B = 200$ with $X = 1$): $100$.

## Dry run

| $A$ | $B$ | gap $B-A$ | $X$ | $\text{gap}/X$ | output |
|---:|---:|---:|---:|---:|---|
| 100 | 200 | 100 | 10 | 10 | `10` |
| 111 | 199 | 88 | 11 | 8 | `8` |
| 190 | 200 | 10 | 10 | 1 | `1` |
