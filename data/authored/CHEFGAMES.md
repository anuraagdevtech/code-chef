---
topic: Conditionals & Case Work
subtopic: Reducing an AND over flags to a sum
time: $O(1)$ per test case
space: $O(1)$
---
The ball is `IN` only when **every** referee calls it inside. Read the encoding carefully, because it is inverted from the intuitive one: $R_i = 0$ means *inside* limits and $R_i = 1$ means *outside*. Skimming this is the main way to lose the problem.

So the condition is $R_1 = R_2 = R_3 = R_4 = 0$. Rather than writing a four-way `and`, note that each $R_i$ is non-negative, so their sum is zero exactly when all of them are zero:

$$R_1 + R_2 + R_3 + R_4 = 0$$

Equivalently, a single `1` anywhere makes the sum positive and the ball is `OUT`. This "sum of non-negative flags is zero iff all are zero" reduction scales to any number of referees without changing the code, and it is the same idea used in the water-bottle problem, just with the threshold at zero instead of one.

Python's built-in `any` over the raw values would read just as well; the sum is used here because the values arrive as integers already.

## Edge cases

- **All four zero**: the only way to answer `IN`, since every rating must be inside its limit.
- **A single one anywhere**: `OUT`. The sample puts it in the last position ($0\,0\,0\,1$) precisely because a check that only inspects the first value or two would pass it.
- **All four one**: `OUT`.
- **The polarity is inverted** from the obvious reading: a $1$ marks a *violation*, not a pass, so `IN` is the all-zero case. Reading it the other way flips every answer.
- Summing the flags turns a four-way AND into one comparison against zero, which is harder to get subtly wrong than four chained conditions.

## Dry run

| $R_1$ | $R_2$ | $R_3$ | $R_4$ | sum | sum $= 0$? | output |
|---:|---:|---:|---:|---:|:---:|---|
| 1 | 1 | 0 | 0 | 2 | no | `OUT` |
| 0 | 0 | 0 | 0 | 0 | yes | `IN` |
| 0 | 0 | 0 | 1 | 1 | no | `OUT` |
| 1 | 1 | 1 | 1 | 4 | no | `OUT` |

Only row 2 clears every limit.
