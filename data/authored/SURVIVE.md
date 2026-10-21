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

## Edge cases

- **Sundays make the supply uneven, so a total count is not enough.** By day $d$ only $d - \lfloor d/7 \rfloor$ open days have passed, capping the chocolates available at $(d - \lfloor d/7 \rfloor) N$ against the $dK$ eaten — and this must hold for *every* prefix, not just for $S$.
- **Checking only the final day is wrong**, because a shortfall can occur mid-way and be hidden by later open days. The feasibility test is a running one.
- **The count starts on Monday**, so the Sundays among the first $d$ days number exactly $\lfloor d/7 \rfloor$ — day $7$ is the first.
- **Buying and eating on the same day is allowed**, which is what makes day $1$ survivable whenever $N \geq K$.
- **The answer is $\lceil SK/N \rceil$** when feasible, computed as `-(-s * k // n)` to stay in exact integers.
- **The second sample fails on day $7$**: six open days supply $300$ chocolates against $336$ needed, so `-1` — even though days $1$ through $6$ are each fine.
- **$S \leq 1000$** makes the day-by-day check trivially cheap.

## Dry run

First sample: $N = 16$ per box, $K = 2$ per day, $S = 10$ days.

| day $d$ | open days so far | chocolates available | eaten by then | ok? |
|---:|---:|---:|---:|:---:|
| 1 | 1 | 16 | 2 | ✓ |
| 6 | 6 | 96 | 12 | ✓ |
| 7 | 6 | 96 | 14 | ✓ |
| 10 | 9 | 144 | 20 | ✓ |

Feasible, so the answer is $\lceil 10 \cdot 2 / 16 \rceil = $ `2` buying days.
