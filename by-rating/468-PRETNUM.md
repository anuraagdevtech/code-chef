[&larr; 467. Chef and Wedding Arrangements](467-CHEFWED.md) &middot; [Index](README.md) &middot; [469. XOR with Subset &rarr;](469-XORSUB.md)

# 468. Yet Another Cute Girl

> [`PRETNUM`](https://www.codechef.com/problems/PRETNUM) &middot; difficulty **1850** &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Segmented sieve plus prime-power exponents |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(\sqrt{R} \log\log \sqrt{R} + (R-L))$ per test case |
| **Space** | $O(\sqrt{R} + (R-L))$ |

## Question

Chef doesn't love math anymore. He loves Sasha. Sashen'ka is cute.

Chef goes on a date with her. Flowers are boring, while numbers are not. He knows that most of all this girl loves numbers, that's why he is going to bring ribbon with numbers **L, L+1, L+2, ..., R** written on it.

Sasha thinks that numbers with prime number of divisors are special. That's why she is going to kiss boy for each such number he will bring.

Now Chef wonder how many times he will be kissed by Sashen'ka ?

 

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.
The first line of each test case contains two number **L, R**.
 

**Output**

For each test case, output a single line containing answer for corresponding test case.
 

**Constraints**

- **1** ≤ **T** ≤ **5**

- **1** ≤ **L** ≤ **R** ≤ **10^12**

- **0** ≤ **R-L** ≤ **10^6**

## Constraints

- 1 ≤ T ≤ 5
- 1 ≤ L ≤ R ≤ 10^12
- 0 ≤ R-L ≤ 10^6

## Sample

**Sample input**

```
1
1 10
```

**Sample output**

```
6
```

<details><summary>Explanation</summary>

**Example case 1.** Numbers 2,3,4,5,7,9 are special.

</details>

## Approach

Start by characterising the special numbers. If $n = p_1^{e_1} \cdots p_r^{e_r}$ then

$$d(n) = \prod_{i=1}^{r} (e_i + 1)$$

For that product to be **prime** it must have exactly one factor above $1$, so $r = 1$: the special numbers are precisely the prime powers $p^e$ with $e + 1$ prime. ($n = 1$ has $d = 1$, which is not prime.)

That splits the count into cases by exponent, and the cases are wildly uneven:

- **$e = 1$** — the primes themselves, $d = 2$. These are dense in $[L, R]$ and need a **segmented sieve**: sieve base primes up to $\sqrt{R} = 10^6$, then mark their multiples inside the window of size at most $10^6$. Starting each prime's marking at $\max(p^2, \text{first multiple} \geq L)$ keeps a base prime that lies in the window from crossing itself off.
- **$e = 2$** — squares of primes, $d = 3$. Count primes in $[\lceil\sqrt{L}\rceil, \lfloor\sqrt{R}\rfloor]$ by binary-searching the base prime list; no second sieve needed.
- **$e \geq 4$** — handfuls. Since $2^{40} > 10^{12}$, only $e \in \{4, 6, 10, 12, 16, 18, 22, 28, 30, 36\}$ can occur (each $e+1$ prime), and for $e = 4$ already $p \leq 1000$. Enumerate directly and test the window.

Note the exponents are not $1, 2, 3, \ldots$: $e = 3$ is excluded because $d = 4$ is composite, so cubes of primes are *not* special — an easy case to include by mistake.

Use `isqrt` for the $e = 2$ bounds; floating-point square roots are off by one near perfect squares at $10^{12}$ and would miscount the endpoints.

For $[1, 10]$ the primes $2, 3, 5, 7$ give four, and the prime squares $4$ and $9$ give two more, totalling $6$. Note $8 = 2^3$ has four divisors and is correctly skipped.

## Solution

```python
import sys
from bisect import bisect_left, bisect_right
from math import isqrt

LIMIT = 10 ** 6 + 1          # sqrt of the largest R


def main() -> None:
    sieve = bytearray([1]) * LIMIT
    sieve[0:2] = b"\0\0"
    for p in range(2, isqrt(LIMIT) + 1):
        if sieve[p]:
            sieve[p * p::p] = bytearray(len(sieve[p * p::p]))
    primes = [i for i in range(2, LIMIT) if sieve[i]]
    # d(p^e) = e + 1 must be prime; 2^40 already exceeds 10^12.
    exps = [e for e in range(4, 41) if sieve[e + 1]]

    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        lo, hi = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # e = 1: the primes in [lo, hi], by segmented sieve.
        window = bytearray([1]) * (hi - lo + 1)
        if lo == 1:
            window[0] = 0
        for p in primes:
            if p * p > hi:
                break
            start = max(p * p, (lo + p - 1) // p * p)
            if start <= hi:
                window[start - lo::p] = bytearray(len(window[start - lo::p]))
        total = sum(window)
        # e = 2: prime squares, counted in the base prime list.
        left, right = isqrt(lo - 1) + 1, isqrt(hi)
        if right >= left:
            total += bisect_right(primes, right) - bisect_left(primes, left)
        # e >= 4: only a handful of prime powers are small enough.
        for e in exps:
            for p in primes:
                v = p ** e
                if v > hi:
                    break
                if v >= lo:
                    total += 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A prime divisor count forces a prime power.** If $n$ had two distinct primes its divisor count would factor as a product of two factors above $1$, hence be composite — so $n = p^e$ with $e+1$ prime.
- **That splits into three regimes**: $e = 1$ (the primes themselves), $e = 2$ (prime squares, since $3$ is prime), and $e \geq 4$ with $e+1$ prime — $e = 3$ is excluded because $4$ is composite.
- **The primes in the range need a segmented sieve**, since $R$ reaches $10^{12}$ while the window is at most $10^6$ wide — sieving by the base primes up to $10^6$ is what makes it feasible.
- **$1$ must be excluded**, as $d(1) = 1$ is not prime; the window explicitly clears it when $L = 1$.
- **Prime squares are counted through the base prime list**, by taking integer square roots of the range bounds — exact `isqrt`, since a float root can land one off at $10^{12}$.
- **The high exponents are few.** Only $e \in \{4, 6, 10, 12, 16, 18, 22, 28, 30, 36, 40\}$ have $e+1$ prime and $2^e \leq 10^{12}$, so that part is a short double loop.
- **$R - L$ may be $0$**, giving a single-element window.

## Dry run

Sample: the range $1 \dots 10$.

| $n$ | form | divisor count | prime? |
|---:|---|---:|:---:|
| 2 | $2^1$ | 2 | yes |
| 3 | $3^1$ | 2 | yes |
| 4 | $2^2$ | 3 | yes |
| 5 | $5^1$ | 2 | yes |
| 7 | $7^1$ | 2 | yes |
| 9 | $3^2$ | 3 | yes |

Six such numbers, so the output is `6`. Note $6, 8, 10$ all have four divisors.

---

Same problem grouped by topic: [../docs/number-theory/PRETNUM.md](../docs/number-theory/PRETNUM.md)
