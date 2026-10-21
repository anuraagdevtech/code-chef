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

## Edge cases

- **$X = 50$ and $X = 51$** straddle the midpoint and both appear in the sample: at $50$ the distances are $49$ left and $50$ right, so `LEFT`; at $51$ they are $50$ and $49$, so `RIGHT`.
- **$X = 1$**: already at the left exit, distance $0$, so `LEFT`.
- **$X = 100$**: already at the right exit, so `RIGHT`.
- **No tie is possible.** The two distances are $X - 1$ and $100 - X$, which always sum to $99$ — an odd number, so they can never be equal. That is why the problem needs no third answer, and why the test collapses to the single comparison $X \leq 50$.

## Dry run

| $X$ | left $X-1$ | right $100-X$ | nearer | output |
|---:|---:|---:|---|---|
| 1 | 0 | 99 | left | `LEFT` |
| 50 | 49 | 50 | left | `LEFT` |
| 100 | 99 | 0 | right | `RIGHT` |
| 30 | 29 | 70 | left | `LEFT` |
| 51 | 50 | 49 | right | `RIGHT` |
| 73 | 72 | 27 | right | `RIGHT` |

Rows 2 and 5 are the two sides of the midpoint, one unit apart.
