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
