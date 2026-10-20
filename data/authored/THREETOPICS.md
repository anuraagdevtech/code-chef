---
topic: Conditionals & Case Work
subtopic: Membership test
time: $O(1)$
space: $O(1)$
---
Chef prepared topics $A$, $B$ and $C$, and was handed topic $X$. He has a chance precisely when $X$ is one of the three he prepared:

$$X \in \{A, B, C\}$$

In Python that is literally `x in (a, b, c)`, which reads exactly like the mathematics and avoids the three-way `or` chain that is easy to mistype — writing `x == a or x == b or c` is a classic bug, since the bare `c` is truthy for every non-zero value and would answer `Yes` always.

The guarantee that $A$, $B$ and $C$ are distinct is a convenience, not something the solution depends on; a membership test behaves identically with duplicates.

The one genuine gotcha is the input format. Unlike almost every other problem in this set, there is **no $T$ on the first line** — the input is a single line of four integers, one test case. The output section's "for each testcase" phrasing is boilerplate left over from a template and contradicts the input section. Reading a leading $T$ here would consume $A$ as the count and produce nonsense, so the format is worth confirming against the sample before writing the loop.
