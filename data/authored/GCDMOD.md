---
topic: Number Theory
subtopic: Reducing the big operand modulo the small one
time: $O(\log N)$ per test case
space: $O(1)$
---
$A^N + B^N$ is astronomically large, but a GCD only needs it **modulo the other operand**. Let $d = A - B$. Since $A \equiv B \pmod d$,

$$A^N + B^N \equiv B^N + B^N = 2B^N \pmod d$$

and therefore

$$\gcd\bigl(A^N + B^N,\ d\bigr) = \gcd\bigl(2B^N \bmod d,\ d\bigr)$$

which is computable with one modular exponentiation — $O(\log N)$ multiplications of numbers below $10^{12}$ — followed by a Euclidean GCD.

The degenerate case is $A = B$, where $d = 0$. The statement's convention $\gcd(0, a) = a$ then makes the answer $A^N + B^N = 2A^N$ itself, which must be reduced modulo $10^9+7$ — the only branch where the modulus actually does any work, since otherwise the answer is at most $d \leq 10^{12}$... and still needs reducing, as $10^{12}$ exceeds the modulus.

The reduction is what makes the problem tractable: computing $A^N + B^N$ modulo $10^9+7$ and *then* taking a GCD would be wrong, because reducing by the wrong modulus destroys the divisibility structure.

The samples: $A{=}10, B{=}1, N{=}1$ gives $d = 9$ and $2 \cdot 1 = 2$, so $\gcd(2,9) = 1$. And $A{=}9, B{=}1, N{=}5$ gives $d = 8$ with $2 \cdot 1^5 = 2$, so $\gcd(2,8) = 2$ — matching $\gcd(9^5 + 1, 8) = \gcd(59050, 8) = 2$.
