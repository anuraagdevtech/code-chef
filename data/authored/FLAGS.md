---
topic: Combinatorics
subtopic: Chromatic polynomials of small graphs
time: $O(1)$ per test case
space: $O(1)$
---
Each pattern is a map whose regions must be coloured so that regions **sharing an edge** differ. That is exactly proper graph colouring, so each pattern contributes its graph's **chromatic polynomial** evaluated at $N$, and the answer is the sum over the five patterns.

Reading the adjacency structure off the five patterns:

| Pattern | Region graph | Colourings |
|---|---|---|
| three vertical stripes | path $1{-}2{-}3$ | $N(N-1)^2$ |
| three horizontal stripes | path $1{-}2{-}3$ | $N(N-1)^2$ |
| L-shape split | triangle $K_3$ | $N(N-1)(N-2)$ |
| pinwheel of three | triangle $K_3$ | $N(N-1)(N-2)$ |
| four-region block | $K_4$ minus one edge | $N(N-1)(N-2)^2$ |

Summing gives

$$2N(N-1)^2 \;+\; 2N(N-1)(N-2) \;+\; N(N-1)(N-2)^2$$

The standard results behind the table: a **path** of $k$ vertices has $N(N-1)^{k-1}$ colourings, since each vertex after the first need only differ from its single predecessor; a **triangle** has $N(N-1)(N-2)$, all three being mutually adjacent; and $K_4$ minus an edge — two triangles sharing an edge — has $N(N-1)(N-2)^2$, because the shared edge takes $N(N-1)$ and each remaining vertex avoids both of its endpoints.

Checking against the samples confirms the reading. $N = 1$ gives $0$: with one colour, even a single shared edge is unsatisfiable. $N = 2$ gives $4$ — only the two striped patterns are two-colourable, at $2$ each, while the three patterns containing a triangle contribute nothing. $N = 3$ gives $12 + 12 + 6 + 6 + 6 = 42$.

Evaluating the polynomial is $O(1)$, which matters at $T = 10^4$.
