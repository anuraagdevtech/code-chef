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

## Edge cases

- **No overlap** ($\{4,3\}$ against $\{1,2\}$): both races are won, so $2$.
- **Complete overlap** ($\{2,1\}$ against $\{1,2\}$): neither, so $0$. This row also shows that order inside a pair is irrelevant — the sets are equal even though the numbers are listed in the opposite order.
- **Partial overlap**: exactly $1$.
- **$X \neq Y$ and $A \neq B$ are guaranteed**, so each pair really has two distinct members and the answer is $2$ minus the overlap size — no deduplication inside a pair is needed.
- The answer is always $0$, $1$ or $2$.

## Dry run

| Chef's races | rival's races | difference | output |
|---|---|---|---:|
| $\{4, 3\}$ | $\{1, 2\}$ | $\{4, 3\}$ | `2` |
| $\{4, 2\}$ | $\{1, 2\}$ | $\{4\}$ | `1` |
| $\{2, 1\}$ | $\{1, 2\}$ | $\varnothing$ | `0` |
