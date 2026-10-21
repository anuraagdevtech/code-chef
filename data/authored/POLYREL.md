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
