# 327. Forest Gathering

> CodeChef problem code [`FORESTGA`](https://www.codechef.com/problems/FORESTGA) &middot; difficulty **1829** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Searching time on a monotonic yield |
| **Time** | $O(N \log(\text{months}))$ |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Chef is the head of commercial logging industry that recently bought a farm containing **N** trees. You are given initial height of the i-th tree by **H_i** and the rate of growth of height as **R_i** meters per month. For simplicity, you can assume that all the trees are perfect cylinders of equal radius. This allows us to consider only the height of trees when we talk about the amount of wood.

In Chef's country, laws don't allow one to cut a tree partially, so one has to cut the tree completely for gathering wood. Also, laws prohibit cutting trees of heights (strictly) lower than **L** meters.

Today Chef received an order of **W** meters (of height) of wood. Chef wants to deliver this order as soon as possible. Find out how minimum number of months he should wait after which he will able to fulfill the order. You can assume that Chef's company's sawing machines are very efficient and take negligible amount of time to cut the trees.

**Input**

There is a single test case per test file.

The first line of the input contains three space separated integers **N**, **W** and **L** denoting the number of trees in the farm, the amount of wood (in meters) that have to be gathered and the minimum allowed height of the tree to cut.

Each of next **N** lines contain two space separated integers denoting **H_i** and **R_i** respectively.

**Output**

Output a single integer denoting the number of months that have to pass before Chef will be able to fulfill the order.

**Constraints**

- **1** ≤ **N** ≤ **10^5**

- **1** ≤ **W**, **L** ≤ **10^18**

- **1** ≤ **H_i**, **R_i** ≤ **10^9**

**Subtasks**

- **Subtask #1 [40 points]:** **1 ≤ ** **N**, **W**, **L** ≤ **10^4**

- **Subtask #2 [60 points]:** No additional constraints

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ W, L ≤ 10^18
- 1 ≤ H_i, R_i ≤ 10^9

## Sample

**Sample input**

```
3 74 51
2 2
5 7
2 9
```

**Sample output**

```
7
```

<details><summary>Explanation</summary>

After **6** months, heights of each tree will be **14**, **47** and **56** respectively. Chef is allowed to cut only the third tree, sadly it is not enough to fulfill an order of 74 meters of wood.

After **7** months, heights of each tree will be **16**, **54** and **65** respectively. Now Chef is allowed to cut second and third trees. Cutting both of them would provide him **119** meters of wood, which is enough to fulfill the order.

</details>

## Approach

After $m$ months tree $i$ stands at $H_i + R_i m$, and it may be cut only once that reaches the legal minimum $L$. So the harvest available at month $m$ is

$$f(m) = \sum_{i \,:\, H_i + R_i m \,\geq\, L} \bigl(H_i + R_i m\bigr)$$

$f$ is **non-decreasing** in $m$ for two reinforcing reasons: every already-legal tree keeps growing, and trees only ever *enter* the legal set, never leave it. That monotonicity is what licenses binary search on the answer — find the smallest $m$ with $f(m) \geq W$.

The search bound needs care. With $W$ up to $10^{18}$ and a single tree growing at $R = 1$, the answer can itself approach $10^{18}$, so the upper limit must be set around $2 \times 10^{18}$ rather than something comfortable like $10^9$. Each probe is one $O(N)$ pass, and roughly $61$ probes cover that range.

Note the legality test uses the **tree's own height**, not the total — a short fast-growing tree contributes nothing until it individually clears $L$.

The sample makes that concrete: with $L = 51$ and $W = 74$, at month $6$ the trees stand at $14$, $47$ and $56$, so only the last is legal and yields $56$ — short of the order. One month later they reach $16$, $54$ and $65$; two are now legal and together give $119$. So the answer is $7$, and the jump from $56$ to $119$ comes from a tree *becoming* harvestable rather than merely growing.

There is **no $T$**: the file holds a single test case.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    # Single test case: N, W, L then N pairs.
    n, w, l = int(data[0]), int(data[1]), int(data[2])
    trees = [(int(data[3 + 2 * i]), int(data[4 + 2 * i])) for i in range(n)]

    def harvest(months):
        total = 0
        for h, r in trees:
            height = h + r * months
            if height >= l:          # legality is per tree, not per total
                total += height
                if total >= w:       # early exit keeps the probe cheap
                    return total
        return total

    # Yield only ever grows, so binary search the first month that suffices.
    lo, hi = 0, 2 * 10 ** 18
    while lo < hi:
        mid = (lo + hi) // 2
        if harvest(mid) >= w:
            hi = mid
        else:
            lo = mid + 1
    print(lo)


main()
```

## Complexity

- **Time:** $O(N \log(\text{months}))$
- **Space:** $O(N)$
