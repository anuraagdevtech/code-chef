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
