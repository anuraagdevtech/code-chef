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

## Edge cases

- **Points from different values never collide**, since $x + y = A_i$ differs — so each value's contribution can be counted on its own and simply summed.
- **A value $v$ offers only $v - 1$ distinct points**: $(1, v-1)$ through $(v-1, 1)$, because both parts must be strictly positive. That is the per-value ceiling.
- **The copies are the other ceiling**, so each value contributes $\min(\text{count}, v - 1)$ — and the sample has one row binding on each: the three $2$s are capped at $1$ point, while the two $4$s use both copies.
- **$A_i = 2$ is the tightest case**: the only split is $(1,1)$, so any number of $2$s yields a single point.
- **$A_i \geq 2$ is guaranteed**, so every value admits at least one split and no index is unusable.
- **Every index must be split** — there is no option to skip one — but a duplicate point simply does not add to the count.
- **$N$ up to $2 \times 10^5$** with the note to use fast I/O, so the whole input is read in one call.

## Dry run

First sample: $A = 2, 2, 4, 4, 2, 6$.

| value | copies | splits available ($v - 1$) | points contributed |
|---:|---:|---:|---:|
| 2 | 3 | 1 | 1 |
| 4 | 2 | 3 | 2 |
| 6 | 1 | 5 | 1 |

Total `4` — for instance $(1,1)$, $(1,3)$, $(2,2)$ and $(1,5)$.
