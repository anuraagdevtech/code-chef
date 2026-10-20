---
topic: Basic Math
subtopic: Maximum of a fixed set
time: $O(1)$ per test case
space: $O(1)$
---
The final score is the longest of the three throws, so the answer is $\max(A, B, C)$ — a single built-in call.

Python's `max` takes any number of positional arguments, so `max(a, b, c)` works directly without building a list. Writing a manual chain of comparisons would also work but invites the usual mistakes: forgetting to seed the running maximum with the first value, or initialising it to $0$, which is safe here only because all distances are at least $1$. Seeding from the data rather than from a magic constant is the habit that survives into problems where negatives are allowed.

Ties need no special handling. The maximum of equal values is that value, so sample case 2 with three throws of $32$ simply returns $32$. Nothing in the problem distinguishes *which* throw produced the best distance, only its length.

The $O(1)$ bound is because the count of throws is fixed at three; for $n$ throws this would be the usual $O(n)$ single-pass scan.
