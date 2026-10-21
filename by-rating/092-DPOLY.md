# 092. Degree of Polynomial

> [`DPOLY`](https://www.codechef.com/problems/DPOLY) &middot; difficulty **793** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Last index satisfying a predicate |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Basic Math`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

In mathematics, the [degree](https://en.wikipedia.org/wiki/Degree_of_a_polynomial) of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable $x$ with $N$ terms. The polynomial looks like $A_0\cdot x^0 + A_1\cdot x^1 + \ldots + A_{N-2}\cdot x^{N-2} + A_{N-1}\cdot x^{N-1}$ where $A_{i-1}$ denotes the coefficient of the $i^{th}$ term $x^{i-1}$ for all $(1\le i\le N)$.

Find the degree of the polynomial.

**Note:** It is guaranteed that there exists **at least** one term with non-zero coefficient.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains of a single integer $N$ - the number of terms in the polynomial.
- Second line of each test case contains of $N$ space-separated integers - the $i^{th}$ integer $A_{i-1}$ corresponds to the coefficient of $x^{i-1}$.

**Output**

For each test case, output in a single line, the degree of the polynomial.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $-1000 \le A_i \le 1000$
- $A_i \ne 0$ for at least one $(0\le i \lt N)$.

## Sample

**Sample input**

```
4
1
5
2
-3 3
3
0 0 5
4
1 2 4 0
```

**Sample output**

```
0
1
2
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one term $x^0$ with coefficient $5$. Thus, we are given a constant polynomial and the degree is $0$.

**Test case $2$:** The polynomial is $-3\cdot x^0 + 3\cdot x^1 = -3 + 3\cdot x$. Thus, the highest power of $x$ with non-zero coefficient is $1$.

**Test case $3$:** The polynomial is $0\cdot x^0 + 0\cdot x^1 + 5\cdot x^2= 0+0 + 5\cdot x^2$. Thus, the highest power of $x$ with non-zero coefficient is $2$.

**Test case $4$:** The polynomial is $1\cdot x^0 + 2\cdot x^1+ 4\cdot x^2 + 0\cdot x^3= 1 + 2\cdot x + 4\cdot x^2$. Thus, the highest power of $x$ with non-zero coefficient is $2$.

</details>

## Approach

Coefficient $A_i$ belongs to the term $x^i$, so the array index *is* the exponent. The degree is the highest power with a non-zero coefficient, which makes this a scan for the **last non-zero entry** and a report of its index.

Scanning from the right and stopping at the first non-zero is the natural phrasing and exits early. Scanning left to right while remembering the most recent non-zero index works equally well and is what the code below does, since it reads cleanly and still costs one pass.

Three things make this less trivial than it looks.

**Trailing zeros are not part of the polynomial.** Sample case 4 is $1 + 2x + 4x^2 + 0x^3$, whose degree is $2$, not $3$. Taking $N - 1$ as the answer ignores the actual coefficients and fails exactly here.

**Leading zeros are fine.** Sample case 3 is $0 + 0x + 5x^2$, degree $2$ — zeros below the top term are irrelevant, so the scan must look at the highest non-zero index rather than the first.

**Coefficients may be negative.** The test is `!= 0`, not `> 0`. Sample case 2 has $A_0 = -3$, and a truthiness-style check for "positive" would mishandle such terms in general.

The guarantee that at least one coefficient is non-zero means the scan always finds something, so the zero polynomial — whose degree is conventionally undefined or $-\infty$ — never arises. Sample case 1 is the constant polynomial $5$, of degree $0$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        coeffs = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        degree = 0
        for i, a in enumerate(coeffs):
            # The index is the exponent; negative coefficients still count.
            if int(a) != 0:
                degree = i
        out.append(str(degree))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/DPOLY.md](../docs/arrays/DPOLY.md)
