[&larr; 542. Lucky Sum](542-LUCKY3.md) &middot; [Index](README.md) &middot; [544. Chef and Reversing &rarr;](544-REVERSE.md)

# 543. Ciel and Tomya

> [`CIELTOMY`](https://www.codechef.com/problems/CIELTOMY) &middot; difficulty **1877** &middot; time limit **0.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Dijkstra with counts of equal shortest routes |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((N+M)\log N)$ per test case |
| **Space** | $O(N+M)$ |

## Question

Tomya is a girl. She loves Chef Ciel very much.

Today, too, Tomya is going to Ciel's restaurant.
Of course, Tomya would like to go to Ciel's restaurant as soon as possible.
Therefore Tomya uses one of the shortest paths from Tomya's house to Ciel's restaurant.
On the other hand, Tomya is boring now to use the same path many times.
So Tomya wants to know the number of shortest paths from Tomya's house to Ciel's restaurant.
Your task is to calculate the number under the following assumptions.

This town has **N** intersections and **M** two way roads.
The **i**-th road connects from the **A_i**-th intersection to the **B_i**-th intersection, and its length is

**C_i**.
Tomya's house is in the 1st intersection, and Ciel's restaurant is in the **N**-th intersection.

**Input**

The first line contains an integer **T**, the number of test cases.
Then **T** test cases follow.
The first line of each test case contains 2 integers **N**, **M**.
Then next **M** lines contains 3 integers denoting **A_i**, **B_i** and **C_i**.

**Output**

For each test case, print the number of shortest paths from Tomya's house to Ciel's restaurant.

**Constraints**

1 ≤ **T** ≤ 10

2 ≤ **N** ≤ 10

1 ≤ **M** ≤ **N ∙ (N – 1) / 2**

1 ≤ **A_i**, **B_i** ≤ **N**

1 ≤ **C_i** ≤ 10
**A_i** ≠ **B_i**

If **i** ≠ **j** and **A_i** = **A_j**, then **B_i** ≠ **B_j**

There is at least one path from Tomya's house to Ciel's restaurant.

## Constraints

1 ≤ T ≤ 10
2 ≤ N ≤ 10
1 ≤ M ≤ N ∙ (N – 1) / 2
1 ≤ A_i, B_i ≤ N
1 ≤ C_i ≤ 10
A_i ≠ B_i
If i ≠ j and A_i = A_j, then B_i ≠ B_j
There is at least one path from Tomya's house to Ciel's restaurant.

## Sample

**Sample input**

```
2
3 3
1 2 3
2 3 6
1 3 7
3 3
1 2 3
2 3 6
1 3 9
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

In the first sample, only one shortest path exists, which is 1-3.

In the second sample, both paths 1-2-3 and 1-3 are the shortest paths.

</details>

## Approach

Maintain shortest distance and number of shortest paths for each vertex. A strictly shorter relaxation replaces both the distance and the count with the predecessor's count. An equal-distance relaxation adds the predecessor's count.

All road lengths are positive, so every predecessor of a shortest path is settled before its destination. This guarantees the count is complete when that destination is processed. Counts are exact integers; the problem requests no modulus.

## Solution

```python
import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = int(next(tokens))-1,int(next(tokens))-1,int(next(tokens))
            graph[u].append((v,w))
            graph[v].append((u,w))
        distance = [10**30]*n
        ways = [0]*n
        distance[0] = 0
        ways[0] = 1
        heap = [(0,0)]
        while heap:
            d,u = heappop(heap)
            if d != distance[u]:
                continue
            for v,w in graph[u]:
                candidate = d+w
                if candidate < distance[v]:
                    distance[v] = candidate
                    ways[v] = ways[u]
                    heappush(heap,(candidate,v))
                elif candidate == distance[v]:
                    ways[v] += ways[u]
        out.append(str(ways[-1]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Multiple equal-length routes must all count.
- A direct edge may tie a multi-edge route.
- Do not add counts for stale heap entries.

## Dry run

In sample two, direct path `1-3` and path `1-2-3` both have length nine. The equal-distance relaxation adds their counts, returning two.

---

Same problem grouped by topic: [../docs/graphs/CIELTOMY.md](../docs/graphs/CIELTOMY.md)
