# 1696 &middot; Fencing

> CodeChef problem code [`FENCE`](https://www.codechef.com/problems/FENCE) &middot; time limit **3s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Perimeter as sides minus shared edges |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Constructive`, `Maps`, `Hashmaps`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(K)$ per test case |
| **Space** | $O(K)$ |

Same write-up grouped by topic: [../docs/sets/FENCE.md](../docs/sets/FENCE.md)

## Question

There is a field with plants — a grid with $N$ rows (numbered $1$ through $N$) and $M$ columns (numbered $1$ through $M$); out of its $NM$ cells, $K$ cells contain plants, while the rest contain weeds. Two cells are adjacent if they have a common side.

You want to build fences in the field in such a way that the following conditions hold for each cell that contains a plant:
- it is possible to move from this cell to each adjacent cell containing a plant without crossing any fences
- it is impossible to move from this cell to any cell containing weeds or to leave the grid without crossing any fences

The fences can only be built between cells or on the boundary of the grid, i.e. on the sides of cells. The total length of the built fences is the number of pairs of side-adjacent cells such that there is a fence built on their common side plus the number of sides of cells on the boundary of the grid which have fences built on them. Find the minimum required total length of fences that need to be built.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $M$ and $K$.
- $K$ lines follow. Each of these lines contains two space-separated integers $r$ and $c$ denoting that the cell in row $r$ and column $c$ contains a plant.

### Output
For each test case, print a single line containing one integer — the minimum required length of fences.

### Constraints
- $1 \le T \le 10$
- $1 \le N, M \le 10^9$
- $1 \le K \le 10^5$
- $1 \le r \le N$
- $1 \le c \le M$
- the cells containing plants are pairwise distinct

### Subtasks
**Subtask #1 (30 points):** $1 \le N, M \le 1,000$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le N, M \le 10^9$
- $1 \le K \le 10^5$
- $1 \le r \le N$
- $1 \le c \le M$
- the cells containing plants are pairwise distinct

## Sample

**Sample input**

```
2
4 4 9
1 4
2 1 
2 2
2 3
3 1
3 3
4 1
4 2
4 3
4 4 1
1 1
```

**Sample output**

```
20
4
```

<details><summary>Explanation</summary>

**Example case 1:** The field looks like this ('x' denotes a cell containing a plant, '.' denotes a cell containing weeds):
```
...x
xxx.
x.x.
xxx.
```
An optimal solution is to build fences around the topmost plant (with length $4$), around the remaining eight plants (with length $12$) and around the hole between them (with length $4$). The total length is $4+12+4 = 20$.

</details>

## Approach

The two conditions say the fence must be exactly the **boundary of the plant region**: passable between adjacent plants, impassable everywhere else. So a cell side needs a fence precisely when it separates a plant from a non-plant — another plant's side, the weeds, or the outside.

Count from the plants' point of view. Each of the $K$ plant cells has $4$ sides, giving $4K$ in all. A side shared by **two** plants is counted twice and needs no fence, so each adjacent plant pair removes $2$:

$$\text{answer} = 4K - 2P, \qquad P = \#\{\text{side-adjacent plant pairs}\}$$

Every other side borders weeds or the grid edge and must be fenced, which is why the grid dimensions $N$ and $M$ never enter the formula — a plant on the boundary fences that side against the outside exactly as it would against weeds.

With $N, M$ up to $10^9$ the grid cannot be materialised, but $K \leq 10^5$, so store the plant coordinates in a hash set and count $P$ by checking, for each plant, whether the cell to its right and the cell below are also plants. Looking only right and down counts each pair once.

The first sample has $9$ plants in a horseshoe shape with $8$ adjacencies, giving $36 - 16 = 20$. The isolated plant at $(1,4)$ contributes its full $4$ sides, three against weeds and one against the grid edge — which is what makes that shape's answer larger than a compact block of nine would be. The second sample is that single-cell case alone: $4 - 0 = 4$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        k = int(data[pos + 2])
        pos += 3
        plants = set()
        for _ in range(k):
            plants.add((int(data[pos]), int(data[pos + 1])))
            pos += 2
        # Look only right and down so each adjacent pair is counted once.
        shared = sum(((r, c + 1) in plants) + ((r + 1, c) in plants)
                     for r, c in plants)
        out.append(str(4 * k - 2 * shared))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(K)$ per test case
- **Space:** $O(K)$
