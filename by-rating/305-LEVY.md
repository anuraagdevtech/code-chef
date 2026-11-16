[&larr; 304. Magda and Silly Pairs](304-SILLYPRS.md) &middot; [Index](README.md) &middot; [306. Paying up &rarr;](306-MARCHA1.md)

# 305. Levy Conjecture

> [`LEVY`](https://www.codechef.com/problems/LEVY) &middot; difficulty **1510** &middot; time limit **1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Precompute counts of prime plus twice-prime sums |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(V\log\log V+\pi(V)^2+T)$ overall for $V=\max N$ |
| **Space** | $O(V+T)$ |

## Question

**Problem Statement**

**Levy's conjecture**, named after **Hyman Levy**, states that all odd integers greater than **5** can be represented as the sum of an odd prime number and an even semiprime. To put it algebraically, **2n + 1 = p + 2q** always has a solution in primes **p** and **q** (not necessary to be distinct) for **n > 2**. *(Source: [Wikipedia](http://en.wikipedia.org/wiki/Lemoine))*

In this problem, given a positive integer **N** (not necessary to be odd integer greater than **5**). Your task is to calculate how many distinct ordered pairs **(p, q)** such that **N = p + 2q**, where **p** and **q** are primes.

**Input**

The first line of input contains an integer **T**, denoting the number of test cases. Then **T** test cases follow.

Each test case consists of exactly one line containing an integer **N**.

**Constraints**

- **1** ≤ **T** ≤ **100000 (10^5)**

- **1** ≤ **N** ≤ **10000 (10^4)**

**Output**

For each test case, output the number of ordered pairs **(p, q)** of primes such that **N = p + 2q**.

## Constraints

- 1 ≤ T ≤ 100000 (10^5)
- 1 ≤ N ≤ 10000 (10^4)

## Sample

**Sample input**

```
3
2
7
11
```

**Sample output**

```
0
1
2
```

<details><summary>Explanation</summary>

**Case #1:** There are no ordered pairs **(p, q)** such that **p + 2q = 2**.

**Case #2:** There is only one ordered pair **(p, q) = (3, 2)** such that **p + 2q = 7**.

**Case #3:** There are two ordered pairs **(p, q) = (7, 2), (5, 3)** such that **p + 2q = 11**.

</details>

## Approach

Sieve primes up to the largest query. For every prime $q$, enumerate primes $p$ while $p+2q$ stays within that bound, incrementing the answer at that sum.

The enumeration counts ordered pairs exactly once: $p$ and $q$ have different roles in the equation. Queries then become table lookups. The bound $V\le10000$ makes this pair precomputation small.

## Solution

```python
import sys
from math import isqrt

def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    limit = max(values[1:])
    primes = [i for i,v in enumerate(sieve(limit)) if v]
    answers = [0]*(limit+1)
    for q in primes:
        if 2*q+2 > limit:
            break
        for p in primes:
            total = p+2*q
            if total > limit:
                break
            answers[total] += 1
    sys.stdout.write('\n'.join(str(answers[n]) for n in values[1:])+'\n')

if __name__ == '__main__':
    main()
```

## Edge cases

- The input need not be odd or greater than five.
- Two is a valid prime in either role.
- The two primes may be equal.

## Dry run

For `N=11`, pairs `(7,2)` and `(5,3)` satisfy the equation. Both are counted, so the answer is two.

---

Same problem grouped by topic: [../docs/number-theory/LEVY.md](../docs/number-theory/LEVY.md)
