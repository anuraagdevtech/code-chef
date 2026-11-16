[&larr; 606. Player](RRPLAYER.md) &middot; [Index](../../README.md) &middot; [669. Expected Value &rarr;](EXPVALUE.md)

# 620. E - Make it Zero

> CodeChef problem code [`INFDIV`](https://www.codechef.com/problems/INFDIV) &middot; difficulty **2690** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Probability |
| **Technique** | Expectation recurrence over remainders, summed by quotient blocks |
| **Time** | $O(N \sqrt{N})$ |
| **Space** | $O(N \log N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are given two integers, $n$ and $m$. You want to make $m$ equal to $0$. You decide to keep repeating the following operation until $m$ becomes $0$:

- Choose an integer $r$, uniformly at random from the range $[1, n]$. Set $m$ equal to the remainder obtained on dividing it by $r$. That is, replace $m$ with $m \% r$, where $\%$ denotes the modulo operator.

Find the expected number of operations after which $m$ becomes $0$. Let the answer be equal to $E = \dfrac{P}{Q}$ for some integers $P$ and $Q$ such that $\gcd(P, Q) = 1$. Output the value of $P Q^{-1}$ modulo $10^9 + 7$, where $Q^{-1}$ denotes the modular inverse of $Q$ modulo $10^9 + 7$.

**Input**

The only line of the input contains two integers $n$ and $m$.

**Output**

Output one line containing the value of $P Q^{-1}$ modulo $10^9 + 7$ as described above.

## Constraints

- $1 \leq n \leq 200000$
- $1 \leq m \leq 10^{18}$

## Sample

**Sample input**

```
3 2
```

**Sample output**

```
500000005
```

<details><summary>Explanation</summary>

$m$ is initially $2$. In each operation, we choose a random number $r$ from $\{1, 2, 3\}$. If $r = 1$, then $m \% r = 0$, and we stop. If $r = 2$, then $m \% r = 0$, and we stop. If $r = 3$, then $m \% r = 2$, and we continue the process.

Hence, we will repeat the procedure until we get a $1$ or $2$. You can check that the expected number of steps needed to get this is $\frac{3}{2}$. Hence, we output $3 \times 2^{-1} = 3 \times 500000004 = 500000005 \mod 10^9 + 7$.

</details>

## Approach

Let $E(x)$ be the expected number of operations from value $x$. For $x < n$, a divisor $r > x$ leaves $x$ unchanged, so

$$E(x) = 1 + \frac{1}{n}\Bigl(\sum_{r \le x} E(x \bmod r) + (n - x) E(x)\Bigr) \;\Longrightarrow\; x \cdot E(x) = n + \sum_{r \le x} E(x \bmod r).$$

With $D(x) = E(x) / n$ this becomes $D(x) = \bigl(1 + \sum_{r \le x} D(x \bmod r)\bigr) / x$, which no longer depends on $n$. If $m < n$ the answer is $n \cdot D(m)$. If $m \ge n$ every divisor is at most $m$, so the answer is $1 + \sum_{r=1}^{n} D(m \bmod r)$, and only values below $n$ are ever needed.

Computing the inner sum naively is quadratic. Split the divisors at $\sqrt{x}$: small ones are added directly; large ones are grouped by the quotient $q = \lfloor x / r \rfloor$, and within a group the remainders $x - q r$ form an arithmetic progression with step $q$. Keeping, for each small $q$, prefix sums of $D$ along step $q$ turns every group into one or two lookups. A progression for quotient $q$ only ever needs indices up to $\text{limit} / (q + 1)$, which keeps the tables at $O(N \log N)$ cells.

## Solution (Python)

```python
import sys
from array import array
from math import isqrt


MOD = 1000000007


def expectations(limit):
    inverse = [0, 1] + [0] * max(0, limit - 1)
    for i in range(2, limit + 1):
        inverse[i] = MOD - MOD // i * inverse[MOD % i] % MOD
    values = [0] * (limit + 1)
    maxq = isqrt(limit)
    sums = [None] + [array('I', [0]) * (limit // (q + 1) + 1) for q in range(1, maxq + 1)]
    for value in range(1, limit + 1):
        root = isqrt(value)
        total = 1
        for divisor in range(1, root + 1):
            total += values[value % divisor]
        for quotient in range(1, value // (root + 1) + 1):
            left = max(root + 1, value // (quotient + 1) + 1)
            right = value // quotient
            low = value - quotient * right
            high = value - quotient * left
            row = sums[quotient]
            total += row[high]
            if low >= quotient:
                total -= row[low - quotient]
        current = total % MOD * inverse[value] % MOD
        values[value] = current
        for quotient in range(1, min(maxq, limit // value - 1) + 1):
            row = sums[quotient]
            row[value] = (current + (row[value - quotient] if value >= quotient else 0)) % MOD
    return values


def solve():
    n, m = map(int, sys.stdin.buffer.read().split())
    if m < n:
        print(n * expectations(m)[m] % MOD)
        return
    remainders = [m % r for r in range(1, n + 1)]
    values = expectations(max(remainders))
    print((1 + sum((values[r] for r in remainders))) % MOD)


if __name__ == "__main__":
    solve()
```

## Complexity

- **Time:** $O(N \sqrt{N})$
- **Space:** $O(N \log N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $r = 1$ always ends the process; $D(0) = 0$.
- $m$ can be as large as $10^{18}$, but only $m \bmod r$ for $r \le n$ is used.
- When $m < n$ only values up to $m$ are computed.
- Results are fractions modulo $10^9 + 7$; inverses of $1 \dots$ limit are precomputed linearly.

## Dry run

`n = 3, m = 2`. Since $m < n$ the answer is $3 \cdot D(2)$.

$D(1) = (1 + D(0)) / 1 = 1$. $D(2) = (1 + D(2 \bmod 1) + D(2 \bmod 2)) / 2 = 1/2$.

Answer $3/2$, printed as $3 \cdot 2^{-1} \bmod (10^9 + 7) = 500000005$. Check: each operation stops with probability $2/3$, so the expectation is $3/2$.

---

Same problem in rating order (#705 of 735): [../../by-rating/705-INFDIV.md](../../by-rating/705-INFDIV.md)
