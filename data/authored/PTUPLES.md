---
topic: Number Theory
subtopic: Every prime-sum triple starts with two
time: $O(V\log\log V+T)$ overall for $V=\max N$
space: $O(V+T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Two odd primes have an even sum larger than two, which is not prime. Thus the smaller prime must be two, and every good triple is $(2,p,p+2)$ with both $p$ and $p+2$ prime and $p\ge3$.

Sieve all values up to the largest query and build a prefix count of upper twin-prime endpoints. A query is answered by its prefix entry.

## Edge cases

- One is not prime.
- The primes in a triple must be strictly increasing.
- An endpoint exactly equal to $N$ is allowed.

## Dry run

For `N=6`, the only pair of odd primes differing by two is `(3,5)`, yielding triple `(2,3,5)` and answer one.
