---
topic: Greedy
subtopic: Pushing one variable to its bound
time: $O(1)$ per test case
space: $O(1)$
---
With $T_1 + T_2 = S$ fixed, the difference is

$$|T_1 - T_2| = |2T_1 - S|$$

so maximising it means pushing $T_1$ as far from $S/2$ as possible. Both variables are capped at $N$ and floored at $0$, so the extreme choice is

$$T_1 = \min(N, S)$$

— take everything, unless the cap or the sum itself stops you. The partner is then $T_2 = S - T_1$, and the difference is

$$2\min(N, S) - S$$

Both terms of the `min` are needed. When $S \leq N$ the sum is the binding limit: one dish takes all $S$ and the other takes $0$, giving a difference of $S$. Sample case 2 ($N=4, S=4$) is this, answering $4$. When $S > N$ the cap binds: one dish maxes at $N$ and the other absorbs $S - N$. Sample case 3 ($N=2, S=3$) gives $2 \cdot 2 - 3 = 1$.

The guarantee that some valid pair exists means $S \leq 2N$, so $T_2 = S - \min(N,S)$ never exceeds $N$ and the construction is always legal — no feasibility check is needed.

The answer also carries a parity fact worth noticing: $2\min(N,S) - S$ has the same parity as $S$, which is forced, since $T_1 - T_2$ and $T_1 + T_2$ always share a parity. Sample case 1, with odd $S = 1$, correctly gives the odd answer $1$ rather than $0$.
