---
topic: Basic Math
subtopic: Floor division
time: $O(1)$ per test case
space: $O(1)$
---
Chef has $X$ rupees and each chocolate costs $Y$, so he can afford

$$\left\lfloor \frac{X}{Y} \right\rfloor$$

chocolates. Leftover change buys nothing, so the division rounds **down**.

This is the canonical "how many whole things fit in a fixed budget" question, and it is the floor counterpart to the ceiling problems elsewhere in this set. The distinguishing phrase is *maximum number obtainable from a fixed supply*, as against *minimum number of containers needed to hold everything*. One wastes the remainder; the other pays for it.

Python's `//` is floor division on non-negative integers, so `x // y` is the whole solution. Avoid `int(x / y)` — it routes through a float and begins to misreport once the operands exceed $2^{53}$, even though it happens to agree here.

Sample case 1 is the can't-afford-one case: $5$ rupees against a $10$-rupee chocolate gives $0$, not an error and not $1$. Case 4 is the other extreme, where a unit price of $1$ means the budget is spent exactly.
