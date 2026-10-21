---
topic: Prefix Sums
subtopic: Nearest qualifying index from each side
time: $O(N + M)$ per test case
space: $O(N)$
---
Teleporting is free, so the traveller may board **any** train in the country. The only cost is the ride.

A right-moving train from city $i$ visits $i, i+1, i+2, \ldots$, reaching $B$ in $B - i$ minutes — and only if $i \leq B$. A left-moving train from $i$ reaches $B$ in $i - B$ minutes, and only if $i \geq B$.

To minimise the ride, take the **closest** usable train on each side:

- the largest $i \leq B$ with $A_i = 1$, costing $B - i$;
- the smallest $i \geq B$ with $A_i = 2$, costing $i - B$.

Take the better of the two, or $-1$ if neither exists.

Both are answered in $O(1)$ after two linear sweeps: one left-to-right carrying the most recent right-moving train, one right-to-left carrying the next left-moving train. With the sums of $N$ and $M$ reaching $10^6$, that linear preprocessing plus constant-time queries is what the problem's note about fast I/O is pointing at.

Note that a train **at** $B$ itself costs $0$ in either direction, which the formulas give naturally.

The samples cover each branch. Case 1 has only a right-mover at city $1$, so reaching city $5$ takes $4$ minutes. Case 2 adds a left-mover at city $5$, which reaches city $4$ in a single minute — far better than the $3$ the right-mover would need. Case 3 asks for city $3$, where the right-mover sits to its right and the left-mover to its left, so neither can help: $-1$. Its second query, city $1$, boards the left-mover already there for $0$.
