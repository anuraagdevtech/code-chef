# 269. Dense Bracket Sequence

> [`DENSE`](https://www.codechef.com/problems/DENSE) &middot; difficulty **1472** &middot; time limit **2.5s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Best split between an open prefix and a close suffix |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

A bracket sequence $S$ is called *dense* if one of the following is true:
- $S$ is empty.
- $S = (X)$ where $X$ is dense.

You are given a bracket sequence $S$. What is the **minimum** number of brackets you must remove to make it dense?

**Input**

- The first line of input will contain a single integer $T$, the number of test cases. The description of the $T$ test cases follows.
- The first line of each test case contains one integer $N$, denoting the length of the bracket sequence.
- The second line of each test case contains the bracket sequence $S$ of length $N$.

**Output**

For each test case, output on a new line the minimum number of brackets you must remove from $S$ to make it dense.

## Constraints

- $1 \leq T \leq 2 \cdot 10^4$
- $1 \leq N \leq 3 \cdot 10^5$
- The sum of $N$ over all test cases does not exceed $3 \cdot 10^5$

## Sample

**Sample input**

```
4
8
()(())()
6
((()))
10
()()()()()
8
((()))()
```

**Sample output**

```
2
0
4
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Remove the $2^{nd}$ and $7^{th}$ bracket to obtain `((()))`, which is dense.

**Test case $2$:** The given bracket sequence is already dense.

**Test case $3$:** Remove the $2^{nd}$, $4^{th}$, $7^{th}$, and $9^{th}$ bracket to obtain `((()))`, which is dense.

**Test case $4$:** Remove the last $2$ brackets to obtain `((()))`.

</details>

## Approach

Unfolding the definition, a dense sequence is $\underbrace{(\cdots(}_{k}\underbrace{)\cdots)}_{k}$ — $k$ opening brackets followed by $k$ closing brackets, for some $k \geq 0$. Nothing else qualifies: the recursion only ever wraps, never concatenates, so `()()` is *not* dense even though it is balanced.

Removing brackets leaves a subsequence, so the task is to find the **longest dense subsequence** and remove the rest. A dense subsequence of size $2k$ takes $k$ openings from some prefix and $k$ closings from the complementary suffix, so with $\mathrm{open}(i)$ counting `(` in $S_1 \ldots S_i$ and $\mathrm{close}(i)$ counting `)` in $S_{i+1} \ldots S_N$,

$$k^* = \max_{0 \leq i \leq N} \min\bigl(\mathrm{open}(i),\ \mathrm{close}(i)\bigr), \qquad \text{answer} = N - 2k^*$$

Both counts are prefix sums, so one left-to-right sweep that increments the running open count and decrements the remaining close count evaluates every split in $O(1)$. The answer is well defined because $k = 0$ is always available — the empty sequence is dense, so the worst case is removing everything.

The samples separate "balanced" from "dense". `((()))` is already dense, so $0$. `()()()()()` is perfectly balanced yet costs $4$: the best split takes three `(` from the left and three `)` from the right, keeping $6$ of $10$. `()(())()` keeps the same $6$, costing $2$. And `((()))()` also costs $2$ — the trailing `()` must go, since appending it breaks the nesting even though the prefix was already dense.

## Solution

```python
import sys

OPEN = 0x28


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        closes = n - s.count(OPEN)      # ')' still ahead of the split
        opens = 0
        best = 0
        # Split before each position: take opens from the left, closes right.
        for c in s:
            if c == OPEN:
                opens += 1
            else:
                closes -= 1
            best = max(best, opens if opens < closes else closes)
        out.append(str(n - 2 * best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/prefix-sums/DENSE.md](../docs/prefix-sums/DENSE.md)
