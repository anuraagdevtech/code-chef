---
topic: Basic Math
subtopic: Ceiling division over a distance
time: $O(1)$ per test case
space: $O(1)$
---
The gap to close is $|A - B|$, and a step covers **at most** $K$ units. Since Chef may step any distance up to $K$, the best strategy is full-length steps until the final one, which covers whatever remains:

$$\left\lceil \frac{|A - B|}{K} \right\rceil$$

The phrase "at most $K$" is what makes this a clean ceiling rather than something harder. If a step had to be *exactly* $K$, Chef could overshoot and the answer would involve parity and reachability. Being free to take a shorter final step means the remainder never costs more than one extra move.

Two guards are built in. The absolute value handles Chefina being to the left of Chef, as in sample case 4 where the walk goes from $30$ down to $4$. And a gap of zero yields zero steps — sample case 2, where they already share a coordinate — which the ceiling gives for free since $\lceil 0/K \rceil = 0$.

Sample case 3 is the overshoot-allowed case: a gap of $46$ with $K = 100$ takes a single step, because Chef may move *less* than the maximum.

In integers the ceiling is `(d + k - 1) // k`.

## Edge cases

- **Already at the destination** ($A = B = 36$): the distance is $0$, so no moves — and $\lceil 0/K \rceil = 0$ needs no clamp.
- **One jump is enough** ($A = 50$, $B = 4$, $K = 100$): a single move, since a step may be *shorter* than $K$.
- **Direction is irrelevant**, so the absolute difference is needed — the sample's last two rows both go downward.
- **An exact multiple** ($A = 30$, $B = 4$, $K = 2$: distance $26$): thirteen moves with no short final step.
- Steps are "at most $K$", which is why this rounds up rather than requiring exact multiples.

## Dry run

| $A$ | $B$ | distance $|A-B|$ | $K$ | $\lceil d/K \rceil$ | output |
|---:|---:|---:|---:|---:|---|
| 10 | 20 | 10 | 3 | 4 | `4` |
| 36 | 36 | 0 | 5 | 0 | `0` |
| 50 | 4 | 46 | 100 | 1 | `1` |
| 30 | 4 | 26 | 2 | 13 | `13` |

Row 1's fourth move covers only one unit; row 4 divides exactly.
