---
topic: Basic Math
subtopic: Counting by parity, reduced to lowest terms
time: $O(\log \min(N,M))$ per test case
space: $O(1)$
---
Both choices are uniform and independent, so the probability is a ratio of counts over the $N \cdot M$ equally likely pairs. A sum is odd exactly when the two parts have **different parity**, so with

$$N_{\text{odd}} = \left\lceil \frac{N}{2} \right\rceil = \left\lfloor \frac{N+1}{2} \right\rfloor, \qquad N_{\text{even}} = \left\lfloor \frac{N}{2} \right\rfloor$$

and likewise for $M$, the favourable count is

$$N_{\text{odd}} M_{\text{even}} + N_{\text{even}} M_{\text{odd}}$$

Since $N, M \leq 10^9$ the numerator reaches about $5 \times 10^{17}$ — inside 64-bit range but only just, so C++ needs `long long` here.

The output must be an **irreducible fraction**, so divide both parts by their GCD. The degenerate case is a numerator of $0$: $\gcd(0, d) = d$, so the reduction yields $0/1$ automatically rather than $0/d$ — exactly the expected `0/1` when $N = M = 1$, where the only sum is $2$.

A useful sanity check: whenever either $N$ or $M$ is even the answer is exactly $1/2$, because that side contributes equal numbers of odd and even values and so balances the parities whatever the other side does. Both sample answers of $1/2$ are instances — $N=1, M=2$ and $N=2, M=3$. The probability can differ from $1/2$ only when $N$ and $M$ are both odd, which is when each side has one more odd value than even.

## Edge cases

- **A zero numerator must print `0/1`, not `0/<denominator>`.** Python's `gcd(0, d)` returns `d`, so dividing both parts by the gcd reduces $0/1$ correctly without a special case — and the first row is exactly this, since $1 + 1$ is always even.
- **Counting odds as $\lceil n/2 \rceil$ and evens as $\lfloor n/2 \rfloor$** is what makes $n = 1$ work: one odd, zero evens.
- **An odd sum needs exactly one odd and one even pick**, so the two cross terms are the entire numerator and no other combination contributes.
- **The fraction must be in lowest terms** — the third row reduces $3/6$ to $1/2$.
- **$n$ and $m$ up to $10^9$** put the denominator at $10^{18}$, native in Python but past 32-bit.
- **The two ranges are independent**, so the counts multiply rather than needing any joint enumeration.

## Dry run

Third sample: $n = 2$, $m = 3$.

| | odds | evens |
|---|---:|---:|
| $1 \dots 2$ | 1 | 1 |
| $1 \dots 3$ | 2 | 1 |

Favourable pairs: $1 \times 1$ (odd, even) $+\ 1 \times 2$ (even, odd) $= 3$, out of $2 \times 3 = 6$. Reducing by $\gcd(3,6) = 3$ gives `1/2`.
