---
topic: Number Theory
subtopic: Add every odd divisor to its multiples
time: $O(V\log V+T)$ overall for $V=\max R$
space: $O(V+T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For each odd positive integer $d$, add $d$ to every multiple of $d$. After this divisor sieve, entry $f[n]$ is exactly the sum of odd divisors of $n$. A prefix sum over $f$ answers each interval as `prefix[r]-prefix[l-1]`.

## Edge cases

- Include divisor one.
- Powers of two have odd-divisor sum one.
- The left endpoint may be one, using prefix entry zero.

## Dry run

For the singleton range `[42,42]`, odd divisors are `1,3,7,21`, summing to 32. For `[1,10]`, the prefix sum is 45.
