# 176. A Subtask Problem

> CodeChef problem code [`SUBTASK`](https://www.codechef.com/problems/SUBTASK) &middot; difficulty **1217** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Ordered condition checks |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef recently solved his first problem on CodeChef. The problem he solved has $N$ test cases. He gets a score for his submission according to the following rules:

1) If Chef’s code passes all the $N$ test cases, he gets $100$ points.

2) If Chef’s code does not pass all the test cases, but passes all the **first** $M\;(M \lt N)$ test cases, he gets $K\;(K \lt 100)$ points.

3) If the conditions $1$ and $2$ are not satisfied, Chef does not get any points (i.e his score remains at $0$ points).

You are given a binary array $A_1, A_2, \dots, A_N$ of length $N$, where $A_i = 1$ denotes Chef's code passed the $i^{th}$ test case, $A_i = 0$ denotes otherwise. You are also given the two integers $M, K$. Can you find how many points does Chef get?

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case contains three space-separated integers $N, M, K$.
- The second line contains $N$ space-separated integer $A_1, A_2,\dots, A_N$.

**Output**

For each testcase, output in a single line the score of Chef.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 100$
- $1 \leq M \lt N$
- $1 \leq K \lt 100$
- $0 \leq A_i \leq 1$

## Sample

**Sample input**

```
4
4 2 50
1 0 1 1
3 2 50
1 1 0
4 2 50
1 1 1 1
5 3 30
1 1 0 1 1
```

**Sample output**

```
0
50
100
0
```

<details><summary>Explanation</summary>

**Test case $1$**: Chef's code neither passes all $4$ test cases nor passes the first $2$ test cases. Hence he does not get any points.

**Test case $2$**: Chef's code does not pass all $3$ test cases, but passes the first $2$ test cases. Hence he gets $50$ points.

**Test case $3$**: Chef's code passes all the $4$ test cases. Hence he gets $100$ points.

</details>

## Approach

Three rules, and the **order** in which they are tested is what makes the solution correct:

1. All $N$ tests pass → $100$.
2. Otherwise, all of the first $M$ pass → $K$.
3. Otherwise → $0$.

Rule 2 carries the qualifier $M < N$, so a submission passing everything scores $100$, never $K$. Checking the prefix first would wrongly award $K$ to a perfect submission — sample case 3 is there to catch exactly that, with all four tests passing and the answer $100$.

In Python each check is a single `all(...)` over a slice, which short-circuits on the first failure:

- `all(v == 1 for v in a)` for the full set
- `all(v == 1 for v in a[:m])` for the prefix

Sample case 2 is the partial-credit case: the first two pass and the third fails, scoring $K = 50$.

Sample case 4 is the one that punishes a loose reading. Four of five tests pass — more than in case 2 — yet the score is $0$, because the failure sits at position $3$, *inside* the first $M = 3$. Partial credit depends on an unbroken **prefix**, not on a count of passes. A solution comparing the number of passes against $M$ would wrongly award $30$ here.

The constraint $M < N$ guarantees the two rules never collide, so there is no ambiguity about which applies.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        a = data[pos + 3:pos + 3 + n]
        pos += 3 + n
        # Full pass must be checked first, or a perfect run scores only k.
        if all(v == b"1" for v in a):
            out.append("100")
        elif all(v == b"1" for v in a[:m]):
            out.append(str(k))
        else:
            out.append("0")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
