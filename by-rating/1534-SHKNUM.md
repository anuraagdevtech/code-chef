# 1534 &middot; Sheokand and Number

> CodeChef problem code [`SHKNUM`](https://www.codechef.com/problems/SHKNUM) &middot; time limit **1.5s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Precomputed candidate set with a bisect |
| **CodeChef category** | main |
| **Time** | $O(\log C)$ per test case after an $O(C \log C)$ precomputation |
| **Space** | $O(C)$ |

Same write-up grouped by topic: [../docs/binary-search/SHKNUM.md](../docs/binary-search/SHKNUM.md)

## Question

Sheokand is good at mathematics. One day, to test his math skills, Kaali gave him an integer $N$. To impress Kaali, Sheokand has to convert $N$ into an integer $M$ that can be represented in the form $2^x + 2^y$ (where $x$ and $y$ are non-negative integers such that $x \neq y$). In order to do that, he can perform two types of operations:
- add $1$ to $N$
- subtract $1$ from $N$

However, Sheokand is preparing for his exams. Can you help him find the minimum number of operations required to convert $N$ into a valid integer $M$?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each testcase contains a single integer $N$.

### Output
For each test case, print a single line containing one integer — the minimum required number of operations.

### Constraints
- $1 \le T \le 100,000$
- $1 \le N \le 10^9$

### Subtasks
**Subtask #1 (30 points):** $1 \le T \le 1,000$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 100,000$
- $1 \le N \le 10^9$

## Sample

**Sample input**

```
3
10
22
4
```

**Sample output**

```
0
2
1
```

<details><summary>Explanation</summary>

**Example case 1:** $N=10$ is already in the form $2^x + 2^y$, with $x=3$ and $y=1$.

**Example case 2:** $N=22$ can be converted into $M=20=2^2+2^4$ or $M=24=2^3+2^4$ in two operations.

**Example case 3:** $N=4$ can be converted into $M=3=2^0+2^1$ or $M=5=2^0+2^2$ in one operation.

</details>

## Approach

The targets $M = 2^x + 2^y$ with $x \neq y$ are numbers with **exactly two set bits**, and there are very few of them below the bound: $N \leq 10^9 < 2^{30}$, so taking $x < y \leq 31$ covers every target that could be nearest, giving only $\binom{32}{2} = 496$ candidates.

Since the cost is $|N - M|$, the answer is the distance to the nearest candidate. With the candidates sorted once, each query is a binary search plus a comparison of the two neighbours:

$$\text{answer} = \min_{M \in \mathcal{C}} |N - M|$$

Both neighbours must be checked — the nearest candidate can lie on either side, and for $N = 22$ it is a tie: $20 = 16+4$ below and $24 = 16+8$ above, each $2$ away. The upper neighbour must exist, which is why the candidate list is generated past $10^9$ (up to $2^{31} + 2^{30}$) rather than stopping at it.

Generating candidates and bisecting is what makes $T = 10^5$ trivial; scanning all 496 per query would also pass, but the bisect makes the per-query cost logarithmic.

The samples show the three shapes. $N = 10 = 8 + 2$ is already a target, so $0$. $N = 4$ needs $1$ — note $4 = 2^2$ has a single set bit, so a *power of two* is never a target, and its nearest neighbours are $3 = 1+2$ and $5 = 1+4$. And $22 = 10110_2$ has three set bits, needing $2$.

## Solution (Python)

```python
import sys
from bisect import bisect_left


def main() -> None:
    # Numbers with exactly two set bits; 32 bits is past the 10^9 bound.
    targets = sorted((1 << x) + (1 << y) for y in range(32) for x in range(y))
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        i = bisect_left(targets, n)
        best = targets[i] - n
        if i:                                 # the lower neighbour may be nearer
            best = min(best, n - targets[i - 1])
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log C)$ per test case after an $O(C \log C)$ precomputation
- **Space:** $O(C)$
