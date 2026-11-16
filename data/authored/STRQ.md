---
topic: Prefix Sums
subtopic: Prefix counts of ordered character pairs, corrected for starts before L
time: $O(16 \cdot N + Q)$
space: $O(N + Q)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a query $(a, b, L, R)$ with $a \ne b$ we need the pairs of positions $L \le s < e \le R$ with $P_s = a$ and $P_e = b$.

For a fixed character pair let `prefix[i]` be the number of such pairs with $e \le i$ and no lower bound on $s$; it grows by the number of $a$'s seen so far every time a $b$ is read. Then `prefix[R] - prefix[L-1]` counts pairs with $e \in [L, R]$ but still allows $s < L$. Those unwanted pairs are exactly (an $a$ before $L$) times (a $b$ inside $[L, R]$), so

$$\text{answer} = \text{prefix}[R] - \text{prefix}[L-1] - \text{cntA}[L-1] \cdot (\text{cntB}[R] - \text{cntB}[L-1]).$$

There are at most 12 useful pairs. Queries are grouped by pair and each pair's prefix array is built once, so memory stays linear even with a million queries.

## Edge cases

- The statement guarantees $a \ne b$; a character that never occurs in the string gives 0.
- Counts reach about $N^2 / 4$, beyond 32 bits - 64-bit arrays are used.
- Output is written in chunks to keep the peak memory bounded.
- $L$ is converted to a 0-based prefix index once, when the query is read.

## Dry run

`P = checfcheff`, query `c h 1 10`.

`c` occurs at positions 1, 4, 6 and `h` at 2, 7. Reading the string, the `h` at 2 has one `c` before it and the `h` at 7 has three, so `prefix[10] = 4`. With $L = 1$ nothing lies before the range, so the correction is 0.

Answer 4: `ch`, `checfch`, `cfch`, `ch`.
