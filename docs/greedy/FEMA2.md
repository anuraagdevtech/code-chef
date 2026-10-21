# 342. Iron, Magnet and Wall

> CodeChef problem code [`FEMA2`](https://www.codechef.com/problems/FEMA2) &middot; difficulty **1725** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Interval bipartite matching with two queues |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Chef loves to play with iron (Fe) and magnets (Ma). He took a row of $N$ cells (numbered $1$ through $N$) and placed some objects in some of these cells. You are given a string $S$ with length $N$ describing them; for each valid $i$, the $i$-th character of $S$ is one of the following:
- 'I' if the $i$-th cell contains a piece of iron
- 'M' if the $i$-th cell contains a magnet
- '_' if the $i$-th cell is empty
- ':' if the $i$-th cell contains a conducting sheet
- 'X' if the $i$-th cell is blocked

If there is a magnet in a cell $i$ and iron in a cell $j$, the *attraction power* between these cells is $P_{i,j} = K+1 - |j-i| - S_{i,j}$, where $S_{i,j}$ is the number of cells containing sheets between cells $i$ and $j$. This magnet can only *attract* this iron if $P_{i, j} \gt 0$ and there are no blocked cells between the cells $i$ and $j$.

Chef wants to choose some magnets (possibly none) and to each of these magnets, assign a piece of iron which this magnet should attract. Each piece of iron may only be attracted by at most one magnet and only if the attraction power between them is positive and there are no blocked cells between them. Find the maximum number of magnets Chef can choose.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains a single string $S$ with length $N$.

**Output**
For each test case, print a single line containing one integer ― the maximum number of magnets that can attract iron.

**Constraints**
- $1 \le T \le 2,000$
- $1 \le N \le 10^5$
- $0 \le K \le 10^5$
- $S$ contains only characters 'I', 'M', '_', ':' and 'X'
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^6$

**Subtasks**
**Subtask #1 (30 points):** there are no sheets, i.e. $S$ does not contain the character ':'

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 2,000$
- $1 \le N \le 10^5$
- $0 \le K \le 10^5$
- $S$ contains only characters 'I', 'M', '_', ':' and 'X'
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^6$

## Sample

**Sample input**

```
2
4 5
I::M
9 10
MIM_XII:M
```

**Sample output**

```
1
2
```

<details><summary>Explanation</summary>

**Example case 1**: The attraction power between the only magnet and the only piece of iron is $5+1-3-2 = 1$. Note that it decreases with distance and the number of sheets.

**Example case 2:**
The magnets in cells $1$ and $3$ can attract the piece of iron in cell $2$, since the attraction power is $10$ in both cases. They cannot attract iron in cells $6$ or $7$ because there is a wall between them.

The magnet in cell $9$ can attract the pieces of iron in cells $7$ and $6$; the attraction power is $8$ and $7$ respectively.

</details>

## Approach

The attraction condition $P_{i,j} = K + 1 - |j - i| - S_{i,j} > 0$ rearranges to a budget:

$$|j - i| + S_{i,j} \leq K$$

Both terms depend on the pair, which looks awkward — but they collapse into a single coordinate. Let $\mathrm{pre}[i]$ count the sheets in cells $1 \ldots i$ and define

$$w(i) = i + \mathrm{pre}[i]$$

For a magnet at $i$ and iron at $j > i$, neither of which is a sheet, $w(j) - w(i) = (j - i) + (\mathrm{pre}[j-1] - \mathrm{pre}[i])$, and that second bracket is exactly the sheet count strictly between them. So the condition is just

$$|w(j) - w(i)| \leq K$$

Each sheet costs the same as a cell of distance, so folding it into the coordinate makes the problem one-dimensional. Blocked cells are a hard cut rather than a cost, so they split the row into independent **blocks**, solved separately and summed.

Within a block, every magnet can serve any iron whose $w$ lies in a window of radius $K$ around it. Scanning left to right, $w$ only increases, so an unmatched piece that has fallen out of the current window can never come back and is discarded for good. That makes a two-queue greedy optimal: hold pending magnets and pending irons in FIFO order, and on reaching a new piece, drop the stale opposite-type entries and then match the **oldest** survivor. The oldest is the one with the smallest $w$, hence the one whose window expires soonest — the earliest-deadline-first exchange: if an optimal matching pairs the new piece with a later partner while an older one goes unused, swapping them keeps the matching valid and the same size.

In `I::M` with $K = 5$ the two sheets make $w(1) = 1$ and $w(4) = 6$, a gap of exactly $5$, so the single magnet just reaches its iron. In `MIM_XII:M` the `X` cuts the row in two; each half yields one pair, so the answer is $2$ — note the left block has two magnets but only one iron, and the right block two irons but only one magnet, so the surplus is wasted on both sides.

## Solution (Python)

```python
import sys
from collections import deque


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        row = data[pos + 2]
        pos += 3
        matched = 0
        sheets = 0
        magnets, irons = deque(), deque()
        for idx in range(n):
            cell = row[idx]
            if cell == 0x58:              # 'X' cuts the row into blocks
                magnets.clear()
                irons.clear()
                continue
            if cell == 0x3A:              # ':' costs the same as one cell
                sheets += 1
                continue
            if cell == 0x5F:              # '_'
                continue
            # Distance plus sheets between two pieces is a difference of these.
            w = idx + 1 + sheets
            if cell == 0x4D:              # 'M'
                while irons and w - irons[0] > k:
                    irons.popleft()
                if irons:
                    irons.popleft()       # oldest == window expires soonest
                    matched += 1
                else:
                    magnets.append(w)
            else:                         # 'I'
                while magnets and w - magnets[0] > k:
                    magnets.popleft()
                if magnets:
                    magnets.popleft()
                    matched += 1
                else:
                    irons.append(w)
        out.append(str(matched))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Data Structures`, `Algorithms`
