---
topic: Game Theory
subtopic: Largest free run against the runner-up
time: $O(N)$ per test case
space: $O(1)$
---
The blocked ends split the strip into maximal runs of free cells, and because a player's second and later moves must be to an adjacent cell, each player stays inside the run she entered and walks in one direction until stuck.

Suppose Nayeon enters a run of length $L$ with $a$ free cells to her left and $b$ to her right ($a + b = L - 1$). Tzuyu has two replies:

- **Contest the same run.** She steps in next to Nayeon on the larger side, so Nayeon can only walk the smaller side, making $1 + \min(a,b)$ moves while Tzuyu makes $\max(a,b)$. Nayeon needs $1 + \min > \max$, which is possible only with $a = b$, i.e. **$L$ odd**, taking the exact middle.
- **Take another run.** Entering a run of length $L'$ at its end gives her $L'$ moves, while Nayeon, unopposed from the middle, makes $1 + \frac{L-1}{2} = \frac{L+1}{2}$.

Since Nayeon commits her cell first, she must survive both replies, so her run must be odd *and* satisfy $\frac{L+1}{2} > L'$ for every other run. Only the longest run can qualify — any shorter one is beaten by the longest. With $M$ the largest run length and $M_2$ the second largest ($0$ if there is only one run):

$$\text{Nayeon wins} \iff M \text{ odd and } \frac{M+1}{2} > M_2$$

This matches an exhaustive search over all strips up to length $12$. Note how sharp it is: $[1,3]$ wins but $[2,3]$ loses, and $[2,5]$ wins but $[3,5]$ loses — a runner-up of exactly $\frac{M+1}{2}$ is enough for Tzuyu to draw level, and level means Nayeon runs out first.

The samples: one run of $3$ wins; runs $\{1,2\}$ lose on parity; a single cell wins trivially since Tzuyu has nowhere to go; and a fully blocked strip loses at once.
