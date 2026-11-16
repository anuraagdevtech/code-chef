---
topic: Number Theory
subtopic: Strip common factors with repeated gcd
time: $O(\log^2 B)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Numbers up to $10^{18}$ cannot be factorised in time, but factorisation is not needed. The question is whether every prime of $B$ also divides $A$.

Let $g = \gcd(A, B)$. If $g = 1$ and $B > 1$, then $B$ has a prime that $A$ lacks: answer NO. Otherwise divide $B$ by $g$ and repeat - $g$ contains only primes of $A$, so dividing by it never removes a prime that $A$ lacks, and each division at least halves $B$. If $B$ reaches 1, all of its primes were shared: answer YES.

## Edge cases

- $B = 1$ has no prime factors, so the answer is YES for any $A$.
- High powers in $B$ (for example $A = 2$, $B = 2^{60}$) need several rounds, which is why it is a loop and not a single gcd.
- $A = 1$ gives YES only when $B = 1$.
- Python integers handle $10^{18}$ exactly.

## Dry run

- `A = 21, B = 63`: gcd 21, $B \to 3$; gcd(21, 3) = 3, $B \to 1$. YES.
- `A = 25, B = 20`: gcd 5, $B \to 4$; gcd(25, 4) = 1 with $B > 1$. NO - the prime 2 is missing from 25.
