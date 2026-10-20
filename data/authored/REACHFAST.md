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
