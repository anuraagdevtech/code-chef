# 449. Eugene and function

> [`KFUNC`](https://www.codechef.com/problems/KFUNC) &middot; difficulty **1746** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Digital roots are periodic along an arithmetic progression |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Constructive`, `Basic Math`, `ad-hoc` |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log R)$ per test case |
| **Space** | $O(1)$ |

## Question

Eugene loves sequences, especially [arithmetic progressions](https://en.wikipedia.org/wiki/Arithmetic_progression). One day he was asked to solve a difficult problem.

If a sequence of numbers **A_1**, **A_2**, ... , **A_N** form an arithmetic progression **A**, he was asked to calculate sum of **F(A_i)**, for **L** ≤ **i** ≤ **R**.

**F(X)** is defined as:

If **X** < 10 then **F(X)** = **X**.

Else **F(X)** = **F(**sum_of_digits**(X))**.

Example:

**F(**1378**)** =
**F(**1+3+7+8**)** =
**F(**19**)** =
**F(**1 + 9**)** =
**F(**10**)** =
**F(**1+0**)** =
**F(**1**)** = 1

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases.

- Each test case is described in one line containing four integers: **A_1** denoting the first element of the arithmetic progression **A**, **D** denoting the common difference between successive members of **A**, and **L** and **R** as described in the problem statement.

**Output**

- For each test case, output a single line containing one integer denoting sum of **F(A_i)**.

**Constraints**

- **1** ≤ **T** ≤ **10^5**

- **1** ≤ **A_1** ≤ **10^9**

- **0** ≤ **D** ≤ **10**^9

- **1** ≤ **R** ≤ **10^18**

- **1** ≤ **L** ≤ **R**

**Subtasks**

- **Subtask 1:**  0 ≤ **D** ≤ 100, 1 ≤ **A_1** ≤ 10^9, 1 ≤ R ≤ 100  - **15 points**

- **Subtask 2:**  0 ≤ **D** ≤ 10^9, 1 ≤ **A_1** ≤ 10^9, 1 ≤ R ≤ 10^6  - **25 points**

- **Subtask 3:** Original constraints -** 60 points**

## Constraints

- 1 ≤ T ≤ 10^5
- 1 ≤ A_1 ≤ 10^9
- 0 ≤ D ≤ 10^9
- 1 ≤ R ≤ 10^18
- 1 ≤ L ≤ R

## Sample

**Sample input**

```
2
1 1 1 3
14 7 2 4
```

**Sample output**

```
6
12
```

<details><summary>Explanation</summary>

**Example case 1.**

**A** = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...}

**A_1** = 1

**A_2** = 2

**A_3** = 3

**F(A_1)** = 1

**F(A_2)** = 2

**F(A_3)** = 3

**1+2+3=6**

**Example case 2.**

**A** = {14, 21, 28, 35, 42, 49, 56, 63, 70, 77,  ...}

**A_2** = 21

**A_3** = 28

**A_4** = 35

**F(A_2)** = 3

**F(A_3)** = 1

**F(A_4)** = 8

**3+1+8=12**

</details>

## Approach

$F$ is the **digital root**, and since a number is congruent to its digit sum modulo $9$,

$$F(X) = \begin{cases} 9 & X \equiv 0 \pmod 9 \\ X \bmod 9 & \text{otherwise}\end{cases}$$

for $X \geq 1$. So $F(A_i)$ depends only on $A_i \bmod 9$, and along the progression $A_i = A_1 + (i-1)D$ that residue steps by $D \bmod 9$ each time — a cyclic walk on $\mathbb{Z}_9$ with period

$$p = \frac{9}{\gcd(D \bmod 9,\ 9)}$$

(or $1$ when $D \equiv 0$). So the summands repeat with period at most $9$, and the sum over $[L, R]$ is

$$\left\lfloor \frac{n}{p} \right\rfloor \cdot \bigl(\text{one period's sum}\bigr) + \bigl(\text{first } n \bmod p \text{ terms}\bigr), \qquad n = R - L + 1$$

with the walk started at $(A_1 + (L-1)D) \bmod 9$.

That starting residue must be computed **modulo 9**, because $(L-1)D$ reaches $10^{27}$ — far past 64-bit range in C++, and merely wasteful in Python. Likewise $n$ reaches $10^{18}$, so the periodic collapse is the whole point: the loop runs at most nine times regardless.

The samples check both ends. $A_1 = 1, D = 1$ over $i \in [1,3]$ gives $F = 1, 2, 3$ and a sum of $6$. And $A_1 = 14, D = 7$ over $i \in [2,4]$ gives the terms $21, 28, 35$ with digital roots $3, 1, 8$, summing to $12$ — the period here is $9$, so all three fall inside one cycle.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a1, d = int(data[1 + 4 * i]), int(data[2 + 4 * i])
        l, r = int(data[3 + 4 * i]), int(data[4 + 4 * i])
        step = d % 9
        # Reduce first: (L - 1) * D would otherwise reach 10^27.
        start = (a1 + (l - 1) % 9 * step) % 9
        period = 9 // gcd(step, 9) if step else 1
        roots = []
        cur = start
        for _ in range(period):
            roots.append(cur if cur else 9)
            cur = (cur + step) % 9
        n = r - l + 1
        total = n // period * sum(roots) + sum(roots[:n % period])
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/number-theory/KFUNC.md](../docs/number-theory/KFUNC.md)
