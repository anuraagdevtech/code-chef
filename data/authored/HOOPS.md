---
topic: Basic Math
subtopic: Where two converging sequences meet
time: $O(1)$ per test case
space: $O(1)$
---
You occupy hoops $1, 2, 3, \ldots$ from the left while your friend takes $N, N-1, N-2, \ldots$ from the right. The two sequences march toward each other and the game stops the moment one of you finds the next hoop already taken.

Since $N$ is odd, the two sequences meet exactly at the middle hoop

$$\frac{N+1}{2}$$

and because **you** jump first, you are the one who claims it. Your friend then has nowhere to go, so that middle hoop is the last one jumped into.

Tracing $N = 5$: you take $1$, friend takes $5$, you take $2$, friend takes $4$, you take $3$ — and now the friend's next target would be $3$, already yours. The answer is $3 = (5+1)/2$.

The oddness of $N$ is what makes this clean. With an even $N$ the two sequences would pass each other without landing on a shared hoop, and the stopping condition would need more care — so the constraint is load-bearing, not decoration.

Sample case 1 is the degenerate $N = 1$: you jump into the only hoop and your friend is immediately stuck, giving $1$. The formula handles it without a special case.

In integers this is `(n + 1) // 2`, and with $T$ up to $10^5$ the bulk read matters more than the arithmetic.
