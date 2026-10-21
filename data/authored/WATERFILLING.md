---
topic: Conditionals & Case Work
subtopic: Counting flags instead of enumerating cases
time: $O(1)$ per test case
space: $O(1)$
---
Chef refills when **at least two** of the three bottles are empty. Each $B_i$ is $1$ for full and $0$ for empty, so an empty bottle is a zero.

The naive route is to enumerate the eight possible triples, or to write a chain of `or`s covering each pair that could be empty. Both work but scale badly and are easy to get wrong. The cleaner framing: count the empties and compare against the threshold.

Because the values are exactly $0$ and $1$, the number of *full* bottles is just $B_1 + B_2 + B_3$, so the number of empty ones is $3 - (B_1 + B_2 + B_3)$. The refill condition "at least two empty" becomes

$$3 - (B_1 + B_2 + B_3) \geq 2 \quad\Longleftrightarrow\quad B_1 + B_2 + B_3 \leq 1$$

In words: Chef fills up exactly when **at most one** bottle is full — which is just the problem's own second sentence read from the other side. Encoding a 0/1 flag array as a sum is a trick worth keeping; it turns case analysis into arithmetic.

## Edge cases

- **All three empty** ($0\,0\,0$): zero full tanks, so filling time.
- **All three full** ($1\,1\,1$): three full, so not now.
- **Exactly one full** ($0\,1\,0$): two tanks are empty, which meets the "at least two" requirement — filling time. This is the boundary.
- **Exactly two full** ($1\,1\,0$): only one empty, so not now — the other side of the same boundary.
- Summing the three flags collapses all eight patterns into one comparison, so there is no case list to get wrong; "at least two empty" is simply "at most one full".

## Dry run

| $B_1$ | $B_2$ | $B_3$ | full tanks | $\leq 1$? | output |
|---:|---:|---:|---:|:---:|---|
| 0 | 0 | 0 | 0 | yes | `Water filling time` |
| 1 | 1 | 1 | 3 | no | `Not now` |
| 1 | 1 | 0 | 2 | no | `Not now` |
| 0 | 1 | 0 | 1 | yes | `Water filling time` |
| 0 | 1 | 1 | 2 | no | `Not now` |

Rows 4 and 3 sit either side of the threshold: one full tank passes, two do not.
