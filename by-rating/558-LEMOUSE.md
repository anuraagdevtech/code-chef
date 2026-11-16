[&larr; 557. Snake Eating](557-SNAKEEAT.md) &middot; [Index](README.md) &middot; [559. Even Edges &rarr;](559-EVEDG.md)

# 558. Little Elephant and Mouses

> [`LEMOUSE`](https://www.codechef.com/problems/LEMOUSE) &middot; difficulty **1941** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Grid path DP that remembers the last move to avoid double counting |
| **CodeChef tags** | `Algorithms`, `Dynamic Programming` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(N \cdot M)$ per test case |
| **Space** | $O(N \cdot M)$ |

## Question

It is well-known that the elephants are afraid of mouses. The Little Elephant from the Zoo of Lviv is not an exception.

The Little Elephant is on a board **A** of **n** rows and **m** columns (0-based numeration). At the beginning he is in cell with coordinates **(0; 0)** and he wants to go to cell with coordinates **(n-1; m-1)**. From cell **(x; y)** Little Elephant can go either to **(x+1; y)** or **(x; y+1)**.

Each cell of the board contains either **1** or **0**. If **A[i][j] = 1**, then there is a single mouse in cell **(i; j)**. Mouse at cell **(i; j)** scared Little Elephants if and only if during the path there was at least one such cell **(x; y)** (which belongs to that path) and **|i-x| + |j-y| <= 1**.

Little Elephant wants to find some correct path from **(0; 0)** to **(n-1; m-1)** such that the number of mouses that have scared the Little Elephant is minimal possible. Print that number.

**Input**

First line contains single integer **T** - the number of test cases. Then **T** test cases follow. First line of each test case contain pair of integers **n** and **m** - the size of the board. Next **n** lines contain **n** strings, each of size **m** and consisted of digits **0** and **1**.

**Output**

In **T** lines print **T** integer - the answers for the corresponding test.

**Constraints**

**1** <= **T** <= **50**

**2** <= **n, m** <= **100**

## Constraints

1 <= T <= 50
2 <= n, m <= 100

## Sample

**Sample input**

```
2
3 9
001000001
111111010
100100100
7 9
010101110
110110111
010011111
100100000
000010100
011011000
000100101
```

**Sample output**

```
9
10
```

<details><summary>Explanation</summary>

**Example case 1: **
The optimized path is: (0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (0, 4) -> (0, 5) -> (0, 6) -> (0, 7) -> (0, 8) -> (1, 8) -> (2, 8). The mouses that scared the Little Elephant are at the following cells: (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 7), (0, 2), (0, 8).

**Example case 2: **
The optimized path is: (0, 0) -> (1, 0) -> (1, 1) -> (2, 1) -> (2, 2) -> (3, 2) -> (3, 3) -> (4, 3) -> (4, 4) -> (5, 4) -> (5, 5) -> (6, 5) -> (6, 6) -> (6, 7) -> (6, 8). The 10 mouses that scared the Little Elephant are at the following cells: (0, 1), (1, 0), (1, 1), (2, 1), (3, 3), (4, 4), (5, 4), (5, 5), (6, 6), (6, 8).

</details>

## Approach

A mouse scares the elephant when its cell is on the path or adjacent to a path cell. Counting the mice near each path cell separately would count some of them several times, so the DP has to know which of them were already counted.

The plus-shaped neighbourhood of a new path cell can only overlap the neighbourhoods of the previous two path cells: anything earlier on a monotone path is at Manhattan distance at least 3. The state is therefore the current cell together with the direction of the move that entered it, which identifies the previous cell. When stepping to a new cell, add the mice in its neighbourhood that are not in the neighbourhood of the current cell or of the cell before it.

The answer is the smaller of the two states at the bottom-right corner.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, m = (int(next(tokens)), int(next(tokens)))
        board = [next(tokens) for _ in range(n)]

        def near(x, y):
            return {(u, v) for u, v in ((x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if 0 <= u < n and 0 <= v < m}
        best = [[[10 ** 9] * 2 for _ in range(m)] for _ in range(n)]
        initial = sum((board[x][y] == 49 for x, y in near(0, 0)))
        best[0][0] = [initial, initial]
        for x in range(n):
            for y in range(m):
                for last in range(2):
                    if best[x][y][last] >= 10 ** 9:
                        continue
                    seen = near(x, y)
                    if x + y:
                        seen |= near(x - (last == 0), y - (last == 1))
                    for d, (u, v) in enumerate(((x + 1, y), (x, y + 1))):
                        if u < n and v < m:
                            best[u][v][d] = min(best[u][v][d], best[x][y][last] + sum((board[r][s] == 49 for r, s in near(u, v) - seen)))
        out.append(str(min(best[-1][-1])))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- The start cell has no previous cell; both direction states are initialised with the mice around $(0, 0)$.
- Neighbourhoods are clipped at the border of the board.
- A mouse on the path itself counts too - the neighbourhood includes the cell.
- Rows are strings, so cells are compared with the character `1`, not the integer.

## Dry run

Board `01 / 10`. Around the start $(0,0)$ there are two mice, at $(0,1)$ and $(1,0)$, so the initial value is 2.

Moving right to $(0,1)$: its neighbourhood is $\{(0,1), (0,0), (1,1)\}$; the only mouse there, $(0,1)$, was already counted - still 2. Moving down to $(1,1)$: its neighbourhood adds nothing new - still 2. The path that goes down first is symmetric.

Answer 2.

---

Same problem grouped by topic: [../docs/dynamic-programming/LEMOUSE.md](../docs/dynamic-programming/LEMOUSE.md)
