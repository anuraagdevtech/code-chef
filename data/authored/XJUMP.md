---
topic: Greedy
subtopic: Prefer the large step, then settle the remainder
time: $O(1)$ per test case
space: $O(1)$
---
Chef can move $Y$ stairs or $1$ stair at a time and must land **exactly** on $X$. Since a $Y$-move covers $Y$ stairs for the same price as a $1$-move covers one, the greedy choice is to take as many $Y$-moves as possible and walk the rest:

$$\left\lfloor \frac{X}{Y} \right\rfloor + (X \bmod Y)$$

The greedy is provably optimal because the two move types are independent and unbounded: taking one fewer big jump forces $Y$ extra single steps, a strictly worse trade whenever $Y > 1$. There is no reason to stop short.

The remainder is where the "exactly" matters. Chef cannot overshoot and come back, so the last $X \bmod Y$ stairs must be covered one at a time. That is why the answer is a sum rather than a ceiling division — this is *not* $\lceil X/Y \rceil$.

The degenerate case $Y = 1$ falls out correctly without a guard: the formula gives $X + 0 = X$ single steps, which is right. And when $Y > X$, as in sample case 3, there are no big jumps at all and the answer is $X$ — $0 + 3 = 3$.

Sample case 2 shows both parts working: $8$ stairs with $Y = 3$ gives $2$ jumps covering $6$, then $2$ single steps, for $4$ moves.
