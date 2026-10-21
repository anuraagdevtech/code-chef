---
topic: Greedy
subtopic: Spending a budget on the smallest gaps first
time: $O(N + V)$ per test case
space: $O(V)$
---
The MEX is the smallest non-negative integer absent from the multiset, so raising it to $m$ requires **every** value $0, 1, \ldots, m-1$ to be present. Values at or above $m$ are irrelevant.

So walk upward from $0$, and whenever a value is missing, spend one of the $K$ additions on it. Continue until the budget runs out; the first value that cannot be supplied is the answer.

Greedy is forced rather than chosen here — there is no decision to make. Every missing value below the target must be filled, so the order of spending is immaterial and walking upward simply stops at the right place.

Note what makes this cheap: duplicates in $S$ are useless, so only **membership** matters, recorded in a boolean array indexed by value.

The ceiling on the answer is $\max(S_i) + K + 1$: beyond that, even spending every addition cannot bridge the gap. With $S_i \leq 2 \times 10^5$ and $K \leq 10^5$ the scan is bounded by about $3 \times 10^5$, which keeps the loop safely terminated.

The samples cover the range. $\{1,0,2\}$ with $K=0$ already holds $0,1,2$ and stops at $3$. The same set with $K=1$ buys the $3$ and reaches $4$. $\{2,5,4,9\}$ with $K=3$ is the interesting one: the gaps at $0$, $1$ and $3$ consume exactly the budget, yielding $0$–$5$ present and a MEX of $6$ — note the $9$ contributes nothing.

$\{3,4\}$ with $K=0$ answers $0$, since $0$ itself is missing and unaffordable.
