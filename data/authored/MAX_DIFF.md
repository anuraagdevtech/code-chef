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

## Edge cases

- **$S$ larger than $N$** (the second and third rows): one dish is capped at $N$, so the other must take the remaining $S - N$ and the difference is $2N - S$ rather than $S$.
- **$S$ smaller than $N$** (the first row, $S = 1$ with $N = 3$): the whole sum fits in one dish, the other is $0$, and the difference is $S$ itself — which $2S - S$ gives.
- **The cap must be $\min(N, S)$.** Using $N$ alone makes the second tastiness negative when $S < N$; using $S$ alone breaks the per-dish ceiling when $S > N$.
- **$S = 2N$** (the second row, $N = S = 4$ gives $2 \cdot 4 - 4 = 4$; a true $S = 2N$ case like $N = 2, S = 4$) leaves both dishes full and the difference $0$.
- **Feasibility is guaranteed** — the statement promises some valid pair with $T_1 + T_2 = S$ — so $S \leq 2N$ and the formula never returns a negative number.
- **Tastiness may be $0$**, which is what makes the $S < N$ case work at all.

## Dry run

| $N$ | $S$ | $\min(N, S)$ | other dish | difference $2\min(N,S) - S$ |
|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 0 | `1` |
| 4 | 4 | 4 | 0 | `4` |
| 2 | 3 | 2 | 1 | `1` |

Row 3 is the capped case: the best split is $2 + 1$, not $3 + 0$, because no dish may exceed $N = 2$.
