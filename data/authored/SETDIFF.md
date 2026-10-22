---
topic: Combinatorics
subtopic: Counting how often each element is the extreme
time: $O(N \log N)$ per test case
space: $O(N)$
---
Summing $\max(s) - \min(s)$ over all $2^N$ subsets is hopeless directly, but the sum **splits**:

$$\mathrm{SETDIFF}(S) = \sum_{s} \max(s) \;-\; \sum_{s} \min(s)$$

and each half counts how often an element plays its role. Sort ascending as $a_0 \leq \cdots \leq a_{N-1}$ and fix the tie-break by index. Then $a_i$ is the maximum of a subset exactly when the subset contains $a_i$ and nothing after it — any combination of the $i$ earlier elements, so $2^i$ subsets. Symmetrically it is the minimum of $2^{N-1-i}$ subsets. Hence

$$\mathrm{SETDIFF}(S) = \sum_{i=0}^{N-1} a_i\,2^{i} \;-\; \sum_{i=0}^{N-1} a_i\,2^{N-1-i} \pmod{10^9+7}$$

Singletons contribute $0$ to each half and cancel, which is why they can be left in without a special case.

Fixing the tie-break by index is what makes repeated values correct: the problem counts subsets by *position*, so the two copies of $2$ in $\{1,2,2\}$ give two distinct subsets $\{1,2\}$, and ordering them by index assigns each its own exponent without double counting. That sample gives $13 - 10 = 3$.

The modular subtraction can go negative, so add the modulus before reducing.

The other samples check the formula: $\{1,2\}$ gives $(1 + 4) - (2 + 2) = 1$; $\{1,2,3\}$ gives $(1 + 4 + 12) - (4 + 4 + 3) = 6$; and $\{1,2,3,4\}$ gives $49 - 26 = 23$.

## Edge cases

- **Each element's contribution is counted by how often it is the extreme.** In sorted order, $a_i$ is the maximum of the $2^i$ subsets drawn from the smaller elements plus itself, and the minimum of $2^{n-1-i}$ — so the total is $\sum a_i (2^i - 2^{n-1-i})$ with no subset enumeration.
- **The two powers are maintained incrementally**, one doubling and one halving — the halving by multiplying by the modular inverse of $2$, since there is no integer division under a modulus.
- **The inverse of $2$ is $(p+1)/2$** for an odd prime modulus, which is exact and needs no `pow` call.
- **Duplicates are handled by position, not value.** Sorting breaks ties arbitrarily but consistently, so every subset is still counted exactly once — the fourth sample row has two $2$s and answers $3$.
- **Singleton subsets contribute $0$**, since the maximum and minimum coincide — which the formula gets right because the two counts cancel for them.
- **The subtraction can go negative before reduction**, so the final `% MOD` is needed to bring it back into range.
- **$N$ up to $10^5$** with values to $10^9$, so the sum must be taken modulo throughout rather than at the end.

## Dry run

Third sample: $S = \{1, 2, 3, 4\}$, so $n = 4$.

| $i$ | $a_i$ | times it is the max ($2^i$) | times it is the min ($2^{n-1-i}$) | contribution |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 8 | $-7$ |
| 1 | 2 | 2 | 4 | $-4$ |
| 2 | 3 | 4 | 2 | $+6$ |
| 3 | 4 | 8 | 1 | $+28$ |

Total `23`.
