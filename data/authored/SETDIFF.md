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
