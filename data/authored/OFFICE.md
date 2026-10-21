---
topic: Basic Math
subtopic: Direct formula
time: $O(1)$ per test case
space: $O(1)$
---
The week splits into three kinds of day. Monday through Thursday is four days at $X$ hours each, Friday is a single day at $Y$ hours, and the weekend contributes nothing. Summing them gives the whole answer in one expression:

$$\text{total} = 4X + Y$$

There is no loop to write and no edge case to guard. The constraint $Y < X$ is flavour — it makes Friday genuinely the lighter day — but the formula never depends on it, so no validation is needed.

The thing worth internalising is the counting itself: "Monday to Thursday" is four days, not five. Off-by-one on an inclusive day range is the classic slip, and reading it as $5X + Y$ would pass no sample at all. Checking against the first one: $X=10, Y=5$ gives $4 \cdot 10 + 5 = 45$.

## Edge cases

- **$Y < X$ is guaranteed**, so Friday is always the short day; the formula never needs to decide which day is shorter.
- **Smallest input** ($X = 2$, $Y = 1$): $4 \times 2 + 1 = 9$ hours.
- **Largest input** ($X = 12$, $Y = 11$): $4 \times 12 + 11 = 59$ hours.
- **The weekend contributes nothing** — the count is four full days plus Friday, not five plus two, so a "7 days" reflex overcounts.

## Dry run

| $X$ | $Y$ | $4X$ (Mon&ndash;Thu) | $+Y$ (Fri) | output |
|---:|---:|---:|---:|---|
| 10 | 5 | 40 | 45 | `45` |
| 12 | 2 | 48 | 50 | `50` |
| 8 | 7 | 32 | 39 | `39` |
