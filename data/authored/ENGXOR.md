---
topic: Bit Manipulation
subtopic: Popcount parity is additive under XOR
time: $O(N + Q)$ per test case
space: $O(1)$
---
The queries look independent — each $P$ builds a whole new sequence $B$ — but the quantity asked for is only the **parity** of the popcount, and parity behaves linearly under XOR:

$$\mathrm{popcount}(P \oplus A_i) \equiv \mathrm{popcount}(P) + \mathrm{popcount}(A_i) \pmod 2$$

(each bit position where $P$ and $A_i$ agree contributes $0$ or $2$ ones, both even; each position where they differ contributes exactly $1$ to both sides.)

So $B_i$ has odd popcount iff $\mathrm{popcount}(P)$ and $\mathrm{popcount}(A_i)$ have *different* parity. The entire array collapses to two numbers, $E$ and $O$ — how many $A_i$ have even and odd popcount — computed once:

- $\mathrm{popcount}(P)$ **even**: the parities are unchanged, so the answer is $(E, O)$.
- $\mathrm{popcount}(P)$ **odd**: every parity flips, so the answer is $(O, E)$.

Each query is then $O(1)$, which is what makes $T \cdot (N + Q) \leq 4 \times 10^6$ tractable. Precomputing a popcount table over $P \leq 10^5$ is unnecessary — a single `bit_count()` per query suffices.

In the sample, $A = [4, 2, 15, 9, 8, 8]$ has popcounts $1, 1, 4, 2, 1, 1$, so $E = 2$ and $O = 4$. The query $P = 3$ has popcount $2$, which is even, so the answer is `2 4` unchanged. Had $P$ been $1$, the same precomputation would immediately give `4 2`.

The statement's own warning about large I/O is the real difficulty: read the whole stream at once and join the output rather than printing per query.
