[&larr; 362. XOR-ORED](362-XORORED.md) &middot; [Index](README.md) &middot; [364. Construct Array &rarr;](364-CONSTRRAY.md)

# 363. Non-Divisor Array

> [`DIVCOL`](https://www.codechef.com/problems/DIVCOL) &middot; difficulty **1623** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Colouring the divisibility order by prime-factor count |
| **CodeChef tags** | `Algorithms`, `Mathematics`, `Constructive` |
| **Complexity class** | Near-linear $O(n \log \log n)$ |
| **Time** | $O(N \log \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an integer $N$.
Your task is to find the **minimum** integer $C$ such that there exists an array $A$ of size $N$ satisfying:
- $1\le A_i \le C$;
- For distinct indices $x$ and $y$ where $x$ **divides** $y; \ A_x \neq A_y$.

You need to print the minimum value of $C$ as well as the array $A$. In case multiple arrays exist, you may print any one.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$.

**Output**

For each test case, output two lines.
- The first line should contain a single integer $C$, the minimum integer for which array $A$ exists.
- The second line should contain $N$ space-separated integers $A_1, A_2, \ldots, A_N$ denoting the array $A$ satisfying given conditions.

In case multiple arrays satisfy the conditions, you may print any one.

## Constraints

- $1 \le T \le 10^3$
- $1 \le N \le 2 \cdot 10^5$
- The sum of $N$ does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
2
1
3
```

**Sample output**

```
1
1
2
2 1 1
```

<details><summary>Explanation</summary>

**Test case $2$** : We needed to ensure:

- $A_1 \ne A_2$;
- $A_1 \ne A_3$

It can be verified that the given array $[2, 1, 1]$ does that with the minimum value of $C$ , i.e. $2$.

</details>

## Approach

**The lower bound.** The chain $1 \mid 2 \mid 4 \mid \cdots \mid 2^k$ lies entirely inside $1 \ldots N$ whenever $2^k \leq N$, and every element of a chain must get a different value. The longest such chain has $\lfloor \log_2 N \rfloor + 1$ elements, so

$$C \geq \lfloor \log_2 N \rfloor + 1$$

**A matching construction.** Let $\Omega(i)$ count the prime factors of $i$ **with multiplicity**, and set

$$A_i = \Omega(i) + 1$$

If $x \mid y$ with $x \neq y$, then $y = x \cdot m$ for some $m > 1$, so $\Omega(y) = \Omega(x) + \Omega(m) > \Omega(x)$ — the values differ, as required. In fact they are strictly ordered along every divisibility chain, which is more than the problem demands.

The largest value used is $\Omega(2^k) + 1 = k + 1$ where $2^k \leq N$, matching the lower bound exactly. So this $C$ is optimal.

$\Omega$ is computed for the whole range with a smallest-prime-factor sieve and the recurrence $\Omega(i) = \Omega(i / \mathrm{spf}(i)) + 1$, seeded by $\Omega(1) = 0$.

For $N = 3$ this gives $C = 2$ and $A = [1, 2, 2]$. The published sample prints $[2, 1, 1]$ — the same colouring with the two values swapped, equally valid — so this is judged by a checker. $N = 1$ gives $C = 1$ and $A = [1]$.

Note it is $\Omega$ (with multiplicity) rather than $\omega$ (distinct primes) that is needed: $\omega(2) = \omega(4) = 1$ would collide on the chain $2 \mid 4$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    sizes = [int(data[1 + i]) for i in range(t)]
    limit = max(sizes) + 1
    # Smallest prime factor, then Omega(i) = Omega(i / spf) + 1.
    spf = list(range(limit))
    i = 2
    while i * i < limit:
        if spf[i] == i:
            for j in range(i * i, limit, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    omega = [0] * limit
    for v in range(2, limit):
        omega[v] = omega[v // spf[v]] + 1
    out = []
    for n in sizes:
        # x | y with x != y forces Omega(y) > Omega(x), so colours differ.
        out.append(str(omega[n and 1 << (n.bit_length() - 1)] + 1))
        out.append(" ".join(str(omega[v] + 1) for v in range(1, n + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$\Omega(i) + 1$ is a valid colouring**, because $x \mid y$ with $x \neq y$ forces $\Omega(y) > \Omega(x)$ — the quotient contributes at least one more prime factor — so the colours of a divisor pair always differ.
- **It is also optimal.** The chain $1 \mid 2 \mid 4 \mid \dots \mid 2^k \leq N$ has $k+1$ members all pairwise divisible, so $C \geq k+1$; and $\Omega(i) \leq \log_2 i \leq k$ gives $C \leq k+1$.
- **So $C = \lfloor \log_2 N \rfloor + 1$**, computed here as $\Omega$ of the highest power of two not exceeding $N$, plus one.
- **$N = 1$** gives $C = 1$: a single element with no divisor pair to worry about.
- **$\Omega$ counts multiplicity, not distinct primes.** $\Omega(4) = 2$ while $\omega(4) = 1$, and using the distinct count would give $4$ and $2$ the same colour despite $2 \mid 4$.
- **The smallest-prime-factor sieve gives $\Omega$ in one pass** via $\Omega(v) = \Omega(v / \mathrm{spf}(v)) + 1$, which is why the sieve stores spf rather than just primality.
- **This colouring differs from the sample's** at $N = 3$ (`1 2 2` against `2 1 1`), and both use $C = 2$ validly, so a special judge checks the divisor pairs.

## Dry run

$N = 3$: the highest power of two is $2$, so $C = \Omega(2) + 1 = 2$.

| $i$ | factorisation | $\Omega(i)$ | colour |
|---:|---|---:|---:|
| 1 | — | 0 | 1 |
| 2 | $2$ | 1 | 2 |
| 3 | $3$ | 1 | 2 |

Divisor pairs: $1 \mid 2$ (colours $1 \neq 2$ ✓) and $1 \mid 3$ ($1 \neq 2$ ✓). The pair $2, 3$ has no divisibility, so sharing colour $2$ is fine.

---

Same problem grouped by topic: [../docs/number-theory/DIVCOL.md](../docs/number-theory/DIVCOL.md)
