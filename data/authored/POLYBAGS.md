---
topic: Basic Math
subtopic: Ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
A polybag holds at most $10$ items and every item must be carried, so the count rounds up:

$$\left\lceil \frac{N}{10} \right\rceil$$

written in integers as `(n + 9) // 10`.

This is the same capacity-and-ceiling shape as the cars, pizzas and subscriptions problems, and the signature is identical: a fixed container size, nothing may be left behind, so a partial container still costs a whole unit.

The samples cover both sides of the rounding. $N = 20$ divides exactly and needs $2$ bags, with the formula giving $(20+9)//10 = 2$ rather than overshooting to $3$ — the usual thing to check when using the $+k-1$ trick. $N = 24$ is ragged and needs $3$, the last bag holding only $4$ items. $N = 99$ needs $10$, one short of a clean $100$.

Keeping the arithmetic in integers avoids `math.ceil(n / 10)`, which converts to a float first and would start misbehaving for very large $N$ — not a risk at $N \leq 1000$, but the integer form costs nothing and always holds.
