---
topic: Number Theory
subtopic: Remove one copy of the prime with the largest exponent
time: $O(\sqrt{N})$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Write $N = \prod p_i^{e_i}$; it has $\prod (e_i + 1)$ divisors. Dividing by $K$ lowers some exponents, and every lowered exponent shrinks the divisor count, so an optimal $K$ removes as little as possible: a single prime.

Removing one copy of a prime with exponent $e$ multiplies the divisor count by $e / (e + 1)$, which is largest for the largest $e$. So the answer is the prime with the maximum exponent, and among several such primes the smallest one - the smallest $K$ is asked for.

Trial division up to $\sqrt{N}$ visits the primes in increasing order, so keeping the first prime that strictly improves the best exponent gives the smallest one automatically. A leftover factor greater than 1 is a prime with exponent 1; it is the answer only when $N$ itself is prime.

## Edge cases

- $N$ prime: the only possible $K$ is $N$.
- Ties in the exponent are broken towards the smaller prime by the strict comparison.
- A large prime factor above $\sqrt{N}$ has exponent 1 and never beats an earlier prime.
- $K = 1$ is not allowed, so something always has to be removed.

## Dry run

`N = 12 = 2^2 * 3`. Trial division finds exponent 2 for the prime 2 (best so far) and exponent 1 for 3 (no improvement).

Answer $K = 2$: $M = 6$ has 4 divisors, whereas $K = 3$ would leave $M = 4$ with only 3.
