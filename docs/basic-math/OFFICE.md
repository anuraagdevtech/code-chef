# 5. Chef in his Office

> CodeChef problem code [`OFFICE`](https://www.codechef.com/problems/OFFICE) &middot; difficulty **532** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Direct formula |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Recently Chef joined a new company. In this company, the employees have to work for $X$ hours each day from Monday to Thursday. Also, in this company, Friday is called Chill Day — employees only have to work for $Y$ hours $(Y \lt X)$ on Friday. Saturdays and Sundays are holidays.

Determine the total number of working hours in one week.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the number of working hours on each day from Monday to Thursday and the number of working hours on Friday respectively.

**Output**

For each test case, output the total number of working hours in one week.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq X \leq 12$
- $1 \le Y \lt X$

## Sample

**Sample input**

```
3
10 5
12 2
8 7
```

**Sample output**

```
45
50
39
```

<details><summary>Explanation</summary>

**Test case $1$:** The total number of working hours in a week are: $10 \texttt{(Monday)} + 10 \texttt{(Tuesday)} + 10 \texttt{(Wednesday)} + 10 \texttt{(Thursday)} + 5 \texttt{(Friday)} = 45$

**Test Case 2:** The total number of working hours in a week are: $12 \texttt{(Monday)} + 12 \texttt{(Tuesday)} + 12 \texttt{(Wednesday)} + 12 \texttt{(Thursday)} + 2 \texttt{(Friday)} = 50$

**Test Case 3:** The total number of working hours in a week are: $8 \texttt{(Monday)} + 8 \texttt{(Tuesday)} + 8 \texttt{(Wednesday)} + 8 \texttt{(Thursday)} + 7 \texttt{(Friday)} = 39$

</details>

## Approach

The week splits into three kinds of day. Monday through Thursday is four days at $X$ hours each, Friday is a single day at $Y$ hours, and the weekend contributes nothing. Summing them gives the whole answer in one expression:

$$\text{total} = 4X + Y$$

There is no loop to write and no edge case to guard. The constraint $Y < X$ is flavour — it makes Friday genuinely the lighter day — but the formula never depends on it, so no validation is needed.

The thing worth internalising is the counting itself: "Monday to Thursday" is four days, not five. Off-by-one on an inclusive day range is the classic slip, and reading it as $5X + Y$ would pass no sample at all. Checking against the first one: $X=10, Y=5$ gives $4 \cdot 10 + 5 = 45$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Mon-Thu is four days at x hours, Friday is y, weekend is zero.
        out.append(str(4 * x + y))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
