---
topic: Game Theory
subtopic: Prime-count threshold via the smallest forbidden prime product
time: $O(V\log\log V+T)$ overall for $V=\max X$
space: $O(V+T)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $P$ be the product of the first $Y+1$ primes. Every positive number below $P$ has at most $Y$ distinct prime factors and is a legal subtraction. Every multiple of $P$ is illegal to subtract. Thus multiples of $P$ are losing positions: a legal move leaves a nonmultiple, and from a nonmultiple subtracting its residue modulo $P$ returns to a multiple.

The starting $X!$ is divisible by $P$ exactly when at least $Y+1$ primes are at most $X$. Otherwise $X!$ itself has at most $Y$ prime factors, so Chef wins immediately. Sieve prime prefix counts; print `Divyam` if the prime count through $X$ exceeds $Y$,  else `Chef`.

## Edge cases

- One is a legal subtraction with zero prime factors.
- Equality between the prime count and $Y$ is a Chef win.
- Never construct the factorial or the forbidden prime product.

## Dry run

For `X=3,Y=1`, the factorial has distinct primes two and three, exceeding the threshold. It is a losing position, so Divyam wins.
