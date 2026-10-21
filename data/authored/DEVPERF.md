---
topic: Geometry
subtopic: Manhattan 1-centre via rotated coordinates
time: $O(nm + n \log m)$ per test case
space: $O(nm)$
---
Placing the perfume costs one second and it then spreads one cell per second through side-adjacent houses, so the time is $1$ plus the **largest Manhattan distance** from the chosen cell to an inhabited one. With no inhabited houses the answer is $0$.

So this is the Manhattan 1-centre problem. Rotate coordinates:

$$u = r + c, \qquad v = r - c \qquad\Longrightarrow\qquad |r_1-r_2| + |c_1-c_2| = \max\bigl(|u_1-u_2|,\ |v_1-v_2|\bigr)$$

Manhattan distance becomes Chebyshev distance, which decouples the axes. Then the worst inhabited house seen from a cell $p$ depends only on four numbers over the `*` cells:

$$f(p) = \max\bigl(u_p - u_{\min},\ u_{\max} - u_p,\ v_p - v_{\min},\ v_{\max} - v_p\bigr)$$

so one pass over the grid collects $u_{\min}, u_{\max}, v_{\min}, v_{\max}$ and no per-pair work is needed.

Minimising $f$ still has to respect the grid, since not every $(u,v)$ is a real cell. But $f$ is a maximum of linear functions, hence **convex in $c$ for each fixed row**, so a ternary search over the columns finds each row's best cell in $O(\log m)$ — avoiding the $O(nm)$ scan over placements that would otherwise sit on top of reading the grid.

The sample's second case has `*` cells with $u \in [3,5]$ and $v \in [-1,1]$, so the centre $(2,2)$ gives $f = 1$ and the answer is $2$: one second to place, one to reach the four arms of the plus shape. The first case has a single inhabited house, so placing the perfume there gives $f = 0$ and the answer is $1$ — the placement second is always paid.
