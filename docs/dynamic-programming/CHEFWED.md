# 360. Chef and Wedding Arrangements

> CodeChef problem code [`CHEFWED`](https://www.codechef.com/problems/CHEFWED) &middot; difficulty **1841** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Partition DP with an incrementally maintained segment cost |
| **Time** | $O(N^2)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

There are $N$ guests (numbered $1$ through $N$) coming to Chef's wedding. Each guest is part of a family; for each valid $i$, the $i$-th guest is part of family $F_i$. You need to help Chef find an optimal seating arrangement.

Chef may buy a number of tables, which are large enough for any number of guests, but the people sitting at each table must have consecutive numbers ― for any two guests $i$ and $j$ ($i \lt j$) sitting at the same table, guests $i+1, i+2, \ldots, j-1$ must also sit at that table. Chef would have liked to seat all guests at a single table; however, he noticed that two guests $i$ and $j$ are likely to get into an argument if $F_i = F_j$ and they are sitting at the same table.

Each table costs $K$ rupees. Chef defines the *inefficiency* of a seating arrangement as the total cost of tables plus the number of guests who are likely to get into an argument with another guest. Tell Chef the minimum possible inefficiency which he can achieve.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $F_1, F_2, \ldots, F_N$.

### Output
For each test case, print a single line containing one integer ― the smallest possible inefficiency.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le K \le 1,000$
- $1 \le F_i \le 100$ for each valid $i$
- The sum of $N$ across test cases is $\leq 5,000$
### Subtasks
- **Subtask #1 (20 points):** $K = 1$
- **Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le K \le 1,000$
- $1 \le F_i \le 100$ for each valid $i$
- The sum of $N$ across test cases is $\leq 5,000$

## Sample

**Sample input**

```
3
5 1
5 1 3 3 3
5 14
1 4 2 4 4
5 2
3 5 4 5 1
```

**Sample output**

```
3
17
4
```

<details><summary>Explanation</summary>

**Example case 1:** The optimal solution is to use three tables with groups of guests $[1, 2, 3]$, $[4]$ and $[5]$. None of the tables have any guests that are likely to get into an argument, so the inefficiency is $3 \cdot K = 3$.

**Example case 2:** The optimal solution is to seat all guests at one table. Then, guests $2$, $4$ and $5$ are likely to get into an argument with each other, so the inefficiency is $K + 3 = 17$.

</details>

## Approach

A table seats a **contiguous** block of guests, so a seating plan is nothing more than a partition of $1 \ldots N$ into consecutive segments. That makes this the classic one-dimensional partition DP:

$$\mathrm{dp}[j] = \min_{0 \leq i < j} \bigl(\mathrm{dp}[i] + K + \mathrm{cost}(i+1, j)\bigr)$$

where $\mathrm{dp}[j]$ is the least inefficiency for the first $j$ guests and $\mathrm{cost}(l, r)$ counts the guests in that segment whose family also has another member there. Note what is counted: **guests**, not pairs. A family of three at one table contributes $3$, not $\binom{3}{2} = 3$ — the two coincide at three but diverge elsewhere, and a family of four contributes $4$, not $6$.

Evaluating $\mathrm{cost}$ for every pair of endpoints would be cubic. Instead fix the left end $i+1$ and extend $j$ rightwards, maintaining a family tally. When a family's count rises to $2$, **two** guests become arguers (the newcomer and the one already seated), so add $2$; on every count beyond that add $1$. That makes each cost update $O(1)$ and the whole DP $O(N^2)$, comfortable with $\sum N \leq 5000$.

$$\Delta\mathrm{cost} = \begin{cases} 2 & \text{count becomes } 2 \\ 1 & \text{count becomes } \geq 3 \\ 0 & \text{count becomes } 1\end{cases}$$

The trade-off is genuinely two-sided, as the samples show. With $K = 1$ and families `5 1 3 3 3`, splitting the three identical guests apart costs three tables but zero arguments, for $3$ — cheaper than one table at $1 + 3 = 4$. With $K = 14$ and `1 4 2 4 4`, tables are far too expensive, so everyone shares one at $14 + 3 = 17$. And with $K = 2$ and `3 5 4 5 1`, both plans tie at $4$: one table paying $2 + 2$, or two tables separating the pair of $5$s and paying $4 + 0$.

## Solution (Python)

```python
import sys

FAMILIES = 101


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        fam = [int(x) for x in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        dp = [0] + [None] * n
        for i in range(n):
            base = dp[i]
            seen = [0] * FAMILIES
            cost = 0
            for j in range(i, n):
                seen[fam[j]] += 1
                c = seen[fam[j]]
                # The second member makes *two* guests arguers at once.
                if c == 2:
                    cost += 2
                elif c > 2:
                    cost += 1
                total = base + k + cost
                if dp[j + 1] is None or total < dp[j + 1]:
                    dp[j + 1] = total
        out.append(str(dp[n]))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N^2)$ per test case
- **Space:** $O(N)$
