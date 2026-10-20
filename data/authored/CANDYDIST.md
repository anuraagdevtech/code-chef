---
topic: Number Theory
subtopic: Divisibility by a composite modulus
time: $O(1)$ per test case
space: $O(1)$
---
Two conditions must hold at once. Every one of the $M$ friends gets the same number of candies, so $M$ must divide $N$; and that shared amount $N/M$ must itself be even.

Written directly:

$$M \mid N \quad\text{and}\quad \frac{N}{M} \equiv 0 \pmod 2$$

Both are needed, and each one alone is insufficient. Sample case 1 ($N=9$, $M=3$) divides evenly into $3$ candies each, but $3$ is odd. Sample case 4 ($N=8$, $M=3$) fails the divisibility outright.

There is a neater way to see it. "Divisible by $M$, and the quotient divisible by $2$" is exactly "divisible by $2M$":

$$N \equiv 0 \pmod{2M}$$

a single modulo instead of a division followed by a parity test. This also sidesteps any worry about evaluating `n // m` when `n % m != 0` — with the combined form there is no intermediate quotient at all.

Both formulations are given in the code below, with the compact one used. The guarantee that $N, M \geq 1$ means $2M$ is never zero, so the modulo is always well defined.
