# 016. Water Filling

> [`WATERFILLING`](https://www.codechef.com/problems/WATERFILLING) &middot; difficulty **541** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Counting flags instead of enumerating cases |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, she will wait, and not fill them up now.

You are given three integers - $B_1, B_2,$ and $B_3$. \
If $B_1 = 1$, it means that the first bottle is full. \
If $B_1 = 0$, it means that the first bottle is empty. \
Similarly, $B_2$ denotes whether the second bottle is full or empty, and $B_3$ denotes it for the third bottle.

Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now".

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains three space-separated integers, $B_1, B_2, B_3$.

**Output**

For each test case, output on a new line, either "Water filling time", or "Not now".

## Constraints

- $1 \leq T \leq 1000$
- $B_i$ is either $0$ or $1$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
5
0 0 0
1 1 1
1 1 0
0 1 0
0 1 1
```

**Sample output**

```
Water filling time
Not now
Not now
Water filling time
Not now
```

<details><summary>Explanation</summary>

**Testcase 1:** The inputs are $0, 0, 0$. So all three bottles are empty. Since at least two bottles are empty, it is "Water filling time".

**Testcase 2:** The inputs are $1, 1, 1$. So all three bottles are full. Since it is not the case that at least two bottles are empty, it is "Not now".

**Testcase 3:** The inputs are $1, 1, 0$. So only one bottle is empty. Since it is not the case that at least two bottles are empty, it is "Not now".

**Testcase 4:** The inputs are $0, 1, 0$. So two bottles are empty. Since at least two bottles are empty, it is "Water filling time".

**Testcase 5:** The inputs are $0, 1, 1$. So only one bottle is empty. Since it is not the case that at least two bottles are empty, it is "Not now".

</details>

## Approach

Chef refills when **at least two** of the three bottles are empty. Each $B_i$ is $1$ for full and $0$ for empty, so an empty bottle is a zero.

The naive route is to enumerate the eight possible triples, or to write a chain of `or`s covering each pair that could be empty. Both work but scale badly and are easy to get wrong. The cleaner framing: count the empties and compare against the threshold.

Because the values are exactly $0$ and $1$, the number of *full* bottles is just $B_1 + B_2 + B_3$, so the number of empty ones is $3 - (B_1 + B_2 + B_3)$. The refill condition "at least two empty" becomes

$$3 - (B_1 + B_2 + B_3) \geq 2 \quad\Longleftrightarrow\quad B_1 + B_2 + B_3 \leq 1$$

In words: Chef fills up exactly when **at most one** bottle is full — which is just the problem's own second sentence read from the other side. Encoding a 0/1 flag array as a sum is a trick worth keeping; it turns case analysis into arithmetic.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        full = sum(map(int, data[1 + 3 * i:4 + 3 * i]))
        # At least two empty  <=>  at most one full.
        out.append("Water filling time" if full <= 1 else "Not now")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **All three empty** ($0\,0\,0$): zero full tanks, so filling time.
- **All three full** ($1\,1\,1$): three full, so not now.
- **Exactly one full** ($0\,1\,0$): two tanks are empty, which meets the "at least two" requirement — filling time. This is the boundary.
- **Exactly two full** ($1\,1\,0$): only one empty, so not now — the other side of the same boundary.
- Summing the three flags collapses all eight patterns into one comparison, so there is no case list to get wrong; "at least two empty" is simply "at most one full".

## Dry run

| $B_1$ | $B_2$ | $B_3$ | full tanks | $\leq 1$? | output |
|---:|---:|---:|---:|:---:|---|
| 0 | 0 | 0 | 0 | yes | `Water filling time` |
| 1 | 1 | 1 | 3 | no | `Not now` |
| 1 | 1 | 0 | 2 | no | `Not now` |
| 0 | 1 | 0 | 1 | yes | `Water filling time` |
| 0 | 1 | 1 | 2 | no | `Not now` |

Rows 4 and 3 sit either side of the threshold: one full tank passes, two do not.

---

Same problem grouped by topic: [../docs/conditionals-case-work/WATERFILLING.md](../docs/conditionals-case-work/WATERFILLING.md)
