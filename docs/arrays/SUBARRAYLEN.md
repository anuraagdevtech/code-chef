[&larr; 412. OR Matrix](ORMATRIX.md) &middot; [Index](../../README.md) &middot; [453. Matchsticks &rarr;](MSTICK.md)

# 433. Subarrays with length

> CodeChef problem code [`SUBARRAYLEN`](https://www.codechef.com/problems/SUBARRAYLEN) &middot; difficulty **1691** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Grouping by length, then a union of intervals |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an array $A$ of length $N$.

Determine the count of subarrays of $A$ which contain their length as an element.

Formally, count the number of pairs $(L, R)$ $(1\le L\le R\le N)$ such that: $(R-L+1) \in \{A_L, A_{L+1}, \ldots, A_R\}$.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- First line of each test case contains an integer $N$ denoting the length of the array $A$.
- Second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - denoting the array $A$.

**Output**

For each test case, output the count of subarrays containing their lengths.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq N$
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
3
1 2 1
5
2 3 1 3 5
10
10 7 4 4 2 9 2 1 9 3
```

**Sample output**

```
4
6
15
```

<details><summary>Explanation</summary>

**Test Case $1$:** There are $4$ subarrays $(i,j)$ containing their lengths. They are $(1,1), (1,2), (2,3),$ and $(3,3)$.

**Test Case $2$:** There are $6$ subarrays $(i,j)$ containing their lengths. They are $(1,2), (1,3), (1,5), (2, 4), (3,3),$ and $(3,5)$.

</details>

## Approach

Counting per subarray invites double counting, since a window may contain several elements equal to its own length. Group by **length** instead.

Fix a length $\ell$ and let $p_1 < \cdots < p_m$ be the positions holding the value $\ell$. A window of length $\ell$ is determined by its left end $L \in [1, N-\ell+1]$, and it contains position $p$ exactly when

$$L \in [\,p - \ell + 1,\ p\,]$$

So the valid left ends form a **union of $m$ intervals**, each clipped to the legal range, and the count for this length is the size of that union. Because the $p_j$ are increasing, so are the intervals, and merging them is a single sweep that tracks the furthest left end already used.

Summing over all $\ell$ costs $O(N)$ in total — each position appears in exactly one length's list — and the union handles overlaps exactly once, which is what the direct per-element count gets wrong.

$$\text{answer} = \sum_{\ell=1}^{N} \left|\ \bigcup_{j} \bigl[\max(1, p_j - \ell + 1),\ \min(p_j, N-\ell+1)\bigr]\ \right|$$

Lengths with no matching value contribute nothing, and an interval can come out empty after clipping — for instance a value $\ell$ sitting too near the array's start to anchor a window of that length.

The second sample, $[2,3,1,3,5]$, totals $6$: length $3$ alone contributes $3$, because the two threes at positions $2$ and $4$ give the overlapping ranges $[1,2]$ and $[2,3]$, whose union is $[1,3]$ — counting them separately would give $4$ and overcount the window starting at $2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        spots = [[] for _ in range(n + 1)]
        for i in range(n):
            spots[int(data[pos + 1 + i])].append(i + 1)
        pos += 1 + n
        total = 0
        for length in range(1, n + 1):
            last = 0          # rightmost left-end already counted
            for p in spots[length]:
                lo = max(1, p - length + 1, last + 1)
                hi = min(p, n - length + 1)
                if hi >= lo:
                    total += hi - lo + 1
                    last = hi
            # Intervals arrive sorted, so "last" merges the overlaps in place.
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Group the positions by value, then by the length they license.** A position $p$ holding the value $\ell$ makes every subarray of length $\ell$ that covers $p$ a hit, which is the interval of left ends $[\max(1, p - \ell + 1),\, \min(p, N - \ell + 1)]$.
- **Overlaps must not be double-counted.** Two positions holding the same value license overlapping ranges of left ends, so a running `last` tracks the rightmost left end already counted and clips the next interval.
- **The positions arrive in increasing order**, which is why one pointer suffices instead of a full interval-union pass.
- **The upper clip $N - \ell + 1$ matters**, since a subarray of length $\ell$ cannot start so late that it runs off the end.
- **The lower clip at $1$ matters** for positions near the front, where $p - \ell + 1$ goes non-positive.
- **A value exceeding $N$ would license nothing**, but $A_i \leq N$ is guaranteed so every value indexes a real length.
- **Sum of $N \leq 5 \cdot 10^5$**: the work is linear overall, since each position is visited once inside its own length's bucket.

## Dry run

First sample: $A = 1, 2, 1$.

| length | positions holding it | left-end interval | counted | running total |
|---:|---|---|---:|---:|
| 1 | $p = 1$ | $[1, 1]$ | 1 | 1 |
| 1 | $p = 3$ | $[3, 3]$ | 1 | 2 |
| 2 | $p = 2$ | $[1, 2]$ | 2 | 4 |
| 3 | none | — | 0 | 4 |

Output `4`: the subarrays are $[1]$, $[1]$ (the third element), $[1,2]$ and $[2,1]$.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#401 of 486): [../../by-rating/401-SUBARRAYLEN.md](../../by-rating/401-SUBARRAYLEN.md)
