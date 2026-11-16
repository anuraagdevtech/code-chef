[&larr; 233. Plusle and Minun on Array](233-PMA.md) &middot; [Index](README.md) &middot; [235. String Game  &rarr;](235-STRAME.md)

# 234. Shortest Path in Binary Trees

> [`BINTREE`](https://www.codechef.com/problems/BINTREE) &middot; difficulty **1413** &middot; time limit **1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Repeatedly move the larger heap label to its parent |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(\log\max(i,j))$ per query |
| **Space** | $O(1)$ |

## Question

Consider an infinite full binary tree (each node has two children except the leaf nodes) defined as follows. For a node labelled **v** its left child will be labelled **2*v** and its right child will be labelled **2*v+1**. The root is labelled as **1**.

You are given **N** queries of the form **i j**. For each query, you have to print the length of the shortest path between node labelled **i** and  node labelled **j**.

**Input**

First line contains **N**, the number of queries. Each query consists of two space separated integers **i** and **j** in one line.

**Output**

For each query, print the required answer in one line.

**Constraints**

- **1** ≤ **N** ≤ **10^5**

- **1** ≤ **i,j** ≤ **10^9**

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ i,j ≤ 10^9

## Sample

**Sample input**

```
3
1 2
2 3
4 3
```

**Sample output**

```
1
2
3
```

<details><summary>Explanation</summary>

For first query, 1 is directly connected to 2 by an edge. Hence distance 1.

</details>

## Approach

The parent of a heap-labelled vertex $v$ is $\lfloor v/2\rfloor$. While the labels differ, move the larger label to its parent and count one edge. The larger label cannot be a strict ancestor of the smaller one, so this move stays on the path toward their lowest common ancestor. When the labels meet, all required upward edges from both endpoints have been counted.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        u,v = int(next(tokens)),int(next(tokens))
        answer = 0
        while u != v:
            if u > v:
                u //= 2
            else:
                v //= 2
            answer += 1
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Equal endpoints have distance zero.
- Root label one has no parent to traverse.
- The leading count is the number of queries.

## Dry run

For labels 4 and 3, move `4->2`, `3->1`, and `2->1`. They meet after three edges.

---

Same problem grouped by topic: [../docs/trees/BINTREE.md](../docs/trees/BINTREE.md)
