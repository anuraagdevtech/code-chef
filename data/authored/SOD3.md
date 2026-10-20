---
topic: Number Theory
subtopic: Digit sum congruent to the value mod 3
time: $O(1)$ per test case
space: $O(1)$
---
The problem looks like it needs digit-DP over an $18$-digit range, but a classical congruence collapses it.

Since $10 \equiv 1 \pmod 3$, every power of ten is also $\equiv 1$, so

$$n = \sum_k d_k 10^k \equiv \sum_k d_k \pmod 3$$

That is the familiar divisibility rule: **a number and its digit sum leave the same remainder mod 3**. So "digit sum divisible by $3$" is simply "$n$ divisible by $3$", and the count over $[L, R]$ is a difference of two floors:

$$\left\lfloor \frac{R}{3} \right\rfloor - \left\lfloor \frac{L-1}{3} \right\rfloor$$

Subtracting the prefix below $L$ is what makes the range inclusive at both ends.

With $R$ up to $10^{18}$ and $T$ up to $10^4$, this is the only viable approach — iterating the range is out of the question, and even a digit DP would be needless work.

Checking the first sample: in $[139, 141]$ only $141 = 3 \times 47$ qualifies, and $\lfloor 141/3 \rfloor - \lfloor 138/3 \rfloor = 47 - 46 = 1$.

The same rule holds for $9$ (since $10 \equiv 1 \pmod 9$) but **not** for other moduli — the trick is specific to divisors of $10 - 1$. For a modulus like $7$ the digit sum tells you nothing, and digit DP would genuinely be required.

The values exceed 32 bits, so this needs 64-bit arithmetic outside Python.
