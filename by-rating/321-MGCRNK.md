# 321. Magic Rankings

> [`MGCRNK`](https://www.codechef.com/problems/MGCRNK) &middot; difficulty **1540** &middot; time limit **1.5s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Maximising an average with a fixed denominator |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(N^2)$ per test case |
| **Space** | $O(N)$ |

## Question

Everybody loves magic, especially magicians who compete for glory on the Byteland Magic Tournament. Magician Cyael is one such magician.

Cyael has been having some issues with her last performances and today she’ll have to perform for an audience of some judges, who will change her tournament ranking, possibly increasing it. As she is a great magician she managed to gather a description of the fixed judges’ disposition on the room (which is represented as an $N \times N$ square matrix), such that she knows in advance the fixed points each judge will provide.

She also knows that the room is divided into several parallel corridors, such that we will denote the $j^{th}$ cell on corridor $i$, as $[i][j]$. Note that some judges can award Cyael, zero points or negative points, as they are never pleased with her performance. There is just one judge at each cell of the matrix, except the cells $[1][1]$ and $[N][N]$.
To complete her evaluation, she must start on the top leftmost corner of the room (cell $[1][1]$), and finish on the bottom right corner (cell $[N][N]$), moving either to the cell directly in front of her on the same corridor (that is, moving from cell $[r][c]$ to cell $[r][c+1]$, where $c+1$ $\leq$ $N$) or to the cell in the next corridor directly in front of where she is (that is, moving from cell $[r][c]$ to cell $[r+1][c]$, where $r+1$ $\leq$ $N$). She will keep doing this until she reaches the end point of the room, i.e. last cell $[N][N]$ on the last corridor. Cyael will be judged at all visited cells with a judge.

Cyael wants to maximize her average score at end of her performance. More specifically, if she passes $K$ judges, each being on cell $[i_{1}][j_{1}]$, cell $[i_{2}][j_{2}]$, $\ldots$, cell $[i_{K}][j_{K}]$ respectively, then she wants to maximize $\frac{(S[i_{1}][j_{1}] + S[i_{2}][j_{2}] + \ldots + S[i_{K}][j_{K}])}{K}$, where $S[i][j]$ denotes the points that the judge will give her on the cell $[i][j]$.
Help her determine the best path she has to follow in order to maximize her average points.

**Input**

- The first line contains a single integer $T$ denoting the number of test cases. The description for $T$ test cases follows.
- For each test case, the first line contains a single integer $N$.
- Each of the next $N$ lines contains $N$ space-separated integers. The j-th integer $S[i][j]$ in i-th line denotes the points awarded by the judge at cell $[i][j]$.
- Note that the cells $[1][1]$ and $[N][N]$ have no judges, so $S[1][1]$ and $S[N][N]$ will be 0.

**Output**

- For each test case, if the maximum possible average points Cyael can obtain is negative, output a single line containing "Bad Judges" (quotes for clarity).
- Otherwise, output the maximum possible average points.
- The answer will be considered correct if it has an absolute error no more than  $10^{-6}$.

## Constraints

- 1 $\leq$ $T$ $\leq 20$
- 2 $\leq$ $N$ $\leq 100$
- -2500 $\leq$ $S[i][j]$ $\leq 2500$
- $S[1][1]$ = $S[N][N] = 0$

## Sample

**Sample input**

```
2
2
0 -4
8 0
2
0 -45
-3  0
```

**Sample output**

```
8.000000
Bad Judges
```

<details><summary>Explanation</summary>

**Test case $1$:** An optimal path for Cyael would be $(1,1)\rightarrow (2,1)\rightarrow (2,2)$. This way Cyael faces $1$ judge and gets a total score of $8$. Thus, the average score is $\frac{8}{1} = 8$.

**Test case $2$:** No matter what path Cyael chooses, the final score would be less than $0$.

</details>

## Approach

Maximising an average is usually awkward — it invites binary search on the value or a fractional-programming trick. Here it is neither, because of a counting observation: a monotone path from $[1][1]$ to $[N][N]$ makes exactly $2N - 2$ moves and so visits exactly $2N - 1$ cells, **whatever route it takes**. Two of those, the corners, hold no judge, so every path passes exactly

$$K = 2N - 3$$

judges. The denominator is a constant, so

$$\max \frac{\text{sum}}{K} = \frac{\max \text{sum}}{K}$$

and the problem collapses to the standard maximum-sum monotone path.

That DP is one sweep, since a cell is reachable only from above and from the left:

$$\mathrm{dp}[i][j] = S[i][j] + \max(\mathrm{dp}[i-1][j],\ \mathrm{dp}[i][j-1])$$

with the first row and column having a single predecessor. Negative scores are allowed, but that causes no trouble precisely because the path length is fixed — there is no incentive to take a shortcut, and no shortcut exists. A single row of state suffices, overwritten left to right.

Finally, report `Bad Judges` when the best average is negative, else six decimals. Since $K$ is fixed, the sign of the average is the sign of the sum, so the test needs no division.

The sample's first case has $N = 2$ and $K = 1$: the two paths collect $-4$ and $8$, so the answer is $8.000000$. The second case offers only $-45$ and $-3$, both negative, giving `Bad Judges` — note it is the *maximum* that must be negative, so a single bad route is not enough.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        row = [0] * n
        for i in range(n):
            vals = [int(x) for x in data[pos:pos + n]]
            pos += n
            for j in range(n):
                if i == 0:
                    row[j] = vals[j] + (row[j - 1] if j else 0)
                elif j == 0:
                    row[j] += vals[j]
                else:
                    row[j] = vals[j] + (row[j] if row[j] > row[j - 1] else row[j - 1])
        best = row[n - 1]
        # Every monotone path passes the same 2N - 3 judges, so the average is
        # just the best sum over a constant.
        out.append("Bad Judges" if best < 0 else f"{best / (2 * n - 3):.6f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Every monotone path visits the same number of judges.** A path from $[1][1]$ to $[N][N]$ moving only right or down covers $2N-1$ cells, two of which — the corners — hold no judge. So the denominator is always $2N-3$ and maximising the average reduces to maximising the sum.
- **That is what makes a plain max-path DP correct.** If the path length varied, the average would not be optimised by the best sum, and the problem would need a fractional search.
- **The corner cells are guaranteed zero** ($S[1][1] = S[N][N] = 0$), so including them in the DP sum costs nothing and no special-casing is needed.
- **Negative points are allowed and common**, so the best sum can still be negative — in which case the answer is `Bad Judges` rather than a number.
- **The threshold is strict**: a best sum of exactly $0$ prints `0.000000`, not `Bad Judges`.
- **$N = 2$ gives a denominator of $1$** (the sample), so the average equals the single judge's score; this is also the smallest allowed $N$.
- **The rolling single row** is enough because each cell depends only on its left and upper neighbours, keeping memory at $O(N)$ for $N \leq 100$.

## Dry run

First sample: $N = 2$ with $S = \begin{pmatrix} 0 & -4 \\ 8 & 0\end{pmatrix}$.

| path | judges passed | sum |
|---|---|---:|
| right then down | $S[1][2] = -4$ | $-4$ |
| down then right | $S[2][1] = 8$ | **8** |

Denominator $2N - 3 = 1$, so the answer is `8.000000`. The second sample's best sum is $-3$, hence `Bad Judges`.

---

Same problem grouped by topic: [../docs/dynamic-programming/MGCRNK.md](../docs/dynamic-programming/MGCRNK.md)
