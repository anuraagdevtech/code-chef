---
topic: Bit Manipulation
subtopic: Bits are independent, so count per column
time: $O(N \log \max A)$ per test case
space: $O(1)$
---
An operation picks a **single** bit position $p$ and flips it in at most $K$ chosen elements. Since it never touches any other bit, the $30$ bit positions are **completely independent problems** — the work for bit $p$ cannot help bit $q$.

For bit $p$, let $c_p$ be how many elements currently have it set. Every one of those must be flipped, and each operation flips at most $K$ of them, so bit $p$ needs exactly

$$\left\lceil \frac{c_p}{K} \right\rceil$$

operations — the bound is tight because the chosen indices are free, so every operation can flip a full $K$ until the last.

Summing over the bits gives the answer:

$$\sum_{p} \left\lceil \frac{c_p}{K} \right\rceil$$

Separating a problem by bit position is the standard move whenever the operation is XOR with a power of two, and here it turns an apparently tangled search into $30$ independent counting problems.

Working the sample, $A = [3, 6, 10]$ with $K = 2$: in binary $0011$, $0110$, $1010$. The column counts are $1, 3, 1, 1$ for bits $0$ through $3$, giving $1 + 2 + 1 + 1 = 5$.

Note bit $1$ is the only column needing two operations — three elements at two per operation. Bits set in a single element still cost one operation each, which is why the total exceeds the largest column count.

Counting columns is one pass over the array per bit, or equivalently one pass accumulating all $30$ counters at once.
