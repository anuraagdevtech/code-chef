---
topic: Basic Math
subtopic: Ceiling division with a clamp
time: $O(1)$ per test case
space: $O(1)$
---
Each aircraft seats $100$ passengers, so carrying $N$ people needs

$$\left\lceil \frac{N}{100} \right\rceil$$

planes in total — the leftover passengers still need a whole aircraft, so this rounds up. The airline already owns $X$, so it must buy the shortfall:

$$\max\left(0,\; \left\lceil \frac{N}{100} \right\rceil - X\right)$$

Both operations are load-bearing. The ceiling handles sample case 2, where $523$ passengers need $6$ planes rather than $5$ — the final plane carries just $23$ people. The clamp handles sample case 3, where $245$ passengers need $3$ planes but the airline already has $8$; the answer is $0$, not a negative number. Surplus aircraft cannot be un-bought.

This is the same clamp-after-ceiling shape as the chess-ratings and candy-packet problems, and the ordering matters for the same reason: computing `n // 100 - x` and then rounding would mix the two roundings together. Resolve the requirement first, compare against stock second.

In integers the ceiling is `(n + 99) // 100`.

## Edge cases

- **Already enough planes** ($X = 8$ for $245$ passengers, needing $3$): the shortfall is negative, so the clamp returns $0$. The sample's third row.
- **Passengers an exact multiple of $100$** ($N = 600$): exactly $6$ planes, and the $+99$ must not demand a seventh.
- **A part-full plane still flies** ($N = 523$): $6$ planes, the last carrying $23$ people.
- **A single passenger** ($N = 1$): one plane, since nobody can be left behind.
- Two separate roundings happen here — up for the planes needed, then clamped at zero for the shortfall — and getting either direction wrong is silent.

## Dry run

| $X$ (owned) | $N$ (passengers) | planes needed $\lceil N/100 \rceil$ | shortfall | output |
|---:|---:|---:|---:|---|
| 4 | 600 | 6 | 2 | `2` |
| 3 | 523 | 6 | 3 | `3` |
| 8 | 245 | 3 | $-5 \to 0$ | `0` |

Row 1 is the exact multiple; row 3 is the clamped case.
