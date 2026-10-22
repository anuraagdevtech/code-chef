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

## Edge cases

- **Numbers with even popcount form a linear subspace under XOR**, because popcount parity is additive modulo $2$ — so if every element has even popcount, so does every subset XOR, and the "no bad subset" condition collapses to a per-element one.
- **Doubling preserves popcount**, so $2k$ has the same parity as $k$ — and adding the low bit when $k$ has odd popcount repairs it. That makes the construction a one-line map.
- **Distinctness is automatic**, since the $2k$ values differ by at least $2$ while the correction adds at most $1$.
- **The bound is comfortable**: the largest element is $2N + 1 \leq 2001$, far below $2^{20}$.
- **$k$ starts at $1$, not $0$**, which keeps every element positive and distinct.
- **The subspace argument is what rules out checking subsets.** With $N$ up to $1000$ there are $2^{1000}$ of them, so per-element parity is the only tractable handle.
- **This answer differs from the sample's** for $N = 1$ (`3` against `6`), and both are special — $3 = 11_2$ has popcount $2$ — so a special judge checks the conditions.

## Dry run

$N = 2$ gives the array $3, 5$.

| $k$ | $2k$ | popcount of $k$ | correction | element | popcount |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 1 (odd) | $+1$ | 3 | 2 |
| 2 | 4 | 1 (odd) | $+1$ | 5 | 2 |

Subsets: $\{3\} \to 3$ (popcount $2$), $\{5\} \to 5$ ($2$), $\{3,5\} \to 6$ ($2$). None is bad.
