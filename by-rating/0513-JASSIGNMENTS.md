# 513 &middot; Janmansh and Assignments

> CodeChef problem code [`JASSIGNMENTS`](https://www.codechef.com/problems/JASSIGNMENTS) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Conditional arithmetic |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Arithmetic` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/JASSIGNMENTS.md](../docs/basic-math/JASSIGNMENTS.md)

## Question

Janmansh has to submit $3$ assignments for Chingari before $10$ pm and he starts to do the assignments at $X$ pm. Each assignment takes him $1$ hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?

**Input**

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer $X$ - the time when Janmansh starts doing the assignments.

**Output**

For each test case, output `Yes` if he can complete the assignments on time. Otherwise, output `No`.

You may print each character of `Yes` and `No` in uppercase or lowercase (for example, `yes`, `yEs`, `YES` will be considered identical).

## Constraints

- $1 \le T \le 10$
- $1 \le X \le 9$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
2
7
9
```

**Sample output**

```
Yes
No
```

<details><summary>Explanation</summary>

**Test case-1:** He can start at $7$pm and finish by $10$ pm. Therefore he can complete the assignments.

**Test case-2:** He can not complete all the $3$ assignments if he starts at $9$ pm.

</details>

## Approach

Janmansh starts at $X$ pm and each of the $3$ assignments costs exactly one hour, so he finishes at hour $X + 3$. He is on time when that finishing moment is no later than the $10$ pm deadline:

$$X + 3 \leq 10 \quad\Longleftrightarrow\quad X \leq 7$$

So the whole problem collapses to a single comparison. The constraint $1 \le X \le 9$ keeps everything inside one afternoon, so there is no wrap-around past midnight to worry about and no need to convert to a 24-hour clock.

The boundary is the only place to slip. At $X = 7$ he finishes exactly at $10$ pm, and "before 10 pm" in the sense used here is satisfied — the sample confirms it, since $X = 7$ answers `Yes` while $X = 9$ (finishing at midnight) answers `No`. That makes the comparison `<=`, not `<`.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Starts at x, needs 3 hours, must land no later than 10.
        out.append("Yes" if x + 3 <= 10 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
