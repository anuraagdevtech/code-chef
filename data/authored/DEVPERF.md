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

## Edge cases

- **Manhattan distance becomes Chebyshev distance under the rotation $(u, v) = (r+c,\, r-c)$**, so the worst distance from a cell to every inhabited house is $\max$ of four linear terms over the extremes of $u$ and $v$ — four numbers summarise the whole grid.
- **Only the bounding box in rotated coordinates matters**, not the individual houses, which is what makes the evaluation constant-time per candidate cell.
- **The perfume may go in a haunted house too**, so every cell is a candidate — not just the inhabited ones.
- **No inhabited houses at all** → $0$ seconds, since nothing needs hypnotising; this is checked before any search.
- **The $+1$ is the placement second**, which the statement charges separately from the spreading.
- **The worst-distance function is convex along a row**, being a maximum of linear functions, so a ternary search finds each row's best column — and the final window is swept directly to avoid the usual off-by-one.
- **A single inhabited house** gives $0$ spreading time if the perfume is placed there, for an answer of $1$.

## Dry run

Second sample: a $3 \times 4$ grid with inhabited houses at $(0,1)$, $(1,0)$, $(1,1)$, $(1,2)$, $(2,1)$ (0-based).

| house | $u = r+c$ | $v = r-c$ |
|---|---:|---:|
| $(0,1)$ | 1 | $-1$ |
| $(1,0)$ | 1 | 1 |
| $(1,1)$ | 2 | 0 |
| $(1,2)$ | 3 | $-1$ |
| $(2,1)$ | 3 | 1 |

So $u \in [1,3]$ and $v \in [-1,1]$. Placing the perfume at $(1,1)$ gives $u = 2$, $v = 0$ and a worst distance of $\max(1, 1, 1, 1) = 1$.

Output $1 + 1 = $ `2`.
