[&larr; 670. Make that Array!](670-SWAPGAME.md) &middot; [Index](README.md) &middot; [672. Potato to Gold &rarr;](672-SIMPLEARRAY.md)

# 671. Ancient Berland Roads

> [`ABROADS`](https://www.codechef.com/problems/ABROADS) &middot; difficulty **2324** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Disjoint Set Union |
| **Technique** | Process the queries backwards - deletions become unions |
| **CodeChef tags** | `Advanced Data Structures`, `Disjoint Set Union` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((N + M + Q) \log (N + M + Q))$ |
| **Space** | $O(N + M + Q)$ |

## Question

In Ancient Berland, there were **N** towns, along with **M** bidirectional roads connecting them. With time, some roads became unusable, and nobody repaired them.

As a person who is fond of Ancient Berland history, you now want to undertake a small research study. For this purpose, you want to write a program capable of processing the following kinds of queries:

- <tt>D</tt>** K** : meaning that the road numbered **K** in the input became unusable. The road numbers are 1-indexed.

- <tt>P</tt>** A x** : meaning that the population of the **A**^th town became **x**.

Let's call a subset of towns a **region** if it is possible to get from each town in the subset to every other town in the subset by the usable (those, which haven't already been destroyed) roads, possibly, via some intermediary cities of this subset. The **population** of the region is, then, the sum of populations of all the towns in the region.

You are given the initial road system, the initial population in each town and **Q** queries, each being one of two types above. Your task is to maintain the size of the most populated region after each query.

**Input**

The first line of each test case contains three space-separated integers — **N**, **M**, and **Q** — denoting the number of cities, the number of roads, and the number of queries, respectively.

The following line contains **N** space-separated integers, the **i**^th of which denotes the initial population of the **i**^th city.

The **j**^th of the following **M** lines contains a pair of space-separated integers — **X_j, Y_j** — denoting that there is a bidirectional road connecting the cities numbered **X_j** and **Y_j**.

Each of the following **Q** lines describes a query in one of the forms described earlier.

**Output**

Output **Q** lines. On the **i**^th line, output the size of the most populated region after performing **i** queries.

**Constraints**

- **1** ≤ **X_j**, **Y_j** ≤ **N**

- Roads' numbers are 1-indexed.

- There is no road that gets removed twice or more.

- **1** ≤ **P_i** ≤ **10^5**

- Subtask 1 (30 points) : **1** ≤ **N**, **M**, **Q** ≤ **10^3**

- Subtask 2 (70 points) : **1** ≤ **N**, **M**, **Q** ≤ **5 × 10^5**

**Example**

```
**Input:**
<tt>3 3 6
1 2 3
1 2
2 3
3 1
P 1 3
D 1
P 2 3
D 2
P 3 10
D 3</tt>

**Output:**
<tt>8
8
9
6
13
10</tt>
```

**Explanation**

- After the first query, the populations are **(3, 2, 3)** and the most populated region is **{1, 2, 3}**.

- After the second query the populations and the regions remain the same.

- After the third query the populations are **(3, 3, 3)** and the most populated region is again **{1, 2, 3}**.

- After the fourth query the populations remain the same, but we have two regions: **{1, 3}** and **{2}**. The most populated region is **{1, 3}**.

- After the fifth query the populations become equal to **(3, 3, 10)** respectively, and the most populated region is again **{1, 3}**.

- After the last query we have populations the same, but now every city forms it own separate region, and the most populated region is region **{3}**.

## Constraints

- 1 ≤ X_j, Y_j ≤ N
- Roads' numbers are 1-indexed.
- There is no road that gets removed twice or more.
- 1 ≤ P_i ≤ 10^5
- Subtask 1 (30 points) : 1 ≤ N, M, Q ≤ 10^3
- Subtask 2 (70 points) : 1 ≤ N, M, Q ≤ 5 × 10^5

## Approach

A disjoint-set union can merge but not split, so read all queries first and answer them in reverse.

Forward pass over the input: for a `P` query remember the old population before overwriting it; for a `D` query mark the road as removed. Afterwards build the DSU of the final state: the final populations and all roads that were never removed, with the total population stored at each root.

Backward pass: the state before undoing query $i$ is the state right after it, so first record the current maximum region population as the answer to query $i$, then undo it - a `D` becomes a union of the road's endpoints, a `P` restores the old population by adjusting the sum at the town's root.

The maximum is kept in a max-heap of (sum, root) with lazy deletion: every time a root's sum changes a new entry is pushed, and entries whose vertex is no longer a root or whose sum is outdated are discarded when they reach the top.

## Solution

```python
import sys
import heapq


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    n, m, query_count = (int(next(tokens)), int(next(tokens)), int(next(tokens)))
    population = [int(next(tokens)) for _ in range(n)]
    edges = [(int(next(tokens)) - 1, int(next(tokens)) - 1) for _ in range(m)]
    removed = set()
    queries = []
    for _ in range(query_count):
        kind = next(tokens)
        u = int(next(tokens)) - 1
        if kind == b'D':
            removed.add(u)
            queries.append((0, u, 0))
        else:
            x = int(next(tokens))
            queries.append((1, u, population[u]))
            population[u] = x
    parent = list(range(n))
    size = [1] * n
    region = population.copy()
    heap = []

    def root(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def join(u, v):
        u, v = (root(u), root(v))
        if u == v:
            return
        if size[u] < size[v]:
            u, v = (v, u)
        parent[v] = u
        size[u] += size[v]
        region[u] += region[v]
        heapq.heappush(heap, (-region[u], u))
    for i, (u, v) in enumerate(edges):
        if i not in removed:
            join(u, v)
    for i in range(n):
        if parent[i] == i:
            heapq.heappush(heap, (-region[i], i))
    out = []
    for kind, u, old in reversed(queries):
        while parent[heap[0][1]] != heap[0][1] or -heap[0][0] != region[heap[0][1]]:
            heapq.heappop(heap)
        out.append(str(-heap[0][0]))
        if kind:
            r = root(u)
            region[r] += old - population[u]
            population[u] = old
            heapq.heappush(heap, (-region[r], r))
        else:
            join(*edges[u])
    print('\n'.join(reversed(out)))


if __name__ == "__main__":
    main()
```

## Edge cases

- A road is removed at most once; undoing joins two components or does nothing if they are already joined.
- Population updates can lower a region's total, which is why stale heap entries must be validated.
- Answers are produced in reverse and printed in the original order.
- The query type is a letter, so the input is tokenised as bytes rather than integers.

## Dry run

Towns `1 2 3` with roads `1-2, 2-3, 3-1`; queries `P 1 3`, `D 1`, `P 2 3`, `D 2`, `P 3 10`, `D 3`.

Final state: populations `3 3 10`, no roads; maximum 10 (answer to query 6).

Undo backwards: add road `3-1` -> regions `{1,3} = 13`, `{2} = 3` (answer 13 for query 5); restore town 3 to 3 -> `{1,3} = 6` (answer 6); add road `2-3` -> one region of 9 (answer 9); restore town 2 to 2 -> 8 (answer 8); add road `1-2` -> still 8 (answer 8).

Output `8 8 9 6 13 10`.

---

Same problem grouped by topic: [../docs/disjoint-set-union/ABROADS.md](../docs/disjoint-set-union/ABROADS.md)
