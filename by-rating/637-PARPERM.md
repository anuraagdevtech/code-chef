[&larr; 636. Chef and insomnia](636-CHINSM.md) &middot; [Index](README.md) &middot; [638. Is This JEE &rarr;](638-ICM2003.md)

# 637. Partition It

> [`PARPERM`](https://www.codechef.com/problems/PARPERM) &middot; difficulty **2202** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Only 1 and the primes above N/2 can be separated from the rest |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Algorithms`, `Sieve of Eratosthenes`, `Implementation` |
| **Complexity class** | Linear $O(n)$ (one-off precomputation) |
| **Time** | $O(N \log \log N)$ sieve, then $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has the $N$ numbers $1, 2, 3, \dots, N$. He wants to give exactly $K$ of these numbers to his friend and keep the rest with him.

He can choose any $K$ numbers such that the [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) of any number from Chef's set and any number from his friend's set is equal to $1$.

Formally, suppose Chef gives the set of numbers $A$ to his friend and keeps $B$ with himself (where $|A| = K$ and $|B| = N - K$). Then $A$ and $B$ must satisfy

$$
\gcd(a, b) = 1 \ \ \forall a\in A, b\in B
$$

Chef needs your help in choosing these $K$ numbers. Please find any valid set of $K$ numbers that will satisfy the condition, or tell him that no such set exists.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

**Output**

For each test case first output a single line containing "YES" (without quotes) if a set of size $K$ satisfying Chef's condition exists; and "NO" if no such set exists. This line is not case-sensitive so "YeS", "nO", etc. are also acceptable.

Next, if the answer is "YES", print another line containing $K$ distinct space-separated integers from $1$ to $N$ denoting the numbers which Chef will give to his friend. The integers can be printed in any order.

If there are multiple solutions, you may print any of them.

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq K \leq N - 1$
- Sum of $N$ over all test cases does not exceed $5*10^5$

## Sample

**Sample input**

```
3
4 1
4 2
6 3
```

**Sample output**

```
Yes
3
Yes
4 2
No
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can give $[3]$ to his friend and keep $[1, 2, 4]$ for himself. $3$ is coprime with $1, 2$ and $4$ so the condition is satisfied. Another possible solution is Chef giving $[1]$ to his friend.

**Test case $2$:** Chef can give $[2, 4]$ and keep $[1, 3]$ (or vice versa). It can be seen that $\gcd(2, 1) = 1$, $\gcd(2, 3) = 1$, $\gcd(4, 1) = 1$, $\gcd(4, 3) = 1$ and so the condition is satisfied.

**Test case $3$:** There is no set of 3 numbers that can satisfy the given condition.

</details>

## Approach

Build a graph on $1 \dots N$ joining two numbers when their gcd exceeds 1. Two numbers in the same connected component must go to the same side, so a valid split is a union of components.

Which components are there? The number 1 is alone. A prime $p > N/2$ has no other multiple up to $N$, so it is alone too. Everything else hangs together: a prime $p \le N/2$ is joined to $2p$ and hence to 2, and every composite is joined to its prime factors, all of which are at most $N/2$. So there is one big component and a set of isolated vertices.

One side of the split must therefore consist only of isolated vertices. If $K$ is at most the number of isolated vertices, give $K$ of them to the friend. Otherwise the friend must take the big component, and Chef's $N - K$ numbers must all be isolated; if that fits, give the friend everything except $N - K$ isolated numbers. If neither fits the answer is NO.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    LIMIT = 100000
    sieve = bytearray(b'\x01') * (LIMIT + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, 317):
        if sieve[p]:
            sieve[p * p:LIMIT + 1:p] = b'\x00' * ((LIMIT - p * p) // p + 1)
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        isolated = [1] + [p for p in range(n // 2 + 1, n + 1) if sieve[p]]
        if k <= len(isolated):
            out.append('YES')
            out.append(' '.join(map(str, isolated[:k])))
        elif n - k <= len(isolated):
            removed = set(isolated[:n - k])
            out.append('YES')
            out.append(' '.join((str(i) for i in range(1, n + 1) if i not in removed)))
        else:
            out.append('NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $N = 2$ or $3$: every number is isolated and any split works.
- Any valid set may be printed; the judge checks the gcd condition.
- The "complement" case is needed when $K$ is large.
- The sieve is built once up to the maximum $N$.

## Dry run

`N = 6`: isolated numbers are 1 and 5 (the only prime above 3).

- $K = 3$: more than 2 isolated numbers would be needed on one side, and $N - K = 3$ is also more than 2. NO.
- $K = 2$: `1 5`.
- $K = 4$: Chef keeps the two isolated numbers and the friend gets `2 3 4 6`.

---

Same problem grouped by topic: [../docs/number-theory/PARPERM.md](../docs/number-theory/PARPERM.md)
