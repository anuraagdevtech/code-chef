---
topic: Basic Math
subtopic: Percentage change without floating point
time: $O(1)$ per test case
space: $O(1)$
---
A change of $C\%$ takes the price from $S$ to

$$S \cdot \left(1 + \frac{C}{100}\right) = \frac{S(100 + C)}{100}$$

and Chef buys when that lands in $[A, B]$.

The right way to test this is to **avoid the division entirely**. Multiply the whole comparison through by $100$:

$$100A \leq S(100 + C) \leq 100B$$

Now everything is an integer and the test is exact. Computing the new price as a float and comparing is where this problem is lost: the result is frequently non-integral, and rounding it — in either direction — changes the answer at the boundaries.

Sample case 3 is built precisely on that. $183$ dropping $17\%$ gives $183 \times 83 = 15189$, against a lower bound of $152 \times 100 = 15200$. The true price is $151.89$, just **below** the range, so the answer is `No`. A solution that rounded to $152$ would answer `Yes`.

Note $C$ may be negative, which the formula handles naturally — $100 + C$ simply shrinks. Sample case 2 is a $7\%$ drop to exactly $93$, falling one rupee short of the range.

The range comparison is inclusive at both ends, and Python's chained comparison expresses it in one line.
