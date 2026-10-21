# 300. K Odd Sum

> CodeChef problem code [`ADVITIYA5`](https://www.codechef.com/problems/ADVITIYA5) &middot; difficulty **1614** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Parity blocks and the number of switches |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Given integers $N$ and $K$, construct a permutation $P = [P_1, P_2, \ldots, P_N]$ of the integers $\{1,2,\ldots, N\}$ such that there are **exactly** $K$ indices $i$ ($1 \le i \lt N$) for which $(P_i + P_{i + 1})$ is odd.

It can be proved that the answer always exists under the constraint of $1 \le K \le N - 1$.
If multiple answers exist, any of them will be accepted.

**Note:** A permutation of $\{1, 2, \ldots, N\}$ is a sequence in which every integer from $1$ to $N$ appears *exactly once*.
For example, if $N = 4$, $[4, 2, 1, 3]$ and $[1, 2, 3, 4]$ are valid permutations, but $[1, 4, 2, 1]$ ($1$ is repeated) and $[1, 3, 5, 2]$ ($5$ is larger than $N=4$) are not.

**Input**

- The first line of input contains a single integer $T$, denoting the number of testcases.
- The first and only line of each testcase contains two space-separated integers $N$ and $K$, denoting the length of permutation and the required number of indices $i$ such that $(P_i+ P_{i+1})$ is odd, respectively.

**Output**

For each testcase, output on a new line $N$ space-separated integers $P_1, P_2, \ldots, P_N$ denoting the permutation you found.
Each integer from $1$ to $N$ should appear exactly once, and there should be exactly $K$ indices $i$ such that $(P_i + P_{i+1})$ is odd.

If multiple possible answers exist, any of them will be accepted.

## Constraints

- $1 \le T \le 10^3$
- $2 \le N \le 10^5$
- $1 \le K \le N - 1$
- The sum of $N$ across all testcases does not exceed $2 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
2 1
4 2
```

**Sample output**

```
2 1
4 3 1 2
```

<details><summary>Explanation</summary>

**Test case $1$:** We have $P = [2, 1]$. $i = 1$ is the only index where $P_i + P_{i + 1}$ is odd.
$P = [1, 2]$ is also a valid solution, and will be accepted.

**Test case $2$:** We have $P = [4, 3, 1, 2]$.
- $i = 1$ gives us $(P_1 + P_2) = 4+3 = 7$, which is odd.
- $i = 2$ gives us $(P_2 + P_3) = 3+1 = 4$, which is even.
- $i = 3$ gives us $(P_3 + P_4) = 1+2 = 3$, which is odd.

Exactly $K = 2$ indices satisfy the given criterion, as required.

</details>

## Approach

$P_i + P_{i+1}$ is odd exactly when the two have **different parity**. So reading the permutation as a string of O's and E's, the answer counts the positions where that string changes — and a string with $b$ maximal blocks has exactly $b - 1$ changes.

So the task is to arrange $\lceil N/2 \rceil$ odd numbers and $\lfloor N/2 \rfloor$ even numbers into exactly

$$b = K + 1$$

alternating blocks. Starting with an odd block, that needs $\lceil b/2 \rceil$ odd blocks and $\lfloor b/2 \rfloor$ even blocks — and both fit, since $b \leq N$ gives $\lceil b/2 \rceil \leq \lceil N/2 \rceil$ and likewise for the evens. So starting with odds always works and no case analysis is needed.

The leftovers go into the **first** block of each parity: give every block one number, then dump the surplus odds into the first odd block and the surplus evens into the first even block. Padding a block never creates a new change, since the block's parity is unchanged.

The constraint $K \geq 1$ guarantees $b \geq 2$, so there is at least one even block to receive the evens — with $b = 1$ there would be nowhere to put them.

For $N = 4, K = 2$ this builds three blocks: odds $[1]$, evens $[2,4]$, odds $[3]$, giving `1 2 4 3` with changes at positions $1$ and $3$. The published sample, `4 3 1 2`, has a different block structure with the same count — **any valid permutation is accepted**, so this is judged by a checker.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        odds = list(range(1, n + 1, 2))
        evens = list(range(2, n + 1, 2))
        blocks = k + 1                       # b blocks give b - 1 changes
        o_blocks, e_blocks = (blocks + 1) // 2, blocks // 2
        # Surplus goes into the first block of each parity: padding a block
        # never adds a change.
        res = []
        oi = ei = 0
        for b in range(blocks):
            if b % 2 == 0:
                take = len(odds) - o_blocks + 1 if b == 0 else 1
                res.extend(odds[oi:oi + take])
                oi += take
            else:
                take = len(evens) - e_blocks + 1 if b == 1 else 1
                res.extend(evens[ei:ei + take])
                ei += take
        out.append(" ".join(map(str, res)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Algorithms`
