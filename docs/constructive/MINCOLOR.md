[&larr; 428. Bitwise Equation](BITEQU.md) &middot; [Index](../../README.md) &middot; [478. Same Parity Swaps in Binary Strings &rarr;](MAX01EVSWP.md)

# 449. Minimum Coloring

> CodeChef problem code [`MINCOLOR`](https://www.codechef.com/problems/MINCOLOR) &middot; difficulty **1713** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Checkerboard parity, with a third colour only when forced |
| **Time** | $O(NM)$ per test case |
| **Space** | $O(M)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

There is a matrix of size $N \times M$. Two **distinct** cells of the matrix $(x_1, y_1)$ and $(x_2, y_2)$ are painted with colors $\text{1}$ and $\text{2}$ respectively.

You have to paint the **remaining** cells of the matrix such that:
- No two adjacent cells are painted in same color.
- Each color is an integer from $1$ to $10^9$ (both inclusive).
- The number of **distinct** colors used is **minimum** (including $\text{1}$ and $\text{2}$).

**Note**:
1. You cannot repaint the cells $(x_1, y_1)$ and $(x_2, y_2)$.
2. Two cells are adjacent if they share a common edge. Thus, for a cell $(x,y)$ there are $4$ adjacent cells. The adjacent cells are $(x, y+1), (x, y-1), (x+1,y),$ and $(x-1,y)$.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow. Each test case consists of $3$ lines.
- The first line contains two space seperated integers $N$ and $M$ denoting the dimensions of the matrix.
- The second line contains two integers $x_1$ and $y_1$, denoting the coordinates of cell which is painted $\text{1}$.
- The third line contains two integers $x_2$ and $y_2$, denoting the coordinates of cell which is painted $\text{2}$.

**Output**

For each test case, output $N$ lines, each consisting of $M$ space separated integers where $j^{th}$ integer in $i^{th}$ line denotes the color of cell in $i^{th}$ row and $j^{th}$ column of the matrix and must be in $[1, 10^9]$ inclusive.

In case of multiple possible answers, output any.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N, M \leq 10^5$
- $1 \leq x_1, x_2 \leq N$
- $1 \leq y_1, y_2 \leq M$
- $(x_1, y_1) \neq (x_2, y_2)$
- Sum of $N \cdot M$ over all test cases does not exceed $10^5$.

## Sample

**Sample input**

```
2
2 2
1 1
2 2
2 3
1 1
1 2
```

**Sample output**

```
1 4
4 2
1 2 1
2 1 2
```

<details><summary>Explanation</summary>

**Test Case $1$:**
![](https://s3.amazonaws.com/codechef_shared/download/Images/START30/Sample1.png)
The initially painted cells are $(1,1)$ and $(2,2)$. One possible way is to paint the remaining cells with color $4$. This way, no two adjacent cells have the same color.
Note that, instead of color $4$, we can use any other color in the range $[1, 10^9]$ except colors $1$ and $2$.
The number of distinct colors used in this case is $3$. It can be shown that the minimum number of distinct colors cannot be less than $3$.

**Test Case $2$:**
![](https://s3.amazonaws.com/codechef_shared/download/Images/START30/Sample2.png)
The initially painted cells are $(1,1)$ and $(1,2)$. One possible way is to paint the remaining cells as shown in the figure. This way, no two adjacent cells have the same color.
The number of distinct colors used in this case is $2$. It can be shown that the minimum number of distinct colors cannot be less than $2$.

</details>

## Approach

A grid is bipartite, so two colours always suffice for a proper colouring: paint by the parity of $r + c$. The only question is whether the two pre-painted cells are compatible with such a colouring.

In any 2-colouring of a grid, cells of the same $r + c$ parity get the same colour. So:

- **Parities differ:** the checkerboard assigning colour $1$ to the parity of $(x_1, y_1)$ and colour $2$ to the other parity respects both fixed cells. Two colours, the minimum possible.
- **Parities match:** both fixed cells would need the same colour, but they are $1$ and $2$. So two colours are impossible and **three** is the answer. Build it as a checkerboard in colours $1$ and $3$ — colour $1$ on the parity of $(x_1, y_1)$ — and then overwrite $(x_2, y_2)$ with $2$. That cell's neighbours all lie on the other parity and carry $3$, so the colouring stays proper.

Three is never exceeded, so the construction is optimal in both branches.

The second sample has $(1,1)$ and $(1,2)$ on opposite parities, so the plain checkerboard works and uses two colours. The first sample has $(1,1)$ and $(2,2)$ both on even parity, forcing three: our grid is $\begin{smallmatrix}1 & 3\\ 3 & 2\end{smallmatrix}$ while the sample prints $\begin{smallmatrix}1 & 4\\ 4 & 2\end{smallmatrix}$ — the third colour's value is free, any of $1 \ldots 10^9$ will do, so both are accepted.

Note $N, M \geq 2$, so the grid always has at least one adjacency and the conflict is real rather than vacuous.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        x1, y1 = int(data[pos + 2]), int(data[pos + 3])
        x2, y2 = int(data[pos + 4]), int(data[pos + 5])
        pos += 6
        base = (x1 + y1) % 2
        # Same parity means two colours cannot separate the fixed cells.
        other = 2 if (x2 + y2) % 2 != base else 3
        for r in range(1, n + 1):
            row = [1 if (r + c) % 2 == base else other for c in range(1, m + 1)]
            if other == 3 and r == x2:
                row[y2 - 1] = 2        # its neighbours all carry 3
            out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(NM)$ per test case
- **Space:** $O(M)$

## Edge cases

- **Two colours suffice exactly when the fixed cells sit on opposite checkerboard parities**, since a proper two-colouring of a grid *is* the checkerboard and it assigns colours by $(r+c) \bmod 2$.
- **Same parity forces a third colour**, because the two fixed cells would both have to take colour $1$ — and they cannot be repainted.
- **Three always suffice**, by the construction here: checkerboard with $1$ on the first cell's parity class and $3$ on the other, then overwrite the second fixed cell with $2$. Its neighbours all lie in the opposite class and carry $3$, so nothing clashes.
- **The overwrite is safe precisely because of the parity collision** — the cell being overwritten is surrounded entirely by the other class.
- **The two cells are guaranteed distinct**, so the overwrite never lands on the first fixed cell.
- **The colour range runs to $10^9$**, so the choice of $3$ as the third colour is arbitrary — the sample uses $4$ instead, and a special judge checks adjacency and the colour count rather than the exact values.
- **Sum of $N \cdot M \leq 10^5$**, so the grid is emitted row by row with no stored matrix.

## Dry run

Second sample: $2 \times 3$ with cell $(1,1)$ fixed to $1$ and $(1,2)$ fixed to $2$.

| cell | parity $(r+c) \bmod 2$ |
|---|---:|
| $(1,1)$ | 0 |
| $(1,2)$ | 1 |

Different parities, so two colours are enough:

| row | colouring |
|---:|---|
| 1 | `1 2 1` |
| 2 | `2 1 2` |

Both fixed cells already hold their required colours, and no two neighbours match.

> CodeChef tags: `Algorithms`, `Graph Algos`

---

Same problem in rating order (#419 of 486): [../../by-rating/419-MINCOLOR.md](../../by-rating/419-MINCOLOR.md)
