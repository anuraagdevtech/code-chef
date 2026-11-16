---
topic: Number Theory
subtopic: Add prime exponents across all factors
time: $O(N\pi(\sqrt V))$ trial divisions per test case after a sieve to $\sqrt V$
space: $O(\pi(\sqrt V)+N\log V)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
If the product's prime factorisation is $\prod p^{e_p}$, each divisor independently chooses an exponent from zero through $e_p$. Its number of divisors is therefore $\prod(e_p+1)$.

Factor each input value by precomputed primes up to 1000, accumulating exponents by prime. Stop trial division when the next prime square exceeds the remaining value; any remainder greater than one is prime. Never form the enormous product itself.

## Edge cases

- Repeated input values add exponents, rather than multiply their separate divisor counts.
- A remaining large prime contributes exponent one.
- Return the exact count; there is no modulus.

## Dry run

For factors `[2,4,6]`, their product has factorisation `2^4 * 3`. Its divisor count is `(4+1)(1+1)=10`.
