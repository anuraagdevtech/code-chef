# 198. Reversal Sorting

> [`REVSORT`](https://www.codechef.com/problems/REVSORT) &middot; difficulty **1288** &middot; time limit **3.5s** &middot; Level up from 1* to 2* (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Constraining which inversions may be undone |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef is deriving weird ways to sort his array. Currently he is trying to sort his arrays in increasing order by reversing some of his subarrays.

To make it more challenging for himself, Chef decides that he can reverse only those subarrays that have sum of its elements **at most** $X$. Soon he notices that it might not be always possible to sort the array with this condition.

Can you help the Chef by telling him if the given array can be sorted by reversing subarrays with sum at most $X$.

More formally, for a given array $A$ and an integer $X$, check whether the array can be sorted in increasing order by reversing some (possibly none) of the subarrays such that the sum of all elements of the subarray is **at most** $X$.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains of two space-separated integers $N$ and $X$ denoting the length of the array and the maximum sum of subarrays that you can reverse.
- The second line contains $N$ space-separated integers $A_1, A_2,..., A_N$ representing the initial array.

**Output**

For each test case, output $\texttt{YES}$ if Chef can sort the array using a finite number of operations, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 5\cdot 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 2\cdot 10^9$
- $1 \leq X \leq 2\cdot 10^9$
- Sum of $N$ over all test cases does not exceeds $3\cdot 10^5$.

## Sample

**Sample input**

```
3
4 1
1 2 3 4
4 1
2 1 3 4
5 7
3 2 2 3 3
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** The array is already sorted so we need not make any operations.

**Test case $2$:** There is no subarray with sum less than or equal to $1$ so we cannot sort the array.

**Test case $3$:** We can reverse the subarray $A[1, 3]$ which has a sum of $3+2+2=7$. Thus, the reversed subarray is $[2, 2, 3]$. The resulting array is $[2, 2, 3, 3, 3]$. The array is sorted in $1$ operation.

</details>

## Approach

Reversing a subarray of length $2$ is just swapping an adjacent pair, so the pair $(x, y)$ can be swapped only when $x + y \leq X$. That single observation drives everything.

**Necessity.** If two elements $x$ and $y$ satisfy $x + y > X$, they can never cross each other — not directly, and not by any sequence of moves, since any reversal that reorders them relative to one another would have to contain both and therefore have sum exceeding $X$. So every pair that is **out of order** in the input must be cheap enough to swap:

$$\text{for all } i < j \text{ with } A_i > A_j: \quad A_i + A_j \leq X$$

**Sufficiency.** If that holds, bubble sort works: it only ever swaps adjacent pairs that are currently inverted, and any pair inverted now was inverted in the original array, so its sum is within budget.

Checking all pairs is $O(N^2)$, but only the **worst** inversion matters. Sweeping left to right with a running prefix maximum, each position $j$ contributes the candidate $\max(A_1 \ldots A_{j-1}) + A_j$ whenever that maximum exceeds $A_j$. The answer is `YES` exactly when the largest such candidate is at most $X$ — or when no inversion exists at all.

The already-sorted case is where this matters most. Sample case 1 is $[1,2,3,4]$ with $X = 1$: nothing can be swapped, but nothing needs to be, so `YES`. Sample case 2 is the same tiny budget with one inversion, $2$ before $1$, costing $3 > 1$ — `NO`. Sample case 3 has inversions costing at most $5$, inside the budget of $7$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, x = int(data[pos]), int(data[pos + 1])
        a = [int(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n
        worst = 0
        prefix_max = a[0]
        for j in range(1, n):
            # The costliest inversion ending at j pairs A_j with the largest
            # value before it, when that value is bigger.
            if prefix_max > a[j]:
                worst = max(worst, prefix_max + a[j])
            else:
                prefix_max = a[j]
        out.append("YES" if worst <= x else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/REVSORT.md](../docs/arrays/REVSORT.md)
