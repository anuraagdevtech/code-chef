---
topic: Arrays
subtopic: Ordered condition checks
time: $O(N)$ per test case
space: $O(1)$
---
Three rules, and the **order** in which they are tested is what makes the solution correct:

1. All $N$ tests pass → $100$.
2. Otherwise, all of the first $M$ pass → $K$.
3. Otherwise → $0$.

Rule 2 carries the qualifier $M < N$, so a submission passing everything scores $100$, never $K$. Checking the prefix first would wrongly award $K$ to a perfect submission — sample case 3 is there to catch exactly that, with all four tests passing and the answer $100$.

In Python each check is a single `all(...)` over a slice, which short-circuits on the first failure:

- `all(v == 1 for v in a)` for the full set
- `all(v == 1 for v in a[:m])` for the prefix

Sample case 2 is the partial-credit case: the first two pass and the third fails, scoring $K = 50$.

Sample case 4 is the one that punishes a loose reading. Four of five tests pass — more than in case 2 — yet the score is $0$, because the failure sits at position $3$, *inside* the first $M = 3$. Partial credit depends on an unbroken **prefix**, not on a count of passes. A solution comparing the number of passes against $M$ would wrongly award $30$ here.

The constraint $M < N$ guarantees the two rules never collide, so there is no ambiguity about which applies.
