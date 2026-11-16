[&larr; 730. Jon and Selina](730-SELINA.md) &middot; [Index](README.md) &middot; [732. Sort Checker &rarr;](732-SRTCHK.md)

# 731. Snakes and transition from Capitalism to Socialism

> [`SNSOCIAL`](https://www.codechef.com/problems/SNSOCIAL) &middot; difficulty **unrated** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Multi-source BFS from all maximum-wealth cells |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(NM)$ per test case |
| **Space** | $O(NM)$ |

## Question

After a long duration of the painful, torturous and tumultuous periods of capitalism in Snakeland, now the snakes have decided to adopt socialism. The houses in Snakeland are arranged in a rectangular fashion of dimension **n * m**. The wealth of the snake in the house at cell (i, j) is given by **a**[i][j] rupees.

A bill has been passed for making a smooth transition from capitalism to socialism. At the end of each hour, the wealth of a snake will grow and will become equal to the highest wealth that its neighbor had (at the start of the hour). That is, consider the maximum wealth among its neighbors at the start of the hour, and this snake's wealth will become equal to that at the end of the hour. Note that this increase in wealth will happen simultaneously for each snake. Two houses are said to be neighbors of each other if they share a side or corner with each other. Find out the minimum number of hours required for this transition.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two space separated integers: **n, m**.

Each of the next **n** lines contains **m** space separated integers. The j-th integer in the i-th row denotes **a**[i][j].

**Output**

For each test case output a single integer corresponding to the minimum number of hours required for the transition.

**Constraints**

- 1 ≤ **T** ≤ 4

- 1 ≤ **n, m** ≤ 500

- 1 ≤ **a**[i][j] ≤ 10^6

## Constraints

- 1 ≤ T ≤ 4
- 1 ≤ n, m ≤ 500
- 1 ≤ a[i][j] ≤ 10^6

## Sample

**Sample input**

```
3
2 2
1 1
1 1
2 2
1 1
1 2
3 4
1 2 1 2
1 1 1 2
1 1 2 2
```

**Sample output**

```
0
1
2
```

<details><summary>Explanation</summary>

**Example 1**. The wealth of all the snakes is already equal. So, no time is required for the transition.

**Example 2**. At the end of the first hour, the wealth of snakes at cells (1, 1), (2,1) and (1, 2) will change from 1 to 2. Then, the wealth of all the snakes becomes equal, and hence it required a total of 1 hour.

**Example 3**. At the end of the first hour, the distribution of wealth of Snakeland will be as given below:

```
2 2 2 2
2 2 2 2
1 2 2 2
```

After the end of the second hour, the wealth of all the snakes will be equal. So, the answer is 2.

</details>

## Approach

The global maximum wealth cannot be exceeded. After one hour it spreads to all eight neighbours of every cell already holding it. Consequently, a cell reaches the maximum after its shortest eight-neighbour distance from any initially maximal cell.

Start a BFS with all maximum cells at distance zero. Its largest assigned distance is the first hour at which the entire grid has the maximum. Each cell is enqueued once.

## Solution

```python
import sys
from collections import deque


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m = int(next(tokens)), int(next(tokens))
        a = [int(next(tokens)) for _ in range(n*m)]
        maximum = max(a)
        distance = [-1]*(n*m)
        queue = deque()
        for i,v in enumerate(a):
            if v == maximum:
                distance[i] = 0
                queue.append(i)
        answer = 0
        while queue:
            u = queue.popleft()
            r,c = divmod(u,m)
            answer = distance[u]
            for rr in range(max(0,r-1), min(n,r+2)):
                for cc in range(max(0,c-1), min(m,c+2)):
                    v = rr*m+cc
                    if distance[v] == -1:
                        distance[v] = distance[u]+1
                        queue.append(v)
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Already-equal grids need zero hours.
- Diagonal neighbours count.
- Start from every maximum, not just the first one.

## Dry run

For a two-by-two grid with only its bottom-right cell maximal, every other cell is a side or diagonal neighbour. BFS gives maximum distance one.

---

Same problem grouped by topic: [../docs/graphs/SNSOCIAL.md](../docs/graphs/SNSOCIAL.md)
