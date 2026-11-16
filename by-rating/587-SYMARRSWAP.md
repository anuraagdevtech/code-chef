[&larr; 586. K Increment Palindrome](586-KPAL.md) &middot; [Index](README.md) &middot; [588. Kirito in labyrinth &rarr;](588-KIRLAB.md)

# 587. Symmetric Swaps

> [`SYMARRSWAP`](https://www.codechef.com/problems/SYMARRSWAP) &middot; difficulty **2041** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Smallest value window that contains an option for every index |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Greedy`, `Simple Algos`, `Arrays`, `Sliding Window`, `Sorting`, `Two pointers` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has two arrays $A$ and $B$ of the same size $N$.

In one operation, Chef can:
- Choose an index $i$ $(1 \leq i \leq N)$ and swap the elements $A_i$ and $B_i$.

Chef came up with a task to find the **minimum** possible value of **($A_{max} - A_{min}$)** after performing the swap operation any (possibly zero) number of times.

Since Chef is busy, can you help him solve this task?

Note that $A_{max}$ and $A_{min}$ denote the maximum and minimum elements of the array $A$ respectively.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains one integer $N$ — the number of elements in each array.
    - The second line consists of $N$ space-separated integers $A_1, A_2,\ldots ,A_N$ denoting the elements of the array $A$.
    - The third line consists of $N$ space-separated integers $B_1, B_2, \ldots ,B_N$ denoting the elements of the array $B$.

**Output**

For each test case, output on a new line, the **minimum** possible value of **($A_{max} - A_{min}$)** in the array $A$ after doing swap operation any number of times.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
3
2
1 2
2 1
3
1 5 3
2 3 1
4
4 2 5 1
5 3 4 1
```

**Sample output**

```
0
1
3
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can make the following operations:
- Operation $1$: Choose $i=1$ and swap $A_1$ with $B_1$.

By doing the above operations, array $A$ becomes $[2, 2]$. Here $(A_{max} - A_{min}) = 0$. It can be shown that this is the minimum value possible.

**Test case $2$:** Chef can make the following operations:
- Operation $1$: Choose $i=1$ and swap $A_1$ with $B_1$.
- Operation $2$: Choose $i=2$ and swap $A_2$ with $B_2$.

By doing the above operations, array $A$ becomes $[2, 3, 3]$. Here $(A_{max} - A_{min}) = 1$. It can be shown that this is the minimum value possible.

**Test case $3$:** Chef can make the following operations:
- Operation $1$: Choose $i=2$ and swap $A_2$ with $B_2$.
- Operation $2$: Choose $i=3$ and swap $A_3$ with $B_3$.

By doing the above operations, array $A$ becomes $[4, 3, 4, 1]$. Here $(A_{max} - A_{min}) = 3$. It can be shown that this is the minimum value possible.

</details>

## Approach

After the swaps, $A_i$ is simply one of the two values $\{A_i, B_i\}$, chosen independently for every index. So the task is: choose one value per index so that the range of the chosen values is as small as possible.

A range $[lo, hi]$ is achievable exactly when every index has at least one of its two values inside it. Put all $2N$ values, tagged with their index, into one sorted list and find the shortest window (in value) that contains every index at least once - the classic two-pointer "smallest window covering all colours". Extend the right end; while all indices are covered, record the width and shrink from the left.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        first = [next(tokens) for _ in range(n)]
        second = [next(tokens) for _ in range(n)]
        items = sorted([(value, i) for i, value in enumerate(first)] + [(value, i) for i, value in enumerate(second)])
        counts = [0] * n
        have = 0
        left = 0
        best = 10 ** 18
        for r, (value, i) in enumerate(items):
            if counts[i] == 0:
                have += 1
            counts[i] += 1
            while have == n:
                best = min(best, value - items[left][0])
                j = items[left][1]
                counts[j] -= 1
                left += 1
                if counts[j] == 0:
                    have -= 1
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $A_i = B_i$ contributes the same value twice; the multiplicity counter handles it.
- $N = 1$: the answer is 0.
- The optimal minimum and maximum are always among the given values, so only windows between listed values need checking.
- Values up to $10^9$ only matter through their order and differences.

## Dry run

`A = [1, 5, 3]`, `B = [2, 3, 1]`. Sorted (value, index): `(1,1) (1,3) (2,1) (3,2) (3,3) (5,2)`.

The right end first covers all three indices at `(3,2)`: window from `(1,1)`, width 2. Shrinking: drop `(1,1)` (index 1 still present via `(2,1)`), width $3 - 1 = 2$; drop `(1,3)` - index 3 is lost, stop. Extending to `(3,3)` covers again with left end `(2,1)`: width 1.

Answer 1 (choose 2, 3, 3).

---

Same problem grouped by topic: [../docs/sorting/SYMARRSWAP.md](../docs/sorting/SYMARRSWAP.md)
