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
