---
topic: Number Theory
subtopic: Parity plus a threshold
time: $O(1)$ per test case
space: $O(1)$
---
We need non-negative $X, Y$ with $2X + 7Y = N$. Split on the parity of $N$.

**$N$ even.** Take $Y = 0$ and $X = N/2$. Always works, so every even $N$ is representable — including $N = 2$ itself.

**$N$ odd.** The term $2X$ is always even, so $7Y$ must be odd, which forces $Y$ to be odd. The cheapest odd choice is $Y = 1$, leaving $N - 7$ to be covered by $2$s. Since $N$ is odd, $N - 7$ is even, so it splits into $2$s exactly — provided it is not negative. Hence odd $N$ works precisely when $N \geq 7$.

Larger odd $Y$ never helps: $Y = 3$ consumes $21$, so if that leaves a valid remainder then $Y = 1$ certainly did too. Trying the smallest qualifying $Y$ is enough.

Putting it together:

$$\text{YES} \iff N \text{ is even, or } N \geq 7$$

The only `NO` answers are the odd numbers below $7$: $1, 3, 5$. Sample case 2 is $N = 5$, and $N = 1$ and $N = 3$ fail the same way.

This is a small instance of the **Chicken McNugget / Frobenius** problem. Because $\gcd(2, 7) = 1$, all sufficiently large $N$ are representable, and the largest unrepresentable value is $2 \cdot 7 - 2 - 7 = 5$ — exactly matching the analysis above. With $N$ up to $10^8$, a search over $Y$ would be needlessly slow; the closed condition is $O(1)$.

## Edge cases

- **$N = 7$**, the smallest odd value that works: one $7$ and nothing else, so `YES`. This is the boundary.
- **$N = 5$**, the largest odd failure: too small to contain a $7$, and no combination of even parts can reach an odd total, so `NO`. The sample has both sides of the boundary.
- **$N = 1, 3$**: `NO` for the same reason.
- **$N = 2$**: a single $2$, so `YES`.
- The reasoning in one line: an even $N$ splits entirely into $2$s, while an odd $N$ needs at least one odd part — and the only odd part available is $7$, leaving an even remainder. So odd $N$ works exactly when $N \geq 7$.

## Dry run

| $N$ | parity | reaches 7? | construction | output |
|---:|---|:---:|---|---|
| 2 | even | — | $2$ | `YES` |
| 5 | odd | no | impossible | `NO` |
| 7 | odd | yes | $7$ | `YES` |
| 11 | odd | yes | $7 + 2 + 2$ | `YES` |
