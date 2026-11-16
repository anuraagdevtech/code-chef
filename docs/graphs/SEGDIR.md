[&larr; 528. Fence - INOI 2017](TINOI17A.md) &middot; [Index](../../README.md) &middot; [533. Tourists in Mancunia &rarr;](TOURISTS.md)

# 530. Moving Segments

> CodeChef problem code [`SEGDIR`](https://www.codechef.com/problems/SEGDIR) &middot; difficulty **1940** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Two-colour equal-speed interval overlaps by maximum depth |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

$N$ line segments (numbered $1$ through $N$) are placed on the $x$-axis. For each valid $i$, the $i$-th segment starts at $x = L_i$ and ends at $x = R_i$.

At the time $t = 0$, all segments start moving; for each valid $i$, the $i$-th segment starts moving with speed $V_i$. You need to assign a direction - left or right - to the movement of each segment, i.e. choose a sign for each $V_i$ (not necessarily the same for all segments). The resulting movement must satisfy the following condition: at the time $t = 10^{10000}$, there are no two segments that touch or intersect.

Decide if it is possible to assign directions to the segments in such a way that the above condition is satisfied.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains three space-separated integers $L_i$, $R_i$ and $V_i$.

**Output**
For each test case, print a single line containing the string `"YES"` if it is possible to assign the directions in a valid way or `"NO"` if it is impossible.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le L_i \lt R_i \le 10^9$ for each valid $i$
- $1 \le V_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2,000$

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 1,000$
- $1 \le L_i \lt R_i \le 10^9$ for each valid $i$
- $1 \le V_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2,000$

## Sample

**Sample input**

```
2
4
5 7 2
4 6 1
1 5 2
6 8 1
4
1 2 1
1 2 1
1 2 1
1 2 1
```

**Sample output**

```
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:** We can assign the direction *left* to the $1$-st and $2$-nd segment and *right* to the $3$-rd and $4$-th segment.

**Example case 2:** There is no valid way to assign directions to segments.

</details>

## Approach

At the enormous target time, different speed magnitudes are separated regardless of their assigned signs. Only intervals with equal speeds and equal directions can still overlap. Therefore each speed group must be divided into two classes of pairwise disjoint closed intervals.

For intervals, two such classes exist exactly when no point belongs to three intervals. Sort each speed group by left endpoint and maintain a min-heap of active right endpoints. Remove endpoints strictly less than the next left endpoint, since touching is forbidden. If two intervals remain active before inserting another, three overlap and assignment is impossible.

## Solution (Python)

```python
import sys
from collections import defaultdict
from heapq import heappush, heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        groups = defaultdict(list)
        for _ in range(n):
            left,right,speed = (int(next(tokens)) for _ in range(3))
            groups[speed].append((left,right))
        possible = True
        for intervals in groups.values():
            active = []
            for left,right in sorted(intervals):
                while active and active[0] < left:
                    heappop(active)
                if len(active) >= 2:
                    possible = False
                    break
                heappush(active,right)
            if not possible:
                break
        out.append('YES' if possible else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N\log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Touching endpoints count as an overlap.
- Different speeds impose no final-time constraint.
- More than two intervals may share a speed if their overlaps form only depth two.

## Dry run

The second sample has four identical intervals of the same speed. Three already overlap at every point, so two directions cannot separate them and the answer is `NO`.

---

Same problem in rating order (#556 of 735): [../../by-rating/556-SEGDIR.md](../../by-rating/556-SEGDIR.md)
