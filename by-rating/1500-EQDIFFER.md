# 1500 &middot; Equal Difference

> CodeChef problem code [`EQDIFFER`](https://www.codechef.com/problems/EQDIFFER) &middot; time limit **2.5s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Which multisets have all pairwise differences equal |
| **CodeChef category** | main |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/arrays/EQDIFFER.md](../docs/arrays/EQDIFFER.md)

## Question

You are given an array of $N$ integers. Find the *minimum* number of integers you need to delete from the array such that the absolute difference between each pair of integers in the remaining array will become equal.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

**Output**

For each test case, print a single line containing one integer - the minimum number of integers to be deleted to satisfy the given condition.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
2
1 2
5
2 5 1 2 2
4
1 2 1 2
```

**Sample output**

```
0
2
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one pair of integers and the absolute difference between them is $|A_1 - A_2| = |1 - 2| = 1$. So there is no need to delete any integer from the given array.

**Test case $2$:** If the integers $1$ and $5$ are deleted, the array A becomes $[2, 2, 2]$ and the absolute difference between each pair of integers is $0$. There is no possible way to delete less than two integers to satisfy the given condition.

</details>

## Approach

Ask what the surviving array can look like. If it keeps three distinct values $a < b < c$, then $c - a$ is strictly larger than both $b - a$ and $c - b$, so the pairwise differences cannot all agree. Hence the survivors are one of only two shapes:

- **all equal** — every pairwise difference is $0$, and any number of copies is fine;
- **at most two elements** — there is then at most one pair, so "all differences equal" holds vacuously.

So the best we can keep is

$$\max\bigl(\text{largest frequency},\ \min(N, 2)\bigr)$$

and the answer is $N$ minus that.

Both branches are needed, and the samples separate them. Case 2, $[2,5,1,2,2]$, has three copies of $2$ — keeping them beats keeping any two elements, so the answer is $5 - 3 = 2$. Case 1, $[1,2]$, has no repeats at all, but two elements are always legal, so nothing is deleted.

Case 3, $[1,2,1,2]$, is the tie: the largest frequency is $2$ and the two-element option is also $2$, so either works and the answer is $4 - 2 = 2$.

The $\min(N, 2)$ guard matters for $N = 1$, where only one element exists to keep.

A `Counter` gives the modal frequency in one pass. Values reach $10^9$, so hashing rather than an indexed array is the right structure, and with $\sum N = 5 \times 10^5$ the single pass is what keeps this comfortable.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # Keep all copies of one value, or keep any two elements.
        keep = max(max(counts.values()), min(n, 2))
        out.append(str(n - keep))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
