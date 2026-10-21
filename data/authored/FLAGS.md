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

## Edge cases

- **$N = 1$ gives $0$**, since every one of the five patterns has at least two regions that touch and so needs at least two colours. The `max(0, …)` guard matters here because the $(n-2)$ factors turn negative at $n = 1$.
- **$N = 2$ gives $4$**: only the two three-stripe patterns are colourable, contributing $2 n (n-1)^2 = 4$, while the patterns needing three distinct colours contribute $0$ through their $(n-2)$ factors.
- **The three term shapes are chromatic counts of the five patterns**: two patterns count $n(n-1)^2$ each, two count $n(n-1)(n-2)$ each, and one counts $n(n-1)(n-2)^2$.
- **For $N \geq 2$ every term is non-negative**, so the clamp only ever fires on the single $N = 1$ case.
- **Adjacent regions must differ**, which is why consecutive factors drop by one; non-adjacent regions may repeat a colour, which is why the squared factors appear.
- **$N$ up to $10^4$** puts the total near $10^{16}$ — past 32-bit, and the cube is the dominant term.

## Dry run

| $N$ | $2n(n-1)^2$ | $2n(n-1)(n-2)$ | $n(n-1)(n-2)^2$ | total |
|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | `0` |
| 2 | 4 | 0 | 0 | `4` |
| 3 | 24 | 12 | 6 | `42` |

At $N = 2$ only the stripe patterns survive; the others need a third colour.
