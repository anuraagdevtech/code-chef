[&larr; 436. Summary Power](436-SUMPOWER.md) &middot; [Index](README.md) &middot; [438. Ceiling Sum &rarr;](438-CEILSUM.md)

# 437. Number of Factors

> [`NUMFACT`](https://www.codechef.com/problems/NUMFACT) &middot; difficulty **1710** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Add prime exponents across all factors |
| **Complexity class** | Trial factorisation $O(N \pi(\sqrt V))$ (one-off precomputation) |
| **Time** | $O(N\pi(\sqrt V))$ trial divisions per test case after a sieve to $\sqrt V$ |
| **Space** | $O(\pi(\sqrt V)+N\log V)$ |

## Question

Alice has learnt factorization recently. Bob doesn't think she has learnt it properly and hence he has decided to quiz her. Bob gives Alice a very large number and asks her to find out the number of factors of that number. To make it a little easier for her, he represents the number as a product of **N** numbers. Alice is frightened of big numbers and hence is asking you for help. Your task is simple. Given **N** numbers, you need to tell the number of distinct factors of the product of these **N** numbers.

**Input:**

First line of input contains a single integer **T**, the number of test cases.

Each test starts with a line containing a single integer **N**.
 The next line consists of **N** space separated integers (**A_i**).

**Output:**

For each test case, output on a separate line the total number of factors of the product of given numbers.

**Constraints:**

```
1 ≤ **T** ≤ 100
1 ≤ **N** ≤ 10
2 ≤ **A_i** ≤ 1000000
```

**Scoring:**

You will be awarded **40** points for correctly solving for **A_i** ≤ 100.

You will be awarded another **30** points for correctly solving for **A_i** ≤ 10000.

The remaining **30** points will be awarded for correctly solving for **A_i** ≤ 1000000.

## Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 10
2 ≤ A_i ≤ 1000000

## Sample

**Sample input**

```
3
3
3 5 7
3
2 4 6
2
5 5
```

**Sample output**

```
8
10
3
```

## Approach

If the product's prime factorisation is $\prod p^{e_p}$, each divisor independently chooses an exponent from zero through $e_p$. Its number of divisors is therefore $\prod(e_p+1)$.

Factor each input value by precomputed primes up to 1000, accumulating exponents by prime. Stop trial division when the next prime square exceeds the remaining value; any remainder greater than one is prime. Never form the enormous product itself.

## Solution

```python
import sys
from math import isqrt
from collections import Counter

def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime

PRIMES = [i for i,v in enumerate(sieve(1000)) if v]


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        exponents = Counter()
        for _ in range(n):
            value = int(next(tokens))
            for p in PRIMES:
                if p*p > value:
                    break
                while value%p == 0:
                    exponents[p] += 1
                    value //= p
            if value > 1:
                exponents[value] += 1
        answer = 1
        for exponent in exponents.values():
            answer *= exponent+1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Repeated input values add exponents, rather than multiply their separate divisor counts.
- A remaining large prime contributes exponent one.
- Return the exact count; there is no modulus.

## Dry run

For factors `[2,4,6]`, their product has factorisation `2^4 * 3`. Its divisor count is `(4+1)(1+1)=10`.

---

Same problem grouped by topic: [../docs/number-theory/NUMFACT.md](../docs/number-theory/NUMFACT.md)
