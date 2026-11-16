[&larr; 522. Wealth Disparity](INOI1601.md) &middot; [Index](../../README.md) &middot; [527. Cosmic Temple &rarr;](COSTEMP.md)

# 524. Family Tree

> CodeChef problem code [`FAMTREE`](https://www.codechef.com/problems/FAMTREE) &middot; difficulty **1720** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Carry the minimum and maximum ancestor wealth during DFS |
| **Time** | $O(N)$ overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

You are given a family tree with $N$ members numbered $1 ... N$. Every person $i$, except for the founder of the family (root) has a parent denoted by $P[i]$. $P[root]$ = -1 by definition. Person $i$ is a descendant of person $j$ if $i$ belongs to the subtree rooted at $j$.

The net worth (adjusted for inflation) is given for all the members of the family. Your task is to find the maximum difference in net worth's of two members where one member is a descendant of the other.

You can assume that no two members of this family married each other. So it remains a "family tree".

**Input**

- First line will contain  an integer $N$, denoting the number of members.
- Second line contains N space seperated integers W[1], W[2] ... W[N] denoting the net_worth of the N members.
- Third line contains  N space seperated integers P[1], P[2] ... P[N] denoting the parents of the N members.

**Output**

Output in a single line the maximum difference in net worth's of any two members where one member is a descendant of the other.

## Constraints

- $2 \leq N \leq 10^5$
- $-10^8 \leq W[i] \leq 10^8$
- $1 \leq P[i] \leq N$

## Sample

**Sample input**

```
4 
5 10 6 12 
2 -1 4 2
```

**Sample output**

```
6
```

<details><summary>Explanation</summary>

This structure of the tree is:

            2
           / \
          1   4
             /
            3

The maximum difference occurs between the 3rd and 4th members. $W[3]-W[4] = 6$.

</details>

## Approach

For a fixed descendant, the greatest absolute wealth difference against an ancestor is attained by either the poorest or the richest ancestor. Carry both extremes along the root path during iterative DFS. Evaluate `max(highest - current, current - lowest)` before updating the extremes, so the pair contains two distinct vertices.

Every valid ancestor pair is covered by these two extremes at its descendant. This differs from INOI1601, which specifically asks for ancestor wealth minus descendant wealth. See the [CodeChef editorial](https://discuss.codechef.com/t/famtree-editorial/18864) for the absolute-difference interpretation.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n = int(next(tokens))
    wealth = [int(next(tokens)) for _ in range(n)]
    children = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        p = int(next(tokens))
        if p == -1:
            root = i
        else:
            children[p-1].append(i)
    answer = -10**30
    stack = [(root, wealth[root], wealth[root])]
    while stack:
        u, highest, lowest = stack.pop()
        for v in children[u]:
            answer = max(answer, highest-wealth[v], wealth[v]-lowest)
            stack.append((v,max(highest,wealth[v]),min(lowest,wealth[v])))
    print(answer if n > 1 else 0)

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N)$ overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The root is identified by parent `-1`, not by its index.
- Wealth may be negative.
- Check both directions of the wealth difference; wealth increasing down the tree can determine the answer.

## Dry run

The sample has root 2 with wealth 10, and descendant 3 under vertex 4 of wealth 12. At vertex 3, highest ancestor wealth is 12 and its wealth is 6, giving the maximum difference 6.

---

Same problem in rating order (#448 of 735): [../../by-rating/448-FAMTREE.md](../../by-rating/448-FAMTREE.md)
