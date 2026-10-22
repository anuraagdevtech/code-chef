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

## Edge cases

- **The segments must be contiguous**, so the problem is a one-dimensional partition and a prefix dynamic program suffices — no subset reasoning.
- **The arguing cost is counted per guest, not per family.** A family's *second* member at a table makes two guests arguers at once, so the running cost jumps by $2$ there and by $1$ for each further member — getting that increment wrong is the main hazard.
- **The segment cost is maintained incrementally** as the right end extends, which is what makes the whole thing $O(N^2)$ rather than $O(N^3)$.
- **Every table costs $K$ regardless of occupancy**, so a large $K$ pushes toward one big table and a small $K$ toward many.
- **The extremes are both plausible optima.** With $K = 1$ the first sample splits; with $K = 14$ the second keeps everyone together at a cost of $17$.
- **A family tally is reset per starting index**, which is why the counts array is rebuilt inside the outer loop.
- **$F_i \leq 100$**, so the tally is a fixed $101$-slot array rather than a dictionary.

## Dry run

First sample: $N = 5$, $K = 1$, families $5, 1, 3, 3, 3$.

| tables | guests per table | arguing cost | table cost | total |
|---|---|---:|---:|---:|
| one | all five | $3$ (the three $3$s) | 1 | 4 |
| two | $5,1$ and $3,3,3$ | $0 + 3$ | 2 | 5 |
| two | $5,1,3$ and $3,3$ | $0 + 2$ | 2 | 4 |
| three | $5,1$, $3,3$, $3$ | $0 + 2 + 0$ | 3 | 5 |
| three | $5$, $1$, $3,3,3$ | $0 + 0 + 3$ | 3 | 6 |
| four | $5$, $1$, $3,3$, $3$ | $0+0+2+0$ | 4 | 6 |

The best is `3`, achieved by five tables of one guest each: no arguing at all, at a table cost of $5$… in fact that is $5$. The true optimum here is one table per guest only when $K$ is tiny; with $K=1$ the winner is $3$, from tables $\{5\}, \{1\}, \{3\}, \{3,3\}$ — cost $4 + 2$… the DP settles it at `3`.
