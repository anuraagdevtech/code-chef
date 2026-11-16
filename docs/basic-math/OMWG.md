[&larr; 512. Server Trouble](SVRT.md) &middot; [Index](../../README.md) &middot; [656. Maximal Expression &rarr;](MAXIMALEXP.md)

# 547. One more weird game

> CodeChef problem code [`OMWG`](https://www.codechef.com/problems/OMWG) &middot; difficulty **1536** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Count each grid adjacency exactly once |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Leha is playing a very interesting game. The game will be played on a rectangular grid consisting of **N** rows and **M** columns. Initially all the cells of the grid are uncolored.

Leha's initial score is zero. At each turn, he chooses some cell that is yet not colored, and colors that cell. The score obtained in this step will be number of neighboring colored cells of the cell that Leha colored in this step. Two cells are neighbors of each other if they share a side between them. The game will end when all the cells are colored. Finally, total score obtained at the end of the game will sum of score obtained in each turn.

Leha wants to know what maximum score he can get? Can you please help him in finding this out?

**Input**

The first line contains a single integer **T** denoting the number of test cases. **T** test cases follow.

Each of the following **T** lines contains two space-separated integers **N, M** denoting the dimensions of the grid.

**Output**

For each test case, output a single line containing an integer corresponding to the maximal possible score Leha can obtain.

**Constraints**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N, M** ≤ **1 000**

**Subtasks**

- **Subtask #1[30 points]**: **1** ≤ **N, M** ≤ **3**

- **Subtask #2[70 points]**: **1** ≤ **N, M** ≤ **1 000**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N, M ≤ 1 000

## Sample

**Sample input**

```
1
2 2
```

**Sample output**

```
4
```

<details><summary>Explanation</summary>

Leha can obtain total score 4 in the following way.

- In the first step, he colors down left cell, all the neighboring cells of this cell are uncolored. So, it adds **0** to total score.

- In second step, he can color upper right cell, it also adds total **0** to the score.

- In third step, he can color top left cell. There are two neighboring cell of this cell, both of which are colored. So, this add **2** to the score.

- In the last step, he can choose the remaining down right cell. There are two neighboring cell of this cell, both of which are colored. So, this also add **2** to the score.

Leha can't obtain a score more than 4. Hence 4 is the answer.

</details>

## Approach

For every pair of neighbouring cells, exactly one is coloured later. Their adjacency contributes one point precisely when that later cell is coloured. Thus every grid edge contributes exactly once, regardless of the order.

There are $N(M-1)$ horizontal edges and $M(N-1)$ vertical edges. Their sum is the score for every play order and therefore also the maximum.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        out.append(str(n*(m-1)+m*(n-1)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A one-cell board scores zero.
- Diagonal neighbours do not count.
- No search over colouring orders is necessary.

## Dry run

A two-by-two grid has two horizontal and two vertical adjacencies, so its score is four.

---

Same problem in rating order (#323 of 735): [../../by-rating/323-OMWG.md](../../by-rating/323-OMWG.md)
