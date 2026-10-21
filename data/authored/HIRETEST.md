---
topic: Strings
subtopic: Counting characters, then a two-branch rule
time: $O(N \cdot M)$ per test case
space: $O(N)$
---
For each candidate, count the full solves $F$ and the partial solves $P$ in their result string. The pass rule has two independent routes:

$$F \geq X \quad\text{or}\quad \bigl(F = X - 1 \text{ and } P \geq Y\bigr)$$

The second branch is narrow and precise: it applies at **exactly** $X-1$ full solves, not at "fewer than $X$". A candidate with $X-2$ full solves cannot compensate with any number of partials. Sample case 3 is built on this — one candidate with $X = 2$, zero full solves and three partials fails, because $0 \neq X - 1 = 1$.

Within the first test case, candidates 2 and 3 both have $F = 2 = X - 1$ and differ only in partials: $P = 2$ passes against $Y = 2$, while $P = 1$ does not. Those two rows isolate the second branch exactly.

The `U` characters never enter the rule, so they can be ignored entirely rather than counted.

Output formatting is the other thing to get right: the $N$ results are printed as a single line of digits with **no separators** — `1100`, not `1 1 0 0`. Joining the per-candidate characters and emitting one line per test case does it.

The constraint $1 \leq (X-1) + Y \leq M$ guarantees the second route is always attainable in principle, so neither branch is vacuous.

## Edge cases

- **The fallback needs *exactly* $X - 1$ full solves, not merely fewer.** The first case's fourth candidate `PPPFP` has one full and four partial solves against $X = 3$, and fails despite having far more than $Y = 2$ partials. Writing the condition as `full < x and partial >= y` accepts this row wrongly.
- **$X$ may be $1$**, which makes the fallback need zero full solves — the second case's `PUPP` qualifies on partials alone.
- **Nothing solved at all** (the second case's `UUUU`): a $0$.
- **Meeting the primary bar makes the partials irrelevant.** `FUFFP` has three full solves and is accepted without its partial count ever being consulted.
- **The output is one line of $N$ digits with no separators**, not $N$ separate lines — `1100`, not four lines.
- **$(X-1) + Y \leq M$ is guaranteed**, so the fallback is always attainable by some candidate in principle.

## Dry run

First sample: $N = 4$, $M = 5$, $X = 3$, $Y = 2$.

| candidate | full `F` | partial `P` | $\geq X$? | $= X{-}1$ and $\geq Y$? | digit |
|---|---:|---:|:---:|:---:|:---:|
| `FUFFP` | 3 | 1 | **yes** | — | 1 |
| `PFPFU` | 2 | 2 | no | yes ($2 = 2$, $2 \geq 2$) | 1 |
| `UPFFU` | 2 | 1 | no | no ($1 < 2$ partials) | 0 |
| `PPPFP` | 1 | 4 | no | no ($1 \neq 2$ full) | 0 |

Output `1100`. Rows 3 and 4 fail for different reasons: too few partials, and the wrong number of full solves.
