# 144. First and Last

> [`FIRSTANDLAST`](https://www.codechef.com/problems/FIRSTANDLAST) &middot; difficulty **932** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Cyclically adjacent pairs |
| **CodeChef tags** | `Algorithms`, `Greedy`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an array $A = [A_1, A_2, \ldots, A_N]$ of length $N$.

You can right rotate it any number of times (possibly, zero). What is the maximum value of $A_1 + A_N$ you can get?

**Note:** Right rotating the array $[A_1, A_2, \ldots, A_N]$ once gives the array $[A_N, A_1, A_2, \ldots, A_{N-1}]$. For example, right rotating $[1, 2, 3]$ once gives $[3, 1, 2]$, and right rotating it again gives $[2, 3, 1]$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

**Output**

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
2
5 8
3
5 10 15
4
4 4 4 4
```

**Sample output**

```
13
25
8
```

<details><summary>Explanation</summary>

**Test case $1$:** Whether you right rotate the array or not, you will always end up with $A_1+A_N = 13$.

**Test case $2$:** It is optimal to right rotate the array once after which the array becomes $[15,5,10]$ with $A_1 + A_N = 25$.

**Test case $3$:** No matter how much you right rotate the array, you will always obtain $A_1 + A_N = 8$.

</details>

## Approach

The key observation is what a right rotation does to the *pair* $(A_1, A_N)$, not to the array as a whole.

Initially the first and last elements are $A_1$ and $A_N$ — which are **cyclically adjacent**, since the array wraps from $A_N$ back to $A_1$. After one right rotation the array is $[A_N, A_1, \ldots, A_{N-1}]$, whose ends are $A_N$ and $A_{N-1}$: adjacent again. Each rotation simply slides the split point by one.

So every reachable pair is a cyclically adjacent pair, and every such pair is reachable. The answer is

$$\max_{0 \leq i < N} \left( A_i + A_{(i+1) \bmod N} \right)$$

one pass, $O(N)$ time and $O(1)$ space. No rotation is ever performed — simulating all $N$ rotations would be $O(N^2)$ and far too slow at $N = 10^5$.

The wraparound term is essential and easy to drop. Sample case 2, $[5, 10, 15]$, has adjacent sums $15$ and $25$ from the interior pairs and $20$ from the wrapping pair $(15, 5)$; here the interior wins, but on an array like $[9, 1, 9]$ only the wrapping pair gives the maximum $18$.

Sample case 1 with $N = 2$ is a degenerate case worth checking: both elements are adjacent to each other in both directions, and the sum $13$ is the only possible answer.

Values reach $10^9$, so a pair sums to $2 \times 10^9$ — past the signed 32-bit limit, which a C solution would need to handle with a 64-bit type.

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
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Rotating only slides the split point, so the ends are always a
        # cyclically adjacent pair. The wraparound pair must be included.
        best = max(a[i] + a[(i + 1) % n] for i in range(n))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/FIRSTANDLAST.md](../docs/arrays/FIRSTANDLAST.md)
