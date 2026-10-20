---
topic: Number Theory
subtopic: An invariant from step size and parity
time: $O(1)$ per test case
space: $O(1)$
---
Both move **exactly** $K$ every second, so after $t$ seconds the policeman stands at $x + K p$ and the thief at $y + K q$, where $p$ and $q$ are sums of $t$ terms of $\pm 1$ — hence both have the **same parity as $t$**.

Meeting requires $x + Kp = y + Kq$, that is

$$x - y = K\,(q - p)$$

Two conditions fall out. First, $K$ must divide $x - y$. Second, $q - p$ is a difference of two integers of equal parity, so it is **even** — meaning $(x-y)/K$ must be even too.

Together:

$$K \mid (x - y) \quad\text{and}\quad \frac{x - y}{K} \text{ is even}$$

Both are invariants no evasion can break, so when either fails the answer is `No` regardless of play. When both hold, the policeman can close the gap and pin the thief against a wall, so the answer is `Yes`.

The parity half is the easily missed one, and the samples target it. Case 1 has adjacent positions with $K = 1$: the gap is $1$, odd, so they swap places forever and never coincide. Case 2 has a gap of $3$ with $K = 1$ — divisible, but odd — also `No`. Case 3 has a gap of $2$, even, giving `Yes`.

Cases 4 and 5 show the divisibility doing work: gaps of $4$ and $6$ against steps of $2$ and $3$ give quotients $2$ and $2$, both even.

Note the simultaneous-move rule means they can pass *through* each other without meeting, which is exactly what the parity obstruction encodes.
