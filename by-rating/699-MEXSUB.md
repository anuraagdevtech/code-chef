[&larr; 698. Chef Up](698-CHEF7UP.md) &middot; [Index](README.md) &middot; [700. Expected Sum &rarr;](700-EXPECTEDSUM.md)

# 699. Mex Subsequence

> [`MEXSUB`](https://www.codechef.com/problems/MEXSUB) &middot; difficulty **2494** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Every part needs all values below the global MEX - count partitions with a prefix-sum DP |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Groupings`, `Subarray` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Ridbit is given an array $a_1, a_2, \ldots, a_N$. He needs to find the number of ways to divide the array into contiguous subarrays such that:
- Each element of the sequence $a$ belongs to exactly one of the subarrays.
- There is an integer $m$ such that the MEX of every subarray is equal to $m$. The MEX of a sequence is the smallest non-negative integer which does not occur in this sequence.

Help Ridbit with this task.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

**Output**
For each test case, print a single line containing one integer ― the number of ways to divide the sequence, modulo $10^9 + 7$.

**Constraints**
- $1 \leq T \leq 10$
- $1 \leq N \leq 100,000$
- $0 \leq a_i \leq N$ for each valid $i$

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 100,000$
- $0 \leq a_i \leq N$ for each valid $i$

## Sample

**Sample input**

```
2
6
1 0 0 1 0 1
3
1 2 3
```

**Sample output**

```
5
4
```

<details><summary>Explanation</summary>

**Example case 1:** The five valid ways to divide the sequence are:
- $[1, 0, 0, 1, 0, 1]$
- $[1, 0], [0, 1, 0, 1]$
- $[1, 0, 0], [1, 0, 1]$
- $[1, 0, 0, 1], [0, 1]$
- $[1, 0], [0, 1], [0, 1]$

</details>

## Approach

If every part has MEX $m$, then every part contains $0, \dots, m - 1$ and none contains $m$; so the whole array contains $0, \dots, m - 1$ and not $m$, which means $m$ is the MEX of the whole array. Conversely a part has that MEX as soon as it contains all of $0, \dots, m - 1$, because $m$ does not occur anywhere.

If $m = 0$ there is no requirement at all and every one of the $2^{N-1}$ ways to cut the array is valid.

Otherwise let `ways[i]` be the number of valid partitions of the first $i$ elements. The last part $(j, i]$ is valid exactly when it contains every required value, i.e. when $j$ is at most the smallest among the last occurrences (up to $i$) of the values $0 \dots m - 1$. Call that position $\ell_i$ (0-based index); then

$$\text{ways}[i] = \sum_{j \le \ell_i} \text{ways}[j],$$

a prefix sum of the DP values, and 0 while some required value has not appeared yet. The minimum of the last occurrences changes as the scan proceeds; it is kept in a heap of (last occurrence, value) pairs with outdated entries discarded lazily.

## Solution

```python
import sys
import heapq


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    seen = set(values)
    mex = 0
    while mex in seen:
        mex += 1
    MOD = 1000000007
    if mex == 0:
        return str(pow(2, n - 1, MOD))
    last = [-1] * mex
    heap = [(-1, value) for value in range(mex)]
    heapq.heapify(heap)
    prefix = [1]
    ways = 0
    for i, value in enumerate(values):
        if value < mex:
            last[value] = i
            heapq.heappush(heap, (i, value))
        while heap[0][0] != last[heap[0][1]]:
            heapq.heappop(heap)
        limit = heap[0][0]
        ways = prefix[limit] if limit >= 0 else 0
        prefix.append((prefix[-1] + ways) % MOD)
    return str(ways)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- MEX 0 (no zero in the array): the answer is $2^{N-1}$.
- A prefix that lacks some required value cannot be a complete part: `ways` is 0 there.
- Values at or above the MEX are irrelevant.
- Everything is modulo $10^9 + 7$.

## Dry run

`A = [1, 0, 0, 1, 0, 1]`, MEX 2, required values 0 and 1. `prefix` starts as `[1]` (the empty prefix).

| i | value | last(0), last(1) | limit | ways | prefix |
|---:|---:|---|---:|---:|---|
| 1 | 1 | -, 1 | - | 0 | 1 |
| 2 | 0 | 2, 1 | 1 | 1 | 2 |
| 3 | 0 | 3, 1 | 1 | 1 | 3 |
| 4 | 1 | 3, 4 | 3 | 2 | 5 |
| 5 | 0 | 5, 4 | 4 | 3 | 8 |
| 6 | 1 | 5, 6 | 5 | 5 | 13 |

(Positions are 1-based here; "limit" is the latest allowed start of the last part, and `ways` is the prefix total just before it.) Answer 5.

---

Same problem grouped by topic: [../docs/dynamic-programming/MEXSUB.md](../docs/dynamic-programming/MEXSUB.md)
