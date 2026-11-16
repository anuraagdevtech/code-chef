[&larr; 650. Make Them Alike](650-ALIKE_THEM.md) &middot; [Index](README.md) &middot; [652. Maximize 1s &rarr;](652-MAX1S.md)

# 651. Interesting Representation

> [`INTREP`](https://www.codechef.com/problems/INTREP) &middot; difficulty **2251** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Multiply N by two neighbouring numbers that each add exactly one new prime |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation`, `Divisors`, `Algorithms`, `Constructive`, `Prime Divisors`, `ad-hoc`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Given a positive integer $N$, find two positive integers $A$ and $B$, such that $A - B = N$ and the number of **distinct** prime factors of $A$ and $B$ are equal. If there exist multiple pairs of values of $A$ and $B$ satisfying the given conditions, you can output any one of them.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, integer $N$.

**Output**

For each testcase, output in a single line two space separated integers $A$ and $B$.
If there are multiple answers, you can output any one of them.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^{16}$
- $1 \leq A, B \leq 10^{18}$

**Subtasks**

Subtask 1 (100 points): Original constraints

## Sample

**Sample input**

```
3
1
8
135
```

**Sample output**

```
3 2
97 89
1071 936
```

## Approach

Look for $A = (m + 1) N$ and $B = m N$; their difference is $N$ automatically.

- $N$ even: take $A = 2N$, $B = N$. Multiplying by 2 adds no new prime, so both have the same set of prime factors.
- $N$ odd: let $p$ be the smallest odd prime that does not divide $N$, and take $A = pN$, $B = (p - 1) N$. $A$ has the primes of $N$ plus $p$. For $B$, the number $p - 1$ is even, and all of its odd prime factors are odd primes smaller than $p$, which divide $N$ by the choice of $p$; so $B$ has the primes of $N$ plus exactly the prime 2. Both counts are one more than for $N$.

The product of all odd primes up to 47 exceeds $10^{16}$, so $N$ cannot be divisible by all of them and $p \le 47$ always, and $A = pN \le 47 \cdot 10^{16} < 10^{18}$.

## Solution

```python
import sys


def solve(tokens):
    n = next(tokens)
    if n % 2 == 0:
        return str(2 * n) + ' ' + str(n)
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47):
        if n % p:
            return str(p * n) + ' ' + str((p - 1) * n)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $N = 1$: $p = 3$, giving `3 2`, one prime each.
- Even $N$ never needs a prime search.
- The bound $A, B \le 10^{18}$ is why the smallest missing prime is used.
- Any valid pair is accepted.

## Dry run

`N = 135 = 3^3 * 5`: odd, and the smallest odd prime not dividing it is 7.

$A = 7 \cdot 135 = 945 = 3^3 \cdot 5 \cdot 7$ and $B = 6 \cdot 135 = 810 = 2 \cdot 3^4 \cdot 5$: three distinct primes each, and $945 - 810 = 135$.

`N = 8`: even, so `16 8`, both with the single prime 2.

---

Same problem grouped by topic: [../docs/number-theory/INTREP.md](../docs/number-theory/INTREP.md)
