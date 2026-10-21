---
topic: Geometry
subtopic: Halving the vertex count down to a triangle
time: $O(N)$ per test case, all of it input reading
space: $O(1)$
---
The coordinates are **irrelevant** — the answer depends only on $N$. That is the whole insight, and strict convexity is what licenses it: any set of vertices in convex position forms a simple non-degenerate polygon in their cyclic order, so a candidate child is feasible purely combinatorially.

A child's sides are chords of the parent, so its vertices are parent vertices and consecutive chosen vertices are **non-adjacent** in the parent. Choosing $k$ vertices cyclically from $N$ with every gap at least $2$ needs $N \geq 2k$, so

$$k \leq \left\lfloor \frac{N}{2} \right\rfloor$$

and that bound is attained by taking every second vertex. A polygon also needs $k \geq 3$, which is where the chain stops.

Since larger children can only help — more sides now, and a weakly larger budget for the next step — the greedy "always halve" is optimal, and the answer is

$$N + \left\lfloor \frac{N}{2} \right\rfloor + \left\lfloor \frac{N}{4} \right\rfloor + \cdots$$

truncated at the last term that is still at least $3$. The chain is $O(\log N)$ long.

The two samples sit on either side of the cutoff. A quadrilateral has $\lfloor 4/2 \rfloor = 2 < 3$, so it has no child at all and the answer is just $4$ — note the sample's quadrilateral is deliberately drawn as a thin sliver, which changes nothing. The heptagon gives $\lfloor 7/2 \rfloor = 3$, a triangle, and then $\lfloor 3/2 \rfloor = 1$ stops the chain: $7 + 3 = 10$.

The real work is I/O: $\sum N \leq 2 \times 10^6$ vertex pairs must be read and discarded quickly, so read the whole stream at once rather than parsing per line.

## Edge cases

- **The coordinates are irrelevant.** Only the vertex count matters, so all $2N$ coordinate tokens are skipped wholesale — strict convexity is what guarantees the geometry always permits the counting bound.
- **Each side of a child must be a chord, never a side, of the parent**, so every child edge skips at least one parent vertex — which caps a child at $\lfloor N/2 \rfloor$ vertices and makes the chain a halving sequence.
- **The chain stops below $3$**, since a polygon needs three vertices: $N = 4$ contributes only $4$ (its child would have $2$), while $N = 7$ gives $7 + 3 = 10$.
- **Halving floors**: $7 \to 3$, not $3.5$, so odd counts lose the fractional vertex.
- **$N \geq 3$ is guaranteed**, so the loop always runs at least once and the answer is never $0$.
- **Sum of $N$ up to $2 \cdot 10^6$** coordinate pairs to skip, so the file must be read in one buffered call even though nearly all of it is discarded.

## Dry run

| $N$ | chain of polygons | total sides |
|---:|---|---:|
| 4 | $4$ (child would need $2$ vertices) | `4` |
| 7 | $7 \to 3$ (then $1$, too small) | `10` |

For $N = 7$ the child is a triangle on every second vertex; its own child would have one vertex, so the chain ends.
