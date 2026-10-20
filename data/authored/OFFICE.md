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
