# 867 &middot; Which Division

> CodeChef problem code [`WHICHDIV`](https://www.codechef.com/problems/WHICHDIV) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Ordered threshold ladder |
| **CodeChef tags** | `Algorithms`, `Implementation` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/conditionals-case-work/WHICHDIV.md](../docs/conditionals-case-work/WHICHDIV.md)

## Question

Given the rating $R$ of a person, tell which division he belongs to. The rating range for each division are given below:

- Division $1$: $2000 \le$ Rating.
- Division $2$: $1600 \le$ Rating $\lt 2000$.
- Division $3$: Rating $\lt 1600$.

**Input**

- The first line of the input contains $T$ - the number of test cases. Then the test cases follow.
- Each testcase contains a single line of input, which contains a single integer $R$.

**Output**

For each test case, output on a single line the answer: $1$ if the person belongs to Division $1$, $2$ if the person belongs to Division $2$, and $3$ if the person belongs to Division $3$.

## Constraints

- $1 \leq T \leq 1000$
- $1000 \leq R \leq 4500$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
1500
4000
1900
```

**Sample output**

```
3
1
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Since the rating of the person lies in the range $[1000, 1600)$, he belongs to Division $3$.

**Test case $2$:** Since the rating of the person lies in the range $[2000, 4500]$, he belongs to Division $1$.

**Test case $3$:** Since the rating of the person lies in the range $[1600, 2000)$, he belongs to Division $2$.

</details>

## Approach

Three bands, read off directly:

- Division 1: $R \geq 2000$
- Division 2: $1600 \leq R < 2000$
- Division 3: $R < 1600$

Testing them from the top down lets each branch assume the previous ones failed, so the upper bound of each band is implied and only the lower bound needs stating. That collapses the middle band's two-sided condition into a single comparison.

The boundaries are inclusive at the **bottom** of each division, which is the detail to get right: a rating of exactly $2000$ is Division 1, and exactly $1600$ is Division 2. Using strict `>` would misplace both.

The samples deliberately avoid the boundaries — $1500$, $4000$, $1900$ all sit comfortably inside their bands — so they will not catch an off-by-one here. Worth checking $1600$ and $2000$ by hand before submitting.

The constraint $1000 \leq R \leq 4500$ means no rating falls outside the three bands, so the final `else` is genuinely exhaustive and no error case is needed.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        r = int(data[1 + i])
        # Bands are inclusive at their lower edge; test from the top down.
        out.append("1" if r >= 2000 else "2" if r >= 1600 else "3")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
