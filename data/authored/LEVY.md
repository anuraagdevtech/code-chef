---
topic: Number Theory
subtopic: Precompute counts of prime plus twice-prime sums
time: $O(V\log\log V+\pi(V)^2+T)$ overall for $V=\max N$
space: $O(V+T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Sieve primes up to the largest query. For every prime $q$, enumerate primes $p$ while $p+2q$ stays within that bound, incrementing the answer at that sum.

The enumeration counts ordered pairs exactly once: $p$ and $q$ have different roles in the equation. Queries then become table lookups. The bound $V\le10000$ makes this pair precomputation small.

## Edge cases

- The input need not be odd or greater than five.
- Two is a valid prime in either role.
- The two primes may be equal.

## Dry run

For `N=11`, pairs `(7,2)` and `(5,3)` satisfy the equation. Both are counted, so the answer is two.
