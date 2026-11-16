[&larr; 578. MasterChef](578-MCHEF.md) &middot; [Index](README.md) &middot; [580. Little Elephant and Median &rarr;](580-MEDIAN.md)

# 579. Prime Factor Division

> [`PRIMEFACDIV`](https://www.codechef.com/problems/PRIMEFACDIV) &middot; difficulty **2016** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Strip common factors with repeated gcd |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation`, `Divisors`, `GCD`, `Prime Divisors` |
| **Complexity class** | Polylogarithmic $O(\log^2 n)$ |
| **Time** | $O(\log^2 B)$ per test case |
| **Space** | $O(1)$ |

## Question

*Mario has reached Bowser's Castle and is inches away from rescuing Princess Peach. He has to answer the following problem at the gate to be allowed to enter. Can you help him?*

Let $S(M)$ denote the set of all [prime](https://en.wikipedia.org/wiki/Prime_number) [factors](https://en.wikipedia.org/wiki/Divisor) of $M$.
Given two positive integers $A$ and $B$, determine whether $A$ is divisible by all elements in $S(B)$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, $A$ and $B$, as mentioned in the statement.

**Output**

For each test case, print `YES` if $A$ is divisible by all elements in $S(B)$ and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B \leq 10^{18}$

## Sample

**Sample input**

```
3
21 63
72 72
25 20
```

**Sample output**

```
YES
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** The set of all prime factors of $B = 63$ is given by $S(B) = \{3, 7\}$. Also, $A = 21$ is divisible by all elements in $S(B)$.

**Test case $2$:** The set of all prime factors of $B = 72$ is given by $S(B) = \{2, 3\}$. Also, $A = 72$ is divisible by all elements in $S(B)$.

**Test case $3$:** The set of all prime factors of $B = 20$ is given by $S(B) = \{2, 5\}$. Here, $A = 25$ is not divisible by $2$ in $S(B)$.

</details>

## Approach

Numbers up to $10^{18}$ cannot be factorised in time, but factorisation is not needed. The question is whether every prime of $B$ also divides $A$.

Let $g = \gcd(A, B)$. If $g = 1$ and $B > 1$, then $B$ has a prime that $A$ lacks: answer NO. Otherwise divide $B$ by $g$ and repeat - $g$ contains only primes of $A$, so dividing by it never removes a prime that $A$ lacks, and each division at least halves $B$. If $B$ reaches 1, all of its primes were shared: answer YES.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        a = next(tokens)
        b = next(tokens)
        while b > 1:
            common = gcd(a, b)
            if common == 1:
                break
            b //= common
        out.append('YES' if b == 1 else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $B = 1$ has no prime factors, so the answer is YES for any $A$.
- High powers in $B$ (for example $A = 2$, $B = 2^{60}$) need several rounds, which is why it is a loop and not a single gcd.
- $A = 1$ gives YES only when $B = 1$.
- Python integers handle $10^{18}$ exactly.

## Dry run

- `A = 21, B = 63`: gcd 21, $B \to 3$; gcd(21, 3) = 3, $B \to 1$. YES.
- `A = 25, B = 20`: gcd 5, $B \to 4$; gcd(25, 4) = 1 with $B > 1$. NO - the prime 2 is missing from 25.

---

Same problem grouped by topic: [../docs/number-theory/PRIMEFACDIV.md](../docs/number-theory/PRIMEFACDIV.md)
