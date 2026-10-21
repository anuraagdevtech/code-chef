# 470. ChefTown Parade

> [`CHEFTOWN`](https://www.codechef.com/problems/CHEFTOWN) &middot; difficulty **1882** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Sliding-window maximum and minimum with deques |
| **CodeChef tags** | `Data Structures`, `Queues`, `Mathematics`, `Deque`, `Basic Math` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ |
| **Space** | $O(N)$ |

## Question

ChefTown is the biggest city and the capital of ChefLand. There are N beautiful buildings: restaurants, museums, living houses with large kitchens and so on. Every building has its height. For every i (1<=i<=N) there is exactly one building with height i. The buildings are located in a single line from left to right. The height of ith building is H(i). The Mayor of ChefTown wants to organize a parade, where all great chefs will take part. A parade depends of its location. The location of a parade is a segment of consecutive buildings beginning near the building number L and ending near the building number R (1<=L<=R<=N). Any parade won't be interesting if it is not hold on an interesting segment of buildings. The segment of buildings is interesting if following are hold:

- Imagine, that we have a segment [L,R].

- Let K=R-L+1 be the length of this segment, and B be a list of heights of the buildings that belong to this segment.

- Let's sort B in non-decreasing order.

- Segment [L,R] is interesting if B[i]-B[i-1]=1 for every i (2<=i<=K).

Now the Mayor of ChefTown is interested how many ways to organize an interesting parade of length W for ChefTown citizens. Help him and find out the number of different parades of length W, which can be hold in the city. Two parades ([L1,R1] and [L2,R2]) are considered to be different, if L1≠L2 or R1≠R2.

**Input**

 Each input file consists of two lines, the first one contains two integers N and W (1<=N<=400000, 1<=W<=N). The second line contains N numbers H(i) (1<=i<=N) - the heights of the buildings.

**Output**

For each test case output a single integer - the number of interesting segments of buildings of length W.

## Constraints

- $1 \leq N \leq 400000$
- $1 \leq W \leq N$
- $H$ is a permutation of $1 \ldots N$: for every $i$ there is exactly one building of height $i$
- the input holds a single case (there is no leading $T$)

## Sample

**Sample 1 input**

```
2 1
2 1
```

**Sample 1 output**

```
2
```

**Sample 2 input**

```
4 2
1 2 3 4
```

**Sample 2 output**

```
3
```

## Approach

The heights are a **permutation** of $1 \ldots N$, and that single fact replaces the whole sorting-and-comparing definition. A window of length $W$ therefore holds $W$ *distinct* values, and $W$ distinct integers are consecutive exactly when their span is $W - 1$:

$$\max - \min = W - 1$$

($\geq W-1$ always holds for $W$ distinct integers, and equality forces every value in $[\min, \max]$ to be present.) So the task is: slide a window of length $W$ and count the positions where its span is $W - 1$.

Both window extremes come from **monotonic deques**. For the maximum, hold indices whose values are strictly decreasing: before pushing index $i$, pop from the back every index whose value is $\leq H_i$, since a smaller value that is also older can never be the maximum again. Pop from the front once it falls out of the window. The minimum is the mirror image, with an increasing deque. Each index enters and leaves each deque once, so the sweep is linear rather than the $O(N \log N)$ a heap or balanced tree would cost — which matters at $N = 4 \times 10^5$.

Note the input format is unusual for CodeChef: there is **no leading $T$**, just $N$ and $W$ followed by the heights.

In the sample $N = 2$ and $W = 1$. Every single-element window trivially has span $0 = W - 1$, so both positions count and the answer is $2$. The degenerate $W = 1$ case needs no special handling — the formula covers it.

## Solution

```python
import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, w = int(data[0]), int(data[1])
    h = [int(x) for x in data[2:2 + n]]
    hi, lo = deque(), deque()      # indices, values decreasing / increasing
    count = 0
    for i in range(n):
        while hi and h[hi[-1]] <= h[i]:
            hi.pop()
        hi.append(i)
        while lo and h[lo[-1]] >= h[i]:
            lo.pop()
        lo.append(i)
        left = i - w + 1
        if left < 0:
            continue
        if hi[0] < left:
            hi.popleft()
        if lo[0] < left:
            lo.popleft()
        # W distinct values span W - 1 only when they are consecutive.
        if h[hi[0]] - h[lo[0]] == w - 1:
            count += 1
    sys.stdout.write(f"{count}\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/CHEFTOWN.md](../docs/arrays/CHEFTOWN.md)
