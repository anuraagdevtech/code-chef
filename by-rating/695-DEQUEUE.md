[&larr; 694. Treeversion](694-TREEVERS.md) &middot; [Index](README.md) &middot; [696. Squarified &rarr;](696-SQUAR.md)

# 695. Minimum Popping

> [`DEQUEUE`](https://www.codechef.com/problems/DEQUEUE) &middot; difficulty **2463** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Keep the longest middle part that does not swallow all copies of any value |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Searching`, `1D Arrays`, `Binary Search` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(N + M)$ |

## Question

You are given a double-ended queue $Q$. Initially, it contains elements $Q_1, Q_2, \ldots, Q_M$ in this order. Each of these elements is an integer between $1$ and $N$ (inclusive) and each integer between $1$ and $N$ (inclusive) occurs in the queue at least once.

We want to pop some (possibly zero) elements from the front of the queue and some (not necessarily the same number, possibly zero) elements from the back. Among all the popped elements, each integer between $1$ and $N$ (inclusive) should appear at least once. Find the smallest possible total number of elements we need to pop.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $M$ space-separated integers $Q_1, Q_2, \ldots, Q_M$.

**Output**
For each test case, print a single line containing one integer — the minimum number of elements we need to pop.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $N \leq M \leq 2 \cdot 10^5$
- for each $i$ ($1 \le i \le N$), there is at least one element equal to $i$ in the queue
- the sum of $N$ over all test cases does not exceed $10^5$
- the sum of $M$ over all test cases does not exceed $2 \cdot 10^5$

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $N \leq M \leq 2 \cdot 10^5$
- for each $i$ ($1 \le i \le N$), there is at least one element equal to $i$ in the queue
- the sum of $N$ over all test cases does not exceed $10^5$
- the sum of $M$ over all test cases does not exceed $2 \cdot 10^5$

## Sample

**Sample input**

```
3
2 2
1 2
2 3
1 2 1
3 6
1 1 1 3 2 2
```

**Sample output**

```
2
2
4
```

<details><summary>Explanation</summary>

**Example case 1:** Since $N = M$ and all elements are pairwise distinct, we have to pop everything to get each value at least once.

**Example case 2:** We can pop the first $2$ or the last $2$ elements.

**Example case 3:** We can pop the first element and the last $3$ elements, so the answer is $1 + 3 = 4$.

</details>

## Approach

Popping from the two ends leaves a contiguous middle part (possibly empty). The popped elements contain every value from 1 to $N$ exactly when the middle part does *not* contain all occurrences of any value. Minimising the number of pops is the same as maximising the length of such a middle part.

"Does not contain all occurrences of any value" is preserved when the window shrinks, so two pointers work: extend the right end by one element; if the window now holds every occurrence of that element's value, move the left end forward until one occurrence of it has left the window. (No other value can be violated - only the count of the new element grew.) Track the longest window seen; the answer is $M$ minus its length.

## Solution

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    queue = [next(tokens) - 1 for _ in range(m)]
    total = [0] * n
    for value in queue:
        total[value] += 1
    inside = [0] * n
    left = best = 0
    for right, value in enumerate(queue):
        inside[value] += 1
        while inside[value] == total[value]:
            inside[queue[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return str(m - best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- If every value occurs exactly once, the middle part must be empty and everything is popped.
- The middle part may be empty even otherwise.
- Popping only from one end is covered - the window may touch either end of the queue.
- Values are shifted to 0-based for indexing.

## Dry run

`Q = [1, 1, 1, 3, 2, 2]`, $N = 3$. Totals: value 1 three times, value 2 twice, value 3 once.

The middle part cannot contain the 3 at all, at most two of the 1s and at most one of the 2s. The longest such window is `1 1` (length 2).

Answer $6 - 2 = 4$.

---

Same problem grouped by topic: [../docs/arrays/DEQUEUE.md](../docs/arrays/DEQUEUE.md)
