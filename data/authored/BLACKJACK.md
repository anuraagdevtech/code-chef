---
topic: Basic Math
subtopic: Solving for the unknown, then range checking
time: $O(1)$ per test case
space: $O(1)$
---
The three drawn numbers must total $21$, so the required third card is forced:

$$C = 21 - A - B$$

There is nothing to search. The only question is whether that value is a card that can actually be drawn, which the problem fixes at $1 \leq C \leq 10$. If it falls outside, no draw can win and the answer is $-1$.

This two-step shape — **solve for the unknown, then validate it against the domain** — is worth naming, because the validation is where the problem actually lives. Computing $C$ is arithmetic; remembering that not every integer is a legal card is the part that is easy to skip.

Both ends of the range can fail in principle. With $A$ and $B$ each at most $10$ the sum is at most $20$, so $C \geq 1$ always holds and only the upper bound bites in practice. Sample case 2 shows it: $A = 1, B = 5$ needs a $15$, which no card can supply, so `-1`.

Sample case 1 sits exactly on the boundary at $C = 10$, which is legal — the check must be `<= 10`, not `< 10`.
