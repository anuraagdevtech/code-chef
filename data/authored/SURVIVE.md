---
topic: Basic Math
subtopic: Ceiling division with a running feasibility check
time: $O(S)$ per test case
space: $O(1)$
---
Two separate questions: *how few* purchases suffice, and *whether* any schedule works at all.

The count is pure arithmetic. Surviving $S$ days costs $SK$ chocolates and every purchase yields $N$, so

$$\text{purchases} = \left\lceil \frac{SK}{N} \right\rceil$$

and boxes keep, so leftovers carry forward and nothing is wasted beyond the final box.

Feasibility is the Sunday constraint. Day $1$ is Monday, so Sundays fall on days $7, 14, \ldots$, and by day $d$ the shop has been open on $d - \lfloor d/7 \rfloor$ days. Since you cannot eat what you have not bought, every prefix must balance:

$$\left(d - \left\lfloor \frac{d}{7} \right\rfloor\right) N \;\geq\; dK \qquad \text{for all } 1 \leq d \leq S$$

Checking only $d = S$ is not obviously enough, so with $S \leq 1000$ the honest thing is to check every prefix. (It happens that $\lfloor d/7 \rfloor / d$ peaks at $1/7$ on multiples of $7$, so for $S \geq 7$ the condition reduces to $6N \geq 7K$ — but the loop needs no such reasoning.)

Buying as early as possible is optimal and needs no scheduling logic: if the prefix condition holds everywhere, buying on the first $\lceil SK/N \rceil$ open days both meets the daily demand and uses the minimum number of purchases.

The samples sit on either side. With $N = 16$, $K = 2$, $S = 10$ the need is $20$ chocolates, so $2$ boxes, and supply never lags. With $N = 50$, $K = 48$, $S = 7$ the week has only $6$ open days, giving at most $300$ chocolates against a need of $336$ — the single Sunday is what makes it impossible, so $-1$.
