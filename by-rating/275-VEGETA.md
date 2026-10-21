# 275. Majin Vegeta

> [`VEGETA`](https://www.codechef.com/problems/VEGETA) &middot; difficulty **1477** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Sieve counting distinct prime factors |
| **CodeChef tags** | `prime-factorization`, `sieve-of-eratosthenes` |
| **Complexity class** | Linear $O(n)$ (one-off precomputation) |
| **Time** | $O(V \log\log V)$ once, then $O(m - n)$ per query |
| **Space** | $O(V)$ with $V = 10^6$ |

## Question

Babidi has summoned Majin Vegeta. He orders him to kill Supreme Kai. But Vegeta wants to get out of his control.

Babidi has laid out a trap. Vegeta is standing at the $nth$ level of mind control. In order to defeat Babidi's trap, he needs to reach $mth$ level. The levels are continuous increasing integers. At each increment of level, $nth$ to $(n+1)th$ level, for example, the energy used is - number of distinct prime factors of $n$.

Vegeta needs your help in order to figure out how much total minimum energy he needs to defeat Babidi's trap. The total energy is the sum of energy used at each increment of a level.In the calculation of energy, $n$ and $m$ are inclusive.

**Input:**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follow.
- The first and only line of each test case contains the two integers $n$ and $m$, separated by a single space.

**Output:**
For each test case, print a single line containing one integer denoting the energy needed by Vegeta to escape Babidi's mind control and continue his battle with Kakarot.

**Constraints**
- $1 \leq T \leq 2$
- $1 \leq n \leq m \leq 10^6$

## Constraints

- $1 \leq T \leq 2$
- $1 \leq n \leq m \leq 10^6$

## Sample

**Sample input**

```
2
3 7
1 1023
```

**Sample output**

```
5
2177
```

<details><summary>Explanation</summary>

Example case 1: Vegeta is standing at $n$=3. As he moves from 3 to 4, energy used is 1. From 4 to 5, energy used is 1. Similarly, as he continues to move towards m=7, the total energy used is 1+1+1+2=5.

</details>

## Approach

The energy for the step from level $k$ to $k+1$ is $\omega(k)$, the number of **distinct** prime factors of $k$. Travelling from $n$ to $m$ means taking the steps at $n, n+1, \ldots, m-1$, so the total is

$$\sum_{k=n}^{m-1} \omega(k)$$

Note the upper limit: the step *out of* level $m$ is never taken, so $\omega(m)$ is excluded. The statement's phrase about $n$ and $m$ being inclusive refers to the levels visited, not the steps paid for — and the sample settles it. From $3$ to $7$ the costs are $\omega(3), \omega(4), \omega(5), \omega(6) = 1, 1, 1, 2$, totalling $5$. Including $\omega(7)$ would give $6$.

Computing $\omega$ for every value up to $10^6$ is a **modified sieve**: start an array of zeros and, for each $p$ from $2$ upward, if $\omega[p]$ is still $0$ then $p$ is prime, so add $1$ to every multiple of $p$. Each number ends up counting exactly its distinct prime divisors. That is $O(V \log\log V)$ overall — the same shape as Eratosthenes, but incrementing instead of marking.

Note $\omega(1) = 0$, since $1$ has no prime factors; the sieve gives this for free by never touching index $1$.

A prefix-sum array over $\omega$ would make each query $O(1)$, which would matter for many queries — but $T \leq 2$ here, so a direct sum over the range is plenty. Building the sieve once, outside the test-case loop, is the part that actually matters.

## Solution

```python
import sys

LIMIT = 10 ** 6 + 1


def build_omega():
    """omega[k] = number of distinct prime factors of k."""
    omega = [0] * LIMIT
    for p in range(2, LIMIT):
        if omega[p] == 0:                 # p is prime
            for multiple in range(p, LIMIT, p):
                omega[multiple] += 1
    return omega


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    omega = build_omega()
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # The step out of level m is never taken, so stop at m - 1.
        out.append(str(sum(omega[n:m])))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The step out of level $m$ is never taken**, so the sum runs over $n \dots m-1$ — slicing to `omega[n:m]` is what encodes that. Including $m$ overshoots by $\omega(m)$, which the first sample would report as $5 + 1 = 6$.
- **$n = m$** → he is already there, and the empty slice sums to $0$.
- **$\omega(1) = 0$**, which the sieve gives for free since $1$ has no prime factors — and the second row starts at $1$.
- **Distinct prime factors, not total**: $\omega(8) = 1$ and $\omega(12) = 2$, so the sieve increments each multiple once per *prime*, never per prime power.
- **A prime is detected by $\omega(p)$ still being $0$** when the outer loop reaches it, which is what makes the single pass both a sieve and a counter.
- **The sieve is built once for all test cases** ($T \leq 2$), at $10^6$ entries, after which each query is a slice sum.

## Dry run

First sample: $n = 3$, $m = 7$.

| level $k$ | distinct prime factors | $\omega(k)$ |
|---:|---|---:|
| 3 | $3$ | 1 |
| 4 | $2$ | 1 |
| 5 | $5$ | 1 |
| 6 | $2, 3$ | 2 |

Total `5`. Level $7$ is the destination, so its own $\omega$ is not spent.

---

Same problem grouped by topic: [../docs/number-theory/VEGETA.md](../docs/number-theory/VEGETA.md)
