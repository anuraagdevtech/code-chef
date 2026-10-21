---
topic: Combinatorics
subtopic: Capacity per value
time: $O(N)$ per test case
space: $O(N)$
---
Splitting $A_i$ into $x + y$ with both parts positive allows $x \in \{1, 2, \ldots, A_i - 1\}$, so a value $v$ offers exactly $v - 1$ distinct points: $(1, v-1)$ through $(v-1, 1)$.

Crucially, points coming from **different values never collide** — a point $(x,y)$ determines its source as $x + y$. So the values partition the problem completely and can be handled independently.

For a value $v$ occurring $c$ times, the number of distinct points obtainable is therefore limited by two things: how many copies there are, and how many distinct splits exist. So

$$\text{answer} = \sum_{v} \min\bigl(c_v,\ v - 1\bigr)$$

Both caps genuinely bind, and the first sample shows each. The value $2$ appears three times but admits only the single split $(1,1)$, so it contributes $1$ — surplus copies are wasted. The value $4$ appears twice and admits three splits, so both copies land distinctly and it contributes $2$. The value $6$ appears once, contributing $1$. Total $4$.

The second sample has two large values appearing once each, so each contributes a single point: $2$.

Note that $v = 2$ is the degenerate case, with only one legal split — a value of $2$ repeated many times still yields just one point, which is the main trap.

A `Counter` gives the multiplicities in one pass, and the sum is immediate. The statement's note about fast I/O matters at $N = 2 \times 10^5$ with $T$ up to $10$.
