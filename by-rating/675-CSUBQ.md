[&larr; 674. Candies](674-CANDIES3.md) &middot; [Index](README.md) &middot; [676. Two Piles &rarr;](676-SPLITMIN.md)

# 675. Chef and Subarray Queries

> [`CSUBQ`](https://www.codechef.com/problems/CSUBQ) &middot; difficulty **2345** &middot; time limit **1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Segment tree counting all-good subarrays, used at two thresholds |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((N + Q) \log N)$ |
| **Space** | $O(N)$ in packed arrays |

## Question

Chef has an array **A** consisting of **N** non-negative integers. Initially, all the elements are zero. Assume 1-based indexing. Chef is given two positive integers **L** and **R**. **(L <= R)** Chef has to execute **Q** number of queries on the array **A**. These queries can be of the following two types:

**1 x y (1 ≤ x ≤ n)** - Replace the value of **xth** array element by **y**.

**2 l r (1 ≤ l ≤ r ≤ n)** - Return the number of subarrays **[a , b]** that lies in subarray **[l , r]** such that the value of the maximum array element in that subarray is atleast **L** and atmost **R**.

         (A subarray **[a , b]** lies in a subarray **[l , r]** if and only if **a >= l** and **b <= r**)

Since, Chef couldn't solve this task, can you please help him solve this task?

**Input**

The first line contains four space separated positive integers **N, Q, L** and **R** denoting the total number of elements in an array, total number of queries, value of **L**, and value of **R** respectively.

Each of the next **Q** lines contains one of the two queries described above.

**Output**

For each query of type 2, print the required answer in a new line.

**Constraints**

**1 ≤ N, Q ≤ 5 * 10^5
**
**1 ≤ L ≤ R ≤ 10^9
**
**1 ≤ l ≤ r ≤ N
**
**1 ≤ x ≤ N
**
**1 ≤ y ≤ 10^9
**

**Subtasks**

**Subtask #1** (10 points) : 1 ≤ N , Q ≤ 100

**Subtask #2** (15 points) : 1 ≤ N , Q ≤ 5000

**Subtask #3** (27 points) : 1 ≤ Q ≤ 10^4

**Subtask #4** (48 points) : Original Constraints

## Constraints

1 ≤ N, Q ≤ 5 * 10^5
1 ≤ L ≤ R ≤ 10^9
1 ≤ l ≤ r ≤ N
1 ≤ x ≤ N
1 ≤ y ≤ 10^9

## Sample

**Sample input**

```
5 6 1 10
1 1 2
2 1 5 
1 3 11
1 4 3
2 3 5
2 1 5
```

**Sample output**

```
5
2
4
```

<details><summary>Explanation</summary>

**Query 1.**

 A = {0, 0, 0, 0, 0}

After replacing value of 1st element by 2,

A = {2, 0, 0, 0, 0}

**Query 2.**

A = {2, 0, 0, 0, 0}

All the subarrays that lies in a subarray [1 , 5] whose maximum value is atleast 1 and atmost 10 are -

 [1 , 1], [1 , 2], [1 , 3], [1 , 4] and [1 , 5]. Thus the answer is 5.

**Query 3.**

A = {2, 0, 0, 0, 0}

After replacing value of 3rd element by 11,

A = {2, 0, 11, 0, 0}

**Query 4.**

A = {2, 0, 11, 0, 0}

After replacing value of 4th element by 3,

A = {2, 0, 11, 3, 0}

**Query 5.**

A = {2, 0, 11, 3, 0}

All the subarrays that lies in a subarray [3 , 5] whose maximum value is atleast 1 and atmost 10 are -

 [4 , 4] and [4 , 5]. Thus the answer is 2.

**Query 6.**

A = {2, 0, 11, 3, 0}

All the subarrays that lies in a subarray [1 , 5] whose maximum value is atleast 1 and atmost 10 are -

 [1 , 1], [1 , 2], [4 , 4] and [4 , 5]. Thus the answer is 4.

</details>

## Approach

The maximum of a subarray lies in $[L, R]$ exactly when all elements are $\le R$ but not all are $\le L - 1$. So

$$\text{answer} = \#\{\text{subarrays with all elements} \le R\} - \#\{\text{subarrays with all elements} \le L - 1\}.$$

Each of the two counts is a classic segment-tree monoid. Mark an element good if it is within the threshold. A node stores its length, the length of its good prefix, the length of its good suffix and the number of all-good subarrays inside it. Merging two children adds their counts plus (good suffix of the left) $\times$ (good prefix of the right) for the subarrays crossing the middle; the prefix extends into the right child only if the left child is entirely good, and symmetrically for the suffix.

A point update recomputes one leaf-to-root path for both thresholds; a range query combines the $O(\log N)$ covering nodes from the left and from the right, keeping the order of the pieces.

## Solution

```python
import sys
from array import array


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, q, low, high = (next(tokens) for _ in range(4))
    size = 1
    while size < n:
        size *= 2
    length = array('I', [0]) * (2 * size)
    for i in range(size, size + n):
        length[i] = 1
    for i in range(size - 1, 0, -1):
        length[i] = length[i * 2] + length[i * 2 + 1]
    prefix_good = [array('I', length), array('I', length)]
    suffix_good = [array('I', length), array('I', length)]
    count = [array('Q', [0]) * (2 * size), array('Q', [0]) * (2 * size)]
    for z in range(2):
        for i in range(1, 2 * size):
            count[z][i] = length[i] * (length[i] + 1) // 2
    out = []
    for _ in range(q):
        kind, x, y = (next(tokens), next(tokens), next(tokens))
        if kind == 1:
            leaf = size + x - 1
            for z, bound in enumerate((high, low - 1)):
                good = int(y <= bound)
                prefix_good[z][leaf] = suffix_good[z][leaf] = count[z][leaf] = good
                i = leaf // 2
                pre_z, suf_z, cnt_z = (prefix_good[z], suffix_good[z], count[z])
                while i:
                    a, b = (i * 2, i * 2 + 1)
                    pre_z[i] = pre_z[a] + (pre_z[b] if pre_z[a] == length[a] else 0)
                    suf_z[i] = suf_z[b] + (suf_z[a] if suf_z[b] == length[b] else 0)
                    cnt_z[i] = cnt_z[a] + cnt_z[b] + suf_z[a] * pre_z[b]
                    i //= 2
        else:
            results = []
            for z in range(2):
                l, r = (size + x - 1, size + y)
                ll = lp = ls = lc = 0
                rl = rp = rs = rc = 0
                pre_z, suf_z, cnt_z = (prefix_good[z], suffix_good[z], count[z])
                while l < r:
                    if l & 1:
                        lc += cnt_z[l] + ls * pre_z[l]
                        lp += pre_z[l] if lp == ll else 0
                        ls = suf_z[l] + (ls if suf_z[l] == length[l] else 0)
                        ll += length[l]
                        l += 1
                    if r & 1:
                        r -= 1
                        rc = cnt_z[r] + rc + suf_z[r] * rp
                        rs += suf_z[r] if rs == rl else 0
                        rp = pre_z[r] + (rp if pre_z[r] == length[r] else 0)
                        rl += length[r]
                    l //= 2
                    r //= 2
                results.append(lc + rc + ls * rp)
            out.append(str(results[0] - results[1]))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- All elements start at 0, which is good for both thresholds when $L \ge 1$, so the trees start fully good.
- The merge is not commutative; left-side and right-side partial results are accumulated separately.
- Counts are about $N^2 / 2$, so 64-bit storage is used.
- An update that leaves the element's status unchanged is still processed safely.

## Dry run

`N = 5, L = 1, R = 10`.

After `A = [2, 0, 0, 0, 0]`, query `[1, 5]`: all five elements are $\le 10$, giving $5 \cdot 6 / 2 = 15$ subarrays. Elements $\le 0$ are positions 2-5, a run of 4, giving $4 \cdot 5 / 2 = 10$.

Answer $15 - 10 = 5$ - the subarrays that contain position 1.

---

Same problem grouped by topic: [../docs/trees/CSUBQ.md](../docs/trees/CSUBQ.md)
