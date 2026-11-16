[&larr; 341. Yet Another Constructive Problem](341-ORANDCON.md) &middot; [Index](README.md) &middot; [343. Chef In Infinite Plane &rarr;](343-CHFPLN.md)

# 342. Ada King

> [`ADAKNG`](https://www.codechef.com/problems/ADAKNG) &middot; difficulty **1581** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Geometry |
| **Technique** | Clip a Chebyshev-distance square to the chessboard |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef Ada is training to defend her title of World Chess Champion.

To train her calculation skills, Ada placed a <a >king</a> on a chessboard. Remember that a chessboard has $8$ rows and $8$ columns (for the purposes of this problem, both the rows and the columns are numbered $1$ through $8$); let's denote the square in row $r$ and column $c$ by $(r, c)$. A king on a square $(r, c)$ can move to another square $(r', c')$ if and only if $(r'-r)^2+(c'-c)^2 \le 2$.

Ada placed her king on the square $(R, C)$. Now, she is counting the number of squares that can be visited (reached) by the king in at most $K$ moves. Help Ada verify her answers.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $R$, $C$ and $K$.

**Output**
For each test case, print a single line containing one integer — the number of squares the king can visit.

**Constraints**
- $1 \le T \le 512$
- $1 \le R, C, K \le 8$

## Constraints

- $1 \le T \le 512$
- $1 \le R, C, K \le 8$

## Sample

**Sample input**

```
1
1 3 1
```

**Sample output**

```
6
```

<details><summary>Explanation</summary>

**Example case 1:** The king can stay on its original square or move to one of the squares circled in the following figure.

![](https://codechef_shared.s3.amazonaws.com/download/Images/CK102TST/ADAKNG/ADAKNG.png)

</details>

## Approach

A king reaches a square in the larger of its row and column displacements, since a diagonal move can reduce both at once. Thus reachable rows lie in $[R-K,R+K]$ and columns in $[C-K,C+K]$. Clip both intervals to 1 through 8 and multiply their lengths.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        r, c, k = (int(next(tokens)) for _ in range(3))
        rows = min(8,r+k)-max(1,r-k)+1
        cols = min(8,c+k)-max(1,c-k)+1
        out.append(str(rows*cols))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Include the starting square: the limit is at most $K$ moves.
- Clip both ends independently at board boundaries.
- Large $K$ reaches all 64 squares.

## Dry run

For `(R,C,K)=(1,3,1)`, reachable rows are 1 through 2 and columns 2 through 4, giving `2*3=6`.

---

Same problem grouped by topic: [../docs/geometry/ADAKNG.md](../docs/geometry/ADAKNG.md)
