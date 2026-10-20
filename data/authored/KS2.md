---
topic: Number Theory
subtopic: A bijection between prefixes and solutions
time: $O(\log N)$ per test case
space: $O(1)$
---
Call an integer *round* when its digit sum is a multiple of $10$. The key structural fact:

> For every positive integer $p$, there is **exactly one** digit $d$ making the number $\overline{p\,d}$ round.

Because appending $d$ adds $d$ to the digit sum, and exactly one value of $d \in \{0, \ldots, 9\}$ brings that sum to $0$ modulo $10$ — namely $d = (-S(p)) \bmod 10$.

That gives a bijection between prefixes $p = 1, 2, 3, \ldots$ and round numbers, **order-preserving** because appending a digit is monotonic in the prefix. So the $N$-th round number is simply $N$ with its completing digit attached:

$$\text{answer} = 10N + \bigl((10 - S(N) \bmod 10) \bmod 10\bigr)$$

Checking the sample: $N = 2$ has digit sum $2$, so $d = 8$ and the answer is $28$. For $N = 1$ the digit sum is $1$, giving $19$ — and indeed no smaller positive integer has a digit sum of $10$.

The bijection is what makes this $O(\log N)$ rather than a search. With $N$ up to $10^{18}$, enumerating round numbers is impossible, and even a digit DP with binary search would be far more work than this.

The outer $\bmod 10$ matters for the case $S(N) \equiv 0$, where the completing digit is $0$ rather than $10$ — for example $N = 19$ gives $190$.

The result reaches about $10^{19}$, which **exceeds signed 64-bit range** and needs unsigned or big integers elsewhere; the problem's guarantee that it fits in $2^{64}$ is the hint.
