---
topic: Basic Math
subtopic: Range of achievable sums
time: $O(1)$ per test case
space: $O(1)$
---
Adding two values from $\{L, \ldots, R\}$, with repetition allowed, gives a smallest sum of $L + L = 2L$ and a largest of $R + R = 2R$.

The important claim is that **every** integer in between is reachable. Starting from $(L, L)$, raising one of the two chosen values by one increases the sum by exactly one, and either value may be raised until it hits $R$. So the sums sweep the whole interval with no gaps, and the count is

$$2R - 2L + 1$$

Confirming that there are no gaps is the step that matters. The instinct that pair sums might skip values is reasonable in general — it is true for a set like $\{1, 10\}$ — but a **contiguous** range of integers produces a contiguous range of sums, precisely because unit steps are available.

The "not necessarily distinct" clause is what makes $2L$ and $2R$ themselves reachable. Requiring distinct values would shrink the range to $[2L+1, 2R-1]$ and make $L = R$ a degenerate case with no valid pair at all.

Sample case 1 has $L = R = 2$: the only sum is $4$, and the formula gives $4 - 4 + 1 = 1$. Sample case 2 spans $4$ to $6$ for $3$ reachable values.

The usual fencepost applies — the $+1$ is needed because both endpoints are included.
