# 1419 &middot; Mix the Colors

> CodeChef problem code [`MIXCOLOR`](https://www.codechef.com/problems/MIXCOLOR) &middot; time limit **2s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting duplicates |
| **CodeChef category** | main |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/arrays/MIXCOLOR.md](../docs/arrays/MIXCOLOR.md)

## Question

Chef likes to mix colors a lot. Recently, she was gifted **N** colors **A_1, A_2, ..., A_N** by her friend.

Chef wants to make the values of all her colors pairwise distinct, as they will then look stunningly *beautiful*. In order to achieve that, she can perform the following mixing operation zero or more times:

- Choose any two colors. Let's denote their values by **x** and **y**.

- Mix the color with value **x** into the color with value **y**. After the mixing, the value of the first color remains **x**, but the value of the second color changes to **x + y**.

Find the minimum number of mixing operations Chef needs to perform to make her colors beautiful.

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **N** denoting the number of colors.

- The second line contains **N** space-separated integers **A_1, A_2, ..., A_N** denoting Chef's initial colors.

**Output**

For each test case, print a single line containing one integer — the minimum number of required mixing operations.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 10^5

- 1 ≤ **A_i** ≤ 10^9 for each valid **i**

**Subtasks**

**Subtask #1 (30 points):** 1 ≤ **N** ≤ 100

**Subtask #2 (70 points):** original constraints

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- 1 ≤ A_i ≤ 10^9 for each valid i

## Sample

**Sample input**

```
2
3
1 2 3
3
2 1 2
```

**Sample output**

```
0
1
```

<details><summary>Explanation</summary>

**Example case 1:** No two colors have the same value. Hence, they are already beautiful. No mixing is required.

**Example case 2:** Take the second color (with value **x** = 1) and mix it into the first color (with value **x** = 2). After the mixing, the colors will be 3 1 2. Now the colors are beautiful. This is the minimum number of mixing operations that are required. Hence, the answer is 1.

</details>

## Approach

Each mixing operation changes the value of **exactly one** colour — the receiver becomes $x + y$ while the donor keeps its value. So every operation can fix at most one offending colour, and the question is how many colours must change.

If a value occurs $c$ times, then $c - 1$ of those copies must be altered, since only one may keep it. Summing over all values:

$$\sum_v (c_v - 1) \;=\; N - (\text{number of distinct values})$$

That is a lower bound, and it is achievable: because $A_i \geq 1$, every mix **strictly increases** the receiver's value, so repeatedly mixing a duplicate with the current maximum pushes it above everything present and creates a fresh value each time. No operation is ever wasted.

So the answer is simply $N$ minus the size of the set of values — one pass into a Python `set`.

Sample case 1, $[1,2,3]$, is already distinct and needs nothing. Sample case 2, $[2,1,2]$, has two colours sharing the value $2$, so one of them must be mixed — a single operation.

Values reach $10^9$, so hashing into a set is the right structure rather than an array indexed by value. With $N$ up to $10^5$ and $T \leq 10$ this is comfortable.

Note the answer depends only on **how many** duplicates there are, never on their values — the arithmetic of the mixing never enters the count.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        distinct = len(set(data[pos + 1:pos + 1 + n]))
        pos += 1 + n
        # Each mix changes exactly one colour, so every duplicate copy costs one.
        out.append(str(n - distinct))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
