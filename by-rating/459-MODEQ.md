[&larr; 458. Compare those strings](458-STRCOMPARE.md) &middot; [Index](README.md) &middot; [460. Chef Restaurant  &rarr;](460-CHEFRES.md)

# 459. Modular Equation

> [`MODEQ`](https://www.codechef.com/problems/MODEQ) &middot; difficulty **1761** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Reducing a nested modulo to a divisibility test |
| **Complexity class** | Product of two sizes $O(n m)$ (one-off precomputation) |
| **Time** | $O(N \cdot d)$ per test case after an $O(M)$ sieve |
| **Space** | $O(M)$ |

## Question

Given integers $N$ and $M$, find the number of ordered pairs $(a, b)$ such that $1 \le a < b \le N$ and $((M\ \mathrm{mod}\ a)\ \mathrm{mod}\ b) = ((M\ \mathrm{mod}\ b)\ \mathrm{mod}\ a)$.

**Input**
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The only line of each test case contains two integers $N$, $M$.

**Output**
For each testcase, output in a single line the answer to the problem.

**Constraints**
- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^6$
- $1 \leq M \leq 5\cdot 10^5$
- The sum of $N$ over all test cases does not exceed $10^6$.

**Note:** Multiplier for JAVA for this problem is reduced to $1.25$ instead of usual $2$.

**Subtasks**
**Subtask #1 (10 points):**
- $1 \leq T \leq 10$
- $2 \leq N \leq 10^3$
- $1 \leq M \leq 10^5$

**Subtask #2 (40 points):**
- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$
- The sum of $N$ over all test cases does not exceed $10^6$.

**Subtask #3 (50 points):** Original Constraints

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^6$
- $1 \leq M \leq 5\cdot 10^5$
- The sum of $N$ over all test cases does not exceed $10^6$.

## Sample

**Sample input**

```
3
3 5
3 6
3 10
```

**Sample output**

```
2
3
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** There are $2$ valid pairs satisfying the conditions. These are:
- $(1, 2)$: $(1 \le 1 \lt 2 \le N)$. Given $M = 5$, $((5 \%1) \%2) = (0\%2) = 0$. Also, $((5 \%2) \%1) = (1\%1) = 0$.
- $(1, 3)$: $(1 \le 1 \lt 3 \le N)$. Given $M = 5$, $((5 \%1) \%3) = (0\%3) = 0$. Also, $((5 \%3) \%1) = (2\%1) = 0$.

**Test Case $2$:** There are $3$ valid pairs satisfying the conditions. These are:
- $(1, 2)$: $(1 \le 1 \lt 2 \le N)$. Given $M = 6$, $((6 \%1) \%2) = (0\%2) = 0$. Also, $((6 \%2) \%1) = (0\%1) = 0$.
- $(1, 3)$: $(1 \le 1 \lt 3 \le N)$. Given $M = 6$, $((6 \%1) \%3) = (0\%3) = 0$. Also, $((6 \%3) \%1) = (0\%1) = 0$.
- $(2, 3)$: $(1 \le 2 \lt 3 \le N)$. Given $M = 6$, $((6 \%2) \%3) = (0\%3) = 0$. Also, $((6 \%3) \%2) = (0\%2) = 0$.

**Test Case $3$:** There are $2$ valid pairs satisfying the conditions. These are:
- $(1, 2)$: $(1 \le 1 \lt 2 \le N)$. Given $M = 10$, $((10 \%1) \%2) = (0\%2) = 0$. Also, $((10 \%2) \%1) = (0\%1) = 0$.
- $(1, 3)$: $(1 \le 1 \lt 3 \le N)$. Given $M = 10$, $((10 \%1) \%3) = (0\%3) = 0$. Also, $((10 \%3) \%1) = (1\%1) = 0$.

</details>

## Approach

Fix $a < b$. Then $M \bmod a < a < b$, so the outer modulo on the left does nothing:

$$(M \bmod a) \bmod b = M \bmod a$$

Writing $M = qb + r$ with $q = \lfloor M/b \rfloor$ and $r = M \bmod b$, the right-hand side is $r \bmod a$, and the condition becomes

$$(qb + r) \equiv r \pmod a \quad\Longleftrightarrow\quad qb \equiv 0 \pmod a$$

So the whole nested-modulo equation collapses to a **divisibility test**:

$$a \;\Big|\; b \left\lfloor \frac{M}{b} \right\rfloor \;=\; M - (M \bmod b)$$

Two immediate consequences. Whenever $a \mid b$ the condition holds automatically, so every such pair counts — including all pairs with $a = 1$. And when $b > M$ the quotient is $0$, making the product $0$, which every $a$ divides — so all $b - 1$ partners qualify.

Otherwise the count for a given $b$ is the number of divisors of $V_b = b\lfloor M/b\rfloor$ that fall below $b$, found by factorising $V_b$ through a smallest-prime-factor sieve and enumerating its divisors.

Sample $N = 3, M = 5$ gives $2$: the pairs with $a = 1$ both qualify, while $(2,3)$ has $V = 3$, which $2$ does not divide. Raising $M$ to $6$ makes $V = 6$ for that pair, so all three count.

The honest caveat: with $\sum N = 10^6$ this is near the edge in Python even though the algorithm is right — the sieve and divisor enumeration are what a C++ submission would breeze through.

## Solution

```python
import sys


def build_spf(limit):
    spf = list(range(limit + 1))
    i = 2
    while i * i <= limit:
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def divisors_below(v, bound, spf):
    """How many divisors of v are strictly below bound."""
    divs = [1]
    while v > 1:
        p = spf[v]
        power = 0
        while v % p == 0:
            v //= p
            power += 1
        divs = [d * p ** e for d in divs for e in range(power + 1)]
    return sum(1 for d in divs if d < bound)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = [(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(t)]
    spf = build_spf(max(m for _, m in cases))
    out = []
    for n, m in cases:
        total = 0
        for b in range(2, n + 1):
            # The nested modulo reduces to a | b * floor(M / b).
            v = b * (m // b)
            if v == 0:              # b > M, so every a < b divides 0
                total += b - 1
            else:
                total += divisors_below(v, b, spf)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The nested modulo collapses.** With $a < b$ we have $M \bmod a < a < b$, so the left side is just $M \bmod a$; and the condition becomes $M \bmod a = (M \bmod b) \bmod a$, i.e. $a \mid \bigl(M - (M \bmod b)\bigr) = a \mid b \lfloor M/b \rfloor$.
- **So for each $b$ the answer is the number of its partners below it that divide $b \lfloor M/b \rfloor$** — a divisor count, not a search over pairs.
- **$b > M$ makes the product zero**, and every $a$ divides $0$, so all $b-1$ partners qualify. Without that branch the divisor routine would be handed $0$ and loop forever.
- **$a < b$ is strict**, so the divisors counted are those strictly below $b$.
- **The divisors are generated from the smallest-prime-factor sieve**, built once across all test cases to the largest $M$ — re-factorising per pair would be far too slow.
- **$a = 1$ always qualifies**, since $1$ divides everything, so every $b \geq 2$ contributes at least one pair.
- **Sum of $N \leq 10^6$** with $M \leq 5 \cdot 10^5$, so the sieve dominates the memory and the per-$b$ divisor work stays small.

## Dry run

Second sample: $N = 3$, $M = 6$.

| $b$ | $\lfloor M/b \rfloor$ | $b \lfloor M/b \rfloor$ | divisors below $b$ | pairs |
|---:|---:|---:|---|---:|
| 2 | 3 | 6 | $\{1\}$ | 1 |
| 3 | 2 | 6 | $\{1, 2\}$ | 2 |

Output `3`. Checking $(2,3)$ directly: $((6 \bmod 2) \bmod 3) = 0$ and $((6 \bmod 3) \bmod 2) = 0$ ✓

---

Same problem grouped by topic: [../docs/number-theory/MODEQ.md](../docs/number-theory/MODEQ.md)
