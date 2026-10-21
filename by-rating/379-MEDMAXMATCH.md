# 379. Maximum Median Matching

> [`MEDMAXMATCH`](https://www.codechef.com/problems/MEDMAXMATCH) &middot; difficulty **1647** &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Opposite pairing of the top halves |
| **CodeChef tags** | `Algorithms`, `Greedy`, `Sorting` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

$N$ boys and $N$ girls attend a dance class, where $N$ is **odd**. For today's practice session, they need to form $N$ boy-girl pairs.

The $i$-th boy has a happiness value of $A_i$ and the $i$-th girl has a happiness value of $B_i$.
A pair consisting of the $i$-th boy and the $j$-th girl has a happiness value of $A_i + B_j$.

Let the happiness values of the $N$ pairs be $C_1, C_2, \ldots, C_N$. The dance instructor would like it if many of the pairs have a high happiness value, and passes the task to you — find the **maximum** possible value of the **median of** $C$, if the boy-girl pairs are chosen optimally.

**Note:** The median of a odd-sized list of integers is the middle number when they are sorted. For example, the median of $[1]$ is $1$, the median of $[1, 5, 2]$ is $2$, and the median of $[30, 5, 5, 56, 3]$ is $5$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the happiness values of the boys.
    - The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$ — the happiness values of the girls.

**Output**

For each test case, output on a new line the maximum possible median happiness of the $N$ pairs.

## Constraints

- $1 \leq T \leq 3 \cdot 10^4$
- $1 \leq N \lt 3\cdot 10^5$
- $N$ is odd
- $1 \leq A_i, B_i \leq 10^9$ for each valid $i$
- The sum of $N$ across all test cases won't exceed $3 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):**
    - The sum of $N$ across all test cases won't exceed $10$.
- **Subtask 2 (30 points):**
    - The sum of $N$ across all test cases won't exceed $4000$.
- **Subtask 3 (60 points):**
    - No further constraints.

## Sample

**Sample input**

```
3
1
10
25
3
1 6 6
2 2 7
5
10 4 93 5 16
4 34 62 6 26
```

**Sample output**

```
35
8
50
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one boy and one girl, so they must be paired with each other. The happiness value of the pair is $10 + 25 = 35$, and it is also the median.

**Test case $2$:** Pair $A_1$ with $B_3$, $A_2$ with $B_2$, and $A_3$ with $B_3$. The happiness values are then $[1+7, 2+6, 2+6] = [8, 8, 8]$, with a median of $8$. It can be shown that this is the maximum possible median.

**Test case $3$:** One way of achieving a median of $50$ is as follows:
- Pair $A_1$ with $B_3$, for a happiness of $10 + 62 = 72$
- Pair $A_2$ with $B_4$, for a happiness of $4 + 6 = 10$
- Pair $A_3$ with $B_5$, for a happiness of $93 + 26 = 119$
- Pair $A_4$ with $B_1$, for a happiness of $5 + 4 = 9$
- Pair $A_5$ with $B_2$, for a happiness of $16 + 34 = 50$

The happiness values are $[72, 10, 119, 9, 50]$, with a median of $50$. It can be shown that no other pairing obtains a strictly larger median.

</details>

## Approach

With $N$ odd, the median is the $m$-th largest for $m = \frac{N+1}{2}$. So the median is at least $v$ exactly when $m$ pairs have sum at least $v$, and the task becomes: choose $m$ pairs to **maximise their minimum sum**.

Those $m$ pairs should use the $m$ largest values from each side — a smaller value brings nothing — and within that selection they should be paired in **opposite order**: the largest $A$ with the smallest chosen $B$, and so on. That is the standard max-min pairing: if two pairs were matched in the same order, swapping their partners raises the smaller sum without lowering the larger one above it.

$$\text{answer} = \min_{0 \leq i < m}\ \bigl(A_{N-m+i} + B_{N-1-i}\bigr)$$

with both arrays sorted ascending. The leftover $\frac{N-1}{2}$ values on each side pair arbitrarily; their sums can only be smaller, so they sit below the median and never affect it.

Why opposite rather than same order: pairing the two largest together wastes one of them, since a pair contributes only one sum. Spreading the big values across different pairs is what lifts the minimum.

The third sample shows this clearly. With $A = [4,5,10,16,93]$ and $B = [4,6,26,34,62]$ and $m = 3$, the chosen pairs are $10{+}62 = 72$, $16{+}34 = 50$ and $93{+}26 = 119$, so the median is $50$. Pairing in the same order would give $10{+}26 = 36$ as the minimum instead.

The second sample, $A = [1,6,6]$ and $B = [2,2,7]$, gives $6{+}7$ and $6{+}2$, so the median is $8$ — the leftover $1{+}2 = 3$ sits below it as expected.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        b = sorted(int(x) for x in data[pos + 1 + n:pos + 1 + 2 * n])
        pos += 1 + 2 * n
        m = (n + 1) // 2
        # Top m of each side, paired in opposite order to lift the minimum.
        out.append(str(min(a[n - m + i] + b[n - 1 - i] for i in range(m))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/MEDMAXMATCH.md](../docs/greedy/MEDMAXMATCH.md)
