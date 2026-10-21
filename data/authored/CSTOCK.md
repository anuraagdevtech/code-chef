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

## Edge cases

- **A negative change** (the last two rows): the price falls, and the formula handles it because $100 + C$ stays non-negative for $C \geq -100$. At $C = -100$ exactly the new price is $0$.
- **Scaling by $100$ removes the division entirely.** Computing $S(1 + C/100)$ as a float risks a rounding error at precisely the boundary cases the problem is built around; multiplying both sides by $100$ keeps everything in integers.
- **Exactly at $A$ or $B$**: inside the range, so the comparisons are non-strict.
- **$S = 0$**: the new price is $0$, and since $A$ may also be $0$ the answer can still be `Yes`.
- **$A \leq B$ is guaranteed**, so the range is never empty.

## Dry run

| $S$ | $C$ | $S(100+C)$ | $100A$ | $100B$ | inside? | output |
|---:|---:|---:|---:|---:|:---:|---|
| 100 | 7 | 10700 | 9300 | 10800 | yes | `Yes` |
| 100 | $-7$ | 9300 | 9400 | 10000 | no | `No` |
| 183 | $-17$ | 15189 | 15200 | 17200 | no | `No` |

Row 3 misses by $11$ hundredths of a rupee, which is exactly why the comparison must stay exact.
