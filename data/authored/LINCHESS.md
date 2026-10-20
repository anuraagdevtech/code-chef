---
topic: Number Theory
subtopic: Divisors as reachable positions
time: $O(N)$ per test case
space: $O(1)$
---
Player $i$ places a pawn on square $P_i$ and then advances by $P_i$ each move, so the squares they ever occupy are

$$P_i,\ 2P_i,\ 3P_i,\ \ldots$$

— exactly the positive multiples of $P_i$. So that player can reach Chef's square $K$ **if and only if $P_i$ divides $K$**.

When it does, reaching $K$ takes $\frac{K}{P_i} - 1$ moves, since the pawn starts already placed on $P_i$. That count shrinks as $P_i$ grows, so among the divisors of $K$ present in the list, the **largest** one wins. If none divides $K$, the answer is $-1$.

Recasting "can this player reach that square" as a divisibility test is the whole problem; without it one might try to simulate the moves, which is hopeless with $K$ up to $10^9$.

The output is the **starting square** $P_i$, not the number of moves — easy to misread, since the question is phrased around move counts.

Sample case 1 has $K = 6$ with candidates $\{4,3,2,8\}$. Both $3$ and $2$ divide $6$, needing $1$ and $2$ moves respectively, so the larger divisor $3$ is reported. Sample case 2 has $K = 7$, a prime, and none of $\{4,3,2,8\}$ divides it — note that $7$ itself does not appear, and the guarantee that all values are pairwise distinct means $P_i = K$ never happens anyway.

A single pass over the list suffices; no factorisation of $K$ is required, since the candidates are given.
