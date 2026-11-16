---
topic: Combinatorics
subtopic: Convert labels to (row, column) and choose which steps go right
time: $O(\sqrt{V})$ precomputation and $O(1)$ per query, $V$ the largest label
space: $O(\sqrt{V})$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Row $r$ of the pyramid ends with the triangular number $r(r+1)/2$, so the row of a label $x$ is the smallest $r$ with $r(r+1)/2 \ge x$, found from an integer square root with a one-step correction, and its column is $x - r(r-1)/2$.

Every move goes down one row; the bottom-left move keeps the column and the bottom-right move increases it by one. To get from $(r_1, c_1)$ to $(r_2, c_2)$ we need exactly $d = r_2 - r_1$ moves, of which exactly $k = c_2 - c_1$ go right. This is possible only for $0 \le k \le d$, and then any choice of which moves go right is a valid path:

$$\text{ways} = \binom{d}{k}.$$

Labels up to $10^9$ lie in rows below 45000, so factorials up to 50000 are enough.

## Edge cases

- The end above the start, or too far left or right: 0.
- $s = e$: one way, the empty path.
- The float-free row computation uses `isqrt` and fixes the off-by-one explicitly.
- The pyramid never restricts a path between two valid cells - columns stay within their rows automatically.

## Dry run

- `1 -> 5`: cells $(1, 1)$ and $(3, 2)$, so $d = 2$, $k = 1$: $\binom{2}{1} = 2$.
- `2 -> 7`: cells $(2, 1)$ and $(4, 1)$, $d = 2$, $k = 0$: 1.
- `5 -> 3`: the end is above the start: 0.
