---
topic: Basic Math
subtopic: Counting free items in a repeating group
time: $O(1)$ per test case
space: $O(1)$
---
Every fifth gift is free: Chef pays for four and the fifth comes at no cost, so the gifts arrive in repeating blocks of five costing four coins each.

Out of $N$ gifts, the number that are free is the number of complete blocks of five, $\lfloor N/5 \rfloor$, so the coins needed are

$$N - \left\lfloor \frac{N}{5} \right\rfloor$$

The two samples pin down the boundary. With $N = 5$ exactly one gift is free, so $5 - 1 = 4$ coins. With $N = 4$ no block is complete, so nothing is free and all $4$ are paid — the same answer by a different route, which is what makes this pair a good test: an off-by-one in the block count makes one of them wrong.

A tempting alternative is $4 \lceil N/5 \rceil$, reasoning that each started block costs four coins. That over-charges a partial block: for $N = 6$ it gives $8$ when the true cost is $6 - 1 = 5$, since Chef pays for the sixth gift but has not reached another free one. Counting the *free* items and subtracting is the formulation that handles partial blocks correctly.

With $N$ up to $10^9$, iterating over the gifts is out of the question — but the closed form is $O(1)$ and Python's integers handle the magnitude without comment.
