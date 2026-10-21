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

## Edge cases

- **The $K$-th kilometre burns the *total* of the first $K-1$**, which doubles the running total each step: $X, 2X, 4X, \dots$, so the answer is $X \cdot 2^{N-1}$ with no recurrence to iterate.
- **$N = 1$** → just $X$, and $2^0 = 1$ gives it; writing $2^N$ would double every answer.
- **The exponent must be computed modularly.** At $N = 10^6$ the true value has over $300{,}000$ digits, so `pow(2, n - 1, MOD)` is essential rather than computing the power and reducing afterwards.
- **$X \leq 100$ is already below the modulus**, so the `x % MOD` is defensive rather than necessary.
- **The modulus is $10^9 + 7$**, and the product of two reduced values stays under $10^{18}$ — within 64-bit, and exact in Python.
- **$T$ up to $10^5$** with one modular exponentiation each, at $O(\log N)$.

## Dry run

| $N$ | $X$ | per-kilometre burn | total |
|---:|---:|---|---:|
| 1 | 2 | $2$ | `2` |
| 2 | 1 | $1, 1$ | `2` |
| 4 | 1 | $1, 1, 2, 4$ | 8 |

The totals after each kilometre are $X, 2X, 4X, 8X$ — the running sum doubles because the new kilometre equals everything before it.
