# 1666 &middot; The Optimal Pairs

> CodeChef problem code [`OPTPAIRS`](https://www.codechef.com/problems/OPTPAIRS) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | The minimum is always N, attained by a divisor family |
| **CodeChef tags** | `Number Theory`, `Mathematics`, `GCD` |
| **CodeChef category** | easy |
| **Time** | $O(\sqrt{N})$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/OPTPAIRS.md](../docs/number-theory/OPTPAIRS.md)

## Question

For two positive integers $a$ and $b$, let $g(a, b) =$ [gcd](https://en.wikipedia.org/wiki/Greatest_common_divisor)
$(a, b) +$ [lcm](https://en.wikipedia.org/wiki/Least_common_multiple)$(a, b)$.

For a positive integer $N$, let $f(N)$ denote the **minimum** value of $g(a, b)$ over all the pairs of positive integers $(a, b)$ such that $a+b = N$.

Find out the number of **ordered** pairs $(a, b)$ such that $a+b = N$ and $g(a, b) = f(N)$.

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a positive integer $N$.

**Output**

For each test case, output the number of **ordered** pairs $(a, b)$ such that $a+b = N$ and $g(a, b) = f(N)$.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^9$

## Sample

**Sample input**

```
2
4
105
```

**Sample output**

```
3
14
```

<details><summary>Explanation</summary>

**Test case $1$:**
- For the pair $(1, 3)$, $g(1, 3) = gcd(1,3)+lcm(1,3)=1+3=4$.
- For the pair $(2, 2)$, $g(2, 2) = gcd(2,2)+lcm(2,2)=2+2=4$.
- For the pair $(3, 1)$, $g(3, 1) = gcd(3,1)+lcm(3,1)=1+3=4$.

Hence, $f(4) = 4$. There are three pairs $(a, b)$ satisfying $a+b = N$ and $g(a, b) = f(N)$.

</details>

## Approach

Write $d = \gcd(a,b)$, $a = d a'$, $b = d b'$ with $\gcd(a',b') = 1$ and $a' + b' = s = N/d$. Then $\mathrm{lcm} = d a' b'$ and

$$g(a,b) = d + d a' b' = d\,(1 + a'b')$$

For coprime positive $a', b'$ summing to $s$, the product $a'b'$ is smallest when they are as lopsided as possible, namely $\{1, s-1\}$, giving $a'b' = s - 1$. So $g \geq d \cdot s = N$, and therefore

$$f(N) = N$$

with equality exactly when $\{a', b'\} = \{1, s-1\}$ — that is, when $a$ and $b$ are $d$ and $d(s-1) = N - d$.

So the optimal pairs are indexed by the divisors: each divisor $d$ of $N$ with $d < N$ gives the pair $(d,\, N-d)$, and $\gcd(d, N-d) = d$ confirms that $d$ is recovered from the pair, so distinct divisors give distinct pairs. Counting **ordered** pairs:

$$\text{answer} = 2 \cdot \#\{\,d \mid N : d < N/2\,\} + [\,N \text{ even}\,]$$

The second term is the self-symmetric pair $d = N/2$, where $a = b$ and the two orderings coincide — the detail that makes the answers odd for even $N$.

Enumerating divisors up to $\sqrt{N}$ handles $N \leq 10^9$ in about $3 \times 10^4$ steps.

For $N = 4$ the divisors below $2$ are just $\{1\}$, giving $(1,3)$ and $(3,1)$, plus the symmetric $(2,2)$ — three pairs, and indeed all three have $g = 4$. For $N = 105$ the seven divisors $1, 3, 5, 7, 15, 21, 35$ each give two orderings and $N$ is odd, so the answer is $14$.

## Solution (Python)

```python
import sys
from math import isqrt


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # Every divisor d < N/2 gives the pair (d, N - d) in two orders.
        small = 0
        for d in range(1, isqrt(n) + 1):
            if n % d:
                continue
            if 2 * d < n:
                small += 1
            other = n // d
            if other != d and 2 * other < n:
                small += 1
        out.append(str(2 * small + (n % 2 == 0)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\sqrt{N})$ per test case
- **Space:** $O(1)$
