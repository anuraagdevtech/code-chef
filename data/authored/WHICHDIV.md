---
topic: Conditionals & Case Work
subtopic: Ordered threshold ladder
time: $O(1)$ per test case
space: $O(1)$
---
Three bands, read off directly:

- Division 1: $R \geq 2000$
- Division 2: $1600 \leq R < 2000$
- Division 3: $R < 1600$

Testing them from the top down lets each branch assume the previous ones failed, so the upper bound of each band is implied and only the lower bound needs stating. That collapses the middle band's two-sided condition into a single comparison.

The boundaries are inclusive at the **bottom** of each division, which is the detail to get right: a rating of exactly $2000$ is Division 1, and exactly $1600$ is Division 2. Using strict `>` would misplace both.

The samples deliberately avoid the boundaries — $1500$, $4000$, $1900$ all sit comfortably inside their bands — so they will not catch an off-by-one here. Worth checking $1600$ and $2000$ by hand before submitting.

The constraint $1000 \leq R \leq 4500$ means no rating falls outside the three bands, so the final `else` is genuinely exhaustive and no error case is needed.

## Edge cases

- **$R = 2000$ exactly**: division $1$, since the bands are inclusive at their lower edge.
- **$R = 1600$ exactly**: division $2$; **$R = 1599$**: division $3$. The two together pin the lower boundary.
- **Extremes** ($R = 1000$ and $R = 4500$): divisions $3$ and $1$.
- **Testing from the top down with $\geq$** is what makes the inclusive edges come out right; the same ladder written ascending with $<$ needs the complementary bounds and is easier to get wrong by one.

## Dry run

| $R$ | $\geq 2000$? | $\geq 1600$? | output |
|---:|:---:|:---:|---|
| 1500 | no | no | `3` |
| 4000 | yes | — | `1` |
| 1900 | no | yes | `2` |
