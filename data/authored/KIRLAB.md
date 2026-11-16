---
topic: Number Theory
subtopic: Longest chain DP keyed by prime factor, with a smallest-prime-factor sieve
time: $O(A \log \log A + N \log A)$ over the whole input, $A$ the largest value
space: $O(A)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
We want the longest subsequence in which neighbouring values share a prime factor. Let `best[p]` be the length of the longest valid subsequence seen so far whose last element is divisible by the prime $p$.

For a new value $x$ with distinct prime factors $p_1, \dots, p_k$, the previous chosen element must share one of them, so the longest chain ending at $x$ has length $1 + \max_i \text{best}[p_i]$. Afterwards $x$ itself is a chain end divisible by each $p_i$, so set every `best[p_i]` to that length - it is at least as large as the old value.

Factorisation uses a smallest-prime-factor sieve built once up to the largest value in the input.

## Edge cases

- A room with 1 monster has no prime factors; it can only form a chain of length 1 by itself.
- Read all factors' values before updating any of them, otherwise $x$ would chain with itself.
- The sieve only marks composites, so a zero entry means the number is prime.
- Equal values chain with each other because they share all their primes.

## Dry run

`A = [13, 2, 8, 6, 3, 1, 9]`.

| value | primes | length | updates |
|---:|---|---:|---|
| 13 | 13 | 1 | best[13] = 1 |
| 2 | 2 | 1 | best[2] = 1 |
| 8 | 2 | 2 | best[2] = 2 |
| 6 | 2, 3 | 3 | best[2] = best[3] = 3 |
| 3 | 3 | 4 | best[3] = 4 |
| 1 | - | 1 | - |
| 9 | 3 | 5 | best[3] = 5 |

Answer 5 (rooms 2, 8, 6, 3, 9).
