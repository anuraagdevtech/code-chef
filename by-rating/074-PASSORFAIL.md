# 074. Pass or Fail

> [`PASSORFAIL`](https://www.codechef.com/problems/PASSORFAIL) &middot; difficulty **730** &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Scoring with a penalty |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Algorithms`, `Conditional Statements`, `Basic Math`, `Implementation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is struggling to pass a certain college course.

The test has a total of $N$ questions, each question carries $3$ marks for a correct answer and $-1$ for an incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got $X$ questions correct and the rest of them incorrect. For Chef to pass the course he must score at least $P$ marks.

Will Chef be able to pass the exam or not?

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three integers $N, X, P$.

**Output**

For each test case output `"PASS"` if Chef passes the exam and `"FAIL"` if Chef fails the exam.

You may print each character of the string in uppercase or lowercase (for example, the strings "pASs", "pass", "Pass" and "PASS" will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $0 \leq X \leq N$
- $0 \leq P \leq 3\cdot N$

## Sample

**Sample input**

```
3
5 2 3
5 2 4
4 0 0
```

**Sample output**

```
PASS
FAIL
FAIL
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef gets $2$ questions correct giving him $6$ marks and since he got $3$ questions incorrect so he faces a penalty of $-3$. So Chef's final score is $3$ and the passing marks are also $3$, so he passes the exam :)

**Test case $2$:** Chef's total marks are $3$ and since the passing marks are $4$, Chef fails the test :(

**Test case $3$:** Chef got all the problems wrong and thus his total score is $-4$. Since the passing marks are $0$, Chef fails the exam :(

</details>

## Approach

Chef attempts all $N$ questions, getting $X$ right and therefore $N - X$ wrong. Correct answers pay $3$ and wrong ones cost $1$, so the score is

$$3X - (N - X) = 4X - N$$

and he passes when that reaches $P$.

The simplification to $4X - N$ is worth seeing. Each question answered correctly rather than incorrectly is a swing of $4$ marks — the $3$ gained plus the $1$ penalty avoided — against a baseline of $-N$ if everything were wrong. That reframing makes the arithmetic a single expression and explains why the coefficient is $4$ rather than $3$.

The negative-marking is the trap. Ignoring the penalty and testing $3X \geq P$ passes sample case 1 by luck but fails case 2: with $N = 5, X = 2$ the real score is $8 - 5 = 3$, which falls short of $P = 4$, whereas $3X = 6$ would wrongly pass.

Sample case 3 shows the score going negative: $X = 0$ on $4$ questions gives $-4$, which fails even against $P = 0$. So no clamping at zero is appropriate — the comparison must be done on the signed score.

The bar is "**at least** $P$", so the comparison is `>=` and scoring exactly $P$ passes.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, p = map(int, data[1 + 3 * i:4 + 3 * i])
        # 3x - (n - x) = 4x - n; the score may legitimately go negative.
        out.append("PASS" if 4 * x - n >= p else "FAIL")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/PASSORFAIL.md](../docs/basic-math/PASSORFAIL.md)
