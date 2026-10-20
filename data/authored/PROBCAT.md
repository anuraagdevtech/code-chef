---
topic: Conditionals & Case Work
subtopic: Ordered threshold ladder
time: $O(1)$ per test case
space: $O(1)$
---
Three bands, read straight from the statement:

- `Easy` for $1 \leq x < 100$
- `Medium` for $100 \leq x < 200$
- `Hard` for $200 \leq x \leq 300$

Testing from the bottom up lets each branch assume the earlier ones failed, so only the upper bound of each band needs stating.

The boundaries are **exclusive at the top** of the first two bands and inclusive at the bottom — so $x = 100$ is `Medium`, not `Easy`, and $x = 200$ is `Hard`. Sample case 3 checks the upper boundary with $x = 201$, but $100$ and $200$ themselves are not in the samples, so they are worth testing by hand before submitting.

The statement says explicitly that **the output is case sensitive**, which is unusual in this set — most neighbouring problems accept any casing. So `Easy` must be written with exactly that capitalisation, not `EASY` or `easy`.

The constraint $1 \leq x \leq 300$ means every input falls into one of the three bands, so the final `else` is genuinely exhaustive and no fallback is needed.
