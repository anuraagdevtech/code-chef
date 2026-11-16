[&larr; 632. Sardar and GCD](632-DLTNODE.md) &middot; [Index](README.md) &middot; [634. Pyramid Traversal &rarr;](634-PYRAMIDMOVES.md)

# 633. Mexy Array

> [`MEXYARR`](https://www.codechef.com/problems/MEXYARR) &middot; difficulty **2190** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Reserve constrained values until their last use and always insert the smallest allowed value |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array $B$ containing $N$ integers, each of which is either $-1$ or a non-negative integer. Construct **any** integer array $A$ of length $N$ such that:
- $0 \leq A_i \leq 10^9$ for every $1 \leq i \leq N$
- If $B_i \geq 0$, $A$ must satisfy $mex(A_1, A_2, \ldots, A_i) = B_i$
- Otherwise, $B_i = -1$, which means there is no constraint on $mex(A_1, A_2, \ldots, A_i)$

If there does not exist any array satisfying the constraints, print $-1$ instead.

**Note:** The mex of a set of non-negative integers is the smallest non-negative integer that does not belong to it. For example, $mex(1, 2, 3) = 0, mex(0, 2, 4, 1) = 3,$ and $mex(0, 0, 0) = 1$.

**Input**

- The first line of input contains an integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- The first line of each testcase contains a single integer $N$.
- The second line of each testcase contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

**Output**

For each testcase, output the required answer on a new line: $-1$ if no valid array exists, or $N$ space-separated integers denoting the elements of **any** valid array $A$. The elements of $A$ must satisfy $0 \leq A_i \leq 10^9$.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $-1 \leq B_i \leq 10^5$
- The sum of $N$ across all testcases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
2
7
0 -1 2 -1 5 -1 -1
3
2 -1 -1
```

**Sample output**

```
1 3 0 4 2 6 5
-1
```

<details><summary>Explanation</summary>

**Test case $1$:** We have $A = [1, 3, 0, 4, 2, 6, 5]$. Let $C_i = mex(A_1, A_2, \ldots, A_i)$. Then, it can be seen that $C = [0, 0, 2, 2, 5, 5, 7]$, which matches $B$ at all positions where $B_i \geq 0$.

**Test case $2$:** It can be shown that no array $A$ exists that satisfies the given constraints.

</details>

## Approach

If $B_i = v$, the value $v$ must not occur among the first $i$ elements. So a value that appears as a constraint is *reserved* up to the last index at which it is required; before that it may not be placed at all.

Among the values that may be placed, inserting the smallest one is always best: it pushes the mex up as fast as possible, and a prefix mex can never go down, so being as far ahead as the reservations allow never hurts - reserved values act as hard ceilings that keep the mex from overshooting a pending constraint.

So keep a min-heap of the currently allowed values, initially all values in $[0, N]$ that are never required. At each position pop the smallest, append it, advance the running mex, and compare it with $B_i$ if that is not $-1$. If position $i$ is the last occurrence of $B_i$, release that value into the heap. Any mismatch means no valid array exists.

## Solution

```python
import sys
import heapq


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        required = [next(tokens) for _ in range(n)]
        last = {want: i for i, want in enumerate(required) if want >= 0}
        available = [want for want in range(n + 1) if want not in last]
        heapq.heapify(available)
        seen = bytearray(n + 2)
        mex = 0
        result = []
        ok = True
        for i, want in enumerate(required):
            value = heapq.heappop(available)
            result.append(value)
            seen[value] = 1
            while seen[mex]:
                mex += 1
            if want >= 0 and want != mex:
                ok = False
            if want >= 0 and last[want] == i:
                heapq.heappush(available, want)
        out.append(' '.join(map(str, result)) if ok else '-1')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $B_1$ can only be 0 or 1 (or $-1$).
- A required mex larger than the position index is impossible and shows up as a mismatch.
- Requirements that decrease from left to right are impossible, because the mex never decreases.
- Any valid array is accepted, so the output is checked rather than compared.

## Dry run

`B = [0, -1, 2, -1, 5, -1, -1]`. Reserved: 0 (until index 1), 2 (until index 3), 5 (until index 5). Allowed at the start: `1 3 4 6 7`.

| index | insert | mex | required | released |
|---:|---:|---:|---:|---|
| 1 | 1 | 0 | 0 | 0 |
| 2 | 0 | 2 | - | |
| 3 | 3 | 2 | 2 | 2 |
| 4 | 2 | 4 | - | |
| 5 | 4 | 5 | 5 | 5 |
| 6 | 5 | 6 | - | |
| 7 | 6 | 7 | - | |

Output `1 0 3 2 4 5 6`.

---

Same problem grouped by topic: [../docs/greedy/MEXYARR.md](../docs/greedy/MEXYARR.md)
