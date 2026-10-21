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

## Edge cases

- **There is exactly one round number per prefix.** Appending a digit to any $n \geq 1$ adds that digit to the digit sum, and precisely one choice in $0 \dots 9$ brings the total to a multiple of $10$ — so the $n$-th round number is $n$ with that digit appended, a clean bijection.
- **This makes the answer a string operation**, not a search: the $10^{18}$-th round number is computed in one pass over nineteen digits.
- **A digit sum already divisible by $10$ needs a trailing `0`**, which the outer `% 10` supplies — writing just $10 - s \bmod 10$ would append `10` instead. $N = 19$ has digit sum $10$ and the answer is $190$.
- **The smallest round number is $19$** ($N = 1$), since the number must be greater than $0$ and single digits cannot reach a digit sum of $10$.
- **The result has one more digit than $N$**, so it is produced as text rather than as an integer — at $N = 10^{18}$ the answer has twenty digits.
- **The digit sum is computed on the raw bytes** with `ch - 48`, avoiding a decode per case at $T = 10^5$.

## Dry run

| $N$ | digit sum | needed digit | answer |
|---:|---:|---:|---|
| 1 | 1 | 9 | `19` |
| 2 | 2 | 8 | `28` |
| 10 | 1 | 9 | `109` |
| 19 | 10 | **0** | `190` |

Listing the round numbers confirms it: $19, 28, 37, \dots, 91, 109, 118, \dots, 190$ — the $19$th is $190$.
