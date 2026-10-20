---
topic: Number Theory
subtopic: Which prime factors an operation can supply
time: $O(1)$ per test case
space: $O(1)$
---
Divisibility by $10$ means divisibility by both $2$ and $5$, since $10 = 2 \times 5$. Multiplying by $2$ can supply as many factors of $2$ as wanted — but it can **never** supply a factor of $5$.

So the factor of $5$ must already be present in $X$. That splits the problem into three cases:

- $X \equiv 0 \pmod{10}$ — already done, $0$ turns.
- $X \equiv 5 \pmod{10}$ — divisible by $5$ but odd. One multiplication makes it even, hence divisible by $10$: $1$ turn.
- otherwise — $X$ has no factor of $5$, and doubling never creates one: impossible, $-1$.

Thinking in terms of **which prime factors the operation can introduce** is the move that makes this immediate. Without it, one might search over numbers of doublings and never be sure when to give up.

Note that a single doubling always suffices in the second case; there is no input needing two or more. That is because any multiple of $5$ is either already even (so $\equiv 0 \bmod 10$) or becomes even after one doubling.

The edge case is $X = 0$, which the constraints admit. Zero is divisible by everything, including $10$, so `0 % 10 == 0` correctly yields $0$ turns with no special handling.

Sample case 3 ($X = 1$) is the impossible case, and case 2 ($X = 25$) the one-turn case giving $50$.
