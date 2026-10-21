# 305. College Life 2

> [`COLGLF2`](https://www.codechef.com/problems/COLGLF2) &middot; difficulty **1519** &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Group total with a per-group adjustment |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(\sum E_i)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has just started watching Game of Thrones, and he wants to first calculate the exact time (in minutes) that it'll take him to complete the series.

The series has $S$ seasons, and the $i^{th}$ season has $E_i$ episodes, each of which are $L_{i,1}, L_{i,2}, \ldots, L_{i,E_i}$ minutes long. Note that these $L_{i,j}$ include the duration of the beginning intro song in each episode. The streaming service that he uses, allows Chef to skip the intro song. The intro song changes slightly each season, and so he wants to watch the intro song in the first episode of each season, but he'll skip it in all other episodes of that season (yes, we know, a sacrilege!). You know that the intro song lasts for $Q_i$ minutes in the $i^{th}$ season.

Find the total time in minutes, that he has to watch.

**Input:**
- First line will contain a single integer, $T$, denoting the number of testcases. Then the testcases follow.
- The first line of each testcase will contain a single integer $S$, denoting the total number of seasons.
- The second line contains $S$ space separated integers, $Q_1, Q_2, \ldots, Q_S$, where $Q_i$ denotes the duration of the intro song in the $i^{th}$ season.
- The $i^{th}$ of the next $S$ lines contains $E_i + 1$ space separated integers, where the first integer is $E_i$, denoting the number of episodes in the $i^{th}$ season. That is followed by the duration of each of the $E_i$ episodes, $L_{i,1}, L_{i,2}, \ldots, L_{i,E_i}$.

**Output:**
For each testcase, output the answer in a single line.

**Constraints**
- $1 \leq T \leq 5$
- $1 \leq S \leq 10^5$
- $2 \leq L_{i,j} \leq 10^5$
- $1 \leq E_i$
- Sum of all $E_i$ in a single testcase is at most $10^5$
- $1 \leq Q_i \lt L_{i,j}$, for all valid $j$.

## Constraints

- $1 \leq T \leq 5$
- $1 \leq S \leq 10^5$
- $2 \leq L_{i,j} \leq 10^5$
- $1 \leq E_i$
- Sum of all $E_i$ in a single testcase is at most $10^5$
- $1 \leq Q_i \lt L_{i,j}$, for all valid $j$.

## Sample

**Sample 1 input**

```
1
2
1 2
1 2
2 3 4
```

**Sample 1 output**

```
7
```

<details><summary>Explanation</summary>

**1** in the beginning denotes there is only $1$ test case.

**Testcase 1:**

There are $2$ seasons. The intro song in each of the first season episodes lasts for $1$ minute, and the intro song in the second season episodes lasts for $2$ minutes each.

For the first season, since there is only $1$ episode, Chef will be watching it completely - $2$ minutes.

For the second season, Chef will be watching the first episode completely ($3$ minutes) and will skip the intro song of the second episode ($4 - 2 = 2$ minutes).

So, the total time spent is $2 + (3 + (4 - 2)) = 7$ minutes.

</details>

**Sample 2 input**

```
2
1
10
5 11 11 11 11 11
5
10 10 10 10 10
1 11
1 11
1 11
1 11
1 11
```

**Sample 2 output**

```
15
55
```

<details><summary>Explanation</summary>

**2** in the beginning denotes there are $2$ test cases.

**Testcase 1:**

There is only $1$ season having intro song for $10$ minutes.

Chef will have to watch the entire first episode including the intro song and will be skipping the same in further seasons.

So, the total time spent is $(11 + (11 - 10) * 4) = 15$ minutes.

**Testcase 2:**

There are total $5$ seasons. The intro song in every season lasts for $10$ minutes.

For each of the five seasons, since there is only $1$ episode, Chef will be watching all of them completely - $11$ minutes each.

So, the total time spent is $11 * 5 = 55$ minutes.

</details>

## Approach

Each episode length $L_{i,j}$ already includes the intro. Chef watches the intro only in the **first** episode of each season, skipping it in the other $E_i - 1$. So for season $i$ he saves $Q_i$ minutes $E_i - 1$ times:

$$\text{total} = \sum_i \left( \sum_j L_{i,j} \;-\; Q_i \cdot (E_i - 1) \right)$$

The $E_i - 1$ is the crux. Subtracting $Q_i \cdot E_i$ would strip the intro from the first episode too, which Chef does watch; subtracting nothing ignores the skipping entirely. It is the same *n items, n−1 gaps* shape as the gaming-breaks and tournament problems — here, the first episode of each season is the one that does not get the adjustment.

A season with a single episode saves nothing, since $E_i - 1 = 0$. Sample season 1 is exactly that, contributing its full $2$ minutes. Season 2 sums to $3 + 4 = 7$ and saves one intro of $2$, giving $5$, for a total of $7$.

The input layout is the other hazard: the intro durations arrive on **one line for all seasons**, before any episode data, and each season's line then begins with its own $E_i$ before the lengths. Reading the whole stream as flat tokens and advancing a cursor by $E_i + 1$ per season handles the ragged rows cleanly.

The guarantee $Q_i < L_{i,j}$ means no episode is shorter than its intro, so the per-episode contribution never goes negative.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        s = int(data[pos])
        q = [int(v) for v in data[pos + 1:pos + 1 + s]]
        pos += 1 + s
        total = 0
        for i in range(s):
            e = int(data[pos])
            total += sum(int(v) for v in data[pos + 1:pos + 1 + e])
            # The intro is watched once per season, skipped e - 1 times.
            total -= q[i] * (e - 1)
            pos += 1 + e
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/COLGLF2.md](../docs/arrays/COLGLF2.md)
