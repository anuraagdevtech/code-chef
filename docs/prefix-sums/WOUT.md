[&larr; 594. Gerrymander](GERMANDE.md) &middot; [Index](../../README.md) &middot; [611. Chef and Strings &rarr;](STRQ.md)

# 608. Way Out

> CodeChef problem code [`WOUT`](https://www.codechef.com/problems/WOUT) &middot; difficulty **1845** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Difference array per row, then the best window of H rows |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Oh, no! Chef’s in trouble. He’s got himself stuck in a cave (we don’t know how) and is looking for a way out. The bigger problem is that he needs to get his tractor out of the cave (don't ask why Chef owns a tractor!). He currently faces a large block of height **N** cells and length **N** cells, and needs to get his tractor across this block. The block is made up of vertical columns of soil, each of which is one cell long. Each column has a continuous vertical gap, with the **i**^th column having its gap from the **l_i**^th cell to the **h_i**^th cell (starting from the bottom, 0-indexing). That is, in the **i**^th column, there is no soil from the **l_i**^th cell to the **h_i**^th cell (both inclusive). Chef can build additional gaps by clearing some cells of soil. His tractor has height **H**, and therefore, he needs to build a horizontal corridor of height **H** passing through all the columns. That is, some consecutive **H** rows must have no soil. Please see the figures in the example and explanation sections for more details.

Chef is able to clear one cell of soil by spending one unit of energy. Chef is smart, and will figure out a way to build the horizontal corridor while spending the minimum possible amount of energy. To estimate how many of his tasty dishes he will still be able to cook for you tonight, find out what is the minimum possible energy he needs to spend.

**Input**

First line of input contains one integer **T** - number of test cases. **T** test cases follow.

Each test case starts with two integers **N** and **H** – size of the cave and height of the tractor, respectively. In each of the next **N** lines are two integers **l_i** and **h_i**, respectively indicating lowest and highest number of cell for the gap in the **i**^th column.

**Output**

One integer – minimum energy required.

**Constraints**

- **1** ≤ **T** ≤ **10^3**

- **1** ≤ **N** ≤ **10^6**

- **1** ≤ sum of **N** over all test cases ≤ **10^6**

- **1** ≤ **H** ≤ **N**

- **0** ≤ **l_i** ≤ **h_i** < **N**

**Subtasks**

Subtask 1 (25 points): **T ≤ 100, N ≤ 100**

Subtask 2 (75 points): No additional constraints

## Constraints

- 1 ≤ T ≤ 10^3
- 1 ≤ N ≤ 10^6
- 1 ≤ sum of N over all test cases ≤ 10^6
- 1 ≤ H ≤ N
- 0 ≤ l_i ≤ h_i < N

## Sample

**Sample input**

```
2
4 3
1 2
1 2
1 2
1 2
5 2
2 3
1 2
2 3
1 2
2 3
```

**Sample output**

```
4
2
```

<details><summary>Explanation</summary>

In the second case, the figure describes the initial map, where white cells denote empty cells and brown cells denote soil cells.

<img width="350" height="225" src="http://www.codechef.com/download/AUG15/bef.png" alt="">
When we removed soil in two cells as the following figure, then we can make a corridor of height 2, adn this is the optimal way to make a corridor.

<img width="350" height="225" src="http://www.codechef.com/download/AUG15/aft.png" alt="">

</details>

## Approach

The corridor is $H$ consecutive rows that must be empty in all $N$ columns, so clearing it costs $N \cdot H$ minus the number of cells in those rows that are already empty. We want the window of $H$ rows containing the most existing gap cells.

Each column contributes one gap cell to every row in $[l_i, h_i]$. Add all of these intervals with a difference array, take a prefix sum to get the number of gap cells in each row, and slide a window of $H$ rows over that array.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n, height = (next(tokens), next(tokens))
        row_gaps = [0] * (n + 1)
        for _ in range(n):
            low, high = (next(tokens), next(tokens))
            row_gaps[low] += 1
            row_gaps[high + 1] -= 1
        active = 0
        for i in range(n):
            active += row_gaps[i]
            row_gaps[i] = active
        window = sum(row_gaps[:height])
        best = window
        for i in range(height, n):
            window += row_gaps[i] - row_gaps[i - height]
            best = max(best, window)
        out.append(str(n * height - best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $H = N$: there is a single window and the answer is the number of soil cells.
- A column whose gap already covers the window contributes $H$ and costs nothing.
- The answer can reach $N \cdot H$, about $10^{12}$ for the largest inputs.
- Rows are 0-indexed from the bottom and the gap bounds are inclusive.

## Dry run

`N = 5, H = 2`, gaps `[2,3] [1,2] [2,3] [1,2] [2,3]`.

Gap cells per row 0-4: `0 2 5 3 0`. Windows of two rows: `2, 7, 8, 3`. The best holds 8 empty cells out of $5 \cdot 2 = 10$.

Answer $10 - 8 = 2$.

---

Same problem in rating order (#535 of 735): [../../by-rating/535-WOUT.md](../../by-rating/535-WOUT.md)
