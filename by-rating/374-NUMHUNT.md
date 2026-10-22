# 374. Number Hunt

> [`NUMHUNT`](https://www.codechef.com/problems/NUMHUNT) &middot; difficulty **1638** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Product of the two smallest admissible primes |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Primes` |
| **Complexity class** | Polylogarithmic $O(\log^2 n)$ |
| **Time** | $O(g \log^3 X)$ per test case, where $g$ is the local prime gap |
| **Space** | $O(1)$ |

## Question

Given a positive integer $X$, find the **smallest** positive integer $Y$ satisfying all of the following conditions:
- $Y$ should not be a [prime](https://en.wikipedia.org/wiki/Prime_number);
- $Y$ should not be a [perfect square](https://en.wikipedia.org/wiki/Square_number);
- No [factor](https://en.wikipedia.org/wiki/Divisor) of $Y$ other than $1$ is less than $X$.

Note that $Y$ might not fit in a $32$ bit integer.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a positive integer $X$ as mentioned in the statement.

**Output**

For each test case, output on a new line, the **smallest** positive integer $Y$ satisfying the given conditions.

Note that $Y$ might not fit in a $32$ bit integer.

## Constraints

- $1 \leq T \leq 5$
- $1 \leq X \leq 10^9$

## Sample

**Sample input**

```
3
1
2
3
```

**Sample output**

```
6
6
15
```

<details><summary>Explanation</summary>

**Test case $1$:** Let us consider all values of $Y$ in increasing order:
- $Y = 2$: It is a prime.
- $Y = 3$: It is a prime.
- $Y = 4$: It is a perfect square $(4 = 2^2)$.
- $Y = 5$: It is a prime.
- $Y = 6$: It is neither prime, nor a perfect square. The non-$1$ factors of $6$ are $2, 3$ and $6$, none of which are less than $X = 1$.

Thus, $6$ is the smallest integer satisfying the given conditions.

**Test case $2$:** $Y = 6$ has non-$1$ factors $2, 3,$ and $6$, none of which are less than $X = 2$.

**Test case $3$:** The smallest integer satisfying the conditions is $15$. The non-$1$ factors of $15$ are $3, 5$ and $15$, none of which are less than $X = 3$.

</details>

## Approach

Translate each condition into the factorisation of $Y$:

- "no factor other than $1$ below $X$" means **every prime factor of $Y$ is at least $X$**;
- "not prime" means $Y$ has at least two prime factors counted with multiplicity;
- "not a perfect square" rules out $Y = p^2$, the smallest two-factor option.

So $Y = pq$ with $p \neq q$ both prime and both $\geq X$, and the minimum is obtained by taking $p$ as the smallest prime $\geq X$ and $q$ as the next prime after it. Nothing smaller can work: $p^2$ is excluded as a square, and any product of three or more admissible primes is at least $p^3 > pq$ (since $q < p^2$ by Bertrand's postulate).

At $X \leq 10^9$ the candidates are far too large to sieve, so test individual numbers with a deterministic **Miller–Rabin** over the bases $2, 3, 5, \ldots, 37$, which is exact below $3 \times 10^{24}$. Prime gaps near $10^9$ are only a few hundred, so a handful of tests per query suffices and $T \leq 5$ makes this trivial.

The samples show the small cases and the square trap. $X = 1$ and $X = 2$ both give $2 \cdot 3 = 6$ — note $4 = 2^2$ is rejected as a square, which is why the answer is not $4$. $X = 3$ skips $4$ (factor $2 < 3$) and $9 = 3^2$ (square), landing on $3 \cdot 5 = 15$.

The statement's warning about 32-bit overflow is the product: near $X = 10^9$ the answer is about $10^{18}$.

## Solution

```python
import sys

BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in BASES:
        if n % p == 0:
            return n == p
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in BASES:                 # deterministic below 3 * 10^24
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n: int) -> int:
    while not is_prime(n):
        n += 1
    return n


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        x = int(tok)
        # Two distinct primes: p^2 would be a square, p^3 would be larger.
        p = next_prime(max(2, x))
        out.append(str(p * next_prime(p + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The three conditions force the shape $p \cdot q$ with $p < q$ the two smallest primes at least $X$.** No factor below $X$ means every prime factor is $\geq X$; not prime means at least two factors; not a perfect square rules out $p^2$.
- **$p^2$ is the trap.** It is the smallest composite with all factors $\geq p$, and it is excluded precisely because it is a square — which is why the next prime is needed.
- **$p \cdot q$ beats $p^3$**, since Bertrand's postulate gives $q < 2p \leq p^2$ for $p \geq 2$, so no cube can undercut it.
- **$X = 1$ and $X = 2$ give the same answer**, $6$: the smallest prime at least $1$ is still $2$. Note $4$ is rejected as a square.
- **The answer may exceed 32 bits**, as the statement warns: near $X = 10^9$ the product is about $10^{18}$.
- **Primality must be tested, not sieved.** At $X = 10^9$ a sieve is out of the question, so Miller–Rabin with the first twelve prime bases is used — deterministic well past $10^{18}$.
- **$T \leq 5$** keeps the prime-gap walk cheap; gaps near $10^9$ are only a few hundred.

## Dry run

| $X$ | smallest prime $\geq X$ | next prime | $Y$ |
|---:|---:|---:|---:|
| 1 | 2 | 3 | `6` |
| 2 | 2 | 3 | `6` |
| 3 | 3 | 5 | `15` |

For $X = 3$: $9 = 3^2$ is a square, $3 \cdot 5 = 15$ is composite, non-square, and its only factors are $1, 3, 5, 15$ — none below $3$.

---

Same problem grouped by topic: [../docs/number-theory/NUMHUNT.md](../docs/number-theory/NUMHUNT.md)
