---
topic: Dynamic Programming
subtopic: Maximising an average with a fixed denominator
time: $O(N^2)$ per test case
space: $O(N)$
---
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
