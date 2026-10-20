---
topic: Combinatorics
subtopic: Maximising inversions with limited swaps
time: $O(1)$ per test case
space: $O(1)$
---
The pieces start sorted, so there are no inversions. The absolute maximum is the fully reversed order with $\binom{N}{2}$ inversions, and reversing takes $\lfloor N/2 \rfloor$ swaps — each one exchanging a symmetric pair $(i,\ N+1-i)$.

With only $K$ swaps, use $k = \min(K, \lfloor N/2 \rfloor)$ of them, and spend each on the **outermost remaining pair**, since the wider the swap the more inversions it creates. Exchanging positions $i$ and $N+1-i$ in an otherwise sorted array creates

$$2\,(N - 2i + 1) - 1$$

inversions: the two moved values now invert against each of the $N - 2i$ elements between them, twice over, plus the pair itself.

Summing over $i = 1 \ldots k$ collapses to a closed form:

$$k\,(2N + 1) - 2k(k+1)$$

which is essential — with $N$ and $K$ up to $10^9$ and $T$ up to $10^5$, no loop over swaps is affordable.

The clamp at $\lfloor N/2 \rfloor$ matters. Extra swaps beyond a full reversal cannot help, since $\binom{N}{2}$ is the ceiling. Sample case 1, $N = 7$ with $K = 3$, uses exactly $\lfloor 7/2 \rfloor = 3$ swaps and reaches the maximum $21$. Sample case 4 has $K = 3$ but only $\lfloor 5/2 \rfloor = 2$ useful swaps, giving $10$ rather than the full $\binom{5}{2} = 10$ — which happens to coincide, since two swaps already reverse a five-element array.

Sample case 2 is the degenerate one: a single piece admits no swaps at all, so the answer is $0$ despite $K = 4$.

The result reaches roughly $5 \times 10^{17}$, so this needs **64-bit arithmetic** outside Python.
