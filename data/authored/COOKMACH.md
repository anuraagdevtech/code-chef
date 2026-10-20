---
topic: Bit Manipulation
subtopic: Halving and doubling toward a power of two
time: $O(\log A \cdot \log B)$ per test case
space: $O(1)$
---
The two moves are "halve, rounding down" and "double". Doubling only scales, so it can never remove a factor that halving has not already stripped — which means any optimal route **halves for a while, then doubles**. Interleaving the two would undo work.

So walk the halving chain from $A$: $A, \lfloor A/2 \rfloor, \lfloor A/4 \rfloor, \ldots$, recording the cost to reach each value $v$. From $v$, doubling reaches $B$ only when $B = v \cdot 2^m$ for some $m \geq 0$ — and since $B$ is guaranteed to be a power of two, that requires $v$ to be a power of two as well, with $v \leq B$. The total cost is the halving steps plus $m$, and the answer is the minimum over the chain.

The chain has at most about $24$ entries for $A \leq 10^7$, so this is effectively constant time.

The sample cases show both shapes. $A = 4, B = 16$ doubles twice with no halving. $A = 4, B = 1$ halves twice with no doubling. $A = 3, B = 8$ needs both: $3$ is not a power of two, so it must be halved to $1$ (one step, losing the odd bit) and then doubled three times — four moves in all.

That odd case is the one to understand. Halving $3$ gives $1$, not $1.5$: the rounding **discards information**, which is why $3$ can never reach $8$ in fewer moves. Values must be reduced to a power of two before doubling can help.

The chain must stop before reaching $0$, since $1$ halves to $0$ and $0$ doubles to itself — a dead end, and $B \geq 1$ is never $0$.
