---
topic: Arrays
subtopic: Sparse-table range min and max with end aggregates
time: $O(N \log N + Q)$
space: $O(N \log N)$
---
Lighting the free ends of $L \ldots R$ sets up two phases. The first stick to reach the shared rear is the fastest one, so the junction ignites at

$$m = \min(b_L, \ldots, b_R)$$

and from that instant **every** stick is burning from the rear.

- A **lit** stick $i$ has already consumed $m$ of its length from the front, so $b_i - m$ remains; now burning from both ends it finishes in half that, giving $m + \frac{b_i - m}{2} = \frac{b_i + m}{2}$.
- An **unlit** stick $j$ only starts at time $m$, from one end, finishing at $m + b_j$.

So the answer is the larger of the two worst cases:

$$\max\!\left(\frac{\max_{i \in [L,R]} b_i + m}{2},\ m + \max_{j \notin [L,R]} b_j\right)$$

with the second term dropped when the query covers the whole row. Note the unlit sticks can easily dominate, since they get no head start at all — in the worked example a modest unlit stick of $4$ outlasts the lit stick of $12$.

Each query needs a range minimum and maximum, so build sparse tables for both; the outside maximum is a prefix/suffix maximum, which is $O(1)$ per query. Every value is an integer or a half-integer, since $b_i + m$ is divided by $2$, so one decimal place prints the answer exactly.

The input has **no leading $T$**: it is $N$, the burn times, $Q$, then the queries. Lighting a single stick of $5$ takes $5$ seconds; lighting both of $3$ and $5$ gives $\frac{5+3}{2} = 4$.

## Edge cases

- **The rear junction catches fire the instant the first lit stick burns through**, at time $\mathrm{first} = \min$ over the lit range — and from then on every other stick burns from both ends.
- **A lit stick finishes at $(b + \mathrm{first})/2$.** It has already burned $\mathrm{first}$ from the free end, leaving $b - \mathrm{first}$, which then halves.
- **An unlit stick finishes at $\mathrm{first} + b$**, since it only starts at the junction and burns its full length from one end — so the sticks *outside* the query range often dominate the answer.
- **The third example turns on exactly that**: the lit range alone gives $8.5$, but an unlit stick of length $4$ pushes the answer to $9.0$.
- **No sticks outside means no second term**, which the guard handles — and since $b_i \geq 1$, a maximum of $0$ really does mean the range covers everything.
- **The answer is a half-integer**, hence the single decimal place in the output.
- **There is no test-case count**: the input is $N$, the burn times, then $Q$ and the queries.
- **Sparse tables give both the range minimum and maximum in $O(1)$**, which keeps $10^5$ queries affordable alongside the prefix and suffix maxima for the outside.

## Dry run

Third example: burn times $3,4,2,1,5,7,9,7,10,5,12,3,1,1,2,1,3,2$ with the query $L = 4$, $R = 10$ (0-based).

| quantity | value |
|---|---:|
| minimum inside the range | 5 |
| maximum inside the range | 12 |
| lit sticks finish by $(12+5)/2$ | 8.5 |
| maximum outside the range | 4 |
| unlit sticks finish by $5 + 4$ | **9.0** |

Output `9.0`.
