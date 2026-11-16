---
topic: Number Theory
subtopic: Multiply N by two neighbouring numbers that each add exactly one new prime
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Look for $A = (m + 1) N$ and $B = m N$; their difference is $N$ automatically.

- $N$ even: take $A = 2N$, $B = N$. Multiplying by 2 adds no new prime, so both have the same set of prime factors.
- $N$ odd: let $p$ be the smallest odd prime that does not divide $N$, and take $A = pN$, $B = (p - 1) N$. $A$ has the primes of $N$ plus $p$. For $B$, the number $p - 1$ is even, and all of its odd prime factors are odd primes smaller than $p$, which divide $N$ by the choice of $p$; so $B$ has the primes of $N$ plus exactly the prime 2. Both counts are one more than for $N$.

The product of all odd primes up to 47 exceeds $10^{16}$, so $N$ cannot be divisible by all of them and $p \le 47$ always, and $A = pN \le 47 \cdot 10^{16} < 10^{18}$.

## Edge cases

- $N = 1$: $p = 3$, giving `3 2`, one prime each.
- Even $N$ never needs a prime search.
- The bound $A, B \le 10^{18}$ is why the smallest missing prime is used.
- Any valid pair is accepted.

## Dry run

`N = 135 = 3^3 * 5`: odd, and the smallest odd prime not dividing it is 7.

$A = 7 \cdot 135 = 945 = 3^3 \cdot 5 \cdot 7$ and $B = 6 \cdot 135 = 810 = 2 \cdot 3^4 \cdot 5$: three distinct primes each, and $945 - 810 = 135$.

`N = 8`: even, so `16 8`, both with the single prime 2.
