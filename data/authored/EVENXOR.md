---
topic: Bit Manipulation
subtopic: Even-popcount numbers form a linear subspace
time: $O(N)$ per test case
space: $O(N)$
---
Popcount parity is **linear over XOR**:

$$\mathrm{popcount}(a \oplus b) \equiv \mathrm{popcount}(a) + \mathrm{popcount}(b) \pmod 2$$

because a bit position where $a$ and $b$ agree contributes $0$ or $2$ ones to the pair and $0$ to the XOR, while a position where they differ contributes $1$ to each side. So the even-popcount numbers are the **kernel** of a linear functional on $\mathbb{F}_2^{20}$ — a subspace of dimension $19$, closed under XOR.

That settles both directions. If every element has even popcount, every subset XOR does too, so the array is special. And conversely each singleton is a subset, so every element *must* have even popcount. The condition is therefore element-wise, with no subset enumeration anywhere.

The subspace has $2^{19} = 524288$ members, far more than the $N \leq 1000$ needed, so a simple indexing suffices:

$$A_k = 2k + \bigl(\mathrm{popcount}(k) \bmod 2\bigr), \qquad k = 1, \ldots, N$$

Doubling $k$ shifts its bits up without changing the popcount, and the low bit then repairs the parity, so $\mathrm{popcount}(A_k) = \mathrm{popcount}(k) + (\mathrm{popcount}(k) \bmod 2)$ is always even. Distinctness is immediate since $A_k \in \{2k, 2k+1\}$, and $A_k \leq 2N+1$ stays well inside $2^{20}$.

For $N = 2$ this gives `3 5` — matching the sample — because $k = 1$ needs the parity fix and $k = 2$ does too. For $N = 1$ we print `3` where the sample prints `6`; both have popcount $2$, and any special array is accepted.
