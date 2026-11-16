[&larr; 569. Winter](569-ELWINTER.md) &middot; [Index](README.md) &middot; [571. Subtree Removal &rarr;](571-SUBREM.md)

# 570. Subarray Removal

> [`REMSUBARR`](https://www.codechef.com/problems/REMSUBARR) &middot; difficulty **2007** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Positions of the largest values must form one contiguous block |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has a *permutation* $A$ of length $N$. Chef can perform the following operation on $A$: $\\$
**1)** Select $L$ and $R$ such that $(1 \le L \le R \le N)$ and $(R - L + 1 \lt N)$ $\\$
**2)** Remove the subarray $A_{L \ldots R}$ from $A$. (The remaining parts of $A$ are concatenated)

The score of this operation $ = $ length of the subarray removed $ = R - L + 1$

For e.g., if $A = [3, 1, 4, 6, 5, 2]$, and Chef selects $L = 3, R = 5$, then the score of this operation $ = 3$ and $A$ becomes $[3, 1, 2]$.

Chef wants to perform this operation **exactly once** such that, after the operation, $A$ still remains a permutation. What is the maximum score that Chef can achieve in doing so?

As a reminder, a permutation of length $M$ is an array where every integer from $1$ to $M$ occurs exactly once.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the permutation $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the permutation $A$.

**Output**

For each test case, output the maximum score that Chef can achieve after applying the operation exactly once such that $A$ still remains a permutation.

## Constraints

- $1 \leq T \leq 10^5$
- $2 \le N \le 10^5$
- $A$ is a permutation
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

## Sample

**Sample input**

```
3
3
2 1 3
7
1 2 3 4 5 6 7
6
3 1 4 6 5 2
```

**Sample output**

```
1
6
3
```

<details><summary>Explanation</summary>

**Test Case 1:** Chef can remove subarray $A_{3 \ldots 3}$ after which $A$ becomes $[2, 1]$ which is still a permutation.

**Test Case 2:** Chef can remove subarray $A_{2 \ldots 7}$ after which $A$ becomes $[1]$ which is still a permutation.

**Test Case 3:** Chef can remove subarray $A_{3 \ldots 5}$ after which $A$ becomes $[3, 1, 2]$ which is still a permutation.

</details>

## Approach

What remains must be a permutation of $1 \dots m$ for some $m \ge 1$, so the removed elements are exactly the values $m+1, \dots, N$. Removing them is one operation precisely when they occupy a contiguous block of positions.

Add the values $N, N-1, \dots$ one at a time while tracking the smallest and largest position seen. The values $v \dots N$ form a contiguous block exactly when (largest $-$ smallest $+ 1$) equals how many there are, $N - v + 1$. The best score is the largest such count; removing only the value $N$ is always possible, so the answer is at least 1.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        perm = [next(tokens) for _ in range(n)]
        position = [0] * (n + 1)
        for i, value in enumerate(perm):
            position[value] = i
        leftmost = rightmost = position[n]
        best = 1
        for value in range(n - 1, 1, -1):
            leftmost = min(leftmost, position[value])
            rightmost = max(rightmost, position[value])
            if rightmost - leftmost + 1 == n - value + 1:
                best = n - value + 1
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- At least one element must stay, so the scan stops at value 2.
- A sorted permutation lets everything but the 1 go: answer $N - 1$.
- The value $N$ alone is always a valid block.
- Larger candidate sets are checked later in the scan, so the last success is the maximum.

## Dry run

`A = [3, 1, 4, 6, 5, 2]` (positions 1-6: value 6 at 4, 5 at 5, 4 at 3, 3 at 1, 2 at 6).

| values removed | positions span | count | block? |
|---|---|---:|---|
| 6 | 4-4 | 1 | yes |
| 5, 6 | 4-5 | 2 | yes |
| 4, 5, 6 | 3-5 | 3 | yes |
| 3..6 | 1-5 | 4 | no |
| 2..6 | 1-6 | 5 | no |

Answer 3.

---

Same problem grouped by topic: [../docs/arrays/REMSUBARR.md](../docs/arrays/REMSUBARR.md)
