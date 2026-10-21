# 474. Lowest Sum

> [`LOWSUM`](https://www.codechef.com/problems/LOWSUM) &middot; difficulty **2302** &middot; time limit **3.5s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Heaps |
| **Technique** | $k$ smallest pairwise sums |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(K \log K + n \log n)$ per test case, where $n = \max q_i$ |
| **Space** | $O(n)$ |

## Question

** Read problems statements in Russian [here](https://www.codechef.com/download/translated/COOK40/russian/LOWSUM.pdf)**

The Head Chef is studying the motivation and satisfaction level of his chefs . The motivation and satisfaction of a Chef can be represented as an integer . The Head Chef wants to know the ** N ** th smallest sum of one satisfaction value and one motivation value for various values of ** N ** . The satisfaction and motivation values may correspond to the same chef or different chefs . Given two arrays, the first array denoting the motivation value and the second array denoting the satisfaction value of the chefs . We can get a set of sums(add one element from the first array and one from the second). For each query ( denoted by an integer q_i ( i = 1 to Q ) , Q denotes number of queries ) , find the q_i th element in the set of sums ( in non-decreasing order ) .

**Input**

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a two space seperated integers **K** and **  Q ** denoting the number of chefs and the number of queries .

 - The second line of each test case contains **K** space-separated integers **A_1**, **A_2**, ..., **A_K** denoting the motivation of Chefs.

- The third line of each test case contains **K** space-separated integers **B_1**, **B_2**, ..., **B_K** denoting the satisfaction of Chefs.

-  The next Q lines contain a single integer q_i ( for i = 1 to Q ) , find the q_i th element in the set of sums .

**Output**

- For each query of each test case, output a single line containing the answer to the query of the testcase

**Constraints**

Should contain all the constraints on the input data that you may have. Format it like:

- **1** ≤ **T** ≤ **5**

- **1** ≤ **K** ≤ **20000**

- **1** ≤ **Q** ≤ **500**

- **1** ≤ **q_i ( for i = 1 to Q ) ** ≤ **10000**

- **1** ≤ **A_i** ≤ **10^18  ( for i = 1 to K ) **

- **1** ≤ **B_i  ** ≤ **10^18 ( for i = 1 to K ) **

## Constraints

- $1 \leq T \leq 5$
- $1 \leq K \leq 20000$
- $1 \leq Q \leq 500$
- $1 \leq q_i \leq 10000$ (for $i = 1$ to $Q$)
- $1 \leq A_i \leq 10^{18}$ (for $i = 1$ to $K$)
- $1 \leq B_i \leq 10^{18}$ (for $i = 1$ to $K$)

## Sample

**Sample input**

```
1
3 1
1 2 3
4 5 6
4
```

**Sample output**

```
7
```

<details><summary>Explanation</summary>

There are 9 elements in the set of sums :

1 + 4 = 5

2 + 4 = 6

1 + 5 = 6

1 + 6 = 7

2 + 5 = 7

3 + 4 = 7

2 + 6 = 8

3 + 5 = 8

3 + 6 = 9

The fourth smallest element is 7.

</details>

## Approach

The set of candidate sums is the full $K \times K$ grid $A_i + B_j$, which is up to $4 \times 10^8$ entries — far too many to materialise. But the queries ask only for ranks up to $10^4$, and that caps the work twice over.

First, **truncation**. The $n$-th smallest sum can only use the $n$ smallest values of $A$ and the $n$ smallest of $B$: if a sum used the $(n{+}1)$-th smallest $A$ value, then swapping in each of the $n$ smaller $A$ values with the same $B$ gives $n$ strictly smaller-or-equal sums, so its rank exceeds $n$. So sort both arrays and keep only the first $m = \min(K, n)$ of each.

Second, **a frontier heap**. With both arrays sorted, each row $i$ of the grid is increasing in $j$, so the grid is $m$ sorted lists and the task is a $k$-way merge. Seed a min-heap with the head of every row, $(A_i + B_0,\, i,\, 0)$; each pop yields the next smallest sum overall and is replaced by its row's successor $(A_i + B_{j+1},\, i,\, j+1)$.

Popping $n$ times produces the sorted prefix of sums, after which every query is an array index — so all $Q$ queries of a test case share one $O(n \log m)$ pass rather than each paying for its own.

The sample has $A = [1,2,3]$ and $B = [4,5,6]$, whose nine sums sort to $5, 6, 6, 7, 7, 7, 8, 8, 9$; the $4$th is $7$. Note the repeats — rank counts a multiset, so $(1,6)$, $(2,5)$ and $(3,4)$ all occupy their own rank rather than collapsing into one.

Values reach $10^{18}$, so the sums reach $2 \times 10^{18}$; Python's unbounded integers handle this, but in C++ this needs `unsigned long long` or care with `long long`.

## Solution

```python
import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        k, q = int(data[pos]), int(data[pos + 1])
        pos += 2
        a = sorted(int(x) for x in data[pos:pos + k])
        pos += k
        b = sorted(int(x) for x in data[pos:pos + k])
        pos += k
        queries = [int(x) for x in data[pos:pos + q]]
        pos += q
        need = max(queries)
        # Rank <= need can never use anything past the need-th smallest value.
        m = min(k, need)
        a = a[:m]
        b = b[:m]
        # One head per row: the grid is m lists already sorted along j.
        heap = [(a[i] + b[0], i, 0) for i in range(m)]
        heapq.heapify(heap)
        sums = []
        while heap and len(sums) < need:
            total, i, j = heapq.heappop(heap)
            sums.append(total)
            if j + 1 < m:
                heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))
        out.extend(str(sums[v - 1]) for v in queries)
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/heaps/LOWSUM.md](../docs/heaps/LOWSUM.md)
