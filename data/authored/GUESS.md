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
