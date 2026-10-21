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

## Edge cases

- **Swaps beyond $\lfloor N/2 \rfloor$ add nothing**, since a full reversal already maximises the inversion count. The second row ($N = 1$) and the fourth ($N = 5$ with $K = 3$) both hit the clamp.
- **$N = 1$** → no swap is possible and the answer is $0$, which the clamp produces without a branch.
- **The outermost pair should be swapped first.** Positions $i$ and $N+1-i$ are the farthest apart still available, and swapping a pair at index distance $d$ creates $2d - 1$ inversions — so taking the largest $d$ first is greedily optimal.
- **The closed form is essential**, not a nicety: $K$ reaches $10^9$, so a loop over the swaps would time out even though each step is trivial.
- **Magnitudes**: $K(2N+1)$ with $K \leq 5 \cdot 10^8$ and $N \leq 10^9$ reaches about $10^{18}$ — inside 64-bit but close to its ceiling, and native in Python.
- **$K$ is at least $1$** by the constraints, so the clamp is the only route to a zero answer.

## Dry run

First sample: $N = 7$, $K = 3$, so three swaps on $1 \dots 7$.

| swap | positions | index distance $d$ | inversions gained $2d-1$ | running total |
|---:|---|---:|---:|---:|
| 1 | $1 \leftrightarrow 7$ | 6 | 11 | 11 |
| 2 | $2 \leftrightarrow 6$ | 4 | 7 | 18 |
| 3 | $3 \leftrightarrow 5$ | 2 | 3 | **21** |

The closed form gives $3(15) - 2 \cdot 3 \cdot 4 = 45 - 24 = $ `21`.
