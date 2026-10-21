---
topic: Dynamic Programming
subtopic: Partition DP with an incrementally maintained segment cost
time: $O(N^2)$ per test case
space: $O(N)$
---
A table seats a **contiguous** block of guests, so a seating plan is nothing more than a partition of $1 \ldots N$ into consecutive segments. That makes this the classic one-dimensional partition DP:

$$\mathrm{dp}[j] = \min_{0 \leq i < j} \bigl(\mathrm{dp}[i] + K + \mathrm{cost}(i+1, j)\bigr)$$

where $\mathrm{dp}[j]$ is the least inefficiency for the first $j$ guests and $\mathrm{cost}(l, r)$ counts the guests in that segment whose family also has another member there. Note what is counted: **guests**, not pairs. A family of three at one table contributes $3$, not $\binom{3}{2} = 3$ — the two coincide at three but diverge elsewhere, and a family of four contributes $4$, not $6$.

Evaluating $\mathrm{cost}$ for every pair of endpoints would be cubic. Instead fix the left end $i+1$ and extend $j$ rightwards, maintaining a family tally. When a family's count rises to $2$, **two** guests become arguers (the newcomer and the one already seated), so add $2$; on every count beyond that add $1$. That makes each cost update $O(1)$ and the whole DP $O(N^2)$, comfortable with $\sum N \leq 5000$.

$$\Delta\mathrm{cost} = \begin{cases} 2 & \text{count becomes } 2 \\ 1 & \text{count becomes } \geq 3 \\ 0 & \text{count becomes } 1\end{cases}$$

The trade-off is genuinely two-sided, as the samples show. With $K = 1$ and families `5 1 3 3 3`, splitting the three identical guests apart costs three tables but zero arguments, for $3$ — cheaper than one table at $1 + 3 = 4$. With $K = 14$ and `1 4 2 4 4`, tables are far too expensive, so everyone shares one at $14 + 3 = 17$. And with $K = 2$ and `3 5 4 5 1`, both plans tie at $4$: one table paying $2 + 2$, or two tables separating the pair of $5$s and paying $4 + 0$.
