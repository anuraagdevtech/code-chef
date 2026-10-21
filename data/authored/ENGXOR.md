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

## Edge cases

- **Popcount parity is additive under XOR.** The parity of $\mathrm{popcount}(P \oplus A_i)$ is $\mathrm{popcount}(P) \oplus \mathrm{popcount}(A_i)$ modulo $2$ — so an odd $P$ simply swaps the two tallies and an even $P$ leaves them alone.
- **That makes every query $O(1)$** after one pass over $A$: no per-query recomputation, which matters at $T(N+Q) \leq 4 \times 10^6$.
- **An even-popcount $P$ preserves the tallies** (the sample, where $P = 3$ has popcount $2$), so the output is $A$'s own counts.
- **An odd-popcount $P$ exchanges them**, and the two branches differ only in the order of the two numbers.
- **The output order is (even count, odd count)**, which the sample's `2 4` pins down.
- **$A_i \geq 1$ and $P \geq 1$**, so no zero with its popcount of $0$ needs special thought.
- **`int.bit_count()` is the exact popcount**, and masking with $1$ gives the parity directly.

## Dry run

Sample: $A = 4, 2, 15, 9, 8, 8$.

| value | popcount | parity |
|---:|---:|---|
| 4 | 1 | odd |
| 2 | 1 | odd |
| 15 | 4 | even |
| 9 | 2 | even |
| 8 | 1 | odd |
| 8 | 1 | odd |

Four odd, two even. Query $P = 3$ has popcount $2$, even, so the tallies carry over unchanged: output `2 4`.
