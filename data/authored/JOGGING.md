---
topic: Number Theory
subtopic: A doubling recurrence, taken modulo
time: $O(\log N)$ per test case
space: $O(1)$
---
Let $S_K$ be the total burned after $K$ kilometres. The $K$-th kilometre burns whatever was burned over the first $K-1$, so

$$S_K = S_{K-1} + S_{K-1} = 2\,S_{K-1}$$

Each kilometre **doubles the running total**, and with $S_1 = X$ this gives the closed form

$$S_N = X \cdot 2^{\,N-1} \pmod{10^9+7}$$

Recognising the recurrence as pure doubling is the whole step. Written out, the per-kilometre burns are $X, X, 2X, 4X, 8X, \ldots$ — note the second kilometre burns the same as the first, which is why the exponent is $N-1$ rather than $N$.

Computing $2^{N-1}$ by repeated multiplication would be $O(N)$ per query and far too slow at $N = 10^6$ with $T = 10^5$. Python's three-argument `pow(2, n - 1, MOD)` does modular exponentiation by squaring in $O(\log N)$.

The samples confirm the off-by-one: $N = 1$ gives $X \cdot 2^0 = X = 2$, and $N = 2$ gives $1 \cdot 2^1 = 2$ — the same total, because the second kilometre merely matches the first.

The modulus is prime, but no inverse is needed here — only a power. An alternative for many queries would be to precompute all powers of two up to $10^6$ once, making each query $O(1)$; at these bounds either is comfortable.
