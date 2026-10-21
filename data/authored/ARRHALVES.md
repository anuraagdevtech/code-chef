---
topic: Arrays
subtopic: Minimum adjacent swaps to gather a set
time: $O(N)$ per test case
space: $O(N)$
---
Since $P$ is a permutation of $1 \ldots 2N$, "max of the first half below min of the second half" can only mean the first half holds exactly $\{1, \ldots, N\}$ and the second holds $\{N+1, \ldots, 2N\}$. **Their order within each half is irrelevant.**

So the task is: move the $N$ small values into the first $N$ positions, using adjacent swaps, as cheaply as possible.

The classic result applies. If the small values currently sit at positions $p_1 < p_2 < \cdots < p_N$ (zero-indexed), the minimum number of adjacent swaps to gather them into the first $N$ slots is

$$\sum_{i=0}^{N-1} (p_i - i)$$

The reasoning: the relative order of the small values never needs to change — swapping two of them is wasted work — so the $i$-th small value from the left is destined for slot $i$, and each must step past exactly the large values standing before it. The sum counts precisely those crossings.

That subtraction of $i$ is what prevents double-counting. Summing the raw positions would also charge each small value for the small values ahead of it, which it never has to cross.

Sample case 3 is the worst case: $[6,5,4,3,2,1]$ has its small values at positions $3,4,5$, giving $(3-0)+(4-1)+(5-2) = 9$. Sample case 2 is already good at $0$ cost. Sample case 1, $[3,2,1,4]$ with $N=2$, has small values at $1$ and $2$, giving $1 + 1 = 2$ — note the result is already good without sorting either half.

The answer can reach about $N^2 \approx 10^{10}$, which **overflows 32 bits** — Python is fine, but a C solution needs a 64-bit accumulator.

## Edge cases

- **The first half must hold exactly $1 \dots N$** — not merely be separated from the second. The third row, $6,5,4,3,2,1$, already has the small values grouped in the *second* half, yet the answer is $9$, because they must be moved to the front.
- **Only which half a value lands in matters**, not its order within that half, so the cost is the number of cross-class inversions rather than a full sort.
- **Already good** (the second row) → $0$.
- **Fully reversed** (the third row) → the maximum, $N^2 = 9$.
- **The target pointer advances only when a small value is placed**, so each small value is charged exactly the number of large values preceding it — which is the minimum, since adjacent swaps can fix one such inversion at a time.
- **$P$ is a permutation of $1 \dots 2N$**, so exactly $N$ values are at most $N$ and the pointer ends at $N$.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass, with the threshold test done on converted integers since byte comparison would order `10` before `9`.

## Dry run

First sample: $N = 2$, $P = 3, 2, 1, 4$. Small values are $1$ and $2$.

| index | value | small? | target slot | cost added |
|---:|---:|:---:|---:|---:|
| 0 | 3 | no | 0 | — |
| 1 | 2 | yes | 0 | $1 - 0 = 1$ |
| 2 | 1 | yes | 1 | $2 - 1 = 1$ |
| 3 | 4 | no | 2 | — |

Total `2`: swap $3$ with $2$, then $3$ with $1$, giving $2,1,3,4$.
