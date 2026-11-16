---
topic: Number Theory
subtopic: Factorise N once and answer from prime exponents
time: $O(\sqrt{N} + Q \cdot \omega(N) \log K)$
space: $O(\omega(N))$ besides the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
Factorise $N = \prod p_i^{e_i}$ once by trial division. $N$ has at most about a dozen distinct primes, so each query is cheap.

- Type 1, common divisors of $N$ and $K$: these are the divisors of $\gcd(N, K)$. The gcd only contains primes of $N$, so read its exponents $v_i$ by dividing by each $p_i$; the count is $\prod (v_i + 1)$.
- Type 2, divisors of $N$ that are multiples of $K$: there are none unless $K$ divides $N$. If it does, with exponents $v_i$ in $K$, the divisor's exponent of $p_i$ ranges over $v_i \dots e_i$: the count is $\prod (e_i - v_i + 1)$.
- Type 3, divisors of $N$ not divisible by $K$: the total number of divisors minus the type-2 answer.

## Edge cases

- $K$ not dividing $N$: type 2 is 0 and type 3 is the full divisor count.
- $K$ may have primes that $N$ lacks; the gcd in type 1 removes them.
- $N$ up to $10^{12}$ still factorises quickly by trial division.
- $K = 1$: type 2 counts all divisors and type 3 is 0.

## Dry run

`N = 12 = 2^2 * 3`, 6 divisors.

- `1 6`: gcd 6 = $2 \cdot 3$, count $2 \cdot 2 = 4$.
- `1 14`: gcd 2, count 2.
- `2 4`: $4 = 2^2$ divides 12: $(2 - 2 + 1)(1 - 0 + 1) = 2$.
- `2 3`: $(2 + 1)(1 - 1 + 1) = 3$.
- `3 12`: $6 - 1 = 5$.
- `3 14`: 14 does not divide 12, so $6 - 0 = 6$.
