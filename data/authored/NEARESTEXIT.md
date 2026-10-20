---
topic: Basic Math
subtopic: Comparing distances to two endpoints
time: $O(1)$ per test case
space: $O(1)$
---
Seats run $1$ to $100$ with equal spacing, so from seat $X$ the distance to the left exit (beside seat $1$) is $X - 1$ and the distance to the right exit (beside seat $100$) is $100 - X$.

The passenger takes the left exit when it is no further away:

$$X - 1 \leq 100 - X \quad\Longleftrightarrow\quad 2X \leq 101 \quad\Longleftrightarrow\quad X \leq 50.5$$

Since $X$ is an integer this is simply $X \leq 50$. The midpoint falls *between* seats $50$ and $51$, so there is no genuine tie to resolve — every seat is strictly closer to one exit than the other, and the problem's silence about ties is therefore harmless.

Two details are easy to get wrong. The distances are $X - 1$ and $100 - X$, not $X$ and $100 - X$; the exits sit *beside* the end seats, so the passenger in seat $1$ has distance zero. And the cutoff is $50$, not $49$ or $51$ — the samples pin both sides down, with $X = 50$ answering `LEFT` and $X = 51$ answering `RIGHT`.

Writing the test as `x <= 50` is clearest, though `2 * x <= 101` is equivalent and shows the derivation.
