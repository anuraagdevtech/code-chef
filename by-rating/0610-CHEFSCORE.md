# 610 &middot; Test Score

> CodeChef problem code [`CHEFSCORE`](https://www.codechef.com/problems/CHEFSCORE) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Divisibility with an upper bound |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/CHEFSCORE.md](../docs/number-theory/CHEFSCORE.md)

## Question

In a test, there are $N$ problems, each carrying $X$ marks.
In each problem, Chef either received $X$ marks or $0$ marks.

Determine whether is it possible for Chef to achieve **exactly** $Y$ marks.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three integers $N, X,$ and $Y$, the number of problems, the maximum score for each problem, and the score Chef wants.

**Output**

For each test case, output `YES` if Chef can achieve exactly $Y$ marks, `NO` otherwise.

You can print each character of the string in uppercase or lowercase. For example, the strings `Yes`, `YES`, `yes`, and `yEs`, are all considered identical.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10$
- $1 \leq X \leq 10$
- $0 \leq Y \leq 100$

## Sample

**Sample input**

```
5
1 8 4
3 6 12
4 5 0
10 10 100
8 5 36
```

**Sample output**

```
NO
YES
YES
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** There is no way for Chef to score exactly $4$ marks.

**Test case $2$:** Chef can score $12$ marks by receiving $6$ marks in $2$ problems and $0$ marks in $1$ problem.

**Test case $3$:** Chef can score $0$ marks by receiving $0$ marks in each of the $4$ problems.

**Test case $4$:** Chef can score $100$ marks by receiving $10$ marks in each of the $10$ problems.

**Test case $5$:** There is no way for Chef to score exactly $36$ marks.

</details>

## Approach

Every problem contributes either $X$ marks or $0$, so if Chef solved $k$ of them his score is exactly $kX$. The reachable scores are therefore the multiples of $X$ from $0$ up to $NX$, and $Y$ is achievable when **both** of these hold:

1. $Y$ is a multiple of $X$, that is $Y \bmod X = 0$;
2. the implied count $k = Y / X$ does not exceed the number of problems, that is $Y / X \leq N$.

Checking only divisibility is the natural half-answer and it is wrong, because a score can be a valid multiple yet demand more problems than exist. Equally, checking only $Y \leq NX$ is wrong, because a score below the maximum may still not be a multiple. Both conditions are needed.

Sample case 1 fails the first test ($Y = 4$ is not a multiple of $X = 8$) and sample case 5 fails it too ($36$ is not a multiple of $5$). Case 4 is the tight upper end: $100 / 10 = 10$ problems, exactly the $N$ available, so it is achievable.

The case $Y = 0$ deserves a glance. It satisfies $0 \bmod X = 0$ with $k = 0 \leq N$, so it is always achievable — Chef simply solves nothing. Case 3 confirms it. Since $X \geq 1$ the modulo never divides by zero.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, y = map(int, data[1 + 3 * i:4 + 3 * i])
        # Reachable scores are k * x for 0 <= k <= n: need both conditions.
        ok = y % x == 0 and y // x <= n
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
