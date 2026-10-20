---
topic: Sets
subtopic: Set difference
time: $O(1)$ per test case
space: $O(1)$
---
Chef loses to his rival in any category they share and beats everyone else, so he takes gold in exactly those of his own races that the rival is **not** entered in. That is a set difference:

$$\left|\{X, Y\} \setminus \{A, B\}\right|$$

In Python this is literally `len({x, y} - {a, b})`, which reads as the mathematics does and sidesteps the comparison chain the problem invites. Writing it by hand means testing each of Chef's two races against each of the rival's two — four comparisons — and it is easy to mis-pair one of them.

Note the sets are genuinely sets: the constraints promise $X \neq Y$ and $A \neq B$, so each has exactly two elements and no duplicate-collapsing surprises arise.

The three samples walk through the whole range of answers. No overlap gives $2$ gold medals; one shared category gives $1$; and identical entries give $0$, with the rival shutting Chef out entirely.

Framing a problem as set operations — difference, intersection, union — rather than as nested conditionals is a habit that pays off well beyond four races: the expression stays the same size as the sets grow.
