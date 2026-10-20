---
topic: Prefix Sums
subtopic: Running total compared against the index
time: $O(N)$ per test case
space: $O(1)$
---
Strike rate after $i$ balls is $\frac{\text{runs}}{i} \times 100$, so it equals exactly $100$ precisely when the runs scored so far equal the balls faced:

$$\text{prefix sum}_i = i$$

No division is needed at all — clearing it turns a floating-point comparison into an integer identity, which is both exact and faster. Comparing `total / i * 100 == 100` would be the fragile version.

So the solution is a single pass maintaining a running total, incrementing a counter whenever that total matches the current ball number. Only the running sum needs storing, so this is $O(N)$ time and $O(1)$ space — no prefix array required, since each prefix is consumed immediately.

Sample case 3 is the all-ones case where the condition holds after every ball, giving $3$. Sample case 1 matches at balls $1$ and $3$ — after $[1]$ the total is $1$, and after $[1,0,2]$ it is $3$ — giving $2$. Sample case 2 never matches, since the opening $2$ runs off a single ball puts the total permanently ahead.

The efficiency constraints are worth reading: $T$ reaches $10^5$ and $N$ reaches $10^5$, but the **sum of $N$** is capped at $10^6$. That bound is the setter saying a linear pass per test case is intended and safe, while anything quadratic is not. Reading the whole input in one go rather than line by line matters at this volume.
