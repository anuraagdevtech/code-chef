---
topic: Binary Search
subtopic: Feasibility check with prefix sums
time: $O((N + Q) \log N)$ per test case
space: $O(N)$
---
Suppose we aim to end with $m$ snakes of length at least $K$. Two greedy choices are forced.

**Keep the $m$ longest.** They start closest to the target, so any other choice needs at least as much feeding.

**Feed them the $N - m$ shortest.** Each snake eaten adds exactly $1$ to its eater, so the sacrifices are interchangeable — only their *count* matters.

So after sorting, the kept snakes are the suffix $L[N-m \ldots N-1]$, and the total feeding needed is the sum of their shortfalls:

$$\text{deficit}(m) = \sum_{i=N-m}^{N-1} \max(0,\ K - L_i)$$

which must not exceed the $N - m$ available meals.

As $m$ grows the deficit rises while the supply falls, so feasibility is **monotone** — binary search on $m$ answers each query in $O(\log N)$.

The deficit itself is computed in $O(\log N)$ rather than $O(m)$: binary search for the first index whose length already reaches $K$, then take a prefix-sum slice of everything below it. Without that, the queries would be $O(NQ)$ overall.

The eating rule $L_i \geq L_j$ is automatically respected, since every kept snake is at least as long as every sacrificed one.

Sample case 1 with $K = 10$ keeps $[9,10,21]$: only the $9$ falls short, by $1$, and two meals are available — so $3$ snakes. Pushing to $m = 4$ would need $3$ meals with only $1$ left. At $K = 15$ even $m = 2$ needs $5$ meals against $3$, so the answer drops to $1$.

Sample case 2 asks for length $100$ from snakes topping out at $5$, needing $95$ meals from four — so $0$.
