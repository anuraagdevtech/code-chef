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

## Edge cases

- **$X$ matching each position in turn** — the first, middle or last of $A, B, C$ — must all answer `Yes`, so the test has to cover all three and not just one.
- **$X$ matching none** ($A,B,C = 4,6,8$ with $X = 5$): `No`.
- **$A, B, C$ are guaranteed distinct**, so there are no duplicates to deduplicate and the membership test needs no counting.
- **Input shape**: a single test case — one line of four integers with *no* leading $T$. The two sample blocks are two separate runs, not two cases in one run.

## Dry run

Sample 1: $A,B,C = 2,3,7$ and $X = 3$.

| step | value |
|---|---|
| topics | $\{2, 3, 7\}$ |
| $X$ | $3$ |
| $X$ in topics? | yes (matches $B$) |
| output | `Yes` |

Sample 2: $A,B,C = 4,6,8$ and $X = 5$ — $5$ is in none of them, so `No`.
