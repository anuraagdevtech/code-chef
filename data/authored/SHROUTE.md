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

## Edge cases

- **Teleporting is free, so only the ride matters.** A traveller bound for city $B$ can take a right-moving train from any city $j \leq B$, arriving at time $B - j$, or a left-moving train from any $j \geq B$, arriving at $j - B$.
- **So the best choice is the nearest qualifying train on each side**, and the answer is the smaller of the two distances — which two prefix scans supply in constant time per query.
- **The direction must match the side.** A right-moving train beyond $B$ never arrives, and neither does a left-moving train before it — using the nearest train of *either* direction is the easy mistake.
- **No usable train at all** → $-1$ (the third sample's first query, where the only right-mover is past the destination and the only left-mover is before it).
- **A train originating at $B$ itself gives $0$**, which the inclusive bounds produce — the third sample's second query, with a left-moving train at city $1$ and destination $1$.
- **Teleportation happens at time $0$**, so all trains are still at their origins when the traveller boards.
- **Sum of $N$ and $M$ each up to $10^6$**, so the queries are answered from the two arrays with no per-query scan.

## Dry run

Second sample: $A = 1, 0, 0, 0, 2$ with the destination $B = 4$.

| option | source city | arrival time |
|---|---:|---:|
| nearest right-mover at or before $4$ | 1 | $4 - 1 = 3$ |
| nearest left-mover at or after $4$ | 5 | $5 - 4 = $ **1** |

Output `1` — teleport to city $5$ and ride the left-moving train one stop.
