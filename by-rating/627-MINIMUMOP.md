[&larr; 626. Sum of Goodness](626-SEQGOODNESS.md) &middot; [Index](README.md) &middot; [628. Increase 2 consecutive characters &rarr;](628-CCD.md)

# 627. Minimum Operation

> [`MINIMUMOP`](https://www.codechef.com/problems/MINIMUMOP) &middot; difficulty **2170** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | At most two operations - common gcd, an unused prime, or 2 then 3 |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation`, `Divisors`, `Sieve of Eratosthenes`, `Prime Divisors` |
| **Complexity class** | Linearithmic $O(n \log n)$ (one-off precomputation) |
| **Time** | $O(M_{\max} \log \log M_{\max})$ sieve, then $O(N \log A)$ per test case |
| **Space** | $O(M_{\max} + N)$ |

## Question

You are given positive integers $N$ and $M$ $(M \geq 2)$.
You are also given an array $A$ of size $N$, such that $2 \leq A_i \leq M$.

In one operation on the array, you can:
- Select an integer $X$ $(2 \leq X \leq M)$ and change $A_i$ to $\gcd(A_i,X)$ for **all** $1 \leq i \leq N$.
Note that $\gcd$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

Your task is to make all the elements of $A$ **equal**.
Find the **minimum** number of operations required to do so and also print the selected integer $X$ for each operation.
If there are multiple ways to do so, you may print any.

It can be proven that it is always possible to make all the elements of $A$ equal in finite number of operations.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two integers $N$ and $M$ — the length of the array $A$ and maximum value of $X$ allowed.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$,  representing the array $A$.

**Output**

For each test case, in the first line, print an integer $Z$, denoting the number of operations required.

In case $Z\gt 0$, print another line with $Z$ space-separated integers where the $i^{th}$ integer represents the selected integer $X$ selected in the $i^{th}$ operation in **order**.

If there are multiple ways to do so, you may print any.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $2 \leq M \leq 10^6$
- $2 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.
- Note that sum of $M$ over all test case isn't bounded.

## Sample

**Sample input**

```
2
3 343
343 343 343
5 100
4 8 12 16 20
```

**Sample output**

```
0
1
4
```

<details><summary>Explanation</summary>

**Test case $1$:** Since all elements of the array are already equal, we require $0$ operations.

**Test case $2$:** We require only one operation:
- Select $X = 4$: Thus, the array becomes $[\gcd(4, 4), \gcd(4, 8), \gcd(4, 12), \gcd(4, 16), \gcd(4, 20)] = [4, 4, 4, 4, 4]$, where all elements are equal.

Note that this is the minimum number of operations required.

</details>

## Approach

- All elements already equal: 0 operations.
- Otherwise let $g$ be the gcd of the array. If $g > 1$, the single operation $X = g$ turns every element into $g$.
- If $g = 1$: after one operation with $X$ all elements equal some $d$, which divides every element, so $d = 1$ and $X$ must be coprime to every element. The cheapest such $X$ is the smallest prime that divides none of the elements; if it is at most $M$, one operation suffices.
- If no such prime fits under $M$, one operation is impossible, and two always work: $X = 2$ leaves only ones and twos, and $X = 3$ then turns everything into 1.

The primes dividing the elements are collected with a smallest-prime-factor sieve built once up to $10^6$.

## Solution

```python
import sys
from math import gcd, isqrt


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    LIMIT = 1000000
    spf = list(range(LIMIT + 1))
    primes = []
    for i in range(2, LIMIT + 1):
        if spf[i] == i:
            primes.append(i)
            if i <= 1000:
                for j in range(i * i, LIMIT + 1, i):
                    if spf[j] == j:
                        spf[j] = i
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        values = [next(tokens) for _ in range(n)]
        if min(values) == max(values):
            out.append('0')
            continue
        common = 0
        for x in values:
            common = gcd(common, x)
        if common > 1:
            out.extend(['1', str(common)])
            continue
        used_primes = set()
        for x in set(values):
            while x > 1:
                prime = spf[x]
                used_primes.add(prime)
                while x % prime == 0:
                    x //= prime
        prime = next((prime for prime in primes if prime not in used_primes))
        if prime <= m:
            out.extend(['1', str(prime)])
        else:
            out.extend(['2', '2 3'])
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Equal elements need no operation, whatever their gcd.
- $X$ must lie in $[2, M]$, which is why an unused prime larger than $M$ does not help.
- When two operations are needed, $M \ge 3$ is guaranteed because the elements are not all equal.
- The number of operations is unique but the chosen $X$ values are not, so a checker validates the output.

## Dry run

- `A = [4, 8, 12, 16, 20]`: gcd 4, so one operation with $X = 4$.
- `A = [2, 3]`, `M = 3`: gcd 1; the primes 2 and 3 are both used and the next prime 5 exceeds $M$. Two operations: `2 3` - after $X = 2$ the array is `[2, 1]`, after $X = 3$ it is `[1, 1]`.

---

Same problem grouped by topic: [../docs/number-theory/MINIMUMOP.md](../docs/number-theory/MINIMUMOP.md)
