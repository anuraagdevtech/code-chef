---
topic: Basic Math
subtopic: Ceiling division
time: $O(1)$ per test case
space: $O(1)$
---
One subscription covers $6$ people, so $N$ friends need $\lceil N/6 \rceil$ subscriptions — the leftover group of fewer than six people still needs a whole subscription of its own. The answer is that count multiplied by the unit price $X$.

The only real content here is computing the ceiling without touching floats. `math.ceil(n / 6)` works for these bounds but is the wrong reflex, because `n / 6` is a float and loses exactness once $N$ grows past $2^{53}$. The integer identity

$$\left\lceil \frac{n}{k} \right\rceil = \left\lfloor \frac{n + k - 1}{k} \right\rfloor$$

gives the same value using only `//`. In Python that is `(n + 5) // 6`, and it is exact for arbitrarily large integers.

Checking it against the samples: $N=1$ gives $(1+5)//6 = 1$ subscription, so $1 \times 100 = 100$. $N=12$ gives $(12+5)//6 = 2$, so $2 \times 250 = 500$. $N=16$ gives $(16+5)//6 = 3$, so $3 \times 135 = 405$.
