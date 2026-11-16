[&larr; 599. Array Sum](599-SUMARRAY.md) &middot; [Index](README.md) &middot; [601. Chef and Rectangle Array &rarr;](601-CHSQARR.md)

# 600. Equivalent Numbers

> [`EQUIVALENT`](https://www.codechef.com/problems/EQUIVALENT) &middot; difficulty **2087** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Reduce each number to its primitive root base |
| **CodeChef tags** | `Number Theory`, `Integer Factorisation`, `Divisors`, `Mathematics`, `Sieve of Eratosthenes`, `Prime Divisors` |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{A} + \sqrt{B})$ per uncached pair |
| **Space** | $O(\text{distinct inputs})$ for the cache |

## Question

Chef calls a pair of integers $(A, B)$ *equivalent* if there exist some **positive** integers $X$ and $Y$ such that $A^X = B^Y$.

Given $A$ and $B$, determine whether the pair is *equivalent* or not.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $A$ and $B$, as mentioned in statement.

**Output**

For each test case, output `YES` if $(A, B)$ is an *equivalent* pair, `NO` otherwise.

The output is case-insensitive. Thus, the strings `Yes`, `YES`, `yes`, and `yeS` are all considered identical.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq A, B \leq 10^6$

## Sample

**Sample input**

```
3
2 3
8 4
12 24
```

**Sample output**

```
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** There are no positive integers $X$ and $Y$ which satisfy $A^X = B^Y$.

**Test case $2$:** Let $X = 2$ and $Y = 3$. Thus, $A^X = 8^2 = 64$ and $B^Y = 4^3 = 64$. Thus, the pair $(8, 4)$ is *equivalent*.

**Test case $3$:** There are no positive integers $X$ and $Y$ which satisfy $A^X = B^Y$.

</details>

## Approach

$A^X = B^Y$ means the prime-exponent vectors of $A$ and $B$ are proportional: same primes, and exponents in a fixed positive ratio.

Every integer $n \ge 2$ is a perfect power of a unique *primitive* base: divide all exponents in its factorisation by their gcd $g$, giving $r$ with $n = r^g$ and $r$ not a perfect power. Two numbers have proportional exponent vectors exactly when they have the same primitive base - if $A = r^g$ and $B = r^h$ then $A^h = B^g$.

So factorise both numbers by trial division, build the primitive base and compare. Results are cached because the same values recur across test cases.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []

    def canonical(n):
        rest = n
        prime = 2
        factors = []
        common = 0
        while prime * prime <= rest:
            exponent = 0
            while rest % prime == 0:
                rest //= prime
                exponent += 1
            if exponent:
                factors.append((prime, exponent))
                common = gcd(common, exponent)
            prime = 3 if prime == 2 else prime + 2
        if rest > 1:
            factors.append((rest, 1))
            common = 1
        base = 1
        for prime, exponent in factors:
            base *= prime ** (exponent // common)
        return base
    cache = {}
    for _ in range(next(tokens)):
        a = next(tokens)
        b = next(tokens)
        if a not in cache:
            cache[a] = canonical(a)
        if b not in cache:
            cache[b] = canonical(b)
        out.append('YES' if cache[a] == cache[b] else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- A prime factor left over after trial division has exponent 1, forcing the gcd to 1.
- $A = B$ is always equivalent ($X = Y = 1$).
- Different sets of primes can never be equivalent, and they produce different bases.
- $A, B \ge 2$, so the empty factorisation does not occur.

## Dry run

- `8 4`: $8 = 2^3$ has base 2, $4 = 2^2$ has base 2 - YES ($8^2 = 4^3 = 64$).
- `12 24`: $12 = 2^2 \cdot 3$ has exponent gcd 1, base 12; $24 = 2^3 \cdot 3$ has base 24 - NO.
- `2 3`: bases 2 and 3 - NO.

---

Same problem grouped by topic: [../docs/number-theory/EQUIVALENT.md](../docs/number-theory/EQUIVALENT.md)
