---
topic: Number Theory
subtopic: Reduce each number to its primitive root base
time: $O(\sqrt{A} + \sqrt{B})$ per uncached pair
space: $O(\text{distinct inputs})$ for the cache
complexity_note: Auxiliary space excludes the buffered input and output.
---
$A^X = B^Y$ means the prime-exponent vectors of $A$ and $B$ are proportional: same primes, and exponents in a fixed positive ratio.

Every integer $n \ge 2$ is a perfect power of a unique *primitive* base: divide all exponents in its factorisation by their gcd $g$, giving $r$ with $n = r^g$ and $r$ not a perfect power. Two numbers have proportional exponent vectors exactly when they have the same primitive base - if $A = r^g$ and $B = r^h$ then $A^h = B^g$.

So factorise both numbers by trial division, build the primitive base and compare. Results are cached because the same values recur across test cases.

## Edge cases

- A prime factor left over after trial division has exponent 1, forcing the gcd to 1.
- $A = B$ is always equivalent ($X = Y = 1$).
- Different sets of primes can never be equivalent, and they produce different bases.
- $A, B \ge 2$, so the empty factorisation does not occur.

## Dry run

- `8 4`: $8 = 2^3$ has base 2, $4 = 2^2$ has base 2 - YES ($8^2 = 4^3 = 64$).
- `12 24`: $12 = 2^2 \cdot 3$ has exponent gcd 1, base 12; $24 = 2^3 \cdot 3$ has base 24 - NO.
- `2 3`: bases 2 and 3 - NO.
