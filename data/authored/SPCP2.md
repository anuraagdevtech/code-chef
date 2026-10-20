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
